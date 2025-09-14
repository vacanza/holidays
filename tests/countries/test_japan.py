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

from holidays.countries.japan import Japan, JP, JPN
from tests.common import CommonCountryTests


class TestJapan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Japan, years_non_observed=range(1973, JP.end_year))

    def test_country_aliases(self):
        self.assertAliases(Japan, JP, JPN)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Japan(categories=JP.supported_categories, years=(JP.start_year - 1, JP.end_year + 1))
        )

    def test_special_holiday(self):
        self.assertHoliday(
            "1959-04-10",
            "1989-02-24",
            "1990-11-12",
            "1993-06-09",
            "2019-05-01",
            "2019-10-22",
        )

    def test_new_years_day(self):
        self.assertHolidayName("元日", (f"{year}-01-01" for year in self.full_range))

    def test_coming_of_age(self):
        name = "成人の日"
        self.assertHolidayName(name, (f"{year}-01-15" for year in range(JP.start_year, 2000)))
        self.assertHolidayName(
            name,
            "2000-01-10",
            "2001-01-08",
            "2002-01-14",
            "2020-01-13",
            "2021-01-11",
            "2022-01-10",
            "2023-01-09",
            "2024-01-08",
            "2025-01-13",
        )
        self.assertHolidayName(name, self.full_range)

    def test_foundation_day(self):
        name = "建国記念の日"
        self.assertHolidayName(name, (f"{year}-02-11" for year in range(1967, JP.end_year)))
        self.assertNoHolidayName(name, range(JP.start_year, 1967))

    def test_vernal_equinox_day(self):
        name = "春分の日"
        self.assertHolidayName(
            name,
            "1949-03-21",
            "1950-03-21",
            "1951-03-21",
            "1952-03-21",
            "1953-03-21",
            "1954-03-21",
            "1955-03-21",
            "1956-03-21",
            "1957-03-21",
            "1958-03-21",
            "1959-03-21",
            "1960-03-20",
            "1961-03-21",
            "1962-03-21",
            "1963-03-21",
            "1964-03-20",
            "1965-03-21",
            "1966-03-21",
            "1967-03-21",
            "1968-03-20",
            "1969-03-21",
            "1970-03-21",
            "1971-03-21",
            "1972-03-20",
            "1973-03-21",
            "1974-03-21",
            "1975-03-21",
            "1976-03-20",
            "1977-03-21",
            "1978-03-21",
            "1979-03-21",
            "1980-03-20",
            "1981-03-21",
            "1982-03-21",
            "1983-03-21",
            "1984-03-20",
            "1985-03-21",
            "1986-03-21",
            "1987-03-21",
            "1988-03-20",
            "1989-03-21",
            "1990-03-21",
            "1991-03-21",
            "1992-03-20",
            "1993-03-20",
            "1994-03-21",
            "1995-03-21",
            "1996-03-20",
            "1997-03-20",
            "1998-03-21",
            "1999-03-21",
            "2000-03-20",
            "2001-03-20",
            "2002-03-21",
            "2003-03-21",
            "2004-03-20",
            "2005-03-20",
            "2006-03-21",
            "2007-03-21",
            "2008-03-20",
            "2009-03-20",
            "2010-03-21",
            "2011-03-21",
            "2012-03-20",
            "2013-03-20",
            "2014-03-21",
            "2015-03-21",
            "2016-03-20",
            "2017-03-20",
            "2018-03-21",
            "2019-03-21",
            "2020-03-20",
            "2021-03-20",
            "2022-03-21",
            "2023-03-21",
            "2024-03-20",
            "2025-03-20",
            "2026-03-20",
            "2027-03-21",
            "2028-03-20",
            "2029-03-20",
            "2030-03-20",
            "2031-03-21",
            "2032-03-20",
            "2033-03-20",
            "2034-03-20",
            "2035-03-21",
            "2036-03-20",
            "2037-03-20",
            "2038-03-20",
            "2039-03-21",
            "2040-03-20",
            "2041-03-20",
            "2042-03-20",
            "2043-03-21",
            "2044-03-20",
            "2045-03-20",
            "2046-03-20",
            "2047-03-21",
            "2048-03-20",
            "2049-03-20",
            "2050-03-20",
            "2091-03-20",
            "2092-03-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_showa_day(self):
        name = "昭和の日"
        self.assertHolidayName(name, (f"{year}-04-29" for year in range(2007, JP.end_year)))
        self.assertNoHolidayName(name, range(JP.start_year, 2007))

    def test_constitution_memorial_day(self):
        self.assertHolidayName("憲法記念日", (f"{year}-05-03" for year in self.full_range))

    def test_greenery_day(self):
        name = "みどりの日"
        self.assertHolidayName(
            name,
            (f"{year}-04-29" for year in range(1989, 2007)),
            (f"{year}-05-04" for year in range(2007, JP.end_year)),
        )
        self.assertNoHolidayName(name, range(JP.start_year, 1989))

    def test_national_holiday(self):
        name = "国民の休日"
        for year in (
            1988,
            1989,
            1990,
            1991,
            1993,
            1994,
            1995,
            1996,
            1999,
            2000,
            2001,
            2002,
            2004,
            2005,
            2006,
        ):
            self.assertHolidayName(name, f"{year}-05-04")
            self.assertNoNonObservedHoliday(f"{year}-05-04")

        for dt in (
            "2009-09-22",
            "2015-09-22",
            "2019-04-30",
            "2019-05-02",
            "2026-09-22",
            "2032-09-21",
            "2037-09-22",
            "2043-09-22",
            "2049-09-21",
        ):
            self.assertHolidayName(name, dt)
            self.assertNoNonObservedHoliday(dt)

    def test_childrens_day(self):
        self.assertHolidayName("こどもの日", (f"{year}-05-05" for year in self.full_range))

    def test_marine_day(self):
        name = "海の日"
        self.assertHolidayName(name, (f"{year}-07-20" for year in range(1996, 2003)))
        # 3rd Mon of June, except 2020 & 2021 which are in July instead.
        self.assertHolidayName(
            name,
            "2003-07-21",
            "2004-07-19",
            "2005-07-18",
            "2020-07-23",
            "2021-07-22",
            "2022-07-18",
            "2023-07-17",
            "2024-07-15",
            "2025-07-21",
        )
        self.assertHolidayName(name, range(1996, JP.end_year))
        self.assertNoHolidayName(name, range(JP.start_year, 1996))

    def test_mountain_day(self):
        name = "山の日"
        self.assertHolidayName(
            name,
            (f"{year}-08-11" for year in (*range(2016, 2020), *range(2022, 2050))),
            "2020-08-10",
            "2021-08-08",
        )
        self.assertNoHolidayName(name, range(JP.start_year, 2016))

    def test_respect_for_the_aged_day(self):
        name = "敬老の日"
        self.assertHolidayName(name, (f"{year}-09-15" for year in range(1966, 2003)))
        # 3rd Monday of September.
        self.assertHolidayName(
            name,
            "2020-09-21",
            "2021-09-20",
            "2022-09-19",
            "2023-09-18",
            "2024-09-16",
            "2025-09-15",
        )
        self.assertHolidayName(name, range(1966, JP.end_year))
        self.assertNoHolidayName(name, range(JP.start_year, 1966))

    def test_autumnal_equinox_day(self):
        name = "秋分の日"
        self.assertHolidayName(
            name,
            "1949-09-23",
            "1950-09-23",
            "1951-09-24",
            "1952-09-23",
            "1953-09-23",
            "1954-09-23",
            "1955-09-24",
            "1956-09-23",
            "1957-09-23",
            "1958-09-23",
            "1959-09-24",
            "1960-09-23",
            "1961-09-23",
            "1962-09-23",
            "1963-09-24",
            "1964-09-23",
            "1965-09-23",
            "1966-09-23",
            "1967-09-24",
            "1968-09-23",
            "1969-09-23",
            "1970-09-23",
            "1971-09-24",
            "1972-09-23",
            "1973-09-23",
            "1974-09-23",
            "1975-09-24",
            "1976-09-23",
            "1977-09-23",
            "1978-09-23",
            "1979-09-24",
            "1980-09-23",
            "1981-09-23",
            "1982-09-23",
            "1983-09-23",
            "1984-09-23",
            "1985-09-23",
            "1986-09-23",
            "1987-09-23",
            "1988-09-23",
            "1989-09-23",
            "1990-09-23",
            "1991-09-23",
            "1992-09-23",
            "1993-09-23",
            "1994-09-23",
            "1995-09-23",
            "1996-09-23",
            "1997-09-23",
            "1998-09-23",
            "1999-09-23",
            "2000-09-23",
            "2001-09-23",
            "2002-09-23",
            "2003-09-23",
            "2004-09-23",
            "2005-09-23",
            "2006-09-23",
            "2007-09-23",
            "2008-09-23",
            "2009-09-23",
            "2010-09-23",
            "2011-09-23",
            "2012-09-22",
            "2013-09-23",
            "2014-09-23",
            "2015-09-23",
            "2016-09-22",
            "2017-09-23",
            "2018-09-23",
            "2019-09-23",
            "2020-09-22",
            "2021-09-23",
            "2022-09-23",
            "2023-09-23",
            "2024-09-22",
            "2025-09-23",
            "2026-09-23",
            "2027-09-23",
            "2028-09-22",
            "2029-09-23",
            "2030-09-23",
            "2031-09-23",
            "2032-09-22",
            "2033-09-23",
            "2034-09-23",
            "2035-09-23",
            "2036-09-22",
            "2037-09-23",
            "2038-09-23",
            "2039-09-23",
            "2040-09-22",
            "2041-09-23",
            "2042-09-23",
            "2043-09-23",
            "2044-09-22",
            "2045-09-22",
            "2046-09-23",
            "2047-09-23",
            "2048-09-22",
            "2049-09-22",
            "2050-09-23",
        )
        self.assertHolidayName(name, self.full_range)

    def test_physical_education_day(self):
        name = "体育の日"
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(1966, 2000)))
        self.assertHolidayName(
            name,
            "2000-10-09",
            "2001-10-08",
            "2002-10-14",
            "2003-10-13",
            "2004-10-11",
            "2005-10-10",
            "2006-10-09",
            "2007-10-08",
            "2008-10-13",
            "2009-10-12",
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
        )
        self.assertNoHolidayName(name, range(JP.start_year, 1966), range(2020, JP.end_year))

    def test_sports_day(self):
        name = "スポーツの日"
        self.assertHolidayName(
            name,
            "2020-07-24",
            "2021-07-23",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, range(2020, JP.end_year))
        self.assertNoHolidayName(name, range(JP.start_year, 2020))

    def test_culture_day(self):
        self.assertHolidayName("文化の日", (f"{year}-11-03" for year in self.full_range))

    def test_labour_thanks_giving_day(self):
        self.assertHolidayName("勤労感謝の日", (f"{year}-11-23" for year in self.full_range))

    def test_emperors_birthday(self):
        name = "天皇誕生日"
        self.assertHolidayName(
            name,
            (f"{year}-04-29" for year in range(JP.start_year, 1989)),
            (f"{year}-12-23" for year in range(1989, 2019)),
            (f"{year}-02-23" for year in range(2020, JP.end_year)),
        )
        self.assertNoHolidayName(name, 2019)

    def test_observed_holidays(self):
        name = "振替休日"
        dt = (
            "1973-04-30",
            "1973-09-24",
            "1974-05-06",
            "1974-09-16",
            "1974-11-04",
            "1975-11-24",
            "1976-10-11",
            "1978-01-02",
            "1978-01-16",
            "1979-02-12",
            "1979-04-30",
            "1980-11-24",
            "1981-05-04",
            "1982-03-22",
            "1982-10-11",
            "1984-01-02",
            "1984-01-16",
            "1984-04-30",
            "1984-09-24",
            "1985-05-06",
            "1985-09-16",
            "1985-11-04",
            "1986-11-24",
            "1987-05-04",
            "1988-03-21",
            "1989-01-02",
            "1989-01-16",
            "1990-02-12",
            "1990-04-30",
            "1990-09-24",
            "1990-12-24",
            "1991-05-06",
            "1991-09-16",
            "1991-11-04",
            "1992-05-04",
            "1993-10-11",
            "1995-01-02",
            "1995-01-16",
            "1996-02-12",
            "1996-05-06",
            "1996-09-16",
            "1996-11-04",
            "1997-07-21",
            "1997-11-24",
            "1998-05-04",
            "1999-03-22",
            "1999-10-11",
            "2001-02-12",
            "2001-04-30",
            "2001-09-24",
            "2001-12-24",
            "2002-05-06",
            "2002-09-16",
            "2002-11-04",
            "2003-11-24",
            "2005-03-21",
            "2006-01-02",
            "2007-02-12",
            "2007-04-30",
            "2007-09-24",
            "2007-12-24",
            "2008-05-06",
            "2008-11-24",
            "2009-05-06",
            "2010-03-22",
            "2012-01-02",
            "2012-04-30",
            "2012-12-24",
            "2013-05-06",
            "2013-11-04",
            "2014-05-06",
            "2014-11-24",
            "2015-05-06",
            "2016-03-21",
            "2017-01-02",
            "2018-02-12",
            "2018-04-30",
            "2018-09-24",
            "2018-12-24",
            "2019-05-06",
            "2019-08-12",
            "2019-11-04",
            "2020-02-24",
            "2020-05-06",
            "2023-01-02",
            "2024-02-12",
            "2024-05-06",
            "2024-08-12",
            "2024-09-23",
            "2024-11-04",
            "2025-02-24",
            "2025-05-06",
            "2025-11-24",
            "2026-05-06",
            "2027-03-22",
            "2029-02-12",
            "2029-04-30",
            "2029-09-24",
            "2030-05-06",
            "2030-08-12",
            "2030-11-04",
            "2031-02-24",
            "2031-05-06",
            "2031-11-24",
            "2033-03-21",
            "2034-01-02",
            "2035-02-12",
            "2035-04-30",
            "2035-09-24",
            "2036-05-06",
            "2036-11-24",
            "2037-05-06",
            "2040-01-02",
            "2040-04-30",
            "2041-05-06",
            "2041-08-12",
            "2041-11-04",
            "2042-02-24",
            "2042-05-06",
            "2042-11-24",
            "2043-05-06",
            "2044-03-21",
            "2045-01-02",
            "2046-02-12",
            "2046-04-30",
            "2046-09-24",
            "2047-05-06",
            "2047-08-12",
            "2047-11-04",
            "2048-02-24",
            "2048-05-06",
            "2050-03-21",
        )
        self.assertHolidayName(name, dt)
        self.assertNoNonObservedHoliday(dt)

    def test_bank_holidays(self):
        self.assertBankHolidayName(
            "銀行休業日",
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in self.full_range),
            (f"{year}-01-03" for year in self.full_range),
            (f"{year}-12-31" for year in self.full_range),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "元日; 銀行休業日"),
            ("2022-01-02", "銀行休業日"),
            ("2022-01-03", "銀行休業日"),
            ("2022-01-10", "成人の日"),
            ("2022-02-11", "建国記念の日"),
            ("2022-02-23", "天皇誕生日"),
            ("2022-03-21", "春分の日"),
            ("2022-04-29", "昭和の日"),
            ("2022-05-03", "憲法記念日"),
            ("2022-05-04", "みどりの日"),
            ("2022-05-05", "こどもの日"),
            ("2022-07-18", "海の日"),
            ("2022-08-11", "山の日"),
            ("2022-09-19", "敬老の日"),
            ("2022-09-23", "秋分の日"),
            ("2022-10-10", "スポーツの日"),
            ("2022-11-03", "文化の日"),
            ("2022-11-23", "勤労感謝の日"),
            ("2022-12-31", "銀行休業日"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Bank Holiday; New Year's Day"),
            ("2022-01-02", "Bank Holiday"),
            ("2022-01-03", "Bank Holiday"),
            ("2022-01-10", "Coming of Age Day"),
            ("2022-02-11", "Foundation Day"),
            ("2022-02-23", "Emperor's Birthday"),
            ("2022-03-21", "Vernal Equinox Day"),
            ("2022-04-29", "Showa Day"),
            ("2022-05-03", "Constitution Day"),
            ("2022-05-04", "Greenery Day"),
            ("2022-05-05", "Children's Day"),
            ("2022-07-18", "Marine Day"),
            ("2022-08-11", "Mountain Day"),
            ("2022-09-19", "Respect for the Aged Day"),
            ("2022-09-23", "Autumnal Equinox Day"),
            ("2022-10-10", "Sports Day"),
            ("2022-11-03", "Culture Day"),
            ("2022-11-23", "Labor Thanksgiving Day"),
            ("2022-12-31", "Bank Holiday"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่; วันหยุดธนาคาร"),
            ("2022-01-02", "วันหยุดธนาคาร"),
            ("2022-01-03", "วันหยุดธนาคาร"),
            ("2022-01-10", "วันฉลองบรรลุนิติภาวะ"),
            ("2022-02-11", "วันชาติญี่ปุ่น"),
            ("2022-02-23", "วันคล้ายวันพระราชสมภพ สมเด็จพระจักรพรรดินารุฮิโตะ"),
            ("2022-03-21", "วันวสันตวิษุวัต"),
            ("2022-04-29", "วันโชวะ"),
            ("2022-05-03", "วันรัฐธรรมนูญ"),
            ("2022-05-04", "วันพฤกษชาติ"),
            ("2022-05-05", "วันเด็กแห่งชาติ"),
            ("2022-07-18", "วันแห่งทะเล"),
            ("2022-08-11", "วันแห่งภูเขา"),
            ("2022-09-19", "วันเคารพผู้สูงอายุ"),
            ("2022-09-23", "วันศารทวิษุวัต"),
            ("2022-10-10", "วันกีฬาแห่งชาติ"),
            ("2022-11-03", "วันวัฒนธรรม"),
            ("2022-11-23", "วันขอบคุณแรงงาน"),
            ("2022-12-31", "วันหยุดธนาคาร"),
        )
