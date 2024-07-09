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

from holidays.entities.ISO_3166.AW import AwHolidays
from tests.common import CommonCountryTests


class TestAwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AwHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Новий рік"),
            ("2023-01-25", "День Бетіко"),
            ("2023-02-20", "Понеділок перед Попільною середою"),
            ("2023-03-18", "День державного гімну та прапора"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-04-10", "Великодній понеділок"),
            ("2023-04-27", "День короля"),
            ("2023-05-01", "День праці"),
            ("2023-05-18", "Вознесіння Господнє"),
            ("2023-12-25", "Різдво Христове"),
            ("2023-12-26", "Другий день Різдва"),
        )
