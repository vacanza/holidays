#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.saint_lucia import SaintLucia, LC, LCA
from tests.common import CommonCountryTests


class TestSaintLucia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaintLucia, years=range(1979, 2025))

    def test_country_aliases(self):
        self.assertAliases(SaintLucia, LC, LCA)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-02-22" for year in range(1979, 2025)))

    def test_new_years(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1979, 2025)))

    def test_first_monday_of_august_holiday(self):
        self.assertHolidayName("Emancipation Day", (f"{year}-08-01" for year in range(1979, 2025)))

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(1979, 2025)))

    def test_good_friday(self):
        name = "Good Friday"
        dts = (
            "1999-04-02",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1979, 2025))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1979, 2025)))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(1979, 2025)))

    def test_corpus_christi(self):
        name = "Corpus Christi"
        dt = (
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1979, 2025))

    def test_easter_monday(self):
        name = "Easter Monday"
        dts = (
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
        )
        self.assertHolidayName(name, dts)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day Two"),
            ("2023-02-22", "Independence Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-10-02", "Thanksgiving Day"),
            ("2023-12-13", "National Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2023-01-01", "Jour de l'An"),
            ("2023-01-02", "Deuxième jour de l'An"),
            ("2023-02-22", "Jour de l'indépendance"),
            ("2023-04-07", "Vendredi saint"),
            ("2023-04-10", "Lundi de Pâques"),
            ("2023-05-01", "Fête du Travail"),
            ("2023-05-29", "Lundi de Pentecôte"),
            ("2023-06-08", "Fête-Dieu"),
            ("2023-08-01", "Jour de l'émancipation"),
            ("2023-10-02", "Thanksgiving Day"),
            ("2023-12-13", "Fête nationale"),
            ("2023-12-25", "Jour de Noël"),
            ("2023-12-26", "lendemain de Noël"),
        )

    def test_l10n_es(self):
        self.assertLocalizedHolidays(
            "es",
            ("2023-01-01", "Día de Año Nuevo"),
            ("2023-01-02", "Segundo día de Año Nuevo"),
            ("2023-02-22", "Día de la Independencia"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-04-10", "Lunes de Pascua"),
            ("2023-05-01", "Día del Trabajo"),
            ("2023-05-29", "Lundi de Pentecôte"),
            ("2023-06-08", "Fête-Dieu"),
            ("2023-08-01", "Día de la Emancipación"),
            ("2023-10-02", "Thanksgiving Day"),
            ("2023-12-13", "Fiesta Nacional"),
            ("2023-12-25", "Día de Navidad"),
            ("2023-12-26", "lendemain de Noël"),
        )

    def test_l10n_fr_lc(self):
        self.assertLocalizedHolidays(
            "fr_LC",
            ("2023-01-01", "Premye Janvye"),
            ("2023-01-02", "Dezyèm Janvye"),
            ("2023-02-22", "Jou Endepandans"),
            ("2023-04-07", "Vandredi Sen"),
            ("2023-04-10", "Lendi Pak"),
            ("2023-05-01", "Jou Travay"),
            ("2023-05-29", "Lendi Pantekòt"),
            ("2023-06-08", "Fèt-Dié"),
            ("2023-08-01", "Jou Liberasyon"),
            ("2023-10-02", "Thanksgiving Day"),
            ("2023-12-13", "Jou Nasyonal"),
            ("2023-12-25", "Nwèl"),
            ("2023-12-26", "Landemèn Nwèl"),
        )
