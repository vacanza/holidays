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
        super().setUpClass(
            years = range(2014, 2050)
            SaoTomeAndPrincipe, years=years, years_non_observed=range(2020, 2050)
            cls.subdiv_p_holidays = SaoTomeAndPrincipe(subdiv="P", years=years)
        )

    def test_new_years_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Ano Novo", f"{year}-01-01")

    def test_king_amador_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Dia do Rei Amador", f"{year}-01-04")

    def test_martyrs_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Dia dos Mártires", f"{year}-02-03")

    def test_labor_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Dia do Trabalhador", f"{year}-05-01")

    def test_independence_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Dia da Independência", f"{year}-07-12")

    def test_armed_forces_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Dia das Forças Armadas", f"{year}-09-06")

    def test_agrarian_reform_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Dia da Reforma Agrária", f"{year}-09-30")

    def test_sao_tome_day(self):
        for year in range(2019, 2050):  # Only from 2019 onward
            self.assertHolidayName("Dia de São Tomé", f"{year}-12-21")

    def test_christmas_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Natal", f"{year}-12-25")

    def test_observed_holidays(self):
        # Test New Year's Day observed (Sunday -> Monday)
        self.assertIn("2023-01-02", self.observed_holidays)
        self.assertEqual(self.observed_holidays["2023-01-02"], "Ano Novo (observado)")

        # Test Independence Day observed (Sunday -> Monday)
        self.assertIn("2020-07-13", self.observed_holidays)
        self.assertEqual(self.observed_holidays["2020-07-13"], "Dia da Independência (observado)")

    def test_principe_subdivision(self):
        principe_holidays = SaoTomeAndPrincipe(subdiv="P", years=range(2020, 2026))

        principe_fixed = [
            ("01-17", "Descobrimento da Ilha do Príncipe"),
            ("04-29", "Dia da Autonomia do Príncipe"),
            ("08-15", "Dia de São Lourenço"),
        ]

        for month_day, name in principe_fixed:
            for year in range(2020, 2026):
                self.assertHolidayName(name, principe_holidays, f"{year}-{month_day}")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Ano Novo"),
            ("2022-01-04", "Dia do Rei Amador"),
            ("2022-01-17", "Descobrimento da Ilha do Príncipe"),
            ("2022-02-03", "Dia dos Mártires"),
            ("2022-04-29", "Dia da Autonomia do Príncipe"),
            ("2022-05-01", "Dia do Trabalhador"),
            ("2022-05-02", "Dia do Trabalhador (observado)"),
            ("2022-07-12", "Dia da Independência"),
            ("2022-08-15", "Dia de São Lourenço"),
            ("2022-09-06", "Dia das Forças Armadas"),
            ("2022-09-30", "Dia da Reforma Agrária"),
            ("2022-12-21", "Dia de São Tomé"),
            ("2022-12-25", "Natal"),
            ("2022-12-26", "Natal (observado)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-04", "Day of King Amador"),
            ("2022-01-17", "Discovery of Príncipe Island"),
            ("2022-02-03", "Martyrs' Day"),
            ("2022-04-29", "Autonomy Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-07-12", "Independence Day"),
            ("2022-08-15", "São Lourenço Day"),
            ("2022-09-06", "Armed Forces Day"),
            ("2022-09-30", "Agricultural Reform Day"),
            ("2022-12-21", "São Tomé Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_special_holidays(self):
        # Example of testing special one-time holidays if any exist
        pass

    def test_variable_holidays(self):
        # Test holidays that change dates each year (like Carnival)
        pass
