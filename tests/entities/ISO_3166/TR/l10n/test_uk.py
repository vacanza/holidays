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

from holidays.entities.ISO_3166.TR import TrHolidays
from tests.common import CommonCountryTests


class TestTrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TrHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Новий рік"),
            ("2023-04-20", "Рамазан-байрам (з 13:00)"),
            ("2023-04-21", "Рамазан-байрам"),
            ("2023-04-22", "Рамазан-байрам"),
            ("2023-04-23", "День національної незалежності та дітей; Рамазан-байрам"),
            ("2023-05-01", "День праці та солідарності"),
            ("2023-05-19", "День вшанування памʼяті Ататюрка, молоді та спорту"),
            ("2023-06-27", "Курбан-байрам (з 13:00)"),
            ("2023-06-28", "Курбан-байрам"),
            ("2023-06-29", "Курбан-байрам"),
            ("2023-06-30", "Курбан-байрам"),
            ("2023-07-01", "Курбан-байрам"),
            ("2023-07-15", "День демократії та національної єдності"),
            ("2023-08-30", "День Перемоги"),
            ("2023-10-28", "День Республіки (з 13:00)"),
            ("2023-10-29", "День Республіки"),
        )
