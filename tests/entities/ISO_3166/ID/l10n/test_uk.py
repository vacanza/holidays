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

from holidays.entities.ISO_3166.ID import IdHolidays
from tests.common import CommonCountryTests


class TestIdHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IdHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-02-01", "Китайський Новий рік"),
            ("2022-02-28", "Вознесіння пророка Мухаммада"),
            ("2022-03-03", "День тиші"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-29", "Додатковий вихідний на Курбан-байрам"),
            ("2022-05-01", "Міжнародний день праці"),
            ("2022-05-02", "Рамазан-байрам"),
            ("2022-05-03", "Другий день Рамазан-байрам"),
            ("2022-05-04", "Додатковий вихідний на Курбан-байрам"),
            ("2022-05-05", "Додатковий вихідний на Курбан-байрам"),
            ("2022-05-06", "Додатковий вихідний на Курбан-байрам"),
            ("2022-05-16", "День народження Будди"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-01", "День Панчасіла"),
            ("2022-07-10", "Курбан-байрам"),
            ("2022-07-30", "Ісламський Новий рік"),
            ("2022-08-17", "День незалежності Республіки Індонезія"),
            ("2022-10-08", "День народження пророка Мухаммада"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Додатковий вихідний на Різдво Христове"),
        )
