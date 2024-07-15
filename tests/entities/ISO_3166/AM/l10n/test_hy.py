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

from holidays.entities.ISO_3166.AM import AmHolidays
from tests.common import CommonCountryTests


class TestAmHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AmHolidays)

    def test_hy(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Նոր տարվա օր"),
            ("2022-01-02", "Նոր տարվա օր"),
            ("2022-01-06", "Սուրբ Ծնունդ եւ Հայտնություն"),
            ("2022-01-28", "Բանակի օր"),
            ("2022-03-08", "Կանանց տոն"),
            ("2022-04-24", "Եղեռնի զոհերի հիշատակի օր"),
            ("2022-05-01", "Աշխատանքի օր"),
            ("2022-05-09", "Հաղթանակի և Խաղաղության տոն"),
            ("2022-05-28", "Հանրապետության օր"),
            ("2022-07-05", "Սահմանադրության օր"),
            ("2022-09-21", "Անկախության օր"),
            ("2022-12-31", "Նոր տարվա գիշեր"),
        )
