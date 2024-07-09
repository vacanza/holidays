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

from holidays.entities.ISO_3166.EC import EcHolidays
from tests.common import CommonCountryTests


class TestEcHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EcHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-02-28", "Карнавал"),
            ("2022-03-01", "Карнавал"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "День праці (вихідний)"),
            ("2022-05-23", "День битви біля Пічинча (вихідний)"),
            ("2022-05-24", "День битви біля Пічинча"),
            ("2022-08-10", "День незалежності Кіто"),
            ("2022-08-12", "День незалежності Кіто (вихідний)"),
            ("2022-10-09", "День незалежності Гуаякіля"),
            ("2022-10-10", "День незалежності Гуаякіля (вихідний)"),
            ("2022-11-02", "День усіх померлих"),
            ("2022-11-03", "День незалежності Куенки"),
            ("2022-11-04", "День незалежності Куенки (вихідний); День усіх померлих (вихідний)"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Різдво Христове (вихідний)"),
        )
