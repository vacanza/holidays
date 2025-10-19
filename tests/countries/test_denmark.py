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

from holidays.constants import OPTIONAL
from holidays.countries.denmark import Denmark, DK, DNK
from tests.common import CommonCountryTests


class TestDenmark(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(1771, 2050)
        super().setUpClass(Denmark, years=cls.full_range)
        cls.optional_holidays = Denmark(categories=OPTIONAL, years=cls.full_range)

    def test_country_aliases(self):
        self.assertAliases(Denmark, DK, DNK)

    def test_no_holidays(self):
        self.assertNoHolidays(Denmark(categories=Denmark.supported_categories, years=1770))

    def test_new_years_day(self):
        self.assertHolidayName("Nytårsdag", (f"{year}-01-01" for year in self.full_range))

    def test_holy_thursday(self):
        name = "Skærtorsdag"
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
        name = "Påskedag"
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
        name = "Anden påskedag"
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

    def test_workers_day(self):
        name = "Arbejdernes kampdag"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-05-01" for year in range(1890, 2050))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(1771, 1890))

    def test_great_day_of_prayers(self):
        name = "Store bededag"
        self.assertHolidayName(
            name,
            "2020-05-08",
            "2021-04-30",
            "2022-05-13",
            "2023-05-05",
        )
        self.assertHolidayName(name, range(1771, 2024))
        self.assertNoHolidayName(name, range(2024, 2050))

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

    def test_whit_sunday(self):
        name = "Pinsedag"
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
        name = "Anden pinsedag"
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

    def test_constitution_day(self):
        name = "Grundlovsdag"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-06-05" for year in range(1891, 2050))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(1771, 1891))

    def test_christmas_eve(self):
        name = "Juleaftensdag"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-12-24" for year in self.full_range)
        )

    def test_christmas_day(self):
        self.assertHolidayName("Juledag", (f"{year}-12-25" for year in self.full_range))

    def test_second_day_of_christmas(self):
        self.assertHolidayName("Anden juledag", (f"{year}-12-26" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Nytårsaften"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-12-31" for year in self.full_range)
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nytårsdag"),
            ("2022-04-14", "Skærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Påskedag"),
            ("2022-04-18", "Anden påskedag"),
            ("2022-05-01", "Arbejdernes kampdag"),
            ("2022-05-13", "Store bededag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Grundlovsdag; Pinsedag"),
            ("2022-06-06", "Anden pinsedag"),
            ("2022-12-24", "Juleaftensdag"),
            ("2022-12-25", "Juledag"),
            ("2022-12-26", "Anden juledag"),
            ("2022-12-31", "Nytårsaften"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Workers' Day"),
            ("2022-05-13", "Great Prayer Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Constitution Day; Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-04-14", "วันพฤหัสศักดิสิทธิ์"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-13", "วันแห่งการอธิษฐานใหญ่"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันรัฐธรรมนูญ; วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-12-24", "วันคริสต์มาสอีฟ"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
            ("2022-12-31", "วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День трудящих"),
            ("2022-05-13", "День загальної молитви"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "День Конституції; Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
            ("2022-12-31", "Переддень Нового року"),
        )
