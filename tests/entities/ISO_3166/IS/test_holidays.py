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

from holidays.entities.ISO_3166.IS import IsHolidays
from tests.common import CommonCountryTests


class TestIsHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IsHolidays)

    def test_2018(self):
        self.assertHolidays(
            ("2018-01-01", "Nýársdagur"),
            ("2018-03-29", "Skírdagur"),
            ("2018-03-30", "Föstudagurinn langi"),
            ("2018-04-01", "Páskadagur"),
            ("2018-04-02", "Annar í páskum"),
            ("2018-04-19", "Sumardagurinn fyrsti"),
            ("2018-05-01", "Verkalýðsdagurinn"),
            ("2018-05-10", "Uppstigningardagur"),
            ("2018-05-20", "Hvítasunnudagur"),
            ("2018-05-21", "Annar í hvítasunnu"),
            ("2018-06-17", "Þjóðhátíðardagurinn"),
            ("2018-08-06", "Frídagur verslunarmanna"),
            ("2018-12-24", "Aðfangadagur"),
            ("2018-12-25", "Jóladagur"),
            ("2018-12-26", "Annar í jólum"),
            ("2018-12-31", "Gamlársdagur"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Nýársdagur"),
            ("2022-04-14", "Skírdagur"),
            ("2022-04-15", "Föstudagurinn langi"),
            ("2022-04-17", "Páskadagur"),
            ("2022-04-18", "Annar í páskum"),
            ("2022-04-21", "Sumardagurinn fyrsti"),
            ("2022-05-01", "Verkalýðsdagurinn"),
            ("2022-05-26", "Uppstigningardagur"),
            ("2022-06-05", "Hvítasunnudagur"),
            ("2022-06-06", "Annar í hvítasunnu"),
            ("2022-06-17", "Þjóðhátíðardagurinn"),
            ("2022-08-01", "Frídagur verslunarmanna"),
            ("2022-12-24", "Aðfangadagur"),
            ("2022-12-25", "Jóladagur"),
            ("2022-12-26", "Annar í jólum"),
            ("2022-12-31", "Gamlársdagur"),
        )
