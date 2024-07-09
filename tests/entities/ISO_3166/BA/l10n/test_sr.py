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

from holidays.entities.ISO_3166.BA import BaHolidays
from tests.common import CommonCountryTests


class TestBaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BaHolidays, language="sr")

    def test_sr(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Нова година"),
            ("2022-01-02", "Нова година"),
            ("2022-01-07", "Божић (Православни)"),
            ("2022-04-18", "Ускршњи понедељак (Католички)"),
            ("2022-04-22", "Велики петак (Православни)"),
            ("2022-05-01", "Међународни празник рада"),
            ("2022-05-02", "Међународни празник рада; Рамазански Бајрам"),
            ("2022-07-09", "Курбан Бајрам"),
            ("2022-12-25", "Божић (Католички)"),
        )
