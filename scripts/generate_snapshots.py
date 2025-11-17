#!/usr/bin/env python3


#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import argparse
import json
import shutil
import sys
import warnings
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path.cwd()))  # Make holidays visible.
from holidays import (
    country_holidays,
    financial_holidays,
    list_supported_countries,
    list_supported_financial,
)


class SnapshotGenerator:
    """Creates a snapshot of available holidays for supported entities."""

    years = range(1950, 2051)

    def __init__(self) -> None:
        arg_parser = argparse.ArgumentParser()
        entities_group = arg_parser.add_mutually_exclusive_group()
        entities_group.add_argument(
            "-c",
            "--country",
            action="extend",
            nargs="+",
            default=[],
            help="Country codes to use for snapshot generation",
            type=str,
        )
        entities_group.add_argument(
            "-m",
            "--market",
            action="extend",
            nargs="+",
            default=[],
            help="Market codes to use for snapshot generation",
            type=str,
        )
        self.args = arg_parser.parse_args()

    @staticmethod
    def prepare_snapshot_directory(snapshot_path: Path) -> None:
        """Prepare a directory for snapshots."""
        shutil.rmtree(snapshot_path, ignore_errors=True)
        snapshot_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def save(snapshot: dict, file_path: Path) -> None:
        """Save snapshot to a JSON file."""
        file_path.write_text(
            json.dumps(
                {str(dt): name for dt, name in sorted(snapshot.items())},
                ensure_ascii=False,
                indent=4,
            )
            + "\n",  # Get along with pre-commit.
            encoding="utf-8",
            newline="\n",
        )

    @staticmethod
    def _country_subdiv_snapshot_worker(
        args: tuple[str, str | None, tuple[str, ...], range, Path],
    ) -> None:
        """Worker for generating country holiday snapshots."""
        country_code, subdiv, supported_categories, years, snapshot_path = args
        filename = f"{country_code}_{(subdiv or 'COMMON').replace(' ', '_').upper()}.json"
        file_path = snapshot_path / filename
        snapshot = country_holidays(
            country_code,
            subdiv=subdiv,
            years=years,
            categories=supported_categories,
            language="en_US",
        )
        SnapshotGenerator.save(snapshot, file_path)

    @staticmethod
    def _financial_snapshot_worker(args: tuple[str, range, Path]) -> None:
        """Worker for generating financial market holiday snapshots."""
        market_code, years, snapshot_path = args
        file_path = snapshot_path / f"{market_code}.json"
        snapshot = financial_holidays(
            market_code,
            years=years,
            language="en_US",
        )
        SnapshotGenerator.save(snapshot, file_path)

    def generate_country_snapshots(self) -> None:
        """Generates country snapshots."""
        if self.args.market:
            return None

        supported_countries = list_supported_countries(include_aliases=False)
        country_list = self.args.country or list(supported_countries.keys())
        if unknown_countries := set(country_list).difference(supported_countries.keys()):
            raise ValueError(f"Countries {', '.join(unknown_countries)} not available")

        snapshot_path = Path("snapshots/countries")
        if not self.args.country:
            self.prepare_snapshot_directory(snapshot_path)

        work_items: list[tuple[str, str | None, tuple[str, ...], range, Path]] = []
        for country_code in country_list:
            country = country_holidays(country_code)
            for subdiv in (None, *country.subdivisions):
                work_items.append(
                    (country_code, subdiv, country.supported_categories, self.years, snapshot_path)
                )
        with ProcessPoolExecutor() as executor:
            list(executor.map(SnapshotGenerator._country_subdiv_snapshot_worker, work_items))

    def generate_financial_snapshots(self) -> None:
        """Generates financial snapshots."""
        if self.args.country:
            return None

        supported_markets = list_supported_financial(include_aliases=False)
        market_list = self.args.market or list(supported_markets.keys())
        if unknown_markets := set(market_list).difference(supported_markets.keys()):
            raise ValueError(f"Markets {', '.join(unknown_markets)} not available")

        snapshot_path = Path("snapshots/financial")
        if not self.args.market:
            self.prepare_snapshot_directory(snapshot_path)

        work_items: list[tuple[str, range, Path]] = []
        for market_code in market_list:
            work_items.append((market_code, self.years, snapshot_path))
        with ProcessPoolExecutor() as executor:
            list(executor.map(SnapshotGenerator._financial_snapshot_worker, work_items))

    def run(self):
        """Runs snapshot files generation process."""
        self.generate_country_snapshots()
        self.generate_financial_snapshots()


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    total_time_start = perf_counter()
    SnapshotGenerator().run()
    total_time_end = perf_counter()
    print(f"[TIMER] Total snapshot runtime: {total_time_end - total_time_start:.2f} seconds")
