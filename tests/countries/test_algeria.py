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

from holidays.countries.algeria import Algeria, DZ, DZA
from tests.common import CommonCountryTests


class TestAlgeria(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Algeria)

    def test_country_aliases(self):
        self.assertAliases(Algeria, DZ, DZA)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Algeria(categories=Algeria.supported_categories, years=self.start_year - 1)
        )

    def test_new_years_day(self):
        self.assertHolidayName(
            "رأس السنة الميلادية", (f"{year}-01-01" for year in self.full_range)
        )

    def test_amazigh_new_year(self):
        name = "رأس السنة الأمازيغية"
        self.assertHolidayName(name, (f"{year}-01-12" for year in range(2018, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2018))

    def test_labor_day(self):
        self.assertHolidayName("عيد العمال", (f"{year}-05-01" for year in self.full_range))

    def test_independence_day(self):
        name_1964 = "عيد الاستقلال وجبهة التحرير الوطني"
        name_2005 = "عيد الاستقلال"
        self.assertHolidayName(
            name_1964, (f"{year}-07-05" for year in range(self.start_year, 2005))
        )
        self.assertHolidayName(name_2005, (f"{year}-07-05" for year in range(2005, self.end_year)))
        self.assertNoHolidayName(name_1964, range(2005, self.end_year))
        self.assertNoHolidayName(name_2005, range(self.start_year, 2005))

    def test_revolution_day(self):
        self.assertHolidayName("عيد الثورة", (f"{year}-11-01" for year in self.full_range))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_ashura(self):
        name = "عاشورة"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-29",
            "2021-08-18",
            "2022-08-08",
            "2023-07-28",
            "2024-07-16",
            "2025-07-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "عيد المولد النبوي"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2020-05-25",
            "2021-05-13",
            "2021-05-14",
            "2022-05-02",
            "2022-05-03",
            "2023-04-21",
            "2023-04-22",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 2, range(1964, 1968), range(1969, 2000), range(2001, 2024)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, range(2024, 2033), range(2034, self.end_year)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, 1968, 2000)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, 2033)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2020-08-01",
            "2021-07-20",
            "2021-07-21",
            "2022-07-09",
            "2022-07-10",
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
        self.assertIslamicNoEstimatedHolidayNameCount(name, 1, range(1964, 1969))
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 2, range(1969, 1974), range(1975, 2006), range(2008, 2023)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, range(2006, 2008), range(2023, 2039), range(2040, self.end_year)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, 1974)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, 2039)

    def test_easter_monday(self):
        name = "إثنين الفصح"
        self.assertNoHolidayName(name)
        self.assertChristianHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertChristianHolidayName(name, self.full_range)

    def test_ascension_day(self):
        name = "عيد الصعود"
        self.assertNoHolidayName(name)
        self.assertChristianHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertChristianHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "إثنين العنصرة"
        self.assertNoHolidayName(name)
        self.assertChristianHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertChristianHolidayName(name, self.full_range)

    def test_assumption_day(self):
        name = "عيد انتقال السيدة العذراء"
        self.assertNoHolidayName(name)
        self.assertChristianHolidayName(name, (f"{year}-08-15" for year in self.full_range))

    def test_christmas_day(self):
        name = "عيد الميلاد"
        self.assertNoHolidayName(name)
        self.assertChristianHolidayName(name, (f"{year}-12-25" for year in self.full_range))

    def test_rosh_hashanah(self):
        name = "رأس السنة العبرية"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "2020-09-19",
            "2021-09-07",
            "2022-09-26",
            "2023-09-16",
            "2024-10-03",
            "2025-09-23",
        )
        self.assertHebrewHolidayName(name, self.full_range)

    def test_yom_kippur(self):
        name = "يوم الغفران"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "2020-09-28",
            "2021-09-16",
            "2022-10-05",
            "2023-09-25",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertHebrewHolidayName(name, self.full_range)

    def test_pesach(self):
        name = "عيد الفصح اليهودي"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "2020-04-09",
            "2021-03-28",
            "2022-04-16",
            "2023-04-06",
            "2024-04-23",
            "2025-04-13",
        )
        self.assertHebrewHolidayName(name, self.full_range)

    def test_weekend(self):
        for dt in (
            "1975-01-04",  # SAT.
            "1975-01-05",  # SUN.
            "1976-01-01",  # THU.
            "1976-01-02",  # FRI.
            "2008-01-03",  # THU.
            "2008-01-04",  # FRI.
            "2009-01-02",  # FRI.
            "2009-01-03",  # SAT.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "1975-01-02",  # THU.
            "1975-01-03",  # FRI.
            "1976-01-03",  # SAT.
            "1976-01-04",  # SUN.
            "2008-01-05",  # SAT.
            "2008-01-06",  # SUN.
            "2009-01-01",  # THU.
            "2009-01-04",  # SUN.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-01-12", "رأس السنة الأمازيغية"),
            ("2022-04-16", "عيد الفصح اليهودي"),
            ("2022-04-18", "إثنين الفصح"),
            ("2022-05-01", "عيد العمال"),
            ("2022-05-02", "عيد الفطر (المقدرة)"),
            ("2022-05-03", "عيد الفطر (المقدرة)"),
            ("2022-05-26", "عيد الصعود"),
            ("2022-06-06", "إثنين العنصرة"),
            ("2022-07-05", "عيد الاستقلال"),
            ("2022-07-09", "عيد الأضحى (المقدرة)"),
            ("2022-07-10", "عيد الأضحى (المقدرة)"),
            ("2022-07-30", "رأس السنة الهجرية (المقدرة)"),
            ("2022-08-08", "عاشورة (المقدرة)"),
            ("2022-08-15", "عيد انتقال السيدة العذراء"),
            ("2022-09-26", "رأس السنة العبرية"),
            ("2022-10-05", "يوم الغفران"),
            ("2022-10-08", "عيد المولد النبوي (المقدرة)"),
            ("2022-11-01", "عيد الثورة"),
            ("2022-12-25", "عيد الميلاد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-12", "Amazigh New Year"),
            ("2022-04-16", "Pesach"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-03", "Eid al-Fitr (estimated)"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-07-05", "Independence Day"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-07-10", "Eid al-Adha (estimated)"),
            ("2022-07-30", "Islamic New Year (estimated)"),
            ("2022-08-08", "Ashura (estimated)"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-26", "Rosh Hashanah"),
            ("2022-10-05", "Yom Kippur"),
            ("2022-10-08", "Prophet's Birthday (estimated)"),
            ("2022-11-01", "Revolution Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Jour de l'An Grégorien"),
            ("2022-01-12", "Jour de l'An Amazigh"),
            ("2022-04-16", "Pisah"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-02", "Aïd el-Fitr (estimé)"),
            ("2022-05-03", "Aïd el-Fitr (estimé)"),
            ("2022-05-26", "Ascension"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-05", "Fête de l'Indépendance"),
            ("2022-07-09", "Aïd el-Adha (estimé)"),
            ("2022-07-10", "Aïd el-Adha (estimé)"),
            ("2022-07-30", "Awal Moharram (estimé)"),
            ("2022-08-08", "Achoura (estimé)"),
            ("2022-08-15", "Assomption"),
            ("2022-09-26", "Roch Achana"),
            ("2022-10-05", "Youm Kippour"),
            ("2022-10-08", "El-Mawlid Ennabawi Echarif (estimé)"),
            ("2022-11-01", "Fête de la Révolution"),
            ("2022-12-25", "Noël"),
        )
