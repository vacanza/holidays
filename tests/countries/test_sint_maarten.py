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

from unittest import TestCase

from holidays.countries.sint_maarten import SintMaarten, SX, SXM
from tests.common import CommonCountryTests


class TestSintMaarten(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SintMaarten, years=range(2010, 2077))

    def test_country_aliases(self):
        self.assertAliases(SintMaarten, SX, SXM)

    def test_no_holidays(self):
        self.assertNoHolidays(SintMaarten(years=2009))

    def test_2017(self):
        self.assertHolidays(
            SintMaarten(years=2017),
            ("2017-01-01", "New Year's Day"),
            ("2017-04-14", "Good Friday"),
            ("2017-04-16", "Easter Sunday"),
            ("2017-04-17", "Easter Monday"),
            ("2017-04-27", "King's Day"),
            ("2017-04-30", "Carnival Day"),
            ("2017-05-01", "Labour Day"),
            ("2017-05-25", "Ascension Day"),
            ("2017-06-04", "Whit Sunday"),
            ("2017-10-10", "Constitution Day"),
            ("2017-11-11", "Sint Maarten Day"),
            ("2017-12-25", "Christmas Day"),
            ("2017-12-26", "Second day of Christmas"),
        )

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertNoHolidayName(name, range(2010, 2020))
        self.assertHolidayName(name, (f"{year}-07-01" for year in range(2020, 2077)))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertNoHolidayName(name, range(1900, 2010))
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(2010, 2077)))

    def test_sint_maarten_day(self):
        name = "Sint Maarten Day"
        self.assertHolidayName(name, (f"{year}-11-11" for year in range(2010, 2077)))

    def test_king_day(self):
        name = "King's Day"
        self.assertNoHolidayName(name, range(1900, 2014))
        self.assertHolidayName(
            name,
            "2017-04-27",
            "2019-04-27",
            "2020-04-27",
            "2024-04-27",
            "2025-04-26",  # Observed early due to Sunday
        )
        self.assertNoHoliday(
            "2025-04-27",
            "2031-04-27",
            "2036-04-27",
        )

    def test_carnival_day(self):
        name = "Carnival Day"
        self.assertHolidayName(name, (f"{year}-04-30" for year in range(2010, 2077)))
        self.assertNoHolidayName(name, range(1900, 2010))

    def test_christmas(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(2010, 2077)))
        self.assertHolidayName(
            "Second day of Christmas", (f"{year}-12-26" for year in range(2010, 2077))
        )
