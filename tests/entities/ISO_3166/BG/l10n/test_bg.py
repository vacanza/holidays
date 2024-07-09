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

from holidays.entities.ISO_3166.BG import BgHolidays
from tests.common import CommonCountryTests


class TestBgHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BgHolidays)

    def test_bg(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Нова година"),
            ("2022-01-03", "Нова година (почивен ден)"),
            ("2022-03-03", "Ден на Освобождението на България от османско иго"),
            ("2022-04-22", "Велики петък"),
            ("2022-04-23", "Велика събота"),
            ("2022-04-24", "Великден"),
            ("2022-04-25", "Великден"),
            ("2022-05-01", "Ден на труда и на международната работническа солидарност"),
            (
                "2022-05-02",
                "Ден на труда и на международната работническа солидарност (почивен ден)",
            ),
            ("2022-05-06", "Гергьовден, Ден на храбростта и Българската армия"),
            (
                "2022-05-24",
                "Ден на светите братя Кирил и Методий, на българската азбука, "
                "просвета и култура и на славянската книжовност",
            ),
            ("2022-09-06", "Ден на Съединението"),
            ("2022-09-22", "Ден на Независимостта на България"),
            ("2022-11-01", "Ден на народните будители"),
            ("2022-12-24", "Бъдни вечер"),
            ("2022-12-25", "Рождество Христово"),
            ("2022-12-26", "Рождество Христово"),
            ("2022-12-27", "Бъдни вечер (почивен ден)"),
            ("2022-12-28", "Рождество Христово (почивен ден)"),
        )
