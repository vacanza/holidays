#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import WORKDAY
from holidays.countries.fiji import Fiji, FJ, FJI
from tests.common import CommonCountryTests


class TestFiji(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1970, 2050)
        super().setUpClass(Fiji, years=years)
        cls.workday_holidays = Fiji(categories=WORKDAY, years=years)

    def test_country_aliases(self):
        self.assertAliases(Fiji, FJ, FJI)

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1970, 2050)))

        dt = (
            "2017-01-03",
            "2022-01-03",
            "2023-01-03",
            "2028-01-03",
        )
        self.assertHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        dts = (
            "1999-04-02",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1970, 2050))

    def test_easter_saturday(self):
        name = "Easter Saturday"
        dts = (
            "1999-04-03",
            "2000-04-22",
            "2010-04-03",
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1979, 2050))

    def test_easter_sunday(self):
        name = "Easter Sunday"
        dts = (
            "1999-04-04",
            "2000-04-23",
            "2010-04-04",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1979, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        dts = (
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1979, 2050))

    def test_national_youth_day(self):
        self.assertHolidayName(
            "National Youth Day", (f"{year}-05-04" for year in range(1970, 2050))
        )

    def test_girmit_day(self):
        self.assertHolidayName("Girmit Day", (f"{year}-05-14" for year in range(2023, 2050)))

    def test_fiji_day(self):
        name = "Fiji Day"
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(1970, 2050)))
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertEqual(set(range(1970, 2050)), years_found)

    def test_diwali_and_holi(self):
        dt = (
            "2015-11-11",
            "2016-10-27",
            "2017-10-16",
            "2018-11-07",
            "2019-10-28",
            "2020-11-14",  # also should be a day off on Nov 16
            "2021-11-04",
            "2022-10-25",
            "2023-11-13",
            "2024-11-01",
            "2025-10-21",
        )
        self.assertHolidayName("Diwali", dt)

    def test_christmas_day(self):
        for year in range(1970, 2050):
            self.assertHoliday(f"{year}-12-25")

        dt = (
            "2021-12-27",
            "2027-12-27",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        for year in range(1970, 2050):
            self.assertHoliday(f"{year}-12-26")

        dt = (
            "2020-12-28",
            "2021-12-28",
            "2026-12-28",
            "2027-12-28",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_ratu_sir_lala_sukuna_day(self):
        dt = (
            "2000-05-29",
            "2001-05-28",
            "2002-05-27",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
            "2026-05-25",
            "2027-05-31",
        )

        name = "Ratu Sir Lala Sukuna Day"
        self.assertNoHoliday(dt)
        self.assertNoHolidayName(name, dt)
        self.assertHolidayName(name, self.workday_holidays, dt)

    def test_queen_birthday(self):
        name = "Queen's Birthday"
        self.assertNoHoliday(f"{year}-06-12" for year in range(1970, 2012))
        self.assertNoHolidayName(name, range(1970, 2012))
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-06-12" for year in range(1970, 2012))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2013, 2050))

    def test_2023(self):
        self.assertHolidayDates(
            Fiji(years=2023),
            "2023-01-01",
            "2023-01-03",
            "2023-04-07",
            "2023-04-08",
            "2023-04-09",
            "2023-04-10",
            "2023-05-04",
            "2023-05-14",
            "2023-05-16",
            "2023-09-27",
            "2023-10-10",
            "2023-11-13",
            "2023-12-25",
            "2023-12-26",
        )

    def test_2024(self):
        self.assertHolidayDates(
            Fiji(years=2024),
            "2024-01-01",
            "2024-03-29",
            "2024-03-30",
            "2024-03-31",
            "2024-04-01",
            "2024-05-04",
            "2024-05-13",
            "2024-05-14",
            "2024-09-15",
            "2024-09-17",
            "2024-10-10",
            "2024-11-01",
            "2024-12-25",
            "2024-12-26",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-11", "Easter Saturday"),
            ("2020-04-12", "Easter Sunday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-04", "National Youth Day"),
            ("2020-05-24", "Eid al-Fitr (estimated)"),
            ("2020-10-10", "Fiji Day"),
            ("2020-10-29", "Prophet Mohammed's Birthday (estimated)"),
            ("2020-11-14", "Diwali"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Boxing Day"),
            ("2020-12-28", "Boxing Day (observed)"),
        )
