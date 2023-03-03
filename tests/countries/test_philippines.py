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

from holidays.countries.philippines import Philippines, PH, PHL
from tests.common import TestCase


class TestPhilippines(TestCase):
    def setUp(self):
        self.holidays = Philippines()

    def test_country_aliases(self):
        self.assertCountryAliases(Philippines, PH, PHL)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-01", "Chinese New Year"),
            ("2022-02-25", "EDSA Revolution Anniversary"),
            ("2022-04-09", "Day of Valor"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Black Saturday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid'l Fitr"),
            ("2022-06-12", "Independence Day"),
            ("2022-07-09", "Eid'l Adha"),
            ("2022-08-21", "Ninoy Aquino Day"),
            ("2022-08-29", "National Heroes Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-30", "Bonifacio Day"),
            ("2022-12-08", "Immaculate Conception Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-30", "Rizal Day"),
            ("2022-12-31", "New Year's Eve"),
        )
