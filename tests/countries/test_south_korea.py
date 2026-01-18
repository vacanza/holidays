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

import warnings
from unittest import TestCase

from holidays.constants import BANK, PUBLIC
from holidays.countries.south_korea import SouthKorea, Korea
from tests.common import CommonCountryTests


class TestSouthKorea(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SouthKorea)

    def test_special_holidays(self):
        # Election Dates have its own separate checklists.
        self.assertHoliday(
            "1948-12-15",
            "1949-05-10",
            "1949-07-05",
            "1950-06-21",
            "1957-03-26",
            "1958-03-26",
            "1959-03-26",
            "1960-03-16",
            "1960-03-26",
            "1960-10-01",
            "1961-04-19",
            "1962-04-19",
            "1962-05-16",
            "1963-04-19",
            "1963-05-16",
            "1963-12-17",
            "1966-10-01",
            "1967-01-04",
            "1967-07-01",
            "1969-07-21",
            "1969-10-17",
            "1971-07-01",
            "1972-11-21",
            "1972-12-15",
            "1972-12-27",
            "1974-08-19",
            "1975-02-12",
            "1978-05-18",
            "1978-12-27",
            "1979-11-03",
            "1979-12-21",
            "1980-09-01",
            "1980-10-22",
            "1981-02-11",
            "1981-03-03",
            "1982-10-02",
            "1987-10-27",
            "1988-02-25",
            "1988-09-17",
            "2002-07-01",
            "2017-05-09",
            "2017-10-02",
            "2020-08-17",
            "2023-10-02",
            "2024-10-01",
            "2025-01-27",
        )
        # Pre-2014 Observance sans "1960-12-26"
        self.assertNoNonObservedHoliday(
            "1959-04-06",
            "1960-07-18",
            "1960-10-10",
            "1989-10-02",
        )

    def test_national_assembly_election_day(self):
        self.assertHoliday(
            # 1st Republic.
            "1948-05-10",
            "1950-05-30",
            "1954-05-20",
            "1958-05-02",
            "1960-07-29",
            # No Election during the short 2nd Republic.
            # 3rd Republic.
            "1963-11-26",
            "1967-06-08",
            "1971-05-25",
            # 4th Republic.
            "1973-02-27",
            "1978-12-12",
            # 5th Republic.
            "1981-03-25",
            "1985-02-12",
            # 6th Republic.
            "1988-04-26",
            "1992-03-24",
            "1996-04-11",
            "2000-04-13",
            "2004-04-15",
            # Codified rather than on ad-hoc basis from SEP 2006 onwards.
            "2008-04-09",
            "2012-04-11",
            "2016-04-13",
            "2020-04-15",
            # Preliminary Dates.
            "2024-04-10",
            "2028-04-12",
        )

    def test_presidential_election_day(self):
        self.assertHoliday(
            # 1st Republic. (incl. 2nd Vice President Election in 1951)
            "1948-07-20",
            "1951-05-16",
            "1952-08-05",
            "1956-05-15",
            "1960-03-15",
            # 2nd Republic.
            "1960-08-12",
            # 3rd Republic.
            "1963-10-15",
            "1967-05-03",
            "1971-04-27",
            # 4th Republic.
            "1972-12-23",
            "1978-07-06",
            "1979-12-06",
            "1980-08-27",
            # 5th Republic.
            "1981-02-25",
            # 6th Republic.
            "1987-12-16",
            "1992-12-18",
            "1997-12-18",
            "2002-12-19",
            # Codified rather than on ad-hoc basis from SEP 2006 onwards.
            "2007-12-19",
            "2012-12-19",
            "2017-05-09",
            "2022-03-09",
            # Special Presidential Election (21st) due to Yoon Seok-yeol's impeachment.
            "2025-06-03",
            "2030-04-03",
        )

    def test_local_election_day(self):
        self.assertHoliday(
            # 1st Republic Local Elections.
            "1952-04-25",
            "1952-05-10",
            "1956-08-08",
            "1956-08-13",
            "1960-12-12",
            "1960-12-19",
            "1960-12-26",
            "1960-12-29",
            # 1991 Local Elections.
            "1991-03-26",
            "1991-06-20",
            # Nationwide Local Elections.
            "1995-06-27",
            "1998-06-04",
            "2002-06-13",
            "2006-05-31",
            # Codified rather than on ad-hoc basis from SEP 2006 onwards.
            "2010-06-02",
            "2014-06-04",
            "2018-06-13",
            "2022-06-01",
            # Preliminary Dates.
            "2026-06-03",
            "2030-06-12",
        )

    def test_common(self):
        self.assertNonObservedHolidayName("신정연휴", "2019-01-01")

    def test_new_years_day(self):
        name = "신정연휴"
        self.assertHolidayName(
            name,
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in range(self.start_year, 1999)),
            (f"{year}-01-03" for year in range(self.start_year, 1990)),
        )
        self.assertNoHolidayName(
            name,
            (f"{year}-01-02" for year in range(1999, self.end_year)),
            (f"{year}-01-03" for year in range(1990, self.end_year)),
        )

    def test_korean_new_years_day(self):
        name_1985 = "민속의 날"
        name_1989 = "설날"
        name_1989_eve = f"{name_1989} 전날"
        name_1989_day2 = f"{name_1989} 다음날"
        name_1989_observed = f"{name_1989} 대체 휴일"
        self.assertHolidayName(
            name_1985,
            "1985-02-20",
            "1986-02-09",
            "1987-01-29",
            "1988-02-18",
        )
        self.assertHolidayName(
            name_1989,
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
            "2024-02-10",
            "2025-01-29",
        )
        self.assertHolidayName(name_1989, range(1989, self.end_year))
        self.assertHolidayName(
            name_1989_eve,
            "2020-01-24",
            "2021-02-11",
            "2022-01-31",
            "2023-01-21",
            "2024-02-09",
            "2025-01-28",
        )
        self.assertHolidayName(name_1989_eve, range(1989, self.end_year))
        self.assertHolidayName(
            name_1989_day2,
            "2020-01-26",
            "2021-02-13",
            "2022-02-02",
            "2023-01-23",
            "2024-02-11",
            "2025-01-30",
        )
        self.assertHolidayName(name_1989_day2, range(1989, self.end_year))
        self.assertHolidayName(
            name_1989_observed,
            "2016-02-10",
            "2017-01-30",
            "2020-01-27",
            "2023-01-24",
            "2024-02-12",
            "2027-02-09",
        )
        self.assertNoHolidayName(
            name_1985, range(self.start_year, 1985), range(1989, self.end_year)
        )
        self.assertNoHolidayName(f"{name_1985} 전날")
        self.assertNoHolidayName(f"{name_1985} 다음날")
        self.assertNoHolidayName(f"{name_1985} 대체 휴일")
        self.assertNoHolidayName(name_1989, range(self.start_year, 1989))
        self.assertNoHolidayName(name_1989_eve, range(self.start_year, 1989))
        self.assertNoHolidayName(name_1989_day2, range(self.start_year, 1989))
        self.assertNoHolidayName(name_1989_observed, range(self.start_year, 2014))

    def test_independence_movement_day(self):
        name = "삼일절"
        self.assertHolidayName(name, (f"{year}-03-01" for year in self.full_range))
        self.assertHolidayName(
            f"{name} 대체 휴일",
            "2025-03-03",
            "2026-03-02",
        )

    def test_tree_planting_day(self):
        name = "식목일"
        self.assertHolidayName(
            name, (f"{year}-04-05" for year in (*range(1949, 1960), *range(1961, 2006)))
        )
        self.assertNoHolidayName(
            name, range(self.start_year, 1949), 1960, range(2006, self.end_year)
        )
        self.assertHolidayName(f"{name} 대체 휴일", "1959-04-06")

    def test_childrens_day(self):
        name = "어린이날"
        name_observed = f"{name} 대체 휴일"
        self.assertHolidayName(name, (f"{year}-05-05" for year in range(1975, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1975))
        self.assertHolidayName(
            name_observed,
            "2018-05-07",
            "2019-05-06",
            "2024-05-06",
            "2025-05-06",
            "2029-05-07",
            "2030-05-06",
        )
        self.assertNoHolidayName(name_observed, range(1975, 2014))

    def test_buddhas_birthday(self):
        name_1975 = "석가탄신일"
        name_2017 = "부처님오신날"
        name_2017_observed = f"{name_2017} 대체 휴일"
        self.assertHolidayName(
            name_1975,
            "2006-05-05",
            "2007-05-24",
            "2008-05-12",
            "2009-05-02",
            "2010-05-21",
            "2011-05-10",
            "2012-05-28",
            "2013-05-17",
            "2014-05-06",
            "2015-05-25",
            "2016-05-14",
        )
        self.assertHolidayName(name_1975, range(1975, 2017))
        self.assertHolidayName(
            name_2017,
            "2017-05-03",
            "2018-05-22",
            "2019-05-12",
            "2020-04-30",
            "2021-05-19",
            "2022-05-08",
            "2023-05-27",
            "2024-05-15",
            "2025-05-05",
            "2026-05-24",
            "2027-05-13",
            "2028-05-02",
            "2029-05-20",
        )
        self.assertHolidayName(name_2017, range(2017, self.end_year))
        self.assertHolidayName(
            name_2017_observed,
            "2023-05-29",
            "2026-05-25",
            "2029-05-21",
        )
        self.assertNoHolidayName(
            name_1975, range(self.start_year, 1975), range(2017, self.end_year)
        )
        self.assertNoHolidayName(f"{name_1975} 대체 휴일")
        self.assertNoHolidayName(name_2017, range(self.start_year, 2017))
        self.assertNoHolidayName(name_2017_observed, range(self.start_year, 2023))

    def test_memorial_day(self):
        name = "현충일"
        self.assertHolidayName(name, (f"{year}-06-06" for year in range(1956, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1956))

    def test_constitution_day(self):
        name = "제헌절"
        self.assertHolidayName(name, (f"{year}-07-17" for year in range(self.start_year, 2008)))
        self.assertNoHolidayName(name, range(2008, self.end_year))
        self.assertHolidayName(f"{name} 대체 휴일", "1960-07-18")

    def test_liberation_day(self):
        name = "광복절"
        name_observed = f"{name} 대체 휴일"
        self.assertHolidayName(name, (f"{year}-08-15" for year in self.full_range))
        self.assertHolidayName(
            name_observed,
            "2021-08-16",
            "2026-08-17",
            "2027-08-16",
        )
        self.assertNoHolidayName(name_observed, range(self.start_year, 2021))

    def test_chuseok(self):
        name = "추석"
        name_eve = f"{name} 전날"
        name_day2 = f"{name} 다음날"
        name_observed = f"{name} 대체 휴일"
        self.assertHolidayName(
            name,
            "2020-10-01",
            "2021-09-21",
            "2022-09-10",
            "2023-09-29",
            "2024-09-17",
            "2025-10-06",
        )
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name_eve,
            "2020-09-30",
            "2021-09-20",
            "2022-09-09",
            "2023-09-28",
            "2024-09-16",
            "2025-10-05",
        )
        self.assertHolidayName(name_eve, range(1989, self.end_year))
        self.assertHolidayName(
            name_day2,
            "1986-09-19",
            "1987-10-08",
            "1988-09-26",
            "2020-10-02",
            "2021-09-22",
            "2022-09-11",
            "2023-09-30",
            "2024-09-18",
            "2025-10-07",
        )
        self.assertHolidayName(name_day2, range(1986, self.end_year))
        self.assertHolidayName(
            name_observed,
            "2014-09-10",
            "2015-09-29",
            "2018-09-26",
            "2022-09-12",
            "2025-10-08",
            "2029-09-24",
        )
        self.assertNoHolidayName(name_eve, range(self.start_year, 1989))
        self.assertNoHolidayName(name_day2, range(self.start_year, 1986))
        self.assertNoHolidayName(name_observed, range(self.start_year, 2014))

    def test_armed_forces_day(self):
        name = "국군의 날"
        name_observed = f"{name} 대체 휴일"
        self.assertHolidayName(name, (f"{year}-10-01" for year in range(1976, 1991)))
        self.assertHolidayName(name_observed, "1989-10-02")
        self.assertNoHolidayName(name_observed, range(1976, 1989), range(1990, 1992))

    def test_national_foundation_day(self):
        name = "개천절"
        name_observed = f"{name} 대체 휴일"
        self.assertHolidayName(name, (f"{year}-10-03" for year in self.full_range))
        self.assertHolidayName(
            name_observed,
            "2021-10-04",
            "2026-10-05",
            "2027-10-04",
        )
        self.assertNoHolidayName(name_observed, range(self.start_year, 2021))

    def test_hangul_day(self):
        name = "한글날"
        name_observed = f"{name} 대체 휴일"
        self.assertHolidayName(
            name,
            (
                f"{year}-10-09"
                for year in (*range(self.start_year, 1991), *range(2013, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(1991, 2013))
        self.assertHolidayName(
            name_observed,
            "1960-10-10",
            "2021-10-11",
            "2022-10-10",
            "2027-10-11",
        )
        self.assertNoHolidayName(name_observed, range(self.start_year, 1960), range(1961, 2021))

    def test_united_nations_day(self):
        name = "국제연합일"
        self.assertHolidayName(name, (f"{year}-10-24" for year in range(1950, 1976)))
        self.assertNoHolidayName(name, range(self.start_year, 1950), range(1976, self.end_year))

    def test_christmas_day(self):
        name = "기독탄신일"
        name_observed = f"{name} 대체 휴일"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName(
            name_observed,
            "1960-12-26",
            "2027-12-27",
            "2032-12-27",
            "2033-12-26",
        )
        self.assertNoHolidayName(name_observed, range(self.start_year, 1960), range(1961, 2023))

    def test_workers_day(self):
        self.assertBankHolidayName(
            "근로자의날",
            (f"{year}-03-10" for year in range(self.start_year, 1994)),
            (f"{year}-05-01" for year in range(1994, self.end_year)),
        )

    def test_korea_deprecation_warning(self):
        warnings.simplefilter("default")
        with self.assertWarns(Warning):
            Korea()

    def test_2020_all(self):
        self.assertHolidays(
            SouthKorea(categories=(BANK, PUBLIC), years=2020),
            ("2020-01-01", "신정연휴"),
            ("2020-01-24", "설날 전날"),
            ("2020-01-25", "설날"),
            ("2020-01-26", "설날 다음날"),
            ("2020-01-27", "설날 대체 휴일"),
            ("2020-03-01", "삼일절"),
            ("2020-04-15", "국회의원 선거일"),
            ("2020-04-30", "부처님오신날"),
            ("2020-05-01", "근로자의날"),
            ("2020-05-05", "어린이날"),
            ("2020-06-06", "현충일"),
            ("2020-08-15", "광복절"),
            ("2020-08-17", "임시공휴일"),
            ("2020-09-30", "추석 전날"),
            ("2020-10-01", "추석"),
            ("2020-10-02", "추석 다음날"),
            ("2020-10-03", "개천절"),
            ("2020-10-09", "한글날"),
            ("2020-12-25", "기독탄신일"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "신정연휴"),
            ("2022-01-31", "설날 전날"),
            ("2022-02-01", "설날"),
            ("2022-02-02", "설날 다음날"),
            ("2022-03-01", "삼일절"),
            ("2022-03-09", "대통령 선거일"),
            ("2022-05-01", "근로자의날"),
            ("2022-05-05", "어린이날"),
            ("2022-05-08", "부처님오신날"),
            ("2022-06-01", "지방선거일"),
            ("2022-06-06", "현충일"),
            ("2022-08-15", "광복절"),
            ("2022-09-09", "추석 전날"),
            ("2022-09-10", "추석"),
            ("2022-09-11", "추석 다음날"),
            ("2022-09-12", "추석 대체 휴일"),
            ("2022-10-03", "개천절"),
            ("2022-10-09", "한글날"),
            ("2022-10-10", "한글날 대체 휴일"),
            ("2022-12-25", "기독탄신일"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-31", "The day preceding Korean New Year"),
            ("2022-02-01", "Korean New Year"),
            ("2022-02-02", "The second day of Korean New Year"),
            ("2022-03-01", "Independence Movement Day"),
            ("2022-03-09", "Presidential Election Day"),
            ("2022-05-01", "Workers' Day"),
            ("2022-05-05", "Children's Day"),
            ("2022-05-08", "Buddha's Birthday"),
            ("2022-06-01", "Local Election Day"),
            ("2022-06-06", "Memorial Day"),
            ("2022-08-15", "Liberation Day"),
            ("2022-09-09", "The day preceding Chuseok"),
            ("2022-09-10", "Chuseok"),
            ("2022-09-11", "The second day of Chuseok"),
            ("2022-09-12", "Alternative holiday for Chuseok"),
            ("2022-10-03", "National Foundation Day"),
            ("2022-10-09", "Hangul Day"),
            ("2022-10-10", "Alternative holiday for Hangul Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-31", "วันก่อนเทศกาลซอลลัล"),
            ("2022-02-01", "เทศกาลซอลลัล"),
            ("2022-02-02", "วันหลังเทศกาลซอลลัล"),
            ("2022-03-01", "วันอิสรภาพ"),
            ("2022-03-09", "วันเลือกตั้งประธานาธิบดี"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-05", "วันเด็ก"),
            ("2022-05-08", "วันวิสาขบูชา"),
            ("2022-06-01", "วันเลือกตั้งท้องถิ่น"),
            ("2022-06-06", "วันรำลึกวีรชน"),
            ("2022-08-15", "วันฉลองอิสรภาพ"),
            ("2022-09-09", "วันก่อนเทศกาลชูซอก"),
            ("2022-09-10", "เทศกาลชูซอก"),
            ("2022-09-11", "วันหลังเทศกาลชูซอก"),
            ("2022-09-12", "ชดเชยเทศกาลชูซอก"),
            ("2022-10-03", "วันสถาปนาประเทศ"),
            ("2022-10-09", "วันฮันกึล"),
            ("2022-10-10", "ชดเชยวันฮันกึล"),
            ("2022-12-25", "วันคริสต์มาส"),
        )
