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

from holidays.constants import GOVERNMENT, PUBLIC
from holidays.countries.indonesia import Indonesia, ID, IDN
from tests.common import CommonCountryTests


class TestIndonesia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Indonesia, years=range(1946, 2050), years_non_observed=(2004, 2020))

    def test_country_aliases(self):
        self.assertAliases(Indonesia, ID, IDN)

    def test_no_holidays(self):
        self.assertNoHolidays(Indonesia(years=1945, categories=(GOVERNMENT, PUBLIC)))

    def test_special(self):
        dt = (
            # All Election Types.
            "1999-06-07",
            "2004-04-05",
            "2004-07-05",
            "2004-09-20",
            "2009-04-09",
            "2009-07-08",
            "2014-04-09",
            "2014-07-09",
            "2015-12-09",
            "2017-02-15",
            "2018-06-27",
            "2019-04-17",
            "2020-12-09",
            "2024-02-14",
            "2024-11-27",
        )
        dt_observed = ("2004-11-16",)
        self.assertHoliday(dt, dt_observed)
        self.assertNoNonObservedHoliday(dt_observed)

    def test_special_government(self):
        dt = (
            # Joint Holidays (Cuti Bersama)
            "2002-12-05",
            "2002-12-09",
            "2002-12-10",
            "2002-12-26",
            "2003-11-24",
            "2003-11-27",
            "2003-11-28",
            "2003-12-26",
            "2004-11-17",
            "2004-11-18",
            "2004-11-19",
            "2005-11-02",
            "2005-11-05",
            "2005-11-07",
            "2005-11-08",
            "2006-03-31",
            "2006-05-26",
            "2006-08-18",
            "2006-10-23",
            "2006-10-26",
            "2006-10-27",
            "2007-05-18",
            "2007-10-12",
            "2007-10-15",
            "2007-10-16",
            "2007-10-17",
            "2007-10-18",
            "2007-10-19",
            "2007-12-21",
            "2007-12-24",
            "2007-12-26",
            "2007-12-31",
            "2008-01-11",
            "2008-09-29",
            "2008-09-30",
            "2008-10-03",
            "2008-12-26",
            "2009-01-02",
            "2009-09-18",
            "2009-09-23",
            "2009-12-24",
            "2010-09-09",
            "2010-09-13",
            "2010-12-24",
            "2011-05-16",
            "2011-08-29",
            "2011-09-01",
            "2011-09-02",
            "2011-12-26",
            "2012-05-18",
            "2012-08-21",
            "2012-08-22",
            "2012-11-16",
            "2012-12-24",
            "2012-12-31",
            "2013-08-05",
            "2013-08-06",
            "2013-08-07",
            "2013-10-14",
            "2013-12-26",
            "2014-07-30",
            "2014-07-31",
            "2014-08-01",
            "2014-12-26",
            "2015-07-16",
            "2015-07-20",
            "2015-07-21",
            "2016-07-04",
            "2016-07-05",
            "2016-07-08",
            "2016-12-26",
            "2017-01-02",
            "2017-06-23",
            "2017-06-27",
            "2017-06-28",
            "2017-06-29",
            "2017-06-30",
            "2017-12-26",
            "2018-06-11",
            "2018-06-12",
            "2018-06-13",
            "2018-06-14",
            "2018-06-18",
            "2018-06-19",
            "2018-06-20",
            "2018-12-24",
            "2019-06-03",
            "2019-06-04",
            "2019-06-07",
            "2019-12-24",
            "2020-08-21",
            "2020-10-28",
            "2020-10-30",
            "2020-12-24",
            "2021-05-12",
            "2022-04-29",
            "2022-05-04",
            "2022-05-05",
            "2022-05-06",
            "2023-01-23",
            "2023-03-23",
            "2023-04-19",
            "2023-04-20",
            "2023-04-21",
            "2023-04-24",
            "2023-04-25",
            "2023-06-02",
            "2023-06-28",
            "2023-06-30",
            "2023-12-26",
            "2024-02-09",
            "2024-03-12",
            "2024-04-08",
            "2024-04-09",
            "2024-04-12",
            "2024-04-15",
            "2024-05-10",
            "2024-05-24",
            "2024-06-18",
            "2024-12-26",
            "2025-01-28",
            "2025-03-28",
            "2025-04-02",
            "2025-04-03",
            "2025-04-04",
            "2025-04-07",
            "2025-05-13",
            "2025-05-30",
            "2025-06-09",
            "2025-12-26",
        )
        dt_observed = ("2020-12-31",)
        self.assertHoliday(Indonesia(categories=GOVERNMENT), dt, dt_observed)
        self.assertNoNonObservedHoliday(
            Indonesia(categories=GOVERNMENT, observed=False),
            dt_observed,
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
        self.assertTrue(set(range(2003, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 2003)).intersection(years_found))

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
        self.assertHolidayName(name, range(1953, 1964), range(1971, 2050))
        self.assertNoHolidayName(name, range(1946, 1953), range(1964, 1971))

    def test_easter_sunday(self):
        name = "Kebangkitan Yesus Kristus"
        self.assertHolidayName(
            name,
            "2024-03-31",
            "2025-04-20",
            "2026-04-05",
            "2027-03-28",
            "2028-04-16",
            "2029-04-01",
            "2030-04-21",
        )
        self.assertHolidayName(name, range(2024, 2050))
        self.assertNoHolidayName(name, range(1946, 2024))

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
        self.assertHolidayName(name, range(1953, 1964))
        self.assertNoHolidayName(name, range(1946, 1953), range(1964, 2050))

    def test_vesak_day(self):
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
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1953, 1968)))
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2014, 2050)))
        self.assertNoHoliday(
            f"{year}-05-01" for year in set(range(1968, 2014)).difference({2004, 2008})
        )
        self.assertNoHolidayName(name, range(1968, 2014))

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
        self.assertHolidayName(name, range(1953, 1964), range(1968, 2050))
        self.assertNoHolidayName(name, range(1946, 1953), range(1964, 1968))

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
        self.assertHolidayName(name, range(1953, 1964))
        self.assertNoHolidayName(name, range(1946, 1953), range(1964, 2050))

    def test_pancasila_day(self):
        name = "Hari Lahir Pancasila"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2016, 2050)))
        self.assertNoHolidayName(
            name, (f"{year}-06-01" for year in set(range(1946, 2016)).difference({2000, 2007}))
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
        self.assertNoHolidayName(name, (f"{year}-12-25" for year in range(1946, 1953)))

    def test_eid_al_fitr(self):
        name = "Hari Raya Idul Fitri"
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
        name = "Hari kedua dari Hari Raya Idul Fitri"
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
        name = "Hari Raya Idul Adha"
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
        self.assertTrue(set(range(1953, 1964)).issubset(years_found))
        self.assertTrue(set(range(1968, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))
        self.assertFalse(set(range(1964, 1968)).intersection(years_found))

    def test_prophets_birthday(self):
        name = "Maulid Nabi Muhammad"
        self.assertHolidayName(
            name,
            "2018-11-20",
            "2019-11-09",
            "2020-10-29",
            "2021-10-20",
            "2022-10-08",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1953, 1964)).issubset(years_found))
        self.assertTrue(set(range(1968, 2050)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))
        self.assertFalse(set(range(1964, 1968)).intersection(years_found))

    def test_isra_and_miraj(self):
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
        self.assertTrue(set(range(1953, 1964)).issubset(years_found))
        self.assertFalse(set(range(1946, 1953)).intersection(years_found))
        self.assertFalse(set(range(1964, 2050)).intersection(years_found))

    def test_2021(self):
        self.assertHolidays(
            Indonesia(years=2021),
            ("2021-01-01", "Tahun Baru Masehi"),
            ("2021-02-12", "Tahun Baru Imlek"),
            ("2021-03-11", "Isra Mikraj Nabi Muhammad"),
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
            ("2021-10-20", "Maulid Nabi Muhammad"),
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

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Tahun Baru Masehi"),
            ("2022-02-01", "Tahun Baru Imlek"),
            ("2022-02-28", "Isra Mikraj Nabi Muhammad"),
            ("2022-03-03", "Hari Suci Nyepi"),
            ("2022-04-15", "Wafat Yesus Kristus"),
            ("2022-04-29", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2022-05-01", "Hari Buruh Internasional"),
            ("2022-05-02", "Hari Raya Idul Fitri"),
            ("2022-05-03", "Hari kedua dari Hari Raya Idul Fitri"),
            ("2022-05-04", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2022-05-05", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2022-05-06", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2022-05-16", "Hari Raya Waisak"),
            ("2022-05-26", "Kenaikan Yesus Kristus"),
            ("2022-06-01", "Hari Lahir Pancasila"),
            ("2022-07-10", "Hari Raya Idul Adha"),
            ("2022-07-30", "Tahun Baru Islam"),
            ("2022-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2022-10-08", "Maulid Nabi Muhammad"),
            ("2022-12-25", "Hari Raya Natal"),
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
            ("2022-05-16", "Vesak Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-01", "Pancasila Day"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-07-30", "Islamic New Year"),
            ("2022-08-17", "Independence Day"),
            ("2022-10-08", "Prophet's Birthday"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-02-01", "วันตรุษจีน"),
            ("2022-02-28", "วันเมี๊ยะราจ"),
            ("2022-03-03", "วันแห่งความเงียบ"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-29", "หยุดร่วมพิเศษวันอีฎิ้ลฟิตริ"),
            ("2022-05-01", "วันแรงงานสากล"),
            ("2022-05-02", "วันอีฎิ้ลฟิตริ"),
            ("2022-05-03", "วันอีฎิ้ลฟิตริวันที่สอง"),
            ("2022-05-04", "หยุดร่วมพิเศษวันอีฎิ้ลฟิตริ"),
            ("2022-05-05", "หยุดร่วมพิเศษวันอีฎิ้ลฟิตริ"),
            ("2022-05-06", "หยุดร่วมพิเศษวันอีฎิ้ลฟิตริ"),
            ("2022-05-16", "วันวิสาขบูชา"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-01", "วันปัญจศีล"),
            ("2022-07-10", "วันอีดิ้ลอัฎฮา"),
            ("2022-07-30", "วันขึ้นปีใหม่อิสลาม"),
            ("2022-08-17", "วันประกาศอิสรภาพสาธารณรัฐอินโดนีเซีย"),
            ("2022-10-08", "วันเมาลิดนบี"),
            ("2022-12-25", "วันคริสต์มาส"),
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
        )
