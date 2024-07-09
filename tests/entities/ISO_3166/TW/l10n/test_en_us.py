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

from holidays.entities.ISO_3166.TW import TwHolidays
from tests.common import CommonCountryTests


class TestTwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TwHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Founding Day of the Republic of China"),
            ("2022-01-31", "Chinese New Year's Eve"),
            ("2022-02-01", "Chinese New Year"),
            ("2022-02-02", "Chinese New Year"),
            ("2022-02-03", "Chinese New Year"),
            ("2022-02-04", "Day off (substituted from 01/22/2022)"),
            ("2022-02-28", "Peace Memorial Day"),
            ("2022-04-04", "Children's Day"),
            ("2022-04-05", "Tomb Sweeping Day"),
            ("2022-06-03", "Dragon Boat Festival"),
            ("2022-09-09", "Mid-Autumn Festival (observed)"),
            ("2022-09-10", "Mid-Autumn Festival"),
            ("2022-10-10", "National Day"),
        )
