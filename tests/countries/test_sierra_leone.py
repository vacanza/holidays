#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries import SierraLeone, SL, SLE
from tests.common import CommonCountryTests


class TestSierraLeone(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1962, 2050)
        super().setUpClass(SierraLeone, years=years, years_non_observed=years)
        cls.no_estimated_holidays = SierraLeone(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(SierraLeone, SL, SLE)

    def test_no_holidays(self):
        self.assertNoHolidays(SierraLeone(years=1961))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1962, 2050)))

    def test_armed_forces_day(self):
        name = "Armed Forces Day"
        self.assertHolidayName(name, (f"{year}-02-18" for year in range(2002, 2050)))
        self.assertNoHolidayName(name, range(1962, 2002))

    def test_international_womens_day(self):
        name = "International Women's Day"
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(2018, 2050)))
        self.assertNoHolidayName(name, range(1962, 2018))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(name, "2022-04-15", "2023-04-07", "2024-03-29")
        self.assertHolidayName(name, range(1962, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(name, "2022-04-18", "2023-04-10", "2024-04-01")
        self.assertHolidayName(name, range(1962, 2050))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-04-27" for year in range(1962, 2050)))
        dt = (
            "2008-04-28",
            "2013-04-29",
            "2019-04-29",
            "2024-04-29",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_labor_day(self):
        name = "International Worker's Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1962, 2050)))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1962, 2050)))

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1962, 2050)))

    def test_prophets_birthday(self):
        name = "Prophet's Birthday"
        self.assertHolidayName(
            name,
            "2018-11-21",
            "2019-11-10",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1962, 2050))

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-05",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1962, 2050))

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            "2018-08-22",
            "2019-08-12",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1962, 2050))

    def test_2024(self):
        self.assertHolidays(
            SierraLeone(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-02-18", "Armed Forces Day"),
            ("2024-02-19", "Armed Forces Day (observed)"),
            ("2024-03-08", "International Women's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-27", "Independence Day"),
            ("2024-04-29", "Independence Day (observed)"),
            ("2024-05-01", "International Worker's Day"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-17", "Eid al-Adha (observed)"),
            ("2024-09-15", "Prophet's Birthday"),
            ("2024-09-16", "Prophet's Birthday (observed)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-02-18", "Armed Forces Day"),
            ("2025-03-08", "International Women's Day"),
            ("2025-03-10", "International Women's Day (observed)"),
            ("2025-03-30", "Eid al-Fitr (estimated)"),
            ("2025-03-31", "Eid al-Fitr (observed, estimated)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-27", "Independence Day"),
            ("2025-04-28", "Independence Day (observed)"),
            ("2025-05-01", "International Worker's Day"),
            ("2025-06-06", "Eid al-Adha (estimated)"),
            ("2025-09-04", "Prophet's Birthday (estimated)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-02-18", "Armed Forces Day"),
            ("2025-03-08", "International Women's Day"),
            ("2025-03-10", "International Women's Day (observed)"),
            ("2025-03-30", "Eid al-Fitr (estimated)"),
            ("2025-03-31", "Eid al-Fitr (observed, estimated)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-27", "Independence Day"),
            ("2025-04-28", "Independence Day (observed)"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-06", "Eid al-Adha (estimated)"),
            ("2025-09-04", "Prophet's Birthday (estimated)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
