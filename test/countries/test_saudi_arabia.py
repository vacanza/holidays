#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import importlib.util
import unittest
from datetime import date

import holidays


class TestSaudiArabia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.SA(observed=True)

    def test_2020(self):
        # Eid al-Fitr Holiday
        # (skipping 14, and 15 because they are weekends)
        self.assertIn(date(2021, 5, 12), self.holidays)
        self.assertIn(date(2021, 5, 13), self.holidays)
        self.assertIn(date(2021, 5, 16), self.holidays)
        self.assertIn(date(2021, 5, 17), self.holidays)
        # Eid al-Fitr Holiday
        self.assertIn(date(2021, 7, 19), self.holidays)
        self.assertIn(date(2021, 7, 20), self.holidays)
        self.assertIn(date(2021, 7, 21), self.holidays)
        self.assertIn(date(2021, 7, 22), self.holidays)
        # National day holiday
        self.assertIn(date(2021, 9, 23), self.holidays)

    def test_weekends(self):
        # Weekend changed from (Thursday, Friday) to
        # (Friday, Saturday) at 2013
        # September 23rd, 2010 was Thursday (Weekend)
        # so, observed is Wednesday
        self.assertIn(date(2010, 9, 22), self.holidays)
        self.assertIn(date(2010, 9, 23), self.holidays)
        self.assertNotIn(date(2010, 9, 24), self.holidays)

        # September 23rd, 2006 was Friday (Weekend)
        # so, observed is Saturday
        self.assertNotIn(date(2005, 9, 22), self.holidays)
        self.assertIn(date(2005, 9, 23), self.holidays)
        self.assertIn(date(2005, 9, 24), self.holidays)

        # September 23rd, 2006 was Saturday (Weekday before 2013)
        self.assertNotIn(date(2006, 9, 22), self.holidays)
        self.assertIn(date(2006, 9, 23), self.holidays)
        self.assertNotIn(date(2006, 9, 24), self.holidays)

    def test_national_day(self):
        self.assertIn(date(2020, 9, 23), self.holidays)
        # National day started as a holiday on 2005
        self.assertNotIn(date(2004, 9, 23), self.holidays)
        self.assertIn(date(2005, 9, 23), self.holidays)

    def test_national_day_observed(self):
        # September 23rd, 2016 was Friday (Weekend)
        # so, observed is Thursday
        self.assertIn(date(2016, 9, 22), self.holidays)
        self.assertIn(date(2016, 9, 23), self.holidays)
        self.assertNotIn(date(2016, 9, 24), self.holidays)

        # September 23rd, 2017 was Saturday (Weekend)
        # so, observed is Sunday
        self.assertNotIn(date(2017, 9, 22), self.holidays)
        self.assertIn(date(2017, 9, 23), self.holidays)
        self.assertIn(date(2017, 9, 24), self.holidays)

    def test_national_day_not_observed(self):
        self.holidays.observed = False
        self.assertNotIn(date(2016, 9, 22), self.holidays)
        self.assertNotIn(date(2017, 9, 24), self.holidays)

    def test_national_day_overlaps_hijri_holiday(self):
        # Eid al-Fitr Holiday is on the same day as the
        # national day, so there is no extra holidays given for it.
        self.assertIn(date(2074, 2, 22), self.holidays)

    def test_founding_day(self):
        self.assertIn(date(2022, 2, 22), self.holidays)
        self.assertIn(date(2030, 2, 22), self.holidays)
        # founding day started as a holiday on 2022
        self.assertNotIn(date(2021, 2, 22), self.holidays)
        self.assertNotIn(date(2005, 2, 22), self.holidays)

    def test_founding_day_observed(self):
        # February 22nd, 2030 is Friday (Weekend)
        # so, observed is Thursday
        self.assertIn(date(2030, 2, 21), self.holidays)
        self.assertIn(date(2030, 2, 22), self.holidays)
        self.assertNotIn(date(2016, 2, 23), self.holidays)

        # February 22nd, 2031 is Saturday (Weekend)
        # so, observed is Sunday
        self.assertNotIn(date(2031, 2, 21), self.holidays)
        self.assertIn(date(2031, 2, 22), self.holidays)
        self.assertIn(date(2031, 2, 23), self.holidays)

    def test_founding_day_not_observed(self):
        self.holidays.observed = False
        self.assertNotIn(date(2030, 2, 21), self.holidays)
        self.assertNotIn(date(2031, 2, 23), self.holidays)

    def test_founding_day_overlaps_hijri_holiday(self):
        # Eid al-Fitr Holiday is on the same day as the
        # founding day, so there is no extra holidays given for it.
        self.assertIn(date(2061, 2, 22), self.holidays)

    def test_hijri_based(self):
        if importlib.util.find_spec("hijri_converter"):
            self.holidays = holidays.SA(years=[2020, 2022])
            # eid al-fitr
            self.assertIn(date(2022, 5, 1), self.holidays)
            self.assertIn(date(2022, 5, 2), self.holidays)
            self.assertIn(date(2022, 5, 3), self.holidays)
            self.assertIn(date(2022, 5, 4), self.holidays)

            # eid al-adha
            self.assertIn(date(2022, 7, 10), self.holidays)
            self.assertIn(date(2022, 7, 11), self.holidays)
            self.assertIn(date(2022, 7, 12), self.holidays)
            self.assertIn(date(2022, 7, 13), self.holidays)

            # eid al-fitr
            self.assertIn(date(2020, 5, 23), self.holidays)
            self.assertIn(date(2020, 5, 24), self.holidays)
            self.assertIn(date(2020, 5, 25), self.holidays)
            self.assertIn(date(2020, 5, 26), self.holidays)

            # eid al-adha
            self.assertIn(date(2020, 7, 30), self.holidays)
            self.assertIn(date(2020, 7, 31), self.holidays)
            self.assertIn(date(2020, 8, 1), self.holidays)
            self.assertIn(date(2020, 8, 2), self.holidays)

    def test_hijri_based_observed(self):
        if importlib.util.find_spec("hijri_converter"):
            self.holidays = holidays.SA(years=range(2019, 2023))
            # observed eid al-fitr
            self.assertIn(date(2020, 5, 27), self.holidays)

            self.assertIn(date(2019, 6, 8), self.holidays)

            # osbserved eid al-adha
            self.assertIn(date(2022, 7, 12), self.holidays)
            self.assertIn(date(2022, 7, 13), self.holidays)

            self.assertIn(date(2020, 8, 3), self.holidays)
            self.assertIn(date(2020, 8, 4), self.holidays)

            # self.assertIn(date(2017, 8, 3), self.holidays)
            # self.assertIn(date(2017, 8, 4), self.holidays)

            # self.assertIn(date(2019, 8, 13), self.holidays)
            # self.assertIn(date(2019, 8, 14), self.holidays)

            # self.assertIn(date(2017, 8, 6), self.holidays)

    def test_hijri_based_not_observed(self):
        if importlib.util.find_spec("hijri_converter"):
            self.holidays = holidays.SA(observed=False, years=range(2014, 2021))
            # observed eid al-fitr
            self.assertNotIn(date(2020, 5, 27), self.holidays)

            self.assertNotIn(date(2016, 7, 10), self.holidays)
            self.assertNotIn(date(2016, 7, 11), self.holidays)

            self.assertNotIn(date(2018, 6, 18), self.holidays)
            self.assertNotIn(date(2018, 6, 19), self.holidays)

            self.assertNotIn(date(2019, 6, 9), self.holidays)

            # osbserved eid al-adha
            self.assertNotIn(date(2014, 10, 8), self.holidays)

            self.assertNotIn(date(2017, 8, 3), self.holidays)
            self.assertNotIn(date(2017, 8, 4), self.holidays)

            # self.assertNotIn(date(2019, 8, 13), self.holidays)
            self.assertNotIn(date(2019, 8, 14), self.holidays)

            self.assertNotIn(date(2017, 8, 6), self.holidays)

    def test_hijri_based_with_two_holidays_in_one_year(self):
        """
        Note: this might be required change if weekend changes
        took effect in the holiday.SA class (weekend changed
        on June 28th, 2013), from (Thursdays and Fridays) to
        (Fridays, Saturdays).
        Currently, using newest weekend days (Fridays, and Saturdays)
        """
        if importlib.util.find_spec("hijri_converter"):
            self.holidays = holidays.SA(years=[2006])
            # eid_alfitr
            # 23rd is a weekend day (Saturday), so there
            # is a one day shift
            self.assertIn(date(2006, 10, 23), self.holidays)
            self.assertIn(date(2006, 10, 24), self.holidays)
            self.assertIn(date(2006, 10, 25), self.holidays)
            self.assertIn(date(2006, 10, 26), self.holidays)
            # eid al-adha 1 (hijri year 1426)
            self.assertIn(date(2006, 1, 9), self.holidays)
            self.assertIn(date(2006, 1, 10), self.holidays)
            self.assertIn(date(2006, 1, 11), self.holidays)
            self.assertIn(date(2006, 1, 12), self.holidays)
            # eid al-adha 2 (hijri year 1427)
            # The remaining holidays fall in the next year 2007
            self.assertIn(date(2006, 12, 31), self.holidays)
