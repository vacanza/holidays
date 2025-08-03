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

from holidays.countries import Gambia, GM, GMB
from tests.common import CommonCountryTests


class TestGambia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1966, 2050)
        super().setUpClass(Gambia, years=years, years_non_observed=years)
        cls.no_estimated_holidays = Gambia(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Gambia, GM, GMB)

    def test_no_holidays(self):
        self.assertNoHolidays(Gambia(years=1965))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1966, 2050)))
        dt = ("2023-01-02",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-02-18" for year in range(1966, 2050)))
        dt = ("2024-02-19",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1966, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1966, 2050))

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1966, 2050)))
        dt = ("2022-05-02",)
        self.assertHolidayName(f"{name} (observed)", dt)

    def test_africa_liberation_day(self):
        name = "Africa Liberation Day"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(1966, 2050)))
        dt = ("2025-05-26",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_july_22_revolution_day(self):
        self.assertHolidayName(
            "July 22 Revolution Day", (f"{year}-07-22" for year in range(1966, 2050))
        )

    def test_assumption_day(self):
        name = "Feast of the Assumption"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(1966, 2050)))
        dt = ("2021-08-16",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1966, 2050)))
        dt = ("2022-12-27",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(2021, 2050)))

    def test_yawmul_ashura_day(self):
        name = "Yawmul Ashura"
        self.assertHolidayName(
            name,
            "2021-08-19",
            "2022-08-08",
            "2023-07-28",
            "2024-07-16",
            "2025-07-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1966, 2050))

    def test_mawlid_nabi_day(self):
        name = "Mawlid Nabi"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-28",
            "2024-09-16",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1966, 2050))

    def test_lialat_ul_qadr_day(self):
        name = "Lialat-Ul-Qadr"
        self.assertHolidayName(
            name,
            "2021-05-09",
            "2022-04-29",
            "2023-04-18",
            "2024-04-06",
            "2025-03-27",
        )
        dt = ("2021-05-10",)
        self.assertHolidayName(f"{name} (observed)", self.no_estimated_holidays, dt)
        self.assertNoNonObservedHoliday(dt)

    def test_kotireh(self):
        name = "Koriteh"
        self.assertHolidayName(
            name,
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2023-04-22",
            "2024-04-10",
            "2024-04-11",
            "2025-03-30",
            "2025-03-31",
        )
        dt = ("2025-04-01",)
        self.assertHolidayName(f"{name} (observed)", self.no_estimated_holidays, dt)
        self.assertNoNonObservedHoliday(dt)

    def test_tobaski(self):
        name = "Tobaski"
        self.assertHolidayName(
            name,
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2023-06-29",
            "2024-06-16",
            "2024-06-17",
            "2025-06-06",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1966, 2050))

    def test_2024(self):
        self.assertHolidays(
            Gambia(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-02-18", "Independence Day"),
            ("2024-02-19", "Independence Day (observed)"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-06", "Lialat-Ul-Qadr"),
            ("2024-04-08", "Lialat-Ul-Qadr (observed)"),
            ("2024-04-10", "Koriteh"),
            ("2024-04-11", "Koriteh"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-25", "Africa Liberation Day"),
            ("2024-05-27", "Africa Liberation Day (observed)"),
            ("2024-06-16", "Tobaski"),
            ("2024-06-17", "Tobaski"),
            ("2024-06-18", "Tobaski (observed)"),
            ("2024-07-16", "Yawmul Ashura"),
            ("2024-07-22", "July 22 Revolution Day"),
            ("2024-08-15", "Feast of the Assumption"),
            ("2024-09-16", "Mawlid Nabi"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-02-18", "Independence Day"),
            ("2025-03-27", "Lialat-Ul-Qadr"),
            ("2025-03-30", "Koriteh"),
            ("2025-03-31", "Koriteh"),
            ("2025-04-01", "Koriteh (observed)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labour Day"),
            ("2025-05-25", "Africa Liberation Day"),
            ("2025-05-26", "Africa Liberation Day (observed)"),
            ("2025-06-06", "Tobaski"),
            ("2025-06-07", "Tobaski"),
            ("2025-06-09", "Tobaski (observed)"),
            ("2025-07-05", "Yawmul Ashura"),
            ("2025-07-07", "Yawmul Ashura (observed)"),
            ("2025-07-22", "July 22 Revolution Day"),
            ("2025-08-15", "Feast of the Assumption"),
            ("2025-09-04", "Mawlid Nabi (estimated)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-02-18", "Independence Day"),
            ("2025-03-27", "Laylat al-Qadr"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-01", "Eid al-Fitr (observed)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-25", "Africa Liberation Day"),
            ("2025-05-26", "Africa Liberation Day (observed)"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-09", "Eid al-Adha (observed)"),
            ("2025-07-05", "Ashura"),
            ("2025-07-07", "Ashura (observed)"),
            ("2025-07-22", "July 22 Revolution Day"),
            ("2025-08-15", "Assumption Day"),
            ("2025-09-04", "Prophet's Birthday (estimated)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
