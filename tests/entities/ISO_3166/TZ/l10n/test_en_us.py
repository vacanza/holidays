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

from holidays.entities.ISO_3166.TZ import TzHolidays
from tests.common import CommonCountryTests


class TestTanzania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TzHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-12", "Zanzibar Revolution Day"),
            ("2023-04-07", "Good Friday; The Sheikh Abeid Amani Karume Day"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-26", "Union Celebrations"),
            ("2023-05-01", "Worker's Day"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-07-07", "International Trade Fair"),
            ("2023-08-08", "Peasants Day"),
            ("2023-09-28", "Maulid Day"),
            ("2023-10-14", "The Mwalimu Nyerere Day"),
            ("2023-12-09", "Independence and Republic Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
