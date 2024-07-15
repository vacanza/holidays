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

from holidays.entities.ISO_3166.SE import SeHolidays
from tests.common import CommonCountryTests, SundayHolidays


class TestSeHolidays(CommonCountryTests, SundayHolidays, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SeHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "New Year's Day"),
            ("2018-01-06", "Epiphany"),
            ("2018-01-07", "Sunday"),
            ("2018-01-14", "Sunday"),
            ("2018-01-21", "Sunday"),
            ("2018-01-28", "Sunday"),
            ("2018-02-04", "Sunday"),
            ("2018-02-11", "Sunday"),
            ("2018-02-18", "Sunday"),
            ("2018-02-25", "Sunday"),
            ("2018-03-04", "Sunday"),
            ("2018-03-11", "Sunday"),
            ("2018-03-18", "Sunday"),
            ("2018-03-25", "Sunday"),
            ("2018-03-30", "Good Friday"),
            ("2018-04-01", "Easter Sunday; Sunday"),
            ("2018-04-02", "Easter Monday"),
            ("2018-04-08", "Sunday"),
            ("2018-04-15", "Sunday"),
            ("2018-04-22", "Sunday"),
            ("2018-04-29", "Sunday"),
            ("2018-05-01", "May Day"),
            ("2018-05-06", "Sunday"),
            ("2018-05-10", "Ascension Day"),
            ("2018-05-13", "Sunday"),
            ("2018-05-20", "Sunday; Whit Sunday"),
            ("2018-05-27", "Sunday"),
            ("2018-06-03", "Sunday"),
            ("2018-06-06", "National Day of Sweden"),
            ("2018-06-10", "Sunday"),
            ("2018-06-17", "Sunday"),
            ("2018-06-22", "Midsummer Eve"),
            ("2018-06-23", "Midsummer Day"),
            ("2018-06-24", "Sunday"),
            ("2018-07-01", "Sunday"),
            ("2018-07-08", "Sunday"),
            ("2018-07-15", "Sunday"),
            ("2018-07-22", "Sunday"),
            ("2018-07-29", "Sunday"),
            ("2018-08-05", "Sunday"),
            ("2018-08-12", "Sunday"),
            ("2018-08-19", "Sunday"),
            ("2018-08-26", "Sunday"),
            ("2018-09-02", "Sunday"),
            ("2018-09-09", "Sunday"),
            ("2018-09-16", "Sunday"),
            ("2018-09-23", "Sunday"),
            ("2018-09-30", "Sunday"),
            ("2018-10-07", "Sunday"),
            ("2018-10-14", "Sunday"),
            ("2018-10-21", "Sunday"),
            ("2018-10-28", "Sunday"),
            ("2018-11-03", "All Saints' Day"),
            ("2018-11-04", "Sunday"),
            ("2018-11-11", "Sunday"),
            ("2018-11-18", "Sunday"),
            ("2018-11-25", "Sunday"),
            ("2018-12-02", "Sunday"),
            ("2018-12-09", "Sunday"),
            ("2018-12-16", "Sunday"),
            ("2018-12-23", "Sunday"),
            ("2018-12-24", "Christmas Eve"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Second Day of Christmas"),
            ("2018-12-30", "Sunday"),
            ("2018-12-31", "New Year's Eve"),
        )
