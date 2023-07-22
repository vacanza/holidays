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

from holidays.countries.barbados import Barbados, BB, BRB
from tests.common import TestCase


class TestBarbados(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Barbados)

    def test_country_aliases(self):
        self.assertCountryAliases(Barbados, BB, BRB)

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-21", "Errol Barrow Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-28", "National Heroes Day"),
            ("2023-05-01", "Labor Day / May Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-07-31", "50th Anniversary of CARICOM Holiday"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-08-07", "Kadooment Day"),
            ("2023-11-30", "Independence Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        self.assertNoHoliday("2024-07-31")
        self.assertNoHolidayName("50th Anniversary of CARICOM Holiday", Barbados(years=2024))
