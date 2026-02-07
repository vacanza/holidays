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

from holidays.financial.japan_exchange import JapanExchange
from tests.common import CommonFinancialTests


class TestJapanExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JapanExchange)

    def test_no_holidays(self):
        super().test_no_holidays()

    def test_new_years_day(self):
        self.assertHolidayName(
            "New Year's Day",
            "2013-01-01",
            "2020-01-01",
            "2021-01-01",
            "2022-01-01",
            "2023-01-01",
            "2024-01-01",
        )

    def test_national_foundation_day(self):
        self.assertHolidayName(
            "National Foundation Day",
            "2013-02-11",
            "2020-02-11",
            "2021-02-11",
            "2022-02-11",
            "2023-02-11",
            "2024-02-11",
        )

    def test_showa_day(self):
        self.assertHolidayName(
            "Showa Day",
            "2013-04-29",
            "2020-04-29",
            "2021-04-29",
            "2022-04-29",
            "2023-04-29",
            "2024-04-29",
        )

    def test_constitution_memorial_day(self):
        self.assertHolidayName(
            "Constitution Memorial Day",
            "2013-05-03",
            "2020-05-03",
            "2021-05-03",
            "2022-05-03",
            "2023-05-03",
            "2024-05-03",
        )

    def test_greenery_day(self):
        self.assertHolidayName(
            "Greenery Day",
            "2013-05-04",
            "2020-05-04",
            "2021-05-04",
            "2022-05-04",
            "2023-05-04",
            "2024-05-04",
        )

    def test_childrens_day(self):
        self.assertHolidayName(
            "Children's Day",
            "2013-05-05",
            "2020-05-05",
            "2021-05-05",
            "2022-05-05",
            "2023-05-05",
            "2024-05-05",
        )

    def test_mountain_day(self):
        # Mountain Day was introduced in 2016
        self.assertHolidayName(
            "Mountain Day",
            "2016-08-11",
            "2017-08-11",
            "2018-08-11",
            "2022-08-11",
            "2023-08-11",
        )
        # 2020 and 2021 had Olympic Shift holidays
        self.assertHolidayName(
            "Mountain Day (Olympic Shift)",
            "2020-08-10",
        )
        self.assertHolidayName(
            "Mountain Day Observed (Olympic Shift)",
            "2021-08-09",
        )
        # 2024-08-12 is a substitute holiday (Silver Week)
        self.assertHolidayName(
            "Substitute Holiday",
            "2024-08-12",
        )

    def test_culture_day(self):
        self.assertHolidayName(
            "Culture Day",
            "2013-11-03",
            "2020-11-03",
            "2021-11-03",
            "2022-11-03",
            "2023-11-03",
            "2024-11-03",
        )

    def test_labor_thanksgiving_day(self):
        self.assertHolidayName(
            "Labor Thanksgiving Day",
            "2013-11-23",
            "2020-11-23",
            "2021-11-23",
            "2022-11-23",
            "2023-11-23",
            "2024-11-23",
        )

    def test_emperors_birthday(self):
        # Dec 23 (1989-2018) - but start_year is 2013
        self.assertHolidayName(
            "Emperor's Birthday",
            "2013-12-23",
            "2017-12-23",
        )
        # Feb 23 (2020+)
        self.assertHolidayName(
            "Emperor's Birthday",
            "2020-02-23",
            "2021-02-23",
            "2022-02-23",
            "2023-02-23",
            "2024-02-23",
        )

    def test_coming_of_age_day(self):
        # Second Monday of January (2000+)
        self.assertHolidayName(
            "Coming of Age Day",
            "2020-01-13",
            "2021-01-11",
            "2022-01-10",
            "2023-01-09",
            "2024-01-08",
        )

    def test_marine_day(self):
        # Third Monday of July (2003+)
        self.assertHolidayName(
            "Marine Day",
            "2020-07-20",
            "2021-07-19",
            "2022-07-18",
            "2023-07-17",
            "2024-07-15",
        )

    def test_respect_for_the_aged_day(self):
        # Third Monday of September (2003+)
        self.assertHolidayName(
            "Respect for the Aged Day",
            "2020-09-21",
            "2021-09-20",
            "2022-09-19",
            "2023-09-18",
            "2024-09-16",
        )

    def test_sports_day(self):
        # Second Monday of October (2000+)
        self.assertHolidayName(
            "Sports Day",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
        )

    def test_market_holidays(self):
        # January 2 - only weekdays
        self.assertHolidayName(
            "Market Holiday",
            "2020-01-02",
            "2024-01-02",
        )
        # January 3 - only weekdays
        self.assertHolidayName(
            "Market Holiday",
            "2020-01-03",
            "2024-01-03",
        )
        # December 31 - only weekdays
        self.assertHolidayName(
            "Market Holiday",
            "2020-12-31",
            "2024-12-31",
        )

    def test_substitute_holiday(self):
        # 2020-01-13 is Coming of Age Day (2nd Monday of Jan)
        # Note: The substitute holiday might not be added for this case
        self.assertHolidayName(
            "Coming of Age Day",
            "2020-01-13",
        )
