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

from holidays.countries.sweden import Sweden
from tests.common import CommonCountryTests, SundayHolidays


class TestSweden(CommonCountryTests, SundayHolidays, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Sweden)
        cls.holidays = Sweden(include_sundays=False, years=range(1930, 2050))

    def test_new_years_day(self):
        self.assertHolidayName("Nyårsdagen", (f"{year}-01-01" for year in range(1930, 2050)))

    def test_epiphany(self):
        self.assertHolidayName("Trettondedag jul", (f"{year}-01-06" for year in range(1930, 2050)))

    def test_annunciation(self):
        name = "Jungfru Marie bebådelsedag"
        self.assertHolidayName(name, (f"{year}-03-25" for year in range(1930, 1954)))
        self.assertNoHolidayName(name, range(1954, 2050))

    def test_good_friday(self):
        name = "Långfredagen"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, range(1930, 2050))

    def test_easter_sunday(self):
        name = "Påskdagen"
        self.assertHolidayName(
            name,
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
        )
        self.assertHolidayName(name, range(1952, 2050))

    def test_easter_monday(self):
        name = "Annandag påsk"
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, range(1952, 2050))

    def test_may_day(self):
        name = "Första maj"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1939, 2050)))
        self.assertNoHolidayName(name, range(1930, 1939))

    def test_ascension_day(self):
        name = "Kristi himmelsfärdsdag"
        self.assertHolidayName(
            name,
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
        )
        self.assertHolidayName(name, range(1952, 2050))

    def test_constitution_day(self):
        name = "Sveriges nationaldag"
        self.assertHolidayName(name, (f"{year}-06-06" for year in range(2005, 2050)))
        self.assertNoHolidayName(name, range(1930, 2005))

    def test_whit_sunday(self):
        name = "Pingstdagen"
        self.assertHolidayName(
            name,
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
        )
        self.assertHolidayName(name, range(1930, 2050))

    def test_whit_monday(self):
        name = "Annandag pingst"
        self.assertHolidayName(
            name,
            "1999-05-24",
            "2000-06-12",
            "2001-06-04",
            "2002-05-20",
            "2003-06-09",
            "2004-05-31",
        )
        self.assertHolidayName(name, range(1930, 2005))
        self.assertNoHolidayName(name, range(2005, 2050))

    def test_midsummer_eve(self):
        name = "Midsommarafton"
        self.assertHolidayName(name, (f"{year}-06-23" for year in range(1930, 1953)))
        self.assertHolidayName(
            name,
            "1953-06-19",
            "1954-06-25",
            "2019-06-21",
            "2020-06-19",
            "2021-06-25",
            "2022-06-24",
            "2023-06-23",
            "2024-06-21",
        )
        self.assertHolidayName(name, range(1930, 2050))

    def test_midsummer_day(self):
        name = "Midsommardagen"
        self.assertHolidayName(name, (f"{year}-06-24" for year in range(1930, 1953)))
        self.assertHolidayName(
            name,
            "1953-06-20",
            "1954-06-26",
            "2019-06-22",
            "2020-06-20",
            "2021-06-26",
            "2022-06-25",
            "2023-06-24",
            "2024-06-22",
        )
        self.assertHolidayName(name, range(1930, 2050))

    def test_all_saints_day(self):
        name = "Alla helgons dag"
        self.assertHolidayName(
            name,
            "1953-10-31",
            "1954-11-06",
            "2019-11-02",
            "2020-10-31",
            "2021-11-06",
            "2022-11-05",
            "2023-11-04",
            "2024-11-02",
        )
        self.assertHolidayName(name, range(1953, 2050))
        self.assertNoHolidayName(name, range(1930, 1953))

    def test_christmas(self):
        self.assertHolidayName("Julafton", (f"{year}-12-24" for year in range(1930, 2050)))
        self.assertHolidayName("Juldagen", (f"{year}-12-25" for year in range(1930, 2050)))
        self.assertHolidayName("Annandag jul", (f"{year}-12-26" for year in range(1930, 2050)))

    def test_new_years_eve(self):
        self.assertHolidayName("Nyårsafton", (f"{year}-12-31" for year in range(1930, 2050)))

    def test_sundays(self):
        self.assertSundays(Sweden)  # Sundays are considered holidays in Sweden.

    def test_not_holiday(self):
        # Sundays in Sweden are considered holidays,
        # so make sure none of these are actually Sundays.
        self.assertNoHoliday(
            "2017-02-06",
            "2017-02-07",
            "2017-02-08",
            "2017-02-09",
            "2017-02-10",
            "2016-12-27",
            "2016-12-28",
        )

    def test_2022(self):
        self.assertHolidays(
            Sweden(include_sundays=False, years=2022),
            ("2022-01-01", "Nyårsdagen"),
            ("2022-01-06", "Trettondedag jul"),
            ("2022-04-15", "Långfredagen"),
            ("2022-04-17", "Påskdagen"),
            ("2022-04-18", "Annandag påsk"),
            ("2022-05-01", "Första maj"),
            ("2022-05-26", "Kristi himmelsfärdsdag"),
            ("2022-06-05", "Pingstdagen"),
            ("2022-06-06", "Sveriges nationaldag"),
            ("2022-06-24", "Midsommarafton"),
            ("2022-06-25", "Midsommardagen"),
            ("2022-11-05", "Alla helgons dag"),
            ("2022-12-24", "Julafton"),
            ("2022-12-25", "Juldagen"),
            ("2022-12-26", "Annandag jul"),
            ("2022-12-31", "Nyårsafton"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Nyårsdagen"),
            ("2018-01-06", "Trettondedag jul"),
            ("2018-01-07", "Söndag"),
            ("2018-01-14", "Söndag"),
            ("2018-01-21", "Söndag"),
            ("2018-01-28", "Söndag"),
            ("2018-02-04", "Söndag"),
            ("2018-02-11", "Söndag"),
            ("2018-02-18", "Söndag"),
            ("2018-02-25", "Söndag"),
            ("2018-03-04", "Söndag"),
            ("2018-03-11", "Söndag"),
            ("2018-03-18", "Söndag"),
            ("2018-03-25", "Söndag"),
            ("2018-03-30", "Långfredagen"),
            ("2018-04-01", "Påskdagen; Söndag"),
            ("2018-04-02", "Annandag påsk"),
            ("2018-04-08", "Söndag"),
            ("2018-04-15", "Söndag"),
            ("2018-04-22", "Söndag"),
            ("2018-04-29", "Söndag"),
            ("2018-05-01", "Första maj"),
            ("2018-05-06", "Söndag"),
            ("2018-05-10", "Kristi himmelsfärdsdag"),
            ("2018-05-13", "Söndag"),
            ("2018-05-20", "Pingstdagen; Söndag"),
            ("2018-05-27", "Söndag"),
            ("2018-06-03", "Söndag"),
            ("2018-06-06", "Sveriges nationaldag"),
            ("2018-06-10", "Söndag"),
            ("2018-06-17", "Söndag"),
            ("2018-06-22", "Midsommarafton"),
            ("2018-06-23", "Midsommardagen"),
            ("2018-06-24", "Söndag"),
            ("2018-07-01", "Söndag"),
            ("2018-07-08", "Söndag"),
            ("2018-07-15", "Söndag"),
            ("2018-07-22", "Söndag"),
            ("2018-07-29", "Söndag"),
            ("2018-08-05", "Söndag"),
            ("2018-08-12", "Söndag"),
            ("2018-08-19", "Söndag"),
            ("2018-08-26", "Söndag"),
            ("2018-09-02", "Söndag"),
            ("2018-09-09", "Söndag"),
            ("2018-09-16", "Söndag"),
            ("2018-09-23", "Söndag"),
            ("2018-09-30", "Söndag"),
            ("2018-10-07", "Söndag"),
            ("2018-10-14", "Söndag"),
            ("2018-10-21", "Söndag"),
            ("2018-10-28", "Söndag"),
            ("2018-11-03", "Alla helgons dag"),
            ("2018-11-04", "Söndag"),
            ("2018-11-11", "Söndag"),
            ("2018-11-18", "Söndag"),
            ("2018-11-25", "Söndag"),
            ("2018-12-02", "Söndag"),
            ("2018-12-09", "Söndag"),
            ("2018-12-16", "Söndag"),
            ("2018-12-23", "Söndag"),
            ("2018-12-24", "Julafton"),
            ("2018-12-25", "Juldagen"),
            ("2018-12-26", "Annandag jul"),
            ("2018-12-30", "Söndag"),
            ("2018-12-31", "Nyårsafton"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-01-06", "Epiphany"),
            ("2018-01-07", "Sunday"),
            ("2018-01-14", "Sunday"),
            ("2018-01-21", "Sunday"),
            ("2018-01-28", "Sunday"),
            ("2018-02-04", "Sunday"),
            ("2018-02-11", "Sunday"),
            ("2018-02-18", "Sunday"),
            ("2018-02-25", "Sunday"),
            ("2018-03-04", "Sunday"),
            ("2018-03-11", "Sunday"),
            ("2018-03-18", "Sunday"),
            ("2018-03-25", "Sunday"),
            ("2018-03-30", "Good Friday"),
            ("2018-04-01", "Easter Sunday; Sunday"),
            ("2018-04-02", "Easter Monday"),
            ("2018-04-08", "Sunday"),
            ("2018-04-15", "Sunday"),
            ("2018-04-22", "Sunday"),
            ("2018-04-29", "Sunday"),
            ("2018-05-01", "May Day"),
            ("2018-05-06", "Sunday"),
            ("2018-05-10", "Ascension Day"),
            ("2018-05-13", "Sunday"),
            ("2018-05-20", "Sunday; Whit Sunday"),
            ("2018-05-27", "Sunday"),
            ("2018-06-03", "Sunday"),
            ("2018-06-06", "National Day of Sweden"),
            ("2018-06-10", "Sunday"),
            ("2018-06-17", "Sunday"),
            ("2018-06-22", "Midsummer Eve"),
            ("2018-06-23", "Midsummer Day"),
            ("2018-06-24", "Sunday"),
            ("2018-07-01", "Sunday"),
            ("2018-07-08", "Sunday"),
            ("2018-07-15", "Sunday"),
            ("2018-07-22", "Sunday"),
            ("2018-07-29", "Sunday"),
            ("2018-08-05", "Sunday"),
            ("2018-08-12", "Sunday"),
            ("2018-08-19", "Sunday"),
            ("2018-08-26", "Sunday"),
            ("2018-09-02", "Sunday"),
            ("2018-09-09", "Sunday"),
            ("2018-09-16", "Sunday"),
            ("2018-09-23", "Sunday"),
            ("2018-09-30", "Sunday"),
            ("2018-10-07", "Sunday"),
            ("2018-10-14", "Sunday"),
            ("2018-10-21", "Sunday"),
            ("2018-10-28", "Sunday"),
            ("2018-11-03", "All Saints' Day"),
            ("2018-11-04", "Sunday"),
            ("2018-11-11", "Sunday"),
            ("2018-11-18", "Sunday"),
            ("2018-11-25", "Sunday"),
            ("2018-12-02", "Sunday"),
            ("2018-12-09", "Sunday"),
            ("2018-12-16", "Sunday"),
            ("2018-12-23", "Sunday"),
            ("2018-12-24", "Christmas Eve"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Second Day of Christmas"),
            ("2018-12-30", "Sunday"),
            ("2018-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2018-01-01", "วันขึ้นปีใหม่"),
            ("2018-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2018-01-07", "วันอาทิตย์"),
            ("2018-01-14", "วันอาทิตย์"),
            ("2018-01-21", "วันอาทิตย์"),
            ("2018-01-28", "วันอาทิตย์"),
            ("2018-02-04", "วันอาทิตย์"),
            ("2018-02-11", "วันอาทิตย์"),
            ("2018-02-18", "วันอาทิตย์"),
            ("2018-02-25", "วันอาทิตย์"),
            ("2018-03-04", "วันอาทิตย์"),
            ("2018-03-11", "วันอาทิตย์"),
            ("2018-03-18", "วันอาทิตย์"),
            ("2018-03-25", "วันอาทิตย์"),
            ("2018-03-30", "วันศุกร์ประเสริฐ"),
            ("2018-04-01", "วันอาทิตย์; วันอาทิตย์อีสเตอร์"),
            ("2018-04-02", "วันจันทร์อีสเตอร์"),
            ("2018-04-08", "วันอาทิตย์"),
            ("2018-04-15", "วันอาทิตย์"),
            ("2018-04-22", "วันอาทิตย์"),
            ("2018-04-29", "วันอาทิตย์"),
            ("2018-05-01", "วันเมย์เดย์ (วันแรงงาน)"),
            ("2018-05-06", "วันอาทิตย์"),
            ("2018-05-10", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2018-05-13", "วันอาทิตย์"),
            ("2018-05-20", "วันสมโภชพระจิตเจ้า; วันอาทิตย์"),
            ("2018-05-27", "วันอาทิตย์"),
            ("2018-06-03", "วันอาทิตย์"),
            ("2018-06-06", "วันชาติสวีเดน"),
            ("2018-06-10", "วันอาทิตย์"),
            ("2018-06-17", "วันอาทิตย์"),
            ("2018-06-22", "วันก่อนวันกลางฤดูร้อน"),
            ("2018-06-23", "วันกลางฤดูร้อน"),
            ("2018-06-24", "วันอาทิตย์"),
            ("2018-07-01", "วันอาทิตย์"),
            ("2018-07-08", "วันอาทิตย์"),
            ("2018-07-15", "วันอาทิตย์"),
            ("2018-07-22", "วันอาทิตย์"),
            ("2018-07-29", "วันอาทิตย์"),
            ("2018-08-05", "วันอาทิตย์"),
            ("2018-08-12", "วันอาทิตย์"),
            ("2018-08-19", "วันอาทิตย์"),
            ("2018-08-26", "วันอาทิตย์"),
            ("2018-09-02", "วันอาทิตย์"),
            ("2018-09-09", "วันอาทิตย์"),
            ("2018-09-16", "วันอาทิตย์"),
            ("2018-09-23", "วันอาทิตย์"),
            ("2018-09-30", "วันอาทิตย์"),
            ("2018-10-07", "วันอาทิตย์"),
            ("2018-10-14", "วันอาทิตย์"),
            ("2018-10-21", "วันอาทิตย์"),
            ("2018-10-28", "วันอาทิตย์"),
            ("2018-11-03", "วันสมโภชนักบุญทั้งหลาย"),
            ("2018-11-04", "วันอาทิตย์"),
            ("2018-11-11", "วันอาทิตย์"),
            ("2018-11-18", "วันอาทิตย์"),
            ("2018-11-25", "วันอาทิตย์"),
            ("2018-12-02", "วันอาทิตย์"),
            ("2018-12-09", "วันอาทิตย์"),
            ("2018-12-16", "วันอาทิตย์"),
            ("2018-12-23", "วันอาทิตย์"),
            ("2018-12-24", "วันคริสต์มาสอีฟ"),
            ("2018-12-25", "วันคริสต์มาส"),
            ("2018-12-26", "วันคริสต์มาสวันที่สอง"),
            ("2018-12-30", "วันอาทิตย์"),
            ("2018-12-31", "วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2018-01-01", "Новий рік"),
            ("2018-01-06", "Богоявлення"),
            ("2018-01-07", "Неділя"),
            ("2018-01-14", "Неділя"),
            ("2018-01-21", "Неділя"),
            ("2018-01-28", "Неділя"),
            ("2018-02-04", "Неділя"),
            ("2018-02-11", "Неділя"),
            ("2018-02-18", "Неділя"),
            ("2018-02-25", "Неділя"),
            ("2018-03-04", "Неділя"),
            ("2018-03-11", "Неділя"),
            ("2018-03-18", "Неділя"),
            ("2018-03-25", "Неділя"),
            ("2018-03-30", "Страсна пʼятниця"),
            ("2018-04-01", "Великдень; Неділя"),
            ("2018-04-02", "Великодній понеділок"),
            ("2018-04-08", "Неділя"),
            ("2018-04-15", "Неділя"),
            ("2018-04-22", "Неділя"),
            ("2018-04-29", "Неділя"),
            ("2018-05-01", "Перше травня"),
            ("2018-05-06", "Неділя"),
            ("2018-05-10", "Вознесіння Господнє"),
            ("2018-05-13", "Неділя"),
            ("2018-05-20", "Неділя; Трійця"),
            ("2018-05-27", "Неділя"),
            ("2018-06-03", "Неділя"),
            ("2018-06-06", "Національний день Швеції"),
            ("2018-06-10", "Неділя"),
            ("2018-06-17", "Неділя"),
            ("2018-06-22", "Переддень літнього сонцестояння"),
            ("2018-06-23", "День літнього сонцестояння"),
            ("2018-06-24", "Неділя"),
            ("2018-07-01", "Неділя"),
            ("2018-07-08", "Неділя"),
            ("2018-07-15", "Неділя"),
            ("2018-07-22", "Неділя"),
            ("2018-07-29", "Неділя"),
            ("2018-08-05", "Неділя"),
            ("2018-08-12", "Неділя"),
            ("2018-08-19", "Неділя"),
            ("2018-08-26", "Неділя"),
            ("2018-09-02", "Неділя"),
            ("2018-09-09", "Неділя"),
            ("2018-09-16", "Неділя"),
            ("2018-09-23", "Неділя"),
            ("2018-09-30", "Неділя"),
            ("2018-10-07", "Неділя"),
            ("2018-10-14", "Неділя"),
            ("2018-10-21", "Неділя"),
            ("2018-10-28", "Неділя"),
            ("2018-11-03", "День усіх святих"),
            ("2018-11-04", "Неділя"),
            ("2018-11-11", "Неділя"),
            ("2018-11-18", "Неділя"),
            ("2018-11-25", "Неділя"),
            ("2018-12-02", "Неділя"),
            ("2018-12-09", "Неділя"),
            ("2018-12-16", "Неділя"),
            ("2018-12-23", "Неділя"),
            ("2018-12-24", "Святий вечір"),
            ("2018-12-25", "Різдво Христове"),
            ("2018-12-26", "Другий день Різдва"),
            ("2018-12-30", "Неділя"),
            ("2018-12-31", "Переддень Нового року"),
        )
