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

from holidays.entities.ISO_3166.DO import DoHolidays
from tests.common import CommonCountryTests


class TestDoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DoHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-10", "Богоявлення"),
            ("2022-01-21", "День Богоматері Альтаграсія"),
            ("2022-01-24", "День Дуарте"),
            ("2022-02-27", "День незалежності"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-02", "День праці"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "День реставрації"),
            ("2022-09-24", "День Богоматері Милосердя"),
            ("2022-11-06", "День Конституції"),
            ("2022-12-25", "Різдво Христове"),
        )
