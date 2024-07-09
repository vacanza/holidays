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

from holidays.entities.ISO_3166.MX import MxHolidays
from tests.common import CommonCountryTests


class TestMxHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MxHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-02-07", "День Конституції"),
            ("2022-03-21", "Річниця Беніто Хуареса"),
            ("2022-05-01", "День праці"),
            ("2022-09-16", "День незалежності"),
            ("2022-11-21", "День революції"),
            ("2022-12-25", "Різдво Христове"),
        )
