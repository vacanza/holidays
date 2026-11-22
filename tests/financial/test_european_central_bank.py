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

from holidays.financial.european_central_bank import EuropeanCentralBank
from tests.common import CommonFinancialTests


class TestEuropeanCentralBank(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EuropeanCentralBank)

    def test_special_holidays(self):
        self.assertHoliday(
            "1999-12-31",
            "2001-12-31",
        )

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, range(2000, self.end_year))
        self.assertNoHolidayName(name, 1999)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, range(2000, self.end_year))
        self.assertNoHolidayName(name, 1999)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2000, self.end_year)))
        self.assertNoHolidayName(name, 1999)

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_christmas_holiday(self):
        name = "Christmas Holiday"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2000, self.end_year)))
        self.assertNoHolidayName(name, 1999)

    def test_1999(self):
        self.assertHolidays(
            EuropeanCentralBank(years=1999),
            ("1999-01-01", "New Year's Day"),
            ("1999-12-25", "Christmas Day"),
            ("1999-12-31", "Additional closing day"),
        )

    def test_2015(self):
        self.assertHolidays(
            EuropeanCentralBank(years=2015),
            ("2015-01-01", "New Year's Day"),
            ("2015-04-03", "Good Friday"),
            ("2015-04-06", "Easter Monday"),
            ("2015-05-01", "Labour Day"),
            ("2015-12-25", "Christmas Day"),
            ("2015-12-26", "Christmas Holiday"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2001-01-01", "New Year's Day"),
            ("2001-04-13", "Good Friday"),
            ("2001-04-16", "Easter Monday"),
            ("2001-05-01", "Labour Day"),
            ("2001-12-25", "Christmas Day"),
            ("2001-12-26", "Christmas Holiday"),
            ("2001-12-31", "Additional closing day"),
        )

    def test_l10n_de(self):
        self.assertLocalizedHolidays(
            "de",
            ("2001-01-01", "Neujahr"),
            ("2001-04-13", "Karfreitag"),
            ("2001-04-16", "Ostermontag"),
            ("2001-05-01", "Tag der Arbeit"),
            ("2001-12-25", "Erster Weihnachtsfeiertag"),
            ("2001-12-26", "Zweiter Weihnachtsfeiertag"),
            ("2001-12-31", "Zusätzlicher Schließungstag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2001-01-01", "New Year's Day"),
            ("2001-04-13", "Good Friday"),
            ("2001-04-16", "Easter Monday"),
            ("2001-05-01", "Labor Day"),
            ("2001-12-25", "Christmas Day"),
            ("2001-12-26", "Christmas Holiday"),
            ("2001-12-31", "Additional closing day"),
        )

    def test_l10n_es(self):
        self.assertLocalizedHolidays(
            "es",
            ("2001-01-01", "Año Nuevo"),
            ("2001-04-13", "Viernes Santo"),
            ("2001-04-16", "Lunes de Pascua"),
            ("2001-05-01", "Día del Trabajo"),
            ("2001-12-25", "Navidad"),
            ("2001-12-26", "Día de San Esteban"),
            ("2001-12-31", "Día de cierre adicional"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2001-01-01", "Nouvel An"),
            ("2001-04-13", "Vendredi saint"),
            ("2001-04-16", "Lundi de Pâques"),
            ("2001-05-01", "Fête du travail"),
            ("2001-12-25", "Noël"),
            ("2001-12-26", "Lendemain de Noël"),
            ("2001-12-31", "Jour de fermeture supplémentaire"),
        )

    def test_l10n_it(self):
        self.assertLocalizedHolidays(
            "it",
            ("2001-01-01", "Capodanno"),
            ("2001-04-13", "Venerdì Santo"),
            ("2001-04-16", "Lunedì dell'Angelo"),
            ("2001-05-01", "Festa del lavoro"),
            ("2001-12-25", "Natale"),
            ("2001-12-26", "Santo Stefano"),
            ("2001-12-31", "Giornata di chiusura aggiuntiva"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2001-01-01", "Новий рік"),
            ("2001-04-13", "Страсна пʼятниця"),
            ("2001-04-16", "Великодній понеділок"),
            ("2001-05-01", "День праці"),
            ("2001-12-25", "Різдво Христове"),
            ("2001-12-26", "Другий день Різдва"),
            ("2001-12-31", "Додатковий вихідний"),
        )
