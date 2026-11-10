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

from holidays.calendars.luxembourg_school import LUXEMBOURG_SCHOOL_HOLIDAYS
from holidays.constants import BANK, PUBLIC, SCHOOL
from holidays.countries.luxembourg import Luxembourg
from tests.common import CommonCountryTests


class TestLuxembourg(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Luxembourg)

    def test_new_years_day(self):
        self.assertHolidayName("Neijoerschdag", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Karfreideg"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertBankHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Ouschterméindeg"
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
        self.assertHolidayName(
            "Dag vun der Aarbecht", (f"{year}-05-01" for year in self.full_range)
        )

    def test_europe_day(self):
        name = "Europadag"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2019))

    def test_ascension_day(self):
        name = "Christi Himmelfaart"
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
        name = "Péngschtméindeg"
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

    def test_national_day(self):
        self.assertHolidayName("Nationalfeierdag", (f"{year}-06-23" for year in self.full_range))

    def test_assumption_day(self):
        self.assertHolidayName("Léiffrawëschdag", (f"{year}-08-15" for year in self.full_range))

    def test_all_saints_day(self):
        self.assertHolidayName("Allerhellgen", (f"{year}-11-01" for year in self.full_range))

    def test_christmas_eve(self):
        name = "Hellegowend (nomëtteg)"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Chrëschtdag", (f"{year}-12-25" for year in self.full_range))

    def test_saint_stephens_day(self):
        self.assertHolidayName("Stiefesdag", (f"{year}-12-26" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Silvester"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_all_school_holiday_ids_are_mapped(self):
        known_ids = set(Luxembourg._get_school_holiday_names())
        dataset_ids = {
            holiday_id
            for year_holidays in LUXEMBOURG_SCHOOL_HOLIDAYS.values()
            for *_, holiday_id in year_holidays
        }
        self.assertEqual(dataset_ids, known_ids)

    def test_no_school_holidays(self):
        # School holidays are available from the 1980/81 school year.
        self.assertNoHolidays(
            Luxembourg(
                categories=SCHOOL,
                years=(*range(self.start_year, 1980), *range(2030, self.end_year)),
            )
        )
        self.assertNoSchoolHoliday("1980-10-25", "1980-11-03")

    def test_all_saints_break(self):
        name = "Allerhellegevakanz"
        self.assertSchoolHolidayName(
            name,
            "1980-10-26",
            "1980-11-02",
            "1999-10-31",
            "1999-11-07",
            "2025-11-01",
            "2025-11-09",
            "2028-10-28",
            "2028-11-05",
        )
        self.assertNoSchoolHoliday("1999-10-30", "1999-11-08", "2025-10-31", "2025-11-10")

    def test_christmas_break(self):
        name = "Chrëschtvakanz"
        self.assertSchoolHolidayName(
            name,
            "1980-12-21",
            "1981-01-04",
            "2017-12-16",
            "2018-01-01",
            "2025-12-20",
            "2026-01-04",
            "2028-12-16",
            "2028-12-31",
        )
        self.assertNoSchoolHoliday(
            "1980-12-20", "1981-01-05", "2018-01-02", "2028-12-15", "2029-01-01"
        )

    def test_carnival_break(self):
        name = "Fuesvakanz"
        self.assertSchoolHolidayName(
            name,
            "1981-03-01",
            "1981-03-08",
            "2000-02-26",
            "2000-03-06",
            "2028-02-12",
            "2028-02-20",
        )
        self.assertNoSchoolHoliday("2000-02-25", "2000-03-07", "2028-02-11", "2028-02-21")

    def test_easter_break(self):
        name = "Ouschtervakanz"
        self.assertSchoolHolidayName(
            name,
            "1981-04-12",
            "1981-04-26",
            "2026-03-28",
            "2026-04-12",
            "2029-03-31",
            "2029-04-15",
        )
        self.assertNoSchoolHoliday("2026-03-27", "2026-04-13")

    def test_pentecost_break(self):
        name = "Päischtvakanz"
        self.assertSchoolHolidayName(
            name,
            "1981-06-07",
            "1981-06-14",
            "2009-05-23",
            "2009-06-02",
            "2027-05-29",
            "2027-06-06",
        )
        self.assertNoSchoolHoliday("2009-05-22", "2009-06-03", "2027-05-28", "2027-06-07")

    def test_summer_break(self):
        name = "Summervakanz"
        self.assertSchoolHolidayName(
            name,
            "1981-07-16",
            "1981-09-14",
            "2026-07-16",
            "2026-09-14",
            "2029-07-14",
            "2029-09-16",
        )
        self.assertNoSchoolHoliday("2026-07-15", "2026-09-15", "2029-07-13", "2029-09-17")

    def test_school_holidays_run_across_new_year(self):
        # The Christmas Break belongs to both years it touches.
        self.assertHolidayName(
            "Chrëschtvakanz",
            Luxembourg(categories=SCHOOL, years=(2025, 2026)),
            "2025-12-31",
            "2026-01-01",
        )

    def test_2018(self):
        self.assertHolidaysInYear(
            2018,
            ("2018-01-01", "Neijoerschdag"),
            ("2018-04-02", "Ouschterméindeg"),
            ("2018-05-01", "Dag vun der Aarbecht"),
            ("2018-05-10", "Christi Himmelfaart"),
            ("2018-05-21", "Péngschtméindeg"),
            ("2018-06-23", "Nationalfeierdag"),
            ("2018-08-15", "Léiffrawëschdag"),
            ("2018-11-01", "Allerhellgen"),
            ("2018-12-25", "Chrëschtdag"),
            ("2018-12-26", "Stiefesdag"),
        )

    def test_2018_bank(self):
        self.assertBankHolidaysInYear(
            2018,
            ("2018-03-30", "Karfreideg"),
            ("2018-12-24", "Hellegowend (nomëtteg)"),
            ("2018-12-31", "Silvester"),
        )

    def test_2019(self):
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "Neijoerschdag"),
            ("2019-04-22", "Ouschterméindeg"),
            ("2019-05-01", "Dag vun der Aarbecht"),
            ("2019-05-09", "Europadag"),
            ("2019-05-30", "Christi Himmelfaart"),
            ("2019-06-10", "Péngschtméindeg"),
            ("2019-06-23", "Nationalfeierdag"),
            ("2019-08-15", "Léiffrawëschdag"),
            ("2019-11-01", "Allerhellgen"),
            ("2019-12-25", "Chrëschtdag"),
            ("2019-12-26", "Stiefesdag"),
        )

    def test_2019_bank(self):
        self.assertBankHolidaysInYear(
            2019,
            ("2019-04-19", "Karfreideg"),
            ("2019-12-24", "Hellegowend (nomëtteg)"),
            ("2019-12-31", "Silvester"),
        )

    def test_2020(self):
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "Neijoerschdag"),
            ("2020-04-13", "Ouschterméindeg"),
            ("2020-05-01", "Dag vun der Aarbecht"),
            ("2020-05-09", "Europadag"),
            ("2020-05-21", "Christi Himmelfaart"),
            ("2020-06-01", "Péngschtméindeg"),
            ("2020-06-23", "Nationalfeierdag"),
            ("2020-08-15", "Léiffrawëschdag"),
            ("2020-11-01", "Allerhellgen"),
            ("2020-12-25", "Chrëschtdag"),
            ("2020-12-26", "Stiefesdag"),
        )

    def test_2020_bank(self):
        self.assertBankHolidaysInYear(
            2020,
            ("2020-04-10", "Karfreideg"),
            ("2020-12-24", "Hellegowend (nomëtteg)"),
            ("2020-12-31", "Silvester"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neijoerschdag"),
            ("2022-04-15", "Karfreideg"),
            ("2022-04-18", "Ouschterméindeg"),
            ("2022-05-01", "Dag vun der Aarbecht"),
            ("2022-05-09", "Europadag"),
            ("2022-05-26", "Christi Himmelfaart"),
            ("2022-06-06", "Péngschtméindeg"),
            ("2022-06-23", "Nationalfeierdag"),
            ("2022-08-15", "Léiffrawëschdag"),
            ("2022-11-01", "Allerhellgen"),
            ("2022-12-24", "Hellegowend (nomëtteg)"),
            ("2022-12-25", "Chrëschtdag"),
            ("2022-12-26", "Stiefesdag"),
            ("2022-12-31", "Silvester"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_de(self):
        self.assertLocalizedHolidays(
            "de",
            ("2022-01-01", "Neujahr"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Tag der Arbeit"),
            ("2022-05-09", "Europatag"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-23", "Nationalfeiertag"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-12-24", "Heiligabend (Nachmittag)"),
            ("2022-12-25", "Weihnachten"),
            ("2022-12-26", "Zweiter Weihnachtsfeiertag"),
            ("2022-12-31", "Silvester"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-09", "Europe Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Pentecost Monday"),
            ("2022-06-23", "National Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-24", "Christmas Eve (afternoon)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
            ("2022-12-31", "New Year's Eve"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Jour de l'An"),
            ("2022-04-15", "Vendredi Saint"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-09", "Jour de l'Europe"),
            ("2022-05-26", "Ascension"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-06-23", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-11-01", "Toussaint"),
            ("2022-12-24", "Veille de Noël (après-midi)"),
            ("2022-12-25", "Noël"),
            ("2022-12-26", "Saint-Étienne"),
            ("2022-12-31", "Saint-Sylvestre"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-09", "День Європи"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "Другий день Пʼятидесятниці"),
            ("2022-06-23", "Національне свято"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-24", "Святий вечір (друга половина дня)"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День Святого Стефана"),
            ("2022-12-31", "Переддень Нового року"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_default_school(self):
        default_holidays = Luxembourg(years=2026, categories=SCHOOL)
        for dt, name in (
            ("2026-01-02", "Chrëschtvakanz"),
            ("2026-02-16", "Fuesvakanz"),
            ("2026-04-06", "Ouschtervakanz"),
            ("2026-05-25", "Päischtvakanz"),
            ("2026-08-01", "Summervakanz"),
            ("2026-11-02", "Allerhellegevakanz"),
        ):
            self.assertHolidayName(name, default_holidays, dt)

    def test_l10n_de_school(self):
        de_holidays = Luxembourg(years=2026, language="de", categories=SCHOOL)
        for dt, name in (
            ("2026-01-02", "Weihnachtsferien"),
            ("2026-02-16", "Karnevalsferien"),
            ("2026-04-06", "Osterferien"),
            ("2026-05-25", "Pfingstferien"),
            ("2026-08-01", "Sommerferien"),
            ("2026-11-02", "Allerheiligenferien"),
        ):
            self.assertHolidayName(name, de_holidays, dt)

    def test_l10n_en_us_school(self):
        en_us_holidays = Luxembourg(years=2026, language="en_US", categories=SCHOOL)
        for dt, name in (
            ("2026-01-02", "Christmas Break"),
            ("2026-02-16", "Carnival Break"),
            ("2026-04-06", "Easter Break"),
            ("2026-05-25", "Pentecost Break"),
            ("2026-08-01", "Summer Break"),
            ("2026-11-02", "All Saints' Break"),
        ):
            self.assertHolidayName(name, en_us_holidays, dt)

    def test_l10n_fr_school(self):
        fr_holidays = Luxembourg(years=2026, language="fr", categories=SCHOOL)
        for dt, name in (
            ("2026-01-02", "Vacances de Noël"),
            ("2026-02-16", "Congé de Carnaval"),
            ("2026-04-06", "Vacances de Pâques"),
            ("2026-05-25", "Congé de la Pentecôte"),
            ("2026-08-01", "Vacances d'été"),
            ("2026-11-02", "Congé de la Toussaint"),
        ):
            self.assertHolidayName(name, fr_holidays, dt)

    def test_l10n_uk_school(self):
        uk_holidays = Luxembourg(years=2026, language="uk", categories=SCHOOL)
        for dt, name in (
            ("2026-01-02", "Різдвяні канікули"),
            ("2026-02-16", "Карнавальні канікули"),
            ("2026-04-06", "Великодні канікули"),
            ("2026-05-25", "Канікули на Пʼятидесятницю"),
            ("2026-08-01", "Літні канікули"),
            ("2026-11-02", "Канікули на День усіх святих"),
        ):
            self.assertHolidayName(name, uk_holidays, dt)
