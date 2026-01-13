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

from holidays.constants import HALF_DAY
from holidays.countries.estonia import Estonia
from tests.common import CommonCountryTests


class TestEstonia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Estonia)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Estonia(categories=HALF_DAY, years=range(self.start_year, 2001)))

    def test_new_years_day(self):
        self.assertHolidayName("uusaasta", (f"{year}-01-01" for year in self.full_range))

    def test_independence_day(self):
        self.assertHolidayName("iseseisvuspäev", (f"{year}-02-24" for year in self.full_range))

    def test_good_friday(self):
        name = "suur reede"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1994, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1994))

    def test_easter_sunday(self):
        name = "ülestõusmispühade 1. püha"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(1994, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1994))

    def test_may_day(self):
        name_1991 = "töörahva rahvusvahelise solidaarsuse päev"
        name_1994 = "kevadpüha"
        self.assertHolidayName(
            name_1991, (f"{year}-05-01" for year in range(self.start_year, 1994))
        )
        self.assertHolidayName(name_1994, (f"{year}-05-01" for year in range(1994, self.end_year)))
        self.assertNoHolidayName(name_1991, range(1994, self.end_year))
        self.assertNoHolidayName(name_1994, range(self.start_year, 1994))

    def test_whit_sunday(self):
        name = "nelipühade 1. püha"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, range(1994, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1994))

    def test_victory_day(self):
        self.assertHolidayName("võidupüha", (f"{year}-06-23" for year in self.full_range))

    def test_midsummer_day(self):
        self.assertHolidayName("jaanipäev", (f"{year}-06-24" for year in self.full_range))

    def test_restoration_of_independence_day(self):
        name = "taasiseseisvumispäev"
        self.assertHolidayName(name, (f"{year}-08-20" for year in range(1998, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1998))

    def test_day_of_declaration_of_sovereignty(self):
        name = "taassünnipäev"
        self.assertHolidayName(name, (f"{year}-11-16" for year in range(self.start_year, 1994)))
        self.assertNoHolidayName(name, range(1994, self.end_year))

    def test_christmas_eve(self):
        name = "jõululaupäev"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(2005, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2005))

    def test_christmas_day(self):
        self.assertHolidayName("esimene jõulupüha", (f"{year}-12-25" for year in self.full_range))

    def test_second_christmas_day(self):
        self.assertHolidayName("teine jõulupüha", (f"{year}-12-26" for year in self.full_range))

    def test_pre_holiday_day(self):
        name = "pühade-eelne päev (tööpäev lüheneb 3 tunni võrra)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            (f"{year}-02-23" for year in range(2001, self.end_year)),
            (f"{year}-06-22" for year in range(2001, self.end_year)),
            (f"{year}-12-24" for year in range(2001, 2005)),
            (f"{year}-12-23" for year in range(2005, self.end_year)),
            (f"{year}-12-31" for year in range(2001, self.end_year)),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "uusaasta"),
            ("2022-02-23", "pühade-eelne päev (tööpäev lüheneb 3 tunni võrra)"),
            ("2022-02-24", "iseseisvuspäev"),
            ("2022-04-15", "suur reede"),
            ("2022-04-17", "ülestõusmispühade 1. püha"),
            ("2022-05-01", "kevadpüha"),
            ("2022-06-05", "nelipühade 1. püha"),
            ("2022-06-22", "pühade-eelne päev (tööpäev lüheneb 3 tunni võrra)"),
            ("2022-06-23", "võidupüha"),
            ("2022-06-24", "jaanipäev"),
            ("2022-08-20", "taasiseseisvumispäev"),
            ("2022-12-23", "pühade-eelne päev (tööpäev lüheneb 3 tunni võrra)"),
            ("2022-12-24", "jõululaupäev"),
            ("2022-12-25", "esimene jõulupüha"),
            ("2022-12-26", "teine jõulupüha"),
            ("2022-12-31", "pühade-eelne päev (tööpäev lüheneb 3 tunni võrra)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-23", "Pre-holiday day (workday shortened by 3 hours)"),
            ("2022-02-24", "Independence Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-01", "May Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-22", "Pre-holiday day (workday shortened by 3 hours)"),
            ("2022-06-23", "Victory Day"),
            ("2022-06-24", "Midsummer Day"),
            ("2022-08-20", "Independence Restoration Day"),
            ("2022-12-23", "Pre-holiday day (workday shortened by 3 hours)"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            ("2022-12-31", "Pre-holiday day (workday shortened by 3 hours)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-02-23", "Передсвятковий робочий день (скорочений на 3 години)"),
            ("2022-02-24", "День незалежності"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-05-01", "День весни"),
            ("2022-06-05", "Трійця"),
            ("2022-06-22", "Передсвятковий робочий день (скорочений на 3 години)"),
            ("2022-06-23", "День Перемоги"),
            ("2022-06-24", "День літнього сонцестояння"),
            ("2022-08-20", "День відновлення незалежності"),
            ("2022-12-23", "Передсвятковий робочий день (скорочений на 3 години)"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
            ("2022-12-31", "Передсвятковий робочий день (скорочений на 3 години)"),
        )
