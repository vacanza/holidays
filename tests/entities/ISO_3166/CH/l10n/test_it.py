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

from holidays.entities.ISO_3166.CH import ChHolidays
from tests.common import CommonCountryTests


class TestChHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ChHolidays, language="it")

    def test_it(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Capodanno"),
            ("2023-05-18", "Ascensione di Gesù"),
            ("2023-08-01", "Festa nazionale"),
            ("2023-12-25", "Natale"),
        )
