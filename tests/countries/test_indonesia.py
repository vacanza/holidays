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

from holidays.countries.indonesia import Indonesia, ID, IDN
from tests.common import TestCase


class TestIndonesia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Indonesia, years=range(2000, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Indonesia, ID, IDN)

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(2000, 2050))

    def test_lunar_new_year(self):
        name = "Tahun Baru Imlek"
        self.assertHolidayName(
            name,
            "2005-02-09",
            "2006-01-30",
            "2007-02-19",
            "2008-02-07",
            "2009-01-26",
            "2010-02-15",
            "2011-02-03",
            "2012-01-23",
            "2013-02-11",
            "2014-01-31",
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
        )
        self.assertNoHolidayName(name, Indonesia(years=2002))

    def test_day_of_silence(self):
        name = "Hari Suci Nyepi"
        self.assertHolidayName(
            name,
            "2009-03-26",
            "2014-03-31",
            "2018-03-17",
            "2020-03-25",
            "2021-03-14",
            "2022-03-03",
        )
        self.assertNoHolidayName(name, Indonesia(years=1982))

    def test_labor_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1953, 1969))
        self.assertHoliday(f"{year}-05-01" for year in range(2014, 2050))
        self.assertNoHoliday("1952-05-01", "1969-05-01", "2013-05-01")
        self.assertNoHolidayName("Hari Buruh Internasional", Indonesia(years=(1952, 1969, 2013)))

    def test_pancasila_day(self):
        self.assertHoliday(f"{year}-06-01" for year in range(2017, 2050))
        self.assertNoHoliday("2016-06-01")
        self.assertNoHolidayName("Hari Lahir Pancasila", range(2000, 2017))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-08-17" for year in range(2000, 2050))

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(2000, 2050))

    def test_easter(self):
        # Good Friday
        self.assertHoliday(
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

        # Ascension Day
        self.assertHoliday(
            "2000-06-01",
            "2010-05-13",
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
        )

    def test_islamic_holidays(self):
        self.assertHoliday(
            # Eid al-Fitr
            "2001-12-16",
            "2001-12-17",
            "2011-08-30",
            "2011-08-31",
            "2018-06-15",
            "2018-06-16",
            "1991-04-15",
            "1991-04-16",
            "1996-02-19",
            "1996-02-20",
            "1999-01-18",
            "1999-01-19",
            # Eid al-Adha
            "2001-03-06",
            "2011-11-06",
            "2018-08-22",
            "1991-06-22",
            "1996-04-27",
            "1999-03-27",
            # Islamic New Year
            "2001-03-26",
            "2011-11-27",
            "2018-09-11",
            "1991-07-12",
            "1996-05-18",
            "1999-04-17",
            # The Prophet's Birthday
            "2006-04-10",
            "2011-02-15",
            "2018-11-20",
            "1991-09-20",
            "1996-07-27",
            "1999-06-26",
            # The Prophet's Ascension
            "2001-10-15",
            "2011-06-29",
            "2018-04-14",
            "1991-02-11",
            "1996-12-08",
            "1999-11-05",
        )

    def test_vesak(self):
        self.assertHoliday(
            "2007-06-01",
            "2011-05-17",
            "2018-05-29",
            "1991-05-28",
            "1996-05-31",
            "1999-05-29",
        )

    def test_special(self):
        self.assertHoliday("2018-06-27", "2019-04-17", "2020-12-09")

    def test_2021(self):
        self.assertHolidays(
            Indonesia(years=2021),
            ("2021-01-01", "Tahun Baru Masehi"),
            ("2021-02-12", "Tahun Baru Imlek"),
            ("2021-03-11", "Isra' Mi'raj Nabi Muhammad"),
            ("2021-03-14", "Hari Suci Nyepi"),
            ("2021-04-02", "Wafat Yesus Kristus"),
            ("2021-05-01", "Hari Buruh Internasional"),
            ("2021-05-13", "Hari Raya Idul Fitri; Kenaikan Yesus Kristus"),
            ("2021-05-14", "Hari kedua dari Hari Raya Idul Fitri"),
            ("2021-05-26", "Hari Raya Waisak"),
            ("2021-06-01", "Hari Lahir Pancasila"),
            ("2021-07-20", "Hari Raya Idul Adha"),
            ("2021-08-11", "Tahun Baru Islam"),
            ("2021-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2021-10-19", "Maulid Nabi Muhammad"),
            ("2021-12-25", "Hari Raya Natal"),
        )

    def test_2022(self):
        self.assertHolidays(
            Indonesia(years=2022),
            ("2022-01-01", "Tahun Baru Masehi"),
            ("2022-02-01", "Tahun Baru Imlek"),
            ("2022-02-28", "Isra' Mi'raj Nabi Muhammad"),
            ("2022-03-03", "Hari Suci Nyepi"),
            ("2022-04-15", "Wafat Yesus Kristus"),
            ("2022-05-01", "Hari Buruh Internasional"),
            ("2022-05-02", "Hari Raya Idul Fitri"),
            ("2022-05-03", "Hari kedua dari Hari Raya Idul Fitri"),
            ("2022-05-16", "Hari Raya Waisak"),
            ("2022-05-26", "Kenaikan Yesus Kristus"),
            ("2022-06-01", "Hari Lahir Pancasila"),
            ("2022-07-10", "Hari Raya Idul Adha"),
            ("2022-07-30", "Tahun Baru Islam"),
            ("2022-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2022-10-08", "Maulid Nabi Muhammad"),
            ("2022-12-25", "Hari Raya Natal"),
        )
