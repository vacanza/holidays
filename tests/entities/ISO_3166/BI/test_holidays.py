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

from unittest import TestCase

from holidays.entities.ISO_3166.BI import BiHolidays
from tests.common import CommonCountryTests


class TestBurundi(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BiHolidays, years=range(1962, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(BiHolidays(years=1961))

    def test_new_year_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1962, 2050)))

    def test_unity_day(self):
        name = "Unity Day"
        self.assertNoHolidayName(name, range(1962, 1992))
        self.assertHolidayName(name, (f"{year}-02-05" for year in range(1992, 2050)))

    def test_ntaryamira_day(self):
        name = "President Ntaryamira Day"
        self.assertNoHolidayName(name, range(1962, 1995))
        self.assertHolidayName(name, (f"{year}-04-06" for year in range(1995, 2050)))

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(1962, 2050)))

    def test_ascension_day(self):
        self.assertHolidayName(
            "Ascension Day",
            "2010-05-13",
            "2011-06-02",
            "2012-05-17",
            "2013-05-09",
            "2014-05-29",
            "2015-05-14",
            "2016-05-05",
            "2017-05-25",
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
        )

    def test_nkurunziza_day(self):
        name = "President Nkurunziza Day"
        self.assertNoHolidayName(name, range(1962, 2022))
        self.assertHolidayName(name, (f"{year}-06-08" for year in range(2022, 2050)))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-07-01" for year in range(1962, 2050)))

    def test_assumption_day(self):
        self.assertHolidayName("Assumption Day", (f"{year}-08-15" for year in range(1962, 2050)))

    def test_rwagasore_day(self):
        self.assertHolidayName(
            "Prince Louis Rwagasore Day", (f"{year}-10-13" for year in range(1962, 2050))
        )

    def test_ndadaye_day(self):
        name = "President Ndadaye's Day"
        self.assertNoHolidayName(name, range(1962, 1994))
        self.assertHolidayName(name, (f"{year}-10-21" for year in range(1994, 2050)))

    def test_all_saints_day(self):
        self.assertHolidayName("All Saints' Day", (f"{year}-11-01" for year in range(1962, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1962, 2050)))

    def test_eid_ul_fitr(self):
        self.assertHolidayName(
            "Eid ul Fitr (estimated)",
            "2010-09-10",
            "2011-08-30",
            "2012-08-19",
            "2013-08-08",
            "2014-07-28",
            "2015-07-17",
            "2016-07-06",
            "2017-06-25",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
        )

    def test_eid_al_adha(self):
        self.assertHolidayName(
            "Eid al Adha (estimated)",
            "2010-11-16",
            "2011-11-06",
            "2012-10-26",
            "2013-10-15",
            "2014-10-04",
            "2015-09-23",
            "2016-09-11",
            "2017-09-01",
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
        )

    def test_observed(self):
        observed_holidays = (
            # New Year's Day
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            # Unity Day
            "2012-02-06",
            "2017-02-06",
            "2023-02-06",
            # President Ntaryamira Day
            "2008-04-07",
            "2014-04-07",
            "2025-04-07",
            # Labour Day
            "2011-05-02",
            "2016-05-02",
            "2033-05-02",
            # President Nkurunziza Day
            "2025-06-09",
            "2031-06-09",
            "2036-06-09",
            # Independence Day
            "2012-07-02",
            "2018-07-02",
            "2029-07-02",
            # Assumption Day
            "2010-08-16",
            "2021-08-16",
            "2027-08-16",
            # Prince Louis Rwagasore Day
            "2013-10-14",
            "2019-10-14",
            "2024-10-14",
            # President Ndadaye's Day
            "2012-10-22",
            "2018-10-22",
            "2029-10-22",
            # All Saints' Day
            "2015-11-02",
            "2020-11-02",
            "2026-11-02",
            # Christmas Day
            "2016-12-26",
            "2022-12-26",
            "2033-12-26",
            # Eid ul Fitr
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
            # Eid al Adha
            "2016-09-12",
            "2019-08-12",
            "2024-06-17",
        )
        self.assertHoliday(observed_holidays)
        self.assertNoNonObservedHoliday(observed_holidays)
