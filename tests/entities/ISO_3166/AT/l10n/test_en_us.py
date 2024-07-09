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

from holidays.entities.ISO_3166.AT import AtHolidays
from tests.common import CommonCountryTests


class TestAtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AtHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-26", "National Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "St. Stephen's Day"),
            ("2022-12-31", "New Year's Eve"),
        )
