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

from holidays.countries.ghana import Ghana
from tests.common import CommonCountryTests


class TestGhana(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ghana)

    def test_new_year_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-01-07" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2019))
        obs_dts = (
            "2023-01-09",
            "2024-01-08",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-03-06" for year in self.full_range))
        obs_dts = (
            "2011-03-07",
            "2016-03-07",
            "2021-03-08",
            "2022-03-07",
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

    def test_labor_day(self):
        name = "May Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_founders_day(self):
        name = "Founders' Day"
        self.assertHolidayName(name, (f"{year}-08-04" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2019))
        obs_dts = (
            "2019-08-05",
            "2024-08-05",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_kwame_nkrumah_memorial_day(self):
        name_2009 = "Founder's Day"
        name_2019 = "Kwame Nkrumah Memorial Day"
        self.assertHolidayName(name_2009, (f"{year}-09-21" for year in range(2009, 2019)))
        self.assertHolidayName(name_2019, (f"{year}-09-21" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(
            name_2009, range(self.start_year, 2009), range(2019, self.end_year)
        )
        self.assertNoHolidayName(name_2019, range(self.start_year, 2019))
        obs_dts_2009 = (
            "2013-09-23",
            "2014-09-22",
        )
        self.assertHolidayName(f"{name_2009} (observed)", obs_dts_2009)
        obs_dts_2019 = (
            "2019-09-23",
            "2024-09-23",
            "2025-09-22",
        )
        self.assertHolidayName(f"{name_2019} (observed)", obs_dts_2019)
        self.assertNoNonObservedHoliday(obs_dts_2009, obs_dts_2019)

    def test_farmers_day(self):
        name = "Farmer's Day"
        self.assertHolidayName(
            name,
            "2020-12-04",
            "2021-12-03",
            "2022-12-02",
            "2023-12-01",
            "2024-12-06",
            "2025-12-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2011-12-27",
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
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Eid ul-Fitr"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_adha(self):
        name = "Eid ul-Adha"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2016-09-12",
            "2019-08-12",
            "2022-07-11",
            "2024-06-17",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-07", "Constitution Day"),
            ("2023-01-09", "Constitution Day (observed)"),
            ("2023-03-06", "Independence Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "May Day"),
            ("2023-04-21", "Eid ul-Fitr (estimated)"),
            ("2023-06-28", "Eid ul-Adha (estimated)"),
            ("2023-08-04", "Founders' Day"),
            ("2023-09-21", "Kwame Nkrumah Memorial Day"),
            ("2023-12-01", "Farmer's Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-01-07", "Constitution Day"),
            ("2024-01-08", "Constitution Day (observed)"),
            ("2024-03-06", "Independence Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "May Day"),
            ("2024-04-10", "Eid ul-Fitr (estimated)"),
            ("2024-06-16", "Eid ul-Adha (estimated)"),
            ("2024-06-17", "Eid ul-Adha (observed, estimated)"),
            ("2024-08-04", "Founders' Day"),
            ("2024-08-05", "Founders' Day (observed)"),
            ("2024-09-21", "Kwame Nkrumah Memorial Day"),
            ("2024-09-23", "Kwame Nkrumah Memorial Day (observed)"),
            ("2024-12-06", "Farmer's Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
