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

from holidays.countries.hungary import Hungary, HU, HUN
from tests.common import CommonCountryTests, WorkingDayTests


class TestHungary(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Hungary)

    def test_country_aliases(self):
        self.assertAliases(Hungary, HU, HUN)

    def test_no_holidays(self):
        self.assertNoHolidays(Hungary(years=self.start_year - 1))

    def test_substituted_holidays(self):
        self.assertHoliday(
            "1991-08-19",
            "1992-08-21",
            "1992-12-24",
            "1993-12-24",
            "1994-03-14",
            "1997-05-02",
            "1997-10-24",
            "1997-12-24",
            "1998-01-02",
            "1998-08-21",
            "1998-12-24",
            "1999-12-24",
            "2001-03-16",
            "2001-04-30",
            "2001-10-22",
            "2001-11-02",
            "2001-12-24",
            "2001-12-31",
            "2002-08-19",
            "2002-12-24",
            "2003-05-02",
            "2003-10-24",
            "2003-12-24",
            "2004-01-02",
            "2004-12-24",
            "2005-03-14",
            "2005-10-31",
            "2007-03-16",
            "2007-04-30",
            "2007-10-22",
            "2007-11-02",
            "2007-12-24",
            "2007-12-31",
            "2008-05-02",
            "2008-10-24",
            "2008-12-24",
            "2009-01-02",
            "2009-08-21",
            "2009-12-24",
            "2010-12-24",
            "2011-03-14",
            "2011-10-31",
            "2012-03-16",
            "2012-04-30",
            "2012-10-22",
            "2012-11-02",
            "2012-12-24",
            "2012-12-31",
            "2013-08-19",
            "2013-12-24",
            "2013-12-27",
            "2014-05-02",
            "2014-10-24",
            "2014-12-24",
            "2015-01-02",
            "2015-08-21",
            "2015-12-24",
            "2016-03-14",
            "2016-10-31",
            "2018-03-16",
            "2018-04-30",
            "2018-10-22",
            "2018-11-02",
            "2018-12-24",
            "2018-12-31",
            "2019-08-19",
            "2019-12-24",
            "2019-12-27",
            "2020-08-21",
            "2020-12-24",
            "2021-12-24",
            "2022-03-14",
            "2022-10-31",
            "2024-08-19",
            "2024-12-24",
            "2024-12-27",
            "2025-05-02",
            "2025-10-24",
            "2025-12-24",
            "2026-01-02",
            "2026-08-21",
            "2026-12-24",
        )

    def test_workdays(self):
        self.assertWorkingDay(
            "1991-08-17",
            "1992-08-29",
            "1992-12-19",
            "1993-12-18",
            "1994-03-12",
            "1997-04-26",
            "1997-10-18",
            "1997-12-20",
            "1998-01-10",
            "1998-08-15",
            "1998-12-19",
            "1999-12-18",
            "2001-03-10",
            "2001-04-28",
            "2001-10-20",
            "2001-10-27",
            "2001-12-22",
            "2001-12-29",
            "2002-08-10",
            "2002-12-28",
            "2003-04-26",
            "2003-10-18",
            "2003-12-13",
            "2004-01-10",
            "2004-12-18",
            "2005-03-19",
            "2005-11-05",
            "2007-03-10",
            "2007-04-21",
            "2007-10-20",
            "2007-10-27",
            "2007-12-22",
            "2007-12-29",
            "2008-04-26",
            "2008-10-18",
            "2008-12-20",
            "2009-03-28",
            "2009-08-29",
            "2009-12-19",
            "2010-12-11",
            "2011-03-19",
            "2011-11-05",
            "2012-03-24",
            "2012-04-21",
            "2012-10-27",
            "2012-11-10",
            "2012-12-15",
            "2012-12-01",
            "2013-08-24",
            "2013-12-07",
            "2013-12-21",
            "2014-05-10",
            "2014-10-18",
            "2014-12-13",
            "2015-01-10",
            "2015-08-08",
            "2015-12-12",
            "2016-03-05",
            "2016-10-15",
            "2018-03-10",
            "2018-04-21",
            "2018-10-13",
            "2018-11-10",
            "2018-12-01",
            "2018-12-15",
            "2019-08-10",
            "2019-12-07",
            "2019-12-14",
            "2020-08-29",
            "2020-12-12",
            "2021-12-11",
            "2022-03-26",
            "2022-10-15",
            "2024-08-03",
            "2024-12-07",
            "2024-12-14",
            "2025-05-17",
            "2025-10-18",
            "2025-12-13",
            "2026-01-10",
            "2026-08-08",
            "2026-12-12",
        )

    def test_new_years_day(self):
        self.assertHolidayName("Újév", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Nagypéntek"
        self.assertHolidayName(
            name,
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, range(2017, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2017))

    def test_easter(self):
        name = "Húsvét"
        self.assertHolidayName(
            name,
            "1991-03-31",
            "2000-04-23",
            "2010-04-04",
            "2017-04-16",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Húsvét Hétfő"
        self.assertHolidayName(
            name,
            "1991-04-01",
            "2000-04-24",
            "2010-04-05",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )
        self.assertHolidayName(name, range(self.start_year, 1955), range(1956, self.end_year))
        self.assertNoHolidayName(name, 1955)

    def test_whit_sunday(self):
        name = "Pünkösd"
        self.assertHolidayName(
            name,
            "1991-05-19",
            "2000-06-11",
            "2010-05-23",
            "2017-06-04",
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Pünkösdhétfő"
        self.assertHolidayName(
            name,
            "2000-06-12",
            "2010-05-24",
            "2017-06-05",
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
        )
        self.assertHolidayName(name, range(self.start_year, 1953), range(1992, self.end_year))
        self.assertNoHolidayName(name, range(1953, 1992))

    def test_labor_day(self):
        name = "A Munka ünnepe"
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in range(1946, self.end_year)),
            (f"{year}-05-02" for year in range(1950, 1954)),
        )
        self.assertNoHolidayName(name, self.start_year)
        self.assertHolidayNameCount(name, 1, range(1954, self.end_year))

    def test_foundation_day(self):
        name_1 = "A kenyér ünnepe"
        name_2 = "Az államalapítás ünnepe"
        self.assertHolidayName(name_1, (f"{year}-08-20" for year in range(1950, 1990)))
        self.assertHolidayName(
            name_2,
            (
                f"{year}-08-20"
                for year in (*range(self.start_year, 1950), *range(1990, self.end_year))
            ),
        )
        self.assertNoHolidayName(name_1, range(self.start_year, 1950), range(1990, self.end_year))
        self.assertNoHolidayName(name_2, range(1950, 1990))

    def test_national_day(self):
        name = "Nemzeti ünnep"
        self.assertHolidayName(
            name,
            (
                f"{year}-03-15"
                for year in (*range(self.start_year, 1951), *range(1989, self.end_year))
            ),
            (f"{year}-10-23" for year in range(1991, self.end_year)),
        )
        self.assertNoHolidayName(name, range(1951, 1989))

    def test_all_saints_day(self):
        name = "Mindenszentek"
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(1999, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1999))

    def test_christmas_day(self):
        self.assertHolidayName("Karácsony", (f"{year}-12-25" for year in self.full_range))

    def test_christmas_day_two(self):
        name = "Karácsony másnapja"
        self.assertHolidayName(
            name,
            (
                f"{year}-12-26"
                for year in (*range(self.start_year, 1955), *range(1956, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, 1955)

    def test_proclamation_soviet_republic_day(self):
        name = "A Tanácsköztársaság kikiáltásának ünnepe"
        self.assertHolidayName(name, (f"{year}-03-21" for year in range(1950, 1990)))
        self.assertNoHolidayName(name, range(self.start_year, 1950), range(1990, self.end_year))

    def test_liberation_day(self):
        name = "A felszabadulás ünnepe"
        self.assertHolidayName(name, (f"{year}-04-04" for year in range(1950, 1990)))
        self.assertNoHolidayName(name, range(self.start_year, 1950), range(1990, self.end_year))

    def test_october_socialist_revolution_day(self):
        name = "A nagy októberi szocialista forradalom ünnepe"
        self.assertHolidayName(
            name, (f"{year}-11-07" for year in (*range(1950, 1956), *range(1957, 1989)))
        )
        self.assertNoHolidayName(
            name, range(self.start_year, 1950), 1956, range(1989, self.end_year)
        )

    def test_2021(self):
        self.assertHolidays(
            Hungary(years=2021),
            ("2021-01-01", "Újév"),
            ("2021-03-15", "Nemzeti ünnep"),
            ("2021-04-02", "Nagypéntek"),
            ("2021-04-04", "Húsvét"),
            ("2021-04-05", "Húsvét Hétfő"),
            ("2021-05-01", "A Munka ünnepe"),
            ("2021-05-23", "Pünkösd"),
            ("2021-05-24", "Pünkösdhétfő"),
            ("2021-08-20", "Az államalapítás ünnepe"),
            ("2021-10-23", "Nemzeti ünnep"),
            ("2021-11-01", "Mindenszentek"),
            ("2021-12-24", "Pihenőnap (2021. 12. 11.-től helyettesítve)"),
            ("2021-12-25", "Karácsony"),
            ("2021-12-26", "Karácsony másnapja"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Újév"),
            ("2022-03-14", "Pihenőnap (2022. 03. 26.-től helyettesítve)"),
            ("2022-03-15", "Nemzeti ünnep"),
            ("2022-04-15", "Nagypéntek"),
            ("2022-04-17", "Húsvét"),
            ("2022-04-18", "Húsvét Hétfő"),
            ("2022-05-01", "A Munka ünnepe"),
            ("2022-06-05", "Pünkösd"),
            ("2022-06-06", "Pünkösdhétfő"),
            ("2022-08-20", "Az államalapítás ünnepe"),
            ("2022-10-23", "Nemzeti ünnep"),
            ("2022-10-31", "Pihenőnap (2022. 10. 15.-től helyettesítve)"),
            ("2022-11-01", "Mindenszentek"),
            ("2022-12-25", "Karácsony"),
            ("2022-12-26", "Karácsony másnapja"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-03-14", "Day off (substituted from 03/26/2022)"),
            ("2022-03-15", "National Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-20", "State Foundation Day"),
            ("2022-10-23", "National Day"),
            ("2022-10-31", "Day off (substituted from 10/15/2022)"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-03-14", "Вихідний день (перенесено з 26.03.2022)"),
            ("2022-03-15", "Національне свято"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-08-20", "День заснування держави"),
            ("2022-10-23", "Національне свято"),
            ("2022-10-31", "Вихідний день (перенесено з 15.10.2022)"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
