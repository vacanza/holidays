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

from datetime import date, timedelta
from unittest import TestCase

from holidays.countries.sint_maarten import SintMaarten, SX, SXM
from tests.common import CommonCountryTests


class TestSintMaarten(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SintMaarten, years=range(2011, 2077))

    def test_country_aliases(self):
        self.assertAliases(SintMaarten, SX, SXM)

    def test_no_holidays(self):
        self.assertNoHolidays(SintMaarten(years=2010))

    def test_2017(self):
        self.assertHolidays(
            SintMaarten(years=2017),
            ("2017-01-01", "New Year's Day"),
            ("2017-04-14", "Good Friday"),
            ("2017-04-16", "Easter Sunday"),
            ("2017-04-17", "Easter Monday"),
            ("2017-04-27", "King's Day"),
            ("2017-05-02", "Carnival Day"),
            ("2017-05-01", "Labour Day"),
            ("2017-05-25", "Ascension Day"),
            ("2017-06-04", "Whit Sunday"),
            ("2017-07-01", "Emancipation Day"),
            ("2017-10-09", "Constitution Day"),
            ("2017-11-01", "All Saints' Day"),
            ("2017-11-11", "Sint Maarten Day"),
            ("2017-12-15", "Kingdom Day"),
            ("2017-12-25", "Christmas Day"),
            ("2017-12-26", "Second day of Christmas"),
        )

    def test_pre_2011_branch_coverage(self):
        class TestSintMaarten(SintMaarten):
            start_year = 2010

        holidays = TestSintMaarten(years=2010)
        # Verify holidays that should exist
        self.assertIn(date(2010, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2010, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2010, 4, 4), holidays)  # Easter Sunday
        self.assertIn(date(2010, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2010, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2010, 5, 13), holidays)  # Ascension Day
        self.assertIn(date(2010, 5, 23), holidays)  # Whit Sunday
        self.assertIn(date(2010, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2010, 12, 26), holidays)  # Second Day of Christmas
        self.assertNotIn(date(2010, 4, 27), holidays)  # No King's Day
        self.assertNotIn(date(2010, 4, 26), holidays)  # No King's Day (Sunday)
        self.assertNotIn(date(2010, 4, 30), holidays)  # No Carnival Day
        self.assertNotIn(date(2010, 7, 1), holidays)  # No Emancipation Day
        self.assertNotIn(date(2010, 10, 11), holidays)  # No Constitution Day
        self.assertNotIn(date(2010, 11, 1), holidays)  # No All Saints' Day
        self.assertNotIn(date(2010, 11, 11), holidays)  # No Sint Maarten Day
        self.assertNotIn(date(2010, 12, 15), holidays)  # No Kingdom Day

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertNoHolidayName(name, range(1900, 2012))
        self.assertHolidayName(name, (f"{year}-07-01" for year in range(2012, 2077)))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertNoHolidayName(name, range(1900, 2015))
        second_monday_dates = {
            2015: "2015-10-12",
            2017: "2017-10-09",
            2018: "2018-10-08",
            2019: "2019-10-14",
            2020: "2020-10-12",
            2025: "2025-10-13",
        }
        for year, date_str in second_monday_dates.items():
            self.assertHolidayName(name, date_str)
        for year in range(2015, 2077):
            base_date = date(year, 10, 1)
            second_monday = base_date + timedelta(days=(7 - base_date.weekday()) % 7 + 7)
            self.assertHolidayName(name, second_monday)

    def test_all_saints_day(self):
        name = "All Saints' Day"
        self.assertNoHolidayName(name, range(1900, 2011))
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(2011, 2077)))

    def test_sint_maarten_day(self):
        name = "Sint Maarten Day"
        self.assertNoHolidayName(name, range(1900, 2011))
        self.assertHolidayName(name, (f"{year}-11-11" for year in range(2011, 2077)))

    def test_kings_day(self):
        name = "King's Day"
        self.assertNoHolidayName(name, range(1900, 2014))
        self.assertHolidayName(
            name,
            "2014-04-26",  # Sunday, observed on Saturday
            "2015-04-27",  # Monday
            "2017-04-27",  # Thursday
            "2019-04-27",  # Saturday
            "2020-04-27",  # Monday
            "2024-04-27",  # Saturday
            "2025-04-26",  # Sunday, observed on Saturday
        )
        self.assertNoHoliday(
            "2013-04-27",  # No King's Day
            "2014-04-27",  # No Sunday observance
            "2025-04-27",  # No Sunday observance
        )

    def test_kings_day_shifted_sunday(self):
        name = "King's Day"
        self.assertHolidayName(name, "2014-04-26")  # 2014: April 27 is Sunday
        self.assertHolidayName(name, "2025-04-26")  # 2025: April 27 is Sunday
        self.assertNoHoliday("2014-04-27")
        self.assertNoHoliday("2025-04-27")

    def test_kingdom_day(self):
        name = "Kingdom Day"
        # Check that Kingdom Day is not observed before 2011
        self.assertNoHolidayName(name, range(1900, 2011))

        # Check Kingdom Day from 2011 onward
        for year in range(2011, 2077):
            expected_date = get_expected_kingdom_day(year)
            expected_date_str = expected_date.strftime("%Y-%m-%d")
            self.assertHolidayName(name, expected_date_str)
            # If the holiday is moved to Dec 16, ensure Dec 15 is not a holiday
            if expected_date.day == 16:  # Moved to Monday
                self.assertNoHolidayName(name, f"{year}-12-15")

    def test_carnival_day(self):
        name = "Carnival Day"
        # Check that Carnival Day is not observed before 2011
        self.assertNoHolidayName(name, range(1900, 2011))

        # Check Carnival Day from 2011 onward
        for year in range(2011, 2077):
            expected_date = get_expected_carnival_day(year)
            expected_date_str = expected_date.strftime("%Y-%m-%d")
            self.assertHolidayName(name, expected_date_str)
            # Optionally, ensure the holiday doesn't appear on other dates around April 30
            for offset in [-2, -1, 1, 2]:  # Check nearby dates
                test_date = expected_date + timedelta(days=offset)
                test_date_str = test_date.strftime("%Y-%m-%d")
                if test_date != expected_date:
                    self.assertNoHolidayName(name, test_date_str)

    def test_christmas(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(2011, 2077)))
        self.assertHolidayName(
            "Second day of Christmas", (f"{year}-12-26" for year in range(2011, 2077))
        )


def get_expected_carnival_day(year):
    """Calculate the expected date for Carnival Day (April 30) with movement rule."""
    carnival_date = date(year, 4, 30)
    weekday = carnival_date.weekday()  # Monday=0, Sunday=6
    if weekday == 5:  # Saturday
        return carnival_date - timedelta(days=1)  # Previous Friday
    elif weekday == 6:  # Sunday
        return carnival_date + timedelta(days=2)  # Next Tuesday
    return carnival_date


def get_expected_kingdom_day(year):
    """Calculate the expected date for Kingdom Day (December 15) with movement rule."""
    kingdom_date = date(year, 12, 15)
    weekday = kingdom_date.weekday()  # Monday=0, Sunday=6
    if weekday == 6:  # Sunday
        return kingdom_date + timedelta(days=1)  # Next Monday
    return kingdom_date
