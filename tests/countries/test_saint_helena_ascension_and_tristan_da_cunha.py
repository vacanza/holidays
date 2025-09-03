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
from holidays.countries.saint_helena_ascension_and_tristan_da_cunha import (
    SaintHelenaAscensionAndTristanDaCunha,
    SH,
    SHN,
)
from tests.common import CommonCountryTests


class TestSaintHelenaAscensionAndTristanDaCunha(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2015, 2050)
        super().setUpClass(
            SaintHelenaAscensionAndTristanDaCunha, years=years, years_non_observed=years
        )
        cls.government_holidays = SaintHelenaAscensionAndTristanDaCunha(
            categories=GOVERNMENT, years=years
        )
        cls.government_holidays_non_observed = SaintHelenaAscensionAndTristanDaCunha(
            categories=GOVERNMENT, observed=False, years=years
        )
        cls.subdiv_holidays = {
            subdiv: SaintHelenaAscensionAndTristanDaCunha(subdiv=subdiv, years=years)
            for subdiv in SaintHelenaAscensionAndTristanDaCunha.subdivisions
        }
        cls.subdiv_govt_holidays = {
            subdiv: SaintHelenaAscensionAndTristanDaCunha(
                subdiv=subdiv, categories=GOVERNMENT, years=years
            )
            for subdiv in SaintHelenaAscensionAndTristanDaCunha.subdivisions
        }

    def test_country_aliases(self):
        self.assertAliases(SaintHelenaAscensionAndTristanDaCunha, SH, SHN)

    def test_no_holidays(self):
        self.assertNoHolidays(SaintHelenaAscensionAndTristanDaCunha(years=2014))

    def test_special_holidays(self):
        for dt, name in (
            ("2018-02-09", "Final Departure of R.M.S. St Helena"),
            ("2022-06-03", "Queen Elizabeth II's Platinum Jubilee"),
            ("2022-09-19", "Queen Elizabeth II's State Funeral"),
            ("2023-01-24", "The Duke of Edinburgh's Visit"),
            ("2023-05-08", "Coronation of His Majesty King Charles III"),
        ):
            self.assertHolidayName(name, dt)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.government_holidays, (f"{year}-01-01" for year in range(2015, 2050))
        )
        obs_dt = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", self.government_holidays, obs_dt)
        self.assertNoNonObservedHoliday(self.government_holidays_non_observed, obs_dt)

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
        self.assertHolidayName(name, range(2015, 2050))

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
        self.assertHolidayName(name, range(2015, 2050))

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        self.assertHolidayName(
            name,
            "2018-06-18",
            "2019-06-17",
            "2020-06-08",
            "2021-06-14",
            "2022-06-13",
        )
        self.assertHolidayName(name, range(2015, 2023))
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(
            name,
            "2023-06-19",
            "2024-11-15",
            "2025-11-14",
        )
        self.assertHolidayName(name, range(2023, 2050))
        self.assertNoHolidayName(name, range(2015, 2023))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2015, 2050)))
        obs_dt = (
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2015, 2050)))
        obs_dt = (
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.government_holidays,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.government_holidays, range(2015, 2050))

    def test_ascension_day(self):
        name = "Ascension Day"
        holidays_ac = self.subdiv_holidays["AC"]
        dates = (
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, holidays_ac, dates)
        self.assertHolidayName(name, holidays_ac, range(2015, 2050))
        holidays_ta = self.subdiv_holidays["TA"]
        self.assertHolidayName(name, holidays_ta, dates)
        self.assertHolidayName(name, holidays_ta, range(2015, 2050))
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_saint_helena_day(self):
        holidays = self.subdiv_holidays["HL"]
        self.assertHolidayName(
            "Saint Helena Day", holidays, (f"{year}-05-21" for year in range(2015, 2050))
        )
        obs_dt = (
            "2016-05-20",
            "2017-05-22",
            "2022-05-20",
            "2023-05-22",
        )
        self.assertHolidayName("Saint Helena Day (observed)", holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_ratting_day(self):
        name = "Ratting Day"
        holidays = self.subdiv_holidays["TA"]
        self.assertHolidayName(
            name,
            holidays,
            "2015-05-16",
            "2016-04-30",
            "2017-05-26",
            "2018-06-02",
            "2019-05-24",
            "2020-04-25",
            "2021-04-09",
            "2023-06-02",
            "2025-05-30",
        )
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_anniversary_day(self):
        name = "Anniversary Day"
        holidays = self.subdiv_holidays["TA"]
        self.assertHolidayName(name, holidays, (f"{year}-08-14" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_subdivision_government_holidays(self):
        self.assertNoHolidayName("August Bank Holiday", range(2015, 2050))
        for subdiv, holidays in self.subdiv_govt_holidays.items():
            if subdiv in ("AC", "HL"):
                self.assertHolidayName(
                    "August Bank Holiday",
                    holidays,
                    "2020-08-31",
                    "2021-08-30",
                    "2022-08-29",
                    "2023-08-28",
                    "2024-08-26",
                    "2025-08-25",
                )
                self.assertHolidayName("August Bank Holiday", holidays, range(2015, 2050))
            else:
                self.assertNoHolidayName("August Bank Holiday", holidays, range(2015, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-21", "Saint Helena Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-05-30", "Ratting Day"),
            ("2025-06-09", "Whit Monday"),
            ("2025-08-14", "Anniversary Day"),
            ("2025-08-25", "August Bank Holiday"),
            ("2025-11-14", "King's Birthday"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-21", "Saint Helena Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-05-30", "Ratting Day"),
            ("2025-06-09", "Whit Monday"),
            ("2025-08-14", "Anniversary Day"),
            ("2025-08-25", "August Bank Holiday"),
            ("2025-11-14", "King's Birthday"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
