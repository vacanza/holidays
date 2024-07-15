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

from holidays.entities.ISO_3166.BG import BgHolidays
from tests.common import CommonCountryTests


class TestBgHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BgHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-03-03", "Liberation Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-23", "Holy Saturday"),
            ("2022-04-24", "Easter"),
            ("2022-04-25", "Easter"),
            ("2022-05-01", "Labor Day and International Workers' Solidarity Day"),
            ("2022-05-02", "Labor Day and International Workers' Solidarity Day (observed)"),
            ("2022-05-06", "St. George's Day (Day of the Bulgarian Army)"),
            ("2022-05-24", "Day of Slavonic Alphabet, Bulgarian Enlightenment and Culture"),
            ("2022-09-06", "Unification Day"),
            ("2022-09-22", "Independence Day"),
            ("2022-11-01", "The Day of the People's Awakeners"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day"),
            ("2022-12-27", "Christmas Eve (observed)"),
            ("2022-12-28", "Christmas Day (observed)"),
        )
