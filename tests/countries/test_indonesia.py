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

from holidays.constants import GOVERNMENT
from holidays.countries.indonesia import Indonesia, ID, IDN
from tests.common import CommonCountryTests


class TestIndonesia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Indonesia, years=range(1946, 2050))

    def test_country_aliases(self):
        self.assertAliases(Indonesia, ID, IDN)

    def test_no_holidays(self):
        self.assertNoHolidays(Indonesia(years=1945))

    def test_special(self):
        self.assertHoliday("2018-06-27", "2019-04-17", "2020-12-09")

    def test_special_government(self):
        self.assertHoliday(
            Indonesia(categories=GOVERNMENT),
            "2022-04-29",
            "2022-05-04",
            "2022-05-05",
            "2022-05-06",
            "2022-12-26",
            "2023-01-23",
            "2023-03-23",
            "2023-04-19",
            "2023-04-20",
            "2023-04-21",
            "2023-04-24",
            "2023-04-25",
            "2023-12-26",
        )

    def test_new_years_day(self):
        self.assertHolidayName(
            "Tahun Baru Masehi", (f"{year}-01-01" for year in range(1946, 2050))
        )

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
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(
            set(range(1946, 2050)).difference(set(range(1968, 2003))).issubset(years_found)
        )
        self.assertFalse(set(range(1968, 2003)).intersection(years_found))

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
        self.assertNoHolidayName(name, range(1946, 1983))

    def test_good_friday(self):
        name = "Wafat Yesus Kristus"
        self.assertHolidayName(
            name,
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, range(1953, 1963), range(1971, 2050))
        self.assertNoHolidayName(name, range(1946, 1953), range(1963, 1971))

    def test_easter_monday(self):
        name = "Hari kedua Paskah"
        self.assertHolidayName(
            name,
            "1953-04-06",
            "1954-04-19",
            "1955-04-11",
            "1956-04-02",
            "1957-04-22",
            "1958-04-07",
            "1959-03-30",
            "1960-04-18",
            "1961-04-03",
            "1962-04-23",
        )
        self.assertHolidayName(name, range(1953, 1963))
        self.assertNoHolidayName(name, range(1946, 1953), range(1963, 2050))

    def test_buddhas_birthday(self):
        name = "Hari Raya Waisak"
        self.assertHolidayName(
            name,
            "2018-05-29",
            "2019-05-19",
            "2020-05-07",
            "2021-05-26",
            "2022-05-16",
            "2023-06-04",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1983, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1983)).intersection(years_found))

    def test_labor_day(self):
        name = "Hari Buruh Internasional"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1953, 1969)))
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2014, 2050)))
        self.assertNoHoliday(
            f"{year}-05-01" for year in set(range(1969, 2014)).difference({2004, 2008})
        )
        self.assertNoHolidayName(name, range(1969, 2014))

    def test_ascension_day(self):
        name = "Kenaikan Yesus Kristus"
        self.assertHolidayName(
            name,
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
        )
        self.assertHolidayName(name, range(1953, 1963), range(1968, 2050))
        self.assertNoHolidayName(name, range(1946, 1953), range(1963, 1968))

    def test_whit_monday(self):
        name = "Hari kedua Pentakosta"
        self.assertHolidayName(
            name,
            "1953-05-25",
            "1954-06-07",
            "1955-05-30",
            "1956-05-21",
            "1957-06-10",
            "1958-05-26",
            "1959-05-18",
            "1960-06-06",
            "1961-05-22",
            "1962-06-11",
        )
        self.assertHolidayName(name, range(1953, 1963))
        self.assertNoHolidayName(name, range(1946, 1953), range(1963, 2050))

    def test_pancasila_day(self):
        name = "Hari Lahir Pancasila"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2016, 2050)))
        self.assertNoHoliday(
            f"{year}-06-01" for year in set(range(1946, 2016)).difference({2000, 2007})
        )
        self.assertNoHolidayName(name, range(1946, 2016))

    def test_assumption_of_mary(self):
        name = "Mikraj Santa Maria"
        self.assertHolidayName(
            name,
            "1968-08-15",
            "1969-08-15",
            "1970-08-15",
        )
        years_no_exist = set(range(1946, 2050)).difference({1968, 1969, 1970})
        self.assertNoHoliday(
            f"{year}-08-15" for year in years_no_exist.difference({1974, 1986, 2045})
        )
        self.assertNoHolidayName(name, years_no_exist)

    def test_independence_day(self):
        name = "Hari Kemerdekaan Republik Indonesia"
        self.assertHolidayName(name, (f"{year}-08-17" for year in range(1946, 2050)))

    def test_armed_forces_day(self):
        name = "Hari Angkatan Perang"
        self.assertHolidayName(name, (f"{year}-10-05" for year in range(1946, 1953)))
        self.assertNoHoliday(f"{year}-10-05" for year in set(range(1953, 2050)).difference({2014}))
        self.assertNoHolidayName(name, range(1953, 2050))

    def test_heroes_day(self):
        name = "Hari Pahlawan"
        self.assertHolidayName(name, (f"{year}-11-10" for year in range(1946, 1953)))
        self.assertNoHoliday(
            f"{year}-11-10" for year in set(range(1953, 2050)).difference({1978, 2045})
        )
        self.assertNoHolidayName(name, range(1953, 2050))

    def test_christmas_day(self):
        name = "Hari Raya Natal"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1953, 2050)))
        self.assertNoHoliday(f"{year}-12-25" for year in range(1946, 1953))
        self.assertNoHolidayName(name, range(1946, 1953))

    def test_eid_al_fitr(self):
        name = "Hari Raya Idulfitri"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-05",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1953, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))

    def test_eid_al_fitr_second_day(self):
        name = "Hari kedua dari Hari Raya Idulfitri"
        self.assertHolidayName(
            name,
            "2018-06-16",
            "2019-06-06",
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-23",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1953, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))

    def test_eid_al_adha(self):
        name = "Hari Raya Iduladha"
        self.assertHolidayName(
            name,
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1953, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))

    def test_islamic_new_year(self):
        name = "Tahun Baru Islam"
        self.assertHolidayName(
            name,
            "2008-01-10",
            "2008-12-29",
            "2018-09-11",
            "2019-09-01",
            "2020-08-20",
            "2021-08-11",
            "2022-07-30",
            "2023-07-19",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1953, 1963)).issubset(years_found))
        self.assertTrue(set(range(1968, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))
        self.assertFalse(set(range(1963, 1968)).intersection(years_found))

    def test_prophets_birthday(self):
        name = "Maulid Nabi Muhammad"
        self.assertHolidayName(
            name,
            "2018-11-20",
            "2019-11-09",
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1953, 1963)).issubset(years_found))
        self.assertTrue(set(range(1968, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))
        self.assertFalse(set(range(1963, 1968)).intersection(years_found))

    def test_prophets_ascension(self):
        name = "Isra Mikraj Nabi Muhammad"
        self.assertHolidayName(
            name,
            "2018-04-14",
            "2019-04-03",
            "2020-03-22",
            "2021-03-11",
            "2022-02-28",
            "2023-02-18",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1953, 1963)).issubset(years_found))
        self.assertTrue(set(range(1968, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))
        self.assertFalse(set(range(1963, 1968)).intersection(years_found))

    def test_nuzul_al_quran(self):
        name = "Nuzululqur'an"
        self.assertHoliday(
            "1953-05-30",
            "1954-05-20",
            "1955-05-10",
            "1956-04-28",
            "1957-04-17",
            "1958-04-06",
            "1959-03-27",
            "1960-03-15",
            "1961-03-04",
            "1962-02-21",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1953, 1963)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))
        self.assertFalse(set(range(1963, 2050)).intersection(years_found))

    def test_2021(self):
        self.assertHolidays(
            Indonesia(years=2021),
            ("2021-01-01", "Tahun Baru Masehi"),
            ("2021-02-12", "Tahun Baru Imlek"),
            ("2021-03-11", "Isra Mikraj Nabi Muhammad"),
            ("2021-03-14", "Hari Suci Nyepi"),
            ("2021-04-02", "Wafat Yesus Kristus"),
            ("2021-05-01", "Hari Buruh Internasional"),
            ("2021-05-13", "Hari Raya Idulfitri; Kenaikan Yesus Kristus"),
            ("2021-05-14", "Hari kedua dari Hari Raya Idulfitri"),
            ("2021-05-26", "Hari Raya Waisak"),
            ("2021-06-01", "Hari Lahir Pancasila"),
            ("2021-07-20", "Hari Raya Iduladha"),
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
            ("2022-02-28", "Isra Mikraj Nabi Muhammad"),
            ("2022-03-03", "Hari Suci Nyepi"),
            ("2022-04-15", "Wafat Yesus Kristus"),
            ("2022-05-01", "Hari Buruh Internasional"),
            ("2022-05-02", "Hari Raya Idulfitri"),
            ("2022-05-03", "Hari kedua dari Hari Raya Idulfitri"),
            ("2022-05-16", "Hari Raya Waisak"),
            ("2022-05-26", "Kenaikan Yesus Kristus"),
            ("2022-06-01", "Hari Lahir Pancasila"),
            ("2022-07-10", "Hari Raya Iduladha"),
            ("2022-07-30", "Tahun Baru Islam"),
            ("2022-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2022-10-08", "Maulid Nabi Muhammad"),
            ("2022-12-25", "Hari Raya Natal"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Tahun Baru Masehi"),
            ("2022-02-01", "Tahun Baru Imlek"),
            ("2022-02-28", "Isra Mikraj Nabi Muhammad"),
            ("2022-03-03", "Hari Suci Nyepi"),
            ("2022-04-15", "Wafat Yesus Kristus"),
            ("2022-04-29", "Cuti Bersama Hari Raya Idulfitri"),
            ("2022-05-01", "Hari Buruh Internasional"),
            ("2022-05-02", "Hari Raya Idulfitri"),
            ("2022-05-03", "Hari kedua dari Hari Raya Idulfitri"),
            ("2022-05-04", "Cuti Bersama Hari Raya Idulfitri"),
            ("2022-05-05", "Cuti Bersama Hari Raya Idulfitri"),
            ("2022-05-06", "Cuti Bersama Hari Raya Idulfitri"),
            ("2022-05-16", "Hari Raya Waisak"),
            ("2022-05-26", "Kenaikan Yesus Kristus"),
            ("2022-06-01", "Hari Lahir Pancasila"),
            ("2022-07-10", "Hari Raya Iduladha"),
            ("2022-07-30", "Tahun Baru Islam"),
            ("2022-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2022-10-08", "Maulid Nabi Muhammad"),
            ("2022-12-25", "Hari Raya Natal"),
            ("2022-12-26", "Cuti Bersama Hari Raya Natal"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-01", "Lunar New Year"),
            ("2022-02-28", "Isra' and Mi'raj"),
            ("2022-03-03", "Day of Silence"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-29", "Eid al-Fitr Joint Holiday"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-03", "Eid al-Fitr Second Day"),
            ("2022-05-04", "Eid al-Fitr Joint Holiday"),
            ("2022-05-05", "Eid al-Fitr Joint Holiday"),
            ("2022-05-06", "Eid al-Fitr Joint Holiday"),
            ("2022-05-16", "Buddha's Birthday"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-01", "Pancasila Day"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-07-30", "Islamic New Year"),
            ("2022-08-17", "Independence Day"),
            ("2022-10-08", "Prophet's Birthday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Joint Holiday"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-02-01", "Китайський Новий рік"),
            ("2022-02-28", "Вознесіння пророка Мухаммада"),
            ("2022-03-03", "День тиші"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-29", "Додатковий вихідний на Курбан-байрам"),
            ("2022-05-01", "Міжнародний день праці"),
            ("2022-05-02", "Рамазан-байрам"),
            ("2022-05-03", "Другий день Рамазан-байрам"),
            ("2022-05-04", "Додатковий вихідний на Курбан-байрам"),
            ("2022-05-05", "Додатковий вихідний на Курбан-байрам"),
            ("2022-05-06", "Додатковий вихідний на Курбан-байрам"),
            ("2022-05-16", "День народження Будди"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-01", "День Панчасіла"),
            ("2022-07-10", "Курбан-байрам"),
            ("2022-07-30", "Ісламський Новий рік"),
            ("2022-08-17", "День незалежності Республіки Індонезія"),
            ("2022-10-08", "День народження пророка Мухаммада"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Додатковий вихідний на Різдво Христове"),
        )
