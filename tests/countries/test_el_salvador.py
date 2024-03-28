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

from holidays.countries.el_salvador import ElSalvador, SV, SLV
from tests.common import CommonCountryTests


class TestElSalvador(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ElSalvador, years=range(2000, 2050))

    def test_country_aliases(self):
        self.assertAliases(ElSalvador, SV, SLV)

    def test_mothers_day(self):
        name = "Mothers' Day"
        self.assertHolidayName(name, (f"{year}-05-10" for year in range(2016, 2050)))
        self.assertNoHoliday(f"{year}-05-10" for year in range(2000, 2016))
        self.assertNoHolidayName(name, range(2000, 2016))

    def test_fathers_day(self):
        name = "Fathers' Day"
        self.assertHolidayName(name, (f"{year}-06-17" for year in range(2013, 2050)))
        self.assertNoHoliday(f"{year}-06-17" for year in range(2000, 2013))
        self.assertNoHolidayName(name, range(2000, 2013))

    def test_ss_holidays(self):
        name1 = "San Salvador Day 1"
        name2 = "San Salvador Day 2"
        self.assertNoHolidayName(name1, range(2000, 2050))
        self.assertNoHolidayName(name2, range(2000, 2050))
        ss_holidays = ElSalvador(subdiv="SS", years=range(2000, 2050))
        self.assertHolidayName(name1, ss_holidays, (f"{year}-08-03" for year in range(2016, 2050)))
        self.assertHolidayName(name2, ss_holidays, (f"{year}-08-05" for year in range(2016, 2050)))

    def test_2021(self):
        self.assertHolidays(
            ElSalvador(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-04-01", "Maundy Thursday"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-03", "Holy Saturday"),
            ("2021-05-01", "Labor Day"),
            ("2021-05-10", "Mothers' Day"),
            ("2021-06-17", "Fathers' Day"),
            ("2021-08-06", "Feast of San Salvador"),
            ("2021-09-15", "Independence Day"),
            ("2021-11-02", "All Souls' Day"),
            ("2021-12-25", "Christmas Day"),
        )

    def test_2022(self):
        self.assertHolidays(
            ElSalvador(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-10", "Mothers' Day"),
            ("2022-06-17", "Fathers' Day"),
            ("2022-08-06", "Feast of San Salvador"),
            ("2022-09-15", "Independence Day"),
            ("2022-11-02", "All Souls' Day"),
            ("2022-12-25", "Christmas Day"),
        )
