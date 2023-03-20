#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.vatican_city import VaticanCity, VA, VAT
from tests.common import TestCase


class TestVaticanCity(TestCase):
    def setUp(self):
        self.holidays = VaticanCity()

    def test_country_aliases(self):
        self.assertCountryAliases(VaticanCity, VA, VAT)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Solemnity of Mary Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-02-11", "Lateran Treaty Day"),
            ("2022-03-13", "Anniversary of the election of Pope Francis"),
            ("2022-03-19", "Saint Joseph's Day"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-23", "Saint George's Day"),
            ("2022-05-01", "Saint Joseph the Worker's Day"),
            ("2022-06-29", "Saint Peter and Saint Paul's Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-08", "Nativity of Mary Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
        )

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-01", "Solemnity of Mary Day"),
            ("2023-01-06", "Epiphany"),
            ("2023-02-11", "Lateran Treaty Day"),
            ("2023-03-13", "Anniversary of the election of Pope Francis"),
            ("2023-03-19", "Saint Joseph's Day"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-23", "Saint George's Day"),
            ("2023-05-01", "Saint Joseph the Worker's Day"),
            ("2023-06-29", "Saint Peter and Saint Paul's Day"),
            ("2023-08-15", "Assumption Day"),
            ("2023-09-08", "Nativity of Mary Day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-12-08", "Immaculate Conception Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Saint Stephen's Day"),
        )
