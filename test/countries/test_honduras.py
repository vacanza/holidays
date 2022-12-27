#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.honduras import HN, HND, Honduras
from test.common import TestCase


class TestHonduras(TestCase):
    def setUp(self):
        self.holidays = Honduras()

    def test_aliases(self):
        self.assertCountryAliases(Honduras, HN, HND)

    def test_2014(self):
        self.assertHolidayDatesEqual(
            Honduras(years=2014),
            "2014-01-01",
            "2014-04-14",
            "2014-04-17",
            "2014-04-18",
            "2014-04-19",
            "2014-05-01",
            "2014-09-15",
            "2014-10-03",
            "2014-10-12",
            "2014-10-21",
            "2014-12-25",
        )

    def test_2016(self):
        # https://www.officeholidays.com/countries/honduras/2016
        self.assertHolidayDatesEqual(
            Honduras(years=2016),
            "2016-01-01",
            "2016-03-24",
            "2016-03-25",
            "2016-03-26",
            "2016-04-14",
            "2016-05-01",
            "2016-09-15",
            "2016-10-05",
            "2016-10-06",
            "2016-10-07",
            "2016-12-25",
        )

    def test_2021(self):
        # https://www.officeholidays.com/countries/honduras/2021
        self.assertHolidayDatesEqual(
            Honduras(years=2021),
            "2021-01-01",
            "2021-04-01",
            "2021-04-02",
            "2021-04-03",
            "2021-04-14",
            "2021-05-01",
            "2021-09-15",
            "2021-10-06",
            "2021-10-07",
            "2021-10-08",
            "2021-12-25",
        )

    def test_2022(self):
        self.assertHolidaysEqual(
            Honduras(observed=False, years=2022),
            ("2022-01-01", "Año Nuevo [New Year's Day]"),
            (
                "2022-04-14",
                "Día de las Américas [Panamerican Day], "
                "Jueves Santo [Maundy Thursday]",
            ),
            ("2022-04-15", "Viernes Santo [Good Friday]"),
            ("2022-04-16", "Sábado de Gloria [Holy Saturday]"),
            ("2022-05-01", "Día del Trabajo [Labor Day]"),
            ("2022-09-15", "Día de la Independencia [Independence Day]"),
            ("2022-10-05", "Semana Morazánica [Morazan Weekend]"),
            ("2022-10-06", "Semana Morazánica [Morazan Weekend]"),
            ("2022-10-07", "Semana Morazánica [Morazan Weekend]"),
            ("2022-12-25", "Navidad [Christmas]"),
        )

    def test_2025(self):
        self.assertHolidayDatesEqual(
            Honduras(years=2025),
            "2025-01-01",
            "2025-04-14",
            "2025-04-17",
            "2025-04-18",
            "2025-04-19",
            "2025-05-01",
            "2025-09-15",
            "2025-10-01",
            "2025-10-02",
            "2025-10-03",
            "2025-12-25",
        )
