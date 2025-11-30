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

from holidays.constants import BANK, OPTIONAL
from holidays.countries.sweden import Sweden
from tests.common import CommonCountryTests, SundayHolidays


class TestSweden(CommonCountryTests, SundayHolidays, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Sweden)
        cls.holidays = Sweden(include_sundays=False, years=cls.full_range)

    def test_new_years_day(self):
        self.assertHolidayName("Nyårsdagen", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany(self):
        self.assertHolidayName("Trettondedag jul", (f"{year}-01-06" for year in self.full_range))

    def test_feast_of_annunciation(self):
        name = "Marie bebådelsedag"
        self.assertHolidayName(
            name,
            "1953-03-22",
            "1954-03-28",
            "1955-03-27",
            "1964-03-15",  # Sunday 1964-03-22 is Palm Sunday.
            "1965-03-28",
            "1966-03-27",
            "1967-03-12",  # Sunday 1967-03-26 is Easter Sunday.
            "1985-03-24",
            "1986-03-16",
            "1987-03-22",
            "1988-03-20",
            "1989-03-12",
        )
        self.assertHolidayName(name, range(self.start_year, 1990))
        self.assertNoHolidayName(name, range(1990, self.end_year))

    def test_good_friday(self):
        name = "Långfredagen"
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
        name = "Påskdagen"
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
        name = "Annandag påsk"
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

    def test_may_day(self):
        self.assertHolidayName("Första maj", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        name = "Kristi himmelsfärdsdag"
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

    def test_national_day(self):
        name = "Nationaldagen"
        self.assertHolidayName(name, (f"{year}-06-06" for year in range(2005, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2005))

    def test_whit_sunday(self):
        name = "Pingstdagen"
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
        self.assertHolidayName(name, range(self.start_year, 2005))
        self.assertNoHolidayName(name, range(2005, self.end_year))

    def test_midsummer_day(self):
        name = "Midsommardagen"
        self.assertHolidayName(
            name,
            "2020-06-20",
            "2021-06-26",
            "2022-06-25",
            "2023-06-24",
            "2024-06-22",
            "2025-06-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_all_saints_day(self):
        name = "Alla helgons dag"
        self.assertHolidayName(
            name,
            "2020-10-31",
            "2021-11-06",
            "2022-11-05",
            "2023-11-04",
            "2024-11-02",
            "2025-11-01",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas(self):
        self.assertHolidayName("Juldagen", (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName("Annandag jul", (f"{year}-12-26" for year in self.full_range))

    def test_sundays(self):
        self.assertSundays(Sweden)  # Sundays are considered holidays in Sweden.

    def test_twelfth_night(self):
        name = "Trettondagsafton (från kl. 14.00)"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-01-05" for year in self.full_range))
        self.assertOptionalHolidayName(name, (f"{year}-01-05" for year in self.full_range))

    def test_maundy_thursday(self):
        name = "Skärtorsdagen (från kl. 14.00)"
        self.assertNoHolidayName(name)
        dts = (
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertBankHolidayName(name, dts)
        self.assertOptionalHolidayName(name, dts)
        self.assertBankHolidayName(name, self.full_range)
        self.assertOptionalHolidayName(name, self.full_range)

    def test_walpurgis_night(self):
        name = "Valborgsmässoafton (från kl. 14.00)"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-04-30" for year in self.full_range))
        self.assertOptionalHolidayName(name, (f"{year}-04-30" for year in self.full_range))

    def test_midsummer_eve(self):
        name = "Midsommarafton"
        self.assertNoHolidayName(name)
        dts = (
            "2020-06-19",
            "2021-06-25",
            "2022-06-24",
            "2023-06-23",
            "2024-06-21",
            "2025-06-20",
        )
        self.assertBankHolidayName(name, dts)
        self.assertOptionalHolidayName(name, dts)
        self.assertBankHolidayName(name, self.full_range)
        self.assertOptionalHolidayName(name, self.full_range)

    def test_all_saints_eve(self):
        name = "Allahelgonsafton (från kl. 14.00)"
        self.assertNoHolidayName(name)
        dts = (
            "2020-10-30",
            "2021-11-05",
            "2022-11-04",
            "2023-11-03",
            "2024-11-01",
            "2025-10-31",
        )
        self.assertBankHolidayName(name, dts)
        self.assertOptionalHolidayName(name, dts)
        self.assertBankHolidayName(name, self.full_range)
        self.assertOptionalHolidayName(name, self.full_range)

    def test_christmas_eve(self):
        name = "Julafton"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-24" for year in self.full_range))
        self.assertOptionalHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Nyårsafton"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-31" for year in self.full_range))
        self.assertOptionalHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_day_before_ascension_day(self):
        name = "Dag före Kristi himmelsfärdsdag (från kl. 14.00)"
        self.assertNoHolidayName(name)
        self.assertNoOptionalHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-05-20",
            "2021-05-12",
            "2022-05-25",
            "2023-05-17",
            "2024-05-08",
            "2025-05-28",
        )
        self.assertBankHolidayName(name, self.full_range)

    def test_day_before_midsummer_eve(self):
        name = "Dag före Midsommarafton (från kl. 14.00)"
        self.assertNoHolidayName(name)
        self.assertNoOptionalHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-06-18",
            "2021-06-24",
            "2022-06-23",
            "2023-06-22",
            "2024-06-20",
            "2025-06-19",
        )
        self.assertBankHolidayName(name, self.full_range)

    def test_day_before_whitsun_eve(self):
        name = "Dag före Pingstafton (från kl. 14.00)"
        self.assertNoHolidayName(name)
        self.assertNoOptionalHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-05-29",
            "2021-05-21",
            "2022-06-03",
            "2023-05-26",
            "2024-05-17",
            "2025-06-06",
        )
        self.assertBankHolidayName(name, self.full_range)

    def test_day_before_christmas_eve(self):
        name = "Dag före Julafton (från kl. 14.00)"
        self.assertNoHolidayName(name)
        self.assertNoOptionalHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-23" for year in self.full_range))

    def test_day_before_new_years_eve(self):
        name = "Dag före Nyårsafton (från kl. 14.00)"
        self.assertNoHolidayName(name)
        self.assertNoOptionalHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-30" for year in self.full_range))

    def test_holy_saturday(self):
        name = "Påskafton"
        self.assertNoHolidayName(name)
        self.assertNoBankHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_squeeze_day(self):
        name = "Klämdag"
        self.assertNoHolidayName(name)
        self.assertNoBankHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-05-22",
            "2021-05-14",
            "2022-05-27",
            "2023-05-19",
            "2024-05-10",
            "2025-05-30",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_whitsun_eve(self):
        name = "Pingstafton"
        self.assertNoHolidayName(name)
        self.assertNoBankHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-05-30",
            "2021-05-22",
            "2022-06-04",
            "2023-05-27",
            "2024-05-18",
            "2025-06-07",
        )
        self.assertOptionalHolidayName(name, self.full_range)

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
            ("2022-06-06", "Nationaldagen"),
            ("2022-06-25", "Midsommardagen"),
            ("2022-11-05", "Alla helgons dag"),
            ("2022-12-25", "Juldagen"),
            ("2022-12-26", "Annandag jul"),
        )

    def test_bank_2022(self):
        self.assertHolidays(
            Sweden(categories=BANK, years=2022),
            ("2022-01-05", "Trettondagsafton (från kl. 14.00)"),
            ("2022-04-14", "Skärtorsdagen (från kl. 14.00)"),
            ("2022-04-30", "Valborgsmässoafton (från kl. 14.00)"),
            ("2022-05-25", "Dag före Kristi himmelsfärdsdag (från kl. 14.00)"),
            ("2022-06-03", "Dag före Pingstafton (från kl. 14.00)"),
            ("2022-06-23", "Dag före Midsommarafton (från kl. 14.00)"),
            ("2022-06-24", "Midsommarafton"),
            ("2022-11-04", "Allahelgonsafton (från kl. 14.00)"),
            ("2022-12-23", "Dag före Julafton (från kl. 14.00)"),
            ("2022-12-24", "Julafton"),
            ("2022-12-30", "Dag före Nyårsafton (från kl. 14.00)"),
            ("2022-12-31", "Nyårsafton"),
        )

    def test_optional_2022(self):
        self.assertHolidays(
            Sweden(categories=OPTIONAL, years=2022),
            ("2022-01-05", "Trettondagsafton (från kl. 14.00)"),
            ("2022-04-14", "Skärtorsdagen (från kl. 14.00)"),
            ("2022-04-16", "Påskafton"),
            ("2022-04-30", "Valborgsmässoafton (från kl. 14.00)"),
            ("2022-05-27", "Klämdag"),
            ("2022-06-04", "Pingstafton"),
            ("2022-06-24", "Midsommarafton"),
            ("2022-11-04", "Allahelgonsafton (från kl. 14.00)"),
            ("2022-12-24", "Julafton"),
            ("2022-12-31", "Nyårsafton"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Nyårsdagen"),
            ("2025-01-05", "Söndag; Trettondagsafton (från kl. 14.00)"),
            ("2025-01-06", "Trettondedag jul"),
            ("2025-01-12", "Söndag"),
            ("2025-01-19", "Söndag"),
            ("2025-01-26", "Söndag"),
            ("2025-02-02", "Söndag"),
            ("2025-02-09", "Söndag"),
            ("2025-02-16", "Söndag"),
            ("2025-02-23", "Söndag"),
            ("2025-03-02", "Söndag"),
            ("2025-03-09", "Söndag"),
            ("2025-03-16", "Söndag"),
            ("2025-03-23", "Söndag"),
            ("2025-03-30", "Söndag"),
            ("2025-04-06", "Söndag"),
            ("2025-04-13", "Söndag"),
            ("2025-04-17", "Skärtorsdagen (från kl. 14.00)"),
            ("2025-04-18", "Långfredagen"),
            ("2025-04-19", "Påskafton"),
            ("2025-04-20", "Påskdagen; Söndag"),
            ("2025-04-21", "Annandag påsk"),
            ("2025-04-27", "Söndag"),
            ("2025-04-30", "Valborgsmässoafton (från kl. 14.00)"),
            ("2025-05-01", "Första maj"),
            ("2025-05-04", "Söndag"),
            ("2025-05-11", "Söndag"),
            ("2025-05-18", "Söndag"),
            ("2025-05-25", "Söndag"),
            ("2025-05-28", "Dag före Kristi himmelsfärdsdag (från kl. 14.00)"),
            ("2025-05-29", "Kristi himmelsfärdsdag"),
            ("2025-05-30", "Klämdag"),
            ("2025-06-01", "Söndag"),
            ("2025-06-06", "Dag före Pingstafton (från kl. 14.00); Nationaldagen"),
            ("2025-06-07", "Pingstafton"),
            ("2025-06-08", "Pingstdagen; Söndag"),
            ("2025-06-15", "Söndag"),
            ("2025-06-19", "Dag före Midsommarafton (från kl. 14.00)"),
            ("2025-06-20", "Midsommarafton"),
            ("2025-06-21", "Midsommardagen"),
            ("2025-06-22", "Söndag"),
            ("2025-06-29", "Söndag"),
            ("2025-07-06", "Söndag"),
            ("2025-07-13", "Söndag"),
            ("2025-07-20", "Söndag"),
            ("2025-07-27", "Söndag"),
            ("2025-08-03", "Söndag"),
            ("2025-08-10", "Söndag"),
            ("2025-08-17", "Söndag"),
            ("2025-08-24", "Söndag"),
            ("2025-08-31", "Söndag"),
            ("2025-09-07", "Söndag"),
            ("2025-09-14", "Söndag"),
            ("2025-09-21", "Söndag"),
            ("2025-09-28", "Söndag"),
            ("2025-10-05", "Söndag"),
            ("2025-10-12", "Söndag"),
            ("2025-10-19", "Söndag"),
            ("2025-10-26", "Söndag"),
            ("2025-10-31", "Allahelgonsafton (från kl. 14.00)"),
            ("2025-11-01", "Alla helgons dag"),
            ("2025-11-02", "Söndag"),
            ("2025-11-09", "Söndag"),
            ("2025-11-16", "Söndag"),
            ("2025-11-23", "Söndag"),
            ("2025-11-30", "Söndag"),
            ("2025-12-07", "Söndag"),
            ("2025-12-14", "Söndag"),
            ("2025-12-21", "Söndag"),
            ("2025-12-23", "Dag före Julafton (från kl. 14.00)"),
            ("2025-12-24", "Julafton"),
            ("2025-12-25", "Juldagen"),
            ("2025-12-26", "Annandag jul"),
            ("2025-12-28", "Söndag"),
            ("2025-12-30", "Dag före Nyårsafton (från kl. 14.00)"),
            ("2025-12-31", "Nyårsafton"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-05", "Sunday; Twelfth Night (from 2pm)"),
            ("2025-01-06", "Epiphany"),
            ("2025-01-12", "Sunday"),
            ("2025-01-19", "Sunday"),
            ("2025-01-26", "Sunday"),
            ("2025-02-02", "Sunday"),
            ("2025-02-09", "Sunday"),
            ("2025-02-16", "Sunday"),
            ("2025-02-23", "Sunday"),
            ("2025-03-02", "Sunday"),
            ("2025-03-09", "Sunday"),
            ("2025-03-16", "Sunday"),
            ("2025-03-23", "Sunday"),
            ("2025-03-30", "Sunday"),
            ("2025-04-06", "Sunday"),
            ("2025-04-13", "Sunday"),
            ("2025-04-17", "Maundy Thursday (from 2pm)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-19", "Holy Saturday"),
            ("2025-04-20", "Easter Sunday; Sunday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-27", "Sunday"),
            ("2025-04-30", "Walpurgis Night (from 2pm)"),
            ("2025-05-01", "May Day"),
            ("2025-05-04", "Sunday"),
            ("2025-05-11", "Sunday"),
            ("2025-05-18", "Sunday"),
            ("2025-05-25", "Sunday"),
            ("2025-05-28", "Day before Ascension Day (from 2pm)"),
            ("2025-05-29", "Ascension Day"),
            ("2025-05-30", "Squeeze day"),
            ("2025-06-01", "Sunday"),
            ("2025-06-06", "Day before Whitsun Eve (from 2pm); National Day"),
            ("2025-06-07", "Whitsun Eve"),
            ("2025-06-08", "Sunday; Whit Sunday"),
            ("2025-06-15", "Sunday"),
            ("2025-06-19", "Day before Midsummer Eve (from 2pm)"),
            ("2025-06-20", "Midsummer Eve"),
            ("2025-06-21", "Midsummer Day"),
            ("2025-06-22", "Sunday"),
            ("2025-06-29", "Sunday"),
            ("2025-07-06", "Sunday"),
            ("2025-07-13", "Sunday"),
            ("2025-07-20", "Sunday"),
            ("2025-07-27", "Sunday"),
            ("2025-08-03", "Sunday"),
            ("2025-08-10", "Sunday"),
            ("2025-08-17", "Sunday"),
            ("2025-08-24", "Sunday"),
            ("2025-08-31", "Sunday"),
            ("2025-09-07", "Sunday"),
            ("2025-09-14", "Sunday"),
            ("2025-09-21", "Sunday"),
            ("2025-09-28", "Sunday"),
            ("2025-10-05", "Sunday"),
            ("2025-10-12", "Sunday"),
            ("2025-10-19", "Sunday"),
            ("2025-10-26", "Sunday"),
            ("2025-10-31", "All Saints' Eve (from 2pm)"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-11-02", "Sunday"),
            ("2025-11-09", "Sunday"),
            ("2025-11-16", "Sunday"),
            ("2025-11-23", "Sunday"),
            ("2025-11-30", "Sunday"),
            ("2025-12-07", "Sunday"),
            ("2025-12-14", "Sunday"),
            ("2025-12-21", "Sunday"),
            ("2025-12-23", "Day before Christmas Eve (from 2pm)"),
            ("2025-12-24", "Christmas Eve"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Second Day of Christmas"),
            ("2025-12-28", "Sunday"),
            ("2025-12-30", "Day before New Year's Eve (from 2pm)"),
            ("2025-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2025-01-01", "วันขึ้นปีใหม่"),
            ("2025-01-05", "วันก่อนวันสมโภชพระคริสต์แสดงองค์ (ตั้งแต่ 14:00 น.); วันอาทิตย์"),
            ("2025-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2025-01-12", "วันอาทิตย์"),
            ("2025-01-19", "วันอาทิตย์"),
            ("2025-01-26", "วันอาทิตย์"),
            ("2025-02-02", "วันอาทิตย์"),
            ("2025-02-09", "วันอาทิตย์"),
            ("2025-02-16", "วันอาทิตย์"),
            ("2025-02-23", "วันอาทิตย์"),
            ("2025-03-02", "วันอาทิตย์"),
            ("2025-03-09", "วันอาทิตย์"),
            ("2025-03-16", "วันอาทิตย์"),
            ("2025-03-23", "วันอาทิตย์"),
            ("2025-03-30", "วันอาทิตย์"),
            ("2025-04-06", "วันอาทิตย์"),
            ("2025-04-13", "วันอาทิตย์"),
            ("2025-04-17", "วันพฤหัสศักดิสิทธิ์ (ตั้งแต่ 14:00 น.)"),
            ("2025-04-18", "วันศุกร์ประเสริฐ"),
            ("2025-04-19", "วันเสาร์ศักดิ์สิทธิ์"),
            ("2025-04-20", "วันอาทิตย์; วันอาทิตย์อีสเตอร์"),
            ("2025-04-21", "วันจันทร์อีสเตอร์"),
            ("2025-04-27", "วันอาทิตย์"),
            ("2025-04-30", "คืนวัลเพอร์กิส (ตั้งแต่ 14:00 น.)"),
            ("2025-05-01", "วันเมย์เดย์ (วันแรงงาน)"),
            ("2025-05-04", "วันอาทิตย์"),
            ("2025-05-11", "วันอาทิตย์"),
            ("2025-05-18", "วันอาทิตย์"),
            ("2025-05-25", "วันอาทิตย์"),
            ("2025-05-28", "วันก่อนวันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์ (ตั้งแต่ 14:00 น.)"),
            ("2025-05-29", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2025-05-30", "วันหยุดพิเศษ"),
            ("2025-06-01", "วันอาทิตย์"),
            ("2025-06-06", "วันก่อนวันก่อนวันสมโภชพระจิตเจ้า (ตั้งแต่ 14:00 น.); วันชาติ"),
            ("2025-06-07", "วันก่อนวันสมโภชพระจิตเจ้า"),
            ("2025-06-08", "วันสมโภชพระจิตเจ้า; วันอาทิตย์"),
            ("2025-06-15", "วันอาทิตย์"),
            ("2025-06-19", "วันก่อนวันก่อนวันกลางฤดูร้อน (ตั้งแต่ 14:00 น.)"),
            ("2025-06-20", "วันก่อนวันกลางฤดูร้อน"),
            ("2025-06-21", "วันกลางฤดูร้อน"),
            ("2025-06-22", "วันอาทิตย์"),
            ("2025-06-29", "วันอาทิตย์"),
            ("2025-07-06", "วันอาทิตย์"),
            ("2025-07-13", "วันอาทิตย์"),
            ("2025-07-20", "วันอาทิตย์"),
            ("2025-07-27", "วันอาทิตย์"),
            ("2025-08-03", "วันอาทิตย์"),
            ("2025-08-10", "วันอาทิตย์"),
            ("2025-08-17", "วันอาทิตย์"),
            ("2025-08-24", "วันอาทิตย์"),
            ("2025-08-31", "วันอาทิตย์"),
            ("2025-09-07", "วันอาทิตย์"),
            ("2025-09-14", "วันอาทิตย์"),
            ("2025-09-21", "วันอาทิตย์"),
            ("2025-09-28", "วันอาทิตย์"),
            ("2025-10-05", "วันอาทิตย์"),
            ("2025-10-12", "วันอาทิตย์"),
            ("2025-10-19", "วันอาทิตย์"),
            ("2025-10-26", "วันอาทิตย์"),
            ("2025-10-31", "วันก่อนวันสมโภชนักบุญทั้งหลาย (ตั้งแต่ 14:00 น.)"),
            ("2025-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2025-11-02", "วันอาทิตย์"),
            ("2025-11-09", "วันอาทิตย์"),
            ("2025-11-16", "วันอาทิตย์"),
            ("2025-11-23", "วันอาทิตย์"),
            ("2025-11-30", "วันอาทิตย์"),
            ("2025-12-07", "วันอาทิตย์"),
            ("2025-12-14", "วันอาทิตย์"),
            ("2025-12-21", "วันอาทิตย์"),
            ("2025-12-23", "วันก่อนวันคริสต์มาสอีฟ (ตั้งแต่ 14:00 น.)"),
            ("2025-12-24", "วันคริสต์มาสอีฟ"),
            ("2025-12-25", "วันคริสต์มาส"),
            ("2025-12-26", "วันคริสต์มาสวันที่สอง"),
            ("2025-12-28", "วันอาทิตย์"),
            ("2025-12-30", "วันก่อนวันสิ้นปี (ตั้งแต่ 14:00 น.)"),
            ("2025-12-31", "วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2025-01-01", "Новий рік"),
            ("2025-01-05", "Дванадцята ніч (з 14:00); Неділя"),
            ("2025-01-06", "Богоявлення"),
            ("2025-01-12", "Неділя"),
            ("2025-01-19", "Неділя"),
            ("2025-01-26", "Неділя"),
            ("2025-02-02", "Неділя"),
            ("2025-02-09", "Неділя"),
            ("2025-02-16", "Неділя"),
            ("2025-02-23", "Неділя"),
            ("2025-03-02", "Неділя"),
            ("2025-03-09", "Неділя"),
            ("2025-03-16", "Неділя"),
            ("2025-03-23", "Неділя"),
            ("2025-03-30", "Неділя"),
            ("2025-04-06", "Неділя"),
            ("2025-04-13", "Неділя"),
            ("2025-04-17", "Великий четвер (з 14:00)"),
            ("2025-04-18", "Страсна пʼятниця"),
            ("2025-04-19", "Велика субота"),
            ("2025-04-20", "Великдень; Неділя"),
            ("2025-04-21", "Великодній понеділок"),
            ("2025-04-27", "Неділя"),
            ("2025-04-30", "Вальпургієва ніч (з 14:00)"),
            ("2025-05-01", "Перше травня"),
            ("2025-05-04", "Неділя"),
            ("2025-05-11", "Неділя"),
            ("2025-05-18", "Неділя"),
            ("2025-05-25", "Неділя"),
            ("2025-05-28", "Переддень Вознесіння Господнього (з 14:00)"),
            ("2025-05-29", "Вознесіння Господнє"),
            ("2025-05-30", "Проміжний вихідний"),
            ("2025-06-01", "Неділя"),
            ("2025-06-06", "День перед передднем Трійці (з 14:00); Національний день"),
            ("2025-06-07", "Переддень Трійці"),
            ("2025-06-08", "Неділя; Трійця"),
            ("2025-06-15", "Неділя"),
            ("2025-06-19", "День перед передднем літнього сонцестояння (з 14:00)"),
            ("2025-06-20", "Переддень літнього сонцестояння"),
            ("2025-06-21", "День літнього сонцестояння"),
            ("2025-06-22", "Неділя"),
            ("2025-06-29", "Неділя"),
            ("2025-07-06", "Неділя"),
            ("2025-07-13", "Неділя"),
            ("2025-07-20", "Неділя"),
            ("2025-07-27", "Неділя"),
            ("2025-08-03", "Неділя"),
            ("2025-08-10", "Неділя"),
            ("2025-08-17", "Неділя"),
            ("2025-08-24", "Неділя"),
            ("2025-08-31", "Неділя"),
            ("2025-09-07", "Неділя"),
            ("2025-09-14", "Неділя"),
            ("2025-09-21", "Неділя"),
            ("2025-09-28", "Неділя"),
            ("2025-10-05", "Неділя"),
            ("2025-10-12", "Неділя"),
            ("2025-10-19", "Неділя"),
            ("2025-10-26", "Неділя"),
            ("2025-10-31", "Переддень Дня усіх святих (з 14:00)"),
            ("2025-11-01", "День усіх святих"),
            ("2025-11-02", "Неділя"),
            ("2025-11-09", "Неділя"),
            ("2025-11-16", "Неділя"),
            ("2025-11-23", "Неділя"),
            ("2025-11-30", "Неділя"),
            ("2025-12-07", "Неділя"),
            ("2025-12-14", "Неділя"),
            ("2025-12-21", "Неділя"),
            ("2025-12-23", "День перед Святим вечором (з 14:00)"),
            ("2025-12-24", "Святий вечір"),
            ("2025-12-25", "Різдво Христове"),
            ("2025-12-26", "Другий день Різдва"),
            ("2025-12-28", "Неділя"),
            ("2025-12-30", "День перед передднем Нового року (з 14:00)"),
            ("2025-12-31", "Переддень Нового року"),
        )
