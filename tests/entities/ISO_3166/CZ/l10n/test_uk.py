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

from holidays.entities.ISO_3166.CZ import CzHolidays
from tests.common import CommonCountryTests


class TestCzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CzHolidays, language="uk")

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "День відновлення незалежної чеської держави"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День перемоги"),
            ("2022-07-05", "День Святих Кирила та Мефодія"),
            ("2022-07-06", "День спалення Яна Гуса"),
            ("2022-09-28", "День чеської державності"),
            ("2022-10-28", "День створення незалежної чехословацької держави"),
            ("2022-11-17", "День боротьби за свободу і демократію"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
