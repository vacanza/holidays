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
        name = "Neujahr"
        years_absent = {2017, 2022, 2023, 2028, 2033, 2034, 2039, 2040, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-01-01" for year in self.full_range if year not in years_absent)
        )

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
        name = "Erster Mai"
        years_absent = {2016, 2021, 2022, 2027, 2032, 2033, 2038, 2039, 2044, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in self.full_range if year not in years_absent)
        )

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
        self.assertHolidayName(name, (f"{year}-10-03" for year in range(self.start_year, 2020)))
        self.assertNoHolidayName(name, range(2020, self.end_year))

    def test_christmas_eve(self):
        name = "Heiligabend"
        years_absent = {2016, 2017, 2022, 2023, 2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-24" for year in self.full_range if year not in years_absent)
        )

    def test_christmas_day(self):
        name = "Erster Weihnachtstag"
        years_absent = {2016, 2021, 2022, 2027, 2032, 2033, 2038, 2039, 2044, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-25" for year in self.full_range if year not in years_absent)
        )

    def test_second_day_of_christmas(self):
        name = "Zweiter Weihnachtstag"
        years_absent = {2020, 2021, 2026, 2027, 2032, 2037, 2038, 2043, 2048, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-26" for year in self.full_range if year not in years_absent)
        )

    def test_new_years_eve(self):
        name = "Silvester"
        years_absent = {2016, 2017, 2022, 2023, 2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-31" for year in self.full_range if year not in years_absent)
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-04-15", "Karfreitag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-12-26", "Zweiter Weihnachtstag"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Neujahr"),
            ("2026-04-03", "Karfreitag"),
            ("2026-04-06", "Ostermontag"),
            ("2026-05-01", "Erster Mai"),
            ("2026-12-24", "Heiligabend"),
            ("2026-12-25", "Erster Weihnachtstag"),
            ("2026-12-31", "Silvester"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2019-01-01", "Neujahr"),
            ("2019-04-19", "Karfreitag"),
            ("2019-04-22", "Ostermontag"),
            ("2019-05-01", "Erster Mai"),
            ("2019-06-10", "Pfingstmontag"),
            ("2019-10-03", "Tag der Deutschen Einheit"),
            ("2019-12-24", "Heiligabend"),
            ("2019-12-25", "Erster Weihnachtstag"),
            ("2019-12-26", "Zweiter Weihnachtstag"),
            ("2019-12-31", "Silvester"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2019-01-01", "New Year's Day"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-05-01", "Labor Day"),
            ("2019-06-10", "Pentecost Monday"),
            ("2019-10-03", "German Unity Day"),
            ("2019-12-24", "Christmas Eve"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-26", "Second Day of Christmas"),
            ("2019-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2019-01-01", "วันขึ้นปีใหม่"),
            ("2019-04-19", "วันศุกร์ประเสริฐ"),
            ("2019-04-22", "วันจันทร์อีสเตอร์"),
            ("2019-05-01", "วันแรงงาน"),
            ("2019-06-10", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2019-10-03", "วันรวมชาติเยอรมัน"),
            ("2019-12-24", "วันคริสต์มาสอีฟ"),
            ("2019-12-25", "วันคริสต์มาสวันแรก"),
            ("2019-12-26", "วันคริสต์มาสวันที่สอง"),
            ("2019-12-31", "วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2019-01-01", "Новий рік"),
            ("2019-04-19", "Страсна пʼятниця"),
            ("2019-04-22", "Великодній понеділок"),
            ("2019-05-01", "День праці"),
            ("2019-06-10", "Другий день Пʼятидесятниці"),
            ("2019-10-03", "День німецької єдності"),
            ("2019-12-24", "Святий вечір"),
            ("2019-12-25", "Перший день Різдва"),
            ("2019-12-26", "Другий день Різдва"),
            ("2019-12-31", "Переддень Нового року"),
        )
