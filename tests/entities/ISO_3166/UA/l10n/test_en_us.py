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

from holidays.entities.ISO_3166.UA import UaHolidays
from tests.common import CommonCountryTests


class TestUaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UaHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2021-01-01", "New Year's Day"),
            ("2021-01-07", "Christmas Day (Julian calendar)"),
            ("2021-01-08", "Day off (substituted from 01/16/2021)"),
            ("2021-03-08", "International Women's Day"),
            ("2021-05-01", "Labor Day"),
            ("2021-05-02", "Easter Sunday (Pascha)"),
            ("2021-05-03", "Labor Day (observed)"),
            ("2021-05-04", "Easter Sunday (Pascha) (observed)"),
            ("2021-05-09", "Day of Victory over Nazism in World War II (Victory Day)"),
            ("2021-05-10", "Day of Victory over Nazism in World War II (Victory Day) (observed)"),
            ("2021-06-20", "Holy Trinity Day"),
            ("2021-06-21", "Holy Trinity Day (observed)"),
            ("2021-06-28", "Day of the Constitution of Ukraine"),
            ("2021-08-23", "Day off (substituted from 08/28/2021)"),
            ("2021-08-24", "Independence Day"),
            ("2021-10-14", "Day of defenders of Ukraine"),
            ("2021-10-15", "Day off (substituted from 10/23/2021)"),
            ("2021-12-25", "Christmas Day (Gregorian calendar)"),
            ("2021-12-27", "Christmas Day (Gregorian calendar) (observed)"),
        )
