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

from holidays.financial.india_national_stock_exchange import (
    NSE,
    XNSE,
    IndiaNationalStockExchange,
)
from tests.common import CommonFinancialTests


class TestIndiaNationalStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IndiaNationalStockExchange, years=range(1994, 2100))

    def test_market_aliases(self):
        self.assertAliases(IndiaNationalStockExchange, NSE, XNSE)

    def test_no_holidays(self):
        self.assertNoHolidays(IndiaNationalStockExchange(years=1993))

    def test_republic_day(self):
        name = "Republic Day"
        self.assertHolidayName(
            name,
            "2023-01-26",
            "2024-01-26",
        )

    def test_mahashivratri(self):
        name = "Mahashivratri"
        self.assertHolidayName(
            name,
            "2024-03-08",
            "2025-02-26",
        )

    def test_holi(self):
        name = "Holi"
        self.assertHolidayName(
            name,
            "2023-03-08",
            "2024-03-25",
            "2025-03-14",
        )

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )

    def test_maharashtra_day(self):
        name = "Maharashtra Day"
        self.assertHolidayName(
            name,
            "2023-05-01",
            "2024-05-01",
            "2025-05-01",
        )

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(
            name,
            "2023-08-15",
            "2024-08-15",
            "2025-08-15",
        )

    def test_gandhi_jayanti(self):
        name = "Mahatma Gandhi Jayanti"
        self.assertHolidayName(
            name,
            "2023-10-02",
            "2024-10-02",
        )

    def test_diwali(self):
        self.assertHolidayName("Diwali-Balipratipada", "2023-11-13", "2024-11-01")
        self.assertHolidayName("Diwali Laxmi Pujan", "2025-10-21")
        self.assertHolidayName("Diwali Balipratipada", "2025-10-22")

    def test_christmas(self):
        name = "Christmas"
        self.assertHolidayName(
            name,
            "2023-12-25",
            "2024-12-25",
        )
        self.assertHolidayName("Christmas Day", "2025-12-25")

    def test_2023(self):
        self.assertHolidays(
            IndiaNationalStockExchange(years=2023),
            ("2023-01-26", "Republic Day"),
            ("2023-03-08", "Holi"),
            ("2023-03-30", "Ram Navami"),
            ("2023-04-04", "Mahavir Jayanti"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-29", "Bakri Id"),
            ("2023-07-29", "Muharram"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Mahatma Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-13", "Diwali-Balipratipada"),
            ("2023-11-27", "Gurunanak Jayanti"),
            ("2023-12-25", "Christmas"),
        )

    def test_2024(self):
        self.assertHolidays(
            IndiaNationalStockExchange(years=2024),
            ("2024-01-26", "Republic Day"),
            ("2024-03-08", "Mahashivratri"),
            ("2024-03-25", "Holi"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-11", "Id-Ul-Fitr (Ramadan Eid)"),
            ("2024-04-17", "Shri Ram Navmi"),
            ("2024-05-01", "Maharashtra Day"),
            ("2024-06-17", "Bakri Id"),
            ("2024-08-15", "Independence Day"),
            ("2024-10-02", "Mahatma Gandhi Jayanti"),
            ("2024-10-12", "Dussehra"),
            ("2024-11-01", "Diwali-Balipratipada"),
            ("2024-11-15", "Gurunanak Jayanti"),
            ("2024-12-25", "Christmas"),
        )

    def test_2025(self):
        self.assertHolidays(
            IndiaNationalStockExchange(years=2025),
            ("2025-02-26", "Mahashivratri"),
            ("2025-03-14", "Holi"),
            ("2025-03-31", "Id-Ul-Fitr (Ramadan Eid)"),
            ("2025-04-10", "Shri Mahavir Jayanti"),
            ("2025-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-01", "Maharashtra Day"),
            ("2025-08-15", "Independence Day"),
            ("2025-08-27", "Ganesh Chaturthi"),
            ("2025-10-02", "Mahatma Gandhi Jayanti/Dussehra"),
            ("2025-10-21", "Diwali Laxmi Pujan"),
            ("2025-10-22", "Diwali Balipratipada"),
            ("2025-11-05", "Prakash Gurpurb Sri Guru Nanak Dev"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-26", "Republic Day"),
            ("2023-03-08", "Holi"),
            ("2023-03-30", "Ram Navami"),
            ("2023-04-04", "Mahavir Jayanti"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-29", "Bakri Id"),
            ("2023-07-29", "Muharram"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Mahatma Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-13", "Diwali-Balipratipada"),
            ("2023-11-27", "Gurunanak Jayanti"),
            ("2023-12-25", "Christmas"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-26", "Republic Day"),
            ("2023-03-08", "Holi"),
            ("2023-03-30", "Ram Navami"),
            ("2023-04-04", "Mahavir Jayanti"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-29", "Bakri Id"),
            ("2023-07-29", "Muharram"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Mahatma Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-13", "Diwali-Balipratipada"),
            ("2023-11-27", "Guru Nanak's Birthday"),
            ("2023-12-25", "Christmas"),
        )

    def test_l10n_hi(self):
        self.assertLocalizedHolidays(
            "hi",
            ("2023-01-26", "गणतंत्र दिवस"),
            ("2023-03-08", "होली"),
            ("2023-03-30", "राम नवमी"),
            ("2023-04-04", "महावीर जयंती"),
            ("2023-04-07", "गुड फ्राइडे"),
            ("2023-04-14", "डॉ. बाबा साहेब अम्बेडकर जयंती"),
            ("2023-05-01", "महाराष्ट्र दिवस"),
            ("2023-06-29", "बकरी ईद"),
            ("2023-07-29", "मुहर्रम"),
            ("2023-08-15", "स्वतंत्रता दिवस"),
            ("2023-09-19", "गणेश चतुर्थी"),
            ("2023-10-02", "महात्मा गांधी जयंती"),
            ("2023-10-24", "दशहरा"),
            ("2023-11-13", "दिवाली-बलिप्रतिपदा"),
            ("2023-11-27", "गुरुनानक जयंती"),
            ("2023-12-25", "क्रिसमस"),
        )
