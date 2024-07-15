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

from holidays.entities.ISO_3166.HU import HuHolidays
from tests.common import CommonCountryTests


class TestHuHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HuHolidays)

    def test_hu(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Újév"),
            ("2022-03-14", "Pihenőnap (2022. 03. 26.-től helyettesítve)"),
            ("2022-03-15", "Nemzeti ünnep"),
            ("2022-04-15", "Nagypéntek"),
            ("2022-04-17", "Húsvét"),
            ("2022-04-18", "Húsvét Hétfő"),
            ("2022-05-01", "A Munka ünnepe"),
            ("2022-06-05", "Pünkösd"),
            ("2022-06-06", "Pünkösdhétfő"),
            ("2022-08-20", "Az államalapítás ünnepe"),
            ("2022-10-23", "Nemzeti ünnep"),
            ("2022-10-31", "Pihenőnap (2022. 10. 15.-től helyettesítve)"),
            ("2022-11-01", "Mindenszentek"),
            ("2022-12-25", "Karácsony"),
            ("2022-12-26", "Karácsony másnapja"),
        )
