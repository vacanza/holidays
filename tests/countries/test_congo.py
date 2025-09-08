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

from holidays.countries.congo import Congo, CG, COG
from tests.common import CommonCountryTests


class TestCongo(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Congo)

    def test_country_aliases(self):
        self.assertAliases(Congo, CG, COG)

    def test_no_holidays(self):
        self.assertNoHolidays(Congo(years=CG.start_year - 1))

    def test_new_years_day(self):
        self.assertHolidayName("Jour de l'An", (f"{year}-01-01" for year in self.full_range))

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
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Fête du Travail", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        name = "Ascension"
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
        self.assertHolidayName(name, self.full_range)

    def test_reconciliation_day(self):
        self.assertHolidayName(
            "Fête de la Réconciliation", (f"{year}-06-10" for year in self.full_range)
        )

    def test_national_day(self):
        self.assertHolidayName("Fête Nationale", (f"{year}-08-15" for year in self.full_range))

    def test_all_saints_day(self):
        self.assertHolidayName("Toussaint", (f"{year}-11-01" for year in self.full_range))

    def test_republic_day(self):
        name = "Jour de la République"
        self.assertHolidayName(name, (f"{year}-11-28" for year in range(2010, 2050)))
        self.assertNoHolidayName(name, range(CG.start_year, 2010))

    def test_christmas_day(self):
        self.assertHolidayName("Noël", (f"{year}-12-25" for year in self.full_range))

    def test_2006(self):
        # http://mokili.free.fr/jours_feries.php
        self.assertHolidays(
            Congo(years=2006),
            ("2006-01-01", "Jour de l'An"),
            ("2006-04-17", "Lundi de Pâques"),
            ("2006-05-01", "Fête du Travail"),
            ("2006-05-25", "Ascension"),
            ("2006-06-05", "Lundi de Pentecôte"),
            ("2006-06-10", "Fête de la Réconciliation"),
            ("2006-08-15", "Fête Nationale"),
            ("2006-11-01", "Toussaint"),
            ("2006-12-25", "Noël"),
        )

    def test_2010(self):
        # http://mokili.free.fr/jours_feries.php
        self.assertHolidays(
            Congo(years=2010),
            ("2010-01-01", "Jour de l'An"),
            ("2010-04-05", "Lundi de Pâques"),
            ("2010-05-01", "Fête du Travail"),
            ("2010-05-13", "Ascension"),
            ("2010-05-24", "Lundi de Pentecôte"),
            ("2010-06-10", "Fête de la Réconciliation"),
            ("2010-08-15", "Fête Nationale"),
            ("2010-11-01", "Toussaint"),
            ("2010-11-28", "Jour de la République"),
            ("2010-12-25", "Noël"),
        )

    def test_2015(self):
        # http://mokili.free.fr/jours_feries.php
        self.assertHolidays(
            Congo(years=2015),
            ("2015-01-01", "Jour de l'An"),
            ("2015-04-06", "Lundi de Pâques"),
            ("2015-05-01", "Fête du Travail"),
            ("2015-05-14", "Ascension"),
            ("2015-05-25", "Lundi de Pentecôte"),
            ("2015-06-10", "Fête de la Réconciliation"),
            ("2015-08-15", "Fête Nationale"),
            ("2015-11-01", "Toussaint"),
            ("2015-11-28", "Jour de la République"),
            ("2015-12-25", "Noël"),
        )

    def test_2016(self):
        # http://mokili.free.fr/jours_feries.php
        self.assertHolidays(
            Congo(years=2016),
            ("2016-01-01", "Jour de l'An"),
            ("2016-03-28", "Lundi de Pâques"),
            ("2016-05-01", "Fête du Travail"),
            ("2016-05-05", "Ascension"),
            ("2016-05-16", "Lundi de Pentecôte"),
            ("2016-06-10", "Fête de la Réconciliation"),
            ("2016-08-15", "Fête Nationale"),
            ("2016-11-01", "Toussaint"),
            ("2016-11-28", "Jour de la République"),
            ("2016-12-25", "Noël"),
        )

    def test_2017(self):
        # http://mokili.free.fr/jours_feries.php
        self.assertHolidays(
            Congo(years=2017),
            ("2017-01-01", "Jour de l'An"),
            ("2017-04-17", "Lundi de Pâques"),
            ("2017-05-01", "Fête du Travail"),
            ("2017-05-25", "Ascension"),
            ("2017-06-05", "Lundi de Pentecôte"),
            ("2017-06-10", "Fête de la Réconciliation"),
            ("2017-08-15", "Fête Nationale"),
            ("2017-11-01", "Toussaint"),
            ("2017-11-28", "Jour de la République"),
            ("2017-12-25", "Noël"),
        )

    def test_l10n_default(self):
        # http://mokili.free.fr/jours_feries.php
        self.assertLocalizedHolidays(
            ("2024-01-01", "Jour de l'An"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-09", "Ascension"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-06-10", "Fête de la Réconciliation"),
            ("2024-08-15", "Fête Nationale"),
            ("2024-11-01", "Toussaint"),
            ("2024-11-28", "Jour de la République"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        # http://mokili.free.fr/jours_feries.php
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-09", "Ascension Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-06-10", "Reconciliation Day"),
            ("2024-08-15", "National Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-28", "Republic Day"),
            ("2024-12-25", "Christmas Day"),
        )
