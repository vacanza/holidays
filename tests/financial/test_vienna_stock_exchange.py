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

from holidays.financial.vienna_stock_exchange import ViennaStockExchange
from tests.common import CommonFinancialTests


class TestViennaStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ViennaStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_new_years_day(self):
        name = "Neujahr"
        years_absent = {2022, 2023, 2028, 2033, 2034, 2039, 2040, 2045}
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
        name = "Staatsfeiertag"
        years_absent = {2021, 2022, 2027, 2032, 2033, 2038, 2039, 2044, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in self.full_range if year not in years_absent)
        )

    def test_ascension_day(self):
        name = "Christi Himmelfahrt"
        self.assertHolidayName(name, "2018-05-10")
        self.assertNoHolidayName(name, range(2019, self.end_year))

    def test_whit_monday(self):
        name = "Pfingstmontag"
        self.assertHolidayName(
            name,
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
        )
        self.assertNoHolidayName(name, range(2023, self.end_year))

    def test_corpus_christi(self):
        name = "Fronleichnam"
        self.assertHolidayName(name, "2018-05-31")
        self.assertNoHolidayName(name, range(2019, self.end_year))

    def test_assumption_day(self):
        name = "Mariä Himmelfahrt"
        self.assertHolidayName(name, "2018-08-15")
        self.assertNoHolidayName(name, range(2019, self.end_year))

    def test_national_day(self):
        name = "Nationalfeiertag"
        years_absent = {2019, 2024, 2025, 2030, 2031, 2036, 2041, 2042, 2047}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-10-26" for year in self.full_range if year not in years_absent)
        )

    def test_all_saints_day(self):
        name = "Allerheiligen"
        self.assertHolidayName(name, "2018-11-01")
        self.assertNoHolidayName(name, range(2019, self.end_year))

    def test_christmas_eve(self):
        name = "Heiliger Abend"
        years_absent = {2022, 2023, 2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-24" for year in self.full_range if year not in years_absent)
        )

    def test_christmas_day(self):
        name = "Christtag"
        years_absent = {2021, 2022, 2027, 2032, 2033, 2038, 2039, 2044, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-25" for year in self.full_range if year not in years_absent)
        )

    def test_saint_stephens_day(self):
        name = "Stephanstag"
        years_absent = {2020, 2021, 2026, 2027, 2032, 2037, 2038, 2043, 2048, 2049}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-26" for year in self.full_range if year not in years_absent)
        )

    def test_new_years_eve(self):
        name = "Silvester"
        years_absent = {2022, 2023, 2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-31" for year in self.full_range if year not in years_absent)
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Neujahr"),
            ("2026-04-03", "Karfreitag"),
            ("2026-04-06", "Ostermontag"),
            ("2026-05-01", "Staatsfeiertag"),
            ("2026-10-26", "Nationalfeiertag"),
            ("2026-12-24", "Heiliger Abend"),
            ("2026-12-25", "Christtag"),
            ("2026-12-31", "Silvester"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Neujahr"),
            ("2018-03-30", "Karfreitag"),
            ("2018-04-02", "Ostermontag"),
            ("2018-05-01", "Staatsfeiertag"),
            ("2018-05-10", "Christi Himmelfahrt"),
            ("2018-05-21", "Pfingstmontag"),
            ("2018-05-31", "Fronleichnam"),
            ("2018-08-15", "Mariä Himmelfahrt"),
            ("2018-10-26", "Nationalfeiertag"),
            ("2018-11-01", "Allerheiligen"),
            ("2018-12-24", "Heiliger Abend"),
            ("2018-12-25", "Christtag"),
            ("2018-12-26", "Stephanstag"),
            ("2018-12-31", "Silvester"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-03-30", "Good Friday"),
            ("2018-04-02", "Easter Monday"),
            ("2018-05-01", "Labor Day"),
            ("2018-05-10", "Ascension Day"),
            ("2018-05-21", "Pentecost Monday"),
            ("2018-05-31", "Corpus Christi"),
            ("2018-08-15", "Assumption Day"),
            ("2018-10-26", "National Day"),
            ("2018-11-01", "All Saints' Day"),
            ("2018-12-24", "Christmas Eve"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Saint Stephen's Day"),
            ("2018-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2018-01-01", "วันขึ้นปีใหม่"),
            ("2018-03-30", "วันศุกร์ประเสริฐ"),
            ("2018-04-02", "วันจันทร์อีสเตอร์"),
            ("2018-05-01", "วันแรงงาน"),
            ("2018-05-10", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2018-05-21", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2018-05-31", "วันสมโภชพระคริสตวรกาย"),
            ("2018-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2018-10-26", "วันชาติออสเตรีย"),
            ("2018-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2018-12-24", "วันคริสต์มาสอีฟ"),
            ("2018-12-25", "วันคริสต์มาส"),
            ("2018-12-26", "วันสมโภชนักบุญสเตเฟน"),
            ("2018-12-31", "วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2018-01-01", "Новий рік"),
            ("2018-03-30", "Страсна пʼятниця"),
            ("2018-04-02", "Великодній понеділок"),
            ("2018-05-01", "День праці"),
            ("2018-05-10", "Вознесіння Господнє"),
            ("2018-05-21", "Другий день Пʼятидесятниці"),
            ("2018-05-31", "Свято Тіла і Крові Христових"),
            ("2018-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2018-10-26", "Національне свято"),
            ("2018-11-01", "День усіх святих"),
            ("2018-12-24", "Святий вечір"),
            ("2018-12-25", "Різдво Христове"),
            ("2018-12-26", "День Святого Стефана"),
            ("2018-12-31", "Переддень Нового року"),
        )
