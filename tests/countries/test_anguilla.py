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

from holidays.countries.anguilla import Anguilla, AI, AIA
from tests.common import CommonCountryTests


class TestAnguilla(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Anguilla)

    def test_country_aliases(self):
        self.assertAliases(Anguilla, AI, AIA)

    def test_no_holidays(self):
        self.assertNoHolidays(Anguilla(years=AI.start_year - 1))

    def test_special_holiday(self):
        self.assertHolidayName("Royal Wedding of Prince William & Kate Middleton", "2011-04-29")
        self.assertHolidayName(
            "Diamond Jubilee Celebration of Her Majesty The Queen", "2012-06-04"
        )
        self.assertHolidayName(
            "Mourning the Death of Her Majesty The Queen Elizabeth II", "2022-09-19"
        )
        self.assertHolidayName("Special Public Holiday", "2025-02-28")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_james_ronald_webster_day(self):
        name = "James Ronald Webster Day"
        self.assertHolidayName(name, (f"{year}-03-02" for year in range(2010, 2050)))
        self.assertNoHolidayName(name, range(AI.start_year, 2010))
        dt = (
            "2013-03-04",
            "2014-03-03",
            "2019-03-04",
            "2024-03-04",
            "2025-03-03",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        dt = (
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        dt = (
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Easter Sunday"
        dt = (
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        dt = (
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_queen_birthday(self):
        name = "Celebration of the Birthday of Her Majesty the Queen"
        self.assertHolidayName(
            name,
            "2016-06-13",
            "2017-06-12",
            "2018-06-11",
            "2019-06-10",
            "2020-06-08",
            "2021-06-14",
            "2022-06-03",
        )
        self.assertHolidayName(name, range(AI.start_year, 2023))
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_king_birthday(self):
        name = "Celebration of the Birthday of His Majesty the King"
        self.assertHolidayName(
            name,
            "2023-06-19",
            "2024-06-17",
            "2025-06-16",
        )
        self.assertHolidayName(name, range(2023, 2050))
        self.assertNoHolidayName(name, range(AI.start_year, 2023))

    def test_anguilla_day(self):
        name = "Anguilla Day"
        self.assertHolidayName(name, (f"{year}-05-30" for year in self.full_range))
        dt = (
            "2004-06-01",
            "2009-06-02",
            "2010-05-31",
            "2015-06-01",
            "2020-06-02",
            "2021-05-31",
            "2039-05-31",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_august_monday(self):
        name = "August Monday"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, self.full_range)

    def test_august_thursday(self):
        name = "August Thursday"
        self.assertHolidayName(
            name,
            "2020-08-06",
            "2021-08-05",
            "2022-08-04",
            "2023-08-10",
            "2024-08-08",
            "2025-08-07",
        )
        self.assertHolidayName(name, self.full_range)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(
            name,
            "2020-08-07",
            "2021-08-06",
            "2022-08-05",
            "2023-08-11",
            "2024-08-09",
            "2025-08-08",
        )
        self.assertHolidayName(name, self.full_range)

    def test_national_heroes_and_heroines_day(self):
        name_2001 = "Separation Day"
        self.assertHolidayName(name_2001, (f"{year}-12-19" for year in range(AI.start_year, 2011)))
        self.assertNoHolidayName(name_2001, range(2011, 2050))
        dt_2001 = (
            "2004-12-17",
            "2009-12-18",
            "2010-12-17",
        )
        self.assertHolidayName(f"{name_2001} (observed)", dt_2001)
        self.assertNoNonObservedHoliday(dt_2001)

        name_2011 = "National Heroes and Heroines Day"
        self.assertHolidayName(name_2011, (f"{year}-12-19" for year in range(2011, 2050)))
        self.assertNoHolidayName(name_2011, range(AI.start_year, 2011))
        dt_2011 = (
            "2015-12-18",
            "2020-12-18",
            "2021-12-17",
        )
        self.assertHolidayName(f"{name_2011} (observed)", dt_2011)
        self.assertNoNonObservedHoliday(dt_2011)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        dt = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        dt = (
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-03-02", "James Ronald Webster Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-05-30", "Anguilla Day"),
            ("2022-06-03", "Celebration of the Birthday of Her Majesty the Queen"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-01", "August Monday"),
            ("2022-08-04", "August Thursday"),
            ("2022-08-05", "Constitution Day"),
            ("2022-09-19", "Mourning the Death of Her Majesty The Queen Elizabeth II"),
            ("2022-12-19", "National Heroes and Heroines Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-03-02", "James Ronald Webster Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-05-30", "Anguilla Day"),
            ("2022-06-03", "Queen's Birthday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-01", "August Monday"),
            ("2022-08-04", "August Thursday"),
            ("2022-08-05", "Constitution Day"),
            ("2022-09-19", "Mourning the Death of Her Majesty The Queen Elizabeth II"),
            ("2022-12-19", "National Heroes and Heroines Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
