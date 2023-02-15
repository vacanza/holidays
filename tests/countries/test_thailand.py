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
from tests.common import TestCase


class TestThailand(TestCase):
    def setUp(self):
        super().setUp()
        # Checks in lieu not observed until 2030
        self.holidays_no_observed = Thailand(observed=False)

    @classmethod
    def setUpClass(cls):
        super().setUpClass(Thailand)

    def test_country_aliases(self):
        self.assertCountryAliases(Thailand, TH, THA)

    def test_no_holidays(self):
        self.assertNoHolidays(Thailand(years=1940))

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
                "HM Queen Sirikit The Queen Mother's Birthday; National Mother's Day",  # noqa: E501
            ),
            ("2022-10-13", "HM King Bhumibol Adulyadej Memorial Day"),
            ("2022-10-14", "Bridge Public Holiday"),
            ("2022-10-23", "Chulalongkorn Memorial Day"),
            ("2022-10-24", "Chulalongkorn Memorial Day (in lieu)"),
            (
                "2022-12-05",
                "HM King Bhumibol Adulyadej's Birthday; National Father's Day",
            ),
            ("2022-12-10", "Constitution Day"),
            ("2022-12-12", "Constitution Day (in lieu)"),
            ("2022-12-30", "Bridge Public Holiday"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1941, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
            "2028-01-03",
        )

    def test_chakri_memorial_day(self):
        self.assertHoliday(f"{year}-04-06" for year in range(1941, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2013-04-08",
            "2014-04-07",
            "2019-04-08",
            "2024-04-08",
            "2025-04-07",
            "2030-04-08",
        )

    def test_songkran_festival(self):
        name = "Songkran Festival"

        self.assertNoHolidayName(name, Thailand(years=1947))
        for year in range(1948, 1954):
            self.assertHoliday(
                f"{year}-04-13", f"{year}-04-14", f"{year}-04-15"
            )
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
            "2012-04-16",
            "2013-04-16",
            "2017-04-17",
            "2018-04-16",
            "2019-04-16",
            # 2020 Songkran Festival special in lieus doesn't counts
            "2023-04-17",
            "2024-04-16",
            "2028-04-17",
            "2029-04-16",
            "2030-04-16",
        )

    def test_national_labour_day(self):
        name = "National Labour Day"

        self.assertNoHoliday("1973-05-01")
        self.assertNoHolidayName(name, Thailand(years=1973))
        self.assertHoliday(f"{year}-05-01" for year in range(1974, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
            "2027-05-03",
        )

    def test_coronation_day(self):
        name = "Coronation Day"

        self.assertNoHoliday("1957-05-05")
        self.assertNoHolidayName(name, Thailand(years=1957))
        self.assertHoliday(f"{year}-05-05" for year in range(1958, 2017))
        self.assertNoHolidayName(name, Thailand(years=range(2017, 2020)))
        self.assertHoliday(f"{year}-05-04" for year in range(2020, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2012-05-07",
            "2013-05-06",
            "2024-05-06",
            "2025-05-05",
            "2030-05-06",
        )

    def test_queen_suthida_birthday(self):
        name = "HM Queen Suthida's Birthday"

        self.assertNoHoliday("2018-06-03")
        self.assertNoHolidayName(name, Thailand(years=2018))
        self.assertHoliday(f"{year}-06-03" for year in range(2019, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2023-06-05",
            "2028-06-05",
            "2029-06-04",
        )

    def test_national_day(self):
        name = "National Day"

        self.assertHoliday(f"{year}-06-24" for year in range(1941, 1960))
        self.assertNoHoliday("1960-06-24")
        self.assertNoHolidayName(name, Thailand(years=1960))

        # No in lieus during its existense

    def test_rama_x_birthday(self):
        name = "HM King Maha Vajiralongkorn's Birthday"

        self.assertNoHoliday("2016-07-28")
        self.assertNoHolidayName(name, Thailand(years=2016))
        self.assertHoliday(f"{year}-07-28" for year in range(2017, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2018-07-30",
            "2019-07-29",
            "2024-07-29",
            "2029-07-30",
            "2030-07-29",
        )

    def test_queen_sirikit_birthday(self):
        name_ix = "HM Queen Sirikit's Birthday"
        name_x = "HM Queen Sirikit The Queen Mother's Birthday"

        self.assertNoHoliday("1975-08-12")
        self.assertNoHolidayName(name_ix, Thailand(years=1975))
        self.assertHolidaysName(
            name_ix, (f"{year}-08-12" for year in range(1976, 2017))
        )
        self.assertNoHolidayName(name_x, Thailand(years=range(1941, 2017)))
        self.assertHolidaysName(
            name_x, (f"{year}-08-12" for year in range(2017, 2058))
        )
        self.assertNoHolidayName(name_ix, Thailand(years=range(2017, 2058)))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2012-08-13",
            "2017-08-14",
            "2018-08-13",
            "2023-08-14",
            "2028-08-14",
            "2029-08-13",
        )

    def test_national_mothers_day(self):
        name = "National Mother's Day"

        self.assertNoHolidayName(name, Thailand(years=1949))
        self.assertHolidaysName(
            name, (f"{year}-04-15" for year in range(1950, 1958))
        )
        self.assertNoHolidayName(name, Thailand(years=range(1958, 1976)))
        self.assertHolidaysName(
            name, (f"{year}-08-12" for year in range(1976, 2058))
        )

        # April 15 (1950-1958) exists prior to in lieu laws
        # In lieus are same as HM Queen Sirikit's Birthday

    def test_rama_ix_memorial_day(self):
        name = "HM King Bhumibol Adulyadej Memorial Day"
        self.assertHoliday(f"{year}-10-13" for year in range(2017, 2058))
        self.assertNoHoliday("2016-10-13")
        self.assertNoHolidayName(name, Thailand(years=2016))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2018-10-15",
            "2019-10-14",
            "2024-10-14",
            "2029-10-15",
            "2030-10-14",
        )

    def test_rama_five_memorial_day(self):
        name = "Chulalongkorn Memorial Day"
        self.assertHoliday(f"{year}-10-23" for year in range(1941, 2058))
        self.assertNoHoliday("1910-10-23", "1940-10-23")
        self.assertNoHolidayName(name, Thailand(years=[1910, 1940]))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2010-10-25",
            "2011-10-24",
            "2016-10-24",
            "2021-10-25",
            "2022-10-24",
            "2027-10-25",
        )

    def test_rama_ix_birthday(self):
        name = "HM King Bhumibol Adulyadej's Birthday"

        self.assertNoHoliday("1959-12-05")
        self.assertNoHolidayName(name, Thailand(years=1959))
        self.assertHoliday(f"{year}-12-05" for year in range(1960, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2010-12-06",
            "2015-12-07",
            "2020-12-07",
            "2021-12-06",
            "2026-12-07",
            "2027-12-06",
        )

    def test_national_fathers_day(self):
        name = "National Father's Day"

        # This concides with HM King Bhumibol Adulyadej's Birthday
        self.assertNoHolidayName(name, Thailand(years=1979))
        self.assertHolidaysName(
            name, (f"{year}-12-05" for year in range(1980, 2058))
        )

        # In lieus are same as HM King Bhumibol Adulyadej's Birthday

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-12-10" for year in range(1941, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2011-12-12",
            "2016-12-12",
            "2017-12-11",
            "2022-12-12",
            "2023-12-11",
            "2028-12-11",
        )

    def test_new_years_eve(self):
        self.assertHoliday(f"{year}-12-31" for year in range(1941, 2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2012-01-03",
            "2017-01-03",
            "2018-01-02",
            "2023-01-03",
            "2024-01-02",
            "2029-01-02",
        )

    def test_makha_bucha(self):
        name = "Makha Bucha"

        dt = (
            "2010-02-28",
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
            "2024-02-24",
            "2025-02-12",
            "2026-03-03",
            "2027-02-21",
            "2028-02-10",
            "2029-02-27",
            "2030-02-17",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2010-03-01",
            "2017-02-13",
            "2020-02-10",
            "2024-02-26",
            "2024-02-22",
            "2030-02-18",
        )

    def test_visakha_bucha(self):
        name = "Visakha Bucha"

        dt = (
            "2010-05-28",
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
            "2024-05-22",
            "2025-05-11",
            "2026-05-31",
            "2027-05-20",
            "2028-05-08",
            "2029-05-27",
            "2030-05-16",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2019-05-20",
            "2022-05-16",
            "2023-06-05",
            "2025-05-12",
            "2026-06-01",
            "2029-05-28",
        )

    def test_asarnha_bucha(self):
        name = "Asarnha Bucha"

        dt = (
            "2010-07-26",
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
            "2024-07-20",
            "2025-07-10",
            "2026-07-29",
            "2027-07-18",
            "2028-07-06",
            "2029-07-25",
            "2030-07-14",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2017-07-10",
            "2020-07-07",
            "2021-07-26",
            "2024-07-22",
            "2027-07-20",
            "2030-07-16",
        )

    def test_khao_phansa(self):
        name = "Buddhist Lent Day"

        dt = (
            "2010-07-27",
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
            "2024-07-21",
            "2025-07-11",
            "2026-07-30",
            "2027-07-19",
            "2028-07-07",
            "2029-07-26",
            "2030-07-15",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoHolidayName(name, Thailand(years=2058))

        self.assertNoHoliday(
            self.holidays_no_observed,
            "2011-07-18",
            "2014-07-14",
            "2018-07-30",
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

        # No Royal Ploughing Ceremony on weekend for 1997-2023

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                th_en = Thailand(language=language)
                self.assertEqual(th_en["2022-01-01"], "New Year's Day")
                self.assertEqual(th_en["2022-04-13"], "Songkran Festival")
                self.assertEqual(
                    th_en["2022-05-02"], "National Labour Day (in lieu)"
                )
                self.assertEqual(th_en["2022-12-10"], "Constitution Day")

        run_tests((Thailand.default_language, None, "invalid"))

        self.set_locale("th")
        run_tests((Thailand.default_language,))

    def test_l10n_th(self):
        language = "th"

        th_th = Thailand(language=language)
        self.assertEqual(th_th["2022-01-01"], "วันขึ้นปีใหม่")
        self.assertEqual(th_th["2022-04-13"], "วันสงกรานต์")
        self.assertEqual(th_th["2022-05-02"], "ชดเชยวันแรงงานแห่งชาติ")
        self.assertEqual(th_th["2022-12-10"], "วันรัฐธรรมนูญ")

        self.set_locale(language)
        for language in (None, language, "invalid"):
            th_th = Thailand(language=language)
            self.assertEqual(th_th["2022-01-01"], "วันขึ้นปีใหม่")
            self.assertEqual(th_th["2022-04-13"], "วันสงกรานต์")
            self.assertEqual(th_th["2022-05-02"], "ชดเชยวันแรงงานแห่งชาติ")
            self.assertEqual(th_th["2022-12-10"], "วันรัฐธรรมนูญ")
