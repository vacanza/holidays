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

from holidays.entities.ISO_3166.UZ import UzHolidays
from tests.common import CommonCountryTests


class TestUzbekistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UzHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "Additional day off by Presidential decree"),
            ("2023-01-03", "Day off (substituted from 01/07/2023)"),
            ("2023-03-08", "Women's Day"),
            ("2023-03-20", "Day off (substituted from 03/11/2023)"),
            ("2023-03-21", "Nowruz"),
            ("2023-03-22", "Day off (substituted from 03/25/2023)"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-24", "Additional day off by Presidential decree"),
            ("2023-05-09", "Day of Memory and Honor"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Additional day off by Presidential decree"),
            ("2023-06-30", "Additional day off by Presidential decree"),
            ("2023-09-01", "Independence Day"),
            ("2023-10-01", "Teachers and Instructors Day"),
            ("2023-10-02", "Teachers and Instructors Day (observed)"),
            ("2023-12-08", "Constitution Day"),
        )
