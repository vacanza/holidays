#!/usr/bin/env python3

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Dict, Set

from git import Repo
from github import Github
from github.GithubException import UnknownObjectException

sys.path.append(f"{Path.cwd()}")
import holidays  # noqa: E402

BRANCH_NAME = "dev"
HEADER_TEMPLATE = """
Version {version}
============

Released {month} {day}, {year}
"""
IGNORED_CONTRIBUTORS = {"dependabot[bot]", "github-actions[bot]"}
REPOSITORY_NAME = "vacanza/python-holidays"


class ReleaseNotesGenerator:
    """
    Generates release notes based on local git commits and GitHub PRs metadata.

    Usage example: scripts/generate_release_notes.py
    """

    def __init__(self) -> None:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument(
            "-a",
            "--author-only",
            action="extend",
            default=[],
            help="Add only author as a contributor for this PR",
            nargs="+",
            type=int,
        )
        arg_parser.add_argument(
            "-c",
            "--cut-off-at",
            help="Cut off at PR",
            required=False,
            type=int,
        )
        arg_parser.add_argument(
            "-e",
            "--exclude",
            action="extend",
            default=[],
            help="Exclude this PR from the release notes",
            nargs="+",
            type=int,
        )
        arg_parser.add_argument(
            "-v",
            "--verbose",
            action="store_true",
            default=False,
            help="Verbose output",
        )
        self.args = arg_parser.parse_args()

        self.local_repo = Repo(Path.cwd())
        self.remote_repo = Github(self.github_token).get_repo(REPOSITORY_NAME)

        self.previous_commits: Set[str] = set()
        self.pull_requests: Dict[int, str] = {}

        self.tag = holidays.__version__

        try:
            latest_tag = self.remote_repo.get_tags()[0]
            self.latest_tag_name = latest_tag.name
            self.previous_commits.add(latest_tag.commit.sha)
        except IndexError:
            self.latest_tag_name = None

    @property
    def github_token(self, path=Path(".github_token")):
        """Return GitHub access token."""
        return path.read_text(encoding="UTF-8").strip()

    @property
    def is_ready(self):
        """Perform environment checks and input validation."""
        current_branch = str(self.local_repo.active_branch)
        if current_branch != BRANCH_NAME:
            exit(
                f"Switch to '{BRANCH_NAME}' first (currently in "
                f"'{current_branch}'). Use 'git switch {BRANCH_NAME}'."
            )

        return True

    @property
    def sorted_pull_requests(self):
        def custom_order(pr):
            if re.findall(r"^(Introduce|Refactor)", pr[0]) or re.findall(r"Add .* support", pr[0]):
                weight = 10
            elif re.findall(r"^Add .* holidays$", pr[0]):
                weight = 20
            elif re.findall(r"(^Localize)|(localization$)", pr[0]):
                weight = 30
            elif re.findall(r"^Fix", pr[0]):
                weight = 40
            elif re.findall(r"^(Change|Improve|Optimize|Update|Upgrade)", pr[0]):
                weight = 50
            else:
                weight = 100

            return weight, pr

        return sorted(self.pull_requests.values(), key=custom_order)

    def add_pull_request(self, pull_request):
        """Add pull request information to the release notes dict."""
        author = pull_request.user.login if pull_request.user else None
        if author in IGNORED_CONTRIBUTORS:
            print((f"Skipping #{pull_request.number} {pull_request.title}" f" by {author}"))
            return None

        # Skip failed release attempt PRs, version upgrades.
        pr_title = pull_request.title
        skip_titles = (f"v.{self.tag}", "Bump", "Revert")
        for skip_title in skip_titles:
            if pr_title.startswith(skip_title):
                return None

        # Get contributors (expand from commits by default).
        contributors = set()
        if pull_request.number not in self.args.author_only:
            for commit in pull_request.get_commits():
                if commit.author:
                    contributors.add(commit.author.login)

        if author in contributors:
            contributors.remove(author)
        contributors = (f"@{c}" for c in [author] + sorted(contributors, key=str.lower))
        self.pull_requests[pull_request.number] = (
            pull_request.title,
            f"#{pull_request.number} by {', '.join(contributors)}",
        )

    def generate_release_notes(self):
        """Generate release notes contents."""
        print("Processing pull requests...")
        self.get_new_pull_requests()
        self.get_old_pull_requests()
        print("Done!")

    def get_new_pull_requests(self):
        """Get PRs created after the latest release.

        This operation also populates a set of previous release commits.
        """
        cut_off_at = self.args.cut_off_at
        excluded_pr_numbers = set(self.args.exclude)
        for pull_request in self.remote_repo.get_pulls(state="closed"):
            # Stop getting pull requests after previous release tag or specific PR number.
            cut_off = cut_off_at and pull_request.number == cut_off_at
            if cut_off or pull_request.title == self.latest_tag_name:
                # Get previous release commits SHAs.
                for commit in pull_request.get_commits():
                    self.previous_commits.add(commit.sha)
                break

            # Skip closed unmerged PRs.
            if not pull_request.merged:
                continue

            if pull_request.number in excluded_pr_numbers:
                if self.args.verbose:
                    print(f"Excluding PR #{pull_request.number} as requested")
                continue

            if self.args.verbose:
                messages = [f"Fetching PR #{pull_request.number}"]
                if pull_request.number in self.args.author_only:
                    messages.append("(keeping PR author as a sole contributor)")
                print(" ".join(messages))

            self.add_pull_request(pull_request)

    def get_old_pull_requests(self):
        """Get PRs created before the latest release."""
        pull_request_numbers = set()
        for commit in self.local_repo.iter_commits():
            if commit.hexsha in self.previous_commits:
                break

            try:
                pull_request_number = re.findall(
                    r"#(\d{3,})",
                    commit.message,
                )[0]
                pull_request_numbers.add(int(pull_request_number))
            except IndexError:
                continue

        # Fetch old PRs metadata only. Skip all known PRs.
        pull_request_numbers -= set(self.pull_requests.keys())
        pull_request_numbers -= set(self.args.exclude)
        for pull_request_number in pull_request_numbers:
            if self.args.verbose:
                messages = [f"Fetching PR #{pull_request_number}"]
                if pull_request_number in self.args.author_only:
                    messages.append("(keeping PR author as a sole contributor)")
                print(" ".join(messages))

            try:
                self.add_pull_request(self.remote_repo.get_pull(pull_request_number))
            # 3rd party contributions to forks.
            except UnknownObjectException:
                pass

    def print_release_notes(self):
        """Print generated release notes."""
        print("")
        if self.pull_requests:
            today = date.today()
            print(
                HEADER_TEMPLATE.format(
                    day=today.day,
                    month=today.strftime("%B"),
                    version=self.tag,
                    year=today.year,
                )
            )
            print("\n".join((f"- {pr[0]} ({pr[1]})" for pr in self.sorted_pull_requests)))

        else:
            print(f"No changes since {self.latest_tag_name} release.")


if __name__ == "__main__":
    rng = ReleaseNotesGenerator()
    if rng.is_ready:
        rng.generate_release_notes()
        rng.print_release_notes()
