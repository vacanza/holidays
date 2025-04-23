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

from datetime import date
from unittest import TestCase

from holidays.countries.sao_tome_and_principe import SaoTomeAndPrincipe, ST, STP
from tests.common import CommonCountryTests


class TestSaoTome(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaoTomeAndPrincipe)
        cls.observed_holidays = SaoTomeAndPrincipe(observed=True)

    def test_country_aliases(self):
        self.assertIsInstance(ST(), SaoTomeAndPrincipe)
        self.assertIsInstance(STP(), SaoTomeAndPrincipe)
        self.assertEqual(ST().subdiv, None)
        self.assertEqual(STP().subdiv, None)

    def test_consistent_holidays(self):
        # Test holidays that exist every year in the same form
        consistent_dates = {
            "2014-01-01": "Ano Novo",
            "2015-02-03": "Dia dos Mártires",
            "2016-05-01": "Dia do Trabalhador",
            "2017-07-12": "Dia da Independência",
            "2018-09-06": "Dia das Forças Armadas",
            "2019-09-30": "Dia da Reforma Agrária",
            "2020-12-25": "Natal",
            "2021-01-04": "Dia do Rei Amador",
            "2022-02-03": "Dia dos Mártires",
            "2023-05-01": "Dia do Trabalhador",
            "2024-07-12": "Dia da Independência",
            "2025-09-06": "Dia das Forças Armadas",
        }

        for date_str, name in consistent_dates.items():
            self.assertIn(date_str, self.holidays)
            self.assertEqual(self.holidays[date_str], name)

    def test_observed_holidays(self):
        # Test observed dates (only from 2020 onwards)
        observed_test_cases = {
            # Before 2020 - no observed dates
            "2015-01-05": None,  # Jan 4 was Sunday
            "2016-07-11": None,  # Jul 12 was Tuesday
            "2017-09-07": None,  # Sep 6 was Wednesday
            "2018-12-24": None,  # Dec 25 was Tuesday
            "2019-01-03": None,  # Jan 4 was Friday
            # From 2020 onwards - with observed dates
            "2020-01-03": "Dia do Rei Amador (observed)",  # Jan 4 was Saturday
            "2020-07-13": "Dia da Independência (observed)",  # Jul 12 was Sunday
            "2021-04-30": "Dia do Trabalhador (observed)",  # May 1 was Saturday
            "2021-12-24": "Natal (observed)",  # Dec 25 was Saturday
            "2022-05-02": "Dia do Trabalhador (observed)",  # May 1 was Sunday
            "2022-12-26": "Natal (observed)",  # Dec 25 was Sunday
            "2023-01-02": "Ano Novo (observed)",  # Jan 1 was Sunday
            "2023-09-29": "Dia da Reforma Agrária (observed)",  # Sep 30 was Saturday
            "2024-02-02": "Dia dos Mártires (observed)",  # Feb 3 was Saturday
            "2025-07-11": "Dia da Independência (observed)",  # Jul 12 was Saturday
            "2025-09-05": "Dia das Forças Armadas (observed)",  # Sep 6 was Saturday
            "2025-12-22": "Dia de São Tomé (observed)",  # Dec 21 was Sunday
        }

        for date_str, expected_name in observed_test_cases.items():
            if expected_name is None:
                self.assertNotIn(date_str, self.observed_holidays)
            else:
                self.assertIn(date_str, self.observed_holidays)
                self.assertEqual(self.observed_holidays[date_str], expected_name)

    def test_sao_tome_day(self):
        # São Tomé Day started in 2019
        self.assertNotIn("2018-12-21", self.holidays)
        self.assertIn("2019-12-21", self.holidays)
        self.assertIn("2020-12-21", self.holidays)
        self.assertIn("2021-12-21", self.holidays)
        self.assertIn("2022-12-21", self.holidays)
        self.assertIn("2023-12-21", self.holidays)
        self.assertIn("2024-12-21", self.holidays)
        self.assertIn("2025-12-21", self.holidays)

        # Observed day for São Tomé Day (only from 2020)
        self.assertNotIn("2019-12-20", self.observed_holidays)  # Before 2020
        self.assertIn("2020-12-21", self.observed_holidays)  # Was Monday
        self.assertIn("2024-12-20", self.observed_holidays)  # Dec 21 was Saturday
        self.assertIn("2025-12-22", self.observed_holidays)  # Dec 21 was Sunday

    def test_all_years_holidays(self):
        # 2014
        self.assertIn("2014-01-01", self.holidays)  # New Year
        self.assertIn("2014-01-04", self.holidays)  # Day of King Amador
        self.assertIn("2014-02-03", self.holidays)  # Commemoration of the Batepá Massacre
        self.assertIn("2014-05-01", self.holidays)  # Labour Day
        self.assertIn("2014-07-12", self.holidays)  # Independence Day
        self.assertIn("2014-09-06", self.holidays)  # Armed Forces' Day
        self.assertIn("2014-09-30", self.holidays)  # Nationalization of the Roças
        self.assertIn("2014-12-25", self.holidays)  # Christmas Day

        # 2015
        self.assertIn("2015-01-01", self.holidays)
        self.assertIn("2015-01-04", self.holidays)
        self.assertIn("2015-02-03", self.holidays)
        self.assertIn("2015-05-01", self.holidays)
        self.assertIn("2015-07-12", self.holidays)
        self.assertIn("2015-09-06", self.holidays)
        self.assertIn("2015-09-30", self.holidays)
        self.assertIn("2015-12-25", self.holidays)

        # 2016
        self.assertIn("2016-01-01", self.holidays)
        self.assertIn("2016-01-04", self.holidays)
        self.assertIn("2016-02-03", self.holidays)
        self.assertIn("2016-05-01", self.holidays)
        self.assertIn("2016-07-12", self.holidays)
        self.assertIn("2016-09-06", self.holidays)
        self.assertIn("2016-09-30", self.holidays)
        self.assertIn("2016-12-25", self.holidays)

        # 2017
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2017-01-04", self.holidays)
        self.assertIn("2017-02-03", self.holidays)
        self.assertIn("2017-05-01", self.holidays)
        self.assertIn("2017-07-12", self.holidays)
        self.assertIn("2017-09-06", self.holidays)
        self.assertIn("2017-09-30", self.holidays)
        self.assertIn("2017-12-25", self.holidays)

        # 2018
        self.assertIn("2018-01-01", self.holidays)
        self.assertIn("2018-01-04", self.holidays)
        self.assertIn("2018-02-03", self.holidays)
        self.assertIn("2018-05-01", self.holidays)
        self.assertIn("2018-07-12", self.holidays)
        self.assertIn("2018-09-06", self.holidays)
        self.assertIn("2018-09-30", self.holidays)
        self.assertIn("2018-12-25", self.holidays)

        # 2019
        self.assertIn("2019-01-01", self.holidays)
        self.assertIn("2019-01-04", self.holidays)
        self.assertIn("2019-02-03", self.holidays)
        self.assertIn("2019-05-01", self.holidays)
        self.assertIn("2019-07-12", self.holidays)
        self.assertIn("2019-09-06", self.holidays)
        self.assertIn("2019-09-30", self.holidays)
        self.assertIn("2019-12-21", self.holidays)  # São Tomé Day (first year)
        self.assertIn("2019-12-25", self.holidays)

        # 2020
        self.assertIn("2020-01-01", self.holidays)
        self.assertIn("2020-01-04", self.holidays)
        self.assertIn("2020-02-03", self.holidays)
        self.assertIn("2020-05-01", self.holidays)
        self.assertIn("2020-07-12", self.holidays)
        self.assertIn("2020-09-06", self.holidays)
        self.assertIn("2020-09-30", self.holidays)
        self.assertIn("2020-12-21", self.holidays)  # São Tomé Day
        self.assertIn("2020-12-25", self.holidays)

        # 2021
        self.assertIn("2021-01-01", self.holidays)
        self.assertIn("2021-01-04", self.holidays)
        self.assertIn("2021-02-03", self.holidays)
        self.assertIn("2021-05-01", self.holidays)
        self.assertIn("2021-07-12", self.holidays)
        self.assertIn("2021-09-06", self.holidays)
        self.assertIn("2021-09-30", self.holidays)
        self.assertIn("2021-12-21", self.holidays)  # São Tomé Day
        self.assertIn("2021-12-25", self.holidays)

        # 2022
        self.assertIn("2022-01-01", self.holidays)
        self.assertIn("2022-01-04", self.holidays)
        self.assertIn("2022-02-03", self.holidays)
        self.assertIn("2022-05-01", self.holidays)
        self.assertIn("2022-07-12", self.holidays)
        self.assertIn("2022-09-06", self.holidays)
        self.assertIn("2022-09-30", self.holidays)
        self.assertIn("2022-12-21", self.holidays)  # São Tomé Day
        self.assertIn("2022-12-25", self.holidays)

        # 2023
        self.assertIn("2023-01-01", self.holidays)
        self.assertIn("2023-01-04", self.holidays)
        self.assertIn("2023-02-03", self.holidays)
        self.assertIn("2023-05-01", self.holidays)
        self.assertIn("2023-07-12", self.holidays)
        self.assertIn("2023-09-06", self.holidays)
        self.assertIn("2023-09-30", self.holidays)
        self.assertIn("2023-12-21", self.holidays)  # São Tomé Day
        self.assertIn("2023-12-25", self.holidays)

        # 2024
        self.assertIn("2024-01-01", self.holidays)
        self.assertIn("2024-01-04", self.holidays)
        self.assertIn("2024-02-03", self.holidays)
        self.assertIn("2024-05-01", self.holidays)
        self.assertIn("2024-07-12", self.holidays)
        self.assertIn("2024-09-06", self.holidays)
        self.assertIn("2024-09-30", self.holidays)
        self.assertIn("2024-12-21", self.holidays)  # São Tomé Day
        self.assertIn("2024-12-25", self.holidays)

        # 2025
        self.assertIn("2025-01-01", self.holidays)
        self.assertIn("2025-01-04", self.holidays)
        self.assertIn("2025-02-03", self.holidays)
        self.assertIn("2025-05-01", self.holidays)
        self.assertIn("2025-07-12", self.holidays)
        self.assertIn("2025-09-06", self.holidays)
        self.assertIn("2025-09-30", self.holidays)
        self.assertIn("2025-12-21", self.holidays)  # São Tomé Day
        self.assertIn("2025-12-25", self.holidays)

    def test_principe_specific_holidays(self):
        # Test Príncipe-specific holidays
        principe_dates = {
            "2020-01-17": "Descobrimento da Ilha do Príncipe",
            "2021-04-29": "Dia da Autonomia do Príncipe",
            "2022-08-15": "Dia de São Lourenço",
            "2023-01-17": "Descobrimento da Ilha do Príncipe",
            "2024-04-29": "Dia da Autonomia do Príncipe",
            "2025-08-15": "Dia de São Lourenço",
        }

        # National versions shouldn't have these
        for holiday_class in (SaoTomeAndPrincipe, ST, STP):
            holidays = holiday_class(years=range(2020, 2026))
            for date_str in principe_dates:
                self.assertNotIn(date_str, holidays)

        # PR subdivision should have them
        holidays = SaoTomeAndPrincipe(subdiv="PR", years=range(2020, 2026))
        for date_str, name in principe_dates.items():
            self.assertIn(date_str, holidays)
            self.assertEqual(holidays[date_str], name)

    def test_localization(self):
        # Test Portuguese localization
        pt_holidays = SaoTomeAndPrincipe(years=2025, language="pt", observed=True)
        self.assertEqual(pt_holidays["2025-01-03"], "Dia do Rei Amador (observed)")
        self.assertEqual(pt_holidays["2025-12-25"], "Natal")

        # Test English localization
        en_holidays = SaoTomeAndPrincipe(years=2025, language="en_US", observed=True)
        self.assertEqual(en_holidays["2025-01-03"], "Day of King Amador (observed)")
        self.assertEqual(en_holidays["2025-12-25"], "Christmas Day")

    def test_observed_suffix_translation(self):
        """Test observed suffix is correctly set based on language."""
        st_en = SaoTomeAndPrincipe(language="en_US")
        self.assertEqual(st_en.observed_suffix, "%s (observed)")

        st_pt = SaoTomeAndPrincipe(language="pt")
        self.assertEqual(st_pt.observed_suffix, "%s (observado)")

        st_fr = SaoTomeAndPrincipe(language="fr")
        self.assertEqual(st_fr.observed_suffix, "%s (observado)")

    def test_no_observed_holidays_before_2020(self):
        """Test that no observed holidays exist before 2020."""
        for year in range(2014, 2020):  # Before observed_start_year (2020)
            holidays = SaoTomeAndPrincipe(years=year, observed=True)

            # Check New Year's Day (Jan 1) never has an observed date before 2020
            jan1 = f"{year}-01-01"
            if jan1 in holidays:
                jan2 = f"{year}-01-02"
                self.assertNotIn(jan2, holidays)  # No observed date should exist

    def test_invalid_language_fallback(self):
        st = ST(language="xx", years=2024)
        # Should fallback to default (Portuguese)
        assert st[date(2024, 1, 1)] == "Ano Novo"

    def test_populate_holidays_and_observed_logic(self):
        """Tests holiday population, observed logic, and pre-2014 early return."""
        from holidays.countries.sao_tome_and_principe import SaoTomeAndPrincipe

        # Test 1: Directly test pre-2014 early return
        st = SaoTomeAndPrincipe.__new__(SaoTomeAndPrincipe)
        st._year = 2013
        result = st._populate_public_holidays()
        self.assertIsNone(result)

        # Test 2: Normal operation with observed holidays
        st_normal = SaoTomeAndPrincipe(years=2020, observed=True)
        self.assertIn(date(2020, 1, 1), st_normal)  # New Year's
        self.assertIn(date(2020, 1, 3), st_normal)  # Observed holiday

        # Test 3: Principe-specific holidays
        st_pr = SaoTomeAndPrincipe(years=2020, subdiv="PR")
        self.assertIn(date(2020, 1, 17), st_pr)  # Principe Discovery Day

        # Test 4: São Tomé Day (post-2019)
        st_2019 = SaoTomeAndPrincipe(years=2019)
        self.assertIn(date(2019, 12, 21), st_2019)

    def test_observed_suffix_and_principe_branch_logic(self):
        """Tests localization of observed suffix and non-Principe subdivision exclusion."""
        from holidays.countries.sao_tome_and_principe import SaoTomeAndPrincipe

        # Test observed_suffix localization
        st_en = SaoTomeAndPrincipe(language="en_US")
        self.assertEqual(st_en.observed_suffix, "%s (observed)")

        st_pt = SaoTomeAndPrincipe(language="pt")
        self.assertEqual(st_pt.observed_suffix, "%s (observado)")

        # Test that non-PR subdivisions do not get Principe holiday
        st_no_pr = SaoTomeAndPrincipe(years=2020, subdiv="01")  # Not PR
        self.assertNotIn("2020-01-17", st_no_pr)
