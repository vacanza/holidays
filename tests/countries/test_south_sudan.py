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

from holidays.constants import ISLAMIC
from holidays.countries.south_sudan import SouthSudan, SS, SSD
from tests.common import CommonCountryTests


class TestSouthSudan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2011, 2050)
        super().setUpClass(SouthSudan, years=years, years_non_observed=years)
        cls.no_estimated_holidays = SouthSudan(years=years, islamic_show_estimated=False)
        cls.islamic_holidays = SouthSudan(categories=ISLAMIC, years=years)

    def test_country_aliases(self):
        self.assertAliases(SouthSudan, SS, SSD)

    def test_no_holidays(self):
        self.assertNoHolidays(SouthSudan(years=2010))
        self.assertNoHolidays(SouthSudan(categories=ISLAMIC, years=2010))

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(2011, 2050)))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_holy_saturday(self):
        name = "Holy Saturday"
        self.assertHolidayName(
            name,
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_easter_sunday(self):
        name = "Easter Sunday"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(2011, 2050))

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
        self.assertHolidayName(name, range(2011, 2050))

    def test_labor_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(2011, 2050)))

    def test_spla_day(self):
        self.assertHolidayName("SPLA Day", (f"{year}-05-16" for year in range(2011, 2050)))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-07-09" for year in range(2011, 2050)))

    def test_martyrs_day(self):
        self.assertHolidayName("Martyrs' Day", (f"{year}-07-30" for year in range(2011, 2050)))

    def test_christmas_eve(self):
        self.assertHolidayName("Christmas Eve", (f"{year}-12-24" for year in range(2011, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(2011, 2050)))

    def test_second_day_of_christmas(self):
        self.assertHolidayName(
            "Second Day of Christmas", (f"{year}-12-26" for year in range(2011, 2050))
        )

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2011, 2050))

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2011, 2050))

    def test_eid_al_fitr_holiday(self):
        name = "Eid al-Fitr Holiday (estimated)"
        self.assertHolidayName(
            name,
            self.islamic_holidays,
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-03-31",
        )
        self.assertHolidayName(name, self.islamic_holidays, range(2011, 2050))

    def test_eid_al_adha_holiday(self):
        name = "Eid al-Adha Holiday (estimated)"
        self.assertHolidayName(
            name,
            self.islamic_holidays,
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.islamic_holidays, range(2011, 2050))

    def test_2020(self):
        self.assertHolidays(
            SouthSudan(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-11", "Holy Saturday"),
            ("2020-04-12", "Easter Sunday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-01", "Labour Day"),
            ("2020-05-16", "SPLA Day"),
            ("2020-05-24", "Eid al-Fitr (estimated)"),
            ("2020-07-09", "Independence Day"),
            ("2020-07-30", "Martyrs' Day"),
            ("2020-07-31", "Eid al-Adha (estimated)"),
            ("2020-12-24", "Christmas Eve"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Second Day of Christmas"),
        )
