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
            if dt in snapshot:
                existing_names = set(snapshot[dt].split(HOLIDAY_NAME_DELIMITER))
                existing_names.update(name.split(HOLIDAY_NAME_DELIMITER))
                name = HOLIDAY_NAME_DELIMITER.join(sorted(existing_names))

            snapshot[dt] = name

    def generate_country_snapshots(self):
        """Generates country snapshots."""
        for country_code in list_supported_countries():
            country = getattr(holidays, country_code)
            snapshot = holidays.country_holidays(
                country_code,
                years=self.years,
                categories=country.supported_categories,
                language="en_US",
            )
            for subdiv in country.subdivisions:
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
        for market_code in list_supported_financial():
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
