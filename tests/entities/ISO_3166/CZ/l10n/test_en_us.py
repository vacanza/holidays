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
        super().setUpClass(CzHolidays, language="cs")

    def test_cs(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Den obnovy samostatného českého státu"),
            ("2022-04-15", "Velký pátek"),
            ("2022-04-18", "Velikonoční pondělí"),
            ("2022-05-01", "Svátek práce"),
            ("2022-05-08", "Den vítězství"),
            ("2022-07-05", "Den slovanských věrozvěstů Cyrila a Metoděje"),
            ("2022-07-06", "Den upálení mistra Jana Husa"),
            ("2022-09-28", "Den české státnosti"),
            ("2022-10-28", "Den vzniku samostatného československého státu"),
            ("2022-11-17", "Den boje za svobodu a demokracii"),
            ("2022-12-24", "Štědrý den"),
            ("2022-12-25", "1. svátek vánoční"),
            ("2022-12-26", "2. svátek vánoční"),
        )
