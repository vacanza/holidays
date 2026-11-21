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

ENTITIES = (
    ("country", "Countries", list_supported_countries, country_holidays, "snapshots/countries"),
    ("market", "Markets", list_supported_financial, financial_holidays, "snapshots/financial"),
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
    def _snapshot_worker(args: tuple) -> None:
        """Worker for generating a single country/market holiday snapshot."""
        warnings.simplefilter("ignore")
        factory, code, subdiv, supported_categories, snapshot_path = args
        snapshot = factory(
            code,
            subdiv=subdiv,
            years=SnapshotGenerator.years,
            categories=supported_categories,
            language="en_US",
        )
        filename = f"{code}_{(subdiv or 'COMMON').replace(' ', '_').upper()}.json"
        SnapshotGenerator.save(snapshot, snapshot_path / filename)

    def run(self) -> None:
        """Runs snapshot files generation process."""
        work_items: list[tuple] = []
        snapshot_paths: list[Path] = []
        reset_paths: list[Path] = []

        for entity_type, label, list_supported, factory, directory in ENTITIES:
            requested = getattr(self.args, entity_type)
            if not requested and (self.args.country or self.args.market):
                continue

            supported = list_supported(include_aliases=False)
            codes = requested or list(supported)
            if unknown := set(codes).difference(supported):
                raise ValueError(f"{label} {', '.join(unknown)} not available")

            snapshot_path = Path(directory)
            snapshot_paths.append(snapshot_path)
            if not requested:
                reset_paths.append(snapshot_path)

            for code in codes:
                entity = factory(code)
                work_items.extend(
                    (factory, code, subdiv, entity.supported_categories, snapshot_path)
                    for subdiv in (None, *entity.subdivisions)
                )

        for snapshot_path in reset_paths:
            shutil.rmtree(snapshot_path, ignore_errors=True)
        for snapshot_path in snapshot_paths:
            snapshot_path.mkdir(parents=True, exist_ok=True)

        with ProcessPoolExecutor() as executor:
            list(executor.map(self._snapshot_worker, work_items))


if __name__ == "__main__":
    total_time_start = perf_counter()
    SnapshotGenerator().run()
    total_time_end = perf_counter()
    print(f"[TIMER] Total snapshot runtime: {total_time_end - total_time_start:.2f} seconds")
