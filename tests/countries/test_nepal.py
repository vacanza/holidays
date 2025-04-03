#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import PUBLIC, WORKDAY
from holidays.countries.nepal import Nepal, NP, NPL
from tests.common import CommonCountryTests


class TestNepal(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1924, 2050)
        super().setUpClass(Nepal, years=years)
        cls.workday_holidays = Nepal(categories=WORKDAY, years=years)

    def test_country_aliases(self):
        self.assertAliases(Nepal, NP, NPL)

    def test_no_holidays(self):
        self.assertNoHolidays(Nepal(years=1923, categories=(PUBLIC, WORKDAY)))

    def test_special_holidays(self):
        name_day_of_national_mourning = "Day of National Mourning"

        for dt, name in (
            ("1999-02-09", name_day_of_national_mourning),
            ("2011-03-06", name_day_of_national_mourning),
            ("2016-02-10", name_day_of_national_mourning),
            ("2023-01-16", name_day_of_national_mourning),
            ("2023-02-13", "People War's Day"),
            ("2023-09-14", name_day_of_national_mourning),
        ):
            self.assertHolidayName(name, dt)

    def test_prithvi_jayanti(self):
        name = "Prithvi Jayanti"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-01-11" for year in range(2021, 2050)))
        self.assertNoHolidayName(name, (f"{year}-01-11" for year in range(2019, 2021)))

        # Workdays.
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-01-11" for year in range(2019, 2021))
        )
        self.assertNoHolidayName(
            name, self.workday_holidays, (f"{year}-01-11" for year in range(2021, 2050))
        )

    def test_martyrs_day(self):
        name = "Martyr's Day"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-01-30" for year in range(2021, 2050)))
        self.assertNoHolidayName(name, (f"{year}-01-30" for year in range(2019, 2021)))

        # Workdays.
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-01-30" for year in range(2019, 2021))
        )
        self.assertNoHolidayName(
            name, self.workday_holidays, (f"{year}-01-30" for year in range(2021, 2050))
        )

    def test_national_democracy_day(self):
        name = "National Democracy Day"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-02-19" for year in range(2021, 2050)))
        self.assertNoHolidayName(name, (f"{year}-02-19" for year in range(2019, 2021)))

        # Workdays.
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-02-19" for year in range(2019, 2021))
        )
        self.assertNoHolidayName(
            name, self.workday_holidays, (f"{year}-02-19" for year in range(2021, 2050))
        )

    def test_womens_day(self):
        self.assertHolidayName("Women's Day", (f"{year}-03-08" for year in range(2019, 2050)))

    def test_labor_day(self):
        self.assertHolidayName("Labor Day", (f"{year}-05-01" for year in range(2019, 2050)))

    def test_republic_day(self):
        name = "Republic Day"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-05-29" for year in range(2021, 2050)))
        self.assertNoHolidayName(name, (f"{year}-05-29" for year in range(2019, 2021)))

        # Workdays.
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-05-29" for year in range(2019, 2021))
        )
        self.assertNoHolidayName(
            name, self.workday_holidays, (f"{year}-05-29" for year in range(2021, 2050))
        )

    def test_constitution_day(self):
        self.assertHolidayName("Constitution Day", (f"{year}-09-19" for year in range(2019, 2050)))

    def test_christmas(self):
        self.assertHolidayName("Christmas", (f"{year}-12-25" for year in range(2019, 2050)))

    def test_tamu_losar(self):
        self.assertHolidayName("Tamu Losar", (f"{year}-12-30" for year in range(2019, 2050)))

    def test_ranged_holidays(self):
        name = "Bakrid"
        dt = (
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2021, 2026))

        name = "Bhai Tika"
        dt = (
            "2019-10-29",
            "2020-11-16",
            "2021-11-06",
            "2022-10-26",
            "2023-11-14",
            "2024-11-03",
            "2025-10-23",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Buddha Jayanti"
        dt = (
            "2019-05-18",
            "2020-05-07",
            "2021-05-26",
            "2022-05-16",
            "2023-05-05",
            "2024-05-23",
            "2025-05-12",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Chhath Parwa"
        dt = (
            "2019-11-02",
            "2020-11-20",
            "2021-11-10",
            "2022-10-30",
            "2023-11-19",
            "2024-11-07",
            "2025-10-28",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Duwadashi (Dashain)"
        dt = (
            "2021-10-17",
            "2022-10-07",
            "2023-10-26",
            "2024-10-14",
            "2025-10-04",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2019))
        self.assertHolidayName(name, range(2021, 2036))
        dt = (
            "2019-10-10",
            "2020-10-27",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, dt)

        name = "Ekadashi (Dashain)"
        dt = (
            "2019-10-09",
            "2020-10-26",
            "2021-10-16",
            "2022-10-06",
            "2023-10-25",
            "2024-10-13",
            "2025-10-03",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Gai Tihar"
        dt = (
            "2019-10-27",
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-11-01",
            "2025-10-21",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Ghatasthapana"
        dt = (
            "2021-10-07",
            "2022-09-26",
            "2023-10-15",
            "2024-10-03",
            "2025-09-22",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2019))
        self.assertHolidayName(name, range(2021, 2036))
        dt = (
            "2019-09-29",
            "2020-10-17",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, dt)

        name = "Govardhan Puja"
        dt = (
            "2019-10-28",
            "2020-11-15",
            "2021-11-05",
            "2022-10-25",
            "2023-11-13",
            "2024-11-02",
            "2025-10-22",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Gyalpo Losar"
        dt = (
            "2019-03-07",
            "2020-02-24",
            "2021-03-14",
            "2022-03-03",
            "2023-02-21",
            "2024-03-11",
            "2025-02-28",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2016, 2036))

        name = "Holi (Mountain & Hilly)"
        dt = (
            "2019-03-20",
            "2020-03-09",
            "2021-03-28",
            "2022-03-17",
            "2023-03-07",
            "2024-03-24",
            "2025-03-13",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Holi (Terai)"
        dt = (
            "2019-03-21",
            "2020-03-10",
            "2021-03-29",
            "2022-03-18",
            "2023-03-08",
            "2024-03-25",
            "2025-03-14",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Id-ul-Fitr"
        dt = (
            "2019-06-05",
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-03-31",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2026))

        name = "Janai Purnima"
        dt = (
            "2021-08-22",
            "2022-08-11",
            "2023-08-30",
            "2024-08-19",
            "2025-08-09",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2019))
        self.assertHolidayName(name, range(2021, 2036))
        dt = (
            "2019-08-15",
            "2020-08-03",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, dt)

        name = "Shree Krishna Janmashtami"
        dt = (
            "2021-08-30",
            "2022-08-19",
            "2023-09-07",
            "2024-08-26",
            "2025-08-16",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2019))
        self.assertHolidayName(name, range(2021, 2036))
        dt = (
            "2019-08-24",
            "2020-08-12",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, dt)

        name = "Lakshmi Puja"
        dt = (
            "2019-10-27",
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-11-01",
            "2025-10-20",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Maha Ashtami"
        dt = (
            "2019-10-06",
            "2020-10-23",
            "2021-10-13",
            "2022-10-03",
            "2023-10-22",
            "2024-10-10",
            "2025-09-30",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Maha Navami"
        dt = (
            "2019-10-07",
            "2020-10-24",
            "2021-10-14",
            "2022-10-04",
            "2023-10-23",
            "2024-10-11",
            "2025-10-01",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Maghe Sankranti"
        dt = (
            "2019-01-15",
            "2020-01-15",
            "2021-01-14",
            "2022-01-14",
            "2023-01-14",
            "2024-01-14",
            "2025-01-14",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Mha Puja"
        dt = (
            "2019-10-28",
            "2020-11-15",
            "2021-11-05",
            "2022-10-25",
            "2023-11-13",
            "2024-11-02",
            "2025-10-22",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Nepali New Year (Vikram Sambat)"
        dt = (
            "2019-04-14",
            "2020-04-13",
            "2021-04-14",
            "2022-04-14",
            "2023-04-14",
            "2024-04-13",
            "2025-04-13",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Phulpati"
        dt = (
            "2019-10-05",
            "2020-10-22",
            "2021-10-12",
            "2022-10-02",
            "2023-10-21",
            "2024-10-09",
            "2025-09-29",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Ram Navami"
        dt = (
            "2021-04-21",
            "2022-04-10",
            "2023-03-30",
            "2024-04-17",
            "2025-04-06",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2019))
        self.assertHolidayName(name, range(2021, 2036))
        dt = (
            "2019-04-13",
            "2020-04-02",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, dt)

        name = "Sonam Losar"
        dt = (
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-02",
            "2023-01-22",
            "2024-02-10",
            "2025-01-30",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2016, 2036))

        name = "Tihar Holiday"
        dt = (
            "2019-10-30",
            "2020-11-17",
            "2021-11-07",
            "2022-10-27",
            "2023-11-15",
            "2024-11-04",
            "2025-10-24",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

        name = "Vijayadashami"
        dt = (
            "2019-10-08",
            "2020-10-25",
            "2021-10-15",
            "2022-10-05",
            "2023-10-24",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2001, 2036))

    def test_2025(self):
        self.assertHolidays(
            Nepal(years=2025),
            ("2025-01-11", "Prithvi Jayanti"),
            ("2025-01-14", "Maghe Sankranti"),
            ("2025-01-30", "Martyr's Day; Sonam Losar"),
            ("2025-02-19", "National Democracy Day"),
            ("2025-02-26", "Maha Shivaratri"),
            ("2025-02-28", "Gyalpo Losar"),
            ("2025-03-08", "Women's Day"),
            ("2025-03-13", "Holi (Mountain & Hilly)"),
            ("2025-03-14", "Holi (Terai)"),
            ("2025-03-31", "Id-ul-Fitr"),
            ("2025-04-06", "Ram Navami"),
            ("2025-04-13", "Nepali New Year (Vikram Sambat)"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-12", "Buddha Jayanti"),
            ("2025-05-29", "Republic Day"),
            ("2025-06-07", "Bakrid"),
            ("2025-08-09", "Janai Purnima"),
            ("2025-08-16", "Shree Krishna Janmashtami"),
            ("2025-09-19", "Constitution Day"),
            ("2025-09-22", "Ghatasthapana"),
            ("2025-09-29", "Phulpati"),
            ("2025-09-30", "Maha Ashtami"),
            ("2025-10-01", "Maha Navami"),
            ("2025-10-02", "Vijayadashami"),
            ("2025-10-03", "Ekadashi (Dashain)"),
            ("2025-10-04", "Duwadashi (Dashain)"),
            ("2025-10-20", "Lakshmi Puja"),
            ("2025-10-21", "Gai Tihar"),
            ("2025-10-22", "Govardhan Puja; Mha Puja"),
            ("2025-10-23", "Bhai Tika"),
            ("2025-10-24", "Tihar Holiday"),
            ("2025-10-28", "Chhath Parwa"),
            ("2025-12-25", "Christmas"),
            ("2025-12-30", "Tamu Losar"),
        )
