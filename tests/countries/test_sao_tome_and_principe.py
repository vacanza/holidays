#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.sao_tome_and_principe import SaoTomeAndPrincipe, ST, STP
from tests.common import CommonCountryTests


class TestSaoTomeAndPrincipe(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaoTomeAndPrincipe, years=range(2014, 2050))
        cls.observed_holidays = SaoTomeAndPrincipe(years=range(2020, 2050), observed=True)
        cls.principe_holidays = SaoTomeAndPrincipe(subdiv="P", years=range(2014, 2050))

    def test_country_aliases(self):
        self.assertIsInstance(ST(), SaoTomeAndPrincipe)
        self.assertIsInstance(STP(), SaoTomeAndPrincipe)
        self.assertIsNone(ST().subdiv)
        self.assertIsNone(STP().subdiv)

    def test_2023(self):
        self.assertHolidays(
            SaoTomeAndPrincipe(years=2023),
            [
                ("2023-01-01", "Ano Novo"),
                ("2023-01-04", "Dia do Rei Amador"),
                ("2023-02-03", "Dia dos Mártires"),
                ("2023-05-01", "Dia do Trabalhador"),
                ("2023-07-12", "Dia da Independência"),
                ("2023-09-06", "Dia das Forças Armadas"),
                ("2023-09-30", "Dia da Reforma Agrária"),
                ("2023-12-21", "Dia de São Tomé"),
                ("2023-12-25", "Natal"),
            ],
        )

    def test_observed_dates(self):
        self.assertHoliday(
            self.observed_holidays,
            # Observed King Amador Day (Jan 4 was Saturday)
            "2020-01-03",
            # Observed Independence Day (Jul 12 was Sunday)
            "2020-07-13",
            # Observed New Year's (Jan 1 was Sunday)
            "2023-01-02",
            # Observed São Tomé Day (Dec 21 was Sunday)
            "2025-12-22",
        )

    def test_subdivisions(self):
        self.assertHoliday(
            self.principe_holidays,
            # Discovery of Príncipe Island
            "2020-01-17",
            # Autonomy Day
            "2020-04-29",
            # São Lourenço Day
            "2020-08-15",
        )
        # Verify national holidays are also present
        self.assertHoliday(
            self.principe_holidays,
            "2020-01-01",
            "2020-05-01",
        )

    def test_sao_tome_day(self):
        self.assertNoHoliday("2018-12-21")
        self.assertHoliday(
            "2019-12-21",
            "2020-12-21",
            "2025-12-21",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            SaoTomeAndPrincipe(years=2023),
            [
                ("2023-01-01", "Ano Novo"),
                ("2023-01-04", "Dia do Rei Amador"),
                ("2023-02-03", "Dia dos Mártires"),
                ("2023-05-01", "Dia do Trabalhador"),
                ("2023-07-12", "Dia da Independência"),
                ("2023-09-06", "Dia das Forças Armadas"),
                ("2023-09-30", "Dia da Reforma Agrária"),
                ("2023-12-21", "Dia de São Tomé"),
                ("2023-12-25", "Natal"),
            ],
        )

    def test_l10n_pt(self):
        self.assertLocalizedHolidays(
            SaoTomeAndPrincipe(years=2023, language="pt_ST"),
            [
                ("2023-01-01", "Ano Novo"),
                ("2023-01-04", "Dia do Rei Amador"),
                ("2023-02-03", "Dia dos Mártires"),
                ("2023-05-01", "Dia do Trabalhador"),
                ("2023-07-12", "Dia da Independência"),
                ("2023-09-06", "Dia das Forças Armadas"),
                ("2023-09-30", "Dia da Reforma Agrária"),
                ("2023-12-21", "Dia de São Tomé"),
                ("2023-12-25", "Natal"),
            ],
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            SaoTomeAndPrincipe(years=2023, language="en_US"),
            [
                ("2023-01-01", "New Year's Day"),
                ("2023-01-04", "Day of King Amador"),
                ("2023-02-03", "Martyrs' Day"),
                ("2023-05-01", "Labor Day"),
                ("2023-07-12", "Independence Day"),
                ("2023-09-06", "Armed Forces Day"),
                ("2023-09-30", "Agricultural Reform Day"),
                ("2023-12-21", "São Tomé Day"),
                ("2023-12-25", "Christmas Day"),
            ],
        )
