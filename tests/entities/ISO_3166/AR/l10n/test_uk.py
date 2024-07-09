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

from holidays.entities.ISO_3166.AR import ArHolidays
from tests.common import CommonCountryTests


class TestArHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ArHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-02-28", "Карнавал"),
            ("2022-03-01", "Карнавал"),
            ("2022-03-24", "День памʼяті заради правди та правосуддя"),
            ("2022-04-02", "День ветеранів та загиблих на Мальвінській війні"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "День праці"),
            ("2022-05-18", "День національного перепису 2022"),
            ("2022-05-25", "День Травневої революції"),
            ("2022-06-17", "День памʼяті генерала Мартіна Мігеля де Гуемеса"),
            ("2022-06-20", "День памʼяті генерала Мануеля Бельграно"),
            ("2022-07-09", "День незалежності"),
            ("2022-08-15", "День памʼяті генерала Хосе де Сан-Мартіна (вихідний)"),
            ("2022-10-07", "Додатковий вихідний"),
            ("2022-10-10", "День поваги до культурного різноманіття (вихідний)"),
            ("2022-11-20", "День національного суверенітету"),
            ("2022-11-21", "Додатковий вихідний"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-09", "Додатковий вихідний"),
            ("2022-12-25", "Різдво Христове"),
        )
