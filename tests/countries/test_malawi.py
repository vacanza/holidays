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

from holidays.countries.malawi import Malawi
from tests.common import CommonCountryTests


class TestMalawi(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Malawi)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_john_chilembwe_day(self):
        name = "John Chilembwe Day"
        self.assertHolidayName(name, (f"{year}-01-15" for year in self.full_range))
        obs_dts = (
            "2011-01-17",
            "2012-01-16",
            "2017-01-16",
            "2022-01-17",
            "2023-01-16",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_martyrs_day(self):
        name = "Martyrs Day"
        self.assertHolidayName(name, (f"{year}-03-03" for year in self.full_range))
        obs_dts = (
            "2012-03-05",
            "2013-03-04",
            "2018-03-05",
            "2019-03-04",
            "2024-03-04",
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

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_kamuzu_day(self):
        name = "Kamuzu Day"
        self.assertHolidayName(name, (f"{year}-05-14" for year in self.full_range))
        obs_dts = (
            "2011-05-16",
            "2016-05-16",
            "2017-05-15",
            "2022-05-16",
            "2023-05-15",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-07-06" for year in self.full_range))
        obs_dts = (
            "2013-07-08",
            "2014-07-07",
            "2019-07-08",
            "2024-07-08",
            "2025-07-07",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_mothers_day(self):
        name = "Mother's Day"
        self.assertHolidayName(name, (f"{year}-10-15" for year in self.full_range))
        obs_dts = (
            "2011-10-17",
            "2016-10-17",
            "2017-10-16",
            "2022-10-17",
            "2023-10-16",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2010-12-27",
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

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-15", "John Chilembwe Day"),
            ("2022-01-17", "John Chilembwe Day (observed)"),
            ("2022-03-03", "Martyrs Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-05-14", "Kamuzu Day"),
            ("2022-05-16", "Kamuzu Day (observed)"),
            ("2022-07-06", "Independence Day"),
            ("2022-10-15", "Mother's Day"),
            ("2022-10-17", "Mother's Day (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
