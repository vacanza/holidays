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

from holidays.countries.saint_helena_ascension_and_tristan_da_cunha import (
    SaintHelenaAscensionAndTristanDaCunha,
    SH,
    SHN,
)
from tests.common import CommonCountryTests


class TestSaintHelenaAscensionAndTristanDaCunha(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaintHelenaAscensionAndTristanDaCunha, with_subdiv_categories=True)

    def test_country_aliases(self):
        self.assertAliases(SaintHelenaAscensionAndTristanDaCunha, SH, SHN)

    def test_no_holidays(self):
        self.assertNoHolidays(
            SaintHelenaAscensionAndTristanDaCunha(
                categories=SaintHelenaAscensionAndTristanDaCunha.supported_categories,
                years=self.start_year - 1,
            )
        )

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
        self.assertGovernmentHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertGovernmentHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoGovernmentNonObservedHoliday(obs_dts)

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
        self.assertHolidayName(name, self.full_range)

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
        self.assertHolidayName(name, self.full_range)

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
        self.assertHolidayName(name, range(self.start_year, 2023))
        self.assertNoHolidayName(name, range(2023, self.end_year))

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(
            name,
            "2023-06-19",
            "2024-11-15",
            "2025-11-14",
        )
        self.assertHolidayName(name, range(2023, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2023))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertGovernmentHolidayName(name, self.full_range)

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"AC", "TA"}:
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-05-21",
                    "2021-05-13",
                    "2022-05-26",
                    "2023-05-18",
                    "2024-05-09",
                    "2025-05-29",
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_helena_day(self):
        name = "Saint Helena Day"
        self.assertNoHolidayName(name)
        obs_dts = (
            "2016-05-20",
            "2017-05-22",
            "2022-05-20",
            "2023-05-22",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "HL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-21" for year in self.full_range)
                )
                self.assertHolidayName(f"{name} (observed)", holidays, obs_dts)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], obs_dts)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_ratting_day(self):
        name = "Ratting Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TA":
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
            else:
                self.assertNoHolidayName(name, holidays)

    def test_anniversary_day(self):
        name = "Anniversary Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-14" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_august_bank_holiday(self):
        name = "August Bank Holiday"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_government_holidays.items():
            if subdiv in {"AC", "HL"}:
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-08-31",
                    "2021-08-30",
                    "2022-08-29",
                    "2023-08-28",
                    "2024-08-26",
                    "2025-08-25",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

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
