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

import os
import re
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from polib import pofile as create_po_file

import holidays


class TestLocalization(unittest.TestCase):
    @mock.patch.dict(os.environ, {"LANGUAGE": "en_US"})
    def test_language_unavailable_en_us(self):
        self.assertEqual(os.environ["LANGUAGE"], "en_US")
        ca_xx = holidays.country_holidays("CA", language="xx")
        self.assertEqual(ca_xx["2022-01-01"], "New Year's Day")

    @mock.patch.dict(os.environ, {"LANGUAGE": "pl"})
    def test_language_unavailable_pl(self):
        self.assertEqual(os.environ["LANGUAGE"], "pl")
        pl_xx = holidays.country_holidays("PL", language="xx")
        self.assertEqual(pl_xx["2022-01-01"], "Nowy Rok")

    def test_localization(self):
        locale_dir = Path(__file__).parents[1] / "holidays" / "locale"
        placeholder_re = re.compile(r"%[a-zA-Z]")
        mandatory_fields = {
            "Project-Id-Version",
            "Report-Msgid-Bugs-To",
            "POT-Creation-Date",
            "PO-Revision-Date",
            "Last-Translator",
            "Language-Team",
            "Language",
            "MIME-Version",
            "Content-Type",
            "Content-Transfer-Encoding",
            "X-Source-Language",
        }

        for po_path in sorted(locale_dir.rglob("*.po")):
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

            missing_fields = mandatory_fields - set(po_file.metadata.keys())
            self.assertFalse(
                missing_fields,
                f"{po_path} metadata does not contain mandatory fields: "
                f"{', '.join(missing_fields)}",
            )

            # Collect `<country_code>` part from
            # holidays/locale/<locale>/LC_MESSAGES/<country_code>.po.
            entity_code = po_path.stem
            # Collect `<locale>` part from
            # holidays/locale/<locale>/LC_MESSAGES/<country_code>.po.
            language = po_path.parts[-3]

            entity = getattr(holidays, entity_code)

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
                f"{', '.join(oe.msgid for oe in obsolete_entries)}",
            )

            for entry in po_file:
                self.assertEqual(
                    Counter(placeholder_re.findall(entry.msgid)),
                    Counter(placeholder_re.findall(entry.msgstr)),
                    f"The {entity_code} {language} localization contains placeholders "
                    f"mismatch in line {entry.linenum}: msgid `{entry.msgid}`, "
                    f"msgstr `{entry.msgstr}`.",
                )
