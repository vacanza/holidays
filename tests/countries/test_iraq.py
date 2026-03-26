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

from holidays.countries.iraq import Iraq
from tests.common import CommonCountryTests


class TestIraq(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Iraq)

    def test_new_years_day(self):
        name = "رأس السنة الميلادية"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1973, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1973))
        self.assertChristianHolidayName(
            name, (f"{year}-01-01" for year in range(self.start_year, 1973))
        )
        self.assertNoChristianHolidayName(name, range(1973, self.end_year))

    def test_army_day(self):
        self.assertHolidayName(
            "عيد الجيش", (f"{year}-01-06" for year in range(1973, self.end_year))
        )

    def test_february_8_revolution_day(self):
        name = "ثورة 8 شباط"
        self.assertHolidayName(name, (f"{year}-02-08" for year in range(self.start_year, 2025)))
        self.assertNoHolidayName(name, range(2025, self.end_year))

    def test_commemoration_of_saddam_baath_crimes_against_iraqi_people(self):
        name = "ذكرى جرائم البعث والأنفال والهجوم على حلبجة"
        self.assertHolidayName(name, (f"{year}-03-16" for year in range(2025, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2025))

    def test_nowruz(self):
        name = "عيد نوروز"
        self.assertHolidayName(name, (f"{year}-03-21" for year in range(1969, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1969))

    def test_labor_day(self):
        self.assertHolidayName(
            "عيد العمال العالمي", (f"{year}-05-01" for year in range(1973, self.end_year))
        )

    def test_july_14_revolution_day(self):
        name = "ثورة 14 تموز"
        self.assertHolidayName(name, (f"{year}-07-14" for year in range(self.start_year, 2024)))
        self.assertNoHolidayName(name, range(2024, self.end_year))

    def test_july_17_revolution_day(self):
        name = "ثورة 17 تموز"
        self.assertHolidayName(name, (f"{year}-07-17" for year in range(1969, 2024)))
        self.assertNoHolidayName(name, range(self.start_year, 1969), range(2024, self.end_year))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_ashura(self):
        name = "عاشوراء"
        self.assertHolidayName(
            name,
            "2021-08-19",
            "2022-08-08",
            "2023-07-29",
            "2024-07-16",
            "2025-07-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "المولد النبوي الشريف"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertHolidayName(
            name,
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_day_of_arafah(self):
        name = "يوم عرفة"
        self.assertHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_ghadir(self):
        name = "عيد الغدير"
        self.assertHolidayName(
            name,
            "2024-06-24",
            "2025-06-15",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(2024, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 2024))

    def test_easter_sunday(self):
        name = "أحد الفصح"
        self.assertNoHolidayName(name)
        self.assertChristianHolidayName(
            name,
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertChristianHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "إثنين الفصح"
        self.assertNoHolidayName(name)
        self.assertChristianHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertChristianHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "عيد الميلاد"
        self.assertNoHolidayName(name)
        self.assertChristianHolidayName(name, (f"{year}-12-25" for year in self.full_range))

    def test_pesach(self):
        name = "عيد الفصح"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "2021-03-28",
            "2021-03-29",
            "2022-04-16",
            "2022-04-17",
            "2023-04-06",
            "2023-04-07",
        )
        self.assertHebrewHolidayName(name, range(self.start_year, 2024))
        self.assertNoHebrewHolidayName(name, range(2024, self.end_year))

    def test_yom_kippur(self):
        name = "يوم الكفارة"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "2021-09-16",
            "2022-10-05",
            "2023-09-25",
        )
        self.assertHebrewHolidayName(name, range(self.start_year, 2024))
        self.assertNoHebrewHolidayName(name, range(2024, self.end_year))

    def test_sukkot(self):
        name = "عيد المظلة"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "2021-09-21",
            "2021-09-22",
            "2022-10-10",
            "2022-10-11",
            "2023-09-30",
            "2023-10-01",
        )
        self.assertHebrewHolidayName(name, range(self.start_year, 2024))
        self.assertNoHebrewHolidayName(name, range(2024, self.end_year))

    def test_great_feast(self):
        name = "يوما عيد البنجة"
        self.assertNoHolidayName(name)
        self.assertSabianHolidayName(
            name,
            "2023-07-22",
            "2023-07-23",
            "2024-07-21",
            "2024-07-22",
            "2024-07-23",
            "2024-07-24",
        )
        self.assertSabianHolidayNameCount(name, 2, range(1973, 2024))
        self.assertSabianHolidayNameCount(name, 4, range(2024, self.end_year))
        self.assertNoSabianHolidayName(name, range(self.start_year, 1973))

    def test_parwanaya(self):
        name = "عيد الخليقة"
        self.assertNoHolidayName(name)
        self.assertSabianHolidayName(
            name,
            "2023-03-14",
            "2023-03-15",
            "2024-03-13",
            "2024-03-14",
            "2024-03-15",
            "2024-03-16",
            "2024-03-17",
        )
        self.assertSabianHolidayNameCount(name, 2, range(1973, 2024))
        self.assertSabianHolidayNameCount(name, 5, range(2024, self.end_year))
        self.assertNoSabianHolidayName(name, range(self.start_year, 1973))
        self.assertNoSabianHolidayName(
            name,
            "2023-03-16",
            "2023-03-17",
            "2023-03-18",
        )

    def test_little_feast(self):
        name = "عيد الصغير"
        self.assertNoHolidayName(name)
        self.assertSabianHolidayName(
            name,
            "2023-04-10",
            "2024-04-09",
            "2024-04-10",
            "2025-04-09",
            "2025-04-10",
        )
        self.assertSabianHolidayNameCount(name, 1, range(1973, 2024))
        self.assertSabianHolidayNameCount(name, 2, range(2024, self.end_year))
        self.assertNoSabianHolidayName(name, range(self.start_year, 1973))

    def test_prophet_yahyas_birthday(self):
        name = "مولد النبي يحيى عليه السلام"
        self.assertNoHolidayName(name)
        self.assertSabianHolidayName(
            name,
            "2021-05-18",
            "2022-05-18",
            "2023-05-18",
            "2024-05-17",
            "2025-05-17",
        )
        self.assertSabianHolidayName(name, range(1973, self.end_year))
        self.assertNoSabianHolidayName(name, range(self.start_year, 1973))

    def test_yazidi_new_year(self):
        name = "رأس السنة الإيزيدية"
        self.assertNoHolidayName(name)
        self.assertYazidiHolidayName(
            name,
            "2021-04-14",
            "2022-04-20",
            "2023-04-19",
            "2024-04-17",
            "2025-04-16",
        )
        self.assertYazidiHolidayName(name, self.full_range)

    def test_yazidi_summer_festival(self):
        name = "مهرجان الصيف اليزيدي"
        self.assertNoHolidayName(name)
        self.assertYazidiHolidayName(
            name,
            (f"{year}-07-31" for year in range(self.start_year, 2024)),
            (f"{year}-08-01" for year in range(self.start_year, 2024)),
            (f"{year}-08-02" for year in self.full_range),
            (f"{year}-08-03" for year in self.full_range),
        )

    def test_feast_of_the_assembly(self):
        name = "عيد الجمعية"
        self.assertNoHolidayName(name)
        self.assertYazidiHolidayName(
            name,
            (f"{year}-10-06" for year in self.full_range),
            (f"{year}-10-07" for year in self.full_range),
            (f"{year}-10-08" for year in self.full_range),
            (f"{year}-10-09" for year in self.full_range),
            (f"{year}-10-10" for year in self.full_range),
            (f"{year}-10-11" for year in self.full_range),
            (f"{year}-10-12" for year in self.full_range),
            (f"{year}-10-13" for year in self.full_range),
        )

    def test_feast_of_ezi(self):
        name = "عيد إيزي"
        self.assertNoHolidayName(name)
        self.assertYazidiHolidayName(
            name,
            "2021-12-17",
            "2022-12-16",
            "2023-12-15",
            "2024-12-20",
            "2025-12-19",
        )
        self.assertYazidiHolidayName(name, self.full_range)

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-01-06", "عيد الجيش"),
            ("2024-02-08", "ثورة 8 شباط"),
            ("2024-03-21", "عيد نوروز"),
            ("2024-04-10", "عيد الفطر"),
            ("2024-04-11", "عيد الفطر"),
            ("2024-04-12", "عيد الفطر"),
            ("2024-05-01", "عيد العمال العالمي"),
            ("2024-06-15", "يوم عرفة"),
            ("2024-06-16", "عيد الأضحى"),
            ("2024-06-17", "عيد الأضحى"),
            ("2024-06-18", "عيد الأضحى"),
            ("2024-06-24", "عيد الغدير"),
            ("2024-07-07", "رأس السنة الهجرية"),
            ("2024-07-16", "عاشوراء"),
            ("2024-09-15", "المولد النبوي الشريف"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "رأس السنة الميلادية"),
            ("2025-01-06", "عيد الجيش"),
            ("2025-03-13", "عيد الخليقة"),
            ("2025-03-14", "عيد الخليقة"),
            ("2025-03-15", "عيد الخليقة"),
            ("2025-03-16", "ذكرى جرائم البعث والأنفال والهجوم على حلبجة; عيد الخليقة"),
            ("2025-03-17", "عيد الخليقة"),
            ("2025-03-21", "عيد نوروز"),
            ("2025-03-31", "عيد الفطر"),
            ("2025-04-01", "عيد الفطر"),
            ("2025-04-02", "عيد الفطر"),
            ("2025-04-09", "عيد الصغير"),
            ("2025-04-10", "عيد الصغير"),
            ("2025-04-16", "رأس السنة الإيزيدية"),
            ("2025-04-20", "أحد الفصح"),
            ("2025-04-21", "إثنين الفصح"),
            ("2025-05-01", "عيد العمال العالمي"),
            ("2025-05-17", "مولد النبي يحيى عليه السلام"),
            ("2025-06-05", "يوم عرفة"),
            ("2025-06-06", "عيد الأضحى"),
            ("2025-06-07", "عيد الأضحى"),
            ("2025-06-08", "عيد الأضحى"),
            ("2025-06-15", "عيد الغدير"),
            ("2025-06-26", "رأس السنة الهجرية"),
            ("2025-07-05", "عاشوراء"),
            ("2025-07-21", "يوما عيد البنجة"),
            ("2025-07-22", "يوما عيد البنجة"),
            ("2025-07-23", "يوما عيد البنجة"),
            ("2025-07-24", "يوما عيد البنجة"),
            ("2025-08-02", "مهرجان الصيف اليزيدي"),
            ("2025-08-03", "مهرجان الصيف اليزيدي"),
            ("2025-09-04", "المولد النبوي الشريف"),
            ("2025-10-06", "عيد الجمعية"),
            ("2025-10-07", "عيد الجمعية"),
            ("2025-10-08", "عيد الجمعية"),
            ("2025-10-09", "عيد الجمعية"),
            ("2025-10-10", "عيد الجمعية"),
            ("2025-10-11", "عيد الجمعية"),
            ("2025-10-12", "عيد الجمعية"),
            ("2025-10-13", "عيد الجمعية"),
            ("2025-12-19", "عيد إيزي"),
            ("2025-12-25", "عيد الميلاد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-06", "Army Day"),
            ("2025-03-13", "Feast of Creation"),
            ("2025-03-14", "Feast of Creation"),
            ("2025-03-15", "Feast of Creation"),
            (
                "2025-03-16",
                "Commemoration of the Saddam Baath crimes against the Iraqi people"
                "; Feast of Creation",
            ),
            ("2025-03-17", "Feast of Creation"),
            ("2025-03-21", "Nowruz"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-01", "Eid al-Fitr"),
            ("2025-04-02", "Eid al-Fitr"),
            ("2025-04-09", "Little Feast"),
            ("2025-04-10", "Little Feast"),
            ("2025-04-16", "Yazidi New Year"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-17", "Prophet Yahya's Birthday"),
            ("2025-06-05", "Day of Arafah"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-08", "Eid al-Adha"),
            ("2025-06-15", "Eid al-Ghadir"),
            ("2025-06-26", "Islamic New Year"),
            ("2025-07-05", "Ashura"),
            ("2025-07-21", "Great Feast"),
            ("2025-07-22", "Great Feast"),
            ("2025-07-23", "Great Feast"),
            ("2025-07-24", "Great Feast"),
            ("2025-08-02", "Yazidi Summer Festival"),
            ("2025-08-03", "Yazidi Summer Festival"),
            ("2025-09-04", "Prophet's Birthday"),
            ("2025-10-06", "Feast of the Assembly"),
            ("2025-10-07", "Feast of the Assembly"),
            ("2025-10-08", "Feast of the Assembly"),
            ("2025-10-09", "Feast of the Assembly"),
            ("2025-10-10", "Feast of the Assembly"),
            ("2025-10-11", "Feast of the Assembly"),
            ("2025-10-12", "Feast of the Assembly"),
            ("2025-10-13", "Feast of the Assembly"),
            ("2025-12-19", "Feast of Êzî"),
            ("2025-12-25", "Christmas Day"),
        )
