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

from holidays.financial.national_stock_exchange_of_india import (
    NSE,
    XNSE,
    NationalStockExchangeOfIndia,
)
from tests.common import CommonFinancialTests


class TestNationalStockExchangeOfIndia(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NationalStockExchangeOfIndia, years=range(2022, 2026))

    def test_market_aliases(self):
        self.assertAliases(NationalStockExchangeOfIndia, NSE, XNSE)

    def test_no_holidays(self):
        self.assertNoHolidays(NationalStockExchangeOfIndia(years=1993))

    def test_republic_day(self):
        name = "Republic Day"
        dt = (
            "2022-01-26",
            "2023-01-26",
            "2024-01-26",
            "2026-01-26",
        )
        self.assertHolidayName(name, dt)
        no_dt = ("2025-01-26",)
        self.assertNoHoliday(no_dt)

    def test_good_friday(self):
        name = "Good Friday"
        dt = ("2022-04-15", "2023-04-07", "2024-03-29", "2025-04-18")
        self.assertHolidayName(name, dt)

    def test_dr_baba_saheb_ambedkar_jayanti(self):
        name = "Dr. Baba Saheb Ambedkar Jayanti"
        dt = (
            "2022-04-14",
            "2023-04-14",
            "2025-04-14",
            "2026-04-14",
        )
        self.assertHolidayName(name, dt)
        no_dt = ("2024-04-14",)
        self.assertNoHoliday(no_dt)

    def test_maharashtra_day(self):
        name = "Maharashtra Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2023, 2026)))
        dt = ("2022-05-01",)
        self.assertNoHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(2022, 2026)))

    def test_mahatma_gandhi_jayanti(self):
        name = "Mahatma Gandhi Jayanti"
        self.assertHolidayName(name, (f"{year}-10-02" for year in range(2023, 2026)))
        dt = ("2022-10-02",)
        self.assertNoHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2023, 2026)))
        dt = ("2022-12-25",)
        self.assertNoHoliday(dt)

    def test_mahashivratri(self):
        name = "Maha Shivaratri"
        dt = (
            "2022-03-01",
            "2024-03-08",
            "2025-02-26",
        )
        self.assertHolidayName(name, dt)
        no_dt = ("2023-02-18",)
        self.assertNoHoliday(no_dt)

    def test_holi(self):
        name = "Holi"
        dt = (
            "2022-03-18",
            "2023-03-07",
            "2024-03-25",
            "2025-03-14",
        )
        self.assertHolidayName(f"{name}", dt)

    def test_mahavir_jayanti(self):
        name = "Mahavir Jayanti"
        dt = (
            "2022-04-14",
            "2023-04-04",
            "2025-04-10",
        )
        self.assertHolidayName(name, dt)
        no_dt = ("2024-04-21",)
        self.assertNoHoliday(no_dt)

    def test_ram_navami(self):
        name = "Ram Navami"
        dt = (
            "2023-03-30",
            "2024-04-17",
        )
        self.assertHolidayName(name, dt)
        no_dt = (
            "2022-04-10",
            "2025-04-06",
        )
        self.assertNoHoliday(no_dt)

    def test_bhai_dooj_and_govardhan_puja(self):
        name = "Diwali Balipratipada"
        bhai_dooj_dt = (
            "2022-10-26",
            "2023-11-14",
        )
        self.assertHolidayName(name, bhai_dooj_dt)
        govardhan_puja_dt = ("2025-10-22",)
        self.assertHolidayName(name, govardhan_puja_dt)

    def test_diwali_laxmi_pujan(self):
        name = "Diwali Laxmi Pujan"
        dt = (
            "2022-10-24",
            "2024-11-01",
            "2025-10-21",
        )
        self.assertHolidayName(name, dt)

    def test_dussehra(self):
        name = "Dussehra"
        dt = (
            "2022-10-05",
            "2023-10-24",
            "2025-10-02",
        )
        self.assertHolidayName(name, dt)

    def test_ganesh_chaturthi(self):
        name = "Ganesh Chaturthi"
        dt = (
            "2023-09-19",
            "2025-08-27",
        )
        self.assertHolidayName(name, dt)

    def test_guru_nanak_jayanti(self):
        name = "Guru Nanak Jayanti"
        dt = (
            "2022-11-08",
            "2023-11-27",
            "2024-11-15",
            "2025-11-05",
        )
        self.assertHolidayName(name, dt)

    def test_2023(self):
        self.assertHolidays(
            NationalStockExchangeOfIndia(years=2023),
            ("2023-01-26", "Republic Day"),
            ("2023-03-07", "Holi"),
            ("2023-03-30", "Ram Navami"),
            ("2023-04-04", "Mahavir Jayanti"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-28", "Bakri Id"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Mahatma Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-14", "Diwali Balipratipada"),
            ("2023-11-27", "Guru Nanak Jayanti"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            NationalStockExchangeOfIndia(years=2024),
            ("2024-01-26", "Republic Day"),
            ("2024-03-08", "Maha Shivaratri"),
            ("2024-03-25", "Holi"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-11", "Id-Ul-Fitr (Ramadan Eid)"),
            ("2024-04-17", "Ram Navami"),
            ("2024-05-01", "Maharashtra Day"),
            ("2024-06-17", "Bakri Id"),
            ("2024-07-17", "Muharram"),
            ("2024-08-15", "Independence Day"),
            ("2024-10-02", "Mahatma Gandhi Jayanti"),
            ("2024-11-01", "Diwali Laxmi Pujan"),
            ("2024-11-15", "Guru Nanak Jayanti"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_2025(self):
        self.assertHolidays(
            NationalStockExchangeOfIndia(years=2025),
            ("2025-02-26", "Maha Shivaratri"),
            ("2025-03-14", "Holi"),
            ("2025-03-31", "Id-Ul-Fitr (Ramadan Eid)"),
            ("2025-04-10", "Mahavir Jayanti"),
            ("2025-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-01", "Maharashtra Day"),
            ("2025-08-15", "Independence Day"),
            ("2025-08-27", "Ganesh Chaturthi"),
            ("2025-10-02", "Dussehra; Mahatma Gandhi Jayanti"),
            ("2025-10-21", "Diwali Laxmi Pujan"),
            ("2025-10-22", "Diwali Balipratipada"),
            ("2025-11-05", "Guru Nanak Jayanti"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-26", "Republic Day"),
            ("2023-03-07", "Holi"),
            ("2023-03-30", "Ram Navami"),
            ("2023-04-04", "Mahavir Jayanti"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-28", "Bakri Id"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Mahatma Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-14", "Diwali Balipratipada"),
            ("2023-11-27", "Guru Nanak Jayanti"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-26", "Republic Day"),
            ("2023-03-07", "Holi"),
            ("2023-03-30", "Ram Navami"),
            ("2023-04-04", "Mahavir Jayanti"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Mahatma Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-14", "Diwali Balipratipada"),
            ("2023-11-27", "Guru Nanak Jayanti"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_hi(self):
        self.assertLocalizedHolidays(
            "hi",
            ("2023-01-26", "गणतंत्र दिवस"),
            ("2023-03-07", "होली"),
            ("2023-03-30", "राम नवमी"),
            ("2023-04-04", "महावीर जयंती"),
            ("2023-04-07", "गुड फ्राइडे"),
            ("2023-04-14", "डॉ. बाबा साहेब अम्बेडकर जयंती"),
            ("2023-05-01", "महाराष्ट्र दिवस"),
            ("2023-06-28", "बकरी ईद"),
            ("2023-08-15", "स्वतंत्रता दिवस"),
            ("2023-09-19", "गणेश चतुर्थी"),
            ("2023-10-02", "महात्मा गांधी जयंती"),
            ("2023-10-24", "दशहरा"),
            ("2023-11-14", "दिवाली बलिप्रतिपदा"),
            ("2023-11-27", "गुरु नानक जयंती"),
            ("2023-12-25", "क्रिसमस डे"),
        )

    def test_not_observed(self):
        self.assertNoHoliday(
            "2022-05-01",
            "2024-04-14",
            "2022-10-02",
        )
