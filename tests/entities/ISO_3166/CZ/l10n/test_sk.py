#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.entities.ISO_3166.CZ import CzHolidays
from tests.common import CommonCountryTests


class TestCzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CzHolidays, language="sk")

    def test_l10n_sk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Deň obnovy samostatného českého štátu"),
            ("2022-04-15", "Veľký piatok"),
            ("2022-04-18", "Veľkonočný pondelok"),
            ("2022-05-01", "Sviatok práce"),
            ("2022-05-08", "Deň víťazstva"),
            ("2022-07-05", "Deň slovanských vierozvestcov Cyrila a Metoda"),
            ("2022-07-06", "Deň upálenia majstra Jána Husa"),
            ("2022-09-28", "Deň českej štátnosti"),
            ("2022-10-28", "Deň vzniku samostatného československého štátu"),
            ("2022-11-17", "Deň boja za slobodu a demokraciu"),
            ("2022-12-24", "Štedrý deň"),
            ("2022-12-25", "1. sviatok vianočný"),
            ("2022-12-26", "2. sviatok vianočný"),
        )
