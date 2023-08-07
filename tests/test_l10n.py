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

import re
import unittest
from pathlib import Path

from polib import pofile as create_po_file

import holidays


class TestLocalization(unittest.TestCase):
    def test_localization(self):
        tests_dir = Path(__file__).parent
        locale_dir = tests_dir.parent / "holidays" / "locale"

        for po_path in sorted(Path(locale_dir).rglob("*.po")):
            try:
                po_file = create_po_file(po_path, check_for_duplicates=True)
            except ValueError as e:
                # Make sure no duplicated entries added.
                match = re.match(r"Entry (.*) already exists", str(e))
                self.assertEqual(
                    0,
                    len(match.groups()),
                    f"Entry `{match.group(1)}` already exists in {po_path}. "
                    "Please remove the duplicate.",
                )

                raise e

            entity_code = str(po_path.parts[-1]).split(".")[0]
            entity = getattr(holidays, entity_code)
            # Collect `<locale>` part from
            # holidays/locale/<locale>/LC_MESSAGES/<country_code>.po.
            language = po_path.parts[-3]

            # Skip original language files.
            if entity.default_language == language:
                continue

            # Make sure no entries left unlocalized.
            coverage = po_file.percent_translated()
            self.assertEqual(
                100,
                coverage,
                f"The {entity_code} {language} localization is incomplete ({coverage}% < 100%)",
            )

            # Make sure no obsolete entries left.
            obsolete_entries = po_file.obsolete_entries()
            self.assertFalse(
                obsolete_entries,
                f"The {entity_code} {language} localization contains obsolete entries: "
                f"{', '.join((oe.msgid for oe in obsolete_entries))}",
            )
