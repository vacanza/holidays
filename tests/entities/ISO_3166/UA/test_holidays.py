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

from holidays.entities.ISO_3166.UA import UaHolidays
from tests.common import CommonCountryTests


class TestUaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            UaHolidays, years=range(1991, 2023), years_non_observed=range(1991, 2023)
        )

    def test_no_holidays(self):
        self.assertNoHolidays(UaHolidays(years=1990))
        self.assertNoHolidays(UaHolidays(years=2023))

    def test_special_holidays(self):
        self.assertHoliday("1995-01-09")

    def test_new_year_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1991, 2023))
        dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_julian_day(self):
        self.assertHoliday(f"{year}-01-07" for year in range(1991, 2023))
        dt = (
            "2012-01-09",
            "2017-01-09",
            "2018-01-08",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_womens_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1991, 2023))
        dt = (
            "2014-03-10",
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_easter(self):
        name = "Великдень (Пасха)"
        self.assertHolidayName(
            name,
            "2010-04-04",
            "2011-04-24",
            "2012-04-15",
            "2013-05-05",
            "2014-04-20",
            "2015-04-12",
            "2016-05-01",
            "2017-04-16",
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
        )
        self.assertHolidayName(name, range(1992, 2022))
        self.assertNoHolidayName(name, 1991)

        dt = (
            "2010-04-05",
            "2011-04-25",
            "2012-04-16",
            "2013-05-06",
            "2014-04-21",
            "2015-04-13",
            "2016-05-03",
            "2017-04-17",
            "2018-04-09",
            "2019-04-29",
            "2020-04-20",
            "2021-05-04",
            # special cases
            "2000-05-03",
            "2005-05-03",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_trinity(self):
        self.assertHolidayName(
            "Трійця",
            "2010-05-23",
            "2011-06-12",
            "2012-06-03",
            "2013-06-23",
            "2014-06-08",
            "2015-05-31",
            "2016-06-19",
            "2017-06-04",
            "2018-05-27",
            "2019-06-16",
            "2020-06-07",
            "2021-06-20",
        )

        dt = (
            "2010-05-24",
            "2011-06-13",
            "2012-06-04",
            "2013-06-24",
            "2014-06-09",
            "2015-06-01",
            "2016-06-20",
            "2017-06-05",
            "2018-05-28",
            "2019-06-17",
            "2020-06-08",
            "2021-06-21",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_labour_day(self):
        name_before = "День міжнародної солідарності трудящих"
        name_after = "День праці"
        self.assertHoliday(f"{year}-05-01" for year in range(1991, 2022))
        self.assertHoliday(f"{year}-05-02" for year in range(1991, 2018))
        self.assertNoHoliday("2018-05-02")
        self.assertNoHolidayName(name_after, range(1919, 2018))
        self.assertNoHolidayName(name_before, range(2018, 2022))

        dt = (
            "2010-05-03",
            "2010-05-04",
            "2011-05-03",
            "2015-05-04",
            "2016-05-03",
            "2021-05-03",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_victory_day(self):
        name = "День перемоги над нацизмом у Другій світовій війні (День перемоги)"
        self.assertHoliday(f"{year}-05-09" for year in range(1991, 2022))
        self.assertNoHolidayName(name, range(1991, 2016))

        dt = (
            "2010-05-10",
            "2015-05-11",
            "2020-05-11",
            "2021-05-10",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_constitution_day(self):
        self.assertNoHoliday(f"{year}-06-28" for year in range(1991, 1997))
        self.assertNoHolidayName("День Конституції України", range(1991, 1997))
        self.assertHoliday(f"{year}-06-28" for year in range(1997, 2022))

        dt = (
            "2014-06-30",
            "2015-06-29",
            "2020-06-29",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        self.assertHoliday("1991-07-16")
        self.assertHoliday(f"{year}-08-24" for year in range(1992, 2022))
        self.assertNoHoliday("1991-08-24", "1992-07-16")

        dt = (
            "2013-08-26",
            "2014-08-25",
            "2019-08-26",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_defenders_day(self):
        name_before = "День захисника України"
        name_after = "День захисників і захисниць України"
        self.assertNoHoliday(f"{year}-10-14" for year in range(1991, 2015))
        self.assertHoliday(f"{year}-10-14" for year in range(2015, 2022))
        self.assertNoHolidayName(name_before, range(1991, 2015))
        self.assertNoHolidayName(name_before, range(2021, 2022))
        self.assertNoHolidayName(name_after, range(1991, 2021))

        dt = (
            "2017-10-16",
            "2018-10-15",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_october_revolution_day(self):
        self.assertHoliday(f"{year}-11-07" for year in range(1991, 2000))
        self.assertHoliday(f"{year}-11-08" for year in range(1991, 2000))
        self.assertNoHoliday(f"{year}-11-07" for year in range(2000, 2022))
        self.assertNoHoliday(f"{year}-11-08" for year in range(2000, 2022))
        self.assertNoHolidayName(
            "Річниця Великої Жовтневої соціалістичної революції", range(2000, 2022)
        )

        dt = (
            "1997-11-10",
            "1999-11-09",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_gregorian_day(self):
        self.assertNoHoliday(f"{year}-12-25" for year in range(1991, 2017))
        self.assertNoHolidayName(
            "Різдво Христове (за григоріанським календарем)", range(1991, 2017)
        )
        self.assertHoliday(f"{year}-12-25" for year in range(2017, 2022))

        dt = "2021-12-27"
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_substituted(self):
        self.assertHoliday(
            "1992-01-06",
            "1992-04-27",
            "1993-01-08",
            "1993-08-23",
            "1994-03-07",
            "1995-05-08",
            "1995-08-25",
            "1995-11-06",
            "1996-05-03",
            "1996-05-10",
            "1997-01-02",
            "1997-01-06",
            "1997-04-29",
            "1997-04-30",
            "1999-01-08",
            "1999-04-12",
            "1999-08-23",
            "2000-05-08",
            "2000-08-25",
            "2001-03-09",
            "2001-04-30",
            "2001-05-10",
            "2001-05-11",
            "2001-06-29",
            "2001-12-31",
            "2002-05-03",
            "2002-12-30",
            "2002-12-31",
            "2003-01-06",
            "2004-01-02",
            "2004-01-05",
            "2004-01-06",
            "2004-08-23",
            "2005-03-07",
            "2005-05-10",
            "2005-06-27",
            "2006-01-03",
            "2006-01-04",
            "2006-01-05",
            "2006-01-06",
            "2006-05-08",
            "2006-08-25",
            "2007-01-02",
            "2007-01-03",
            "2007-01-04",
            "2007-01-05",
            "2007-03-09",
            "2007-04-30",
            "2007-06-29",
            "2007-12-31",
            "2008-01-02",
            "2008-01-03",
            "2008-01-04",
            "2008-04-29",
            "2008-04-30",
            "2009-01-02",
            "2009-01-05",
            "2009-01-06",
            "2010-01-04",
            "2010-01-05",
            "2010-01-06",
            "2010-01-08",
            "2010-08-23",
            "2011-03-07",
            "2011-06-27",
            "2012-03-09",
            "2012-04-20",
            "2012-06-29",
            "2012-12-31",
            "2013-05-03",
            "2013-05-10",
            "2014-01-02",
            "2014-01-03",
            "2014-01-06",
            "2015-01-02",
            "2015-01-08",
            "2015-01-09",
            "2016-01-08",
            "2016-03-07",
            "2016-06-27",
            "2017-05-08",
            "2017-08-25",
            "2018-03-09",
            "2018-04-30",
            "2018-06-29",
            "2018-12-24",
            "2018-12-31",
            "2019-04-30",
            "2019-12-30",
            "2019-12-31",
            "2020-01-06",
            "2021-01-08",
            "2021-08-23",
            "2021-10-15",
            "2022-03-07",
        )

    def test_2018(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/3678-3678-normi-trivalosti-robochogo-chasu.html
        self.assertHolidayDates(
            UaHolidays(years=2018),
            "2018-01-01",
            "2018-01-07",
            "2018-01-08",
            "2018-03-08",
            "2018-03-09",
            "2018-04-08",
            "2018-04-09",
            "2018-04-30",
            "2018-05-01",
            "2018-05-09",
            "2018-05-27",
            "2018-05-28",
            "2018-06-28",
            "2018-06-29",
            "2018-08-24",
            "2018-10-14",
            "2018-10-15",
            "2018-12-24",
            "2018-12-25",
            "2018-12-31",
        )

    def test_2019(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/3946-3946-normi-trivalosti-robochogo-chasu.html
        self.assertHolidayDates(
            UaHolidays(years=2019),
            "2019-01-01",
            "2019-01-07",
            "2019-03-08",
            "2019-04-28",
            "2019-04-29",
            "2019-04-30",
            "2019-05-01",
            "2019-05-09",
            "2019-06-16",
            "2019-06-17",
            "2019-06-28",
            "2019-08-24",
            "2019-08-26",
            "2019-10-14",
            "2019-12-25",
            "2019-12-30",
            "2019-12-31",
        )

    def test_2020(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4058-4058-normi-trivalosti-robochogo-chasu.html
        self.assertHolidayDates(
            UaHolidays(years=2020),
            "2020-01-01",
            "2020-01-06",
            "2020-01-07",
            "2020-03-08",
            "2020-03-09",
            "2020-04-19",
            "2020-04-20",
            "2020-05-01",
            "2020-05-09",
            "2020-05-11",
            "2020-06-07",
            "2020-06-08",
            "2020-06-28",
            "2020-06-29",
            "2020-08-24",
            "2020-10-14",
            "2020-12-25",
        )

    def test_2021(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4221-4221-norma-trivalosti-robochogo-chasu.html
        self.assertHolidays(
            UaHolidays(years=2021),
            ("2021-01-01", "Новий рік"),
            ("2021-01-07", "Різдво Христове (за юліанським календарем)"),
            ("2021-01-08", "Вихідний день (перенесено з 16.01.2021)"),
            ("2021-03-08", "Міжнародний жіночий день"),
            ("2021-05-01", "День праці"),
            ("2021-05-02", "Великдень (Пасха)"),
            ("2021-05-03", "День праці (вихідний)"),
            ("2021-05-04", "Великдень (Пасха) (вихідний)"),
            ("2021-05-09", "День перемоги над нацизмом у Другій світовій війні (День перемоги)"),
            (
                "2021-05-10",
                "День перемоги над нацизмом у Другій світовій війні (День перемоги) (вихідний)",
            ),
            ("2021-06-20", "Трійця"),
            ("2021-06-21", "Трійця (вихідний)"),
            ("2021-06-28", "День Конституції України"),
            ("2021-08-23", "Вихідний день (перенесено з 28.08.2021)"),
            ("2021-08-24", "День незалежності України"),
            ("2021-10-14", "День захисників і захисниць України"),
            ("2021-10-15", "Вихідний день (перенесено з 23.10.2021)"),
            ("2021-12-25", "Різдво Христове (за григоріанським календарем)"),
            ("2021-12-27", "Різдво Христове (за григоріанським календарем) (вихідний)"),
        )

    def test_2022(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4246-norma-trivalosti-robochogo-chasu-2022.html
        self.assertHolidayDates(
            UaHolidays(years=2022),
            "2022-01-01",
            "2022-01-03",
            "2022-01-07",
            "2022-03-07",
            "2022-03-08",
        )
