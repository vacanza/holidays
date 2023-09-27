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

# flake8: noqa: F402

import argparse
import json
import sys
import warnings
from pathlib import Path

sys.path.append(f"{Path.cwd()}")  # Make holidays visible.

import holidays
from holidays import HOLIDAY_NAME_DELIMITER, list_supported_countries, list_supported_financial


class SnapshotGenerator:
    """Creates a snapshot of available holidays for supported entities."""

    years = range(1950, 2051)

    def __init__(self) -> None:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument(
            "-c",
            "--countries",
            action="extend",
            nargs="+",
            default=[],
            help="Countries to generate",
            required=False,
            type=str,
        )
        arg_parser.add_argument(
            "-m",
            "--markets",
            action="extend",
            nargs="+",
            default=[],
            help="Markets to generate",
            required=False,
            type=str,
        )
        self.args = arg_parser.parse_args()

    @staticmethod
    def save(snapshot, file_path):
        with open(file_path, "w") as output:
            output.write(
                json.dumps({str(dt): name for dt, name in sorted(snapshot.items())}, indent=4)
            )
            output.write("\n")  # Get along with pre-commit.

    @staticmethod
    def update_snapshot(snapshot, data):
        for dt, name in data.items():
            holiday_names = set(
                snapshot[dt].split(HOLIDAY_NAME_DELIMITER) if dt in snapshot else ()
            )
            holiday_names.update(name.split(HOLIDAY_NAME_DELIMITER))
            snapshot[dt] = HOLIDAY_NAME_DELIMITER.join(sorted(holiday_names))

    def generate_country_snapshots(self):
        """Generates country snapshots."""
        if len(self.args.markets) > 0:
            return None
        country_list = self.args.countries or list_supported_countries()
        for country_code in country_list:
            country = getattr(holidays, country_code)
            snapshot = {}

            for subdiv in (None,) + country.subdivisions:
                self.update_snapshot(
                    snapshot,
                    holidays.country_holidays(
                        country_code,
                        subdiv=subdiv,
                        years=self.years,
                        categories=country.supported_categories,
                        language="en_US",
                    ),
                )
            self.save(snapshot, f"snapshots/countries/{country_code}.json")

    def generate_financial_snapshots(self):
        """Generates financial snapshots."""
        if len(self.args.countries) > 0:
            return None
        market_list = self.args.markets or list_supported_financial()
        for market_code in market_list:
            self.save(
                holidays.country_holidays(
                    market_code,
                    years=self.years,
                    language="en_US",
                ),
                f"snapshots/financial/{market_code}.json",
            )

    def run(self):
        """Runs snapshot files generation process."""
        self.generate_country_snapshots()
        self.generate_financial_snapshots()


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    SnapshotGenerator().run()
