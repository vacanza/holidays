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

from holidays.entities.ISO_3166.CW import CwHolidays
from tests.common import CommonCountryTests


class TestCwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CwHolidays, years=range(1954, 2077))

    def test_no_holidays(self):
        self.assertNoHolidays(CwHolidays(years=1953))

    def test_2016(self):
        self.assertHolidays(
            CwHolidays(years=2016),
            ("2016-01-01", "Aña Nobo"),
            ("2016-02-08", "Dialuna despues di Carnaval Grandi"),
            ("2016-03-25", "Bièrnèsantu"),
            ("2016-03-27", "Pasku di Resurekshon"),
            ("2016-03-28", "Di dos dia di Pasku di Resurekshon"),
            ("2016-04-27", "Dia di Rey"),
            ("2016-05-02", "Dia di Obrero"),
            ("2016-05-05", "Dia di Asenshon"),
            ("2016-07-02", "Dia di Himno i Bandera"),
            ("2016-10-10", "Dia di Pais Kòrsou"),
            ("2016-12-25", "Pasku di Nasementu"),
            ("2016-12-26", "Di dos dia di Pasku di Nasementu"),
        )

    def test_queens_day(self):
        name = "Dia di la Reina"
        self.assertHolidayName(
            name,
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
        name = "Dia di Rey"
        self.assertNoHolidayName(name, 2013)
        self.assertHolidayName(
            name,
            "2016-04-27",
            "2017-04-27",
            "2018-04-27",
            "2019-04-27",
            "2020-04-27",
            "2021-04-27",
            "2022-04-27",
            "2023-04-27",
            "2024-04-27",
            "2025-04-26",
            "2031-04-26",
            "2036-04-26",
        )
        self.assertNoHoliday(
            "2014-04-27",
            "2025-04-27",
            "2031-04-27",
            "2036-04-27",
        )

    def test_labor_day(self):
        self.assertHolidayName(
            "Dia di Obrero",
            "2016-05-02",
            "2017-05-01",
            "2018-05-01",
            "2019-05-01",
            "2020-05-01",
            "2021-05-01",
            "2022-05-02",
            "2023-05-01",
        )
        self.assertNoHoliday(
            "2011-05-01",
            "2016-05-01",
            "2022-05-01",
        )

    def test_anthem_and_flag_day(self):
        name = "Dia di Himno i Bandera"
        self.assertNoHolidayName(name, 1983)
        self.assertHolidayName(name, (f"{year}-07-02" for year in range(1984, 2077)))

    def test_curacao_day(self):
        name = "Dia di Pais Kòrsou"
        self.assertNoHolidayName(name, 2009)
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(2010, 2077)))
