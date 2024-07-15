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

from holidays.entities.ISO_3166.KR import KrHolidays
from tests.common import CommonCountryTests


class TestKrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(KrHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-31", "The day preceding Korean New Year"),
            ("2022-02-01", "Korean New Year"),
            ("2022-02-02", "The second day of Korean New Year"),
            ("2022-03-01", "Independence Movement Day"),
            ("2022-03-09", "Presidential Election Day"),
            ("2022-05-01", "Workers' Day"),
            ("2022-05-05", "Children's Day"),
            ("2022-05-08", "Buddha's Birthday"),
            ("2022-06-01", "Local Election Day"),
            ("2022-06-06", "Memorial Day"),
            ("2022-08-15", "Liberation Day"),
            ("2022-09-09", "The day preceding Chuseok"),
            ("2022-09-10", "Chuseok"),
            ("2022-09-11", "The second day of Chuseok"),
            ("2022-09-12", "Alternative holiday for Chuseok"),
            ("2022-10-03", "National Foundation Day"),
            ("2022-10-09", "Hangul Day"),
            ("2022-10-10", "Alternative holiday for Hangul Day"),
            ("2022-12-25", "Christmas Day"),
        )
