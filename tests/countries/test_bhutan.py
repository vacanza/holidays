#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.bhutan import Bhutan, BT, BTN
from tests.common import CommonCountryTests


class TestBhutan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bhutan, years=range(1970, 2050))

    def test_country_aliases(self):
        self.assertAliases(Bhutan, BT, BTN)

    def test_no_holidays(self):
        self.assertNoHolidays(Bhutan(years=2006))

    def test_winter_solstice(self):
        self.assertHolidayName("Winter Solstice", (f"{year}-01-02" for year in range(2007, 2050)))

    def test_losar(self):
        name = "Losar"
        self.assertHolidayName(
            name,
            "2020-02-24",
            "2021-02-12",
            "2022-03-03",
            "2023-02-21",
            "2024-02-11",
            "2025-02-28",
        )
        self.assertHolidayName(name, range(2007, 2050))

    def test_birthday_anniversary_of_his_majesty_the_king(self):
        name = "Birth Anniversary of His Majesty the King"
        self.assertHolidayName(name, (f"{year}-02-21" for year in range(2007, 2050)))
        self.assertHolidayName(name, (f"{year}-02-22" for year in range(2007, 2050)))
        self.assertHolidayName(name, (f"{year}-02-23" for year in range(2007, 2050)))

    def test_birth_anniversary_third_druk_gyalpo(self):
        self.assertHolidayName(
            "Birth Anniversary of the 3rd Druk Gyalpo",
            (f"{year}-05-02" for year in range(2007, 2050)),
        )

    def test_lord_buddha_parinirvana(self):
        name = "Lord Buddha's Parinirvana"
        self.assertHolidayName(
            name,
            "2020-06-05",
            "2021-05-26",
            "2022-06-14",
            "2023-06-04",
            "2024-05-23",
            "2025-06-11",
        )
        self.assertHolidayName(name, range(2007, 2050))

    def test_birth_anniversary_guru_rinpoche(self):
        name = "Birth Anniversary of Guru Rinpoche"
        self.assertHolidayName(
            name,
            "2020-06-30",
            "2021-06-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-07-05",
        )
        self.assertHolidayName(name, range(2007, 2050))

    def test_first_sermon_lord_buddha(self):
        name = "First Sermon of Lord Buddha"
        self.assertHolidayName(
            name,
            "2020-07-24",
            "2021-07-14",
            "2022-08-01",
            "2023-07-21",
            "2024-07-10",
            "2025-07-28",
        )
        self.assertHolidayName(name, range(2007, 2050))

    def test_thimphu_drubchoe(self):
        name = "Thimphu Drubchoe"
        self.assertHolidayName(
            name,
            "2020-09-23",
            "2021-09-13",
            "2022-10-02",
            "2023-09-22",
            "2024-10-09",
            "2025-09-29",
        )
        self.assertHolidayName(name, range(2007, 2050))

    def test_thimphu_tshechu(self):
        name = "Thimphu Tshechu"
        distinct_dates = [
            "2020-09-26",
            "2021-09-16",
            "2022-10-05",
            "2023-09-24",
            "2024-10-12",
            "2025-10-02",
        ]
        for start_date in distinct_dates:
            year, month, day = map(int, start_date.split("-"))
            for offset in range(3):
                date_str = f"{year:04d}-{month:02d}-{day + offset:02d}"
                self.assertHolidayName(name, date_str)
        self.assertHolidayName(name, range(2007, 2050))

    def test_blessed_rainy_day(self):
        name = "Blessed Rainy Day"
        self.assertHolidayName(
            name,
            "2020-09-22",
            "2021-09-23",
            "2022-09-23",
            "2023-09-23",
            "2024-09-23",
            "2025-09-23",
        )
        self.assertHolidayName(name, range(2007, 2050))

    def test_dassain(self):
        name = "Dassain"
        self.assertHolidayName(
            name,
            "2020-10-25",
            "2021-10-15",
            "2022-10-05",
            "2023-10-24",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertHolidayName(name, range(2007, 2050))

    def test_coronation_his_majesty(self):
        self.assertHolidayName(
            "Coronation of His Majesty the King", (f"{year}-11-01" for year in range(2007, 2050))
        )

    def test_birth_anniversary_fourth_druk_gyalpo(self):
        self.assertHolidayName(
            "Birth Anniversary of the 4th Druk Gyalpo - Constitution Day",
            (f"{year}-11-11" for year in range(2007, 2050)),
        )

    def test_descending_day_lord_buddha(self):
        name = "Descending Day of Lord Buddha"
        self.assertHolidayName(
            name,
            "2020-11-07",
            "2021-10-27",
            "2022-11-15",
            "2023-11-04",
            "2024-11-22",
            "2025-11-11",
        )
        self.assertHolidayName(name, range(2007, 2050))

    def test_national_day(self):
        self.assertHolidayName("National Day", (f"{year}-12-17" for year in range(2007, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-02", "Winter Solstice"),
            ("2024-01-12", "Traditional Day of Offering"),
            ("2024-02-11", "Losar"),
            ("2024-02-12", "Losar"),
            ("2024-02-21", "Birth Anniversary of His Majesty the King"),
            ("2024-02-22", "Birth Anniversary of His Majesty the King"),
            ("2024-02-23", "Birth Anniversary of His Majesty the King"),
            ("2024-04-18", "Death Anniversary of Zhabdrung (Zhabdrung Kuchoe)"),
            ("2024-05-02", "Birth Anniversary of the 3rd Druk Gyalpo"),
            ("2024-05-23", "Lord Buddha's Parinirvana"),
            ("2024-06-16", "Birth Anniversary of Guru Rinpoche"),
            ("2024-07-10", "First Sermon of Lord Buddha"),
            ("2024-09-23", "Blessed Rainy Day"),
            ("2024-10-09", "Thimphu Drubchoe"),
            ("2024-10-12", "Dassain; Thimphu Tshechu"),
            ("2024-10-13", "Thimphu Tshechu"),
            ("2024-10-14", "Thimphu Tshechu"),
            ("2024-11-01", "Coronation of His Majesty the King"),
            ("2024-11-11", "Birth Anniversary of the 4th Druk Gyalpo - Constitution Day"),
            ("2024-11-22", "Descending Day of Lord Buddha"),
            ("2024-12-17", "National Day"),
        )
