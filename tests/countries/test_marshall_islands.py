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

import warnings
from unittest import TestCase

from holidays.countries.marshall_islands import HolidaysMH, MH, MHL
from tests.common import CommonCountryTests


class TestMH(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysMH)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore")

    def test_country_aliases(self):
        self.assertAliases(HolidaysMH, MH, MHL)

    def test_2020(self):
        # http://web.archive.org/web/20201125072002/https://www.pscrmi.net/rmi-holiday-memos
        self.assertHolidays(
            HolidaysMH(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-03-01", "Nuclear Victims Remembrance Day"),
            ("2020-03-02", "Nuclear Victims Remembrance Day Holiday"),
            ("2020-04-10", "Good Friday"),
            ("2020-05-01", "Constitution Day"),
            ("2020-07-03", "Fisherman's Day"),
            ("2020-09-04", "Dri-jerbal Day"),
            ("2020-09-25", "Manit Day"),
            ("2020-11-17", "President's Day"),
            ("2020-12-04", "Gospel Day"),
            ("2020-12-25", "Christmas Day"),
        )

    def test_2021(self):
        # http://web.archive.org/web/20210617163816/https://www.pscrmi.net/rmi-holiday-memos
        self.assertHolidays(
            HolidaysMH(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-03-01", "Nuclear Victims Remembrance Day"),
            ("2021-04-02", "Good Friday"),
            ("2021-05-01", "Constitution Day"),
            ("2021-07-02", "Fisherman's Day"),
            ("2021-09-03", "Dri-jerbal Day"),
            ("2021-09-24", "Manit Day"),
            ("2021-11-17", "President's Day"),
            ("2021-12-03", "Gospel Day"),
            ("2021-12-24", "Christmas Day"),
        )

    def test_2022(self):
        # http://web.archive.org/web/20220704021442/https://www.pscrmi.net/rmi-holiday-memos
        self.assertHolidays(
            HolidaysMH(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-03-01", "Nuclear Victims Remembrance Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Constitution Day"),
            ("2022-05-02", "Constitution Day Holiday"),
            ("2022-07-01", "Fisherman's Day"),
            ("2022-09-02", "Dri-jerbal Day"),
            ("2022-09-30", "Manit Day"),
            ("2022-11-17", "President's Day"),
            ("2022-12-02", "Gospel Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day Holiday"),
        )

    def test_2023(self):
        # https://web.archive.org/web/20230628074915/https://www.pscrmi.net/rmi-holiday-memos
        self.assertHolidays(
            HolidaysMH(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day Holiday"),
            ("2023-03-01", "Nuclear Victims Remembrance Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "Constitution Day"),
            ("2023-07-07", "Fisherman's Day"),
            ("2023-09-01", "Dri-jerbal Day"),
            ("2023-09-29", "Manit Day"),
            ("2023-11-17", "President's Day"),
            ("2023-11-20", "General Election Day"),
            ("2023-12-01", "Gospel Day"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_special_holidays(self):
        self.assertHoliday(
            # General Election are held on the 3rd Monday of November
            # see https://en.wikipedia.org/wiki/Elections_in_the_Marshall_Islands
            "1995-11-20",
            "1999-11-22",
            "2003-11-17",
            "2007-11-19",
            "2011-11-21",
            "2015-11-16",
            "2019-11-18",
            "2023-11-20",
        )

    def test_not_observed(self):
        self.assertNoNonObservedHoliday(
            "2020-03-02",
            "2022-05-02",
            "2022-12-26",
            "2023-01-02",
        )
