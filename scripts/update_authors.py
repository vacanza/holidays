#!/usr/bin/env python3

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from pathlib import Path

from git import Repo

HEADER_TEMPLATE = """Python Holidays Authors
=======================

{authors}
"""
OUTPUT_FILENAME = "AUTHORS"
PROJECT_DIR = Path(__file__).parent.parent
REPOSITORY_NAME = "vacanza/python-holidays"


class AuthorsGenerator:
    """
    Generates authors based on the commits metadata.

    Usage example: scripts/update_authors.py
    """

    @staticmethod
    def run():
        """Update authors list."""
        authors = set()
        for commit in Repo(PROJECT_DIR).iter_commits():
            names = set((ca.name for ca in commit.co_authors))
            names.add(commit.author.name)
            for name in names:
                # Add meaningful names only.
                if " " not in name:
                    continue

                tokens = name.split()
                # Capitalize first name and last name.
                for idx in (0, -1):
                    tokens[idx] = tokens[idx].capitalize()
                authors.add(" ".join(tokens))

        with open(PROJECT_DIR / OUTPUT_FILENAME, "w") as output_file:
            output_file.write(HEADER_TEMPLATE.format(authors="\n".join(sorted(authors))))


if __name__ == "__main__":
    AuthorsGenerator.run()
