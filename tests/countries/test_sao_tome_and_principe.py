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

    def test_country_aliases(self):
        self.assertAliases(SaoTomeAndPrincipe, ST, STP)

    def test_no_holidays(self):
        self.assertNoHolidays(SaoTomeAndPrincipe(years=2013)

    def test_new_years_day(self):
        name = "Ano Novo"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2014, 2050)))
        obs_dt = ("2023-01-02", )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_day_of_king_amador(self):
        self.assertHolidayName("Dia do Rei Amador", (f"{year}-01-04" for year in range(2014, 2050)))

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
        name = "Dia de São Tomé"
        self.assertHolidayName(name, (f"{year}-12-21" for year in range(2019, 2050)))
        self.assertNoHolidayName(name, range(2014, 2019))

    def test_christmas_day(self):
        for year in range(2014, 2050):
            self.assertHolidayName("Natal", f"{year}-12-25")


    def test_discovery_of_principe_island(self):
        name = "Descobrimento da Ilha do Príncipe"
        self.assertHolidayName(
            name, subdiv_p_holidays, (f"{year}-01-17" for year in range(2014, 2050))
        )
        self.assertNoHolidayName(name)

    def test_autonomy_day(self):
        name = "Dia da Autonomia do Príncipe"
        self.assertHolidayName(
            name, subdiv_p_holidays, (f"{year}-04-29" for year in range(2014, 2050))
        )
        self.assertNoHolidayName(name)
        obs_dt = ("2023-04-28", )
        self.assertHolidayName(f"{name} (observado)", subdiv_p_holidays, obs_dt)
        self.assertNoNonObservedHoliday(subdiv_p_holidays, obs_dt)

    def test_sao_lorenco_day(self):
        name = "Dia de São Lourenço"
        self.assertHolidayName(
            name, subdiv_p_holidays, (f"{year}-08-15" for year in range(2014, 2050))
        )
        self.assertNoHolidayName(name)
        obs_dt = ("2020-08-14", "2021-08-16")
        self.assertHolidayName(f"{name} (observado)", subdiv_p_holidays, obs_dt)
        self.assertNoNonObservedHoliday(subdiv_p_holidays, obs_dt)

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
