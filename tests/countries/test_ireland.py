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

from holidays.countries.ireland import Ireland
from tests.common import CommonCountryTests


class TestIreland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ireland)

    def test_special_holidays(self):
        self.assertHoliday(
            "1999-12-31",
            "2011-09-14",
            "2022-03-18",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1975, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1975))

    def test_st_brigids_day(self):
        name = "Saint Brigid's Day"
        self.assertHolidayName(
            name,
            "2023-02-06",
            "2024-02-05",
            "2025-02-03",
            "2026-02-02",
            "2027-02-01",
            "2028-02-07",
            "2029-02-05",
            "2030-02-01",
            "2031-02-03",
            "2032-02-02",
        )
        self.assertHolidayName(name, range(2023, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2023))

    def test_st_patricks_day(self):
        name = "Saint Patrick's Day"
        self.assertHolidayName(name, (f"{year}-03-17" for year in range(1903, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1903))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_may_day(self):
        name = "May Day"
        self.assertHolidayName(
            name,
            "2020-05-04",
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
            "2025-05-05",
        )
        self.assertHolidayName(name, range(1994, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1994))

    def test_june_bank_holiday(self):
        name = "June Bank Holiday"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-06-07",
            "2022-06-06",
            "2023-06-05",
            "2024-06-03",
            "2025-06-02",
        )
        self.assertHolidayName(name, range(1973, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1973))

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "1940-05-13",
            "1950-05-29",
            "1960-06-06",
            "1970-05-18",
            "1971-05-31",
            "1972-05-22",
        )
        self.assertHolidayName(name, range(self.start_year, 1973))
        self.assertNoHolidayName(name, range(1973, self.end_year))

    def test_august_bank_holiday(self):
        name = "August Bank Holiday"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, self.full_range)

    def test_october_bank_holiday(self):
        name = "October Bank Holiday"
        self.assertHolidayName(
            name,
            "2020-10-26",
            "2021-10-25",
            "2022-10-31",
            "2023-10-30",
            "2024-10-28",
            "2025-10-27",
        )
        self.assertHolidayName(name, range(1977, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1977))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_st_stephens_day(self):
        self.assertHolidayName(
            "Saint Stephen's Day", (f"{year}-12-26" for year in self.full_range)
        )

    def test_2020(self):
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "New Year's Day"),
            ("2020-03-17", "Saint Patrick's Day"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-04", "May Day"),
            ("2020-06-01", "June Bank Holiday"),
            ("2020-08-03", "August Bank Holiday"),
            ("2020-10-26", "October Bank Holiday"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Saint Stephen's Day"),
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-03-17", "Saint Patrick's Day"),
            ("2022-03-18", "Day of Remembrance and Recognition"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "May Day"),
            ("2022-06-06", "June Bank Holiday"),
            ("2022-08-01", "August Bank Holiday"),
            ("2022-10-31", "October Bank Holiday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
        )
    def test_good_friday(self):
        name = "Good Friday"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertOptionalHolidayName(name, self.full_range)
