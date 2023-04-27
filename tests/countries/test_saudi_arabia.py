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

from holidays.countries.saudi_arabia import SaudiArabia, SA, SAU
from tests.common import TestCase


class TestSaudiArabia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaudiArabia, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(SaudiArabia, SA, SAU)

    def test_special_holidays(self):
        self.assertHoliday("2022-11-23")

    def test_2021(self):
        self.assertHolidayDates(
            SaudiArabia(years=2021),
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2021-05-16",
            "2021-05-17",
            "2021-05-18",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2021-09-23",
        )

    def test_weekends(self):
        # Weekend changed from (Thursday, Friday) to
        # (Friday, Saturday) at 2013
        # September 23rd, 2010 was Thursday (Weekend)
        # so, observed is Wednesday
        self.assertHoliday("2010-09-22", "2010-09-23")
        self.assertNoHoliday("2010-09-24")

        # September 23rd, 2006 was Friday (Weekend)
        # so, observed is Saturday
        self.assertHoliday("2005-09-23", "2005-09-24")
        self.assertNoHoliday("2005-09-22")

        # September 23rd, 2006 was Saturday (Weekday before 2013)
        self.assertHoliday("2006-09-23")
        self.assertNoHoliday("2006-09-22", "2006-09-24")

    def test_national_day(self):
        self.assertHoliday(f"{year}-09-23" for year in range(2005, 2050))
        self.assertNoHolidayNameInYears(
            "National Day Holiday", range(1950, 2005)
        )

    def test_national_day_observed(self):
        dt = (
            "2005-09-24",
            "2010-09-22",
            "2011-09-24",
            "2016-09-22",
            "2017-09-24",
            "2022-09-22",
            "2023-09-24",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_day_overlaps_hijri_holiday(self):
        for dt in (
            "2009-09-23",
            "2015-09-23",
            "2048-09-23",
            "2074-09-23",
        ):
            self.assertNotIn("National Day Holiday", self.holidays[dt])

    def test_founding_day(self):
        self.assertHoliday(f"{year}-02-22" for year in range(2022, 2050))
        self.assertNoHolidayNameInYears(
            "Founding Day Holiday", range(1950, 2022)
        )

    def test_founding_day_observed(self):
        dt = (
            "2025-02-23",
            "2030-02-21",
            "2031-02-23",
            "2036-02-21",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_founding_day_overlaps_hijri_holiday(self):
        self.assertNotIn("National Day Holiday", self.holidays["2061-02-22"])

    def test_hijri_based(self):
        self.assertHoliday(
            # eid al-fitr
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2021-05-16",
            # eid al-adha
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            # eid al-fitr
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2022-05-05",
            # eid al-adha
            "2022-07-08",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
        )

    def test_hijri_based_observed(self):
        dt = (
            # observed eid al-fitr
            "2018-06-19",
            "2018-06-20",
            "2019-06-08",
            "2021-05-17",
            "2021-05-18",
            "2023-04-25",
            "2023-04-26",
            # osbserved eid al-adha
            "2001-01-01",  # special case
            "2019-08-14",
            "2020-08-03",
            "2020-08-04",
            "2022-07-12",
            "2022-07-13",
            "2023-07-01",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_hijri_based_with_two_holidays_in_one_year(self):
        self.assertHoliday(
            # eid al-fitr 1 (hijri year 1420)
            "2000-01-08",
            "2000-01-09",
            "2000-01-10",
            "2000-01-11",
            # eid al-fitr 2 (hijri year 1421)
            "2000-12-27",
            "2000-12-28",
            "2000-12-29",
            "2000-12-30",
            # eid al-adha 1 (hijri year 1426)
            "2006-01-09",
            "2006-01-10",
            "2006-01-11",
            "2006-01-12",
            # eid al-adha 2 (hijri year 1427)
            "2006-12-30",
            "2006-12-31",
        )
