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

from holidays.entities.ISO_3166.MD import MdHolidays
from tests.common import CommonCountryTests


class TestMdHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MdHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-07", "Christmas Day (by old style)"),
            ("2022-01-08", "Christmas Day (by old style)"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-24", "Easter"),
            ("2022-04-25", "Easter"),
            ("2022-05-01", "International Workers' Solidarity Day"),
            ("2022-05-02", "Day of Rejoicing"),
            (
                "2022-05-09",
                "Europe Day; Victory Day and Commemoration of the heroes "
                "fallen for Independence of Fatherland",
            ),
            ("2022-06-01", "International Children's Day"),
            ("2022-08-27", "Republic of Moldova Independence Day"),
            ("2022-08-31", "National Language Day"),
            ("2022-12-25", "Christmas Day (by new style)"),
        )
