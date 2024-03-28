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

from holidays.countries.singapore import Singapore, SG, SGP
from tests.common import CommonCountryTests


class TestSingapore(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Singapore)

    def test_country_aliases(self):
        self.assertAliases(Singapore, SG, SGP)

    def test_common(self):
        self.assertNonObservedHolidayName("New Year's Day", "2022-01-01")

    def test_singapore(self):
        self.assertHoliday(
            # <= 1968 holidays
            "1968-04-13",
            "1968-04-15",
            "1968-12-26",
            # latest polling day
            "2015-09-11",
            # Year with lunar leap month
            "2015-08-07",
            # holidays estimated using lunar calendar
            "2050-06-04",  # Vesak Day
            "2050-11-12",  # Deepavali
        )

    def test_hijri_holidays(self):
        self.assertHoliday(
            # <= 1968 holidays
            "1968-01-02",
            # > 2022
            "2050-06-20",  # Hari Raya Puasa
            "2050-08-28",  # Hari Raya Haji
            # twice in a Gregorian calendar year
            "2006-01-10",
            "2006-12-31",
            # special rare case (Hari Raya Haji from 2006)
            "2007-01-02",
        )

    # Source: https://www.mom.gov.sg/employment-practices/public-holidays
    def test_2018(self):
        self.assertHolidays(
            ("2018-01-01", "New Year's Day"),
            ("2018-02-16", "Chinese New Year"),
            ("2018-02-17", "Chinese New Year"),
            ("2018-03-30", "Good Friday"),
            ("2018-05-01", "Labour Day"),
            ("2018-05-29", "Vesak Day"),
            ("2018-06-15", "Hari Raya Puasa"),
            ("2018-08-09", "National Day"),
            ("2018-08-22", "Hari Raya Haji"),
            ("2018-11-06", "Deepavali"),
            ("2018-12-25", "Christmas Day"),
        )

    def test_2019(self):
        self.assertHolidays(
            ("2019-01-01", "New Year's Day"),
            ("2019-02-05", "Chinese New Year"),
            ("2019-02-06", "Chinese New Year"),
            ("2019-04-19", "Good Friday"),
            ("2019-05-01", "Labour Day"),
            ("2019-05-19", "Vesak Day"),
            ("2019-05-20", "Vesak Day (observed)"),
            ("2019-06-05", "Hari Raya Puasa"),
            ("2019-08-09", "National Day"),
            ("2019-08-11", "Hari Raya Haji"),
            ("2019-08-12", "Hari Raya Haji (observed)"),
            ("2019-10-27", "Deepavali"),
            ("2019-10-28", "Deepavali (observed)"),
            ("2019-12-25", "Christmas Day"),
        )

    def test_2020(self):
        self.assertHolidays(
            ("2020-01-01", "New Year's Day"),
            ("2020-01-25", "Chinese New Year"),
            ("2020-01-26", "Chinese New Year"),
            ("2020-01-27", "Chinese New Year (observed)"),
            ("2020-04-10", "Good Friday"),
            ("2020-05-01", "Labour Day"),
            ("2020-05-07", "Vesak Day"),
            ("2020-05-24", "Hari Raya Puasa"),
            ("2020-05-25", "Hari Raya Puasa (observed)"),
            ("2020-07-10", "Polling Day"),
            ("2020-07-31", "Hari Raya Haji"),
            ("2020-08-09", "National Day"),
            ("2020-08-10", "National Day (observed)"),
            ("2020-11-14", "Deepavali"),
            ("2020-12-25", "Christmas Day"),
        )

    def test_2021(self):
        self.assertHolidays(
            ("2021-01-01", "New Year's Day"),
            ("2021-02-12", "Chinese New Year"),
            ("2021-02-13", "Chinese New Year"),
            ("2021-04-02", "Good Friday"),
            ("2021-05-01", "Labour Day"),
            ("2021-05-13", "Hari Raya Puasa"),
            ("2021-05-26", "Vesak Day"),
            ("2021-07-20", "Hari Raya Haji"),
            ("2021-08-09", "National Day"),
            ("2021-11-04", "Deepavali"),
            ("2021-12-25", "Christmas Day"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-01", "Chinese New Year"),
            ("2022-02-02", "Chinese New Year"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-05-03", "Hari Raya Puasa"),
            ("2022-05-15", "Vesak Day"),
            ("2022-05-16", "Vesak Day (observed)"),
            ("2022-07-10", "Hari Raya Haji"),
            ("2022-07-11", "Hari Raya Haji (observed)"),
            ("2022-08-09", "National Day"),
            ("2022-10-24", "Deepavali"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-22", "Chinese New Year"),
            ("2023-01-23", "Chinese New Year"),
            ("2023-01-24", "Chinese New Year (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-22", "Hari Raya Puasa"),
            ("2023-05-01", "Labour Day"),
            ("2023-06-02", "Vesak Day"),
            ("2023-06-29", "Hari Raya Haji"),
            ("2023-08-09", "National Day"),
            ("2023-09-01", "Polling Day"),
            ("2023-11-12", "Deepavali"),
            ("2023-11-13", "Deepavali (observed)"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-02-10", "Chinese New Year"),
            ("2024-02-11", "Chinese New Year"),
            ("2024-02-12", "Chinese New Year (observed)"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-10", "Hari Raya Puasa"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-22", "Vesak Day"),
            ("2024-06-17", "Hari Raya Haji"),
            ("2024-08-09", "National Day"),
            ("2024-10-31", "Deepavali"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_non_observed(self):
        self.assertNoNonObservedHoliday("2023-01-02")

    def test_special_holidays(self):
        self.assertHoliday("2015-08-07")
