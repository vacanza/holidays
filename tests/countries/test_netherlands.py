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
from holidays.countries.netherlands import Netherlands
from tests.common import CommonCountryTests


class TestNetherlands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Netherlands)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Netherlands(categories=OPTIONAL, years=range(self.start_year, 1982)))

    def test_new_years_day(self):
        self.assertHolidayName("Nieuwjaarsdag", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Goede Vrijdag"
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
        name = "Eerste paasdag"
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
        name = "Tweede paasdag"
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

    def test_queens_day(self):
        name = "Koninginnedag"
        self.assertHolidayName(
            name,
            "1967-05-01",
            "1972-05-01",
            "1978-05-01",
            "1989-04-29",
            "1995-04-29",
            "2000-04-29",
            "2006-04-29",
            "2013-04-30",
        )
        self.assertHolidayName(name, range(self.start_year, 2014))
        self.assertNoHolidayName(
            name,
            "1967-04-30",
            "1972-04-30",
            "1978-04-30",
            "1995-04-30",
            "1989-04-30",
            "2000-04-30",
            "2006-04-30",
        )
        self.assertNoHolidayName(name, range(2014, self.end_year))

    def test_king_day(self):
        name = "Koningsdag"
        self.assertHolidayName(
            name,
            "2016-04-27",
            "2017-04-27",
            "2018-04-27",
            "2019-04-27",
            "2020-04-27",
            "2021-04-27",
            "2022-04-27",
            "2023-04-27",
            "2024-04-27",
            "2025-04-26",
            "2031-04-26",
            "2036-04-26",
        )
        self.assertHolidayName(name, range(2014, self.end_year))
        self.assertNoHolidayName(
            name,
            "2014-04-27",
            "2025-04-27",
            "2031-04-27",
            "2036-04-27",
        )
        self.assertNoHolidayName(name, range(self.start_year, 2014))

    def test_liberation_day(self):
        name = "Bevrijdingsdag"
        # PUBLIC.
        self.assertHolidayName(
            name, (f"{year}-05-05" for year in self.full_range if year % 5 == 0)
        )
        self.assertNoHolidayName(
            name, (f"{year}-05-05" for year in self.full_range if year % 5 != 0)
        )
        # OPTIONAL.
        self.assertOptionalHolidayName(
            name, (f"{year}-05-05" for year in range(1982, self.end_year))
        )
        self.assertNoOptionalHolidayName(name, range(self.start_year, 1982))

    def test_ascension_day(self):
        name = "Hemelvaartsdag"
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
        name = "Eerste Pinksterdag"
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
        name = "Tweede Pinksterdag"
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
        self.assertHolidayName("Eerste Kerstdag", (f"{year}-12-25" for year in self.full_range))

    def test_second_day_of_christmas(self):
        self.assertHolidayName("Tweede Kerstdag", (f"{year}-12-26" for year in self.full_range))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nieuwjaarsdag"),
            ("2022-04-15", "Goede Vrijdag"),
            ("2022-04-17", "Eerste paasdag"),
            ("2022-04-18", "Tweede paasdag"),
            ("2022-04-27", "Koningsdag"),
            ("2022-05-05", "Bevrijdingsdag"),
            ("2022-05-26", "Hemelvaartsdag"),
            ("2022-06-05", "Eerste Pinksterdag"),
            ("2022-06-06", "Tweede Pinksterdag"),
            ("2022-12-25", "Eerste Kerstdag"),
            ("2022-12-26", "Tweede Kerstdag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "King's Day"),
            ("2022-05-05", "Liberation Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_fy(self):
        self.assertLocalizedHolidays(
            "fy",
            ("2022-01-01", "Nijjiersdei"),
            ("2022-04-15", "Goedfreed"),
            ("2022-04-17", "Peaskesnein"),
            ("2022-04-18", "Peaskemoandei"),
            ("2022-04-27", "Keningsdei"),
            ("2022-05-05", "Befrijingsdei"),
            ("2022-05-26", "Himelfeartsdei"),
            ("2022-06-05", "Pinkstersnein"),
            ("2022-06-06", "Pinkstermoandei"),
            ("2022-12-25", "Eerste Krystdei"),
            ("2022-12-26", "Twadde Krystdei"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-04-27", "วันเฉลิมพระชนมพรรษาสมเด็จพระราชาธิบดี"),
            ("2022-05-05", "วันประกาศอิสรภาพ"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-12-25", "วันคริสต์มาสวันแรก"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-27", "День короля"),
            ("2022-05-05", "День визволення"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
