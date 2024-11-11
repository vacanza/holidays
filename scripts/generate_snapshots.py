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
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import argparse
import json
import shutil
import sys
import warnings
from pathlib import Path

sys.path.append(f"{Path.cwd()}")  # Make holidays visible.

import holidays  # noqa: E402
from holidays import list_supported_countries, list_supported_financial  # noqa: E402


class SnapshotGenerator:
    """Creates a snapshot of available holidays for supported entities."""

    years = range(1950, 2051)

    def __init__(self) -> None:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument(
            "-c",
            "--country",
            action="extend",
            nargs="+",
            default=[],
            help="Country codes to use for snapshot generation",
            required=False,
            type=str,
        )
        arg_parser.add_argument(
            "-m",
            "--market",
            action="extend",
            nargs="+",
            default=[],
            help="Market codes to use for snapshot generation",
            required=False,
            type=str,
        )
        self.args = arg_parser.parse_args()

    @staticmethod
    def prepare_snapshot_directory(snapshot_path):
        """Prepare a directory for snapshots."""
        path = Path(snapshot_path)
        shutil.rmtree(path, ignore_errors=True)
        path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def save(snapshot, file_path):
        with open(file_path, "w") as output:
            output.write(
                json.dumps({str(dt): name for dt, name in sorted(snapshot.items())}, indent=4)
            )
            output.write("\n")  # Get along with pre-commit.

    def generate_country_snapshots(self):
        """Generates country snapshots."""
        if self.args.market:
            return None

        supported_countries = list_supported_countries(include_aliases=False)
        country_list = self.args.country or supported_countries
        if unknown_countries := set(country_list).difference(supported_countries.keys()):
            raise ValueError(f"Countries {', '.join(unknown_countries)} not available")

        snapshot_path = "snapshots/countries"
        if not self.args.country:
            self.prepare_snapshot_directory(snapshot_path)
        for country_code in country_list:
            country = getattr(holidays, country_code)

            for subdiv in (None,) + country.subdivisions:
                self.save(
                    holidays.country_holidays(
                        country_code,
                        subdiv=subdiv,
                        years=self.years,
                        categories=country.supported_categories,
                        language="en_US",
                    ),
                    f"{snapshot_path}/"
                    f"{country_code}_{(subdiv or 'COMMON').replace(' ', '_').upper()}.json",
                )

    def generate_financial_snapshots(self):
        """Generates financial snapshots."""
        if self.args.country:
            return None

        supported_markets = list_supported_financial(include_aliases=False)
        market_list = self.args.market or supported_markets
        if unknown_markets := set(market_list).difference(supported_markets.keys()):
            raise ValueError(f"Markets {', '.join(unknown_markets)} not available")

        snapshot_path = "snapshots/financial"
        if not self.args.market:
            self.prepare_snapshot_directory(snapshot_path)
        for market_code in market_list:
            self.save(
                holidays.country_holidays(
                    market_code,
                    years=self.years,
                    language="en_US",
                ),
                f"{snapshot_path}/{market_code}.json",
            )

    def run(self):
        """Runs snapshot files generation process."""
        self.generate_country_snapshots()
        self.generate_financial_snapshots()


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    SnapshotGenerator().run()
