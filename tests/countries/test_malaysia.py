#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import APR, AUG, DEC, FEB, JAN, JUL, JUN, MAR, MAY, NOV, OCT, SEP
from holidays.countries.malaysia import Malaysia, MY, MYS
from tests.common import CommonCountryTests


class TestMalaysia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Malaysia)

    def test_country_aliases(self):
        self.assertAliases(Malaysia, MY, MYS)
        holidays1 = MY()
        holidays2 = MYS()
        self.assertEqual(list(holidays1), list(holidays2))

    def test_malaysia_wikipedia(self):
        # reproduce table at
        # https://en.wikipedia.org/wiki/Public_holidays_in_Malaysia
        # as of 19-Sep-21
        columns = (
            "JHR",  # "Johor"
            "KDH",  # "Kedah"
            "KTN",  # "Kelantan"
            "KUL",  # "FT Kuala Lumpur"
            "LBN",  # "FT Labuan"
            "MLK",  # "Malacca"
            "NSN",  # "Negeri Sembilan"
            "PHG",  # "Pahang"
            "PNG",  # "Penang"
            "PRK",  # "Perak"
            "PLS",  # "Perlis"
            "PJY",  # "FT Putrajaya"
            "SBH",  # "Sabah"
            "SWK",  # "Sarawak"
            "SGR",  # "Selangor"
            "TRG",  # "Terengganu"
        )
        rows = (
            (
                date(2021, JAN, 1),
                (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0),
            ),
            (
                date(2021, JAN, 14),
                (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, JAN, 28),
                (1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0),
            ),
            (
                date(2021, FEB, 1),
                (0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
            ),
            (
                date(2021, FEB, 12),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, FEB, 13),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, FEB, 14),
                (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            ),
            (
                date(2021, MAR, 4),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            ),
            (
                date(2021, MAR, 11),
                (0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1),
            ),
            (
                date(2021, MAR, 23),
                (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, APR, 2),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0),
            ),
            (
                date(2021, APR, 13),
                (1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, APR, 15),
                (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, APR, 26),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            ),
            (
                date(2021, APR, 29),
                (0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1),
            ),
            (
                date(2021, MAY, 1),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, MAY, 2),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            ),
            (
                date(2021, MAY, 13),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, MAY, 14),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, MAY, 16),
                (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, MAY, 22),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, MAY, 26),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, MAY, 30),
                (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
            ),
            (
                date(2021, MAY, 31),
                (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
            ),
            (
                date(2021, JUN, 1),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
            ),
            (
                date(2021, JUN, 2),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
            ),
            (
                date(2021, JUN, 7),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, JUN, 20),
                (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, JUL, 7),
                (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, JUL, 10),
                (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, JUL, 17),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, JUL, 19),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            ),
            (
                date(2021, JUL, 20),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, JUL, 21),
                (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1),
            ),
            (
                date(2021, JUL, 22),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
            ),
            (
                date(2021, JUL, 30),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, AUG, 10),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, AUG, 24),
                (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, AUG, 31),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, SEP, 13),
                (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, SEP, 16),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, OCT, 2),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
            ),
            (
                date(2021, OCT, 9),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
            ),
            (
                date(2021, OCT, 19),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, NOV, 4),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1),
            ),
            (
                date(2021, NOV, 5),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, NOV, 11),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, NOV, 12),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ),
            (
                date(2021, DEC, 3),
                (0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
            ),
            (
                date(2021, DEC, 11),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
            ),
            (
                date(2021, DEC, 24),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
            ),
            (
                date(2021, DEC, 25),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            ),
            (
                date(2021, DEC, 26),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            ),
        )

        for col, state in enumerate(columns):
            my_holidays = Malaysia(years=2021, subdiv=state)
            # check if all holidays are in here
            for dt, is_holiday in rows:
                if is_holiday[col]:
                    self.assertIn(dt, my_holidays)
                else:
                    self.assertNotIn(dt, my_holidays)

    def test_malaysia(self):
        # Federal Public Holidays
        # https://www.timeanddate.com/holidays/malaysia/2001
        self.assertHolidayDates(
            "2001-01-24",
            "2001-01-25",
            "2001-03-06",
            "2001-03-26",
            "2001-05-01",
            "2001-05-07",
            "2001-06-02",
            "2001-06-04",
            "2001-08-31",
            "2001-11-14",
            "2001-12-17",
            "2001-12-18",
            "2001-12-25",
        )

    def test_special_holidays(self):
        self.assertHoliday(
            "1999-11-29",
            "2018-05-09",
            "2019-07-30",
        )

    def test_observed(self):
        dt = (
            "2012-02-06",
            "2012-08-21",
            "2012-09-17",
            "2013-02-12",
            "2014-09-01",
            "2014-10-06",
            "2015-05-04",
            "2016-05-02",
            "2016-12-26",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_JHR_holidays(self):
        state_holidays = Malaysia(subdiv="JHR")
        self.assertHoliday(
            state_holidays,
            # Birthday of the Sultan of Johor
            "2015-03-23",
            "2018-03-23",
            "2020-03-23",
            "2022-03-23",
            # Hari Hol of Sultan Iskandar of Johor
            "2018-10-15",
            "2019-10-05",
            "2020-09-24",
            "2021-09-13",
            "2022-09-03",
            "2023-08-22",
            # Thaipusam
            "2018-01-31",
            "2019-01-21",
            "2020-02-08",
            "2021-01-28",
            "2022-01-18",
            "2023-02-05",
            # Beginning of Ramadan
            "2018-05-17",
            "2019-05-06",
            "2020-04-24",
            "2021-04-13",
            "2022-04-03",
            "2023-03-23",
            # Labour Day Holiday
            "2022-05-04",
        )
        self.assertNoHoliday(
            state_holidays,
            # Birthday of the Sultan of Johor
            "2014-03-23",
            # Hari Hol of Sultan Iskandar of Johor
            "2010-01-21",
            # Malaysia Day (in lieu)
            "2018-09-17",
        )
        dt = (
            "2017-09-03",
            "2017-12-03",
            "2018-02-18",
            "2018-06-17",
            "2018-09-02",
            "2020-04-26",
            "2020-05-03",
            "2020-08-02",
            "2020-12-27",
            "2021-02-14",
            "2021-05-16",
            "2022-09-18",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_KDH_holidays(self):
        state_holidays = Malaysia(subdiv="KDH")
        self.assertHoliday(
            state_holidays,
            # Hari Raya Haji
            "2006-12-31",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
            # Hari Raya Haji Holiday
            "2007-01-01",
            "2018-08-23",
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-11",
            "2023-06-30",
            # Isra and Mi'raj
            "2018-04-14",
            "2019-04-03",
            "2020-03-22",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            # Beginning of Ramadan
            "2018-05-17",
            "2019-05-06",
            "2020-04-24",
            "2021-04-13",
            "2022-04-03",
            "2023-03-23",
            # Thaipusam in 2022
            "2022-01-18",
        )
        self.assertNoHoliday(
            state_holidays,
            # Malaysia Day (in lieu)
            "2018-09-17",
        )
        dt = (
            "2017-09-03",
            "2017-12-03",
            "2018-02-18",
            "2018-06-17",
            "2018-09-02",
            "2020-04-26",
            "2020-05-03",
            "2020-08-02",
            "2020-12-27",
            "2021-02-14",
            "2021-05-16",
            "2022-09-18",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_KTN_holidays(self):
        state_holidays = Malaysia(subdiv="KTN")
        self.assertHoliday(
            state_holidays,
            # Birthday of the Sultan of Kelantan
            "2018-11-11",
            "2019-11-12",
            "2020-11-11",
            # Hari Raya Haji
            "2006-12-31",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
            # Hari Raya Haji Holiday
            "2007-01-01",
            "2018-08-23",
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-11",
            "2023-06-30",
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            "2023-04-09",  # In lieu
            # Labour Day Holiday
            "2022-05-04",
        )
        self.assertNoHoliday(
            state_holidays,
            # Birthday of the Sultan of Kelantan
            "2001-11-11",
            # Malaysia Day (in lieu)
            "2018-09-17",
        )
        dt = (
            "2017-01-30",
            "2017-06-04",
            "2017-09-03",
            "2017-09-17",
            "2018-02-18",
            "2018-06-03",
            "2018-06-17",
            "2019-11-10",
            "2020-01-27",
            "2020-08-02",
            "2020-11-15",
            "2021-02-14",
            "2021-05-02",
            "2021-12-26",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_NSN_holidays(self):
        state_holidays = Malaysia(subdiv="NSN")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Isra and Mi'raj
            "2018-04-14",
            "2019-04-03",
            "2020-03-22",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            # Birthday of the Sultan of Negeri Sembilan
            "2018-01-14",
            "2023-01-14",
            # Thaipusam
            "2018-01-31",
            "2019-01-21",
            "2020-02-08",
            "2021-01-28",
            "2022-01-18",
            "2023-02-05",
        )
        self.assertNoHoliday(
            state_holidays,
            # Birthday of the Sultan of Negeri Sembilan
            "2008-01-14",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-01-15",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-03-23",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_PNG_holidays(self):
        state_holidays = Malaysia(subdiv="PNG")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            # Thaipusam
            "2018-01-31",
            "2019-01-21",
            "2020-02-08",
            "2021-01-28",
            "2022-01-18",
            "2023-02-05",
            "2023-02-06",  # In lieu
            # George Town Heritage Day
            "2009-07-07",
            "2020-07-07",
            # Birthday of the Governor of Penang
            "2017-07-08",
            "2019-07-13",
            "2020-07-11",
            "2022-07-09",
            "2023-07-08",
        )
        self.assertNoHoliday(
            state_holidays,
            # George Town Heritage Day
            "2008-07-07",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-07-08",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-11",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_PRK_holidays(self):
        state_holidays = Malaysia(subdiv="PRK")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            # Thaipusam
            "2018-01-31",
            "2019-01-21",
            "2020-02-08",
            "2021-01-28",
            "2022-01-18",
            "2023-02-05",
            "2023-02-06",  # In lieu
            # Birthday of the Sultan of Perak
            "2009-11-27",
            "2017-11-27",
            "2018-11-02",
            "2019-11-01",
            "2020-11-06",
            "2021-11-05",
            "2022-11-04",
        )
        self.assertNoHoliday(
            state_holidays,
            # Birthday of the Sultan of Perak
            "2018-11-27",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-11",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_SBH_holidays(self):
        state_holidays = Malaysia(subdiv="SBH")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Pesta Kaamatan
            "2018-05-30",
            "2019-05-31",
            # Good Friday
            "2018-03-30",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            # Birthday of the Governor of Sabah
            "2017-10-07",
            "2018-10-06",
            "2019-10-05",
            "2020-10-03",
            # Christmas Eve
            "2019-12-24",
            "2020-12-24",
        )
        self.assertNoHoliday(
            state_holidays,
            # Christmas Eve
            "2018-12-24",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_SWK_holidays(self):
        state_holidays = Malaysia(subdiv="SWK")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Good Friday
            "2018-03-30",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            # Gawai Dayak
            "2018-06-01",
            "2018-06-02",
            "2020-06-02",
            "2020-06-02",
            # Birthday of the Governor of Sarawak
            "2018-10-13",
            "2019-10-12",
            "2020-10-10",
            "2021-10-09",
            "2022-10-08",
            # Sarawak Day
            "2017-07-22",
            "2018-07-22",
            "2022-07-22",
        )
        self.assertNoHoliday(
            state_holidays,
            # Sarawak Day
            "2014-07-22",
            # Deepavali
            "2018-11-06",
            "2022-10-24",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-07-23",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-06-04",
            "2019-08-12",
            "2020-01-27",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_SGR_holidays(self):
        state_holidays = Malaysia(subdiv="SGR")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            # Thaipusam
            "2018-01-31",
            "2019-01-21",
            "2020-02-08",
            "2021-01-28",
            "2022-01-18",
            "2023-02-05",
            "2023-02-06",  # In lieu
            # Birthday of The Sultan of Selangor
            "2018-12-11",
            "2019-12-11",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-11",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-12",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_TRG_holidays(self):
        state_holidays = Malaysia(subdiv="TRG")
        self.assertHoliday(
            state_holidays,
            # Arafat Day
            "2018-08-21",
            "2019-08-10",
            "2020-07-30",
            "2021-07-19",
            "2022-07-09",
            "2023-06-28",
            # Hari Raya Haji
            "2006-12-31",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
            # Hari Raya Haji Holiday
            "2007-01-01",
            "2018-08-23",
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-11",
            "2023-06-30",
            # Isra and Mi'raj
            "2020-03-22",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2023-02-19",  # In lieu
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            "2023-04-09",  # In lieu
            # Anniversary of the Installation of the Sultan of Terengganu
            "2000-03-04",
            "2018-03-04",
            "2019-03-04",
            # Birthday of the Sultan of Terengganu
            "2020-04-26",
            "2022-04-26",
            # Labour Day Holiday
            "2022-05-04",
        )
        self.assertNoHoliday(
            state_holidays,
            # Isra and Mi'raj
            "2018-04-14",
            "2019-04-03",
            # Anniversary of the Installation of the Sultan of Terengganu
            "1999-03-04",
            # Birthday of the Sultan of Terengganu
            "1999-04-26",
            # Malaysia Day (in lieu)
            "2018-09-17",
        )
        dt = (
            "2017-01-30",
            "2017-03-05",
            "2017-06-04",
            "2017-09-03",
            "2017-09-17",
            "2018-02-18",
            "2018-06-03",
            "2018-06-17",
            "2019-08-13",
            "2019-11-10",
            "2020-01-27",
            "2020-08-02",
            "2020-11-15",
            "2021-02-14",
            "2021-05-02",
            "2021-12-26",
            "2022-07-12",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_KUL_holidays(self):
        state_holidays = Malaysia(subdiv="KUL")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Federal Territory Day
            "2018-02-01",
            "2019-02-01",
            # Thaipusam
            "2018-01-31",
            "2019-01-21",
            "2020-02-08",
            "2021-01-28",
            "2022-01-18",
            "2023-02-05",
            # Malaysia Cup Holiday
            "2021-12-03",
        )
        self.assertNoHoliday(
            state_holidays,
            # Federal Territory Day
            "1970-02-01",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-11",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_MLK_holidays(self):
        state_holidays = Malaysia(subdiv="MLK")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Beginning of Ramadan
            "2018-05-17",
            "2019-05-06",
            "2020-04-24",
            "2021-04-13",
            "2022-04-03",
            "2023-03-23",
            # Declaration of Malacca as a Historical City
            "2018-04-15",
            "2019-04-15",
            # Birthday of the Governor of Malacca
            "2018-10-12",
            "2019-10-11",
            "2020-08-24",
            "2021-08-24",
            "2022-08-24",
        )
        self.assertNoHoliday(
            state_holidays,
            # Declaration of Malacca as a Historical City
            "1985-04-15",
            # Birthday of the Governor of Malacca
            "2019-08-24",
            "2020-10-09",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-04-16",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-26",
            "2022-04-04",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_LBN_holidays(self):
        state_holidays = Malaysia(subdiv="LBN")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Federal Territory Day
            "2020-02-01",
            "2022-02-01",
            # Pesta Kaamatan
            "2018-05-30",
            "2019-05-31",
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            # Malaysia Cup Holiday
            "2021-12-03",
        )
        self.assertNoHoliday(
            state_holidays,
            # Federal Territory Day
            "1970-02-01",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-11",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_PHG_holidays(self):
        state_holidays = Malaysia(subdiv="PHG")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            # Hari Hol of Pahang
            "2001-05-07",
            "2018-05-07",
            "2019-05-07",
            "2020-05-07",
            "2021-05-22",
            "2022-05-22",
        )
        self.assertNoHoliday(
            state_holidays,
            # Hari Hol of Pahang
            "2010-05-22",
            "2021-05-07",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-05-08",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-11",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-05-23",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_PLS_holidays(self):
        state_holidays = Malaysia(subdiv="PLS")
        self.assertHoliday(
            state_holidays,
            # Hari Raya Haji
            "2006-12-31",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
            # Hari Raya Haji Holiday
            "2007-01-01",
            "2018-08-23",
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-11",
            "2023-06-30",
            # Isra and Mi'raj
            "2018-04-14",
            "2019-04-03",
            "2020-03-22",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            # Birthday of The Raja of Perlis
            "2000-05-17",
            "2010-05-17",
            "2017-05-17",
            "2018-07-17",
            "2022-07-17",
        )
        self.assertNoHoliday(
            state_holidays,
            # Birthday of The Raja of Perlis
            "2017-07-17",
            "2018-05-17",
        )
        dt = (
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-13",
            "2019-10-28",
            "2020-01-27",
            "2020-03-23",
            "2020-05-11",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-12",
            "2022-07-18",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_PJY_holidays(self):
        state_holidays = Malaysia(subdiv="PJY")
        self.assertHoliday(
            state_holidays,
            # New Year's Day
            "2018-01-01",
            "2020-01-01",
            "2022-01-01",
            "2023-01-02",  # In lieu
            # Nuzul Al-Quran Day
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            # Thaipusam
            "2018-01-31",
            "2019-01-21",
            "2020-02-08",
            "2021-01-28",
            "2022-01-18",
            "2023-02-05",
            "2023-02-06",  # In lieu
            # Federal Territory Day
            "2018-02-01",
            "2019-02-01",
            # Malaysia Cup Holiday
            "2021-12-03",
        )
        self.assertNoHoliday(
            state_holidays,
            # Federal Territory Day
            "1970-02-01",
        )
        dt = (
            "2017-01-02",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2019-10-28",
            "2020-01-27",
            "2020-05-11",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            # special case
            "2007-01-02",
        )
        self.assertHoliday(state_holidays, dt)

        state_holidays.observed = False
        self.assertNoNonObservedHoliday(state_holidays, dt)

    def test_2024(self):
        self.assertHolidays(
            Malaysia(years=2024),
            ("2024-02-10", "Chinese New Year"),
            ("2024-04-11", "Second day of Hari Raya Puasa"),
            ("2024-10-31", "Deepavali"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-22", "Vesak Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-07-07", "Awal Muharram (Hijri New Year)"),
            ("2024-02-11", "Chinese New Year Holiday"),
            ("2024-06-03", "Birthday of SPB Yang di-Pertuan Agong"),
            ("2024-08-31", "National Day"),
            ("2024-04-10", "Hari Raya Puasa"),
            ("2024-06-17", "Hari Raya Haji"),
            ("2024-09-16", "Malaysia Day; Maulidur Rasul (Birthday of the Prophet Muhammad)"),
            ("2024-02-12", "Chinese New Year Holiday (in lieu)"),
        )
