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
        cls.full_range = range(DZ.start_year, 2050)
        super().setUpClass(Algeria, years=cls.full_range)

    def test_country_aliases(self):
        self.assertAliases(Algeria, DZ, DZA)

    def test_no_holidays(self):
        self.assertNoHolidays(Algeria(years=DZ.start_year - 1))

    def test_new_years_day(self):
        self.assertHolidayName(
            "رأس السنة الميلادية", (f"{year}-01-01" for year in self.full_range)
        )

    def test_amazigh_new_year(self):
        name = "رأس السنة الأمازيغية"
        self.assertHolidayName(name, (f"{year}-01-12" for year in range(2018, 2050)))
        self.assertNoHolidayName(name, range(DZ.start_year, 2018))

    def test_labor_day(self):
        self.assertHolidayName("عيد العمال", (f"{year}-05-01" for year in self.full_range))

    def test_independence_day(self):
        self.assertHolidayName("عيد الإستقلال", (f"{year}-07-05" for year in self.full_range))

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
        name_holiday = f"عطلة {name}"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        self.assertIslamicNoEstimatedHolidayName(
            name_holiday,
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name_holiday, self.full_range)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        name_holiday = f"عطلة {name}"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(
            name_holiday,
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2023-06-30",
            "2024-06-17",
            "2024-06-18",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        self.assertIslamicNoEstimatedHolidayName(name_holiday, self.full_range)

    def test_l10_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-01-12", "رأس السنة الأمازيغية"),
            ("2022-05-01", "عيد العمال"),
            ("2022-05-02", "عيد الفطر (المقدرة)"),
            ("2022-05-03", "عطلة عيد الفطر (المقدرة)"),
            ("2022-07-05", "عيد الإستقلال"),
            ("2022-07-09", "عيد الأضحى (المقدرة)"),
            ("2022-07-10", "عطلة عيد الأضحى (المقدرة)"),
            ("2022-07-30", "رأس السنة الهجرية (المقدرة)"),
            ("2022-08-08", "عاشورة (المقدرة)"),
            ("2022-10-08", "عيد المولد النبوي (المقدرة)"),
            ("2022-11-01", "عيد الثورة"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-12", "Amazigh New Year"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-03", "Eid al-Fitr Holiday (estimated)"),
            ("2022-07-05", "Independence Day"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-07-10", "Eid al-Adha Holiday (estimated)"),
            ("2022-07-30", "Islamic New Year (estimated)"),
            ("2022-08-08", "Ashura (estimated)"),
            ("2022-10-08", "Prophet's Birthday (estimated)"),
            ("2022-11-01", "Revolution Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Nouvel an"),
            ("2022-01-12", "Nouvel an Amazigh"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-02", "Fête de la rupture du jeûne (estimé)"),
            ("2022-05-03", "Congé de fête de la rupture du jeûne (estimé)"),
            ("2022-07-05", "Fête de l'indépendance"),
            ("2022-07-09", "Fête du sacrifice (estimé)"),
            ("2022-07-10", "Congé de fête du sacrifice (estimé)"),
            ("2022-07-30", "Nouvel an musulman (estimé)"),
            ("2022-08-08", "Achoura (estimé)"),
            ("2022-10-08", "Anniversaire du prophète (estimé)"),
            ("2022-11-01", "Fête de la Révolution"),
        )
