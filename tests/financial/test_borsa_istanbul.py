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
        super().setUpClass(BorsaIstanbul)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_special_holidays(self):
        self.assertHolidayName(
            "Piyasa Kapalı (Deprem)",
            "2023-02-08",
            "2023-02-09",
            "2023-02-10",
            "2023-02-13",
            "2023-02-14",
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Yılbaşı"),
            ("2024-04-10", "Ramazan Bayramı"),
            ("2024-04-11", "Ramazan Bayramı"),
            ("2024-04-12", "Ramazan Bayramı"),
            ("2024-04-23", "Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2024-05-01", "Emek ve Dayanışma Günü"),
            ("2024-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2024-06-16", "Kurban Bayramı"),
            ("2024-06-17", "Kurban Bayramı"),
            ("2024-06-18", "Kurban Bayramı"),
            ("2024-06-19", "Kurban Bayramı"),
            ("2024-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2024-08-30", "Zafer Bayramı"),
            ("2024-10-29", "Cumhuriyet Bayramı"),
        )

    def test_2024_half_day(self):
        self.assertHalfDayHolidaysInYear(
            2024,
            ("2024-04-09", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2024-06-15", "Kurban Bayramı (saat 13.00'ten)"),
            ("2024-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Yılbaşı"),
            ("2023-02-08", "Piyasa Kapalı (Deprem)"),
            ("2023-02-09", "Piyasa Kapalı (Deprem)"),
            ("2023-02-10", "Piyasa Kapalı (Deprem)"),
            ("2023-02-13", "Piyasa Kapalı (Deprem)"),
            ("2023-02-14", "Piyasa Kapalı (Deprem)"),
            ("2023-04-20", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2023-04-21", "Ramazan Bayramı"),
            ("2023-04-22", "Ramazan Bayramı"),
            ("2023-04-23", "Ramazan Bayramı; Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2023-05-01", "Emek ve Dayanışma Günü"),
            ("2023-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2023-06-27", "Kurban Bayramı (saat 13.00'ten)"),
            ("2023-06-28", "Kurban Bayramı"),
            ("2023-06-29", "Kurban Bayramı"),
            ("2023-06-30", "Kurban Bayramı"),
            ("2023-07-01", "Kurban Bayramı"),
            ("2023-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2023-08-30", "Zafer Bayramı"),
            ("2023-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
            ("2023-10-29", "Cumhuriyet Bayramı"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-02-08", "Market Closed (Earthquake)"),
            ("2023-02-09", "Market Closed (Earthquake)"),
            ("2023-02-10", "Market Closed (Earthquake)"),
            ("2023-02-13", "Market Closed (Earthquake)"),
            ("2023-02-14", "Market Closed (Earthquake)"),
            ("2023-04-20", "Eid al-Fitr (from 1pm)"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr; National Sovereignty and Children's Day"),
            ("2023-05-01", "Labour and Solidarity Day"),
            ("2023-05-19", "Commemoration of Atatürk, Youth and Sports Day"),
            ("2023-06-27", "Eid al-Adha (from 1pm)"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-01", "Eid al-Adha"),
            ("2023-07-15", "Democracy and National Unity Day"),
            ("2023-08-30", "Victory Day"),
            ("2023-10-28", "Republic Day (from 1pm)"),
            ("2023-10-29", "Republic Day"),
        )
