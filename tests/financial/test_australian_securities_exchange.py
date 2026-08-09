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

from holidays.financial.australian_securities_exchange import AustralianSecuritiesExchange
from tests.common import CommonFinancialTests


class TestAustralianSecuritiesExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AustralianSecuritiesExchange)

    def test_special_holidays(self):
        self.assertHoliday(
            "2011-04-26",
            "2022-09-22",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name,
            "2020-01-01",
            "2021-01-01",
            "2022-01-03",
            "2023-01-02",
            "2024-01-01",
            "2025-01-01",
            "2026-01-01",
        )
        self.assertNoHoliday(
            "2022-01-01",
            "2023-01-01",
        )

    def test_australia_day(self):
        name = "Australia Day"
        self.assertNonObservedHolidayName(name, (f"{year}-01-26" for year in self.full_range))
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name,
            "2020-01-27",
            "2021-01-26",
            "2022-01-26",
            "2023-01-26",
            "2024-01-26",
            "2025-01-27",
            "2026-01-26",
        )
        self.assertNoHoliday(
            "2020-01-26",
            "2025-01-26",
        )

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
            "2026-04-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
            "2026-04-06",
        )
        self.assertHolidayName(name, self.full_range)

    def test_anzac_day(self):
        name = "ANZAC Day"
        self.assertNonObservedHolidayName(name, (f"{year}-04-25" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2010-04-26",
            "2019-04-25",
            "2022-04-25",
            "2023-04-25",
            "2024-04-25",
            "2025-04-25",
        )
        self.assertNoHoliday(
            "2010-04-25",
            "2020-04-25",
            "2021-04-25",
            "2026-04-25",
            "2027-04-25",
        )

    def test_sovereigns_birthday(self):
        name_queen = "Queen's Birthday"
        name_king = "King's Birthday"
        self.assertHolidayName(
            name_queen,
            "2020-06-08",
            "2021-06-14",
            "2022-06-13",
        )
        self.assertHolidayName(
            name_king,
            "2023-06-12",
            "2024-06-10",
            "2025-06-09",
            "2026-06-08",
        )
        self.assertHolidayName(name_queen, range(self.start_year, 2023))
        self.assertHolidayName(name_king, range(2023, self.end_year))
        self.assertNoHolidayName(name_queen, range(2023, self.end_year))
        self.assertNoHolidayName(name_king, range(self.start_year, 2023))

    def test_anzac_day_(self):
        name = "ANZAC Day (No Settlement)"
        self.assertNoRestrictedSettlementHolidayName(
            name,
            "2000-04-25",
            "2001-04-25",
            "2002-04-25",
            "2003-04-25",
            "2005-04-25",
            "2006-04-25",
            "2007-04-25",
            "2008-04-25",
        )
        self.assertNoRestrictedSettlementHolidayName(name, range(2009, self.end_year))
        self.assertRestrictedSettlementHolidayName(name, "2004-04-26")

    def test_labour_day_(self):
        name = "Labour Day (No Settlement)"
        self.assertRestrictedSettlementHolidayName(
            name,
            "2005-03-14",
            "2005-10-03",
            "2010-03-08",
            "2010-10-04",
            "2015-03-09",
            "2015-10-05",
            "2016-03-14",
            "2016-10-03",
        )
        self.assertNoRestrictedSettlementHolidayName(
            name,
            "2017-03-13",
            "2017-10-02",
            "2020-03-09",
            "2020-10-05",
        )
        self.assertRestrictedSettlementHolidayName(name, range(self.start_year, 2017))
        self.assertNoRestrictedSettlementHolidayName(name, range(2017, self.end_year))

    def test_bank_holiday(self):
        name = "Bank Holiday (No Settlement)"
        self.assertNoHolidayName(name)
        self.assertRestrictedSettlementHolidayName(
            name,
            "2005-08-01",
            "2010-08-02",
            "2015-08-03",
            "2016-08-01",
        )
        self.assertNoRestrictedSettlementHolidayName(
            name,
            "2017-08-07",
            "2020-08-03",
        )
        self.assertRestrictedSettlementHolidayName(name, range(self.start_year, 2017))
        self.assertNoRestrictedSettlementHolidayName(name, range(2017, self.end_year))

    def test_melbourne_cup_day(self):
        name = "Melbourne Cup Day (No Settlement)"
        self.assertRestrictedSettlementHolidayName(
            name,
            "2005-11-01",
            "2009-11-03",
            "2010-11-02",
            "2015-11-03",
            "2016-11-01",
        )
        self.assertNoRestrictedSettlementHolidayName(
            name,
            "2017-11-07",
            "2020-11-03",
        )
        self.assertNoRestrictedSettlementHolidayName(name, range(2017, self.end_year))
        self.assertRestrictedSettlementHolidayName(name, range(self.start_year, 2017))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name,
            "2020-12-25",
            "2021-12-27",
            "2022-12-27",
            "2023-12-25",
            "2024-12-25",
            "2025-12-25",
        )

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name,
            "2020-12-28",
            "2021-12-28",
            "2023-12-26",
            "2024-12-26",
            "2025-12-26",
        )

    def test_last_business_day_before_christmas_day(self):
        name = "Last Business day before Christmas Day (markets close at 14:10 AEDT)"
        self.assertNoHolidayName(name)
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-24" for year in self.full_range)
        )
        self.assertHalfDayHolidayName(
            name,
            "2000-12-22",
            "2006-12-22",
            "2016-12-23",
            "2017-12-22",
            "2020-12-24",
            "2021-12-24",
            "2024-12-24",
            "2025-12-24",
            "2026-12-24",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2000-12-24",
            "2005-12-24",
            "2006-12-24",
            "2011-12-24",
            "2016-12-24",
            "2017-12-24",
            "2022-12-24",
            "2023-12-24",
        )

    def test_last_business_day_of_the_year(self):
        name = "Last Business day of the Year (markets close at 14:10 AEDT)"
        self.assertNoHolidayName(name)
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-31" for year in self.full_range)
        )
        self.assertHalfDayHolidayName(
            name,
            "2000-12-29",
            "2005-12-30",
            "2006-12-29",
            "2011-12-30",
            "2016-12-30",
            "2017-12-29",
            "2020-12-31",
            "2021-12-31",
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2000-12-31",
            "2005-12-31",
            "2011-12-31",
            "2016-12-31",
            "2017-12-31",
            "2022-12-31",
            "2023-12-31",
        )

    def test_easter_thursday(self):
        name = "Easter Thursday (markets close at 14:10 AEDT)"
        self.assertHalfDayHolidayName(
            name,
            "2000-04-20",
            "2004-04-08",
            "2008-03-20",
        )
        self.assertHalfDayHolidayName(name, range(self.start_year, 2009))
        self.assertNoHalfDayHolidayName(name, range(2009, self.end_year))

    def test_day_following_new_years_day(self):
        name = "Day following New Year's Day (markets close at 14:10 AEDT)"
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-01-02" for year in range(self.start_year, 2006))
        )
        self.assertHalfDayHolidayName(
            name,
            "2001-01-02",
            "2002-01-02",
            "2003-01-02",
            "2004-01-02",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2000-01-02",
            "2005-01-02",
            "2006-01-02",
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-27", "Australia Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-25", "ANZAC Day"),
            ("2025-06-09", "King's Birthday"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-12-24", "Last Business day before Christmas Day (markets close at 14:10 AEDT)"),
            ("2025-12-31", "Last Business day of the Year (markets close at 14:10 AEDT)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-26", "Australia Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-25", "ANZAC Day"),
            ("2024-06-10", "King's Birthday"),
            ("2024-12-24", "Last Business day before Christmas Day (markets close at 14:10 AEDT)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
            ("2024-12-31", "Last Business day of the Year (markets close at 14:10 AEDT)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-26", "Australia Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-25", "ANZAC Day"),
            ("2024-06-10", "King's Birthday"),
            ("2024-12-24", "Last Business day before Christmas Day (markets close at 14:10 AEDT)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
            ("2024-12-31", "Last Business day of the Year (markets close at 14:10 AEDT)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-01-26", "วันชาติออสเตรเลีย"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-04-01", "วันจันทร์อีสเตอร์"),
            ("2024-04-25", "วันแอนแซค"),
            ("2024-06-10", "วันเฉลิมพระชนมพรรษาสมเด็จพระราชาธิบดี"),
            ("2024-12-24", "วันทำการสุดท้ายก่อนวันคริสต์มาส (ตลาดปิดทำการเวลา 14:10 น. AEDT)"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-26", "วันเปิดกล่องของขวัญ"),
            ("2024-12-31", "วันทำการสุดท้ายของปี (ตลาดปิดทำการเวลา 14:10 น. AEDT)"),
        )
