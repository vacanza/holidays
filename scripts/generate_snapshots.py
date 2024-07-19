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
from holidays import (  # noqa: E402
    iso_3166_holidays,
    iso_10383_holidays,
    list_iso_3166_entities,
    list_iso_10383_entities,
)
from holidays.entities.ISO_3166 import SCOPE_ISO_3166
from holidays.entities.ISO_10383 import SCOPE_ISO_10383


class SnapshotGenerator:
    """Creates a snapshot of available holidays for supported entities."""

    years = range(1950, 2051)

    def __init__(self) -> None:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument(
            "-c",
            "--code",
            action="extend",
            nargs="+",
            default=[],
            help="Entity codes to use for snapshot generation",
            required=False,
            type=str,
        )
        arg_parser.add_argument(
            "-s",
            "--scope",
            choices=(SCOPE_ISO_3166, SCOPE_ISO_10383),
            help="Entity scope to use for snapshot generation",
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

    def generate_snapshots(self, scope):
        """Generates scope snapshots."""

        list_scope_entities_func = {
            SCOPE_ISO_3166: list_iso_3166_entities,
            SCOPE_ISO_10383: list_iso_10383_entities,
        }.get(scope)
        get_scope_holidays_func = {
            SCOPE_ISO_3166: iso_3166_holidays,
            SCOPE_ISO_10383: iso_10383_holidays,
        }.get(scope)

        if not list_scope_entities_func or not get_scope_holidays_func:
            raise ValueError(f"Scope {scope} is not supported.")

        entity_codes = self.args.code
        supported_entities = list_scope_entities_func()
        if entity_codes:
            unknown_countries = set(entity_codes).difference(supported_entities.keys())
            if len(unknown_countries) > 0:
                raise ValueError(f"Entities {', '.join(unknown_countries)} are not available")
        else:
            entity_codes = list_scope_entities_func()

        Path(f"snapshots/{scope}").mkdir(exist_ok=True)
        for entity_code in entity_codes:
            entity = getattr(holidays, entity_code)
            Path(f"snapshots/{scope}/{entity_code}").mkdir(exist_ok=True)

            for subdiv in (None,) + entity.subdivisions:
                self.save(
                    holidays.iso_3166_holidays(
                        entity_code,
                        subdiv=subdiv,
                        years=self.years,
                        categories=entity.supported_categories,
                        language="en_US",
                    ),
                    f"snapshots/{scope}/{entity_code}/{subdiv or 'COMMON'}.json",
                )

    def run(self):
        """Runs snapshot files generation process."""
        if self.args.scope is not None:
            self.generate_snapshots(self.args.scope)
        else:
            self.generate_snapshots(SCOPE_ISO_3166)
            self.generate_snapshots(SCOPE_ISO_10383)


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    SnapshotGenerator().run()
