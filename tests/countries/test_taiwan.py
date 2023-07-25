#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.taiwan import Taiwan, TW, TWN
from tests.common import TestCase


class TestTaiwan(TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1990, 2030)
        super().setUpClass(Taiwan, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertCountryAliases(Taiwan, TW, TWN)

    def test_no_holidays(self):
        self.assertNoHolidays(Taiwan(years=1911))

    def test_new_years_day(self):
        name = "Republic of China Founding Day / New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1990, 2030)))

        obs_dt = (
            "2017-01-02",
            "2021-12-31",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_lunar_new_year(self):
        name_eve = "Lunar New Year's Eve"
        name = "Lunar New Year"
        name_hol = "Lunar New Year Holiday"
        self.assertHolidayName(
            name_eve,
            "2011-02-02",
            "2012-01-22",
            "2013-02-09",
            "2014-01-30",
            "2015-02-18",
            "2016-02-07",
            "2017-01-27",
            "2018-02-15",
            "2019-02-04",
            "2020-01-24",
            "2021-02-11",
            "2022-01-31",
            "2023-01-21",
        )

        self.assertHolidayName(
            name,
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
        )

        self.assertHolidayName(
            name_hol,
            "2015-02-20",
            "2015-02-21",
            "2016-02-09",
            "2016-02-10",
            "2017-01-29",
            "2017-01-30",
            "2018-02-17",
            "2018-02-18",
            "2019-02-06",
            "2019-02-07",
            "2020-01-26",
            "2020-01-27",
            "2021-02-13",
            "2021-02-14",
            "2022-02-02",
            "2022-02-03",
            "2023-01-23",
            "2023-01-24",
        )

        obs_dt = (
            "2015-02-23",
            "2016-02-11",
            "2017-01-31",
            "2017-02-01",
            "2018-02-19",
            "2018-02-20",
            "2020-01-28",
            "2020-01-29",
            "2021-02-15",
            "2021-02-16",
            "2023-01-25",
            "2023-01-26",
        )
        self.assertHolidayName(name_hol, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_peace_memorial_day(self):
        name = "Peace Memorial Day"
        self.assertHolidayName(name, (f"{year}-02-28" for year in range(1997, 2030)))
        self.assertNoHoliday(f"{year}-02-28" for year in range(1990, 1997))
        self.assertNoHolidayName(name, range(1990, 1997))

        obs_dt = (
            "2015-02-27",
            "2016-02-29",
            "2021-03-01",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_childrens_day(self):
        name = "Children's Day"
        self.assertHolidayName(name, (f"{year}-04-04" for year in range(1990, 2000)))
        self.assertHolidayName(name, (f"{year}-04-04" for year in range(2011, 2030)))
        self.assertNoHolidayName(name, range(2000, 2011))
        self.assertNoHolidayName(name, Taiwan(years=1989))

        obs_dt = (
            "2015-04-03",
            "2020-04-03",
            "2021-04-05",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_tomb_sweeping_day(self):
        name = "Tomb Sweeping Day"
        self.assertHolidayName(
            name,
            "2011-04-05",
            "2012-04-04",
            "2013-04-04",
            "2014-04-05",
            "2015-04-05",
            "2016-04-04",
            "2017-04-04",
            "2018-04-05",
            "2019-04-05",
            "2020-04-04",
            "2021-04-04",
            "2022-04-05",
            "2023-04-05",
        )
        self.assertNoHolidayName(name, Taiwan(years=1971))

        obs_dt = (
            "2015-04-06",
            "2020-04-02",
            "2021-04-06",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_dragon_boat_festival(self):
        name = "Dragon Boat Festival"
        self.assertHolidayName(
            name,
            "2011-06-06",
            "2012-06-23",
            "2013-06-12",
            "2014-06-02",
            "2015-06-20",
            "2016-06-09",
            "2017-05-30",
            "2018-06-18",
            "2019-06-07",
            "2020-06-25",
            "2021-06-14",
            "2022-06-03",
            "2023-06-22",
        )

        obs_dt = (
            "2015-06-19",
            "2025-05-30",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_mid_autumn_festival(self):
        name = "Mid-Autumn Festival"
        self.assertHolidayName(
            name,
            "2011-09-12",
            "2012-09-30",
            "2013-09-19",
            "2014-09-08",
            "2015-09-27",
            "2016-09-15",
            "2017-10-04",
            "2018-09-24",
            "2019-09-13",
            "2020-10-01",
            "2021-09-21",
            "2022-09-10",
            "2023-09-29",
        )

        obs_dt = (
            "2015-09-28",
            "2022-09-09",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_day(self):
        name = "National Day"
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(1990, 2030)))

        obs_dt = (
            "2015-10-09",
            "2020-10-09",
            "2021-10-11",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_2022(self):
        self.assertHolidays(
            Taiwan(years=2022),
            ("2022-01-01", "Republic of China Founding Day / New Year's Day"),
            ("2022-01-31", "Lunar New Year's Eve"),
            ("2022-02-01", "Lunar New Year"),
            ("2022-02-02", "Lunar New Year Holiday"),
            ("2022-02-03", "Lunar New Year Holiday"),
            ("2022-02-28", "Peace Memorial Day"),
            ("2022-04-04", "Children's Day"),
            ("2022-04-05", "Tomb Sweeping Day"),
            ("2022-06-03", "Dragon Boat Festival"),
            ("2022-09-09", "Mid-Autumn Festival (Observed)"),
            ("2022-09-10", "Mid-Autumn Festival"),
            ("2022-10-10", "National Day"),
        )
