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

from holidays.entities.ISO_3166.KH import KhHolidays
from tests.common import CommonCountryTests


class TestKhHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(KhHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "International New Year Day"),
            ("2023-01-07", "Day of Victory over the Genocidal Regime"),
            ("2023-03-08", "International Women's Rights Day"),
            ("2023-04-14", "Khmer New Year's Day"),
            ("2023-04-15", "Khmer New Year's Day"),
            ("2023-04-16", "Khmer New Year's Day"),
            ("2023-05-01", "International Labor Day"),
            ("2023-05-04", "Visaka Bochea Day"),
            ("2023-05-08", "Royal Ploughing Ceremony"),
            ("2023-05-14", "HM King Norodom Sihamoni's Birthday"),
            (
                "2023-06-18",
                "HM Queen Norodom Monineath Sihanouk the Queen-Mother's Birthday",
            ),
            ("2023-09-24", "Constitution Day"),
            ("2023-10-13", "Pchum Ben Day"),
            ("2023-10-14", "Pchum Ben Day"),
            (
                "2023-10-15",
                "HM King Norodom Sihanouk Mourning Day; Pchum Ben Day",
            ),
            ("2023-10-29", "HM King Norodom Sihamoni's Coronation Day"),
            ("2023-11-09", "National Independence Day"),
            ("2023-11-26", "Water Festival"),
            ("2023-11-27", "Water Festival"),
            ("2023-11-28", "Water Festival"),
        )
