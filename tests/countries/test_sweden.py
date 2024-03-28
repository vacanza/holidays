#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.sweden import Sweden, SE, SWE
from tests.common import CommonCountryTests, SundayHolidays


class TestSweden(CommonCountryTests, SundayHolidays, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Sweden)

    def setUp(self):
        super().setUp()
        self.holidays.include_sundays = False

    def test_country_aliases(self):
        self.assertAliases(Sweden, SE, SWE)

    def test_new_years(self):
        self.assertHoliday(
            "1900-01-01",
            "2017-01-01",
            "2023-01-01",
        )

    def test_annunciation(self):
        self.assertHoliday(
            "1950-03-25",
            "1951-03-25",
            "1952-03-25",
            "1953-03-25",
        )
        self.assertNoHoliday("1954-03-25")
        self.assertNoHolidayName("Jungfru Marie bebådelsedag", Sweden(years=1954))

    def test_easter(self):
        self.assertHoliday(
            "2000-04-21",
            "2000-04-23",
            "2000-04-24",
            "2010-04-02",
            "2010-04-04",
            "2010-04-05",
            "2021-04-02",
            "2021-04-04",
            "2021-04-05",
            "2024-03-29",
            "2024-03-31",
            "2024-04-01",
        )
        self.assertNoHoliday(
            "2000-04-20",
            "2010-04-01",
            "2021-04-01",
            "2024-03-28",
        )

    def test_may_day(self):
        self.assertHoliday(
            "1939-05-01",
            "2017-05-01",
            "2023-05-01",
        )
        self.assertNoHoliday("1938-05-01")
        self.assertNoHolidayName("Första maj", Sweden(years=1938))

    def test_constitution_day(self):
        self.assertHoliday(
            "2005-06-06",
            "2017-06-06",
            "2999-06-06",
        )
        self.assertNoHoliday("2004-06-06")
        self.assertNoHolidayName("Sveriges nationaldag", Sweden(years=2004))

    def test_pentecost(self):
        self.assertHoliday(
            "2000-06-11",
            "2000-06-12",
            "2010-05-23",
            "2021-05-23",
            "2003-06-09",
            "2024-05-19",
        )
        self.assertNoHoliday(
            "2010-05-24",
            "2021-05-24",
            "2024-05-20",
        )
        self.assertNoHolidayName("Annandag pingst", Sweden(years=2005))

    def test_midsommar(self):
        self.assertHoliday(
            "1950-06-23",
            "1950-06-24",
            "1951-06-23",
            "1951-06-24",
            "1952-06-23",
            "1952-06-24",
            "1953-06-19",
            "1953-06-20",
            "1954-06-25",
            "1954-06-26",
            "2019-06-21",
            "2019-06-22",
            "2020-06-19",
            "2020-06-20",
            "2021-06-25",
            "2021-06-26",
            "2022-06-24",
            "2022-06-25",
        )
        self.assertNoHoliday(
            "1952-06-20",
            "1952-06-21",
            "1953-06-23",
            "1953-06-24",
            "1954-06-23",
            "1954-06-24",
        )

    def test_christmas(self):
        self.assertHoliday(
            "1901-12-25",
            "1901-12-26",
            "2016-12-25",
            "2016-12-26",
        )

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
