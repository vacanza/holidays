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


class TestSaoTome(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaoTomeAndPrincipe, years=range(2014, 2026))
        cls.observed_holidays = SaoTomeAndPrincipe(years=range(2014, 2026), observed=True)

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
