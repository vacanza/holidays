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

from holidays.countries.bonaire_sint_eustatius_and_saba import BonaireSintEustatiusAndSaba, BQ, BES
from tests.common import CommonCountryTests


class TestBonaireSintEustatiusAndSaba(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2011, 2050)
        super().setUpClass(BonaireSintEustatiusAndSaba, years=years)
        cls.subdiv_holidays = {
            subdiv: BonaireSintEustatiusAndSaba(subdiv=subdiv, years=years)
            for subdiv in BonaireSintEustatiusAndSaba.subdivisions
        }

    def test_country_aliases(self):
        self.assertAliases(BonaireSintEustatiusAndSaba, BQ, BES)

    def test_new_years(self):
        name = "Nieuwjaar"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2011, 2050)))

    def test_carnival_monday(self):
        name = "Carnavalsmaandag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SAB":
                self.assertHolidayName(name, holidays, range(2011, 2050))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_good_friday(self):
        name = "Goede Vrijdag"
        dt = (
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, dt)

    def test_easter_sunday(self):
        name = "Pasen"
        dt = (
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, dt)

    def test_easter_monday(self):
        name = "Paasmaandag"
        dt = (
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, dt)

    def test_kings_birthday(self):
        name = "Koningsdag"
        self.assertHolidayName(name, (f"{year}-04-27" for year in range(2011, 2050)))

    def test_rincon_day(self):
        name = "Rincon Dag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BON":
                self.assertHolidayName(name, holidays, range(2011, 2050))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_labor_day(self):
        name = "Dag van de Arbeid"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2011, 2050)))

    def test_ascension_day(self):
        name = "Hemelvaart"
        dt = (
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, dt)

    def test_whit_sunday(self):
        name = "Pinksteren"
        dt = (
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, dt)

    def test_emancipation_day(self):
        name = "Dag van de Emancipatie"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BON" or subdiv == "STA":
                self.assertHolidayName(name, holidays, range(2011, 2050))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bonaire_day(self):
        name = "Bonaire Dag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BON":
                self.assertHolidayName(name, holidays, range(2011, 2050))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_statia_day(self):
        name = "Statia Dag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "STA":
                self.assertHolidayName(name, holidays, range(2011, 2050))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saba_day(self):
        name = "Saba Dag"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SAB":
                self.assertHolidayName(name, holidays, range(2011, 2050))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_christmas_day(self):
        name = "Kerstmis"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2011, 2050)))

    def test_boxing_day(self):
        name = "Tweede Kerstdag"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2011, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Nieuwjaar"),
            ("2023-04-07", "Goede Vrijdag"),
            ("2023-04-09", "Pasen"),
            ("2023-04-10", "Paasmaandag"),
            ("2023-04-27", "Koningsdag"),
            ("2023-04-30", "Rincon Dag"),
            ("2023-05-01", "Dag van de Arbeid"),
            ("2023-05-18", "Hemelvaart"),
            ("2023-05-28", "Pinksteren"),
            ("2023-07-01", "Dag van de Emancipatie"),
            ("2023-07-10", "Carnavalsmaandag"),
            ("2023-09-06", "Bonaire Dag"),
            ("2023-11-16", "Statia Dag"),
            ("2023-12-06", "Saba Dag"),
            ("2023-12-25", "Kerstmis"),
            ("2023-12-26", "Tweede Kerstdag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Birthday"),
            ("2023-04-30", "Rincon Day"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-05-28", "Whit Sunday"),
            ("2023-07-01", "Emancipation Day"),
            ("2023-07-10", "Carnavalsmaandag"),
            ("2023-09-06", "Bonaire Day"),
            ("2023-11-16", "Statia Day"),
            ("2023-12-06", "Saba Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_l10n_en_bq(self):
        self.assertLocalizedHolidays(
            "en_BQ",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Birthday"),
            ("2023-04-30", "Rincon Day"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-05-28", "Whit Sunday"),
            ("2023-07-01", "Emancipation Day"),
            ("2023-07-10", "Carnavalsmaandag"),
            ("2023-09-06", "Bonaire Day"),
            ("2023-11-16", "Statia Day"),
            ("2023-12-06", "Saba Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
