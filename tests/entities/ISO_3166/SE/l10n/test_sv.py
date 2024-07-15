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
        super().setUpClass(SeHolidays)

    def test_sv(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Nyårsdagen"),
            ("2018-01-06", "Trettondedag jul"),
            ("2018-01-07", "Söndag"),
            ("2018-01-14", "Söndag"),
            ("2018-01-21", "Söndag"),
            ("2018-01-28", "Söndag"),
            ("2018-02-04", "Söndag"),
            ("2018-02-11", "Söndag"),
            ("2018-02-18", "Söndag"),
            ("2018-02-25", "Söndag"),
            ("2018-03-04", "Söndag"),
            ("2018-03-11", "Söndag"),
            ("2018-03-18", "Söndag"),
            ("2018-03-25", "Söndag"),
            ("2018-03-30", "Långfredagen"),
            ("2018-04-01", "Påskdagen; Söndag"),
            ("2018-04-02", "Annandag påsk"),
            ("2018-04-08", "Söndag"),
            ("2018-04-15", "Söndag"),
            ("2018-04-22", "Söndag"),
            ("2018-04-29", "Söndag"),
            ("2018-05-01", "Första maj"),
            ("2018-05-06", "Söndag"),
            ("2018-05-10", "Kristi himmelsfärdsdag"),
            ("2018-05-13", "Söndag"),
            ("2018-05-20", "Pingstdagen; Söndag"),
            ("2018-05-27", "Söndag"),
            ("2018-06-03", "Söndag"),
            ("2018-06-06", "Sveriges nationaldag"),
            ("2018-06-10", "Söndag"),
            ("2018-06-17", "Söndag"),
            ("2018-06-22", "Midsommarafton"),
            ("2018-06-23", "Midsommardagen"),
            ("2018-06-24", "Söndag"),
            ("2018-07-01", "Söndag"),
            ("2018-07-08", "Söndag"),
            ("2018-07-15", "Söndag"),
            ("2018-07-22", "Söndag"),
            ("2018-07-29", "Söndag"),
            ("2018-08-05", "Söndag"),
            ("2018-08-12", "Söndag"),
            ("2018-08-19", "Söndag"),
            ("2018-08-26", "Söndag"),
            ("2018-09-02", "Söndag"),
            ("2018-09-09", "Söndag"),
            ("2018-09-16", "Söndag"),
            ("2018-09-23", "Söndag"),
            ("2018-09-30", "Söndag"),
            ("2018-10-07", "Söndag"),
            ("2018-10-14", "Söndag"),
            ("2018-10-21", "Söndag"),
            ("2018-10-28", "Söndag"),
            ("2018-11-03", "Alla helgons dag"),
            ("2018-11-04", "Söndag"),
            ("2018-11-11", "Söndag"),
            ("2018-11-18", "Söndag"),
            ("2018-11-25", "Söndag"),
            ("2018-12-02", "Söndag"),
            ("2018-12-09", "Söndag"),
            ("2018-12-16", "Söndag"),
            ("2018-12-23", "Söndag"),
            ("2018-12-24", "Julafton"),
            ("2018-12-25", "Juldagen"),
            ("2018-12-26", "Annandag jul"),
            ("2018-12-30", "Söndag"),
            ("2018-12-31", "Nyårsafton"),
        )
