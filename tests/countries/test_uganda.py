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

from holidays.countries.uganda import Uganda, UG, UGA
from tests.common import CommonCountryTests


class TestUganda(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1963, 2050)
        super().setUpClass(Uganda, years=years, years_non_observed=years)
        cls.no_estimated_holidays = Uganda(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Uganda, UG, UGA)

    def test_no_holidays(self):
        self.assertNoHolidays(Uganda(years=1962))

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1963, 2050)))

    def test_nrm_liberation_day(self):
        name = "NRM Liberation Day"
        self.assertHolidayName(name, (f"{year}-01-26" for year in range(1987, 2050)))
        self.assertNoHolidayName(name, range(1963, 1987))

    def test_archbishop_janani_luwum_day(self):
        name = "Archbishop Janani Luwum Day"
        self.assertHolidayName(name, (f"{year}-02-16" for year in range(2016, 2050)))
        self.assertNoHolidayName(name, range(1963, 2016))

    def test_womens_day(self):
        self.assertHolidayName("Women's Day", (f"{year}-03-08" for year in range(1963, 2050)))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1963, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1963, 2050))

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(1963, 2050)))

    def test_uganda_martyrs_day(self):
        self.assertHolidayName(
            "Uganda Martyrs' Day", (f"{year}-06-03" for year in range(1963, 2050))
        )

    def test_national_heroes_day(self):
        name = "National Heroes' Day"
        self.assertHolidayName(name, (f"{year}-06-09" for year in range(2001, 2050)))
        self.assertNoHolidayName(name, range(1963, 2001))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-10-09" for year in range(1963, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1963, 2050)))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(1963, 2050)))

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
        self.assertHolidayName(name, self.no_estimated_holidays, range(1963, 2050))

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
        self.assertHolidayName(name, self.no_estimated_holidays, range(1963, 2050))

    def test_2020(self):
        self.assertHolidays(
            Uganda(years=2020),
            ("2020-06-09", "National Heroes' Day"),
            ("2020-05-01", "Labour Day"),
            ("2020-06-03", "Uganda Martyrs' Day"),
            ("2020-03-08", "Women's Day"),
            ("2020-12-26", "Boxing Day"),
            ("2020-07-31", "Eid al-Adha (estimated)"),
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-05-24", "Eid al-Fitr (estimated)"),
            ("2020-04-13", "Easter Monday"),
            ("2020-10-09", "Independence Day"),
            ("2020-02-16", "Archbishop Janani Luwum Day"),
            ("2020-01-26", "NRM Liberation Day"),
            ("2020-12-25", "Christmas Day"),
        )
