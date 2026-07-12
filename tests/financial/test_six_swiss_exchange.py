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

from holidays.financial.six_swiss_exchange import SIXSwissExchange, XSWX, SIX
from tests.common import CommonFinancialTests


class TestSIXSwissExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SIXSwissExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_market_aliases(self):
        self.assertAliases(SIXSwissExchange, XSWX, SIX)

    def test_no_holidays(self):
        self.assertNoHolidays(SIXSwissExchange(years=1999))

    def test_berchtolds_day(self):
        name = "Berchtoldstag"
        self.assertNonObservedHolidayName(name, (f"{year}-01-02" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2020-01-02",
            "2023-01-02",
            "2024-01-02",
            "2025-01-02",
        )
        self.assertNoHoliday(
            "2021-01-02",
            "2022-01-02",
        )

    def test_christmas_eve(self):
        name = "Heiligabend"
        self.assertNonObservedHolidayName(name, (f"{year}-12-24" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2020-12-24",
            "2021-12-24",
            "2024-12-24",
            "2025-12-24",
        )
        self.assertNoHoliday(
            "2022-12-24",
            "2023-12-24",
        )

    def test_new_years_eve(self):
        name = "Vortag vor Neujahr"
        self.assertNonObservedHolidayName(name, (f"{year}-12-31" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2020-12-31",
            "2021-12-31",
            "2024-12-31",
            "2025-12-31",
        )
        self.assertNoHoliday(
            "2022-12-31",
            "2023-12-31",
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Neujahrstag"),
            ("2025-01-02", "Berchtoldstag"),
            ("2025-04-18", "Karfreitag"),
            ("2025-04-21", "Ostermontag"),
            ("2025-05-01", "Tag der Arbeit"),
            ("2025-05-29", "Auffahrt"),
            ("2025-06-09", "Pfingstmontag"),
            ("2025-08-01", "Nationalfeiertag"),
            ("2025-12-24", "Heiligabend"),
            ("2025-12-25", "Weihnachten"),
            ("2025-12-26", "Stephanstag"),
            ("2025-12-31", "Vortag vor Neujahr"),
        )

    def test_l10n_de(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Neujahrstag"),
            ("2024-01-02", "Berchtoldstag"),
            ("2024-03-29", "Karfreitag"),
            ("2024-04-01", "Ostermontag"),
            ("2024-05-01", "Tag der Arbeit"),
            ("2024-05-09", "Auffahrt"),
            ("2024-05-20", "Pfingstmontag"),
            ("2024-08-01", "Nationalfeiertag"),
            ("2024-12-24", "Heiligabend"),
            ("2024-12-25", "Weihnachten"),
            ("2024-12-26", "Stephanstag"),
            ("2024-12-31", "Vortag vor Neujahr"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "Saint Berchtold's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-09", "Ascension Day"),
            ("2024-05-20", "Pentecost Monday"),
            ("2024-08-01", "National Day"),
            ("2024-12-24", "Christmas Eve"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Saint Stephen's Day"),
            ("2024-12-31", "New Year's Eve"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2024-01-01", "Nouvel An"),
            ("2024-01-02", "Saint-Berchtold"),
            ("2024-03-29", "Vendredi saint"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-09", "Ascension"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-08-01", "Fête nationale"),
            ("2024-12-24", "Veille de Noël"),
            ("2024-12-25", "Noël"),
            ("2024-12-26", "Saint-Étienne"),
            ("2024-12-31", "Réveillon de la Saint-Sylvestre"),
        )

    def test_l10n_it(self):
        self.assertLocalizedHolidays(
            "it",
            ("2024-01-01", "Capodanno"),
            ("2024-01-02", "Giorno di Bertoldo"),
            ("2024-03-29", "Venerdì Santo"),
            ("2024-04-01", "Lunedì dell'Angelo"),
            ("2024-05-01", "Festa del lavoro"),
            ("2024-05-09", "Ascensione di Gesù"),
            ("2024-05-20", "Lunedì di Pentecoste"),
            ("2024-08-01", "Festa nazionale"),
            ("2024-12-24", "Vigilia di Natale"),
            ("2024-12-25", "Natale"),
            ("2024-12-26", "Giorno di Santo Stefano"),
            ("2024-12-31", "Vigilia di Capodanno"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-01-02", "วันสมโภชนักบุญแบร์กโทลด์"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-04-01", "วันจันทร์อีสเตอร์"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-05-09", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2024-05-20", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2024-08-01", "วันชาติสวิตเซอร์แลนด์"),
            ("2024-12-24", "วันคริสต์มาสอีฟ"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-26", "วันสมโภชนักบุญสเตเฟน"),
            ("2024-12-31", "วันส่งท้ายปีเก่า"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-01-02", "День Святого Бертольда"),
            ("2024-03-29", "Страсна пʼятниця"),
            ("2024-04-01", "Великодній понеділок"),
            ("2024-05-01", "День праці"),
            ("2024-05-09", "Вознесіння Господнє"),
            ("2024-05-20", "Другий день Пʼятидесятниці"),
            ("2024-08-01", "Національне свято"),
            ("2024-12-24", "Святвечір"),
            ("2024-12-25", "Різдво Христове"),
            ("2024-12-26", "День Святого Стефана"),
            ("2024-12-31", "Переддень Нового року"),
        )
