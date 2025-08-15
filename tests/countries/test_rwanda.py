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

from holidays.countries.rwanda import Rwanda, RW, RWA
from tests.common import CommonCountryTests


class TestRwanda(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2012, 2050)
        super().setUpClass(Rwanda, years=years, years_non_observed=years)
        cls.no_estimated_holidays = Rwanda(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Rwanda, RW, RWA)

    def test_no_holidays(self):
        self.assertNoHolidays(Rwanda(years=2011))

    def test_new_years_day(self):
        name = "Ubunani"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2012, 2050)))
        dt = (
            "2022-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (yizihijwe)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_day_after_new_years_day(self):
        name = "Umunsi ukurikira Ubunani"
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(2016, 2050)))
        self.assertNoHolidayName(name, range(2012, 2016))
        dt = (
            "2021-01-04",
            "2022-01-04",
        )
        self.assertHolidayName(f"{name} (yizihijwe)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_heroes_day(self):
        name = "Umunsi w'Intwari"
        self.assertHolidayName(name, (f"{year}-02-01" for year in range(2012, 2050)))
        dt = (
            "2020-02-03",
            "2025-02-03",
        )
        self.assertHolidayName(f"{name} (yizihijwe)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_genocide_memorial_day(self):
        self.assertHolidayName(
            "Umunsi wo Kwibuka Jenoside yakorewe Abatutsi",
            (f"{year}-04-07" for year in range(2012, 2050)),
        )

    def test_good_friday(self):
        name = "Umunsi wa Gatanu Mutagatifu"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2012, 2050))

    def test_easter_monday(self):
        name = "Ku wa mbere wa Pasika"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(2017, 2050))
        self.assertNoHolidayName(name, range(2012, 2017))

    def test_labor_day(self):
        name = "Umunsi Mukuru w'Umurimo"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2012, 2050)))
        dt = (
            "2021-05-03",
            "2022-05-03",
        )
        self.assertHolidayName(f"{name} (yizihijwe)", dt)

    def test_eid_al_fitr(self):
        name = "Eid El Fitr"
        dt = (
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(f"{name} (yagereranijwe)", dt)
        self.assertHolidayName(
            name, Rwanda(years=range(2012, 2050), islamic_show_estimated=False), range(2012, 2050)
        )

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        dt = (
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(f"{name} (yagereranijwe)", dt)
        self.assertHolidayName(
            name, Rwanda(years=range(2015, 2050), islamic_show_estimated=False), range(2015, 2050)
        )
        self.assertNoHolidayName(name, range(2012, 2015))

    def test_independence_day(self):
        name = "Umunsi w'Ubwigenge"
        self.assertHolidayName(name, (f"{year}-07-01" for year in range(2012, 2050)))
        dt = ("2023-07-03",)
        self.assertHolidayName(f"{name} (yizihijwe)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_liberation_day(self):
        name = "Umunsi wo Kwibohora"
        self.assertHolidayName(name, (f"{year}-07-04" for year in range(2012, 2050)))
        dt = (
            "2020-07-06",
            "2021-07-05",
        )
        self.assertHolidayName(f"{name} (yizihijwe)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_umuganura_day(self):
        name = "Umunsi w'Umuganura"
        self.assertHolidayName(
            name,
            "2020-08-07",
            "2021-08-06",
            "2022-08-05",
            "2023-08-04",
            "2024-08-02",
            "2025-08-01",
        )
        self.assertHolidayName(name, range(2015, 2050))
        self.assertNoHolidayName(name, range(2012, 2015))

    def test_assumption_day(self):
        name = "Ijyanwa mu Ijuru rya Bikiramariya"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(2012, 2050)))
        dt = (
            "2020-08-17",
            "2021-08-16",
        )
        self.assertHolidayName(f"{name} (yizihijwe)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Noheli"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2012, 2050)))
        dt = (
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (yizihijwe)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        name = "Umunsi ukurikira Noheli"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2012, 2050)))
        dt = (
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (yizihijwe)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Ubunani"),
            ("2024-01-02", "Umunsi ukurikira Ubunani"),
            ("2024-02-01", "Umunsi w'Intwari"),
            ("2024-03-29", "Umunsi wa Gatanu Mutagatifu"),
            ("2024-04-01", "Ku wa mbere wa Pasika"),
            ("2024-04-07", "Umunsi wo Kwibuka Jenoside yakorewe Abatutsi"),
            ("2024-04-10", "Eid El Fitr (yagereranijwe)"),
            ("2024-05-01", "Umunsi Mukuru w'Umurimo"),
            ("2024-06-16", "Eid al-Adha (yagereranijwe)"),
            ("2024-06-17", "Eid al-Adha (yizihijwe, yagereranijwe)"),
            ("2024-07-01", "Umunsi w'Ubwigenge"),
            ("2024-07-04", "Umunsi wo Kwibohora"),
            ("2024-08-02", "Umunsi w'Umuganura"),
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
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-05-01", "Labour Day"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-06-17", "Eid al-Adha (observed, estimated)"),
            ("2024-07-01", "Independence Day"),
            ("2024-07-04", "Liberation Day"),
            ("2024-08-02", "Umuganura Day"),
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
            ("2024-04-10", "Aïd el-Fitr (estimé)"),
            ("2024-05-01", "Journée du Travail"),
            ("2024-06-16", "Aïd al-Adha (estimé)"),
            ("2024-06-17", "Aïd al-Adha (observé, estimé)"),
            ("2024-07-01", "Journée de l'Indépendance"),
            ("2024-07-04", "Journée de la Libération"),
            ("2024-08-02", "Journée d'Umuganura"),
            ("2024-08-15", "Assomption"),
            ("2024-12-25", "Noël"),
            ("2024-12-26", "Le lendemain de Noël"),
        )
