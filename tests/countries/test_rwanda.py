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

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           prateekshit.jaiswal (c) 2024
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.rwanda import Rwanda, RW, RWA
from tests.common import CommonCountryTests


class TestRwanda(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Rwanda, years=range(2018, 2050), years_non_observed=range(2018, 2050))

    def test_country_aliases(self):
        self.assertAliases(Rwanda, RW, RWA)

    def test_no_holidays(self):
        self.assertNoHolidays(Rwanda(years=2017))

    def test_new_years_day(self):
        name = "Ubunani"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2018, 2050)))
        dt = ("2022-01-03",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_day_after_new_years_day(self):
        name = "Umunsi ukurikira Ubunani"
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(2018, 2050)))
        dt = ("2022-01-04",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_heroes_day(self):
        self.assertHolidayName("Umunsi w'Intwari", (f"{year}-02-01" for year in range(2018, 2050)))

    def test_genocide_memorial_day(self):
        self.assertHolidayName(
            "Umunsi wo Kwibuka Jenoside yakorewe Abatutsi",
            (f"{year}-04-07" for year in range(2018, 2050)),
        )

    def test_good_friday(self):
        name = "Umunsi wa Gatanu Mutagatifu"
        self.assertHolidayName(
            name,
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2018, 2050))

    def test_easter_monday(self):
        name = "Ku wa mbere wa Pasika"
        self.assertHolidayName(
            name,
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(2018, 2050))

    def test_labor_day(self):
        self.assertHolidayName(
            "Umunsi Mukuru w'Umurimo", (f"{year}-05-01" for year in range(2018, 2050))
        )

    def test_eid_al_fitr(self):
        name = "EID EL FITR"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-05",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertHolidayName(
            name, Rwanda(years=range(2018, 2050), islamic_show_estimated=False), range(2018, 2050)
        )

    def test_eid_al_adha(self):
        name = "EID AL-ADHA"
        self.assertHolidayName(
            name,
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-06",
        )
        self.assertHolidayName(
            name, Rwanda(years=range(2018, 2050), islamic_show_estimated=False), range(2018, 2050)
        )

    def test_independence_day(self):
        self.assertHolidayName(
            "Umunsi w'Ubwigenge", (f"{year}-07-01" for year in range(2018, 2050))
        )

    def test_liberation_day(self):
        self.assertHolidayName(
            "Umunsi wo Kwibohora", (f"{year}-07-04" for year in range(2018, 2050))
        )

    def test_umuganura_day(self):
        self.assertHolidayName(
            "Umunsi w'Umuganura", (f"{year}-08-06" for year in range(2018, 2050))
        )

    def test_assumption_day(self):
        self.assertHolidayName(
            "Ijyanwa mu Ijuru rya Bikiramariya", (f"{year}-08-15" for year in range(2018, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Noheli", (f"{year}-12-25" for year in range(2018, 2050)))

    def test_boxing_day(self):
        self.assertHolidayName(
            "Umunsi ukurikira Noheli", (f"{year}-12-26" for year in range(2018, 2050))
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Ubunani"),
            ("2024-01-02", "Umunsi ukurikira Ubunani"),
            ("2024-02-01", "Umunsi w'Intwari"),
            ("2024-03-29", "Umunsi wa Gatanu Mutagatifu"),
            ("2024-04-01", "Ku wa mbere wa Pasika"),
            ("2024-04-07", "Umunsi wo Kwibuka Jenoside yakorewe Abatutsi"),
            ("2024-04-10", "EID EL FITR"),
            ("2024-05-01", "Umunsi Mukuru w'Umurimo"),
            ("2024-06-17", "EID AL-ADHA"),
            ("2024-07-01", "Umunsi w'Ubwigenge"),
            ("2024-07-04", "Umunsi wo Kwibohora"),
            ("2024-08-06", "Umunsi w'Umuganura"),
            ("2024-08-15", "Ijyanwa mu Ijuru rya Bikiramariya"),
            ("2024-12-25", "Noheli"),
            ("2024-12-26", "Umunsi ukurikira Noheli"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "Day after New Year's Day"),
            ("2024-02-01", "National Heroes' Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-07", "Genocide perpetrated against the Tutsi Memorial Day"),
            ("2024-04-10", "EID EL FITR"),
            ("2024-05-01", "Labor Day"),
            ("2024-06-17", "EID AL-ADHA"),
            ("2024-07-01", "Independence Day"),
            ("2024-07-04", "Liberation Day"),
            ("2024-08-06", "Umuganura Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2024-01-01", "Nouvel An"),
            ("2024-01-02", "Le lendemain du Nouvel An"),
            ("2024-02-01", "Journée Nationale des Héros"),
            ("2024-03-29", "Vendredi Saint"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-04-07", "Journée commémorative du Génocide perpétré contre les Tutsi"),
            ("2024-04-10", "EID EL FITR"),
            ("2024-05-01", "Journée du Travail"),
            ("2024-06-17", "EID AL-ADHA"),
            ("2024-07-01", "Journée de l’Indépendance"),
            ("2024-07-04", "Journée de la Libération"),
            ("2024-08-06", "Journée d’Umuganura"),
            ("2024-08-15", "Assomption"),
            ("2024-12-25", "Noël"),
            ("2024-12-26", "Le lendemain de Noël"),
        )
