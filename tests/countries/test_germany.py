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

import warnings
from unittest import TestCase

from holidays.calendars.germany_school import GERMANY_SCHOOL_HOLIDAYS
from holidays.constants import CATHOLIC, PUBLIC, SCHOOL
from holidays.countries.germany import Germany
from tests.common import CommonCountryTests


class TestGermany(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_deprecated(self):
        self.assertEqual(
            sorted(Germany(subdiv="BYP", years=2023).keys()),
            sorted(Germany(subdiv="BY", years=2023).keys()),
        )

    def test_no_holidays(self):
        super().test_no_holidays()

        for subdiv in Germany.subdivisions:
            self.assertNoHolidays(Germany(years=self.start_year - 1, subdiv=subdiv))
            self.assertNoHolidays(
                Germany(subdiv=subdiv, years=self.start_year - 1, categories=SCHOOL)
            )
            if subdiv in {"BY", "SN", "TH"}:
                self.assertNoHolidays(
                    Germany(subdiv=subdiv, years=self.start_year - 1, categories=CATHOLIC)
                )
        self.assertNoHolidays(Germany(years=2025, categories=SCHOOL))

    def test_special_holidays(self):
        # 2017's Reformation Day is tested in test_reformation_day.
        be_dts = (
            "2020-05-08",
            "2025-05-08",
            "2028-06-17",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            # Berlin.
            if subdiv == "BE":
                self.assertHoliday(holidays, be_dts)
            else:
                self.assertNoHoliday(holidays, be_dts)

    def test_new_years_day(self):
        self.assertHolidayName("Neujahr", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany(self):
        name = "Heilige Drei Könige"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Bayern, Sachsen, Thüringen, Augsburg.
            if subdiv in {"BW", "BY", "ST", "Augsburg"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-06" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_womens_day(self):
        name = "Frauentag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            match subdiv:
                # Berlin - 2019.
                case "BE":
                    self.assertHolidayName(
                        name, holidays, (f"{year}-03-08" for year in range(2019, self.end_year))
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2019))
                # Mecklenburg-Vorpommern - 2023.
                case "MV":
                    self.assertHolidayName(
                        name, holidays, (f"{year}-03-08" for year in range(2023, self.end_year))
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2023))
                case _:
                    self.assertNoHolidayName(name, holidays)

    def test_good_friday(self):
        name = "Karfreitag"
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
        name = "Ostersonntag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Brandenburg.
            if subdiv == "BB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-04-12",
                    "2021-04-04",
                    "2022-04-17",
                    "2023-04-09",
                    "2024-03-31",
                    "2025-04-20",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_easter_monday(self):
        name = "Ostermontag"
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

    def test_ascension_day(self):
        name = "Christi Himmelfahrt"
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

    def test_labor_day(self):
        self.assertHolidayName("Erster Mai", (f"{year}-05-01" for year in self.full_range))

    def test_whit_sunday(self):
        name = "Pfingstsonntag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Brandenburg.
            if subdiv == "BB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-05-31",
                    "2021-05-23",
                    "2022-06-05",
                    "2023-05-28",
                    "2024-05-19",
                    "2025-06-08",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_whit_monday(self):
        name = "Pfingstmontag"
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

    def test_corpus_christi(self):
        name = "Fronleichnam"
        self.assertNoHolidayName(name)
        dts = (
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            # Baden-Württemberg, Bayern, Hessen, Nordrhein-Westfalen,
            # Rheinland-Pfalz, Saarland, Augsburg.
            if subdiv in {"BW", "BY", "HE", "NW", "RP", "SL", "Augsburg"}:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

        # Sachsen, Thüringen.
        self.assertSubdivSnCatholicHolidayName(name, dts)
        self.assertSubdivSnCatholicHolidayName(name, self.full_range)
        self.assertSubdivThCatholicHolidayName(name, dts)
        self.assertSubdivThCatholicHolidayName(name, self.full_range)

    def test_augsburg_peace_festival(self):
        name = "Augsburger Hohes Friedensfest"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Augsburg.
            if subdiv == "Augsburg":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-08" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_assumption_day(self):
        name = "Mariä Himmelfahrt"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Saarland.
            if subdiv in {"SL", "Augsburg"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

        # Bayern.
        self.assertSubdivByCatholicHolidayName(name, (f"{year}-08-15" for year in self.full_range))

    def test_world_childrens_day(self):
        name = "Weltkindertag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Thüringen.
            if subdiv == "TH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-20" for year in range(2019, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2019))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_german_unity_day(self):
        self.assertHolidayName(
            "Tag der Deutschen Einheit", (f"{year}-10-03" for year in self.full_range)
        )

    def test_reformation_day(self):
        name = "Reformationstag"
        for subdiv, holidays in self.subdiv_holidays.items():
            match subdiv:
                # Brandenburg, Mecklenburg-Vorpommern, Sachsen, Sachsen-Anhalt, Thüringen.
                case "BB" | "MV" | "SN" | "ST" | "TH":
                    self.assertHolidayName(
                        name, holidays, (f"{year}-10-31" for year in self.full_range)
                    )
                # Bremen, Hamburg, Niedersachsen, Schleswig-Holstein.
                case "HB" | "HH" | "NI" | "SH":
                    # While these subdivisions started their holiday observance in 2018,
                    # this is de facto implemented in 2017's nationwide special observance.
                    self.assertHolidayName(
                        name, holidays, (f"{year}-10-31" for year in range(2017, self.end_year))
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2017))
                case _:
                    self.assertHolidayName(name, holidays, "2017-10-31")
                    self.assertNoHolidayName(
                        name, holidays, range(self.start_year, 2017), range(2018, self.end_year)
                    )
        self.assertHolidayName(name, "2017-10-31")

    def test_all_saints_day(self):
        name = "Allerheiligen"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Baden-Württemberg, Bayern, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Augsburg.
            if subdiv in {"BW", "BY", "NW", "RP", "SL", "Augsburg"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_repentance_and_prayer_day(self):
        name = "Buß- und Bettag"
        dts_pre_1995 = (
            "1991-11-20",
            "1992-11-18",
            "1993-11-17",
            "1994-11-16",
        )
        dts = (
            "2020-11-18",
            "2021-11-17",
            "2022-11-16",
            "2023-11-22",
            "2024-11-20",
            "2025-11-19",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            # Sachsen.
            if subdiv == "SN":
                self.assertHolidayName(name, holidays, dts, dts_pre_1995)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertHolidayName(name, holidays, dts_pre_1995)
                self.assertNoHolidayName(name, holidays, range(1995, self.end_year))
        self.assertHolidayName(name, dts_pre_1995)
        self.assertNoHolidayName(name, range(1995, self.end_year))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Erster Weihnachtstag", (f"{year}-12-25" for year in self.full_range)
        )

    def test_second_day_of_christmas(self):
        self.assertHolidayName(
            "Zweiter Weihnachtstag", (f"{year}-12-26" for year in self.full_range)
        )

    def test_all_states_present_for_all_dataset_years(self):
        expected_subdivs = set(Germany.subdivisions) - {"Augsburg"}
        for year, year_data in GERMANY_SCHOOL_HOLIDAYS.items():
            self.assertEqual(set(year_data), expected_subdivs, year)

    def test_all_school_holiday_ids_are_mapped(self):
        known_ids = set(Germany._get_school_holiday_names())
        dataset_ids = {
            holiday_id
            for year_data in GERMANY_SCHOOL_HOLIDAYS.values()
            for holidays in year_data.values()
            for *_, holiday_id in holidays
        }
        self.assertEqual(dataset_ids, known_ids)

    def test_school_holidays(self):
        self.assertSubdivBeSchoolHolidayName(
            "Himmelfahrts-/Pfingstferien",
            "2004-05-21",
        )
        self.assertSubdivBeSchoolHolidayName(
            "Sommerferien",
            "2012-06-20",
            "2013-06-19",
            "2014-07-09",
            "2016-07-20",
        )
        self.assertSubdivBeSchoolHolidayName(
            "Herbstferien",
            "2025-10-20",
            "2025-11-01",
        )
        self.assertSubdivBwSchoolHolidayName(
            "Winterferien",
            "1991-02-11",
            "1991-02-16",
        )
        self.assertSubdivBwSchoolHolidayName(
            "Sommerferien",
            "1991-07-11",
            "1991-08-24",
        )
        self.assertSubdivBwSchoolHolidayName("Herbstferien", "2022-11-04")
        self.assertSubdivBwSchoolHolidayName(
            "Himmelfahrts-/Pfingstferien",
            "2025-06-10",
            "2025-06-20",
        )
        self.assertSubdivBySchoolHolidayName(
            "Sommerferien",
            "2025-08-01",
            "2025-08-31",
        )
        self.assertSubdivBySchoolHolidayName(
            "Weihnachtsferien",
            "2026-01-02",
            "2026-12-24",
        )
        self.assertSubdivHbSchoolHolidayName(
            "Winterferien",
            "2009-02-02",
            "2009-02-03",
        )
        self.assertSubdivHhSchoolHolidayName(
            "Weihnachtsferien",
            "2004-01-30",
            "2004-12-22",
        )
        self.assertSubdivNiSchoolHolidayName(
            "Winterferien",
            "2001-01-29",
            "2001-01-30",
        )
        self.assertSubdivNwSchoolHolidayName(
            "Sommerferien",
            "2026-07-20",
            "2026-09-01",
        )
        self.assertSubdivShSchoolHolidayName(
            "Sommerferien",
            "2026-07-04",
            "2026-08-15",
        )
        self.assertSubdivSlSchoolHolidayName(
            "Himmelfahrts-/Pfingstferien",
            "2004-05-21",
            "2004-06-11",
        )
        self.assertSubdivSnSchoolHolidayName(
            "Winterferien",
            "2026-02-09",
            "2026-02-21",
        )
        self.assertSubdivStSchoolHolidayName(
            "Herbstferien",
            "2004-10-18",
            "2004-10-23",
        )
        self.assertSubdivStSchoolHolidayName(
            "Winterferien",
            "2006-02-01",
            "2006-02-10",
        )
        self.assertSubdivThSchoolHolidayName(
            "Sommerferien",
            "2001-06-28",
            "2001-08-08",
        )

    def test_school_holidays_subdivision_aliases(self):
        self.assertHolidayName(
            "Sommerferien",
            Germany(subdiv="Bayern", years=2025, categories=SCHOOL),
            "2025-08-01",
            "2025-08-31",
        )

        self.assertHolidayName(
            "Sommerferien",
            Germany(subdiv="Augsburg", years=2025, categories=SCHOOL),
            "2025-08-01",
            "2025-08-31",
        )

        self.assertHolidayName(
            "Sommerferien",
            Germany(subdiv="BYP", years=2025, categories=SCHOOL),
            "2025-08-01",
            "2025-08-31",
        )

    def test_school_and_public_categories(self):
        self.assertHolidayName(
            "Frauentag",
            Germany(subdiv="BE", years=2025, categories=(PUBLIC, SCHOOL)),
            "2025-03-08",
        )
        self.assertHolidayName(
            "Herbstferien",
            Germany(subdiv="BE", years=2025, categories=(PUBLIC, SCHOOL)),
            "2025-10-20",
        )
        self.assertHolidayName(
            "Neujahr",
            Germany(subdiv="Bayern", years=2025, categories=(PUBLIC, SCHOOL)),
            "2025-01-01",
        )
        self.assertHolidayName(
            "Sommerferien",
            Germany(subdiv="Bayern", years=2025, categories=(PUBLIC, SCHOOL)),
            "2025-08-01",
        )

    def test_public_category_excludes_school_holidays(self):
        self.assertHolidayName(
            "Neujahr",
            Germany(subdiv="BY", years=2025, categories=PUBLIC),
            "2025-01-01",
        )
        self.assertNoHolidayName(
            "Sommerferien",
            Germany(subdiv="BY", years=2025, categories=PUBLIC),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-03-08", "Frauentag"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-17", "Ostersonntag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Erster Mai"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-05", "Pfingstsonntag"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-16", "Fronleichnam"),
            ("2022-08-08", "Augsburger Hohes Friedensfest"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-09-20", "Weltkindertag"),
            ("2022-10-03", "Tag der Deutschen Einheit"),
            ("2022-10-31", "Reformationstag"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-16", "Buß- und Bettag"),
            ("2022-12-25", "Erster Weihnachtstag"),
            ("2022-12-26", "Zweiter Weihnachtstag"),
            categories=(CATHOLIC, PUBLIC),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-03-08", "Women's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-08", "Augsburg Peace Festival"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-20", "World Children's Day"),
            ("2022-10-03", "German Unity Day"),
            ("2022-10-31", "Reformation Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-16", "Repentance and Prayer Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            categories=(CATHOLIC, PUBLIC),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-03-08", "วันสตรี"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-06-16", "วันสมโภชพระคริสตวรกาย"),
            ("2022-08-08", "วันเทศกาลสันติภาพเอาก์สบวร์ก"),
            ("2022-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2022-09-20", "วันเด็กสากล"),
            ("2022-10-03", "วันรวมชาติเยอรมัน"),
            ("2022-10-31", "วันแห่งการปฏิรูป"),
            ("2022-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-16", "วันแห่งการอธิษฐานและการกลับใจ"),
            ("2022-12-25", "วันคริสต์มาสวันแรก"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
            categories=(CATHOLIC, PUBLIC),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-03-08", "Жіночий день"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-08", "Аугсбурзьке свято миру"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-09-20", "Всесвітній день дітей"),
            ("2022-10-03", "День німецької єдності"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-16", "День молитви та покаяння"),
            ("2022-12-25", "Перший день Різдва"),
            ("2022-12-26", "Другий день Різдва"),
            categories=(CATHOLIC, PUBLIC),
        )

    def test_l10n_default_school(self):
        default_holidays = Germany(subdiv="BB", years=2025, categories=SCHOOL)
        for dt, name in (
            ("2025-02-03", "Winterferien"),
            ("2025-04-14", "Oster-/Frühjahrsferien"),
            ("2025-06-10", "Himmelfahrts-/Pfingstferien"),
            ("2025-07-24", "Sommerferien"),
            ("2025-10-20", "Herbstferien"),
            ("2025-12-22", "Weihnachtsferien"),
        ):
            self.assertHolidayName(name, default_holidays, dt)

    def test_l10n_en_us_school(self):
        en_us_holidays = Germany(subdiv="BB", years=2025, language="en_US", categories=SCHOOL)
        for dt, name in (
            ("2025-02-03", "Winter Break"),
            ("2025-04-14", "Easter/Spring Break"),
            ("2025-06-10", "Ascension/Whit Break"),
            ("2025-07-24", "Summer Break"),
            ("2025-10-20", "Autumn Break"),
            ("2025-12-22", "Christmas Break"),
        ):
            self.assertHolidayName(name, en_us_holidays, dt)

    def test_l10n_th_school(self):
        th_holidays = Germany(subdiv="BB", years=2025, language="th", categories=SCHOOL)
        for dt, name in (
            ("2025-02-03", "ปิดเทอมฤดูหนาว"),
            ("2025-04-14", "ปิดเทอมอีสเตอร์/ฤดูใบไม้ผลิ"),
            ("2025-06-10", "ปิดเทอมวันสมโภชพระเยซูเจ้าเสด็จสู่สวรรค์/เพ็นเทคอสต์"),
            ("2025-07-24", "ปิดเทอมฤดูร้อน"),
            ("2025-10-20", "ปิดเทอมฤดูใบไม้ร่วง"),
            ("2025-12-22", "ปิดเทอมคริสต์มาส"),
        ):
            self.assertHolidayName(name, th_holidays, dt)

    def test_l10n_uk_school(self):
        uk_holidays = Germany(subdiv="BB", years=2025, language="uk", categories=SCHOOL)
        for dt, name in (
            ("2025-02-03", "Зимові канікули"),
            ("2025-04-14", "Великодні/весняні канікули"),
            ("2025-06-10", "Канікули на Вознесіння/Трійцю"),
            ("2025-07-24", "Літні канікули"),
            ("2025-10-20", "Осінні канікули"),
            ("2025-12-22", "Різдвяні канікули"),
        ):
            self.assertHolidayName(name, uk_holidays, dt)
