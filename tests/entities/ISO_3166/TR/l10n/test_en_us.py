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

from unittest import TestCase

from holidays.entities.ISO_3166.TR import TrHolidays
from tests.common import CommonCountryTests


class TestTrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TrHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-04-20", "Eid al-Fitr (from 1pm)"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr; National Sovereignty and Children's Day"),
            ("2023-05-01", "Labour and Solidarity Day"),
            ("2023-05-19", "Commemoration of Atatürk, Youth and Sports Day"),
            ("2023-06-27", "Eid al-Adha (from 1pm)"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-01", "Eid al-Adha"),
            ("2023-07-15", "Democracy and National Unity Day"),
            ("2023-08-30", "Victory Day"),
            ("2023-10-28", "Republic Day (from 1pm)"),
            ("2023-10-29", "Republic Day"),
        )
