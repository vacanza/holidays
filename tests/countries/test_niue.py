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

from holidays.countries.niue import Niue, NU, NIU
from tests.common import CommonCountryTests


class TestNiue(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1962, 2050)
        super().setUpClass(Niue, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(Niue, NU, NIU)

    def test_no_holidays(self):
        self.assertNoHolidays(Niue(years=1961))

    def test_special_holidays(self):
        self.assertHoliday(
            "2022-09-19",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1962, 2050)))
        obs_dt = (
            "2011-01-03",
            "2012-01-03",
            "2017-01-03",
            "2022-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_takai_commission_holiday(self):
        name = "Takai Commission Holiday"
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(1962, 2050)))
        obs_dt = (
            "2011-01-04",
            "2016-01-04",
            "2021-01-04",
            "2022-01-04",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

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
        self.assertHolidayName(name, range(1962, 2050))

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
        self.assertHolidayName(name, range(1962, 2050))

    def test_anzac_day(self):
        name = "ANZAC Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1962, 2050)))
        obs_dt = (
            "2009-04-27",
            "2010-04-26",
            "2015-04-27",
            "2020-04-27",
            "2021-04-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        self.assertHolidayName(
            name,
            "2018-06-04",
            "2019-06-03",
            "2020-06-01",
            "2021-06-07",
            "2022-06-06",
        )
        self.assertHolidayName(name, range(1962, 2023))
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(
            name,
            "2023-06-05",
            "2024-06-03",
            "2025-06-02",
        )
        self.assertHolidayName(name, range(2023, 2050))
        self.assertNoHolidayName(name, range(1962, 2023))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-10-19" for year in range(1974, 2050)))
        self.assertNoHolidayName(name, range(1962, 1974))
        obs_dt = (
            "2013-10-21",
            "2014-10-21",
            "2019-10-21",
            "2024-10-21",
            "2025-10-21",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_constitution_day_holiday(self):
        name = "Constitution Day Holiday"
        self.assertHolidayName(name, (f"{year}-10-20" for year in range(1974, 2050)))
        self.assertNoHolidayName(name, range(1962, 1974))
        obs_dt = (
            "2013-10-22",
            "2019-10-22",
            "2024-10-22",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_annexation_day(self):
        name = "Annexation Day"
        self.assertHolidayName(
            name,
            "1969-10-20",
            "1970-10-19",
            "1971-10-18",
            "1972-10-16",
            "1973-10-15",
        )
        self.assertHolidayName(name, range(1962, 1974))
        self.assertNoHolidayName(name, range(1974, 2050))

    def test_peniamina_gospel_day(self):
        name = "Peniamina Gospel Day"
        self.assertHolidayName(
            name,
            "2020-10-26",
            "2021-10-25",
            "2022-10-24",
            "2023-10-23",
            "2024-10-28",
            "2025-10-27",
        )
        self.assertHolidayName(name, range(1962, 2050))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1962, 2050)))
        obs_dt = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1962, 2050)))
        obs_dt = (
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "Takai Commission Holiday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-25", "ANZAC Day"),
            ("2025-06-02", "King's Birthday"),
            ("2025-10-19", "Constitution Day"),
            ("2025-10-20", "Constitution Day Holiday"),
            ("2025-10-21", "Constitution Day (observed)"),
            ("2025-10-27", "Peniamina Gospel Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "Takai Commission Holiday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-25", "ANZAC Day"),
            ("2025-06-02", "King's Birthday"),
            ("2025-10-19", "Constitution Day"),
            ("2025-10-20", "Constitution Day Holiday"),
            ("2025-10-21", "Constitution Day (observed)"),
            ("2025-10-27", "Peniamina Gospel Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
