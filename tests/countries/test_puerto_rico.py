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

from holidays.countries.puerto_rico import PuertoRico
from tests.common import CommonCountryTests


class TestPuertoRico(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PuertoRico)

    def test_epiphany(self):
        name = "Epiphany"
        self.assertHolidayName(name, (f"{year}-01-06" for year in range(1932, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1932))

    def test_birthday_of_eugenio_maria_de_hostos(self):
        name = "Birthday of Eugenio María de Hostos"
        self.assertHolidayName(name, (f"{year}-01-11" for year in range(1940, 1971)))
        self.assertHolidayName(
            name,
            "2010-01-11",
            "2011-01-10",
            "2012-01-09",
            "2013-01-14",
            "2014-01-13",
        )
        self.assertHolidayName(name, range(1971, 2015))
        self.assertNoHolidayName(name, range(self.start_year, 1940), range(2015, self.end_year))
        obs_dts = (
            "1953-01-12",
            "1959-01-12",
            "1970-01-12",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_the_day_of_the_women_and_men_heroes_of_puerto_rico(self):
        name_1903 = "George Washington Day"
        name_2015 = "George Washington Day, Presidents' Day, and the Puerto Rican Heroes Day"
        name_2016 = (
            "George Washington Day, Presidents' Day, and the Day of the Hero "
            "and the Illustrious Woman of Puerto Rico"
        )
        name_2019 = (
            "George Washington Day, Presidents' Day, and the Day of the Women and Men "
            "Heroes of Puerto Rico"
        )
        self.assertHolidayName(name_1903, (f"{year}-02-22" for year in range(1903, 1971)))
        self.assertHolidayName(
            name_1903,
            "2010-02-15",
            "2011-02-21",
            "2012-02-20",
            "2013-02-18",
            "2014-02-17",
        )
        self.assertHolidayName(name_1903, range(1971, 2015))
        self.assertHolidayName(name_2015, "2015-02-16")
        self.assertHolidayName(
            name_2016,
            "2016-02-15",
            "2017-02-20",
            "2018-02-19",
        )
        self.assertHolidayName(
            name_2019,
            "2019-02-18",
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
            "2024-02-19",
            "2025-02-17",
        )
        self.assertHolidayName(name_2019, range(2019, self.end_year))
        self.assertNoHolidayName(name_1903, range(2019, self.end_year))
        self.assertNoHolidayName(name_2015, range(1903, 2015), range(2016, self.end_year))
        self.assertNoHolidayName(name_2016, range(1903, 2016), range(2019, self.end_year))
        self.assertNoHolidayName(name_2019, range(1903, 2019))
        obs_dts = (
            "1953-02-23",
            "1959-02-23",
            "1970-02-23",
        )
        self.assertHolidayName(f"{name_1903} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-03-22" for year in self.full_range))
        obs_dts = (
            "1998-03-23",
            "2009-03-23",
            "2015-03-23",
            "2020-03-23",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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
        )
        self.assertHolidayName(name, self.full_range)

    def test_jose_de_diego_day(self):
        name = "José de Diego Day"
        self.assertHolidayName(name, (f"{year}-04-16" for year in range(1925, 1971)))
        self.assertHolidayName(
            name,
            "2010-04-19",
            "2011-04-18",
            "2012-04-16",
            "2013-04-15",
            "2014-04-21",
        )
        self.assertHolidayName(name, range(1971, 2015))
        self.assertNoHolidayName(name, range(self.start_year, 1925), range(2015, self.end_year))
        obs_dts = (
            "1961-04-17",
            "1967-04-17",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_luis_munoz_rivera_day(self):
        name = "Luis Muñoz Rivera Day"
        self.assertHolidayName(name, (f"{year}-07-17" for year in range(1918, 1971)))
        self.assertHolidayName(
            name,
            "2010-07-19",
            "2011-07-18",
            "2012-07-16",
            "2013-07-15",
            "2014-07-21",
        )
        self.assertHolidayName(name, range(1971, 2015))
        self.assertNoHolidayName(name, range(self.start_year, 1918), range(2015, self.end_year))
        obs_dts = (
            "1955-07-18",
            "1960-07-18",
            "1966-07-18",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_constitution_day(self):
        name_1903 = "Occupation Day"
        name_1953 = "Puerto Rico Constitution Day"
        self.assertHolidayName(name_1903, (f"{year}-07-25" for year in range(1903, 1953)))
        self.assertHolidayName(name_1953, (f"{year}-07-25" for year in range(1953, self.end_year)))
        self.assertNoHolidayName(name_1903, range(1953, self.end_year))
        self.assertNoHolidayName(name_1953, range(self.start_year, 1953))
        obs_dts = (
            "2004-07-26",
            "2010-07-26",
            "2021-07-26",
        )
        self.assertHolidayName(f"{name_1953} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_jose_celso_barbosa_day(self):
        name = "José Celso Barbosa Day"
        self.assertHolidayName(
            name, (f"{year}-07-27" for year in (*range(1938, 1971), *range(1994, 2015)))
        )
        self.assertHolidayName(
            name,
            "1989-07-24",
            "1990-07-23",
            "1991-07-22",
            "1992-07-27",
            "1993-07-26",
        )
        self.assertHolidayName(name, range(1971, 1994))
        self.assertNoHolidayName(name, range(self.start_year, 1938), range(2015, self.end_year))
        obs_dts = (
            "1958-07-28",
            "2003-07-28",
            "2008-07-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_puerto_rican_identity_day(self):
        name_1938 = "Discovery of Puerto Rico Day"
        name_2014 = "Puerto Rican Culture and Discovery of Puerto Rico Day"
        name_2023 = "Puerto Rican Identity Day"
        self.assertHolidayName(name_1938, (f"{year}-11-19" for year in range(1938, 2014)))
        self.assertHolidayName(name_2014, (f"{year}-11-19" for year in range(2014, 2023)))
        self.assertHolidayName(name_2023, (f"{year}-11-19" for year in range(2023, self.end_year)))
        self.assertNoHolidayName(
            name_1938, range(self.start_year, 1938), range(2014, self.end_year)
        )
        self.assertNoHolidayName(
            name_2014, range(self.start_year, 2014), range(2023, self.end_year)
        )
        self.assertNoHolidayName(name_2023, range(self.start_year, 2023))

        obs_dts_1938 = (
            "2000-11-20",
            "2006-11-20",
        )
        obs_dts_2014 = ("2017-11-20",)
        obs_dts_2023 = ("2023-11-20",)
        self.assertHolidayName(f"{name_1938} (observed)", obs_dts_1938)
        self.assertHolidayName(f"{name_2014} (observed)", obs_dts_2014)
        self.assertHolidayName(f"{name_2023} (observed)", obs_dts_2023)
        self.assertNoNonObservedHoliday(obs_dts_1938, obs_dts_2014, obs_dts_2023)

    def test_christmas_eve(self):
        name = "Christmas Eve (from 12pm)"
        self.assertHalfDayHolidayName(
            name, (f"{year}-12-24" for year in range(2003, self.end_year))
        )
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 2003))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-01-17", "Martin Luther King Jr. Day"),
            ("2022-02-14", "Valentine's Day"),
            (
                "2022-02-21",
                "George Washington Day, Presidents' Day, and the Day of the Women and Men "
                "Heroes of Puerto Rico",
            ),
            ("2022-03-17", "Saint Patrick's Day"),
            ("2022-03-22", "Emancipation Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-08", "Mother's Day"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-19", "Father's Day; Juneteenth National Independence Day"),
            ("2022-06-20", "Juneteenth National Independence Day (observed)"),
            ("2022-07-04", "Independence Day"),
            ("2022-07-25", "Puerto Rico Constitution Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-10", "Columbus Day"),
            ("2022-10-31", "Halloween"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-19", "Puerto Rican Culture and Discovery of Puerto Rico Day"),
            ("2022-11-24", "Thanksgiving Day"),
            ("2022-12-24", "Christmas Eve; Christmas Eve (from 12pm)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-01-17", "วันมาร์ติน ลูเทอร์ คิง จูเนียร์"),
            ("2022-02-14", "วันวาเลนไทน์"),
            ("2022-02-21", "วันจอร์จ วอชิงตัน, วันประธานาธิบดี และวันวีรบุรุษและวีรสตรีแห่งเปอร์โตริโก"),
            ("2022-03-17", "วันนักบุญแพทริก"),
            ("2022-03-22", "วันเลิกทาส"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-05-08", "วันแม่"),
            ("2022-05-30", "วันรำลึก"),
            ("2022-06-19", "วันประกาศอิสรภาพแห่งชาติจูนทีนท์; วันพ่อ"),
            ("2022-06-20", "ชดเชยวันประกาศอิสรภาพแห่งชาติจูนทีนท์"),
            ("2022-07-04", "วันประกาศอิสรภาพ"),
            ("2022-07-25", "วันรัฐธรรมนูญเปอร์โตริโก"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-10", "วันโคลัมบัส"),
            ("2022-10-31", "วันฮาโลวีน"),
            ("2022-11-11", "วันทหารผ่านศึก"),
            ("2022-11-19", "วันวัฒนธรรมเปอร์โตริโกและการค้นพบเปอร์โตริโก"),
            ("2022-11-24", "วันขอบคุณพระเจ้า"),
            ("2022-12-24", "วันคริสต์มาสอีฟ; วันคริสต์มาสอีฟ (ตั้งแต่ 12:00 น.)"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส"),
            ("2022-12-31", "วันสิ้นปี"),
        )
