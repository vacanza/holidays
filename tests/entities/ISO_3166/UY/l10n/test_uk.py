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

from holidays.entities.ISO_3166.UY import UyHolidays
from tests.common import CommonCountryTests


class TestUyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UyHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "День дітей"),
            ("2022-02-28", "Карнавал"),
            ("2022-03-01", "Карнавал"),
            ("2022-04-11", "Тиждень туризму"),
            ("2022-04-12", "Тиждень туризму"),
            ("2022-04-13", "Тиждень туризму"),
            ("2022-04-14", "Тиждень туризму"),
            ("2022-04-15", "Тиждень туризму"),
            ("2022-04-18", "День висадки 33 патріотів"),
            ("2022-05-01", "День трудящих"),
            ("2022-05-16", "День битви при Лас-Пʼєдрас"),
            ("2022-06-19", "Річниця Артігаса"),
            ("2022-07-18", "День присяги Конституції"),
            ("2022-08-25", "День проголошення незалежності"),
            ("2022-10-10", "День культурного різноманіття"),
            ("2022-11-02", "День усіх померлих"),
            ("2022-12-25", "День родини"),
        )
