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

from holidays.entities.ISO_3166.PE import PeHolidays
from tests.common import CommonCountryTests


class TestPeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PeHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-05-01", "День праці"),
            ("2022-06-29", "День Святих Петра і Павла"),
            ("2022-07-28", "День незалежності"),
            ("2022-07-29", "День Великого військового параду"),
            ("2022-08-06", "День битви під Хуніном"),
            ("2022-08-30", "День Святої Рози Лімської"),
            ("2022-10-08", "День битви під Ангамосом"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-09", "День битви при Аякучо"),
            ("2022-12-25", "Різдво Христове"),
        )
