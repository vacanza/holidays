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

from holidays.countries.iceland import Iceland
from tests.common import CommonCountryTests


class TestIceland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Iceland)

    def test_new_years_day(self):
        self.assertHolidayName("Nýársdagur", (f"{year}-01-01" for year in self.full_range))

    def test_maundy_thursday(self):
        name = "Skírdagur"
        self.assertHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Föstudagurinn langi"
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
        name = "Páskadagur"
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
        name = "Annar í páskum"
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

    def test_first_day_of_summer(self):
        name = "Sumardagurinn fyrsti"
        self.assertHolidayName(
            name,
            "2020-04-23",
            "2021-04-22",
            "2022-04-21",
            "2023-04-20",
            "2024-04-25",
            "2025-04-24",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Verkalýðsdagurinn", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        name = "Uppstigningardagur"
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

    def test_whit_sunday(self):
        name = "Hvítasunnudagur"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Annar í hvítasunnu"
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
        self.assertHolidayName(
            "Þjóðhátíðardagurinn", (f"{year}-06-17" for year in self.full_range)
        )

    def test_commerce_day(self):
        name = "Frídagur verslunarmanna"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, range(1983, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1983))

    def test_christmas_eve(self):
        name = "Aðfangadagur (frá kl. 13.00)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Jóladagur", (f"{year}-12-25" for year in self.full_range))

    def test_second_day_of_christmas(self):
        self.assertHolidayName("Annar í jólum", (f"{year}-12-26" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Gamlársdagur (frá kl. 13.00)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_2018_public(self):
        self.assertHolidaysInYear(
            2018,
            ("2018-01-01", "Nýársdagur"),
            ("2018-03-29", "Skírdagur"),
            ("2018-03-30", "Föstudagurinn langi"),
            ("2018-04-01", "Páskadagur"),
            ("2018-04-02", "Annar í páskum"),
            ("2018-04-19", "Sumardagurinn fyrsti"),
            ("2018-05-01", "Verkalýðsdagurinn"),
            ("2018-05-10", "Uppstigningardagur"),
            ("2018-05-20", "Hvítasunnudagur"),
            ("2018-05-21", "Annar í hvítasunnu"),
            ("2018-06-17", "Þjóðhátíðardagurinn"),
            ("2018-08-06", "Frídagur verslunarmanna"),
            ("2018-12-25", "Jóladagur"),
            ("2018-12-26", "Annar í jólum"),
        )

    def test_2018_half_day(self):
        self.assertHalfDayHolidaysInYear(
            2018,
            ("2018-12-24", "Aðfangadagur (frá kl. 13.00)"),
            ("2018-12-31", "Gamlársdagur (frá kl. 13.00)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nýársdagur"),
            ("2022-04-14", "Skírdagur"),
            ("2022-04-15", "Föstudagurinn langi"),
            ("2022-04-17", "Páskadagur"),
            ("2022-04-18", "Annar í páskum"),
            ("2022-04-21", "Sumardagurinn fyrsti"),
            ("2022-05-01", "Verkalýðsdagurinn"),
            ("2022-05-26", "Uppstigningardagur"),
            ("2022-06-05", "Hvítasunnudagur"),
            ("2022-06-06", "Annar í hvítasunnu"),
            ("2022-06-17", "Þjóðhátíðardagurinn"),
            ("2022-08-01", "Frídagur verslunarmanna"),
            ("2022-12-24", "Aðfangadagur (frá kl. 13.00)"),
            ("2022-12-25", "Jóladagur"),
            ("2022-12-26", "Annar í jólum"),
            ("2022-12-31", "Gamlársdagur (frá kl. 13.00)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-21", "First Day of Summer"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-17", "National Day"),
            ("2022-08-01", "Commerce Day"),
            ("2022-12-24", "Christmas Eve (from 1pm)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            ("2022-12-31", "New Year's Eve (from 1pm)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-21", "Перший день літа"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-17", "Національне свято"),
            ("2022-08-01", "День торгівлі"),
            ("2022-12-24", "Святий вечір (з 13:00)"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
            ("2022-12-31", "Переддень Нового року (з 13:00)"),
        )
