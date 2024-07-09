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

from holidays.entities.ISO_3166.LV import LvHolidays
from tests.common import CommonCountryTests


class TestLvHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LvHolidays)

    def test_lv(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jaunais Gads"),
            ("2022-04-15", "Lielā Piektdiena"),
            ("2022-04-17", "Lieldienas"),
            ("2022-04-18", "Otrās Lieldienas"),
            ("2022-05-01", "Darba svētki"),
            ("2022-05-04", "Latvijas Republikas Neatkarības atjaunošanas diena"),
            ("2022-05-08", "Mātes diena"),
            ("2022-06-23", "Līgo diena"),
            ("2022-06-24", "Jāņu diena"),
            ("2022-11-18", "Latvijas Republikas proklamēšanas diena"),
            ("2022-12-24", "Ziemassvētku vakars"),
            ("2022-12-25", "Ziemassvētki"),
            ("2022-12-26", "Otrie Ziemassvētki"),
            ("2022-12-31", "Vecgada vakars"),
        )
