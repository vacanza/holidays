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

from holidays.financial.zagreb_stock_exchange import ZagrebStockExchange
from tests.common import CommonFinancialTests


class TestZagrebStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ZagrebStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_special_holidays(self):
        self.assertHolidayName("Uvođenje eura", "2022-12-29", "2022-12-30")
        self.assertNoHoliday("2022-12-28")
        self.assertHolidayName("Dan izbora zastupnika u Hrvatski sabor", "2024-04-17")

    def test_good_friday(self):
        name = "Veliki petak"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
            "2026-04-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_eve(self):
        name = "Badnjak"
        years_absent = {2016, 2017, 2022, 2023, 2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-24" for year in self.full_range if year not in years_absent)
        )

    def test_new_years_eve(self):
        name = "Stara godina"
        years_absent = {2016, 2017, 2022, 2023, 2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-31" for year in self.full_range if year not in years_absent)
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Nova godina"),
            ("2025-01-06", "Bogojavljenje ili Sveta tri kralja"),
            ("2025-04-18", "Veliki petak"),
            ("2025-04-21", "Uskrsni ponedjeljak"),
            ("2025-05-01", "Praznik rada"),
            ("2025-05-30", "Dan državnosti"),
            ("2025-06-19", "Tijelovo"),
            ("2025-08-05", "Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja"),
            ("2025-08-15", "Velika Gospa"),
            (
                "2025-11-18",
                "Dan sjećanja na žrtve Domovinskog rata i "
                "Dan sjećanja na žrtvu Vukovara i Škabrnje",
            ),
            ("2025-12-24", "Badnjak"),
            ("2025-12-25", "Božić"),
            ("2025-12-26", "Sveti Stjepan"),
            ("2025-12-31", "Stara godina"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Nova godina"),
            ("2026-01-06", "Bogojavljenje ili Sveta tri kralja"),
            ("2026-04-03", "Veliki petak"),
            ("2026-04-06", "Uskrsni ponedjeljak"),
            ("2026-05-01", "Praznik rada"),
            ("2026-06-04", "Tijelovo"),
            ("2026-06-22", "Dan antifašističke borbe"),
            ("2026-08-05", "Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja"),
            (
                "2026-11-18",
                "Dan sjećanja na žrtve Domovinskog rata i "
                "Dan sjećanja na žrtvu Vukovara i Škabrnje",
            ),
            ("2026-12-24", "Badnjak"),
            ("2026-12-25", "Božić"),
            ("2026-12-31", "Stara godina"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Nova godina"),
            ("2024-03-29", "Veliki petak"),
            ("2024-04-01", "Uskrsni ponedjeljak"),
            ("2024-04-17", "Dan izbora zastupnika u Hrvatski sabor"),
            ("2024-05-01", "Praznik rada"),
            ("2024-05-30", "Dan državnosti; Tijelovo"),
            ("2024-08-05", "Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja"),
            ("2024-08-15", "Velika Gospa"),
            ("2024-11-01", "Svi sveti"),
            (
                "2024-11-18",
                "Dan sjećanja na žrtve Domovinskog rata i "
                "Dan sjećanja na žrtvu Vukovara i Škabrnje",
            ),
            ("2024-12-24", "Badnjak"),
            ("2024-12-25", "Božić"),
            ("2024-12-26", "Sveti Stjepan"),
            ("2024-12-31", "Stara godina"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-17", "Parliamentary Election Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-30", "Corpus Christi; Statehood Day"),
            ("2024-08-05", "Victory and Homeland Thanksgiving Day and Croatian Veterans Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-18", "Remembrance Day"),
            ("2024-12-24", "Christmas Eve"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Saint Stephen's Day"),
            ("2024-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-03-29", "Страсна пʼятниця"),
            ("2024-04-01", "Великодній понеділок"),
            ("2024-04-17", "День виборів депутатів Хорватського сабору"),
            ("2024-05-01", "День праці"),
            ("2024-05-30", "День державності; Свято Тіла і Крові Христових"),
            ("2024-08-05", "День перемоги і подяки вітчизні та День хорватських захисників"),
            ("2024-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2024-11-01", "День усіх святих"),
            ("2024-11-18", "День памʼяті жертв Вітчизняної війни та жертв Вуковара і Шкабрні"),
            ("2024-12-24", "Святвечір"),
            ("2024-12-25", "Різдво Христове"),
            ("2024-12-26", "День Святого Стефана"),
            ("2024-12-31", "Переддень Нового року"),
        )
