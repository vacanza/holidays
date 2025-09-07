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
    NationalStockExchangeOfIndia,
    XNSE,
    NSE,
)
from tests.common import CommonFinancialTests


class TestNationalStockExchangeOfIndia(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2001, 2050)
        super().setUpClass(NationalStockExchangeOfIndia, years=years, years_non_observed=years)
        cls.nonobs_no_estimated_holidays = NationalStockExchangeOfIndia(
            observed=False, years=years, islamic_show_estimated=False
        )

    def test_market_aliases(self):
        self.assertAliases(NationalStockExchangeOfIndia, XNSE, NSE)

    def test_no_holidays(self):
        self.assertNoHolidays(NationalStockExchangeOfIndia(years=2000))

    def test_new_year(self):
        self.assertNonObservedHolidayName("New Year", (f"{year}-01-01" for year in {2010}))
        self.assertNoHoliday(
            "2025-01-01",
        )

    def test_republic_day(self):
        self.assertNonObservedHolidayName(
            "Republic Day", (f"{year}-01-26" for year in range(2001, 2050))
        )
        self.assertNoHoliday(
            "2025-01-26",
        )

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2001, 2050))

    def test_dr_baba_saheb_ambedkar_jayanti(self):
        self.assertNonObservedHolidayName(
            "Dr. Baba Saheb Ambedkar Jayanti", (f"{year}-04-14" for year in range(2001, 2050))
        )
        self.assertNoHoliday(
            "2024-04-14",
        )

    def test_maharashtra_day(self):
        self.assertNonObservedHolidayName(
            "Maharashtra Day",
            (f"{year}-05-01" for year in range(2001, 2009)),
            (f"{year}-05-01" for year in range(2015, 2050)),
        )
        self.assertNoHoliday(
            "2022-05-01",
        )

    def test_may_day(self):
        self.assertNonObservedHolidayName(
            "May Day", (f"{year}-05-01" for year in range(2010, 2015))
        )
        self.assertNoHoliday(
            "2022-05-01",
        )
        self.assertNoHolidayName("May Day", range(2001, 2010), range(2015, 2050))

    def test_independence_day(self):
        self.assertNonObservedHolidayName(
            "Independence Day", (f"{year}-08-15" for year in range(2001, 2050))
        )
        self.assertNoHoliday(
            "2021-08-15",
        )

    def test_mahatma_gandhi_jayanti(self):
        self.assertNonObservedHolidayName(
            "Mahatma Gandhi Jayanti", (f"{year}-10-02" for year in range(2001, 2050))
        )
        self.assertNoHoliday(
            "2022-10-02",
        )

    def test_christmas_day(self):
        self.assertNonObservedHolidayName(
            "Christmas Day", (f"{year}-12-25" for year in range(2001, 2050))
        )
        self.assertNoHoliday(
            "2022-12-25",
        )

    def test_maha_shivratri(self):
        name = "Maha Shivaratri"
        self.assertNonObservedHolidayName(
            name,
            "2022-03-01",
            "2023-02-18",
            "2024-03-08",
            "2025-02-26",
        )
        self.assertNonObservedHolidayName(name, range(2007, 2036))
        self.assertNoHoliday(
            "2023-02-18",
        )

    def test_holi(self):
        name = "Holi"
        self.assertNonObservedHolidayName(
            name,
            "2022-03-18",
            "2023-03-07",
            "2024-03-25",
            "2025-03-14",
        )
        self.assertNonObservedHolidayName(name, range(2001, 2036))

    def test_mahavir_jayanti(self):
        name = "Mahavir Jayanti"
        self.assertNonObservedHolidayName(
            name,
            "2022-04-14",
            "2023-04-04",
            "2024-04-21",
            "2025-04-10",
        )
        self.assertNonObservedHolidayName(name, range(2006, 2036))
        self.assertNoHoliday(
            "2024-04-21",
        )

    def test_ram_navami(self):
        name = "Ram Navami"
        self.assertNonObservedHolidayName(
            name,
            "2007-03-27",
            "2022-04-10",
            "2023-03-30",
            "2024-04-17",
            "2025-04-06",
        )
        self.assertNonObservedHolidayName(name, range(2006, 2036))
        self.assertNoHoliday(
            "2022-04-10",
            "2025-04-06",
        )

    def test_diwali_balipratipada(self):
        name = "Diwali Balipratipada"
        self.assertNonObservedHolidayName(
            name,
            "2001-11-16",
            "2002-11-06",
            "2022-10-26",
            "2023-11-14",
            "2024-11-02",
            "2025-10-22",
        )
        self.assertNonObservedHolidayName(name, range(2001, 2002), range(2011, 2035))
        self.assertNoHoliday(
            "2024-11-02",
        )

    def test_diwali_laxmi_pujan(self):
        name = "Diwali Laxmi Pujan"
        self.assertNonObservedHolidayName(
            name,
            "2022-10-24",
            "2023-11-12",
            "2024-11-01",
            "2025-10-21",
        )
        self.assertNonObservedHolidayName(name, range(2001, 2036))
        self.assertNoHoliday(
            "2023-11-12",
        )

    def test_dussehra(self):
        name = "Dussehra"
        self.assertNonObservedHolidayName(
            name,
            "2022-10-05",
            "2023-10-24",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertNonObservedHolidayName(name, range(2001, 2036))
        self.assertNoHoliday(
            "2024-10-12",
        )

    def test_ganesh_chaturthi(self):
        name = "Ganesh Chaturthi"
        self.assertNonObservedHolidayName(
            name,
            "2022-08-31",
            "2023-09-19",
            "2024-09-07",
            "2025-08-27",
        )
        self.assertNonObservedHolidayName(name, range(2001, 2036))
        self.assertNoHoliday(
            "2024-09-07",
        )

    def test_guru_nanak_jayanti(self):
        name = "Guru Nanak Jayanti"
        self.assertNonObservedHolidayName(
            name,
            "2022-11-08",
            "2023-11-27",
            "2024-11-15",
            "2025-11-05",
        )
        self.assertNonObservedHolidayName(name, range(2001, 2036))
        self.assertNoHoliday(
            "2017-11-04",
        )

    def test_bhai_bhij(self):
        name = "Bhai Bij"
        self.assertNonObservedHolidayName(
            name,
            "2003-10-26",
            "2005-11-03",
            "2006-10-24",
            "2008-10-30",
            "2009-10-19",
        )
        self.assertNonObservedHolidayName(name, range(2003, 2010))
        self.assertNoHoliday(
            "2010-10-06",
            "2002-11-05",
        )

    def test_buddha_purnima(self):
        name = "Buddha Purnima"
        self.assertNonObservedHolidayName(
            name,
            "2007-05-02",
            "2008-05-19",
        )

    def test_muharram(self):
        name = "Muharram"
        self.assertNonObservedHolidayName(
            name,
            "2001-04-05",
            "2002-03-25",
            "2004-03-02",
            "2007-01-30",
            "2009-01-08",
            "2009-12-28",
            "2010-12-17",
            "2011-12-06",
            "2013-11-14",
            "2014-11-04",
            "2016-10-12",
            "2019-09-10",
            "2021-08-19",
            "2022-08-09",
            "2023-07-29",
            "2024-07-17",
            "2025-07-06",
        )
        self.assertNonObservedHolidayName(
            name, self.nonobs_no_estimated_holidays, range(2001, 2050)
        )
        self.assertNoHoliday(
            "2023-07-29",
            "2025-07-06",
        )

    def test_id_ul_fitr(self):
        name = "Id-Ul-Fitr (Ramadan Eid)"
        self.assertNonObservedHolidayName(
            name,
            "2001-12-17",
            "2003-11-26",
            "2004-11-15",
            "2005-11-05",
            "2006-10-25",
            "2008-10-02",
            "2009-09-21",
            "2011-08-31",
            "2012-08-20",
            "2013-08-09",
            "2014-07-29",
            "2017-06-26",
            "2019-06-05",
            "2020-05-25",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-03-31",
        )
        self.assertNonObservedHolidayName(
            name, self.nonobs_no_estimated_holidays, range(2001, 2050)
        )
        self.assertNoHoliday(
            "2023-04-22",
        )

    def test_bakri_id(self):
        name = "Bakri Id"
        self.assertNonObservedHolidayName(
            name,
            "2001-03-06",
            "2003-02-13",
            "2004-02-02",
            "2006-01-11",
            "2007-01-01",
            "2007-12-21",
            "2008-12-09",
            "2010-11-17",
            "2011-11-07",
            "2013-10-16",
            "2014-10-06",
            "2015-09-25",
            "2016-09-13",
            "2018-08-22",
            "2019-08-12",
            "2021-07-21",
            "2022-07-10",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertNonObservedHolidayName(
            name, self.nonobs_no_estimated_holidays, range(2001, 2050)
        )
        self.assertNoHoliday(
            "2022-07-10",
            "2025-06-07",
        )

    def test_id_e_milad_un_nabi(self):
        name = "Id-E-Milad-Un-Nabi"
        self.assertNonObservedHolidayName(
            name,
            # "2006-04-11",
            "2009-03-10",
        )

        self.assertNoHoliday(
            "2005-04-21",
        )

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
            ("2023-04-14", "Dr. B. R. Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-14", "Diwali"),
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
