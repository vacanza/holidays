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

from holidays.countries.madagascar import Madagascar
from tests.common import CommonCountryTests


class TestMadagascar(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Madagascar)

    def test_new_years_day(self):
        self.assertHolidayName("Taom-baovao", (f"{year}-01-01" for year in self.full_range))

    def test_womens_day(self):
        self.assertHolidayName("Fetin'ny vehivavy", (f"{year}-03-08" for year in self.full_range))

    def test_martyrs_day(self):
        self.assertHolidayName("Fetin'ny mahery fo", (f"{year}-03-29" for year in self.full_range))

    def test_easter_sunday(self):
        name = "Fetin'ny paska"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        self.assertHolidayName(
            "Alatsinain'ny paska",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName("Alatsinain'ny paska", self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Fetin'ny asa", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        self.assertHolidayName(
            "Fiakaran'ny Jesosy kristy tany an-danitra",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName("Fiakaran'ny Jesosy kristy tany an-danitra", self.full_range)

    def test_pentecost(self):
        self.assertHolidayName(
            "Pentekosta",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName("Pentekosta", self.full_range)

    def test_pentecost_monday(self):
        self.assertHolidayName(
            "Alatsinain'ny pentekosta",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName("Alatsinain'ny pentekosta", self.full_range)

    def test_mothers_day(self):
        self.assertHolidayName(
            "Fetin'ny reny",
            "2020-06-07",
            "2021-05-30",
            "2022-05-29",
            "2023-06-04",
            "2024-05-26",
            "2025-05-25",
        )
        self.assertHolidayName("Fetin'ny reny", self.full_range)

    def test_father_day(self):
        self.assertHolidayName(
            "Fetin'ny ray",
            "2020-06-21",
            "2021-06-20",
            "2022-06-19",
            "2023-06-18",
            "2024-06-16",
            "2025-06-15",
        )
        self.assertHolidayName("Fetin'ny ray", self.full_range)

    def test_independence_day(self):
        name = "Fetin'ny fahaleovantena"
        self.assertHolidayName(name, (f"{year}-06-26" for year in range(1960, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1960))

    def test_assumption_day(self):
        self.assertHolidayName(
            "Fiakaran'ny Masina Maria tany an-danitra",
            (f"{year}-08-15" for year in self.full_range),
        )

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Fetin'ny olo-masina",
            (f"{year}-11-01" for year in self.full_range),
        )

    def test_republic_day(self):
        name = "Fetin'ny Repoblika"
        self.assertHolidayName(name, (f"{year}-12-11" for year in range(2011, 2050)))
        self.assertNoHolidayName(name, range(1947, 2011))

    def test_christmas_day(self):
        self.assertHolidayName("Fetin'ny noely", (f"{year}-12-25" for year in self.full_range))

    def test_2021(self):
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "Taom-baovao"),
            ("2021-03-08", "Fetin'ny vehivavy"),
            ("2021-03-29", "Fetin'ny mahery fo"),
            ("2021-04-04", "Fetin'ny paska"),
            ("2021-04-05", "Alatsinain'ny paska"),
            ("2021-05-01", "Fetin'ny asa"),
            ("2021-05-13", "Fiakaran'ny Jesosy kristy tany an-danitra"),
            ("2021-05-23", "Pentekosta"),
            ("2021-05-24", "Alatsinain'ny pentekosta"),
            ("2021-05-30", "Fetin'ny reny"),
            ("2021-06-20", "Fetin'ny ray"),
            ("2021-06-26", "Fetin'ny fahaleovantena"),
            ("2021-08-15", "Fiakaran'ny Masina Maria tany an-danitra"),
            ("2021-11-01", "Fetin'ny olo-masina"),
            ("2021-12-11", "Fetin'ny Repoblika"),
            ("2021-12-25", "Fetin'ny noely"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Taom-baovao"),
            ("2022-03-08", "Fetin'ny vehivavy"),
            ("2022-03-29", "Fetin'ny mahery fo"),
            ("2022-04-17", "Fetin'ny paska"),
            ("2022-04-18", "Alatsinain'ny paska"),
            ("2022-05-01", "Fetin'ny asa"),
            ("2022-05-26", "Fiakaran'ny Jesosy kristy tany an-danitra"),
            ("2022-05-29", "Fetin'ny reny"),
            ("2022-06-05", "Pentekosta"),
            ("2022-06-06", "Alatsinain'ny pentekosta"),
            ("2022-06-19", "Fetin'ny ray"),
            ("2022-06-26", "Fetin'ny fahaleovantena"),
            ("2022-08-15", "Fiakaran'ny Masina Maria tany an-danitra"),
            ("2022-11-01", "Fetin'ny olo-masina"),
            ("2022-12-11", "Fetin'ny Repoblika"),
            ("2022-12-25", "Fetin'ny noely"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-03-08", "Women's Day"),
            ("2022-03-29", "Martyrs' Day"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-05-29", "Mother's Day"),
            ("2022-06-05", "Pentecost"),
            ("2022-06-06", "Pentecost Monday"),
            ("2022-06-19", "Father's Day"),
            ("2022-06-26", "Independence Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-11", "Republic Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-03-08", "Жіночий день"),
            ("2022-03-29", "День мучеників"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-05-29", "День матері"),
            ("2022-06-05", "Пʼятидесятниця"),
            ("2022-06-06", "Другий день Пʼятидесятниці"),
            ("2022-06-19", "День батька"),
            ("2022-06-26", "День незалежності"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-11", "День Республіки"),
            ("2022-12-25", "Різдво Христове"),
        )
