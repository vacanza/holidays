#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.russia import Russia, RU, RUS
from tests.common import CommonCountryTests


class TestRussia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Russia, years=range(1991, 2025))

    def test_country_aliases(self):
        self.assertAliases(Russia, RU, RUS)

    def test_no_holidays(self):
        self.assertNoHolidays(Russia(years=1990))

    def test_special_holidays(self):
        self.assertHoliday(
            # Substituted Holidays.
            "1991-05-03",
            "1991-05-10",
            "1994-03-07",
            "1995-05-08",
            "1995-11-06",
            "1995-12-11",
            "1996-05-03",
            "1996-05-10",
            "1996-07-03",
            "1996-11-08",
            "1996-12-13",
            "1997-01-03",
            "1997-06-13",
            "1999-01-08",
            "2000-05-08",
            "2000-11-06",
            "2000-12-11",
            "2001-03-09",
            "2001-04-30",
            "2001-06-11",
            "2001-12-31",
            "2002-05-03",
            "2002-05-10",
            "2002-11-08",
            "2002-12-13",
            "2003-01-03",
            "2003-01-06",
            "2003-06-13",
            "2005-03-07",
            "2005-05-10",
            "2006-02-24",
            "2006-05-08",
            "2007-04-30",
            "2007-06-11",
            "2007-12-31",
            "2008-05-02",
            "2008-06-13",
            "2008-11-03",
            "2009-01-09",
            "2010-02-22",
            "2010-11-05",
            "2011-03-07",
            "2012-03-09",
            "2012-04-30",
            "2012-05-07",
            "2012-05-08",
            "2012-06-11",
            "2012-12-31",
            "2013-05-02",
            "2013-05-03",
            "2013-05-10",
            "2014-05-02",
            "2014-06-13",
            "2014-11-03",
            "2015-01-09",
            "2015-05-04",
            "2016-02-22",
            "2016-03-07",
            "2016-05-03",
            "2017-02-24",
            "2017-05-08",
            "2018-03-09",
            "2018-04-30",
            "2018-05-02",
            "2018-06-11",
            "2018-12-31",
            "2019-05-02",
            "2019-05-03",
            "2019-05-10",
            "2020-05-04",
            "2020-05-05",
            "2021-02-22",
            "2021-11-05",
            "2021-12-31",
            "2022-03-07",
            "2022-05-03",
            "2022-05-10",
            "2023-02-24",
            "2023-05-08",
            "2024-04-29",
            "2024-04-30",
            "2024-05-10",
            "2024-12-30",
            "2024-12-31",
            "2025-05-02",
            "2025-05-08",
            "2025-06-13",
            "2025-11-03",
            "2025-12-31",
        )
        self.assertNoNonObservedHoliday(
            # Substituted Holidays (observed).
            "1992-05-04",
            "1992-05-11",
            "1992-11-09",
            "1993-01-04",
            "1993-05-03",
            "1993-05-04",
            "1993-05-10",
            "1993-06-14",
            "1993-11-08",
            "1994-01-03",
            "1994-01-04",
            "1994-05-03",
            "1994-05-10",
            "1994-06-13",
            "1995-01-03",
            "1995-01-09",
            "1996-01-08",
            "1997-03-10",
            "1998-03-09",
            "1998-05-04",
            "1998-05-11",
            "1998-11-09",
            "1998-12-14",
            "1999-01-04",
            "1999-05-03",
            "1999-05-04",
            "1999-05-10",
            "1999-06-14",
            "1999-11-08",
            "1999-12-13",
            "2000-01-03",
            "2000-01-04",
            "2001-01-08",
            "2002-02-25",
            "2003-02-24",
            "2003-03-10",
            "2004-05-03",
            "2004-05-04",
            "2004-05-10",
            "2004-06-14",
            "2004-11-08",
            "2004-12-13",
            "2005-01-06",
            "2005-01-10",
            "2005-05-02",
            "2005-06-13",
            "2006-01-06",
            "2006-01-09",
            "2006-11-06",
            "2007-01-08",
            "2007-11-05",
            "2008-01-08",
            "2008-02-25",
            "2008-03-10",
            "2009-01-06",
            "2009-01-08",
            "2009-03-09",
            "2009-05-11",
            "2010-01-06",
            "2010-01-08",
            "2010-05-03",
            "2010-05-10",
            "2010-06-14",
            "2011-01-06",
            "2011-01-10",
            "2011-05-02",
            "2011-06-13",
            "2012-01-06",
            "2012-01-09",
            "2012-11-05",
            "2014-03-10",
            "2015-03-09",
            "2015-05-11",
            "2016-05-02",
            "2016-06-13",
            "2017-11-06",
            "2018-11-05",
            "2020-02-24",
            "2020-03-09",
            "2020-05-11",
            "2021-05-03",
            "2021-05-10",
            "2021-06-14",
            "2022-05-02",
            "2022-06-13",
            "2023-11-06",
        )

    def test_new_year(self):
        name_1 = "Новый год"
        name_2 = "Новогодние каникулы"
        self.assertHolidayName(name_1, (f"{year}-01-01" for year in range(1991, 2005)))
        self.assertHolidayName(name_1, (f"{year}-01-02" for year in range(1993, 2005)))
        self.assertNoHoliday(f"{year}-01-02" for year in range(1991, 1992))
        for year in range(2005, 2025):
            self.assertHolidayName(
                name_2,
                f"{year}-01-01",
                f"{year}-01-02",
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
            )
        for year in range(2013, 2025):
            self.assertHolidayName(name_2, f"{year}-01-06", f"{year}-01-08")
        for year in range(1991, 2005):
            self.assertNoHolidayName(name_1, (f"{year}-01-03", f"{year}-01-04", f"{year}-01-05"))
            self.assertNoHolidayName(name_2, (f"{year}-01-03", f"{year}-01-04", f"{year}-01-05"))
        for year in range(1991, 2013):
            self.assertNoHolidayName(name_1, (f"{year}-01-06", f"{year}-01-08"))
            self.assertNoHolidayName(name_2, (f"{year}-01-06", f"{year}-01-08"))
        self.assertNoHolidayName(name_1, range(2005, 2025))
        self.assertNoHolidayName(name_2, range(1991, 2005))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Рождество Христово", (f"{year}-01-07" for year in range(1991, 2025))
        )

    def test_defender_of_fatherland_day(self):
        name = "День защитника Отечества"
        self.assertHolidayName(name, (f"{year}-02-23" for year in range(2002, 2025)))
        self.assertNoHoliday(f"{year}-02-23" for year in range(1991, 2002))
        self.assertNoHolidayName(name, range(1991, 2002))

    def test_international_womens_day(self):
        self.assertHolidayName(
            "Международный женский день", (f"{year}-03-08" for year in range(1991, 2025))
        )

    def test_labor_day(self):
        name_1 = "День международной солидарности трудящихся"
        name_2 = "Праздник Весны и Труда"
        self.assertHolidayName(name_1, "1991-05-01", "1991-05-02")
        self.assertHolidayName(name_2, (f"{year}-05-01" for year in range(1992, 2025)))
        self.assertHolidayName(name_2, (f"{year}-05-02" for year in range(1992, 2005)))
        self.assertNoHolidayName(name_2, (f"{year}-05-02" for year in range(2005, 2025)))
        self.assertNoHolidayName(name_1, range(1992, 2025))
        self.assertNoHolidayName(name_2, 1991)

    def test_victory_day(self):
        self.assertHolidayName("День Победы", (f"{year}-05-09" for year in range(1991, 2025)))

    def test_russia_day(self):
        name_1 = "День принятия Декларации о государственном суверенитете Российской Федерации"
        name_2 = "День России"
        self.assertHolidayName(name_1, (f"{year}-06-12" for year in range(1992, 2002)))
        self.assertHolidayName(name_2, (f"{year}-06-12" for year in range(2002, 2025)))
        self.assertNoHoliday("1991-06-12")
        self.assertNoHolidayName(name_1, 1991, range(2002, 2025))
        self.assertNoHolidayName(name_2, range(1991, 2002))

    def test_unity_day(self):
        name = "День народного единства"
        self.assertHolidayName(name, (f"{year}-11-04" for year in range(2005, 2025)))
        self.assertNoHoliday(f"{year}-11-04" for year in range(1991, 2005))
        self.assertNoHolidayName(name, range(1991, 2005))

    def test_october_revolution(self):
        name_1 = "Годовщина Великой Октябрьской социалистической революции"
        name_2 = "День согласия и примирения"
        self.assertHolidayName(name_1, (f"{year}-11-07" for year in range(1991, 1996)))
        self.assertHolidayName(name_1, "1991-11-08")
        self.assertHolidayName(name_2, (f"{year}-11-07" for year in range(1996, 2005)))
        self.assertNoHolidayName(name_1, (f"{year}-11-07" for year in range(2005, 2025)))
        self.assertNoHolidayName(name_2, (f"{year}-11-07" for year in range(2005, 2025)))
        self.assertNoHolidayName(name_1, (f"{year}-11-08" for year in range(1992, 2025)))
        self.assertNoHolidayName(name_2, (f"{year}-11-08" for year in range(1992, 2025)))
        self.assertNoHolidayName(name_1, range(1996, 2025))
        self.assertNoHolidayName(name_2, range(1991, 1996), range(2005, 2025))

    def test_2018(self):
        self.assertHolidays(
            Russia(years=2018),
            ("2018-01-01", "Новогодние каникулы"),
            ("2018-01-02", "Новогодние каникулы"),
            ("2018-01-03", "Новогодние каникулы"),
            ("2018-01-04", "Новогодние каникулы"),
            ("2018-01-05", "Новогодние каникулы"),
            ("2018-01-06", "Новогодние каникулы"),
            ("2018-01-07", "Рождество Христово"),
            ("2018-01-08", "Новогодние каникулы"),
            ("2018-02-23", "День защитника Отечества"),
            ("2018-03-08", "Международный женский день"),
            ("2018-03-09", "Выходной (перенесено с 06.01.2018)"),
            ("2018-04-30", "Выходной (перенесено с 28.04.2018)"),
            ("2018-05-01", "Праздник Весны и Труда"),
            ("2018-05-02", "Выходной (перенесено с 07.01.2018)"),
            ("2018-05-09", "День Победы"),
            ("2018-06-11", "Выходной (перенесено с 09.06.2018)"),
            ("2018-06-12", "День России"),
            ("2018-11-04", "День народного единства"),
            ("2018-11-05", "Выходной (перенесено с 04.11.2018)"),
            ("2018-12-31", "Выходной (перенесено с 29.12.2018)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Новогодние каникулы"),
            ("2018-01-02", "Новогодние каникулы"),
            ("2018-01-03", "Новогодние каникулы"),
            ("2018-01-04", "Новогодние каникулы"),
            ("2018-01-05", "Новогодние каникулы"),
            ("2018-01-06", "Новогодние каникулы"),
            ("2018-01-07", "Рождество Христово"),
            ("2018-01-08", "Новогодние каникулы"),
            ("2018-02-23", "День защитника Отечества"),
            ("2018-03-08", "Международный женский день"),
            ("2018-03-09", "Выходной (перенесено с 06.01.2018)"),
            ("2018-04-30", "Выходной (перенесено с 28.04.2018)"),
            ("2018-05-01", "Праздник Весны и Труда"),
            ("2018-05-02", "Выходной (перенесено с 07.01.2018)"),
            ("2018-05-09", "День Победы"),
            ("2018-06-11", "Выходной (перенесено с 09.06.2018)"),
            ("2018-06-12", "День России"),
            ("2018-11-04", "День народного единства"),
            ("2018-11-05", "Выходной (перенесено с 04.11.2018)"),
            ("2018-12-31", "Выходной (перенесено с 29.12.2018)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year Holidays"),
            ("2018-01-02", "New Year Holidays"),
            ("2018-01-03", "New Year Holidays"),
            ("2018-01-04", "New Year Holidays"),
            ("2018-01-05", "New Year Holidays"),
            ("2018-01-06", "New Year Holidays"),
            ("2018-01-07", "Christmas Day"),
            ("2018-01-08", "New Year Holidays"),
            ("2018-02-23", "Fatherland Defender's Day"),
            ("2018-03-08", "International Women's Day"),
            ("2018-03-09", "Day off (substituted from 01/06/2018)"),
            ("2018-04-30", "Day off (substituted from 04/28/2018)"),
            ("2018-05-01", "Holiday of Spring and Labor"),
            ("2018-05-02", "Day off (substituted from 01/07/2018)"),
            ("2018-05-09", "Victory Day"),
            ("2018-06-11", "Day off (substituted from 06/09/2018)"),
            ("2018-06-12", "Russia Day"),
            ("2018-11-04", "Unity Day"),
            ("2018-11-05", "Day off (substituted from 11/04/2018)"),
            ("2018-12-31", "Day off (substituted from 12/29/2018)"),
        )
