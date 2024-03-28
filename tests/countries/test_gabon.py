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

from holidays.countries.gabon import Gabon, GA, GAB
from tests.common import CommonCountryTests


class TestGabon(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Gabon)

    def test_country_aliases(self):
        self.assertAliases(Gabon, GA, GAB)

    def test_no_holidays(self):
        self.assertNoHolidays(Gabon(years=1960))

    def test_womens_rights_day(self):
        name = "Women's Rights Day"
        self.assertHolidayName(name, (f"{year}-04-17" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, Gabon(years=range(1961, 2015)))
        self.assertNoHoliday(
            f"{year}-04-17" for year in set(range(1961, 2015)).difference({1995, 1997, 2006})
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-04-17", "Women's Rights Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-08-15", "Assumption Day"),
            ("2022-08-16", "Independence Day"),
            ("2022-08-17", "Independence Day Holiday"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-25", "Christmas Day"),
        )
