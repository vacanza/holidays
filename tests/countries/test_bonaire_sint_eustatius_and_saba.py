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

    def test_country_aliases(self):
        self.assertAliases(BonaireSintEustatiusAndSaba, BQ, BES)

    def test_new_years(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2011, 2050)))

    def test_good_friday(self):
        name = "Good Friday"
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
        name = "Easter Sunday"
        dt = ("2020-04-12", "2021-04-04", "2022-04-17", "2023-04-09", "2024-03-31", "2025-04-20")
        self.assertHolidayName(name, dt)

    def test_easter_monday(self):
        name = "Easter Monday"
        dt = ("2020-04-13", "2021-04-05", "2022-04-18", "2023-04-10", "2024-04-01", "2025-04-21")
        self.assertHolidayName(name, dt)

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(name, (f"{year}-04-27" for year in range(2011, 2050)))

    def test_labor_day(self):
        name = "Labor Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2011, 2050)))

    def test_ascension_day(self):
        name = "Ascension Day"
        dt = ("2020-05-21", "2021-05-13", "2022-05-26", "2023-05-18", "2024-05-09", "2025-05-29")
        self.assertHolidayName(name, dt)

    def test_whit_sunday(self):
        name = "Whit Sunday"
        dt = ("2020-05-31", "2021-05-23", "2022-06-05", "2023-05-28", "2024-05-19", "2025-06-08")
        self.assertHolidayName(name, dt)

    def test_carnival_monday(self):
        name = "Carnival Monday"
        dt = (
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, dt)

    def test_saba_day(self):
        name = "Saba Day"
        self.assertHolidayName(name, (f"{year}-12-05" for year in range(2011, 2050)))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2011, 2050)))

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2011, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-02-20", "Carnival Monday"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Birthday"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-05-28", "Whit Sunday"),
            ("2023-12-05", "Saba Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-02-20", "Carnival Monday"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Birthday"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-05-28", "Whit Sunday"),
            ("2023-12-05", "Saba Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_l10n_nl(self):
        self.assertLocalizedHolidays(
            "nl",
            ("2023-01-01", "Nieuwjaar"),
            ("2023-02-20", "Carnavalsmaandag"),
            ("2023-04-07", "Goede Vrijdag"),
            ("2023-04-09", "Pasen"),
            ("2023-04-10", "Paasmaandag"),
            ("2023-04-27", "Koningsdag"),
            ("2023-05-01", "Dag van de Arbeid"),
            ("2023-05-18", "Hemelvaart"),
            ("2023-05-28", "Pinksteren"),
            ("2023-12-05", "Saba Dag"),
            ("2023-12-25", "Kerstmis"),
            ("2023-12-26", "Tweede Kerstdag"),
        )
