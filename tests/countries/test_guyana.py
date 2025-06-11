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

from holidays.countries import Guyana, GY, GUY
from tests.common import CommonCountryTests


class TestGuyana(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1968, 2050)
        super().setUpClass(Guyana, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(Guyana, GY, GUY)

    def test_no_holidays(self):
        self.assertNoHolidays(Guyana(years=1967))

    def test_special_holidays(self):
        for dt, name in (("2020-03-02", "Public Holiday"),):
            self.assertHolidayName(name, dt)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1968, 2050)))
        dt = (
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-05-26" for year in range(1968, 1970)))
        self.assertNoHolidayName(name, range(1970, 2050))

    def test_republic_day(self):
        name = "Republic Day"
        self.assertHolidayName(name, (f"{year}-02-23" for year in range(1970, 2050)))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1968, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1968, 2050))

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1968, 2050)))
        dt = ("2011-05-02", "2016-05-02", "2022-05-02")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_commonwealth_day(self):
        name = "Commonwealth Day"
        self.assertHolidayName(name, range(1968, 2050))
        self.assertHolidayName(
            name, "2021-08-02", "2022-08-01", "2023-08-07", "2024-08-05", "2025-08-04"
        )

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1968, 2050)))
        dt = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_day_after_christmas(self):
        name = "Day after Christmas"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1968, 2050)))
        dt = (
            "2004-12-28",
            "2010-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_phagwah_day(self):
        name = "Phagwah Day"
        self.assertHolidayName(
            name,
            "2020-03-10",
            "2021-03-28",
            "2022-03-18",
            "2023-03-07",
            "2024-03-25",
            "2025-03-14",
            "2026-03-03",
        )
        self.assertHolidayName(name, range(2005, 2027))
        dt = ("2017-03-13",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_deepavali_day(self):
        name = "Deepavali Day"
        self.assertHolidayName(
            name,
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self.assertHolidayName(name, range(2001, 2025))
        dt = (
            "2019-10-28",
            "2023-11-13",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_youman_nabi_day(self):
        name = "Youman Nabi Day"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-09",
            "2023-09-28",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertHolidayName(name, range(2001, 2025))
        dt = ("2012-02-06", "2022-10-10")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_eid_ul_azha_day(self):
        name = "Eid-Ul-Azha Day"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-21",
            "2022-07-09",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, range(2001, 2025))
        dt = ("2014-10-06", "2019-08-12")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2024(self):
        self.assertHolidays(
            Guyana(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-02-23", "Republic Day"),
            ("2024-03-25", "Phagwah Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labour Day"),
            ("2024-06-17", "Eid-Ul-Azha Day"),
            ("2024-08-05", "Commonwealth Day"),
            ("2024-09-16", "Youman Nabi Day"),
            ("2024-10-31", "Deepavali Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Day after Christmas"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-02-23", "Republic Day"),
            ("2025-03-14", "Phagwah Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labour Day"),
            ("2025-06-07", "Eid-Ul-Azha Day"),
            ("2025-08-04", "Commonwealth Day"),
            ("2025-09-05", "Youman Nabi Day"),
            ("2025-10-20", "Deepavali Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Day after Christmas"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-02-23", "Republic Day"),
            ("2025-03-14", "Holi"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-08-04", "Commonwealth Day"),
            ("2025-09-05", "Prophet's Birthday"),
            ("2025-10-20", "Diwali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Day after Christmas"),
        )
