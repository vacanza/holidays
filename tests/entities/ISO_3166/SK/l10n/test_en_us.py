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

from holidays.entities.ISO_3166.SK import SkHolidays
from tests.common import CommonCountryTests


class TestSkHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SkHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Day of the Establishment of the Slovak Republic"),
            ("2022-01-06", "Epiphany (Three Kings' Day and Orthodox Christmas)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "Day of Victory over Fascism"),
            ("2022-07-05", "St. Cyril and Methodius Day"),
            ("2022-08-29", "Slovak National Uprising Anniversary"),
            ("2022-09-01", "Constitution Day"),
            ("2022-09-15", "Day of Our Lady of the Seven Sorrows"),
            ("2022-10-28", "Day of the Establishment of the Independent Czech-Slovak State"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-17", "Struggle for Freedom and Democracy Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )
