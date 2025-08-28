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
        years = range(2001, 2050)
        super().setUpClass(NationalStockExchangeOfIndia, years=years)
        cls.nonobs_no_estimated_holidays = NationalStockExchangeOfIndia(
            observed=False, years=years, islamic_show_estimated=False
        )

    def test_market_aliases(self):
        self.assertAliases(NationalStockExchangeOfIndia, NSE, XNSE)

    def test_no_holidays(self):
        self.assertNoHolidays(NationalStockExchangeOfIndia(years=2000))

    def test_republic_day(self):
        name = "Republic Day"
        self.assertNonObservedHolidayName(name, (f"{year}-01-26" for year in range(2001, 2050)))
        no_dt = ("2025-01-26",)
        self.assertNoHolidayName(name, no_dt)

    def test_good_friday(self):
        name = "Good Friday"
        dt = (
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
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
        self.assertNonObservedHolidayName(name, (f"{year}-05-01" for year in range(2001, 2050)))
        dt = ("2022-05-01",)
        self.assertNoHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertNonObservedHolidayName(name, (f"{year}-08-15" for year in range(2001, 2050)))

    def test_mahatma_gandhi_jayanti(self):
        name = "Mahatma Gandhi Jayanti"
        self.assertNonObservedHolidayName(name, (f"{year}-10-02" for year in range(2001, 2050)))
        dt = ("2022-10-02",)
        self.assertNoHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in range(2001, 2050)))
        dt = ("2022-12-25",)
        self.assertNoHoliday(dt)

    def test_mahashivratri(self):
        name = "Maha Shivaratri"
        dt = (
            "2001-02-21",
            "2002-03-12",
            "2003-03-01",
            "2004-02-18",
            "2005-03-08",
            "2006-02-26",
            "2007-02-16",
            "2008-03-06",
            "2009-02-23",
            "2010-02-12",
            "2011-03-02",
            "2012-02-20",
            "2013-03-10",
            "2014-02-27",
            "2015-02-17",
            "2016-03-07",
            "2017-02-24",
            "2018-02-13",
            "2019-03-04",
            "2020-02-21",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2024-03-08",
            "2025-02-26",
            "2026-02-15",
            "2027-03-06",
            "2028-02-23",
            "2029-02-11",
            "2030-03-02",
            "2031-02-20",
            "2032-03-10",
            "2033-02-27",
            "2034-02-17",
            "2035-03-08",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2036))
        no_dt = ("2023-02-18",)
        self.assertNoHolidayName(name, no_dt)

    def test_holi(self):
        name = "Holi"
        dt = (
            "2001-03-10",
            "2002-03-29",
            "2003-03-18",
            "2004-03-07",
            "2005-03-26",
            "2006-03-15",
            "2007-03-04",
            "2008-03-22",
            "2009-03-11",
            "2010-03-01",
            "2011-03-20",
            "2012-03-08",
            "2013-03-27",
            "2014-03-17",
            "2015-03-06",
            "2016-03-24",
            "2017-03-13",
            "2018-03-02",
            "2019-03-21",
            "2020-03-10",
            "2021-03-29",
            "2022-03-18",
            "2023-03-07",
            "2024-03-25",
            "2025-03-14",
            "2026-03-04",
            "2027-03-22",
            "2028-03-11",
            "2029-03-01",
            "2030-03-20",
            "2031-03-09",
            "2032-03-27",
            "2033-03-16",
            "2034-03-05",
            "2035-03-24",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2036))

    def test_mahavir_jayanti(self):
        name = "Mahavir Jayanti"
        dt = (
            "2001-04-06",
            "2002-04-25",
            "2003-04-15",
            "2004-04-03",
            "2005-04-22",
            "2006-04-11",
            "2007-03-31",
            "2008-04-18",
            "2009-04-07",
            "2010-04-28",
            "2011-04-16",
            "2012-04-05",
            "2013-04-24",
            "2014-04-13",
            "2015-04-02",
            "2016-04-20",
            "2017-04-09",
            "2018-03-29",
            "2019-04-17",
            "2020-04-06",
            "2021-04-25",
            "2022-04-14",
            "2023-04-04",
            "2024-04-21",
            "2025-04-10",
            "2026-03-31",
            "2027-04-18",
            "2028-04-07",
            "2029-04-26",
            "2030-04-16",
            "2031-04-05",
            "2032-04-23",
            "2033-04-12",
            "2034-04-01",
            "2035-04-20",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2036))
        no_dt = ("2024-04-21",)
        self.assertNoHoliday(no_dt)

    def test_ram_navami(self):
        name = "Ram Navami"
        dt = (
            "2001-04-02",
            "2002-04-21",
            "2003-04-11",
            "2004-03-30",
            "2005-04-18",
            "2006-04-06",
            "2007-03-26",
            "2008-04-13",
            "2009-04-03",
            "2010-03-24",
            "2011-04-12",
            "2012-04-01",
            "2013-04-19",
            "2014-04-08",
            "2015-03-28",
            "2016-04-15",
            "2017-04-04",
            "2018-03-25",
            "2019-04-13",
            "2020-04-02",
            "2021-04-21",
            "2022-04-10",
            "2023-03-30",
            "2024-04-17",
            "2025-04-06",
            "2026-03-26",
            "2027-04-15",
            "2028-04-03",
            "2029-04-22",
            "2030-04-12",
            "2031-04-01",
            "2032-04-19",
            "2033-04-07",
            "2034-03-28",
            "2035-04-16",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2036))
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
        govardhan_puja_dt = (
            "2001-11-15",
            "2002-11-05",
            "2003-10-26",
            "2004-11-13",
            "2005-11-02",
            "2006-10-22",
            "2007-11-10",
            "2008-10-29",
            "2009-10-18",
            "2010-11-06",
            "2011-10-27",
            "2012-11-14",
            "2013-11-04",
            "2014-10-24",
            "2015-11-12",
            "2016-10-31",
            "2017-10-20",
            "2018-11-08",
            "2019-10-28",
            "2020-11-15",
            "2021-11-05",
            "2022-10-26",
            "2023-11-14",
            "2024-11-02",
            "2025-10-22",
            "2026-11-10",
            "2027-10-30",
            "2028-10-18",
            "2029-11-06",
            "2030-10-27",
            "2031-11-15",
            "2032-11-03",
            "2033-10-23",
            "2034-11-11",
            "2035-10-31",
        )
        self.assertNonObservedHolidayName(name, govardhan_puja_dt)
        self.assertNonObservedHolidayName(name, range(2001, 2036))

    def test_diwali_laxmi_pujan(self):
        name = "Diwali Laxmi Pujan"
        dt = (
            "2001-11-14",
            "2002-11-04",
            "2003-10-25",
            "2004-11-12",
            "2005-11-01",
            "2006-10-21",
            "2007-11-09",
            "2008-10-28",
            "2009-10-17",
            "2010-11-05",
            "2011-10-26",
            "2012-11-13",
            "2013-11-03",
            "2014-10-23",
            "2015-11-11",
            "2016-10-30",
            "2017-10-19",
            "2018-11-07",
            "2019-10-27",
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-11-01",
            "2025-10-21",
            "2026-11-09",
            "2027-10-29",
            "2028-10-17",
            "2029-11-05",
            "2030-10-26",
            "2031-11-14",
            "2032-11-02",
            "2033-10-22",
            "2034-11-10",
            "2035-10-30",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2036))

    def test_dussehra(self):
        name = "Dussehra"
        dt = (
            "2001-10-26",
            "2002-10-15",
            "2003-10-05",
            "2004-10-22",
            "2005-10-12",
            "2006-10-02",
            "2007-10-21",
            "2008-10-09",
            "2009-09-28",
            "2010-10-17",
            "2011-10-06",
            "2012-10-24",
            "2013-10-13",
            "2014-10-03",
            "2015-10-22",
            "2016-10-11",
            "2017-09-30",
            "2018-10-19",
            "2019-10-08",
            "2020-10-25",
            "2021-10-15",
            "2022-10-05",
            "2023-10-24",
            "2024-10-12",
            "2025-10-02",
            "2026-10-20",
            "2027-10-09",
            "2028-09-27",
            "2029-10-16",
            "2030-10-06",
            "2031-10-25",
            "2032-10-14",
            "2033-10-03",
            "2034-10-22",
            "2035-10-11",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2036))

    def test_ganesh_chaturthi(self):
        name = "Ganesh Chaturthi"
        dt = (
            "2001-08-22",
            "2002-09-10",
            "2003-08-31",
            "2004-09-18",
            "2005-09-07",
            "2006-08-27",
            "2007-09-15",
            "2008-09-03",
            "2009-08-23",
            "2010-09-11",
            "2011-09-01",
            "2012-09-19",
            "2013-09-09",
            "2014-08-29",
            "2015-09-17",
            "2016-09-05",
            "2017-08-25",
            "2018-09-13",
            "2019-09-02",
            "2020-08-22",
            "2021-09-10",
            "2022-08-31",
            "2023-09-19",
            "2024-09-07",
            "2025-08-27",
            "2026-09-14",
            "2027-09-04",
            "2028-08-23",
            "2029-09-11",
            "2030-09-01",
            "2031-09-20",
            "2032-09-08",
            "2033-08-28",
            "2034-09-16",
            "2035-09-05",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2036))

    def test_guru_nanak_jayanti(self):
        name = "Guru Nanak Jayanti"
        dt = (
            "2001-11-30",
            "2002-11-19",
            "2003-11-08",
            "2004-11-26",
            "2005-11-15",
            "2006-11-05",
            "2007-11-24",
            "2008-11-13",
            "2009-11-02",
            "2010-11-21",
            "2011-11-10",
            "2012-11-28",
            "2013-11-17",
            "2014-11-06",
            "2015-11-25",
            "2016-11-14",
            "2017-11-04",
            "2018-11-23",
            "2019-11-12",
            "2020-11-30",
            "2021-11-19",
            "2022-11-08",
            "2023-11-27",
            "2024-11-15",
            "2025-11-05",
            "2027-11-14",
            "2028-11-02",
            "2029-11-21",
            "2030-11-10",
            "2031-11-28",
            "2032-11-17",
            "2033-11-06",
            "2034-11-25",
            "2035-11-15",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2026))
        self.assertNonObservedHolidayName(name, range(2027, 2036))

    def test_muharram(self):
        name = "Muharram (estimated)"
        dt = (
            "2001-04-04",
            "2002-03-24",
            "2003-03-13",
            "2004-03-01",
            "2005-02-19",
            "2006-02-09",
            "2007-01-29",
            "2008-01-19",
            "2009-12-27",
            "2010-12-16",
            "2011-12-05",
            "2012-11-24",
            "2013-11-13",
            "2014-11-03",
            "2015-10-23",
            "2016-10-11",
            "2017-09-30",
            "2018-09-20",
            "2019-09-09",
            "2020-08-29",
            "2021-08-18",
            "2026-06-25",
            "2027-06-15",
            "2028-06-03",
            "2029-05-23",
            "2030-05-12",
            "2031-05-02",
            "2032-04-20",
            "2033-04-10",
            "2034-03-30",
            "2035-03-20",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2022))
        self.assertNonObservedHolidayName(name, range(2026, 2036))

        name = "Muharram"
        dt = (
            "2022-08-09",
            "2023-07-29",
            "2024-07-17",
            "2025-07-06",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2022, 2026))

    def test_id_ul_fitr(self):
        name = "Id-Ul-Fitr (Ramadan Eid) (estimated)"
        dt = (
            "2001-12-16",
            "2002-12-05",
            "2003-11-25",
            "2004-11-14",
            "2005-11-03",
            "2006-10-23",
            "2007-10-13",
            "2008-10-01",
            "2009-09-20",
            "2010-09-10",
            "2011-08-30",
            "2012-08-19",
            "2013-08-08",
            "2014-07-28",
            "2015-07-17",
            "2016-07-06",
            "2017-06-25",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2026-03-20",
            "2027-03-09",
            "2028-02-26",
            "2029-02-14",
            "2030-02-04",
            "2031-01-24",
            "2032-01-14",
            "2033-01-02",
            "2034-12-12",
            "2035-12-01",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2022))
        self.assertNonObservedHolidayName(name, range(2026, 2036))

        name = "Id-Ul-Fitr (Ramadan Eid)"
        dt = (
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-03-31",
        )

        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2022, 2026))

    def test_bakri_id(self):
        name = "Bakri Id (estimated)"
        dt = (
            "2001-03-05",
            "2002-02-22",
            "2003-02-11",
            "2004-02-01",
            "2005-01-21",
            "2006-01-10",
            "2007-12-20",
            "2008-12-08",
            "2009-11-27",
            "2010-11-16",
            "2011-11-06",
            "2012-10-26",
            "2013-10-15",
            "2014-10-04",
            "2015-09-23",
            "2016-09-11",
            "2017-09-01",
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2026-05-27",
            "2027-05-16",
            "2028-05-05",
            "2029-04-24",
            "2030-04-13",
            "2031-04-02",
            "2032-03-22",
            "2033-03-11",
            "2034-03-01",
            "2035-02-18",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, range(2001, 2022))
        self.assertNonObservedHolidayName(name, range(2026, 2035))

        name = "Bakri Id"
        dt = (
            "2022-07-10",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertNonObservedHolidayName(name, dt)
        self.assertNonObservedHolidayName(name, {2022, 2024, 2025})

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
