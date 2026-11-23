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

from holidays.financial.prague_stock_exchange import PragueStockExchange
from tests.common import CommonFinancialTests


class TestPragueStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PragueStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_new_years_eve(self):
        name = "Silvestr"
        years_absent = {2017, 2022, 2023, 2028, 2033, 2034, 2039, 2044, 2045}
        self.assertNoHolidayName(name, years_absent)
        self.assertHolidayName(
            name, (f"{year}-12-31" for year in self.full_range if year not in years_absent)
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Den obnovy samostatného českého státu; Nový rok"),
            ("2026-04-03", "Velký pátek"),
            ("2026-04-06", "Velikonoční pondělí"),
            ("2026-05-01", "Svátek práce"),
            ("2026-05-08", "Den vítězství"),
            ("2026-07-06", "Den upálení mistra Jana Husa"),
            ("2026-09-28", "Den české státnosti"),
            ("2026-10-28", "Den vzniku samostatného československého státu"),
            ("2026-11-17", "Den boje za svobodu a demokracii a Mezinárodní den studentstva"),
            ("2026-12-24", "Štědrý den"),
            ("2026-12-25", "1. svátek vánoční"),
            ("2026-12-31", "Silvestr"),
        )

    def test_2027(self):
        self.assertHolidaysInYear(
            2027,
            ("2027-01-01", "Den obnovy samostatného českého státu; Nový rok"),
            ("2027-03-26", "Velký pátek"),
            ("2027-03-29", "Velikonoční pondělí"),
            ("2027-07-05", "Den slovanských věrozvěstů Cyrila a Metoděje"),
            ("2027-07-06", "Den upálení mistra Jana Husa"),
            ("2027-09-28", "Den české státnosti"),
            ("2027-10-28", "Den vzniku samostatného československého státu"),
            ("2027-11-17", "Den boje za svobodu a demokracii a Mezinárodní den studentstva"),
            ("2027-12-24", "Štědrý den"),
            ("2027-12-31", "Silvestr"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2020-01-01", "Den obnovy samostatného českého státu; Nový rok"),
            ("2020-04-10", "Velký pátek"),
            ("2020-04-13", "Velikonoční pondělí"),
            ("2020-05-01", "Svátek práce"),
            ("2020-05-08", "Den vítězství"),
            ("2020-07-06", "Den upálení mistra Jana Husa"),
            ("2020-09-28", "Den české státnosti"),
            ("2020-10-28", "Den vzniku samostatného československého státu"),
            ("2020-11-17", "Den boje za svobodu a demokracii a Mezinárodní den studentstva"),
            ("2020-12-24", "Štědrý den"),
            ("2020-12-25", "1. svátek vánoční"),
            ("2020-12-31", "Silvestr"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2020-01-01", "Independent Czech State Restoration Day; New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-01", "Labor Day"),
            ("2020-05-08", "Victory Day"),
            ("2020-07-06", "Jan Hus Day"),
            ("2020-09-28", "Statehood Day"),
            ("2020-10-28", "Independent Czechoslovak State Day"),
            (
                "2020-11-17",
                "Struggle for Freedom and Democracy Day and International Students' Day",
            ),
            ("2020-12-24", "Christmas Eve"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-31", "New Year's Eve"),
        )

    def test_l10n_sk(self):
        self.assertLocalizedHolidays(
            "sk",
            ("2020-01-01", "Deň obnovy samostatného českého štátu; Nový rok"),
            ("2020-04-10", "Veľký piatok"),
            ("2020-04-13", "Veľkonočný pondelok"),
            ("2020-05-01", "Sviatok práce"),
            ("2020-05-08", "Deň víťazstva"),
            ("2020-07-06", "Deň upálenia majstra Jána Husa"),
            ("2020-09-28", "Deň českej štátnosti"),
            ("2020-10-28", "Deň vzniku samostatného československého štátu"),
            ("2020-11-17", "Deň boja za slobodu a demokraciu a Medzinárodný deň študentstva"),
            ("2020-12-24", "Štedrý deň"),
            ("2020-12-25", "1. sviatok vianočný"),
            ("2020-12-31", "Silvester"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2020-01-01", "День відновлення незалежної чеської держави; Новий рік"),
            ("2020-04-10", "Страсна пʼятниця"),
            ("2020-04-13", "Великодній понеділок"),
            ("2020-05-01", "День праці"),
            ("2020-05-08", "День Перемоги"),
            ("2020-07-06", "День спалення Яна Гуса"),
            ("2020-09-28", "День чеської державності"),
            ("2020-10-28", "День створення незалежної чехословацької держави"),
            ("2020-11-17", "День боротьби за свободу та демократію і Міжнародний день студентів"),
            ("2020-12-24", "Святий вечір"),
            ("2020-12-25", "Різдво Христове"),
            ("2020-12-31", "Переддень Нового року"),
        )
