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

from holidays.entities.ISO_3166.FI import FiHolidays
from tests.common import CommonCountryTests


class TestFiHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(FiHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "Ваппу"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-24", "Переддень літнього сонцестояння"),
            ("2022-06-25", "День літнього сонцестояння"),
            ("2022-11-05", "День усіх святих"),
            ("2022-12-06", "День незалежності"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
