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

from holidays.countries.norway import Norway
from tests.common import CommonCountryTests, SundayHolidays


class TestNorway(CommonCountryTests, SundayHolidays, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(1940, 2050)
        super().setUpClass(Norway)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_new_years_day(self):
        self.assertHolidayName("Første nyttårsdag", (f"{year}-01-01" for year in self.full_range))

    def test_maundy_thursday(self):
        name = "Skjærtorsdag"
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
        name = "Langfredag"
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
        name = "Første påskedag"
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
        name = "Andre påskedag"
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
        name = "Arbeidernes dag"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1947, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1947))

    def test_constitution_day(self):
        name = "Grunnlovsdag"
        self.assertHolidayName(name, (f"{year}-05-17" for year in range(1947, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1947))

    def test_ascension_day(self):
        name = "Kristi himmelfartsdag"
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

    def test_pentecost(self):
        name = "Første pinsedag"
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

    def test_pentecost_monday(self):
        name = "Andre pinsedag"
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

    def test_christmas_day(self):
        self.assertHolidayName("Første juledag", (f"{year}-12-25" for year in self.full_range))

    def test_second_day_of_christmas(self):
        self.assertHolidayName("Andre juledag", (f"{year}-12-26" for year in self.full_range))

    def test_sundays(self):
        self.assertSundays(Norway)  # Sundays are considered holidays in Norway.

    def test_not_holiday(self):
        # TODO: Add more dates that are often confused for being a holiday.

        # Sundays in Norway are considered holidays,
        # so make sure none of these are actually Sundays.
        self.assertNoHoliday(
            "2017-02-06",
            "2017-02-07",
            "2017-02-08",
            "2017-02-09",
            "2017-02-10",
            "2001-12-24",
            "2001-05-16",
            "2001-05-18",
            "1999-12-31",
            "2016-12-31",
            "2016-12-27",
            "2016-12-28",
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Første nyttårsdag"),
            ("2022-04-14", "Skjærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Første påskedag"),
            ("2022-04-18", "Andre påskedag"),
            ("2022-05-01", "Arbeidernes dag"),
            ("2022-05-17", "Grunnlovsdag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Første pinsedag"),
            ("2022-06-06", "Andre pinsedag"),
            ("2022-12-25", "Første juledag"),
            ("2022-12-26", "Andre juledag"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Første nyttårsdag"),
            ("2022-04-14", "Skjærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Første påskedag"),
            ("2022-04-18", "Andre påskedag"),
            ("2022-05-01", "Arbeidernes dag"),
            ("2022-05-17", "Grunnlovsdag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Første pinsedag"),
            ("2022-06-06", "Andre pinsedag"),
            ("2022-12-25", "Første juledag"),
            ("2022-12-26", "Andre juledag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-17", "Constitution Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Pentecost"),
            ("2022-06-06", "Pentecost Monday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-17", "День Конституції"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Пʼятидесятниця"),
            ("2022-06-06", "Другий день Пʼятидесятниці"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-04-14", "วันพฤหัสศักดิ์สิทธิ์"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-17", "วันรัฐธรรมนูญ"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-12-25", "วันคริสต์มาสวันแรก"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
        )
