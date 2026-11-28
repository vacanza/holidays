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

from holidays.financial.nasdaq_stockholm import NasdaqStockholm
from tests.common import CommonFinancialTests


class TestNasdaqStockholm(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NasdaqStockholm)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_new_years_day(self):
        name = "Nyårsdagen"
        years_absent = {2028, 2033, 2034, 2039, 2040, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-01-01" for year in self.full_range if year not in years_absent)
        )

    def test_epiphany(self):
        name = "Trettondedag jul"
        years_absent = {2024, 2029, 2030, 2035, 2036, 2041, 2046, 2047}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-01-06" for year in self.full_range if year not in years_absent)
        )

    def test_good_friday(self):
        name = "Långfredagen"
        self.assertHolidayName(
            name,
            "2024-03-29",
            "2025-04-18",
            "2026-04-03",
            "2027-03-26",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Annandag påsk"
        self.assertHolidayName(
            name,
            "2024-04-01",
            "2025-04-21",
            "2026-04-06",
            "2027-03-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_may_day(self):
        name = "Första maj"
        years_absent = {2027, 2032, 2033, 2038, 2039, 2044, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in self.full_range if year not in years_absent)
        )

    def test_ascension_day(self):
        name = "Kristi himmelsfärdsdag"
        self.assertHolidayName(
            name,
            "2024-05-09",
            "2025-05-29",
            "2026-05-14",
            "2027-05-06",
        )
        self.assertHolidayName(name, self.full_range)

    def test_national_day(self):
        name = "Nationaldagen"
        years_absent = {2026, 2027, 2032, 2037, 2038, 2043, 2048, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-06-06" for year in self.full_range if year not in years_absent)
        )

    def test_midsummer_eve(self):
        name = "Midsommarafton"
        self.assertHolidayName(
            name,
            "2024-06-21",
            "2025-06-20",
            "2026-06-19",
            "2027-06-25",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_eve(self):
        name = "Julafton"
        years_absent = {2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-24" for year in self.full_range if year not in years_absent)
        )

    def test_christmas_day(self):
        name = "Juldagen"
        years_absent = {2027, 2032, 2033, 2038, 2039, 2044, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-25" for year in self.full_range if year not in years_absent)
        )

    def test_second_day_of_christmas(self):
        name = "Annandag jul"
        years_absent = {2026, 2027, 2032, 2037, 2038, 2043, 2048, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-26" for year in self.full_range if year not in years_absent)
        )

    def test_new_years_eve(self):
        name = "Nyårsafton"
        years_absent = {2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-31" for year in self.full_range if year not in years_absent)
        )

    def test_twelfth_night(self):
        name = "Trettondagsafton"
        years_absent = {2025, 2030, 2031, 2036, 2041, 2042, 2047, 2048}
        self.assertNoHolidayName(name)
        self.assertNoHalfDayHolidayName(name, years_absent)
        self.assertHalfDayHolidayName(
            name, (f"{year}-01-05" for year in self.full_range if year not in years_absent)
        )

    def test_maundy_thursday(self):
        name = "Skärtorsdagen"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2024-03-28",
            "2025-04-17",
            "2026-04-02",
            "2027-03-25",
        )
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_walpurgis_night(self):
        name = "Valborgsmässoafton"
        years_absent = {2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name)
        self.assertNoHalfDayHolidayName(name, years_absent)
        self.assertHalfDayHolidayName(
            name, (f"{year}-04-30" for year in self.full_range if year not in years_absent)
        )

    def test_day_before_ascension_day(self):
        name = "Dag före Kristi himmelsfärdsdag"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2024-05-08",
            "2025-05-28",
            "2026-05-13",
            "2027-05-05",
        )
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_all_saints_eve(self):
        name = "Allahelgonsafton"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2024-11-01",
            "2025-10-31",
            "2026-10-30",
            "2027-11-05",
        )
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_excluded_swedish_bank_days(self):
        self.assertNoHoliday(
            "2025-05-30",
            "2025-06-05",
            "2025-06-19",
            "2025-12-23",
            "2025-12-30",
            "2026-05-15",
            "2026-06-05",
            "2026-06-18",
            "2026-12-23",
            "2026-12-30",
        )
        self.assertNoHalfDayHoliday(
            "2025-05-30",
            "2025-06-05",
            "2025-06-19",
            "2025-12-23",
            "2025-12-30",
            "2026-05-15",
            "2026-06-05",
            "2026-06-18",
            "2026-12-23",
            "2026-12-30",
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Nyårsdagen"),
            ("2025-01-06", "Trettondedag jul"),
            ("2025-04-18", "Långfredagen"),
            ("2025-04-21", "Annandag påsk"),
            ("2025-05-01", "Första maj"),
            ("2025-05-29", "Kristi himmelsfärdsdag"),
            ("2025-06-06", "Nationaldagen"),
            ("2025-06-20", "Midsommarafton"),
            ("2025-12-24", "Julafton"),
            ("2025-12-25", "Juldagen"),
            ("2025-12-26", "Annandag jul"),
            ("2025-12-31", "Nyårsafton"),
        )
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-04-17", "Skärtorsdagen"),
            ("2025-04-30", "Valborgsmässoafton"),
            ("2025-05-28", "Dag före Kristi himmelsfärdsdag"),
            ("2025-10-31", "Allahelgonsafton"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Nyårsdagen"),
            ("2026-01-06", "Trettondedag jul"),
            ("2026-04-03", "Långfredagen"),
            ("2026-04-06", "Annandag påsk"),
            ("2026-05-01", "Första maj"),
            ("2026-05-14", "Kristi himmelsfärdsdag"),
            ("2026-06-19", "Midsommarafton"),
            ("2026-12-24", "Julafton"),
            ("2026-12-25", "Juldagen"),
            ("2026-12-31", "Nyårsafton"),
        )
        self.assertHalfDayHolidaysInYear(
            2026,
            ("2026-01-05", "Trettondagsafton"),
            ("2026-04-02", "Skärtorsdagen"),
            ("2026-04-30", "Valborgsmässoafton"),
            ("2026-05-13", "Dag före Kristi himmelsfärdsdag"),
            ("2026-10-30", "Allahelgonsafton"),
        )

    def test_2027(self):
        self.assertHolidaysInYear(
            2027,
            ("2027-01-01", "Nyårsdagen"),
            ("2027-01-06", "Trettondedag jul"),
            ("2027-03-26", "Långfredagen"),
            ("2027-03-29", "Annandag påsk"),
            ("2027-05-06", "Kristi himmelsfärdsdag"),
            ("2027-06-25", "Midsommarafton"),
            ("2027-12-24", "Julafton"),
            ("2027-12-31", "Nyårsafton"),
        )
        self.assertHalfDayHolidaysInYear(
            2027,
            ("2027-01-05", "Trettondagsafton"),
            ("2027-03-25", "Skärtorsdagen"),
            ("2027-04-30", "Valborgsmässoafton"),
            ("2027-05-05", "Dag före Kristi himmelsfärdsdag"),
            ("2027-11-05", "Allahelgonsafton"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Nyårsdagen"),
            ("2025-01-06", "Trettondedag jul"),
            ("2025-04-17", "Skärtorsdagen"),
            ("2025-04-18", "Långfredagen"),
            ("2025-04-21", "Annandag påsk"),
            ("2025-04-30", "Valborgsmässoafton"),
            ("2025-05-01", "Första maj"),
            ("2025-05-28", "Dag före Kristi himmelsfärdsdag"),
            ("2025-05-29", "Kristi himmelsfärdsdag"),
            ("2025-06-06", "Nationaldagen"),
            ("2025-06-20", "Midsommarafton"),
            ("2025-10-31", "Allahelgonsafton"),
            ("2025-12-24", "Julafton"),
            ("2025-12-25", "Juldagen"),
            ("2025-12-26", "Annandag jul"),
            ("2025-12-31", "Nyårsafton"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-06", "Epiphany"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-30", "Walpurgis Night"),
            ("2025-05-01", "May Day"),
            ("2025-05-28", "Day before Ascension Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-06", "National Day"),
            ("2025-06-20", "Midsummer Eve"),
            ("2025-10-31", "All Saints' Eve"),
            ("2025-12-24", "Christmas Eve"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Second Day of Christmas"),
            ("2025-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2025-01-01", "วันขึ้นปีใหม่"),
            ("2025-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2025-04-17", "วันพฤหัสศักดิ์สิทธิ์"),
            ("2025-04-18", "วันศุกร์ประเสริฐ"),
            ("2025-04-21", "วันจันทร์อีสเตอร์"),
            ("2025-04-30", "คืนวัลเพอร์กิส"),
            ("2025-05-01", "วันเมย์เดย์ (วันแรงงาน)"),
            ("2025-05-28", "วันก่อนวันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2025-05-29", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2025-06-06", "วันชาติสวีเดน"),
            ("2025-06-20", "วันก่อนวันกลางฤดูร้อน"),
            ("2025-10-31", "วันก่อนวันสมโภชนักบุญทั้งหลาย"),
            ("2025-12-24", "วันคริสต์มาสอีฟ"),
            ("2025-12-25", "วันคริสต์มาส"),
            ("2025-12-26", "วันคริสต์มาสวันที่สอง"),
            ("2025-12-31", "วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2025-01-01", "Новий рік"),
            ("2025-01-06", "Богоявлення"),
            ("2025-04-17", "Великий четвер"),
            ("2025-04-18", "Страсна пʼятниця"),
            ("2025-04-21", "Великодній понеділок"),
            ("2025-04-30", "Вальпургієва ніч"),
            ("2025-05-01", "Перше травня"),
            ("2025-05-28", "Переддень Вознесіння Господнього"),
            ("2025-05-29", "Вознесіння Господнє"),
            ("2025-06-06", "Національний день"),
            ("2025-06-20", "Переддень літнього сонцестояння"),
            ("2025-10-31", "Переддень Дня усіх святих"),
            ("2025-12-24", "Святий вечір"),
            ("2025-12-25", "Різдво Христове"),
            ("2025-12-26", "Другий день Різдва"),
            ("2025-12-31", "Переддень Нового року"),
        )
