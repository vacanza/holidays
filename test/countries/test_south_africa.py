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

import unittest

import holidays


class TestSouthAfrica(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ZA()

    def test_new_years(self):
        self.assertNotIn("1908-01-01", self.holidays)
        self.assertIn("1910-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday

    def test_easter(self):
        self.assertIn("2017-04-14", self.holidays)
        self.assertIn("2017-04-17", self.holidays)
        self.assertIn("1994-04-01", self.holidays)

    def test_static(self):
        self.assertIn("2004-08-09", self.holidays)

    def test_not_holiday(self):
        self.assertNotIn("2016-12-28", self.holidays)
        self.assertNotIn("2015-03-02", self.holidays)

    def test_special_holidays(self):
        self.assertIn("1999-06-02", self.holidays)
        self.assertIn("1999-12-31", self.holidays)  # Y2K
        self.assertIn("2000-01-02", self.holidays)  # Y2K
        self.assertIn("2004-04-14", self.holidays)
        self.assertIn("2006-03-01", self.holidays)
        self.assertIn("2008-05-02", self.holidays)
        self.assertIn("2009-04-22", self.holidays)
        self.assertIn("2011-05-18", self.holidays)
        self.assertIn("2011-12-27", self.holidays)
        self.assertIn("2014-05-07", self.holidays)
        self.assertIn("2016-08-03", self.holidays)
        self.assertIn("2019-05-08", self.holidays)
        self.assertIn("2021-11-01", self.holidays)
        self.assertIn("2022-12-27", self.holidays)

    def test_presidential(self):
        self.assertIn("2008-05-02", self.holidays)
        self.assertIn("2011-12-27", self.holidays)
        self.assertIn("2016-12-27", self.holidays)

    def test_observed(self):
        self.assertIn("1995-01-02", self.holidays)
        self.assertIn("1995-09-25", self.holidays)
        self.assertIn("1996-06-17", self.holidays)
        self.assertIn("1997-04-28", self.holidays)
        self.assertIn("1998-08-10", self.holidays)
        self.assertIn("1999-03-22", self.holidays)
        self.assertIn("1999-12-27", self.holidays)
        self.assertIn("2000-01-03", self.holidays)
        self.assertIn("2005-05-02", self.holidays)
        self.assertIn("2010-12-27", self.holidays)
        self.assertIn("2014-04-28", self.holidays)
        self.assertIn("2017-01-02", self.holidays)
        self.assertIn("2019-06-17", self.holidays)
        self.assertIn("2020-08-10", self.holidays)
        self.assertIn("2021-03-22", self.holidays)
        self.assertIn("2021-12-27", self.holidays)
        self.assertIn("2022-05-02", self.holidays)

    def test_historic(self):
        self.assertIn("1980-05-31", self.holidays)  # Union/Republic Day
        self.assertNotIn("2018-05-31", self.holidays)

        self.assertIn("1952-12-16", self.holidays)  # Day of the Vow
        self.assertIn("1987-05-01", self.holidays)  # Workers' Day
        self.assertIn("1988-05-06", self.holidays)  # Workers' Day
        self.assertIn("1961-07-10", self.holidays)  # Family Day

        # "Queen's Birthday"
        self.assertIn("1952-07-14", self.holidays)
        self.assertIn("1954-07-12", self.holidays)
        self.assertIn("1955-07-11", self.holidays)
        self.assertIn("1956-07-09", self.holidays)
        self.assertIn("1957-07-08", self.holidays)
        self.assertIn("1958-07-14", self.holidays)
        self.assertIn("1959-07-13", self.holidays)
        self.assertIn("1960-07-11", self.holidays)
        self.assertIn("1953-07-13", self.holidays)
        self.assertNotIn("1951-07-09", self.holidays)

        # King's Birthday
        self.assertIn("1910-08-01", self.holidays)
        self.assertIn("1921-08-01", self.holidays)
        self.assertIn("1922-08-07", self.holidays)
        self.assertIn("1941-08-04", self.holidays)
        self.assertIn("1947-08-04", self.holidays)
        self.assertIn("1951-08-06", self.holidays)
        self.assertNotIn("1952-08-04", self.holidays)

        # Settler's Day
        self.assertIn("1952-09-01", self.holidays)
        self.assertIn("1959-09-07", self.holidays)
        self.assertIn("1965-09-06", self.holidays)
        self.assertIn("1975-09-01", self.holidays)
        self.assertIn("1979-09-03", self.holidays)
        self.assertNotIn("1951-09-03", self.holidays)
        self.assertNotIn("1980-09-01", self.holidays)

    def test_elections(self):
        self.assertIn("1999-06-02", self.holidays)  # Election Day 1999
        self.assertIn("2004-04-14", self.holidays)  # Election Day 2004
        self.assertIn("2006-03-01", self.holidays)  # Local Election
        self.assertIn("2009-04-22", self.holidays)  # Election Day 2008
        self.assertIn("2011-05-18", self.holidays)  # Election Day 2011
        self.assertIn("2014-05-07", self.holidays)  # Election Day 2014
        self.assertIn("2016-08-03", self.holidays)  # Election Day 2016
        self.assertIn("2019-05-08", self.holidays)  # Election Day 2019
        self.assertIn("2021-11-01", self.holidays)  # Election Day 2019
