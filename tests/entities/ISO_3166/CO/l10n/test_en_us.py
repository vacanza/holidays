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

from holidays.entities.ISO_3166.CO import CoHolidays
from tests.common import CommonCountryTests


class TestCoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CoHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-10", "Epiphany (observed)"),
            ("2022-03-21", "Saint Joseph's Day (observed)"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-30", "Ascension Day (observed)"),
            ("2022-06-20", "Corpus Christi (observed)"),
            ("2022-06-27", "Sacred Heart (observed)"),
            ("2022-07-04", "Saint Peter and Saint Paul (observed)"),
            ("2022-07-20", "Independence Day"),
            ("2022-08-07", "Battle of Boyacá"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-17", "Columbus Day (observed)"),
            ("2022-11-07", "All Saints' Day (observed)"),
            ("2022-11-14", "Independence of Cartagena (observed)"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-25", "Christmas Day"),
        )
