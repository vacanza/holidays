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

from holidays.financial.korea_exchange import KoreaExchange
from tests.common import CommonFinancialTests


class TestKoreaExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(2000, 2026)
        super().setUpClass(KoreaExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_workers_day(self):
        name = "근로자의날"
        years_absent = {2004, 2005, 2010, 2011, 2016, 2021, 2022, 2027}
        self.assertNoHolidayName(name, (f"{year}-05-01" for year in years_absent))
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in self.full_range if year not in years_absent)
        )

    def test_end_of_year_holiday(self):
        name = "연말휴장일"
        years_absent = {2000, 2005, 2006, 2011, 2016, 2017, 2022, 2023, 2028}
        self.assertNoHolidayName(name, (f"{year}-12-31" for year in years_absent))
        self.assertHolidayName(
            name, (f"{year}-12-31" for year in self.full_range if year not in years_absent)
        )
        self.assertHolidayName(
            name,
            "2000-12-29",
            "2005-12-30",
            "2006-12-29",
            "2011-12-30",
            "2016-12-30",
            "2017-12-29",
            "2022-12-30",
            "2023-12-29",
            "2028-12-29",
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "신정연휴"),
            ("2025-01-27", "임시공휴일"),
            ("2025-01-28", "설날 전날"),
            ("2025-01-29", "설날"),
            ("2025-01-30", "설날 다음날"),
            ("2025-03-03", "삼일절 대체 휴일"),
            ("2025-05-01", "근로자의날"),
            ("2025-05-05", "부처님오신날; 어린이날"),
            ("2025-05-06", "부처님오신날 대체 휴일; 어린이날 대체 휴일"),
            ("2025-06-03", "대통령 선거일"),
            ("2025-06-06", "현충일"),
            ("2025-08-15", "광복절"),
            ("2025-10-03", "개천절"),
            ("2025-10-06", "추석"),
            ("2025-10-07", "추석 다음날"),
            ("2025-10-08", "추석 대체 휴일"),
            ("2025-10-09", "한글날"),
            ("2025-12-25", "기독탄신일"),
            ("2025-12-31", "연말휴장일"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "신정연휴"),
            ("2024-02-09", "설날 전날"),
            ("2024-02-12", "설날 대체 휴일"),
            ("2024-03-01", "삼일절"),
            ("2024-04-10", "국회의원 선거일"),
            ("2024-05-01", "근로자의날"),
            ("2024-05-06", "어린이날 대체 휴일"),
            ("2024-05-15", "부처님오신날"),
            ("2024-06-06", "현충일"),
            ("2024-08-15", "광복절"),
            ("2024-09-16", "추석 전날"),
            ("2024-09-17", "추석"),
            ("2024-09-18", "추석 다음날"),
            ("2024-10-01", "국군의 날"),
            ("2024-10-03", "개천절"),
            ("2024-10-09", "한글날"),
            ("2024-12-25", "기독탄신일"),
            ("2024-12-31", "연말휴장일"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "The day preceding Korean New Year"),
            ("2024-02-12", "Alternative holiday for Korean New Year"),
            ("2024-03-01", "Independence Movement Day"),
            ("2024-04-10", "National Assembly Election Day"),
            ("2024-05-01", "Workers' Day"),
            ("2024-05-06", "Alternative holiday for Children's Day"),
            ("2024-05-15", "Buddha's Birthday"),
            ("2024-06-06", "Memorial Day"),
            ("2024-08-15", "Liberation Day"),
            ("2024-09-16", "The day preceding Chuseok"),
            ("2024-09-17", "Chuseok"),
            ("2024-09-18", "The second day of Chuseok"),
            ("2024-10-01", "Armed Forces Day"),
            ("2024-10-03", "National Foundation Day"),
            ("2024-10-09", "Hangul Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-31", "End of Year Holiday"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันปีใหม่สากล"),
            ("2024-02-09", "วันก่อนเทศกาลซอลลัล"),
            ("2024-02-12", "ชดเชยเทศกาลซอลลัล"),
            ("2024-03-01", "วันอิสรภาพ"),
            ("2024-04-10", "วันเลือกตั้งสมัชชาแห่งชาติ"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-05-06", "ชดเชยวันเด็ก"),
            ("2024-05-15", "วันวิสาขบูชา"),
            ("2024-06-06", "วันรำลึกวีรชน"),
            ("2024-08-15", "วันฉลองอิสรภาพ"),
            ("2024-09-16", "วันก่อนเทศกาลชูซอก"),
            ("2024-09-17", "เทศกาลชูซอก"),
            ("2024-09-18", "วันหลังเทศกาลชูซอก"),
            ("2024-10-01", "วันกองทัพ"),
            ("2024-10-03", "วันสถาปนาประเทศ"),
            ("2024-10-09", "วันฮันกึล"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-31", "วันหยุดสิ้นปี"),
        )
