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

from holidays.countries.cameroon import Cameroon
from tests.common import CommonCountryTests


class TestCameroon(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Cameroon)

    def test_special_holidays(self):
        self.assertHoliday("2021-05-14", "2021-07-19")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_youth_day(self):
        name = "Youth Day"
        self.assertHolidayName(name, (f"{year}-02-11" for year in range(1966, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1966))
        obs_dts = (
            "2018-02-12",
            "2024-02-12",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2016-05-02",
            "2022-05-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_day(self):
        name = "National Day"
        self.assertHolidayName(name, (f"{year}-05-20" for year in range(1972, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1972))
        obs_dts = (
            "2012-05-21",
            "2018-05-21",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_assumption_day(self):
        name = "Assumption Day"
        self.assertHolidayName(name, (f"{year}-08-15" for year in self.full_range))
        obs_dts = (
            "2010-08-16",
            "2021-08-16",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2012-08-20",
            "2020-05-25",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2007-01-02",  # special case
            "2014-10-06",
            "2019-08-12",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_prophets_birthday(self):
        name = "Mawlid"
        self.assertHolidayName(
            name,
            "2018-11-21",
            "2019-11-10",
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2012-02-06",
            "2019-11-11",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2022(self):
        self.assertHolidays(
            Cameroon(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-02-11", "Youth Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-03", "Labour Day (observed)"),
            ("2022-05-20", "National Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-08", "Mawlid"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )
