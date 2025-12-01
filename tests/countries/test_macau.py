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

from holidays.constants import GOVERNMENT, OPTIONAL, PUBLIC
from holidays.countries.macau import Macau
from tests.common import CommonCountryTests


class TestMacau(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Macau, years=range(1985, 2050))
        cls.government_holidays = Macau(categories=GOVERNMENT, years=range(2005, 2050))
        cls.optional_holidays = Macau(categories=OPTIONAL, years=range(1982, 2050))

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Macau(categories=GOVERNMENT, years=2004))
        self.assertNoHolidays(Macau(categories=OPTIONAL, years=1981))
        self.assertNoHolidays(Macau(categories=PUBLIC, years=1984))

    def test_special_holidays(self):
        dt_optional_full = (
            # https://www.io.gov.mo/pt/legis/rec/111020
            "1998-12-23",
            "1999-02-15",
            "1999-12-20",
            "1999-12-21",
            "2015-09-03",
        )
        dt_optional_half = (
            # https://www.io.gov.mo/pt/legis/rec/111020
            "1998-12-31",
            "1999-12-31",
            "2000-02-04",
        )
        dt_government_full = (
            # https://www.io.gov.mo/pt/legis/rec/111020
            "2008-12-22",
            # https://web.archive.org/web/20171207162948/http://portal.gov.mo/web/guest/info_detail?infoid=1887061
            "2012-10-03",
            "2012-12-31",
            "2014-10-03",
            # https://www.gov.mo/en/public-holidays/year-2020/
            "2020-10-05",
        )
        dt_mandatory = (
            # https://www.dsal.gov.mo/en/text/holiday_table.html
            "2015-09-03"
        )
        self.assertHoliday(dt_mandatory)
        self.assertHoliday(Macau(categories=GOVERNMENT), dt_government_full)
        self.assertHoliday(Macau(categories=OPTIONAL), dt_optional_full, dt_optional_half)

    def test_new_years_day(self):
        name = "元旦"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日", self.government_holidays, "2012-01-02", "2017-01-02"
        )
        self.assertHolidayName(
            f"{name}的補假",
            self.government_holidays,
            "2022-01-03",
            "2023-01-02",
            "2028-01-03",
            "2033-01-03",
            "2034-01-02",
            "2039-01-03",
            "2040-01-02",
            "2045-01-02",
        )

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-01-01" for year in range(1982, 2050))
        )

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1985, 2050)))

    def test_freedom_day(self):
        name = "自由日"

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-04-25" for year in range(1982, 1999))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(2000, 2050))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_labor_day(self):
        name = "勞動節"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日", self.government_holidays, "2011-05-02", "2016-05-02"
        )
        self.assertHolidayName(
            f"{name}的補假",
            self.government_holidays,
            "2021-05-03",
            "2022-05-02",
            "2027-05-03",
            "2032-05-03",
            "2033-05-02",
            "2038-05-03",
            "2039-05-03",
            "2044-05-02",
            "2049-05-03",
        )

        # Optional Holidays
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-05-01" for year in range(1982, 2050))
        )

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1985, 2050)))

    def test_day_of_portugal_camoes_and_the_portuguese_communities(self):
        name = "葡國日、賈梅士日暨葡僑日"

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-06-10" for year in range(1982, 2000))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(2000, 2050))

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-06-10" for year in range(1985, 2000)))
        self.assertNoHolidayName(name, range(2000, 2050))

    def test_assumption_day(self):
        name = "聖母升天"

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-08-15" for year in range(1982, 1987))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(1987, 2050))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_national_day(self):
        name = "中華人民共和國國慶日"
        name_following = f"{name}翌日"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日", self.government_holidays, "2016-10-03", "2017-10-03"
        )
        self.assertHolidayName(
            f"{name}的補假", self.government_holidays, "2022-10-03", "2023-10-04"
        )
        self.assertHolidayName(
            f"{name_following}後首個工作日", self.government_holidays, "2011-10-03", "2016-10-04"
        )
        self.assertHolidayName(
            f"{name_following}的補假", self.government_holidays, "2021-10-04", "2022-10-05"
        )

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-10-01" for year in range(1982, 2050))
        )
        self.assertHolidayName(
            name_following, self.optional_holidays, (f"{year}-10-02" for year in range(2000, 2050))
        )
        self.assertNoHolidayName(name_following, self.optional_holidays, range(1982, 2000))

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-10-01" for year in range(1985, 2050)))

    def test_republic_day(self):
        name = "葡萄牙共和國國慶日"

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-10-05" for year in range(1982, 2000))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(2000, 2050))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_all_saints_day(self):
        name = "諸聖節"

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-11-01" for year in range(1982, 1987))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(1987, 2050))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_all_souls_day(self):
        name = "追思節"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日", self.government_holidays, "2014-11-03", "2019-11-04"
        )
        self.assertHolidayName(
            f"{name}的補假", self.government_holidays, "2024-11-04", "2025-11-03"
        )

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-11-02" for year in range(1982, 2050))
        )

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_restoration_of_independence_day(self):
        name = "恢復獨立紀念日"

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-12-01" for year in range(1982, 2000))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(2000, 2050))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_immaculate_conception(self):
        name = "聖母無原罪瞻禮"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日",
            self.government_holidays,
            "2012-12-10",
            "2013-12-09",
            "2018-12-10",
            "2019-12-09",
        )
        self.assertHolidayName(f"{name}的補假", self.government_holidays, "2024-12-09")

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-12-08" for year in range(1982, 2050))
        )

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_macao_sar_establishment_day(self):
        name = "澳門特別行政區成立紀念日"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日", self.government_holidays, "2014-12-23", "2015-12-21"
        )
        self.assertHolidayName(
            f"{name}的補假", self.government_holidays, "2020-12-22", "2025-12-22"
        )

        # Optional Holidays
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-12-20" for year in range(2000, 2050))
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(1982, 2000))

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-12-20" for year in range(2000, 2050)))
        self.assertNoHolidayName(name, range(1985, 2000))

    def test_winter_solstice(self):
        name = "冬至"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日",
            self.government_holidays,
            "2013-12-23",
            "2018-12-26",
            "2019-12-23",
        )
        self.assertHolidayName(
            f"{name}的補假", self.government_holidays, "2024-12-23", "2025-12-23"
        )

        # Optional Holidays.
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-12-22" for year in range(1982, 2000))
        )
        self.assertHolidayName(
            name,
            self.optional_holidays,
            # Regulamento Administrativo n.º 4/1999.
            "2000-12-21",
            # Ordem Executiva n.º 60/2000.
            "2006-12-22",
            "2007-12-22",
            "2008-12-21",
            "2009-12-22",
            "2010-12-22",
            "2011-12-22",
            "2012-12-21",
            "2013-12-22",
            "2014-12-22",
            "2015-12-22",
            "2016-12-21",
            "2017-12-22",
            "2018-12-22",
            "2019-12-22",
            "2020-12-21",
            "2021-12-21",
            "2022-12-22",
            "2023-12-22",
            "2024-12-21",
            "2025-12-21",
        )
        self.assertHolidayName(name, self.optional_holidays, range(2000, 2050))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_christmas_eve(self):
        name_1982 = "聖誕前夕"
        name_1999 = "聖誕節前夕"
        name_2000 = "聖誕節前日"

        # Government Holidays.
        self.assertHolidayName(
            f"{name_2000}後首個工作日", self.government_holidays, "2016-12-26", "2017-12-26"
        )
        self.assertHolidayName(
            f"{name_2000}的補假", self.government_holidays, "2022-12-26", "2023-12-26"
        )

        # Optional Holidays.
        self.assertHolidayName(
            name_1982, self.optional_holidays, (f"{year}-12-24" for year in range(1982, 1999))
        )
        self.assertHolidayName(name_1999, self.optional_holidays, "1999-12-24")
        self.assertHolidayName(
            name_2000, self.optional_holidays, (f"{year}-12-24" for year in range(2000, 2050))
        )
        self.assertNoHolidayName(name_1982, self.optional_holidays, range(1999, 2050))
        self.assertNoHolidayName(
            name_1999, self.optional_holidays, range(1982, 1999), range(2000, 2050)
        )
        self.assertNoHolidayName(name_2000, self.optional_holidays, range(1982, 2000))

        # Public Holidays.
        self.assertNoHolidayName(name_1982)
        self.assertNoHolidayName(name_1999)
        self.assertNoHolidayName(name_2000)

    def test_christmas_day(self):
        name_1982 = "聖誕"
        name_1999 = "聖誕節"

        # Government Holidays.
        self.assertHolidayName(
            f"{name_1999}後首個工作日", self.government_holidays, "2011-12-26", "2016-12-27"
        )
        self.assertHolidayName(
            f"{name_1999}的補假", self.government_holidays, "2021-12-27", "2022-12-27"
        )

        # Optional Holidays.
        self.assertHolidayName(
            name_1982, self.optional_holidays, (f"{year}-12-25" for year in range(1982, 1999))
        )
        self.assertHolidayName(
            name_1999, self.optional_holidays, (f"{year}-12-25" for year in range(1999, 2050))
        )
        self.assertNoHolidayName(name_1982, self.optional_holidays, range(1999, 2050))
        self.assertNoHolidayName(name_1999, self.optional_holidays, range(1982, 1999))

        # Public Holidays.
        self.assertNoHolidayName(name_1982)
        self.assertNoHolidayName(name_1999)

    def test_chinese_new_year(self):
        name_eve_afternoon = "農曆除夕（下午）"
        name_d1 = "農曆正月初一"
        name_d2 = "農曆正月初二"
        name_d3 = "農曆正月初三"
        name_d4 = "農曆正月初四"
        name_d5 = "農曆正月初五"
        name_d1_obs = f"{name_d1}的補假"
        name_d2_obs = f"{name_d2}的補假"
        name_d3_obs = f"{name_d3}的補假"

        # Government Holidays.
        self.assertHolidayName(
            name_eve_afternoon,
            self.government_holidays,
            "2005-02-08",
            "2008-02-06",
            "2011-02-02",
            "2014-01-30",
            "2015-02-18",
            "2017-01-27",
            "2018-02-15",
            "2019-02-04",
            "2020-01-24",
            "2021-02-11",
            "2022-01-31",
            "2024-02-09",
            "2025-01-28",
        )
        self.assertHolidayName(name_eve_afternoon, self.government_holidays, range(2024, 2050))
        self.assertNoHolidayName(
            name_eve_afternoon,
            self.government_holidays,
            2006,
            2007,
            2009,
            2010,
            2012,
            2013,
            2016,
            2023,
        )
        self.assertNoHolidayName(name_eve_afternoon)

        self.assertHolidayName(
            name_d4,
            self.government_holidays,
            "2006-02-01",
            "2007-02-21",
            "2010-02-17",
            "2013-02-13",
            "2014-02-03",
            "2017-01-31",
            "2018-02-19",
        )
        self.assertNoHolidayName(
            name_d4,
            self.government_holidays,
            2005,
            2008,
            2009,
            2011,
            2012,
            2015,
            2016,
            range(2019, 2050),
        )
        self.assertNoHolidayName(name_d4)

        self.assertHolidayName(
            name_d5,
            self.government_holidays,
            "2014-02-04",
            "2015-02-23",
            "2017-02-01",
            "2018-02-20",
        )
        self.assertNoHolidayName(
            name_d5, self.government_holidays, range(2005, 2014), 2016, range(2019, 2050)
        )
        self.assertNoHolidayName(name_d5)

        self.assertHolidayName(
            name_d1_obs,
            self.government_holidays,
            "2020-01-28",
            "2023-01-25",
            "2024-02-13",
        )
        self.assertNoHolidayName(name_d1_obs)

        self.assertHolidayName(
            name_d2_obs,
            self.government_holidays,
            "2020-01-29",
            "2021-02-15",
            "2024-02-14",
        )
        self.assertNoHolidayName(name_d2_obs)

        self.assertHolidayName(
            name_d3_obs,
            self.government_holidays,
            "2021-02-16",
        )
        self.assertNoHolidayName(name_d3_obs)

        # Optional Holidays.
        dt = (
            "2009-01-26",
            "2010-02-14",
            "2011-02-03",
            "2012-01-23",
            "2014-01-31",
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2024-02-10",
            "2025-01-29",
        )
        self.assertHolidayName(name_d1, self.optional_holidays, dt)
        self.assertHolidayName(name_d1, self.optional_holidays, range(1982, 2050))
        self.assertHolidayName(name_d2, self.optional_holidays, range(1982, 2050))
        self.assertHolidayName(name_d3, self.optional_holidays, range(1982, 2050))

        # Public Holidays.
        self.assertHolidayName(name_d1, dt)
        self.assertHolidayName(name_d1, range(1985, 2050))
        self.assertHolidayName(name_d2, range(1985, 2050))
        self.assertHolidayName(name_d3, range(1985, 2050))

    def test_tomb_sweeping_day(self):
        name = "清明節"
        dt = (
            "2009-04-04",
            "2011-04-05",
            "2012-04-04",
            "2013-04-04",
            "2014-04-05",
            "2016-04-04",
            "2017-04-04",
            "2018-04-05",
            "2019-04-05",
            "2020-04-04",
            "2022-04-05",
            "2023-04-05",
            "2024-04-04",
            "2025-04-04",
        )

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日", self.government_holidays, "2014-04-07", "2015-04-07"
        )
        self.assertHolidayName(
            f"{name}的補假", self.government_holidays, "2020-04-06", "2021-04-06"
        )

        # Optional Holidays.
        self.assertHolidayName(name, self.optional_holidays, dt)
        self.assertHolidayName(name, self.optional_holidays, range(1982, 2050))

        # Public Holidays.
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1989, 2050))
        self.assertNoHolidayName(name, range(1985, 1989))

    def test_good_friday(self):
        name_1982 = "聖周星期五"
        name_2000 = "耶穌受難日"

        # Optional Holidays.
        self.assertHolidayName(
            name_2000,
            self.optional_holidays,
            "2009-04-10",
            "2010-04-02",
            "2011-04-22",
            "2012-04-06",
            "2013-03-29",
            "2014-04-18",
            "2015-04-03",
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name_1982, self.optional_holidays, range(1982, 2000))
        self.assertHolidayName(name_2000, self.optional_holidays, range(2000, 2050))
        self.assertNoHolidayName(name_1982, self.optional_holidays, range(2000, 2050))
        self.assertNoHolidayName(name_2000, self.optional_holidays, range(1982, 2000))

        # Public Holidays.
        self.assertNoHolidayName(name_1982)
        self.assertNoHolidayName(name_2000)

    def test_the_day_before_easter(self):
        name_1982 = "聖周星期六"
        name_2000 = "復活節前日"

        # Government Holiday.
        name_2000_obs_2005 = f"{name_2000}後首個工作日"
        name_2000_obs_2020 = f"{name_2000}的補假"
        self.assertHolidayName(
            name_2000_obs_2005,
            self.government_holidays,
            "2012-04-09",
            "2013-04-01",
            "2014-04-21",
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
        )
        self.assertHolidayName(
            name_2000_obs_2020,
            self.government_holidays,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name_2000_obs_2020, self.government_holidays, range(2020, 2050))
        self.assertNoHolidayName(
            name_2000_obs_2005,
            self.government_holidays,
            range(2005, 2012),
            range(2020, 2050),
        )
        self.assertNoHolidayName(name_2000_obs_2020, self.government_holidays, range(1982, 2020))
        self.assertNoHolidayName(name_2000_obs_2005)
        self.assertNoHolidayName(name_2000_obs_2020)

        # Optional Holidays.
        self.assertHolidayName(
            name_2000,
            self.optional_holidays,
            "2009-04-11",
            "2010-04-03",
            "2011-04-23",
            "2012-04-07",
            "2013-03-30",
            "2014-04-19",
            "2015-04-04",
            "2016-03-26",
            "2017-04-15",
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertHolidayName(name_1982, self.optional_holidays, range(1982, 2000))
        self.assertHolidayName(name_2000, self.optional_holidays, range(2000, 2050))
        self.assertNoHolidayName(name_1982, self.optional_holidays, range(2000, 2050))
        self.assertNoHolidayName(name_2000, self.optional_holidays, range(1982, 2000))

        # Public Holidays.
        self.assertNoHolidayName(name_1982)
        self.assertNoHolidayName(name_2000)

    def test_the_buddhas_birthday(self):
        name = "佛誕節"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日",
            self.government_holidays,
            "2012-04-30",
            "2016-05-16",
            "2019-05-13",
        )
        self.assertHolidayName(f"{name}的補假", self.government_holidays, "2022-05-09")

        # Optional Holidays.
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "2022-05-08",
            "2023-05-26",
            "2024-05-15",
            "2025-05-05",
            "2026-05-24",
            "2027-05-13",
            "2028-05-02",
            "2029-05-20",
            "2030-05-09",
            "2031-05-28",
            "2032-05-16",
            "2033-05-06",
            "2034-05-25",
            "2035-05-15",
        )
        self.assertHolidayName(name, self.optional_holidays, range(2000, 2050))
        self.assertNoHolidayName(name, self.optional_holidays, range(1982, 2000))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_corpus_christi(self):
        name = "基督聖體聖血節"

        # Optional Holidays.
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "1982-06-10",
            "1983-06-02",
            "1984-06-21",
            "1985-06-06",
            "1986-05-29",
            "1987-06-18",
        )
        self.assertNoHolidayName(name, self.optional_holidays, range(1988, 2050))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_dragon_boat_festival(self):
        name = "端午節"

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日", self.government_holidays, "2012-06-25", "2015-06-22"
        )
        self.assertHolidayName(f"{name}的補假", self.government_holidays, "2025-06-02")

        # Optional Holidays.
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "2009-05-28",
            "2010-06-16",
            "2011-06-06",
            "2012-06-23",
            "2013-06-12",
            "2014-06-02",
            "2015-06-20",
            "2016-06-09",
            "2017-05-30",
            "2018-06-18",
            "2019-06-07",
            "2020-06-25",
            "2021-06-14",
            "2022-06-03",
            "2023-06-22",
            "2024-06-10",
            "2025-05-31",
        )
        self.assertHolidayName(name, self.optional_holidays, range(1982, 2050))

        # Public Holidays.
        self.assertNoHolidayName(name)

    def test_double_ninth_festival(self):
        name = "重陽節"
        dt = (
            "2009-10-26",
            "2010-10-16",
            "2011-10-05",
            "2012-10-23",
            "2013-10-13",
            "2014-10-02",
            "2015-10-21",
            "2016-10-09",
            "2017-10-28",
            "2018-10-17",
            "2019-10-07",
            "2020-10-25",
            "2021-10-14",
            "2022-10-04",
            "2023-10-23",
            "2024-10-11",
            "2025-10-29",
        )

        # Government Holidays.
        self.assertHolidayName(
            f"{name}後首個工作日",
            self.government_holidays,
            "2013-10-14",
            "2016-10-10",
            "2017-10-30",
        )
        self.assertHolidayName(f"{name}的補假", self.government_holidays, "2020-10-26")

        # Optional Holidays.
        self.assertHolidayName(name, self.optional_holidays, dt)
        self.assertHolidayName(name, self.optional_holidays, range(1982, 2050))

        # Public Holidays.
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1985, 2050))

    def test_mid_autumn_festival(self):
        name = "中秋節"

        # Public Holidays.
        self.assertHolidayName(
            name,
            "1985-09-29",
            "1986-09-18",
            "1987-10-07",
            "1988-09-25",
            "1989-09-14",
            "1990-10-03",
            "1991-09-22",
            "1992-09-11",
            "1993-09-30",
            "1994-09-20",
            "1995-09-09",
            "1996-09-27",
            "1997-09-16",
            "1998-10-05",
            "1999-09-24",
        )
        self.assertNoHolidayName(name, range(2000, 2050))

    def test_the_day_following_mid_autumn_festival(self):
        name = "中秋節翌日"
        dt = (
            "2009-10-04",
            "2010-09-23",
            "2011-09-13",
            "2012-10-01",
            "2013-09-20",
            "2014-09-09",
            "2015-09-28",
            "2016-09-16",
            "2017-10-05",
            "2018-09-25",
            "2019-09-14",
            "2020-10-02",
            "2021-09-22",
            "2023-09-30",
            "2024-09-18",
            "2025-10-07",
        )

        # Government Holidays.
        self.assertHolidayName(f"{name}後首個工作日", self.government_holidays, "2019-09-16")
        self.assertHolidayName(
            f"{name}的補假", self.government_holidays, "2022-09-12", "2023-10-03"
        )

        # Optional Holidays.
        self.assertHolidayName(name, self.optional_holidays, dt)
        self.assertHolidayName(name, self.optional_holidays, range(1982, 2050))

        # Public Holidays.
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2000, 2050))
        self.assertNoHolidayName(name, range(1985, 2000))

    def test_new_years_eve(self):
        name = "除夕"
        name_afternoon = f"{name}（下午）"

        # Government Holidays.
        self.assertHolidayName(name, self.government_holidays, "2012-12-31")
        self.assertNoHolidayName(name)

        self.assertHolidayName(
            name_afternoon,
            self.government_holidays,
            (
                f"{year}-12-31"
                for year in (
                    *range(2007, 2011),
                    *range(2013, 2016),
                    *range(2018, 2022),
                    *range(2024, 2050),
                )
            ),
        )
        self.assertNoHolidayName(
            name_afternoon, self.government_holidays, 2011, 2012, 2016, 2017, 2022, 2023
        )
        self.assertNoHolidayName(name_afternoon)

    def test_macau_city_day(self):
        name = "澳門市日"

        # Optional Holidays.
        m_optional_holidays = Macau(categories=OPTIONAL, subdiv="M", years=range(1982, 2023))
        self.assertHolidayName(
            name, m_optional_holidays, (f"{year}-06-24" for year in range(1982, 2000))
        )
        self.assertNoHolidayName(name, m_optional_holidays, range(2000, 2050))
        self.assertNoHolidayName(name)

    def test_day_of_the_municipality_of_ilhas(self):
        name = "海島市日"

        # Optional Holidays.
        i_optional_holidays = Macau(categories=OPTIONAL, subdiv="I", years=range(1982, 2023))
        self.assertHolidayName(
            name, i_optional_holidays, (f"{year}-11-30" for year in range(1982, 1993))
        )
        self.assertHolidayName(
            name, i_optional_holidays, (f"{year}-07-13" for year in range(1993, 2000))
        )
        self.assertNoHolidayName(name, i_optional_holidays, range(2000, 2050))
        self.assertNoHolidayName(name)

    def test_2024_government(self):
        # https://www.gov.mo/en/public-holidays/year-2024/
        dt = (
            # Exemption from work granted to public employees by the Chief Executive.
            "2024-02-09",
            "2024-12-31",
        )
        dt_observed = (
            # Compensatory rest days for public employees set forth in
            # No. 4 of Article 79 of the ETAPM.
            "2024-02-13",
            "2024-02-14",
            "2024-04-01",
            "2024-11-04",
            "2024-12-09",
            "2024-12-23",
        )
        self.assertHoliday(Macau(categories=GOVERNMENT, years=2024), dt, dt_observed)
        self.assertNoNonObservedHoliday(
            Macau(categories=GOVERNMENT, years=2024, observed=False), dt_observed
        )

    def test_2024_public(self):
        # https://www.dsal.gov.mo/en/text/holiday_table.html
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "元旦"),
            ("2024-02-10", "農曆正月初一"),
            ("2024-02-11", "農曆正月初二"),
            ("2024-02-12", "農曆正月初三"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "中華人民共和國國慶日"),
            ("2024-10-11", "重陽節"),
            ("2024-12-20", "澳門特別行政區成立紀念日"),
        )

    def test_2017_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2017/
        self.assertOptionalHolidaysInYear(
            2017,
            ("2017-01-01", "元旦"),
            ("2017-01-28", "農曆正月初一"),
            ("2017-01-29", "農曆正月初二"),
            ("2017-01-30", "農曆正月初三"),
            ("2017-04-04", "清明節"),
            ("2017-04-14", "耶穌受難日"),
            ("2017-04-15", "復活節前日"),
            ("2017-05-01", "勞動節"),
            ("2017-05-03", "佛誕節"),
            ("2017-05-30", "端午節"),
            ("2017-10-01", "中華人民共和國國慶日"),
            ("2017-10-02", "中華人民共和國國慶日翌日"),
            ("2017-10-05", "中秋節翌日"),
            ("2017-10-28", "重陽節"),
            ("2017-11-02", "追思節"),
            ("2017-12-08", "聖母無原罪瞻禮"),
            ("2017-12-20", "澳門特別行政區成立紀念日"),
            ("2017-12-22", "冬至"),
            ("2017-12-24", "聖誕節前日"),
            ("2017-12-25", "聖誕節"),
        )

    def test_2018_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2018/
        self.assertOptionalHolidaysInYear(
            2018,
            ("2018-01-01", "元旦"),
            ("2018-02-16", "農曆正月初一"),
            ("2018-02-17", "農曆正月初二"),
            ("2018-02-18", "農曆正月初三"),
            ("2018-03-30", "耶穌受難日"),
            ("2018-03-31", "復活節前日"),
            ("2018-04-05", "清明節"),
            ("2018-05-01", "勞動節"),
            ("2018-05-22", "佛誕節"),
            ("2018-06-18", "端午節"),
            ("2018-09-25", "中秋節翌日"),
            ("2018-10-01", "中華人民共和國國慶日"),
            ("2018-10-02", "中華人民共和國國慶日翌日"),
            ("2018-10-17", "重陽節"),
            ("2018-11-02", "追思節"),
            ("2018-12-08", "聖母無原罪瞻禮"),
            ("2018-12-20", "澳門特別行政區成立紀念日"),
            ("2018-12-22", "冬至"),
            ("2018-12-24", "聖誕節前日"),
            ("2018-12-25", "聖誕節"),
        )

    def test_2019_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2019/
        self.assertOptionalHolidaysInYear(
            2019,
            ("2019-01-01", "元旦"),
            ("2019-02-05", "農曆正月初一"),
            ("2019-02-06", "農曆正月初二"),
            ("2019-02-07", "農曆正月初三"),
            ("2019-04-05", "清明節"),
            ("2019-04-19", "耶穌受難日"),
            ("2019-04-20", "復活節前日"),
            ("2019-05-01", "勞動節"),
            ("2019-05-12", "佛誕節"),
            ("2019-06-07", "端午節"),
            ("2019-09-14", "中秋節翌日"),
            ("2019-10-01", "中華人民共和國國慶日"),
            ("2019-10-02", "中華人民共和國國慶日翌日"),
            ("2019-10-07", "重陽節"),
            ("2019-11-02", "追思節"),
            ("2019-12-08", "聖母無原罪瞻禮"),
            ("2019-12-20", "澳門特別行政區成立紀念日"),
            ("2019-12-22", "冬至"),
            ("2019-12-24", "聖誕節前日"),
            ("2019-12-25", "聖誕節"),
        )

    def test_2020_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2020/
        self.assertOptionalHolidaysInYear(
            2020,
            ("2020-01-01", "元旦"),
            ("2020-01-25", "農曆正月初一"),
            ("2020-01-26", "農曆正月初二"),
            ("2020-01-27", "農曆正月初三"),
            ("2020-04-04", "清明節"),
            ("2020-04-10", "耶穌受難日"),
            ("2020-04-11", "復活節前日"),
            ("2020-04-30", "佛誕節"),
            ("2020-05-01", "勞動節"),
            ("2020-06-25", "端午節"),
            ("2020-10-01", "中華人民共和國國慶日"),
            ("2020-10-02", "中秋節翌日; 中華人民共和國國慶日翌日"),
            ("2020-10-25", "重陽節"),
            ("2020-11-02", "追思節"),
            ("2020-12-08", "聖母無原罪瞻禮"),
            ("2020-12-20", "澳門特別行政區成立紀念日"),
            ("2020-12-21", "冬至"),
            ("2020-12-24", "聖誕節前日"),
            ("2020-12-25", "聖誕節"),
        )

    def test_2021_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2021/
        self.assertOptionalHolidaysInYear(
            2021,
            ("2021-01-01", "元旦"),
            ("2021-02-12", "農曆正月初一"),
            ("2021-02-13", "農曆正月初二"),
            ("2021-02-14", "農曆正月初三"),
            ("2021-04-02", "耶穌受難日"),
            ("2021-04-03", "復活節前日"),
            ("2021-04-04", "清明節"),
            ("2021-05-01", "勞動節"),
            ("2021-05-19", "佛誕節"),
            ("2021-06-14", "端午節"),
            ("2021-09-22", "中秋節翌日"),
            ("2021-10-01", "中華人民共和國國慶日"),
            ("2021-10-02", "中華人民共和國國慶日翌日"),
            ("2021-10-14", "重陽節"),
            ("2021-11-02", "追思節"),
            ("2021-12-08", "聖母無原罪瞻禮"),
            ("2021-12-20", "澳門特別行政區成立紀念日"),
            ("2021-12-21", "冬至"),
            ("2021-12-24", "聖誕節前日"),
            ("2021-12-25", "聖誕節"),
        )

    def test_2022_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2022/
        self.assertOptionalHolidaysInYear(
            2022,
            ("2022-01-01", "元旦"),
            ("2022-02-01", "農曆正月初一"),
            ("2022-02-02", "農曆正月初二"),
            ("2022-02-03", "農曆正月初三"),
            ("2022-04-05", "清明節"),
            ("2022-04-15", "耶穌受難日"),
            ("2022-04-16", "復活節前日"),
            ("2022-05-01", "勞動節"),
            ("2022-05-08", "佛誕節"),
            ("2022-06-03", "端午節"),
            ("2022-09-11", "中秋節翌日"),
            ("2022-10-01", "中華人民共和國國慶日"),
            ("2022-10-02", "中華人民共和國國慶日翌日"),
            ("2022-10-04", "重陽節"),
            ("2022-11-02", "追思節"),
            ("2022-12-08", "聖母無原罪瞻禮"),
            ("2022-12-20", "澳門特別行政區成立紀念日"),
            ("2022-12-22", "冬至"),
            ("2022-12-24", "聖誕節前日"),
            ("2022-12-25", "聖誕節"),
        )

    def test_2023_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2023/
        self.assertOptionalHolidaysInYear(
            2023,
            ("2023-01-01", "元旦"),
            ("2023-01-22", "農曆正月初一"),
            ("2023-01-23", "農曆正月初二"),
            ("2023-01-24", "農曆正月初三"),
            ("2023-04-05", "清明節"),
            ("2023-04-07", "耶穌受難日"),
            ("2023-04-08", "復活節前日"),
            ("2023-05-01", "勞動節"),
            ("2023-05-26", "佛誕節"),
            ("2023-06-22", "端午節"),
            ("2023-09-30", "中秋節翌日"),
            ("2023-10-01", "中華人民共和國國慶日"),
            ("2023-10-02", "中華人民共和國國慶日翌日"),
            ("2023-10-23", "重陽節"),
            ("2023-11-02", "追思節"),
            ("2023-12-08", "聖母無原罪瞻禮"),
            ("2023-12-20", "澳門特別行政區成立紀念日"),
            ("2023-12-22", "冬至"),
            ("2023-12-24", "聖誕節前日"),
            ("2023-12-25", "聖誕節"),
        )

    def test_2024_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2024/
        self.assertOptionalHolidaysInYear(
            2024,
            ("2024-01-01", "元旦"),
            ("2024-02-10", "農曆正月初一"),
            ("2024-02-11", "農曆正月初二"),
            ("2024-02-12", "農曆正月初三"),
            ("2024-03-29", "耶穌受難日"),
            ("2024-03-30", "復活節前日"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-05-15", "佛誕節"),
            ("2024-06-10", "端午節"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "中華人民共和國國慶日"),
            ("2024-10-02", "中華人民共和國國慶日翌日"),
            ("2024-10-11", "重陽節"),
            ("2024-11-02", "追思節"),
            ("2024-12-08", "聖母無原罪瞻禮"),
            ("2024-12-20", "澳門特別行政區成立紀念日"),
            ("2024-12-21", "冬至"),
            ("2024-12-24", "聖誕節前日"),
            ("2024-12-25", "聖誕節"),
        )

    def test_2025_optional(self):
        # https://www.gov.mo/en/public-holidays/year-2025/
        self.assertOptionalHolidaysInYear(
            2025,
            ("2025-01-01", "元旦"),
            ("2025-01-29", "農曆正月初一"),
            ("2025-01-30", "農曆正月初二"),
            ("2025-01-31", "農曆正月初三"),
            ("2025-04-04", "清明節"),
            ("2025-04-18", "耶穌受難日"),
            ("2025-04-19", "復活節前日"),
            ("2025-05-01", "勞動節"),
            ("2025-05-05", "佛誕節"),
            ("2025-05-31", "端午節"),
            ("2025-10-01", "中華人民共和國國慶日"),
            ("2025-10-02", "中華人民共和國國慶日翌日"),
            ("2025-10-07", "中秋節翌日"),
            ("2025-10-29", "重陽節"),
            ("2025-11-02", "追思節"),
            ("2025-12-08", "聖母無原罪瞻禮"),
            ("2025-12-20", "澳門特別行政區成立紀念日"),
            ("2025-12-21", "冬至"),
            ("2025-12-24", "聖誕節前日"),
            ("2025-12-25", "聖誕節"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "元旦"),
            ("2024-02-09", "農曆除夕（下午）"),
            ("2024-02-10", "農曆正月初一"),
            ("2024-02-11", "農曆正月初二"),
            ("2024-02-12", "農曆正月初三"),
            ("2024-02-13", "農曆正月初一的補假"),
            ("2024-02-14", "農曆正月初二的補假"),
            ("2024-03-29", "耶穌受難日"),
            ("2024-03-30", "復活節前日"),
            ("2024-04-01", "復活節前日的補假"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-05-15", "佛誕節"),
            ("2024-06-10", "端午節"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "中華人民共和國國慶日"),
            ("2024-10-02", "中華人民共和國國慶日翌日"),
            ("2024-10-11", "重陽節"),
            ("2024-11-02", "追思節"),
            ("2024-11-04", "追思節的補假"),
            ("2024-12-08", "聖母無原罪瞻禮"),
            ("2024-12-09", "聖母無原罪瞻禮的補假"),
            ("2024-12-20", "澳門特別行政區成立紀念日"),
            ("2024-12-21", "冬至"),
            ("2024-12-23", "冬至的補假"),
            ("2024-12-24", "聖誕節前日"),
            ("2024-12-25", "聖誕節"),
            ("2024-12-31", "除夕（下午）"),
        )

    def test_l10n_en_mo(self):
        self.assertLocalizedHolidays(
            "en_MO",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Lunar New Year's Eve (Afternoon)"),
            ("2024-02-10", "Lunar New Year's Day"),
            ("2024-02-11", "The second day of Lunar New Year"),
            ("2024-02-12", "The third day of Lunar New Year"),
            ("2024-02-13", "Compensatory rest day for Lunar New Year's Day"),
            ("2024-02-14", "Compensatory rest day for The second day of Lunar New Year"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "The Day before Easter"),
            ("2024-04-01", "Compensatory rest day for The Day before Easter"),
            ("2024-04-04", "Ching Ming Festival"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-15", "The Buddha's Birthday (Feast of Buddha)"),
            ("2024-06-10", "Tung Ng Festival (Dragon Boat Festival)"),
            ("2024-09-18", "The Day following Chong Chao (Mid-Autumn) Festival"),
            ("2024-10-01", "National Day of the People's Republic of China"),
            ("2024-10-02", "The day following National Day of the People's Republic of China"),
            ("2024-10-11", "Chung Yeung Festival (Festival of Ancestors)"),
            ("2024-11-02", "All Soul's Day"),
            ("2024-11-04", "Compensatory rest day for All Soul's Day"),
            ("2024-12-08", "Immaculate Conception"),
            ("2024-12-09", "Compensatory rest day for Immaculate Conception"),
            ("2024-12-20", "Macao S.A.R. Establishment Day"),
            ("2024-12-21", "Winter Solstice"),
            ("2024-12-23", "Compensatory rest day for Winter Solstice"),
            ("2024-12-24", "Christmas Eve"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-31", "New Year's Eve (Afternoon)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Chinese New Year's Eve (Afternoon)"),
            ("2024-02-10", "Chinese New Year's Day"),
            ("2024-02-11", "The second day of Chinese New Year"),
            ("2024-02-12", "The third day of Chinese New Year"),
            ("2024-02-13", "Compensatory rest day for Chinese New Year's Day"),
            ("2024-02-14", "Compensatory rest day for The second day of Chinese New Year"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "The Day before Easter"),
            ("2024-04-01", "Compensatory rest day for The Day before Easter"),
            ("2024-04-04", "Tomb-Sweeping Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-15", "The Buddha's Birthday"),
            ("2024-06-10", "Dragon Boat Festival"),
            ("2024-09-18", "The Day following Mid-Autumn Festival"),
            ("2024-10-01", "National Day of the People's Republic of China"),
            ("2024-10-02", "The day following National Day of the People's Republic of China"),
            ("2024-10-11", "Double Ninth Festival"),
            ("2024-11-02", "All Soul's Day"),
            ("2024-11-04", "Compensatory rest day for All Soul's Day"),
            ("2024-12-08", "Immaculate Conception"),
            ("2024-12-09", "Compensatory rest day for Immaculate Conception"),
            ("2024-12-20", "Macao S.A.R. Establishment Day"),
            ("2024-12-21", "Winter Solstice"),
            ("2024-12-23", "Compensatory rest day for Winter Solstice"),
            ("2024-12-24", "Christmas Eve"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-31", "New Year's Eve (Afternoon)"),
        )

    def test_l10n_pt_mo(self):
        self.assertLocalizedHolidays(
            "pt_MO",
            ("2024-01-01", "Fraternidade Universal"),
            ("2024-02-09", "Véspera do Novo Ano Lunar (na parte da tarde)"),
            ("2024-02-10", "1.º dia do Novo Ano Lunar"),
            ("2024-02-11", "2.º dia do Novo Ano Lunar"),
            ("2024-02-12", "3.º dia do Novo Ano Lunar"),
            ("2024-02-13", "Dia de descanso compensatório relativo ao 1.º dia do Novo Ano Lunar"),
            ("2024-02-14", "Dia de descanso compensatório relativo ao 2.º dia do Novo Ano Lunar"),
            ("2024-03-29", "Morte de Cristo"),
            ("2024-03-30", "Véspera da Ressurreição de Cristo"),
            (
                "2024-04-01",
                "Dia de descanso compensatório relativo ao Véspera da Ressurreição de Cristo",
            ),
            ("2024-04-04", "Cheng Ming (Dia de Finados)"),
            ("2024-05-01", "Dia do Trabalhador"),
            ("2024-05-15", "Dia do Buda"),
            ("2024-06-10", "Tung Ng (Barco Dragão)"),
            ("2024-09-18", "Dia seguinte ao Chong Chao (Bolo Lunar)"),
            ("2024-10-01", "Implantação da República Popular da China"),
            ("2024-10-02", "Dia seguinte à Implantação da República Popular da China"),
            ("2024-10-11", "Chong Yeong (Culto dos Antepassados)"),
            ("2024-11-02", "Dia de Finados"),
            ("2024-11-04", "Dia de descanso compensatório relativo ao Dia de Finados"),
            ("2024-12-08", "Imaculada Conceição"),
            ("2024-12-09", "Dia de descanso compensatório relativo ao Imaculada Conceição"),
            (
                "2024-12-20",
                "Dia Comemorativo do Estabelecimento da Região Administrativa Especial de Macau",
            ),
            ("2024-12-21", "Solstício de Inverno"),
            ("2024-12-23", "Dia de descanso compensatório relativo ao Solstício de Inverno"),
            ("2024-12-24", "Véspera de Natal"),
            ("2024-12-25", "Natal"),
            ("2024-12-31", "Véspera do Dia da Fraternidade Universal (na parte da tarde)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-02-09", "วันก่อนวันตรุษจีน (ครึ่งบ่าย)"),
            ("2024-02-10", "วันตรุษจีน"),
            ("2024-02-11", "วันตรุษจีนวันที่สอง"),
            ("2024-02-12", "วันตรุษจีนวันที่สาม"),
            ("2024-02-13", "ชดเชยวันตรุษจีน"),
            ("2024-02-14", "ชดเชยวันตรุษจีนวันที่สอง"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-03-30", "วันก่อนวันอาทิตย์อีสเตอร์"),
            ("2024-04-01", "ชดเชยวันก่อนวันอาทิตย์อีสเตอร์"),
            ("2024-04-04", "วันเช็งเม้ง"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-05-15", "วันวิสาขบูชา"),
            ("2024-06-10", "วันไหว้บ๊ะจ่าง"),
            ("2024-09-18", "วันหลังวันไหว้พระจันทร์"),
            ("2024-10-01", "วันชาติจีน"),
            ("2024-10-02", "วันหลังวันชาติจีน"),
            ("2024-10-11", "วันไหว้บรรพบุรุษ"),
            ("2024-11-02", "วันภาวนาอุทิศแด่ผู้ล่วงลับ"),
            ("2024-11-04", "ชดเชยวันภาวนาอุทิศแด่ผู้ล่วงลับ"),
            ("2024-12-08", "วันสมโภชแม่พระผู้ปฏิสนธินิรมล"),
            ("2024-12-09", "ชดเชยวันสมโภชแม่พระผู้ปฏิสนธินิรมล"),
            ("2024-12-20", "วันสถาปนาเขตบริหารพิเศษมาเก๊า"),
            ("2024-12-21", "วันตงจื้อ(เหมายัน)"),
            ("2024-12-23", "ชดเชยวันตงจื้อ(เหมายัน)"),
            ("2024-12-24", "วันคริสต์มาสอีฟ"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-31", "วันสิ้นปี (ครึ่งบ่าย)"),
        )

    def test_l10n_zh_cn(self):
        self.assertLocalizedHolidays(
            "zh_CN",
            ("2024-01-01", "元旦"),
            ("2024-02-09", "农历除夕（下午）"),
            ("2024-02-10", "农历正月初一"),
            ("2024-02-11", "农历正月初二"),
            ("2024-02-12", "农历正月初三"),
            ("2024-02-13", "农历正月初一的补假"),
            ("2024-02-14", "农历正月初二的补假"),
            ("2024-03-29", "耶稣受难日"),
            ("2024-03-30", "复活节前日"),
            ("2024-04-01", "复活节前日的补假"),
            ("2024-04-04", "清明节"),
            ("2024-05-01", "劳动节"),
            ("2024-05-15", "佛诞节"),
            ("2024-06-10", "端午节"),
            ("2024-09-18", "中秋节翌日"),
            ("2024-10-01", "中华人民共和国国庆日"),
            ("2024-10-02", "中华人民共和国国庆日翌日"),
            ("2024-10-11", "重阳节"),
            ("2024-11-02", "追思节"),
            ("2024-11-04", "追思节的补假"),
            ("2024-12-08", "圣母无原罪瞻礼"),
            ("2024-12-09", "圣母无原罪瞻礼的补假"),
            ("2024-12-20", "澳门特别行政区成立纪念日"),
            ("2024-12-21", "冬至"),
            ("2024-12-23", "冬至的补假"),
            ("2024-12-24", "圣诞节前日"),
            ("2024-12-25", "圣诞节"),
            ("2024-12-31", "除夕（下午）"),
        )
