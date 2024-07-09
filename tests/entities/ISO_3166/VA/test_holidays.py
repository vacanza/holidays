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

from holidays.entities.ISO_3166.VA import VaHolidays
from tests.common import CommonCountryTests


class TestVaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(VaHolidays, years=range(1970, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(VaHolidays(years=1928))

    def test_solemnity_of_mary_day(self):
        self.assertHolidayName(
            "Solemnity of Mary Day", (f"{year}-01-01" for year in range(1970, 2050))
        )

    def test_epiphany(self):
        self.assertHolidayName("Epiphany", (f"{year}-01-06" for year in range(1970, 2050)))

    def test_lateran_treaty_day(self):
        self.assertHolidayName(
            "Lateran Treaty Day", (f"{year}-02-11" for year in range(1970, 2050))
        )

    def test_anniversary_election_of_holy_father(self):
        name = "Anniversary of the Election of the Holy Father"
        self.assertHolidayName(name, (f"{year}-10-16" for year in range(1978, 2005)))
        self.assertHolidayName(name, (f"{year}-04-19" for year in range(2005, 2013)))
        self.assertHolidayName(name, (f"{year}-03-13" for year in range(2013, 2050)))
        self.assertNoHolidayName(name, range(1970, 1978))

    def test_saint_josephs_day(self):
        self.assertHolidayName(
            "Saint Joseph's Day", (f"{year}-03-19" for year in range(1970, 2050))
        )

    def test_easter_sunday(self):
        self.assertHolidayName(
            "Easter Sunday",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Easter Monday",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_saint_georges_day(self):
        name = "Saint George's Day"
        self.assertHolidayName(name, (f"{year}-04-23" for year in range(2013, 2050)))
        self.assertNoHolidayName(name, range(1970, 2013))

    def test_ascension(self):
        name = "Ascension of Christ"
        self.assertHolidayName(
            name,
            "2000-06-01",
            "2001-05-24",
            "2002-05-09",
            "2003-05-29",
            "2004-05-20",
            "2005-05-05",
            "2006-05-25",
            "2007-05-17",
            "2008-05-01",
            "2009-05-21",
        )
        self.assertNoHolidayName(name, range(2010, 2050))

    def test_corpus_christi(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "2000-06-22",
            "2001-06-14",
            "2002-05-30",
            "2003-06-19",
            "2004-06-10",
            "2005-05-26",
            "2006-06-15",
            "2007-06-07",
            "2008-05-22",
            "2009-06-11",
        )
        self.assertNoHolidayName(name, range(2010, 2050))

    def test_saint_joseph_workers_day(self):
        name = "Saint Joseph the Worker's Day"
        self.assertNoHolidayName(name, VaHolidays(years=1954))
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1955, 2050)))

    def test_saints_peter_and_paul_day(self):
        self.assertHolidayName(
            "Saint Peter and Saint Paul's Day", (f"{year}-06-29" for year in range(1970, 2050))
        )

    def test_assumption_day(self):
        self.assertHolidayName("Assumption Day", (f"{year}-08-15" for year in range(1970, 2050)))

    def test_nativity_of_mary_day(self):
        self.assertHolidayName(
            "Nativity of Mary Day", (f"{year}-09-08" for year in range(1970, 2050))
        )

    def test_all_saints_day(self):
        self.assertHolidayName("All Saints' Day", (f"{year}-11-01" for year in range(1970, 2050)))

    def test_saint_charles_borromeo_day(self):
        name = "Saint Charles Borromeo Day"
        self.assertHolidayName(name, (f"{year}-11-04" for year in range(1978, 2005)))
        self.assertNoHolidayName(name, range(1970, 1978), range(2005, 2050))

    def test_immaculate_conception_day(self):
        self.assertHolidayName(
            "Immaculate Conception Day", (f"{year}-12-08" for year in range(1970, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1970, 2050)))

    def test_saint_stephens_day(self):
        self.assertHolidayName(
            "Saint Stephen's Day", (f"{year}-12-26" for year in range(1970, 2050))
        )

    def test_2022(self):
        self.assertHolidays(
            VaHolidays(years=2022),
            ("2022-01-01", "Solemnity of Mary Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-02-11", "Lateran Treaty Day"),
            ("2022-03-13", "Anniversary of the Election of the Holy Father"),
            ("2022-03-19", "Saint Joseph's Day"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-23", "Saint George's Day"),
            ("2022-05-01", "Saint Joseph the Worker's Day"),
            ("2022-06-29", "Saint Peter and Saint Paul's Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-08", "Nativity of Mary Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
        )

    def test_2023(self):
        self.assertHolidays(
            VaHolidays(years=2023),
            ("2023-01-01", "Solemnity of Mary Day"),
            ("2023-01-06", "Epiphany"),
            ("2023-02-11", "Lateran Treaty Day"),
            ("2023-03-13", "Anniversary of the Election of the Holy Father"),
            ("2023-03-19", "Saint Joseph's Day"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-23", "Saint George's Day"),
            ("2023-05-01", "Saint Joseph the Worker's Day"),
            ("2023-06-29", "Saint Peter and Saint Paul's Day"),
            ("2023-08-15", "Assumption Day"),
            ("2023-09-08", "Nativity of Mary Day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-12-08", "Immaculate Conception Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Saint Stephen's Day"),
        )
