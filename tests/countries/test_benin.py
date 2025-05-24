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

from holidays.countries.benin import Benin, BJ, BEN
from tests.common import CommonCountryTests


class TestBenin(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1960, 2050)
        super().setUpClass(Benin, years=years, years_non_observed=years)
        cls.no_estimated_holidays = Benin(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Benin, BJ, BEN)

    def test_no_holidays(self):
        self.assertNoHolidays(Benin(years=1959))

    def test_new_years_day(self):
        name = "Jour de l'An"
        self.assertHolidayName(
            name,
            "2020-01-01",
            "2021-01-01",
            "2022-01-01",
            "2023-01-01",
            "2024-01-01",
            "2025-01-01",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_vodoun_festival(self):
        name = "Journée Vaudoun"
        self.assertHolidayName(name, (f"{year}-01-10" for year in range(1960, 2050)))
        obs_dt = ("2024-01-09",)
        self.assertHolidayName(f"{name} (observé)", obs_dt)

    def test_easter_monday(self):
        name = "Lundi de Pâques"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_labor_day(self):
        name = "Fête du Travail"
        self.assertHolidayName(
            name,
            "2020-05-01",
            "2021-05-01",
            "2022-05-01",
            "2023-05-01",
            "2024-05-01",
            "2025-05-01",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_ascention_day(self):
        name = "Jour de l'Ascension"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_whit_monday(self):
        name = "Lundi de Pentecôte"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_independence_day(self):
        name = "Jour de l'indépendance"
        self.assertHolidayName(
            name,
            "2020-08-01",
            "2021-08-01",
            "2022-08-01",
            "2023-08-01",
            "2024-08-01",
            "2025-08-01",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_assumption_day(self):
        name = "Jour de l'Assomption"
        self.assertHolidayName(
            name,
            "2020-08-15",
            "2021-08-15",
            "2022-08-15",
            "2023-08-15",
            "2024-08-15",
            "2025-08-15",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_all_saints_day(self):
        name = "La Toussaint"
        self.assertHolidayName(
            name,
            "2020-11-01",
            "2021-11-01",
            "2022-11-01",
            "2023-11-01",
            "2024-11-01",
            "2025-11-01",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_christmas_day(self):
        name = "Jour de Noël"
        self.assertHolidayName(
            name,
            "2020-12-25",
            "2021-12-25",
            "2022-12-25",
            "2023-12-25",
            "2024-12-25",
            "2025-12-25",
        )
        self.assertHolidayName(name, range(1960, 2050))

    def test_prophets_birthday(self):
        name = "Maouloud"
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
        self.assertHolidayName(name, self.no_estimated_holidays, range(1985, 2050))

    def test_eid_al_fitr(self):
        name = "Korité"
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
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))

    def test_eid_al_adha(self):
        name = "Tabaski"
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
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jour de l'An"),
            ("2022-01-10", "Journée Vaudoun"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-02", "Korité (estimé)"),
            ("2022-05-26", "Jour de l'Ascension"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-09", "Tabaski (estimé)"),
            ("2022-08-01", "Jour de l'indépendance"),
            ("2022-08-15", "Jour de l'Assomption"),
            ("2022-10-08", "Maouloud (estimé)"),
            ("2022-11-01", "La Toussaint"),
            ("2022-12-25", "Jour de Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-10", "Vodoun Festival"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-08-01", "Independence Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-08", "Prophet's Birthday (estimated)"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-25", "Christmas Day"),
        )
