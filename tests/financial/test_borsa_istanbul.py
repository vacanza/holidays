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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import _timedelta
from holidays.financial.borsa_istanbul import BorsaIstanbul
from tests.common import CommonFinancialTests


class TestBorsaIstanbul(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BorsaIstanbul)

    def test_special_holidays(self):
        self.assertHoliday(
            "2023-02-08",
            "2023-02-09",
            "2023-02-10",
            "2023-02-13",
            "2023-02-14",
        )

    def test_new_years_day(self):
        self.assertHolidayName("Yılbaşı", (f"{year}-01-01" for year in self.full_range))

    def test_national_sovereignty_and_childrens_day(self):
        name = "Ulusal Egemenlik ve Çocuk Bayramı"
        self.assertHolidayName(name, (f"{year}-04-23" for year in self.full_range))

    def test_labor_day(self):
        name = "Emek ve Dayanışma Günü"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2009, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2009))

    def test_ataturk_youth_and_sports_day(self):
        name = "Atatürk'ü Anma, Gençlik ve Spor Bayramı"
        self.assertHolidayName(name, (f"{year}-05-19" for year in self.full_range))

    def test_democracy_and_national_unity_day(self):
        name = "Demokrasi ve Millî Birlik Günü"
        self.assertHolidayName(name, (f"{year}-07-15" for year in range(2017, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2017))

    def test_victory_day(self):
        self.assertHolidayName("Zafer Bayramı", (f"{year}-08-30" for year in self.full_range))

    def test_republic_day(self):
        name = "Cumhuriyet Bayramı"
        self.assertHolidayName(name, (f"{year}-10-29" for year in self.full_range))
        self.assertHalfDayHolidayName(
            f"{name} (saat 13.00'ten)", (f"{year}-10-28" for year in self.full_range)
        )

    def test_ramadan_feast(self):
        name = "Ramazan Bayramı"
        for ymd in (
            (2000, 1, 8),
            (2000, 12, 27),
            (2010, 9, 9),
            (2018, 6, 15),
            (2019, 6, 4),
            (2020, 5, 24),
            (2021, 5, 13),
            (2022, 5, 2),
            (2023, 4, 21),
            (2024, 4, 10),
            (2025, 3, 30),
        ):
            dt = date(*ymd)
            self.assertHolidayName(name, dt, _timedelta(dt, +1), _timedelta(dt, +2))
            self.assertHalfDayHolidayName(f"{name} (saat 13.00'ten)", _timedelta(dt, -1))
        exception_years = {2000, 2033}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, (year for year in self.full_range if year not in exception_years)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, exception_years)

    def test_feast_of_the_sacrifice(self):
        name = "Kurban Bayramı"
        for ymd in (
            (2006, 1, 10),
            (2006, 12, 31),
            (2010, 11, 16),
            (2018, 8, 21),
            (2019, 8, 11),
            (2020, 7, 31),
            (2021, 7, 20),
            (2022, 7, 9),
            (2023, 6, 28),
            (2024, 6, 16),
            (2025, 6, 6),
        ):
            dt = date(*ymd)
            self.assertHolidayName(
                name, dt, _timedelta(dt, +1), _timedelta(dt, +2), _timedelta(dt, +3)
            )
            self.assertHalfDayHolidayName(f"{name} (saat 13.00'ten)", _timedelta(dt, -1))
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 4, (year for year in self.full_range if year not in {2006, 2007, 2039})
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 5, {2006})
        self.assertIslamicNoEstimatedHolidayNameCount(name, 7, {2007})
        self.assertIslamicNoEstimatedHolidayNameCount(name, 8, {2039})

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Yılbaşı"),
            ("2025-03-30", "Ramazan Bayramı"),
            ("2025-03-31", "Ramazan Bayramı"),
            ("2025-04-01", "Ramazan Bayramı"),
            ("2025-04-23", "Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2025-05-01", "Emek ve Dayanışma Günü"),
            ("2025-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2025-06-06", "Kurban Bayramı"),
            ("2025-06-07", "Kurban Bayramı"),
            ("2025-06-08", "Kurban Bayramı"),
            ("2025-06-09", "Kurban Bayramı"),
            ("2025-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2025-08-30", "Zafer Bayramı"),
            ("2025-10-29", "Cumhuriyet Bayramı"),
        )

    def test_2025_half_day(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-03-29", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2025-06-05", "Kurban Bayramı (saat 13.00'ten)"),
            ("2025-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Yılbaşı"),
            ("2025-03-29", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2025-03-30", "Ramazan Bayramı"),
            ("2025-03-31", "Ramazan Bayramı"),
            ("2025-04-01", "Ramazan Bayramı"),
            ("2025-04-23", "Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2025-05-01", "Emek ve Dayanışma Günü"),
            ("2025-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2025-06-05", "Kurban Bayramı (saat 13.00'ten)"),
            ("2025-06-06", "Kurban Bayramı"),
            ("2025-06-07", "Kurban Bayramı"),
            ("2025-06-08", "Kurban Bayramı"),
            ("2025-06-09", "Kurban Bayramı"),
            ("2025-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2025-08-30", "Zafer Bayramı"),
            ("2025-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
            ("2025-10-29", "Cumhuriyet Bayramı"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-29", "Eid al-Fitr (from 1pm)"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-01", "Eid al-Fitr"),
            ("2025-04-23", "National Sovereignty and Children's Day"),
            ("2025-05-01", "Labour and Solidarity Day"),
            ("2025-05-19", "Commemoration of Atatürk, Youth and Sports Day"),
            ("2025-06-05", "Eid al-Adha (from 1pm)"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-08", "Eid al-Adha"),
            ("2025-06-09", "Eid al-Adha"),
            ("2025-07-15", "Democracy and National Unity Day"),
            ("2025-08-30", "Victory Day"),
            ("2025-10-28", "Republic Day (from 1pm)"),
            ("2025-10-29", "Republic Day"),
        )
