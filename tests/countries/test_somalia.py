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

from holidays.countries.somalia import Somalia, SO, SOM
from tests.common import CommonCountryTests


class TestSomalia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1960, 2050)
        super().setUpClass(Somalia, years=years)
        cls.no_estimated_holidays = Somalia(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Somalia, SO, SOM)

    def test_no_holidays(self):
        self.assertNoHolidays(Somalia(years=1959))

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1960, 2050)))

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(1960, 2050)))

    def test_restoration_of_somaliland_sovereignty_day(self):
        self.assertHolidayName(
            "Restoration of Somaliland Sovereignty Day",
            (f"{year}-05-18" for year in range(1960, 2050)),
            (f"{year}-05-19" for year in range(1960, 2050)),
        )

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-06-26" for year in range(1960, 2050)))

    def test_republic_day(self):
        self.assertHolidayName("Republic Day", (f"{year}-07-01" for year in range(1960, 2050)))

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))

    def test_birthday_of_muhammad(self):
        name = "Birthday of Muhammad"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))

    def test_muhammads_ascension_to_heaven(self):
        name = "Muhammad's Ascension to Heaven"
        self.assertHolidayName(
            name,
            "2020-03-22",
            "2021-03-11",
            "2022-02-28",
            "2023-02-18",
            "2024-02-08",
            "2025-01-27",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))

    def test_islamic_new_year(self):
        name = "Islamic New Year (estimated)"
        self.assertHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_ashura(self):
        name = "Ashura"
        self.assertHolidayName(
            name,
            "2020-08-29",
            "2021-08-18",
            "2022-08-08",
            "2023-07-28",
            "2024-07-16",
            "2025-07-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))

    def test_2018(self):
        self.assertHolidays(
            Somalia(years=2018),
            ("2018-01-01", "New Year's Day"),
            ("2018-04-13", "Muhammad's Ascension to Heaven"),
            ("2018-05-01", "Labour Day"),
            ("2018-05-18", "Restoration of Somaliland Sovereignty Day"),
            ("2018-05-19", "Restoration of Somaliland Sovereignty Day"),
            ("2018-06-15", "Eid al-Fitr"),
            ("2018-06-26", "Independence Day"),
            ("2018-07-01", "Republic Day"),
            ("2018-08-21", "Eid al-Adha"),
            ("2018-09-11", "Islamic New Year (estimated)"),
            ("2018-09-20", "Ashura"),
            ("2018-11-20", "Birthday of Muhammad"),
        )
