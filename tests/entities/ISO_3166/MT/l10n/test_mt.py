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

from holidays.entities.ISO_3166.MT import MtHolidays
from tests.common import CommonCountryTests


class TestMtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MtHolidays)

    def test_mt(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "L-Ewwel tas-Sena"),
            ("2023-02-10", "Il-Festa tan-Nawfraġju ta' San Pawl"),
            ("2023-03-19", "Il-Festa ta' San Ġużepp"),
            ("2023-03-31", "Jum il-Ħelsien"),
            ("2023-04-07", "Il-Ġimgħa l-Kbira"),
            ("2023-05-01", "Jum il-Ħaddiem"),
            ("2023-06-07", "Sette Giugno"),
            ("2023-06-29", "Il-Festa ta' San Pietru u San Pawl"),
            ("2023-08-15", "Il-Festa ta' Santa Marija"),
            ("2023-09-08", "Jum il-Vitorja"),
            ("2023-09-21", "Jum l-Indipendenza"),
            ("2023-12-08", "Il-Festa tal-Immakulata Kunċizzjoni"),
            ("2023-12-13", "Jum ir-Repubblika"),
            ("2023-12-25", "Il-Milied"),
        )
