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

from datetime import date

from holidays.countries.singapore import Singapore, SG, SGP
from tests.common import TestCase


class TestSingapore(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Singapore)

    def test_country_aliases(self):
        self.assertCountryAliases(Singapore, SG, SGP)

    def test_common(self):
        self.assertNonObservedHolidayName("New Year's Day", "2022-01-01")

    def test_Singapore(self):
        # <= 1968 holidays
        self.assertIn(date(1968, 4, 13), self.holidays)
        self.assertIn(date(1968, 4, 15), self.holidays)
        self.assertIn(date(1968, 12, 26), self.holidays)
        # latest polling day
        self.assertIn(date(2015, 9, 11), self.holidays)
        # Year with lunar leap month
        self.assertIn(date(2015, 8, 7), self.holidays)
        # holidays estimated using lunar calendar
        self.assertIn(date(2050, 6, 4), self.holidays)  # Vesak Day
        self.assertIn(date(2050, 11, 12), self.holidays)  # Deepavali

    def test_hijri_holidays(self):
        # holidays estimated using library hijri-converter
        # <= 1968 holidays
        self.assertIn(date(1968, 1, 2), self.holidays)
        # > 2022
        self.assertIn(date(2050, 6, 20), self.holidays)  # Hari Raya Puasa
        self.assertIn(date(2050, 8, 28), self.holidays)  # Hari Raya Haji
        # twice in a Gregorian calendar year
        self.assertIn(date(2006, 1, 10), self.holidays)
        self.assertIn(date(2006, 12, 31), self.holidays)
        # special rare case (Hari Raya Haji from 2006)
        self.assertIn(date(2007, 1, 2), self.holidays)

    # Latest holidays
    # Source: https://www.mom.gov.sg/employment-practices/public-holidays
    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 2, 16), self.holidays)
        self.assertIn(date(2018, 2, 17), self.holidays)
        self.assertIn(date(2018, 3, 30), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 29), self.holidays)
        self.assertIn(date(2018, 6, 15), self.holidays)
        self.assertIn(date(2018, 8, 9), self.holidays)
        self.assertIn(date(2018, 8, 22), self.holidays)
        self.assertIn(date(2018, 11, 6), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        # 2018: total holidays (11 + 0 falling on a Sunday)
        self.assertEqual(len(Singapore(years=[2018])), 11 + 0)

    def test_2019(self):
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 2, 5), self.holidays)
        self.assertIn(date(2019, 2, 6), self.holidays)
        self.assertIn(date(2019, 4, 19), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 19), self.holidays)
        self.assertIn(date(2019, 5, 20), self.holidays)
        self.assertIn(date(2019, 6, 5), self.holidays)
        self.assertIn(date(2019, 8, 9), self.holidays)
        self.assertIn(date(2019, 8, 11), self.holidays)
        self.assertIn(date(2019, 8, 12), self.holidays)
        self.assertIn(date(2019, 10, 27), self.holidays)
        self.assertIn(date(2019, 10, 28), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
        self.assertEqual(len(Singapore(years=[2019])), 14)

    def test_2020(self):
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 25), self.holidays)
        self.assertIn(date(2020, 1, 26), self.holidays)
        self.assertIn(date(2020, 1, 27), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 5, 7), self.holidays)
        self.assertIn(date(2020, 5, 24), self.holidays)
        self.assertIn(date(2020, 5, 25), self.holidays)
        self.assertIn(date(2020, 7, 10), self.holidays)
        self.assertIn(date(2020, 7, 31), self.holidays)
        self.assertIn(date(2020, 8, 9), self.holidays)
        self.assertIn(date(2020, 8, 10), self.holidays)
        self.assertIn(date(2020, 11, 14), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertEqual(len(Singapore(years=[2020])), 15)

    def test_2021(self):
        self.assertIn(date(2021, 1, 1), self.holidays)
        self.assertIn(date(2021, 2, 12), self.holidays)
        self.assertIn(date(2021, 2, 13), self.holidays)
        self.assertIn(date(2021, 4, 2), self.holidays)
        self.assertIn(date(2021, 5, 1), self.holidays)
        self.assertIn(date(2021, 5, 13), self.holidays)
        self.assertIn(date(2021, 5, 26), self.holidays)
        self.assertIn(date(2021, 7, 20), self.holidays)
        self.assertIn(date(2021, 8, 9), self.holidays)
        self.assertIn(date(2021, 11, 4), self.holidays)
        self.assertIn(date(2021, 12, 25), self.holidays)
        self.assertEqual(len(Singapore(years=[2021])), 11)

    def test_2022(self):
        self.assertIn(date(2022, 1, 1), self.holidays)
        self.assertIn(date(2022, 2, 1), self.holidays)
        self.assertIn(date(2022, 2, 2), self.holidays)
        self.assertIn(date(2022, 4, 15), self.holidays)
        self.assertIn(date(2022, 5, 1), self.holidays)
        self.assertIn(date(2022, 5, 2), self.holidays)
        self.assertIn(date(2022, 5, 3), self.holidays)
        self.assertIn(date(2022, 5, 15), self.holidays)
        self.assertIn(date(2022, 5, 16), self.holidays)
        self.assertIn(date(2022, 7, 10), self.holidays)
        self.assertIn(date(2022, 7, 11), self.holidays)
        self.assertIn(date(2022, 8, 9), self.holidays)
        self.assertIn(date(2022, 10, 24), self.holidays)
        self.assertIn(date(2022, 12, 25), self.holidays)
        self.assertIn(date(2022, 12, 26), self.holidays)
        # 2022: total holidays (11 + 4 falling on a Sunday)
        self.assertEqual(len(Singapore(years=[2022])), 11 + 4)

    def test_2023(self):
        self.assertIn(date(2023, 1, 1), self.holidays)
        self.assertIn(date(2023, 1, 2), self.holidays)
        self.assertIn(date(2023, 1, 22), self.holidays)
        self.assertIn(date(2023, 1, 23), self.holidays)
        self.assertIn(date(2023, 1, 24), self.holidays)
        self.assertIn(date(2023, 4, 7), self.holidays)
        self.assertIn(date(2023, 4, 22), self.holidays)
        self.assertIn(date(2023, 5, 1), self.holidays)
        self.assertIn(date(2023, 6, 2), self.holidays)
        self.assertIn(date(2023, 6, 29), self.holidays)
        self.assertIn(date(2023, 8, 9), self.holidays)
        self.assertIn(date(2023, 9, 1), self.holidays)
        self.assertIn(date(2023, 11, 12), self.holidays)
        self.assertIn(date(2023, 11, 13), self.holidays)
        self.assertIn(date(2023, 12, 25), self.holidays)
        # 2023: total holidays (11 + 3 falling on a Sunday + Polling Day)
        self.assertEqual(len(Singapore(years=[2023])), 11 + 3 + 1)

    def test_non_observed(self):
        self.assertNotIn(date(2023, 1, 2), Singapore(observed=False, years=2023))

    def test_special_holidays(self):
        self.assertIn(date(2015, 8, 7), self.holidays)
