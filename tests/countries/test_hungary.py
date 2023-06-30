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

from holidays.countries.hungary import Hungary, HU, HUN
from tests.common import TestCase


class TestHungary(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Hungary, years=range(1945, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Hungary, HU, HUN)

    def test_new_years_day(self):
        self.assertHolidayName("Újév", (f"{year}-01-01" for year in range(1945, 2050)))

    def test_national_day_march(self):
        name = "Nemzeti ünnep"
        years_absent = set(range(1951, 1989))
        self.assertHolidayName(
            name, (f"{year}-03-15" for year in set(range(1945, 2050)).difference(years_absent))
        )
        self.assertNoHoliday(f"{year}-03-15" for year in years_absent)
        self.assertNoHolidayName(name, years_absent)

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
        self.assertNoHolidayName(name, range(1945, 2017))

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
        self.assertHolidayName(name, range(1945, 2050))

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
        self.assertHolidayName(name, set(range(1945, 2050)).difference({1955}))
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
        self.assertHolidayName(name, range(1945, 2050))

    def test_whit_monday(self):
        name = "Pünkösdhétfő"
        years_absent = set(range(1953, 1992))
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
        self.assertHolidayName(name, set(range(1945, 2050)).difference(years_absent))
        self.assertNoHolidayName(name, years_absent)

    def test_labour_day(self):
        name = "A Munka ünnepe"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1946, 2050)))
        self.assertNoHoliday("1945-05-01")
        self.assertNoHolidayName(name, 1945)
        self.assertHolidayName(name, (f"{year}-05-02" for year in range(1950, 1954)))

    def test_foundation_day(self):
        name_1 = "A kenyér ünnepe"
        name_2 = "Az államalapítás ünnepe"
        years_1 = set(range(1950, 1990))
        years_2 = set(range(1945, 2050)).difference(years_1)
        self.assertHolidayName(name_1, (f"{year}-08-20" for year in years_1))
        self.assertHolidayName(name_2, (f"{year}-08-20" for year in years_2))
        self.assertNoHolidayName(name_1, years_2)
        self.assertNoHolidayName(name_2, years_1)

    def test_national_day_october(self):
        name = "Nemzeti ünnep"
        self.assertHolidayName(name, (f"{year}-10-23" for year in range(1991, 2050)))
        self.assertNoHoliday(f"{year}-10-23" for year in range(1945, 1991))
        self.assertNoHolidayName(name, range(1951, 1989))

    def test_all_saints_day(self):
        name = "Mindenszentek"
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(1999, 2050)))
        self.assertNoHoliday(f"{year}-11-01" for year in range(1945, 1999))
        self.assertNoHolidayName(name, range(1945, 1999))

    def test_christmas(self):
        self.assertHolidayName("Karácsony", (f"{year}-12-25" for year in range(1945, 2050)))

        name = "Karácsony másnapja"
        self.assertHolidayName(
            name, (f"{year}-12-26" for year in set(range(1945, 2050)).difference({1955}))
        )
        self.assertNoHoliday("1955-12-26")
        self.assertNoHolidayName(name, 1955)

    def test_proclamation_soviet_republic_day(self):
        name = "A Tanácsköztársaság kikiáltásának ünnepe"
        years_present = set(range(1950, 1990))
        years_absent = set(range(1945, 2050)).difference(years_present)
        self.assertHolidayName(name, (f"{year}-03-21" for year in years_present))
        self.assertNoHoliday(f"{year}-03-21" for year in years_absent)
        self.assertNoHolidayName(name, years_absent)

    def test_liberation_day(self):
        name = "A felszabadulás ünnepe"
        years_present = set(range(1950, 1990))
        years_absent = set(range(1945, 2050)).difference(years_present)
        self.assertHolidayName(name, (f"{year}-04-04" for year in years_present))
        self.assertNoHolidayName(name, years_absent)

    def test_october_socialist_revolution_day(self):
        name = "A nagy októberi szocialista forradalom ünnepe"
        years_present = set(range(1950, 1989)).difference({1956})
        years_absent = set(range(1945, 2050)).difference(years_present)
        self.assertHolidayName(name, (f"{year}-11-07" for year in years_present))
        self.assertNoHoliday(f"{year}-11-07" for year in years_absent)
        self.assertNoHolidayName(name, years_absent)

    def test_additional_day_off(self):
        dt = (
            "2011-03-14",
            "2011-10-31",
            "2012-03-16",
            "2012-04-30",
            "2012-10-22",
            "2012-11-02",
            "2013-08-19",
            "2013-12-27",
            "2014-05-02",
            "2014-10-24",
            "2015-01-02",
            "2015-08-21",
            "2016-03-14",
            "2016-10-31",
            "2018-03-16",
            "2018-04-30",
            "2018-10-22",
            "2018-11-02",
            "2018-12-31",
            "2019-08-19",
            "2019-12-27",
            "2020-08-21",
            "2022-03-14",
            "2022-10-31",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

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
            ("2021-12-25", "Karácsony"),
            ("2021-12-26", "Karácsony másnapja"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Újév"),
            ("2022-03-14", "Nemzeti ünnep előtti pihenőnap"),
            ("2022-03-15", "Nemzeti ünnep"),
            ("2022-04-15", "Nagypéntek"),
            ("2022-04-17", "Húsvét"),
            ("2022-04-18", "Húsvét Hétfő"),
            ("2022-05-01", "A Munka ünnepe"),
            ("2022-06-05", "Pünkösd"),
            ("2022-06-06", "Pünkösdhétfő"),
            ("2022-08-20", "Az államalapítás ünnepe"),
            ("2022-10-23", "Nemzeti ünnep"),
            ("2022-10-31", "Mindenszentek előtti pihenőnap"),
            ("2022-11-01", "Mindenszentek"),
            ("2022-12-25", "Karácsony"),
            ("2022-12-26", "Karácsony másnapja"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-03-14", "Day off before National Day"),
            ("2022-03-15", "National Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-20", "State Foundation Day"),
            ("2022-10-23", "National Day"),
            ("2022-10-31", "Day off before All Saints' Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-03-14", "Національне свято (вихідний за день до)"),
            ("2022-03-15", "Національне свято"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-08-20", "День заснування держави"),
            ("2022-10-23", "Національне свято"),
            ("2022-10-31", "День усіх святих (вихідний за день до)"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
