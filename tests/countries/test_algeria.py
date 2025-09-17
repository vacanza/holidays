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

from holidays.constants import CHRISTIAN, HEBREW
from holidays.countries.algeria import Algeria, DZ, DZA
from tests.common import CommonCountryTests


class TestAlgeria(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1964, 2050)
        super().setUpClass(Algeria, years=years)
        cls.christian_holidays = Algeria(categories=CHRISTIAN, years=years)
        cls.hebrew_holidays = Algeria(categories=HEBREW, years=years)
        cls.no_estimated_holidays = Algeria(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Algeria, DZ, DZA)

    def test_no_holidays(self):
        self.assertNoHolidays(Algeria(categories=Algeria.supported_categories, years=1963))

    def test_new_years_day(self):
        self.assertHolidayName(
            "رأس السنة الميلادية", (f"{year}-01-01" for year in range(1964, 2050))
        )

    def test_amazigh_new_year(self):
        name = "رأس السنة الأمازيغية"
        self.assertHolidayName(name, (f"{year}-01-12" for year in range(2018, 2050)))
        self.assertNoHolidayName(name, range(1964, 2018))

    def test_labor_day(self):
        self.assertHolidayName("عيد العمال", (f"{year}-05-01" for year in range(1964, 2050)))

    def test_independence_day(self):
        name_1964 = "عيد الاستقلال وجبهة التحرير الوطني"
        name_2005 = "عيد الاستقلال"
        self.assertHolidayName(name_1964, (f"{year}-07-05" for year in range(1964, 2005)))
        self.assertHolidayName(name_2005, (f"{year}-07-05" for year in range(2005, 2050)))
        self.assertNoHolidayName(name_1964, range(2005, 2050))
        self.assertNoHolidayName(name_2005, range(1964, 2005))

    def test_revolution_day(self):
        self.assertHolidayName("عيد الثورة", (f"{year}-11-01" for year in range(1964, 2050)))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1964, 2050))

    def test_ashura(self):
        name = "عاشورة"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-08-29",
            "2021-08-18",
            "2022-08-08",
            "2023-07-28",
            "2024-07-16",
            "2025-07-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1964, 2050))

    def test_prophets_birthday(self):
        name = "عيد المولد النبوي"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1964, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
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
        self.assertHolidayNameCount(
            name,
            2,
            self.no_estimated_holidays,
            range(1964, 1968),
            range(1969, 2000),
            range(2001, 2024),
        )
        self.assertHolidayNameCount(
            name, 3, self.no_estimated_holidays, range(2024, 2033), range(2034, 2050)
        )
        self.assertHolidayNameCount(name, 4, self.no_estimated_holidays, 1968, 2000)
        self.assertHolidayNameCount(name, 6, self.no_estimated_holidays, 2033)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
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
        self.assertHolidayNameCount(name, 1, self.no_estimated_holidays, range(1964, 1969))
        self.assertHolidayNameCount(
            name,
            2,
            self.no_estimated_holidays,
            range(1969, 1974),
            range(1975, 2006),
            range(2009, 2023),
        )
        self.assertHolidayNameCount(
            name,
            3,
            self.no_estimated_holidays,
            range(2006, 2008),
            range(2023, 2039),
            range(2040, 2050),
        )
        self.assertHolidayNameCount(name, 4, self.no_estimated_holidays, 1974)
        self.assertHolidayNameCount(name, 6, self.no_estimated_holidays, 2039)

    def test_easter_monday(self):
        name = "إثنين الفصح"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.christian_holidays,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.christian_holidays, range(1964, 2050))

    def test_ascension_day(self):
        name = "عيد الصعود"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.christian_holidays,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.christian_holidays, range(1964, 2050))

    def test_whit_monday(self):
        name = "إثنين العنصرة"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.christian_holidays,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.christian_holidays, range(1964, 2050))

    def test_assumption_day(self):
        name = "عيد انتقال السيدة العذراء"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.christian_holidays, (f"{year}-08-15" for year in range(1964, 2050))
        )

    def test_christmas_day(self):
        name = "عيد الميلاد"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.christian_holidays, (f"{year}-12-25" for year in range(1964, 2050))
        )

    def test_rosh_hashanah(self):
        name = "رأس السنة العبرية"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.hebrew_holidays,
            "2020-09-19",
            "2021-09-07",
            "2022-09-26",
            "2023-09-16",
            "2024-10-03",
            "2025-09-23",
        )
        self.assertHolidayName(name, self.hebrew_holidays, range(1964, 2050))

    def test_yom_kippur(self):
        name = "يوم الغفران"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.hebrew_holidays,
            "2020-09-28",
            "2021-09-16",
            "2022-10-05",
            "2023-09-25",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertHolidayName(name, self.hebrew_holidays, range(1964, 2050))

    def test_pesach(self):
        name = "عيد الفصح اليهودي"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.hebrew_holidays,
            "2020-04-09",
            "2021-03-28",
            "2022-04-16",
            "2023-04-06",
            "2024-04-23",
            "2025-04-13",
        )
        self.assertHolidayName(name, self.hebrew_holidays, range(1964, 2050))

    def test_l10_default(self):
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
