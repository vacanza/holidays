#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.thailand import TH, THA, Thailand
from test.common import TestCase


class TestThailand(TestCase):
    def setUp(self):
        self.holidays = Thailand()
        self.holidays_no_observed = Thailand(observed=False)

    def test_country_aliases(self):
        self.assertCountryAliases(Thailand, TH, THA)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (in lieu)"),
            ("2022-02-16", "Makha Bucha"),
            ("2022-04-06", "Chakri Memorial Day"),
            ("2022-04-13", "Songkran Festival"),
            ("2022-04-14", "Songkran Festival"),
            ("2022-04-15", "Songkran Festival"),
            ("2022-05-01", "National Labour Day"),
            ("2022-05-02", "National Labour Day (in lieu)"),
            ("2022-05-04", "Coronation Day"),
            ("2022-05-15", "Visakha Bucha"),
            ("2022-05-16", "Visakha Bucha (in lieu)"),
            ("2022-05-17", "Royal Ploughing Ceremony"),
            ("2022-06-03", "HM Queen Suthida's Birthday"),
            ("2022-07-13", "Asarnha Bucha"),
            ("2022-07-14", "Buddhist Lent Day"),
            ("2022-07-15", "Bridge Public Holiday"),
            ("2022-07-28", "HM King Maha Vajiralongkorn's Birthday"),
            ("2022-07-29", "Bridge Public Holiday"),
            (
                "2022-08-12",
                "HM Queen Sirikit The Queen Mother's Birthday; Mother's Day",
            ),
            ("2022-10-13", "HM King Bhumibol Adulyadej Memorial Day"),
            ("2022-10-14", "Bridge Public Holiday"),
            ("2022-10-23", "Chulalongkorn Memorial Day"),
            ("2022-10-24", "Chulalongkorn Memorial Day (in lieu)"),
            (
                "2022-12-05",
                "Father's Day; HM King Bhumibol Adulyadej's Birthday",
            ),
            ("2022-12-10", "Constitution Day"),
            ("2022-12-12", "Constitution Day (in lieu)"),
            ("2022-12-30", "Bridge Public Holiday"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1941, 2058))
        self.assertNoHoliday("1940-01-01")
        self.assertNoHolidayName("New Year's Day", Thailand(years=1940))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )

    def test_chakri_memorial_day(self):
        self.assertHoliday(f"{year}-04-06" for year in range(1918, 2058))
        self.assertNoHoliday("1917-01-01")
        self.assertNoHolidayName("Chakri Memorial Day", Thailand(years=1917))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2013-04-08",
            "2014-04-07",
            "2019-04-08",
            "2024-04-08",
            "2025-04-07",
        )

    def test_songkran_festival(self):
        name = "Songkran Festival"
        for year in range(1948, 1954):
            self.assertHoliday(
                f"{year}-04-13", f"{year}-04-14", f"{year}-04-15"
            )
        self.assertNoHolidayName(name, Thailand(years=1947))

        self.assertNoHoliday(f"{year}-04-13" for year in range(1954, 1957))
        self.assertNoHolidayName(name, Thailand(years=range(1954, 1957)))

        self.assertHolidaysName(
            name, (f"{year}-04-13" for year in range(1957, 1989))
        )

        for year in range(1989, 1998):
            self.assertHoliday(
                f"{year}-04-12", f"{year}-04-13", f"{year}-04-14"
            )

        for year in range(1998, 2020):
            self.assertHoliday(
                f"{year}-04-13", f"{year}-04-14", f"{year}-04-15"
            )

        self.assertNoHoliday("2020-04-13", "2020-04-14", "2020-04-15")

        for year in range(2021, 2058):
            self.assertHoliday(
                f"{year}-04-13", f"{year}-04-14", f"{year}-04-15"
            )

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2013-04-16",
            "2017-04-17",
            "2018-04-16",
            "2019-04-16",
            "2023-04-17",
        )

    def test_national_labour_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1974, 2058))
        self.assertNoHoliday("1973-05-01")
        self.assertNoHolidayName("National Labour Day", Thailand(years=1973))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
        )

    def test_national_day(self):
        self.assertHoliday(f"{year}-06-24" for year in range(1939, 1960))
        self.assertNoHoliday("1938-06-24", "1960-06-24")
        self.assertNoHolidayName("National Day", Thailand(years=[1938, 1960]))

    def test_coronation_day(self):
        self.assertHoliday(f"{year}-05-05" for year in range(1958, 2017))
        self.assertNoHolidayName(
            "Coronation Day", Thailand(years=range(2017, 2020))
        )
        self.assertHoliday(f"{year}-05-04" for year in range(2020, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2012-05-07",
            "2013-05-06",
            "2024-05-06",
            "2025-05-05",
        )

    def test_queen_suthiday_birthday(self):
        self.assertHoliday(f"{year}-06-03" for year in range(2019, 2058))
        self.assertNoHoliday("2018-06-03")
        self.assertNoHolidayName(
            "HM Queen Suthida's Birthday", Thailand(years=2018)
        )

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2023-06-05",
            "2028-06-05",
        )

    def test_rama_x_birthday(self):
        self.assertHoliday(f"{year}-07-28" for year in range(2017, 2058))
        self.assertNoHoliday("2016-07-28")
        self.assertNoHolidayName(
            "HM King Maha Vajiralongkorn's Birthday", Thailand(years=2016)
        )

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2018-07-30",
            "2019-07-29",
            "2024-07-29",
        )

    def test_queen_sirikit_birthday(self):
        self.assertHoliday(f"{year}-08-12" for year in range(1976, 2058))
        self.assertNoHoliday("1975-08-12")
        self.assertNoHolidayName(
            "HM Queen Sirikit The Queen Mother's Birthday",
            Thailand(years=2016),
        )
        self.assertNoHolidayName(
            "HM Queen Sirikit's Birthday",
            Thailand(years=2017),
        )

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2012-08-13",
            "2017-08-14",
            "2018-08-13",
            "2023-08-14",
        )

    def test_mothers_day(self):
        name = "Mother's Day"
        self.assertHolidaysName(
            name, (f"{year}-04-15" for year in range(1950, 1958))
        )
        self.assertNoHolidayName(name, Thailand(years=range(1958, 1976)))
        self.assertHolidaysName(
            name, (f"{year}-08-12" for year in range(1976, 2058))
        )

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2012-08-13",
            "2017-08-15",
            "2018-08-14",
            "2023-08-15",
        )

    def test_rama_ix_memorial_day(self):
        self.assertHoliday(f"{year}-10-13" for year in range(2017, 2058))
        self.assertNoHoliday("2016-10-13")
        self.assertNoHolidayName(
            "HM King Bhumibol Adulyadej Memorial Day", Thailand(years=2016)
        )

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2018-10-15",
            "2019-10-14",
            "2024-10-14",
        )

    def test_rama_five_memorial_day(self):
        self.assertHoliday(f"{year}-10-23" for year in range(1911, 2058))
        self.assertNoHoliday("1910-10-23")
        self.assertNoHolidayName(
            "Chulalongkorn Memorial Day", Thailand(years=1910)
        )

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2010-10-25",
            "2011-10-24",
            "2016-10-24",
            "2021-10-25",
            "2022-10-24",
        )

    def test_ix_birthday(self):
        self.assertHoliday(f"{year}-12-05" for year in range(1960, 2058))
        self.assertNoHoliday("1959-12-05")
        self.assertNoHolidayName(
            "HM King Bhumibol Adulyadej's Birthday", Thailand(years=1959)
        )

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2010-12-06",
            "2015-12-07",
            "2020-12-07",
            "2021-12-06",
        )

    def test_fathers_day(self):
        name = "Father's Day"
        self.assertHolidaysName(
            name, (f"{year}-12-05" for year in range(1980, 2058))
        )
        self.assertNoHolidayName(name, Thailand(years=1979))

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-12-10" for year in range(1932, 2058))
        self.assertNoHoliday("1931-12-10")
        self.assertNoHolidayName("Constitution Day", Thailand(years=1931))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2011-12-12",
            "2016-12-12",
            "2017-12-11",
            "2022-12-12",
            "2023-12-11",
        )

    def test_new_years_eve(self):
        self.assertHoliday(f"{year}-12-31" for year in range(1941, 2058))
        self.assertNoHoliday("1940-12-31")
        self.assertNoHolidayName("New Year's Eve", Thailand(years=1940))

    def test_makha_bucha(self):
        name = "Makha Bucha"
        dt = (
            "2011-02-18",
            "2012-03-07",
            "2013-02-25",
            "2014-02-14",
            "2015-03-04",
            "2016-02-22",
            "2017-02-11",
            "2018-03-01",
            "2019-02-19",
            "2020-02-08",
            "2021-02-26",
            "2022-02-16",
            "2023-03-06",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=[1941, 2058]))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2017-02-13",
            "2020-02-10",
            "2024-02-26",
        )

    def test_visakha_bucha(self):
        name = "Visakha Bucha"
        dt = (
            "2011-05-17",
            "2012-06-04",
            "2013-05-24",
            "2014-05-13",
            "2015-06-01",
            "2016-05-20",
            "2017-05-10",
            "2018-05-29",
            "2019-05-18",
            "2020-05-06",
            "2021-05-26",
            "2022-05-15",
            "2023-06-03",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=[1941, 2058]))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2019-05-20",
            "2022-05-16",
            "2023-06-06",
        )

    def test_asarnha_bucha(self):
        name = "Asarnha Bucha"
        dt = (
            "2011-07-15",
            "2012-08-02",
            "2013-07-22",
            "2014-07-11",
            "2015-07-30",
            "2016-07-19",
            "2017-07-08",
            "2018-07-27",
            "2019-07-16",
            "2020-07-05",
            "2021-07-24",
            "2022-07-13",
            "2023-08-01",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=[1941, 2058]))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2017-07-10",
            "2021-07-26",
            "2024-07-22",
        )

    def test_khao_phansa(self):
        name = "Buddhist Lent Day"
        dt = (
            "2011-07-16",
            "2012-08-03",
            "2013-07-23",
            "2014-07-12",
            "2015-07-31",
            "2016-07-20",
            "2017-07-09",
            "2018-07-28",
            "2019-07-17",
            "2020-07-06",
            "2021-07-25",
            "2022-07-14",
            "2023-08-02",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=[1941, 2058]))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2014-07-14",
            "2017-07-11",
            "2021-07-27",
        )

    def test_raeknakhwan(self):
        name = "Royal Ploughing Ceremony"
        dt = (
            "2011-05-13",
            "2012-05-09",
            "2013-05-13",
            "2014-05-09",
            "2015-05-13",
            "2016-05-09",
            "2017-05-12",
            "2018-05-14",
            "2019-05-09",
            "2020-05-11",
            "2021-05-13",
            "2022-05-17",
            "2023-05-11",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=[1956, 1999]))

        self.assertHolidaysName(
            name, (f"{year}-05-13" for year in range(1957, 1997))
        )
