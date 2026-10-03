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

from holidays.financial.borsa_istanbul import BorsaIstanbul
from tests.common import CommonFinancialTests


class TestBorsaIstanbul(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the BorsaIstanbul test fixture."""
        super().setUpClass(BorsaIstanbul)

    def test_code(self):
        """Verify market and country attributes."""
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_special_holidays(self):
        """Verify the 2023 earthquake market suspension."""
        # Inherited one-off public holiday.
        self.assertHolidayName("Genel tati̇l", "1999-12-31")
        # Five-day market suspension after the earthquakes.
        self.assertHoliday(
            "2023-02-08",
            "2023-02-09",
            "2023-02-10",
            "2023-02-13",
            "2023-02-14",
        )

    def test_start_year(self):
        """Verify holidays are observed from 1986 onwards."""
        self.assertNoHolidays(BorsaIstanbul(years=1985))
        self.assertHolidayName("Yılbaşı", "1986-01-01")

    def test_labor_day_gap(self):
        """Verify Labour Day was not a holiday in 2000 but was in 2010."""
        # May 1st wasn't a public holiday in Turkey in 1981-2008.
        self.assertNoHoliday("2000-05-01")
        self.assertHolidayName("Emek ve Dayanışma Günü", "2010-05-01")

    def test_2025(self):
        """Verify the full 2025 holiday list."""
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
        """Verify 2025 half-day holidays."""
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-03-29", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2025-06-05", "Kurban Bayramı (saat 13.00'ten)"),
            ("2025-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
        )

    def test_l10n_default(self):
        """Verify default (Turkish) holiday names."""
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
        """Verify English holiday names."""
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
