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
import json
import sys
import warnings
from pathlib import Path

sys.path.append(f"{Path.cwd()}")  # Make holidays visible.

import holidays  # noqa: E402
from holidays import list_iso_3166_entities, list_iso_10383_entities  # noqa: E402


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
    def save(snapshot, file_path):
        with open(file_path, "w") as output:
            output.write(
                json.dumps({str(dt): name for dt, name in sorted(snapshot.items())}, indent=4)
            )
            output.write("\n")  # Get along with pre-commit.

    def generate_iso3166_snapshots(self):
        """Generates country snapshots."""
        if len(self.args.market) > 0:
            return None

        country_list = self.args.country
        supported_countries = list_iso_3166_entities()
        if country_list:
            unknown_countries = set(country_list).difference(supported_countries.keys())
            if len(unknown_countries) > 0:
                raise ValueError(f"Countries {', '.join(unknown_countries)} not available")
        else:
            country_list = supported_countries

        for country_code in country_list:
            country = getattr(holidays, country_code)

            for subdiv in (None,) + country.subdivisions:
                self.save(
                    holidays.iso_3166_holidays(
                        country_code,
                        subdiv=subdiv,
                        years=self.years,
                        categories=country.supported_categories,
                        language="en_US",
                    ),
                    f"snapshots/ISO_3166/{country_code}_{subdiv or 'COMMON'}.json",
                )

    def generate_iso_10383_snapshots(self):
        """Generates financial snapshots."""
        if len(self.args.country) > 0:
            return None

        market_list = self.args.market
        supported_markets = list_iso_10383_entities()
        if market_list:
            unknown_markets = set(market_list).difference(supported_markets.keys())
            if len(unknown_markets) > 0:
                raise ValueError(f"Markets {', '.join(unknown_markets)} not available")
        else:
            market_list = supported_markets

        for market_code in market_list:
            self.save(
                holidays.iso_3166_holidays(
                    market_code,
                    years=self.years,
                    language="en_US",
                ),
                f"snapshots/ISO_10383/{market_code}.json",
            )

    def run(self):
        """Runs snapshot files generation process."""
        self.generate_iso3166_snapshots()
        self.generate_iso_10383_snapshots()


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    SnapshotGenerator().run()
