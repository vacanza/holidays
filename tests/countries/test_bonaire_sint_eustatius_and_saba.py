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

from holidays.countries.bonaire_sint_eustatius_and_saba import BonaireSintEustatiusAndSaba
from tests.common import CommonCountryTests


class TestBonaireSintEustatiusAndSaba(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BonaireSintEustatiusAndSaba)

    def test_new_years_day(self):
        self.assertHolidayName("Nieuwjaarsdag", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Goede Vrijdag"
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

    def test_easter_sunday(self):
        name = "Eerste Paasdag"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Tweede Paasdag"
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

    def test_kings_day(self):
        name_queen = "Koninginnedag"
        name_king = "Koningsdag"
        self.assertHolidayName(
            name_queen, (f"{year}-04-30" for year in range(self.start_year, 2014))
        )
        self.assertNoHolidayName(name_queen, range(2014, self.end_year))
        self.assertHolidayName(
            name_king,
            "2014-04-26",
            "2015-04-27",
            "2020-04-27",
            "2021-04-27",
            "2022-04-27",
            "2023-04-27",
            "2024-04-27",
            "2025-04-26",
        )
        self.assertNoHoliday(
            "2014-04-27",
            "2025-04-27",
        )
        self.assertHolidayName(name_king, range(2014, self.end_year))
        self.assertNoHolidayName(name_king, range(self.start_year, 2014))

    def test_labor_day(self):
        self.assertHolidayName("Dag van de Arbeid", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        name = "Hemelvaartsdag"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_sunday(self):
        name = "Eerste Pinksterdag"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        self.assertHolidayName("Eerste Kerstdag", (f"{year}-12-25" for year in self.full_range))

    def test_boxing_day(self):
        self.assertHolidayName("Tweede Kerstdag", (f"{year}-12-26" for year in self.full_range))

    def test_rincon_day(self):
        name = "Rincondag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BON":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-30" for year in range(2020, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2020))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bonaire_day(self):
        name = "Bonairedag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BON":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-06" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_carnival_monday(self):
        name = "Dag na de carnavalsoptocht"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SAB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-07-27",
                    "2021-07-26",
                    "2022-07-25",
                    "2023-07-31",
                    "2024-07-29",
                    "2025-07-28",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saba_day(self):
        name = "Sabadag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SAB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-12-04",
                    "2021-12-03",
                    "2022-12-02",
                    "2023-12-01",
                    "2024-12-06",
                    "2025-12-05",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_emancipation_day(self):
        name = "Emancipatiedag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "STA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-01" for year in range(2022, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_statia_day(self):
        name = "Statiadag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "STA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_special_holiday(self):
        name = "Brugdag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BON":
                self.assertHolidayName(name, holidays, "2025-05-02")
            else:
                self.assertNoHolidayName(name, holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Nieuwjaarsdag"),
            ("2023-04-07", "Goede Vrijdag"),
            ("2023-04-09", "Eerste Paasdag"),
            ("2023-04-10", "Tweede Paasdag"),
            ("2023-04-27", "Koningsdag"),
            ("2023-04-30", "Rincondag"),
            ("2023-05-01", "Dag van de Arbeid"),
            ("2023-05-18", "Hemelvaartsdag"),
            ("2023-05-28", "Eerste Pinksterdag"),
            ("2023-07-01", "Emancipatiedag"),
            ("2023-07-31", "Dag na de carnavalsoptocht"),
            ("2023-09-06", "Bonairedag"),
            ("2023-11-16", "Statiadag"),
            ("2023-12-01", "Sabadag"),
            ("2023-12-25", "Eerste Kerstdag"),
            ("2023-12-26", "Tweede Kerstdag"),
        )

    def test_l10n_en_bq(self):
        self.assertLocalizedHolidays(
            "en_BQ",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Day"),
            ("2023-04-30", "Rincon Day"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-05-28", "Whit Sunday"),
            ("2023-07-01", "Emancipation Day"),
            ("2023-07-31", "Carnival Monday"),
            ("2023-09-06", "Bonaire Day"),
            ("2023-11-16", "Statia Day"),
            ("2023-12-01", "Saba Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Second Day of Christmas"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Day"),
            ("2023-04-30", "Rincon Day"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-05-28", "Whit Sunday"),
            ("2023-07-01", "Emancipation Day"),
            ("2023-07-31", "Carnival Monday"),
            ("2023-09-06", "Bonaire Day"),
            ("2023-11-16", "Statia Day"),
            ("2023-12-01", "Saba Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Second Day of Christmas"),
        )

    def test_l10n_pap_bq(self):
        self.assertLocalizedHolidays(
            "pap_BQ",
            ("2023-01-01", "Aña nobo"),
            ("2023-04-07", "Bièrnèsantu"),
            ("2023-04-09", "Pasku di Resurekshon"),
            ("2023-04-10", "Di dos dia di Pasku di Resurekshon"),
            ("2023-04-27", "Dia di Rei"),
            ("2023-04-30", "Dia di Rincon"),
            ("2023-05-01", "Dia di labor"),
            ("2023-05-18", "Asenshon"),
            ("2023-05-28", "Dia di Pentekòste"),
            ("2023-07-01", "Dia di Emansipashon"),
            ("2023-07-31", "Djaluna di Carnaval"),
            ("2023-09-06", "Dia di Boneiru"),
            ("2023-11-16", "Dia di Statia"),
            ("2023-12-01", "Dia di Saba"),
            ("2023-12-25", "Pasku"),
            ("2023-12-26", "Di dos dia di Pasku"),
        )
