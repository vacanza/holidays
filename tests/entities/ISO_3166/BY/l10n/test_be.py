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

from holidays.entities.ISO_3166.BY import ByHolidays
from tests.common import CommonCountryTests


class TestByHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ByHolidays)

    def test_be(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новы год"),
            ("2022-01-02", "Новы год"),
            ("2022-01-07", "Нараджэнне Хрыстова (праваслаўнае Раство)"),
            ("2022-03-07", "Выходны (перанесены з 12.03.2022)"),
            ("2022-03-08", "Дзень жанчын"),
            ("2022-05-01", "Свята працы"),
            ("2022-05-02", "Выходны (перанесены з 14.05.2022)"),
            ("2022-05-03", "Радаўніца"),
            ("2022-05-09", "Дзень Перамогі"),
            ("2022-07-03", "Дзень Незалежнасці Рэспублікі Беларусь (Дзень Рэспублікі)"),
            ("2022-11-07", "Дзень Кастрычніцкай рэвалюцыі"),
            ("2022-12-25", "Нараджэнне Хрыстова (каталіцкае Раство)"),
        )
