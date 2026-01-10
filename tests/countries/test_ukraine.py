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

from holidays.countries.ukraine import Ukraine
from tests.common import CommonCountryTests, WorkingDayTests


class TestUkraine(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ukraine)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHoliday(range(2023, self.end_year))
        self.assertNoWorkdayHoliday(range(self.start_year, 2022))

    def test_special_holidays(self):
        self.assertHoliday("1995-01-09")

    def test_substituted_holidays(self):
        self.assertHoliday(
            "1991-05-03",
            "1991-05-10",
            "1991-07-15",
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
            "1997-01-08",
            "1997-04-29",
            "1997-04-30",
            "1998-01-02",
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
            "2012-04-30",
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

    def test_workdays(self):
        self.assertWorkingDay(
            "1991-05-05",
            "1991-05-12",
            "1991-07-13",
            "1992-01-04",
            "1992-05-16",
            "1993-01-10",
            "1993-08-21",
            "1994-03-05",
            "1995-05-06",
            "1995-08-27",
            "1995-11-04",
            "1996-05-05",
            "1996-05-12",
            "1996-12-28",
            "1997-01-04",
            "1997-01-11",
            "1997-04-19",
            "1997-05-17",
            "1998-01-04",
            "1999-01-10",
            "1999-04-24",
            "1999-08-21",
            "2000-05-06",
            "2000-08-27",
            "2001-03-11",
            "2001-04-28",
            "2001-05-05",
            "2001-05-06",
            "2001-06-23",
            "2001-12-29",
            "2002-05-11",
            "2002-12-28",
            "2002-12-29",
            "2003-01-04",
            "2004-01-10",
            "2004-01-17",
            "2004-01-31",
            "2004-08-21",
            "2005-03-05",
            "2005-05-14",
            "2005-06-25",
            "2006-01-21",
            "2006-02-04",
            "2006-02-18",
            "2006-03-11",
            "2006-05-06",
            "2006-09-09",
            "2007-01-20",
            "2007-01-27",
            "2007-02-10",
            "2007-02-24",
            "2007-03-03",
            "2007-04-28",
            "2007-06-16",
            "2007-12-29",
            "2008-01-12",
            "2008-01-26",
            "2008-02-09",
            "2008-05-17",
            "2008-05-31",
            "2009-01-10",
            "2009-01-24",
            "2009-02-07",
            "2010-01-30",
            "2010-02-13",
            "2010-02-27",
            "2010-03-13",
            "2010-08-21",
            "2011-03-12",
            "2011-06-25",
            "2012-03-03",
            "2012-04-28",
            "2012-07-07",
            "2012-12-29",
            "2013-05-18",
            "2013-06-01",
            "2014-01-11",
            "2014-01-25",
            "2014-02-08",
            "2015-01-17",
            "2015-01-31",
            "2015-02-14",
            "2016-01-16",
            "2016-03-12",
            "2016-07-02",
            "2017-05-13",
            "2017-08-19",
            "2018-03-03",
            "2018-05-05",
            "2018-06-23",
            "2018-12-22",
            "2018-12-29",
            "2019-05-11",
            "2019-12-21",
            "2019-12-28",
            "2020-01-11",
            "2021-01-16",
            "2021-08-28",
            "2021-10-23",
            "2022-03-12",
        )

        for year, dts in {
            1996: (
                "1996-05-05",
                "1996-05-12",
                "1996-12-28",
            ),
        }.items():
            self.assertWorkingDay(Ukraine(years=year), dts)

    def test_new_year_day(self):
        name = "Новий рік"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(self.start_year, 2023)))
        self.assertWorkdayHolidayName(
            name, (f"{year}-01-01" for year in range(2023, self.end_year))
        )
        obs_dts = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
        )
        self.assertHolidayName(f"{name} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Різдво Христове"
        self.assertHolidayName(
            name,
            (f"{year}-01-07" for year in range(self.start_year, 2023)),
            (f"{year}-12-25" for year in range(2017, 2022)),
        )
        self.assertNoHolidayName(name, (f"{year}-12-25" for year in range(self.start_year, 2017)))
        self.assertWorkdayHolidayName(
            name,
            "2023-01-07",
            (f"{year}-12-25" for year in range(2022, self.end_year)),
        )
        self.assertNoWorkdayHolidayName(
            name, (f"{year}-01-07" for year in range(2024, self.end_year))
        )

        obs_dts = (
            "2012-01-09",
            "2017-01-09",
            "2018-01-08",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_womens_day(self):
        name = "Міжнародний жіночий день"
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(self.start_year, 2023)))
        self.assertWorkdayHolidayName(
            name, (f"{year}-03-08" for year in range(2023, self.end_year))
        )

        obs_dts = (
            "2014-03-10",
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHolidayName(f"{name} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_easter_sunday_pascha(self):
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
        self.assertHolidayName(name, range(self.start_year, 2022))
        self.assertWorkdayHolidayName(name, range(2022, self.end_year))

        obs_dts = (
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
        self.assertHolidayName(f"{name} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_holy_trinity_day(self):
        name = "Трійця"
        self.assertHolidayName(
            name,
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
        self.assertHolidayName(name, range(self.start_year, 2022))
        self.assertWorkdayHolidayName(name, range(2022, self.end_year))

        obs_dts = (
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
        self.assertHolidayName(f"{name} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        name_1991 = "День міжнародної солідарності трудящих"
        name_2018 = "День праці"
        self.assertHolidayName(
            name_1991,
            (f"{year}-05-01" for year in range(self.start_year, 2018)),
            (f"{year}-05-02" for year in range(self.start_year, 2018)),
        )
        self.assertHolidayName(name_2018, (f"{year}-05-01" for year in range(2018, 2022)))
        self.assertNoHolidayName(
            name_2018, (f"{year}-05-02" for year in range(2018, self.end_year))
        )
        self.assertNoHolidayName(name_1991, range(2018, self.end_year))
        self.assertNoHolidayName(name_2018, range(self.start_year, 2018))
        self.assertWorkdayHolidayName(
            name_2018, (f"{year}-05-01" for year in range(2022, self.end_year))
        )

        obs_dts_1991 = (
            "2010-05-03",
            "2010-05-04",
            "2011-05-03",
            "2015-05-04",
            "2016-05-03",
        )
        self.assertHolidayName(f"{name_1991} (вихідний)", obs_dts_1991)
        obs_dts_2018 = "2021-05-03"
        self.assertHolidayName(f"{name_2018} (вихідний)", obs_dts_2018)
        self.assertNoNonObservedHoliday(obs_dts_1991, obs_dts_2018)

    def test_victory_day(self):
        name_1991 = "День Перемоги"
        name_2016 = "День перемоги над нацизмом у Другій світовій війні (День перемоги)"
        name_2024 = "День памʼяті та перемоги над нацизмом у Другій світовій війні 1939-1945 років"
        self.assertHolidayName(
            name_1991, (f"{year}-05-09" for year in range(self.start_year, 2016))
        )
        self.assertHolidayName(name_2016, (f"{year}-05-09" for year in range(2016, 2022)))
        self.assertNoHolidayName(name_1991, range(2016, self.end_year))
        self.assertNoHolidayName(name_2016, range(self.start_year, 2016))
        self.assertWorkdayHolidayName(name_2016, (f"{year}-05-09" for year in range(2022, 2024)))
        self.assertWorkdayHolidayName(
            name_2024, (f"{year}-05-08" for year in range(2024, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name_2016, range(2024, self.end_year))
        self.assertNoWorkdayHolidayName(name_2024, range(self.start_year, 2024))

        obs_dts_1991 = (
            "2010-05-10",
            "2015-05-11",
        )
        self.assertHolidayName(f"{name_1991} (вихідний)", obs_dts_1991)
        obs_dts_2016 = (
            "2020-05-11",
            "2021-05-10",
        )
        self.assertHolidayName(f"{name_2016} (вихідний)", obs_dts_2016)
        self.assertNoNonObservedHoliday(obs_dts_1991, obs_dts_2016)

    def test_day_of_the_constitution_of_ukraine(self):
        name = "День Конституції України"
        self.assertHolidayName(name, (f"{year}-06-28" for year in range(1997, 2022)))
        self.assertNoHolidayName(name, range(self.start_year, 1997))
        self.assertWorkdayHolidayName(
            name, (f"{year}-06-28" for year in range(2022, self.end_year))
        )

        obs_dts = (
            "2014-06-30",
            "2015-06-29",
            "2020-06-29",
        )
        self.assertHolidayName(f"{name} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_ukrainian_statehood_day(self):
        name = "День Української Державності"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name,
            (f"{year}-07-28" for year in range(2022, 2024)),
            (f"{year}-07-15" for year in range(2024, self.end_year)),
        )

    def test_independence_day(self):
        name = "День незалежності України"
        self.assertHolidayName(name, "1991-07-16", (f"{year}-08-24" for year in range(1992, 2022)))
        self.assertWorkdayHolidayName(
            name, (f"{year}-08-24" for year in range(2022, self.end_year))
        )

        obs_dts = (
            "2013-08-26",
            "2014-08-25",
            "2019-08-26",
        )
        self.assertHolidayName(f"{name} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_day_of_defenders_of_ukraine(self):
        name_2015 = "День захисника України"
        name_2021 = "День захисників і захисниць України"
        self.assertHolidayName(name_2015, (f"{year}-10-14" for year in range(2015, 2021)))
        self.assertHolidayName(name_2021, (f"{year}-10-14" for year in range(2021, 2022)))
        self.assertNoHolidayName(
            name_2015, range(self.start_year, 2015), range(2021, self.end_year)
        )
        self.assertNoHolidayName(name_2021, range(self.start_year, 2021))
        self.assertWorkdayHolidayName(
            name_2021,
            (f"{year}-10-14" for year in range(2022, 2023)),
            (f"{year}-10-01" for year in range(2023, self.end_year)),
        )
        self.assertNoWorkdayHolidayName(
            name_2021,
            (f"{year}-10-14" for year in range(2023, self.end_year)),
            (f"{year}-10-01" for year in range(self.start_year, 2023)),
        )

        obs_dts = (
            "2017-10-16",
            "2018-10-15",
        )
        self.assertHolidayName(f"{name_2015} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_anniversary_of_the_great_october_revolution(self):
        name = "Річниця Великої Жовтневої соціалістичної революції"
        self.assertHolidayName(
            name,
            (f"{year}-11-07" for year in range(self.start_year, 2000)),
            (f"{year}-11-08" for year in range(self.start_year, 2000)),
        )
        self.assertNoHolidayName(name, range(2000, self.end_year))
        self.assertNoWorkdayHolidayName(name)

        obs_dts = (
            "1997-11-10",
            "1999-11-09",
        )
        self.assertHolidayName(f"{name} (вихідний)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2018(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/3678-3678-normi-trivalosti-robochogo-chasu.html
        self.assertHolidayDatesInYear(
            2018,
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
        self.assertHolidayDatesInYear(
            2019,
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
        self.assertHolidayDatesInYear(
            2020,
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
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "Новий рік"),
            ("2021-01-07", "Різдво Христове"),
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
            ("2021-12-25", "Різдво Христове"),
            ("2021-12-27", "Різдво Христове (вихідний)"),
        )

    def test_2022(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4246-norma-trivalosti-robochogo-chasu-2022.html
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Новий рік"),
            ("2022-01-03", "Новий рік (вихідний)"),
            ("2022-01-07", "Різдво Христове"),
            ("2022-03-07", "Вихідний день (перенесено з 12.03.2022)"),
            ("2022-03-08", "Міжнародний жіночий день"),
        )

    def test_2022_workday(self):
        self.assertWorkdayHolidaysInYear(
            2022,
            ("2022-04-24", "Великдень (Пасха)"),
            ("2022-05-01", "День праці"),
            ("2022-05-09", "День перемоги над нацизмом у Другій світовій війні (День перемоги)"),
            ("2022-06-12", "Трійця"),
            ("2022-06-28", "День Конституції України"),
            ("2022-07-28", "День Української Державності"),
            ("2022-08-24", "День незалежності України"),
            ("2022-10-14", "День захисників і захисниць України"),
            ("2022-12-25", "Різдво Христове"),
        )

    def test_2023_workday(self):
        self.assertWorkdayHolidaysInYear(
            2023,
            ("2023-01-01", "Новий рік"),
            ("2023-01-07", "Різдво Христове"),
            ("2023-03-08", "Міжнародний жіночий день"),
            ("2023-04-16", "Великдень (Пасха)"),
            ("2023-05-01", "День праці"),
            ("2023-05-09", "День перемоги над нацизмом у Другій світовій війні (День перемоги)"),
            ("2023-06-04", "Трійця"),
            ("2023-06-28", "День Конституції України"),
            ("2023-07-28", "День Української Державності"),
            ("2023-08-24", "День незалежності України"),
            ("2023-10-01", "День захисників і захисниць України"),
            ("2023-12-25", "Різдво Христове"),
        )

    def test_2024_workday(self):
        self.assertWorkdayHolidaysInYear(
            2024,
            ("2024-01-01", "Новий рік"),
            ("2024-03-08", "Міжнародний жіночий день"),
            ("2024-05-01", "День праці"),
            ("2024-05-05", "Великдень (Пасха)"),
            (
                "2024-05-08",
                "День памʼяті та перемоги над нацизмом у Другій світовій війні 1939-1945 років",
            ),
            ("2024-06-23", "Трійця"),
            ("2024-06-28", "День Конституції України"),
            ("2024-07-15", "День Української Державності"),
            ("2024-08-24", "День незалежності України"),
            ("2024-10-01", "День захисників і захисниць України"),
            ("2024-12-25", "Різдво Христове"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2021-01-01", "Новий рік"),
            ("2021-01-07", "Різдво Христове"),
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
            ("2021-12-25", "Різдво Христове"),
            ("2021-12-27", "Різдво Христове (вихідний)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2021-01-01", "New Year's Day"),
            ("2021-01-07", "Christmas Day"),
            ("2021-01-08", "Day off (substituted from 01/16/2021)"),
            ("2021-03-08", "International Women's Day"),
            ("2021-05-01", "Labor Day"),
            ("2021-05-02", "Easter Sunday (Pascha)"),
            ("2021-05-03", "Labor Day (observed)"),
            ("2021-05-04", "Easter Sunday (Pascha) (observed)"),
            ("2021-05-09", "Day of Victory over Nazism in World War II (Victory Day)"),
            ("2021-05-10", "Day of Victory over Nazism in World War II (Victory Day) (observed)"),
            ("2021-06-20", "Holy Trinity Day"),
            ("2021-06-21", "Holy Trinity Day (observed)"),
            ("2021-06-28", "Day of the Constitution of Ukraine"),
            ("2021-08-23", "Day off (substituted from 08/28/2021)"),
            ("2021-08-24", "Independence Day"),
            ("2021-10-14", "Day of defenders of Ukraine"),
            ("2021-10-15", "Day off (substituted from 10/23/2021)"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2021-01-01", "السنة الجديدة"),
            ("2021-01-07", "عيد الميلاد"),
            ("2021-01-08", "يوم عطلة (استبدل من 16/01/2021)"),
            ("2021-03-08", "اليوم العالمي للمرأة"),
            ("2021-05-01", "عيد العمال"),
            ("2021-05-02", "عيد الفصح"),
            ("2021-05-03", "عيد العمال (ملاحظة)"),
            ("2021-05-04", "عيد الفصح (ملاحظة)"),
            ("2021-05-09", "يوم النصر على النازية في الحرب العالمية الثانية (يوم النصر)"),
            ("2021-05-10", "يوم النصر على النازية في الحرب العالمية الثانية (يوم النصر) (ملاحظة)"),
            ("2021-06-20", "الثالوث"),
            ("2021-06-21", "الثالوث (ملاحظة)"),
            ("2021-06-28", "يوم الدستور في أوكرانيا"),
            ("2021-08-23", "يوم عطلة (استبدل من 28/08/2021)"),
            ("2021-08-24", "عيد استقلال أوكرانيا"),
            ("2021-10-14", "يوم المدافعين عن أوكرانيا"),
            ("2021-10-15", "يوم عطلة (استبدل من 23/10/2021)"),
            ("2021-12-25", "عيد الميلاد"),
            ("2021-12-27", "عيد الميلاد (ملاحظة)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2021-01-01", "วันขึ้นปีใหม่"),
            ("2021-01-07", "วันคริสต์มาส"),
            ("2021-01-08", "วันหยุด (แทน 16/01/2021)"),
            ("2021-03-08", "วันสตรีสากล"),
            ("2021-05-01", "วันแรงงาน"),
            ("2021-05-02", "วันอาทิตย์อีสเตอร์"),
            ("2021-05-03", "ชดเชยวันแรงงาน"),
            ("2021-05-04", "ชดเชยวันอาทิตย์อีสเตอร์"),
            ("2021-05-09", "วันแห่งชัยชนะเหนือระบอบชาติสังคมนิยมในสงครามโลกครั้งที่สอง (วันแห่งชัยชนะ)"),
            ("2021-05-10", "ชดเชยวันแห่งชัยชนะเหนือระบอบชาติสังคมนิยมในสงครามโลกครั้งที่สอง (วันแห่งชัยชนะ)"),
            ("2021-06-20", "วันสมโภชพระตรีเอกภาพ"),
            ("2021-06-21", "ชดเชยวันสมโภชพระตรีเอกภาพ"),
            ("2021-06-28", "วันรัฐธรรมนูญยูเครน"),
            ("2021-08-23", "วันหยุด (แทน 28/08/2021)"),
            ("2021-08-24", "วันประกาศอิสรภาพยูเครน"),
            ("2021-10-14", "วันแห่งผู้พิทักษ์ยูเครน"),
            ("2021-10-15", "วันหยุด (แทน 23/10/2021)"),
            ("2021-12-25", "วันคริสต์มาส"),
            ("2021-12-27", "ชดเชยวันคริสต์มาส"),
        )
