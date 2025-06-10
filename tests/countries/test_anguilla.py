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
        years = range(2011, 2050)
        super().setUpClass(Anguilla, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(Anguilla, AI, AIA)

    def test_special_holidays(self):
        self.assertHoliday("2011-04-29", "2012-06-04", "2025-02-28")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2011, 2050)))
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
        self.assertHolidayName(name, (f"{year}-03-02" for year in range(2011, 2050)))
        dt = ("2013-03-04", "2014-03-03", "2019-03-04", "2024-03-04", "2025-03-03")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        dt = (
            "2011-04-22",
            "2012-04-06",
            "2013-03-29",
            "2014-04-18",
            "2015-04-03",
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2011, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        dt = (
            "2011-04-25",
            "2012-04-09",
            "2013-04-01",
            "2014-04-21",
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2011, 2050))

    def test_easter_sunday(self):
        name = "Easter Sunday"
        dt = (
            "2011-04-24",
            "2012-04-08",
            "2013-03-31",
            "2014-04-20",
            "2015-04-05",
            "2016-03-27",
            "2017-04-16",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2011, 2050))

    def test_labor_day(self):
        name = "Labor Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2011, 2050)))
        dt = ("2011-05-02", "2016-05-02", "2021-05-03", "2022-05-02")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2011-06-13",
            "2012-05-28",
            "2013-05-20",
            "2014-06-09",
            "2015-05-25",
            "2016-05-16",
            "2017-06-05",
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_celebration_of_the_birthday_of_her_majesty_the_queen(self):
        name = "Celebration of the Birthday of Her Majesty the Queen"
        self.assertHolidayName(
            name,
            "2011-06-13",
            "2012-06-11",
            "2013-06-10",
            "2014-06-09",
            "2015-06-08",
            "2016-06-13",
            "2017-06-12",
            "2018-06-11",
            "2019-06-10",
            "2020-06-08",
            "2021-06-14",
            "2022-06-03",
        )
        self.assertHolidayName(name, range(2011, 2023))
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_anguilla_day(self):
        name = "Anguilla Day"
        self.assertHolidayName(
            name,
            "2011-05-30",
            "2012-05-30",
            "2013-05-30",
            "2014-05-30",
            "2015-05-30",
            "2016-05-30",
            "2017-05-30",
            "2018-05-30",
            "2019-05-30",
            "2020-05-30",
            "2021-05-31",
            "2022-05-30",
            "2023-05-30",
            "2024-05-30",
            "2025-05-30",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_august_monday_day(self):
        name = "August Monday"
        self.assertHolidayName(
            name,
            "2011-08-01",
            "2012-08-06",
            "2013-08-05",
            "2014-08-04",
            "2015-08-03",
            "2016-08-01",
            "2017-08-07",
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_august_thursday_day(self):
        name = "August Thursday"
        self.assertHolidayName(
            name,
            "2011-08-04",
            "2012-08-09",
            "2013-08-08",
            "2014-08-07",
            "2015-08-06",
            "2016-08-04",
            "2017-08-10",
            "2018-08-09",
            "2019-08-08",
            "2020-08-06",
            "2021-08-05",
            "2022-08-04",
            "2023-08-10",
            "2024-08-08",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(
            name,
            "2011-08-05",
            "2012-08-10",
            "2013-08-09",
            "2014-08-08",
            "2015-08-07",
            "2016-08-05",
            "2017-08-11",
            "2018-08-10",
            "2019-08-09",
            "2020-08-07",
            "2021-08-06",
            "2022-08-05",
            "2023-08-11",
            "2024-08-09",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_national_heroes_and_heroines_day(self):
        name = "National Heroes and Heroines Day"
        self.assertHolidayName(name, (f"{year}-12-19" for year in range(2011, 2050)))
        dt = ("2015-12-18", "2020-12-18", "2021-12-17")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2011, 2050)))

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2011, 2050)))
        dt = ("2015-12-28", "2020-12-28")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_special_holiday(self):
        name = "Royal Wedding of Prince William & Kate Middleton"
        self.assertHolidayName(name, "2011-04-29")

        name = "Diamond Jubilee Celebration of Her Majesty The Queen"
        self.assertHolidayName(name, "2012-06-04")

        name = "Special Public Holiday"
        self.assertHolidayName(name, "2025-02-28")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-03-02", "James Ronald Webster Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-05-30", "Anguilla Day"),
            ("2022-06-03", "Celebration of the Birthday of Her Majesty the Queen"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-01", "August Monday"),
            ("2022-08-04", "August Thursday"),
            ("2022-08-05", "Constitution Day"),
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
            ("2022-06-03", "Celebration of the Birthday of Her Majesty the Queen"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-01", "August Monday"),
            ("2022-08-04", "August Thursday"),
            ("2022-08-05", "Constitution Day"),
            ("2022-12-19", "National Heroes and Heroines Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
