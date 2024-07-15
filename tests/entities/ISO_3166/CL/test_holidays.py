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

from holidays.constants import BANK, PUBLIC
from holidays.entities.ISO_3166.CL import ClHolidays
from tests.common import CommonCountryTests


class TestClHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ClHolidays, years=range(1915, 2050))

    def test_special_holidays(self):
        self.assertHoliday(
            "1999-12-31",
            "2022-09-16",
        )

    def test_no_holidays(self):
        self.assertNoHolidays(ClHolidays(categories=(BANK, PUBLIC), years=1914))

    def test_new_year(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1915, 2050))
        self.assertHoliday(
            "2017-01-02",
            "2023-01-02",
        )
        self.assertNoHoliday(
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
        )

    def test_holy_week(self):
        self.assertHoliday(
            "1915-04-02",
            "1940-03-22",
            "1960-04-15",
            "1980-04-04",
            "2000-04-21",
            "2015-04-03",
            "2022-04-15",
            "1915-04-03",
            "1940-03-23",
            "1960-04-16",
            "1980-04-05",
            "2000-04-22",
            "2015-04-04",
            "2022-04-16",
        )

    def test_ascension(self):
        self.assertHoliday(
            "1915-05-13",
            "1930-05-29",
            "1950-05-18",
            "1967-05-04",
        )
        name = "Ascensión del Señor"
        self.assertHolidayName(name, range(1915, 1968))
        self.assertNoHolidayName(name, range(1968, 2050))

    def test_corpus_christi(self):
        self.assertHoliday(
            "1915-06-03",
            "1940-05-23",
            "1950-06-08",
            "1967-05-25",
            "1987-06-18",
            "1998-06-11",
            "2000-06-19",
            "2006-06-12",
        )
        name = "Corpus Christi"
        self.assertHolidayName(name, range(1915, 1968))
        self.assertNoHolidayName(name, range(1968, 1987))
        self.assertHolidayName(name, range(1987, 2006))

    def test_labour_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1932, 2050))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1915, 1932))

    def test_navy_day(self):
        self.assertHoliday(f"{year}-05-21" for year in range(1915, 2050))

    def test_indigenous_peoples_day(self):
        self.assertHoliday(
            "2021-06-21",
            "2022-06-21",
            "2023-06-21",
            "2024-06-20",
            "2025-06-20",
            "2026-06-21",
            "2027-06-21",
            "2028-06-20",
            "2029-06-20",
            "2030-06-21",
            "2031-06-21",
            "2032-06-20",
            "2033-06-20",
            "2034-06-21",
            "2035-06-21",
            "2036-06-20",
            "2037-06-20",
            "2038-06-21",
            "2039-06-21",
            "2040-06-20",
            "2041-06-20",
            "2042-06-21",
            "2043-06-21",
            "2044-06-20",
            "2045-06-20",
            "2046-06-21",
            "2047-06-21",
            "2048-06-20",
            "2049-06-20",
            "2050-06-20",
            "2075-06-21",
            "2076-06-20",
            "2077-06-20",
            "2078-06-20",
            "2079-06-20",
        )
        self.assertNoHolidayName("Día Nacional de los Pueblos Indígenas", range(1915, 2021))

    def test_saint_peter_and_paul(self):
        self.assertHoliday(f"{year}-06-29" for year in range(1915, 1967))
        self.assertHoliday(f"{year}-06-29" for year in range(1986, 2000))
        self.assertHoliday(
            "2000-06-26",
            "2001-07-02",
            "2002-06-29",
            "2003-06-29",
            "2004-06-28",
            "2005-06-27",
            "2006-06-26",
            "2007-07-02",
            "2008-06-29",
            "2009-06-29",
            "2010-06-28",
            "2011-06-27",
            "2012-07-02",
            "2013-06-29",
            "2014-06-29",
            "2015-06-29",
            "2016-06-27",
            "2017-06-26",
            "2018-07-02",
            "2019-06-29",
            "2020-06-29",
            "2021-06-28",
            "2022-06-27",
            "2023-06-26",
            "2024-06-29",
        )

        self.assertNoHolidayName("San Pedro y San Pablo", range(1968, 1986))

    def test_virgin_of_carmen(self):
        self.assertHoliday(f"{year}-07-16" for year in range(2007, 2050))
        self.assertNoHoliday(f"{year}-07-16" for year in range(1915, 2007))

    def test_assumption_of_mary(self):
        self.assertHoliday(f"{year}-08-15" for year in range(1915, 2050))

    def test_national_liberation(self):
        self.assertHoliday(f"{year}-09-11" for year in range(1981, 1999))
        self.assertNoHoliday(
            "1980-09-11",
            "1999-09-11",
        )
        name = "Día de la Liberación Nacional"
        self.assertNoHolidayName(name, range(1915, 1981))
        self.assertNoHolidayName(name, range(1999, 2050))

    def test_national_unity(self):
        self.assertHoliday(
            "1999-09-06",
            "2000-09-04",
            "2001-09-03",
        )
        self.assertNoHoliday(
            "1998-09-07",
            "2002-09-02",
        )

        self.assertNoHolidayName(
            "Día de la Unidad Nacional", set(range(1915, 2050)).difference({1999, 2000, 2001})
        )

    def test_independence_holidays(self):
        self.assertHoliday(f"{year}-09-18" for year in range(1915, 2050))
        self.assertHoliday(f"{year}-09-19" for year in range(1915, 2050))
        self.assertHoliday(
            "2007-09-17",
            "2012-09-17",
            "2013-09-20",
            "2018-09-17",
            "2019-09-20",
            "2021-09-17",
            "2024-09-20",
        )
        self.assertHoliday(f"{year}-09-20" for year in range(1932, 1945))

    def test_columbus_day(self):
        years = set(range(1922, 2000)).difference({1973})
        name = "Día de la Raza"
        self.assertHoliday(f"{year}-10-12" for year in years)
        self.assertHolidayName(name, (f"{year}-10-12" for year in years))
        self.assertNoHolidayName(name, 1973)

        self.assertHoliday(
            "2000-10-09",
            "2005-10-10",
            "2010-10-11",
            "2015-10-12",
            "2019-10-12",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )

        self.assertHolidayName(name, (f"{year}-10-12" for year in years))
        self.assertHolidayName("Día del Encuentro de dos Mundos", range(2000, 2050))

    def test_reformation_day(self):
        self.assertHoliday(
            "2008-10-31",
            "2009-10-31",
            "2010-10-31",
            "2011-10-31",
            "2012-11-02",
            "2013-10-31",
            "2014-10-31",
            "2015-10-31",
            "2016-10-31",
            "2017-10-27",
            "2018-11-02",
            "2019-10-31",
            "2020-10-31",
            "2021-10-31",
            "2022-10-31",
            "2023-10-27",
        )
        self.assertNoHolidayName(
            "Día Nacional de las Iglesias Evangélicas y Protestantes", range(1915, 2008)
        )

    def test_all_saints(self):
        self.assertHoliday(f"{year}-11-01" for year in range(1915, 2050))

    def test_immaculate_conception(self):
        self.assertHoliday(f"{year}-12-08" for year in range(1915, 2050))

    def test_christmas(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1915, 2050))
        self.assertHoliday(f"{year}-12-24" for year in range(1944, 1989))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1915, 1944))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1989, 2050))

    def test_bank_holidays(self):
        name = "Feriado bancario"
        holidays = ClHolidays(categories=BANK, years=range(1915, 2050))
        self.assertHolidayName(name, holidays, (f"{year}-06-30" for year in range(1957, 1976)))
        self.assertHolidayName(name, holidays, (f"{year}-12-31" for year in range(1956, 1997)))
        self.assertHolidayName(name, holidays, (f"{year}-12-31" for year in range(1998, 2050)))
        self.assertNoHoliday(holidays, (f"{year}-06-30" for year in range(1915, 1957)))
        self.assertNoHoliday(holidays, (f"{year}-06-30" for year in range(1976, 2050)))
        self.assertNoHoliday(
            holidays, (f"{year}-12-31" for year in range(1915, 1956)), "1997-12-31"
        )
        self.assertNoHolidayName(name, holidays, range(1915, 1956))

    def test_2019(self):
        self.assertHolidayDates(
            ClHolidays(years=2019),
            "2019-01-01",
            "2019-04-19",
            "2019-04-20",
            "2019-05-01",
            "2019-05-21",
            "2019-06-29",
            "2019-07-16",
            "2019-08-15",
            "2019-09-18",
            "2019-09-19",
            "2019-09-20",
            "2019-10-12",
            "2019-10-31",
            "2019-11-01",
            "2019-12-08",
            "2019-12-25",
        )

    def test_2020(self):
        # from https://feriados.cl/2020.htm
        self.assertHolidayDates(
            ClHolidays(years=2020),
            "2020-01-01",
            "2020-04-10",
            "2020-04-11",
            "2020-05-01",
            "2020-05-21",
            "2020-06-29",
            "2020-07-16",
            "2020-08-15",
            "2020-09-18",
            "2020-09-19",
            "2020-10-12",
            "2020-10-31",
            "2020-11-01",
            "2020-12-08",
            "2020-12-25",
        )

    def test_2021(self):
        # from https://feriados.cl/2021.htm
        self.assertHolidayDates(
            ClHolidays(years=2021),
            "2021-01-01",
            "2021-04-02",
            "2021-04-03",
            "2021-05-01",
            "2021-05-21",
            "2021-06-21",
            "2021-06-28",
            "2021-07-16",
            "2021-08-15",
            "2021-09-17",
            "2021-09-18",
            "2021-09-19",
            "2021-10-11",
            "2021-10-31",
            "2021-11-01",
            "2021-12-08",
            "2021-12-25",
        )

    def test_provinces(self):
        ap_holidays = ClHolidays(subdiv="AP")
        nb_holidays = ClHolidays(subdiv="NB")
        self.assertHoliday(
            ap_holidays,
            "2020-06-07",
            "2021-06-07",
        )
        self.assertNoHoliday(ap_holidays, "2012-06-07")
        self.assertHoliday(
            nb_holidays,
            "2020-08-20",
            "2021-08-20",
        )
        self.assertNoHoliday(nb_holidays, "2013-08-20")

    def test_summer_solstice(self):
        self.assertHoliday("2050-06-20", "2079-06-20")
