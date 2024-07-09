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

from holidays.entities.ISO_3166.AW import AwHolidays
from tests.common import CommonCountryTests


class TestAwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AwHolidays, years=range(1947, 2077))

    def test_no_holidays(self):
        self.assertNoHolidays(AwHolidays(years=1946))

    def test_2017(self):
        self.assertHolidays(
            AwHolidays(years=2017),
            ("2017-01-01", "Aña Nobo"),
            ("2017-01-25", "Dia di Betico"),
            ("2017-02-27", "Dialuna despues di Carnaval Grandi"),
            ("2017-03-18", "Dia di Himno y Bandera"),
            ("2017-04-14", "Bierna Santo"),
            ("2017-04-17", "Di dos dia di Pasco di Resureccion"),
            ("2017-04-27", "Aña di Rey"),
            ("2017-05-01", "Dia di Obrero"),
            ("2017-05-25", "Dia di Asuncion"),
            ("2017-12-25", "Pasco di Nacemento"),
            ("2017-12-26", "Di dos dia di Pasco di Nacemento"),
        )

    def test_betico_day(self):
        name = "Dia di Betico"
        self.assertNoHolidayName(name, 1988)
        self.assertHolidayName(name, (f"{year}-01-25" for year in range(1989, 2077)))

    def test_carnival_monday(self):
        name_carnival = "Dialuna despues di Carnaval Grandi"
        name_mon_ash = "Dialuna prome cu diaranson di shinish"

        self.assertNoHolidayName(name_carnival, 1955)
        self.assertNoHolidayName(name_mon_ash, 1955)
        self.assertHolidayName(
            name_carnival,
            "2016-02-08",
            "2017-02-27",
            "2018-02-12",
            "2019-03-04",
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
        )
        self.assertNoHolidayName(name_mon_ash, range(1956, 2023))
        self.assertHolidayName(name_mon_ash, "2023-02-20")
        self.assertNoHolidayName(name_carnival, range(2023, 2077))

    def test_anthem_and_flag_day(self):
        name = "Dia di Himno y Bandera"
        self.assertNoHolidayName(name, 1975)
        self.assertHolidayName(name, (f"{year}-03-18" for year in range(1976, 2077)))

    def test_queens_day(self):
        name = "Aña di La Reina"
        self.assertHolidayName(
            name,
            "1947-09-01",
            "1948-08-31",
            "1950-05-01",
            "1961-05-01",
            "1965-04-30",
            "1967-05-01",
            "1972-05-01",
            "1978-05-01",
            "1989-04-29",
            "1995-04-29",
            "2000-04-29",
            "2006-04-29",
            "2013-04-30",
        )
        self.assertNoHoliday(
            "1947-08-31",
            "1950-04-30",
            "1961-04-30",
            "1967-04-30",
            "1972-04-30",
            "1978-04-30",
            "1995-04-30",
            "1989-04-30",
            "2000-04-30",
            "2006-04-30",
        )
        self.assertNoHolidayName(name, 2014)

    def test_king_day(self):
        name_ana = "Aña di Rey"
        name_dia = "Dia di Rey"
        self.assertNoHolidayName(name_ana, 2013)
        self.assertNoHolidayName(name_dia, 2013)
        self.assertHolidayName(
            name_ana,
            "2016-04-27",
            "2017-04-27",
            "2018-04-27",
            "2019-04-27",
            "2020-04-27",
        )
        self.assertNoHolidayName(name_dia, range(2013, 2021))
        self.assertHolidayName(
            name_dia,
            "2021-04-27",
            "2022-04-27",
            "2023-04-27",
            "2024-04-27",
            "2025-04-26",
            "2031-04-26",
            "2036-04-26",
        )
        self.assertNoHolidayName(name_ana, range(2021, 2077))
        self.assertNoHoliday(
            "2014-04-27",
            "2025-04-27",
            "2031-04-27",
            "2036-04-27",
        )
