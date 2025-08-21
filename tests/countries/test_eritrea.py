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

from holidays.constants import GOVERNMENT
from holidays.countries.eritrea import Eritrea, ER, ERI
from tests.common import CommonCountryTests


class TestEritrea(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1994, 2050)
        super().setUpClass(Eritrea, years=years)
        cls.government_holidays = Eritrea(categories=GOVERNMENT, years=years)
        cls.no_estimated_holidays = Eritrea(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Eritrea, ER, ERI)

    def test_no_holidays(self):
        self.assertNoHolidays(Eritrea(categories=Eritrea.supported_categories, years=1993))

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1994, 2050)))

    def test_orthodox_christmas(self):
        self.assertHolidayName(
            "Orthodox Christmas", (f"{year}-01-07" for year in range(1994, 2050))
        )

    def test_epiphany(self):
        self.assertHolidayName(
            "Epiphany",
            (f"{year}-01-19" for year in range(1994, 2050) if year % 4 != 0),
            (f"{year}-01-20" for year in range(1994, 2050) if year % 4 == 0),
        )

    def test_womens_day(self):
        self.assertHolidayName("Women's Day", (f"{year}-03-08" for year in range(1994, 2050)))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1994, 2050))

    def test_orthodox_easter(self):
        name = "Orthodox Easter"
        self.assertHolidayName(
            name,
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1994, 2050))

    def test_international_workers_day(self):
        self.assertHolidayName(
            "International Workers' Day", (f"{year}-05-01" for year in range(1994, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-05-24" for year in range(1994, 2050)))

    def test_martyrs_day(self):
        self.assertHolidayName("Martyrs' Day", (f"{year}-06-20" for year in range(1994, 2050)))

    def test_revolution_day(self):
        self.assertHolidayName("Revolution Day", (f"{year}-09-01" for year in range(1994, 2050)))

    def test_ethiopian_new_year(self):
        self.assertHolidayName(
            "Ethiopian New Year",
            (f"{year}-09-11" for year in range(1994, 2050) if year % 4 != 3),
            (f"{year}-09-12" for year in range(1994, 2050) if year % 4 == 3),
        )

    def test_finding_of_the_true_cross(self):
        self.assertHolidayName(
            "Finding of the True Cross",
            (f"{year}-09-27" for year in range(1994, 2050) if year % 4 != 3),
            (f"{year}-09-28" for year in range(1994, 2050) if year % 4 == 3),
        )

    def test_prophets_birthday(self):
        name = "Prophet's Birthday"

        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1994, 2050))

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1994, 2050))

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1994, 2050))

    def test_fenkil_day(self):
        name = "Fenkil Day"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.government_holidays, (f"{year}-02-10" for year in range(1994, 2050))
        )

    def test_2020(self):
        self.assertHolidays(
            Eritrea(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-01-07", "Orthodox Christmas"),
            ("2020-01-20", "Epiphany"),
            ("2020-03-08", "Women's Day"),
            ("2020-04-17", "Good Friday"),
            ("2020-04-19", "Orthodox Easter"),
            ("2020-05-01", "International Workers' Day"),
            ("2020-05-24", "Eid al-Fitr (estimated); Independence Day"),
            ("2020-06-20", "Martyrs' Day"),
            ("2020-07-31", "Eid al-Adha (estimated)"),
            ("2020-09-01", "Revolution Day"),
            ("2020-09-11", "Ethiopian New Year"),
            ("2020-09-27", "Finding of the True Cross"),
            ("2020-10-29", "Prophet's Birthday (estimated)"),
        )

    def test_2020_government(self):
        self.assertHolidays(
            Eritrea(years=2020, categories=GOVERNMENT),
            ("2020-02-10", "Fenkil Day"),
        )
