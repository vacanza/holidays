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

from holidays.countries.nigeria import Nigeria
from tests.common import CommonCountryTests


class TestNigeria(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Nigeria)

    def test_special_holidays(self):
        self.assertHoliday(
            "2007-04-12",
            "2007-04-13",
            "2010-05-06",
            "2019-02-22",
            "2025-07-15",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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
        self.assertHolidayName(name, self.full_range)

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

    def test_workers_day(self):
        name = "Workers' Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1985, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1985))
        obs_dts = (
            "2016-05-02",
            "2021-05-03",
            "2022-05-04",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_democracy_day(self):
        name = "Democracy Day"
        self.assertHolidayName(
            name,
            (f"{year}-05-29" for year in range(2000, 2019)),
            (f"{year}-06-12" for year in range(2019, self.end_year)),
        )
        self.assertNoHolidayName(name, range(self.start_year, 2000))
        obs_dts = (
            "2016-05-30",
            "2021-06-14",
            "2022-06-13",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_presidential_inauguration_day(self):
        name = "Presidential Inauguration Day"
        self.assertHolidayName(
            name,
            "1999-05-29",
            "2003-05-29",
            "2007-05-29",
            "2011-05-29",
            "2015-05-29",
            "2019-05-29",
            "2023-05-29",
        )
        self.assertNoHolidayName(name, range(self.start_year, 1999))

    def test_national_day(self):
        name = "National Day"
        self.assertHolidayName(name, (f"{year}-10-01" for year in self.full_range))
        obs_dts = (
            "2017-10-02",
            "2022-10-03",
            "2023-10-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_prophets_birthday(self):
        name = "Id el Maulud"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-27",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2019-11-11",
            "2022-10-10",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Id el Fitr"
        name_holiday = f"{name} Holiday"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        self.assertIslamicNoEstimatedHolidayName(name_holiday, self.full_range)
        obs_dts = (
            "2020-05-26",
            "2025-04-01",
        )
        obs_holiday_dts = (
            "2018-06-18",
            "2023-04-24",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertHolidayName(f"{name_holiday} (observed)", obs_holiday_dts)
        self.assertNoNonObservedHoliday(obs_dts, obs_holiday_dts)

    def test_eid_al_adha(self):
        name = "Id el Kabir"
        name_holiday = f"{name} Holiday"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        self.assertIslamicNoEstimatedHolidayName(name_holiday, self.full_range)
        obs_dts = (
            "2017-09-04",
            "2022-07-11",
            "2024-06-18",
        )
        obs_holiday_dts = (
            "2020-08-03",
            "2022-07-12",
            "2025-06-09",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertHolidayName(f"{name_holiday} (observed)", obs_holiday_dts)
        self.assertNoNonObservedHoliday(obs_dts, obs_holiday_dts)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Id el Fitr"),
            ("2024-04-11", "Id el Fitr Holiday"),
            ("2024-05-01", "Workers' Day"),
            ("2024-06-12", "Democracy Day"),
            ("2024-06-16", "Id el Kabir"),
            ("2024-06-17", "Id el Kabir Holiday"),
            ("2024-06-18", "Id el Kabir (observed)"),
            ("2024-09-16", "Id el Maulud"),
            ("2024-10-01", "National Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-11", "Eid al-Fitr Holiday"),
            ("2024-05-01", "Workers' Day"),
            ("2024-06-12", "Democracy Day"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-17", "Eid al-Adha Holiday"),
            ("2024-06-18", "Eid al-Adha (observed)"),
            ("2024-09-16", "Prophet's Birthday"),
            ("2024-10-01", "National Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
