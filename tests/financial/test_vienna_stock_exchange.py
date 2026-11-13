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

    def test_2018(self):
        self.assertHolidaysInYear(
            2018,
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

    def test_2019(self):
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "Neujahr"),
            ("2019-04-19", "Karfreitag"),
            ("2019-04-22", "Ostermontag"),
            ("2019-05-01", "Staatsfeiertag"),
            ("2019-06-10", "Pfingstmontag"),
            ("2019-12-24", "Heiliger Abend"),
            ("2019-12-25", "Christtag"),
            ("2019-12-26", "Stephanstag"),
            ("2019-12-31", "Silvester"),
        )

    def test_2020(self):
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "Neujahr"),
            ("2020-04-10", "Karfreitag"),
            ("2020-04-13", "Ostermontag"),
            ("2020-05-01", "Staatsfeiertag"),
            ("2020-06-01", "Pfingstmontag"),
            ("2020-10-26", "Nationalfeiertag"),
            ("2020-12-24", "Heiliger Abend"),
            ("2020-12-25", "Christtag"),
            ("2020-12-31", "Silvester"),
        )

    def test_2021(self):
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "Neujahr"),
            ("2021-04-02", "Karfreitag"),
            ("2021-04-05", "Ostermontag"),
            ("2021-05-24", "Pfingstmontag"),
            ("2021-10-26", "Nationalfeiertag"),
            ("2021-12-24", "Heiliger Abend"),
            ("2021-12-31", "Silvester"),
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-04-15", "Karfreitag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-10-26", "Nationalfeiertag"),
            ("2022-12-26", "Stephanstag"),
        )

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-04-07", "Karfreitag"),
            ("2023-04-10", "Ostermontag"),
            ("2023-05-01", "Staatsfeiertag"),
            ("2023-10-26", "Nationalfeiertag"),
            ("2023-12-25", "Christtag"),
            ("2023-12-26", "Stephanstag"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Neujahr"),
            ("2024-03-29", "Karfreitag"),
            ("2024-04-01", "Ostermontag"),
            ("2024-05-01", "Staatsfeiertag"),
            ("2024-12-24", "Heiliger Abend"),
            ("2024-12-25", "Christtag"),
            ("2024-12-26", "Stephanstag"),
            ("2024-12-31", "Silvester"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Neujahr"),
            ("2025-04-18", "Karfreitag"),
            ("2025-04-21", "Ostermontag"),
            ("2025-05-01", "Staatsfeiertag"),
            ("2025-12-24", "Heiliger Abend"),
            ("2025-12-25", "Christtag"),
            ("2025-12-26", "Stephanstag"),
            ("2025-12-31", "Silvester"),
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

    def test_2027(self):
        self.assertHolidaysInYear(
            2027,
            ("2027-01-01", "Neujahr"),
            ("2027-03-26", "Karfreitag"),
            ("2027-03-29", "Ostermontag"),
            ("2027-10-26", "Nationalfeiertag"),
            ("2027-12-24", "Heiliger Abend"),
            ("2027-12-31", "Silvester"),
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
