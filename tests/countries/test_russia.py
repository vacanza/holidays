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

from holidays.countries.russia import Russia, RU, RUS
from tests.common import CommonCountryTests


class TestRussia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Russia, years=range(1991, 2025))

    def test_country_aliases(self):
        self.assertAliases(Russia, RU, RUS)

    def test_no_holidays(self):
        self.assertNoHolidays(Russia(years=1990))

    def test_special_holidays(self):
        self.assertHoliday(
            "2023-02-24",
            "2023-05-08",
        )

    def test_new_year(self):
        name_1 = "Новый год"
        name_2 = "Новогодние каникулы"
        self.assertHolidayName(name_1, (f"{year}-01-01" for year in range(1991, 2005)))
        self.assertHolidayName(name_1, (f"{year}-01-02" for year in range(1993, 2005)))
        self.assertNoHoliday(f"{year}-01-02" for year in range(1991, 1992))
        for year in range(2005, 2025):
            self.assertHolidayName(
                name_2,
                f"{year}-01-01",
                f"{year}-01-02",
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
            )
        for year in range(2013, 2025):
            self.assertHolidayName(name_2, f"{year}-01-06", f"{year}-01-08")
        for year in range(1991, 2005):
            self.assertNoHoliday(f"{year}-01-03", f"{year}-01-04", f"{year}-01-05")
        for year in range(1991, 2013):
            self.assertNoHoliday(f"{year}-01-06", f"{year}-01-08")
        self.assertNoHolidayName(name_1, range(2005, 2025))
        self.assertNoHolidayName(name_2, range(1991, 2005))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Рождество Христово", (f"{year}-01-07" for year in range(1991, 2025))
        )

    def test_defender_of_fatherland_day(self):
        name = "День защитника Отечества"
        self.assertHolidayName(name, (f"{year}-02-23" for year in range(2002, 2025)))
        self.assertNoHoliday(f"{year}-02-23" for year in range(1991, 2002))
        self.assertNoHolidayName(name, range(1991, 2002))

    def test_international_womens_day(self):
        self.assertHolidayName(
            "Международный женский день", (f"{year}-03-08" for year in range(1991, 2025))
        )

    def test_labor_day(self):
        name_1 = "День международной солидарности трудящихся"
        name_2 = "Праздник Весны и Труда"
        self.assertHolidayName(name_1, "1991-05-01", "1991-05-02")
        self.assertHolidayName(name_2, (f"{year}-05-01" for year in range(1992, 2025)))
        self.assertHolidayName(name_2, (f"{year}-05-02" for year in range(1992, 2005)))
        self.assertNoHoliday(f"{year}-05-02" for year in range(2005, 2025))
        self.assertNoHolidayName(name_1, range(1992, 2025))
        self.assertNoHolidayName(name_2, 1991)

    def test_victory_day(self):
        self.assertHolidayName("День Победы", (f"{year}-05-09" for year in range(1991, 2025)))

    def test_russia_day(self):
        name_1 = "День принятия Декларации о государственном суверенитете Российской Федерации"
        name_2 = "День России"
        self.assertHolidayName(name_1, (f"{year}-06-12" for year in range(1992, 2002)))
        self.assertHolidayName(name_2, (f"{year}-06-12" for year in range(2002, 2025)))
        self.assertNoHoliday("1991-06-12")
        self.assertNoHolidayName(name_1, 1991, range(2002, 2025))
        self.assertNoHolidayName(name_2, range(1991, 2002))

    def test_unity_day(self):
        name = "День народного единства"
        self.assertHolidayName(name, (f"{year}-11-04" for year in range(2005, 2025)))
        self.assertNoHoliday(f"{year}-11-04" for year in range(1991, 2005))
        self.assertNoHolidayName(name, range(1991, 2005))

    def test_october_revolution(self):
        name_1 = "Годовщина Великой Октябрьской социалистической революции"
        name_2 = "День согласия и примирения"
        self.assertHolidayName(name_1, (f"{year}-11-07" for year in range(1991, 1996)))
        self.assertHolidayName(name_1, "1991-11-08")
        self.assertHolidayName(name_2, (f"{year}-11-07" for year in range(1996, 2005)))
        self.assertNoHoliday(f"{year}-11-07" for year in range(2005, 2025))
        self.assertNoHoliday(f"{year}-11-08" for year in range(1992, 2025))
        self.assertNoHolidayName(name_1, range(1996, 2025))
        self.assertNoHolidayName(name_2, range(1991, 1996), range(2005, 2025))

    def test_2018(self):
        self.assertHolidays(
            Russia(years=2018),
            ("2018-01-01", "Новогодние каникулы"),
            ("2018-01-02", "Новогодние каникулы"),
            ("2018-01-03", "Новогодние каникулы"),
            ("2018-01-04", "Новогодние каникулы"),
            ("2018-01-05", "Новогодние каникулы"),
            ("2018-01-06", "Новогодние каникулы"),
            ("2018-01-07", "Рождество Христово"),
            ("2018-01-08", "Новогодние каникулы"),
            ("2018-02-23", "День защитника Отечества"),
            ("2018-03-08", "Международный женский день"),
            ("2018-05-01", "Праздник Весны и Труда"),
            ("2018-05-09", "День Победы"),
            ("2018-06-12", "День России"),
            ("2018-11-04", "День народного единства"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Новогодние каникулы"),
            ("2018-01-02", "Новогодние каникулы"),
            ("2018-01-03", "Новогодние каникулы"),
            ("2018-01-04", "Новогодние каникулы"),
            ("2018-01-05", "Новогодние каникулы"),
            ("2018-01-06", "Новогодние каникулы"),
            ("2018-01-07", "Рождество Христово"),
            ("2018-01-08", "Новогодние каникулы"),
            ("2018-02-23", "День защитника Отечества"),
            ("2018-03-08", "Международный женский день"),
            ("2018-05-01", "Праздник Весны и Труда"),
            ("2018-05-09", "День Победы"),
            ("2018-06-12", "День России"),
            ("2018-11-04", "День народного единства"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year Holidays"),
            ("2018-01-02", "New Year Holidays"),
            ("2018-01-03", "New Year Holidays"),
            ("2018-01-04", "New Year Holidays"),
            ("2018-01-05", "New Year Holidays"),
            ("2018-01-06", "New Year Holidays"),
            ("2018-01-07", "Christmas Day"),
            ("2018-01-08", "New Year Holidays"),
            ("2018-02-23", "Fatherland Defender's Day"),
            ("2018-03-08", "International Women's Day"),
            ("2018-05-01", "Holiday of Spring and Labor"),
            ("2018-05-09", "Victory Day"),
            ("2018-06-12", "Russia Day"),
            ("2018-11-04", "Unity Day"),
        )
