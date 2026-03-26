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

from holidays.financial.germany_exchange import GermanyStockExchange
from tests.common import CommonFinancialTests


class TestGermanyStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GermanyStockExchange)

    def test_special_holidays(self):
        self.assertHoliday("2017-10-31")

    def test_new_years_day(self):
        self.assertHolidayName("Neujahr", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Karfreitag"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Ostermontag"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Erster Mai", (f"{year}-05-01" for year in self.full_range))

    def test_whit_monday(self):
        name = "Pfingstmontag"
        self.assertHolidayName(
            name,
            "2016-05-16",
            "2017-06-05",
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
        )
        self.assertNoHolidayName(name, range(2022, self.end_year))

    def test_german_unity_day(self):
        name = "Tag der Deutschen Einheit"
        self.assertHolidayName(name, (f"{year}-10-03" for year in range(self.start_year, 2022)))
        self.assertNoHolidayName(name, range(2022, self.end_year))

    def test_christmas_eve(self):
        self.assertHolidayName("Heiligabend", (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Erster Weihnachtstag", (f"{year}-12-25" for year in self.full_range)
        )

    def test_second_day_of_christmas(self):
        self.assertHolidayName(
            "Zweiter Weihnachtstag", (f"{year}-12-26" for year in self.full_range)
        )

    def test_new_years_eve(self):
        self.assertHolidayName("Silvester", (f"{year}-12-31" for year in self.full_range))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2020-01-01", "Neujahr"),
            ("2020-04-10", "Karfreitag"),
            ("2020-04-13", "Ostermontag"),
            ("2020-05-01", "Erster Mai"),
            ("2020-06-01", "Pfingstmontag"),
            ("2020-10-03", "Tag der Deutschen Einheit"),
            ("2020-12-24", "Heiligabend"),
            ("2020-12-25", "Erster Weihnachtstag"),
            ("2020-12-26", "Zweiter Weihnachtstag"),
            ("2020-12-31", "Silvester"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-01", "Labor Day"),
            ("2020-06-01", "Whit Monday"),
            ("2020-10-03", "German Unity Day"),
            ("2020-12-24", "Christmas Eve"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Second Day of Christmas"),
            ("2020-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2020-01-01", "วันขึ้นปีใหม่"),
            ("2020-04-10", "วันศุกร์ประเสริฐ"),
            ("2020-04-13", "วันจันทร์อีสเตอร์"),
            ("2020-05-01", "วันแรงงาน"),
            ("2020-06-01", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2020-10-03", "วันรวมชาติเยอรมัน"),
            ("2020-12-24", "วันคริสต์มาสอีฟ"),
            ("2020-12-25", "วันคริสต์มาสวันแรก"),
            ("2020-12-26", "วันคริสต์มาสวันที่สอง"),
            ("2020-12-31", "วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2020-01-01", "Новий рік"),
            ("2020-04-10", "Страсна пʼятниця"),
            ("2020-04-13", "Великодній понеділок"),
            ("2020-05-01", "День праці"),
            ("2020-06-01", "День Святого Духа"),
            ("2020-10-03", "День німецької єдності"),
            ("2020-12-24", "Святий вечір"),
            ("2020-12-25", "Перший день Різдва"),
            ("2020-12-26", "Другий день Різдва"),
            ("2020-12-31", "Переддень Нового року"),
        )
