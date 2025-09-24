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

from holidays.constants import GOVERNMENT, OPTIONAL, PUBLIC, SCHOOL, WORKDAY
from holidays.countries.taiwan import Taiwan, TW, TWN
from tests.common import CommonCountryTests, WorkingDayTests


class TestTaiwan(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Taiwan)

    def test_country_aliases(self):
        self.assertAliases(Taiwan, TW, TWN)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Taiwan(years=self.start_year - 1, categories=(OPTIONAL, PUBLIC, WORKDAY))
        )
        self.assertNoHolidays(
            Taiwan(years=(self.start_year - 1, 2001), categories=(GOVERNMENT, SCHOOL))
        )

    def test_substituted_holidays(self):
        self.assertHoliday(
            "2000-04-03",
            "2001-01-22",
            "2005-02-07",
            "2006-10-09",
            "2007-02-23",
            "2007-04-06",
            "2007-06-18",
            "2007-09-24",
            "2009-01-02",
            "2009-01-30",
            "2009-05-29",
            "2010-02-19",
            "2012-01-27",
            "2012-02-27",
            "2012-12-31",
            "2013-02-15",
            "2013-09-20",
            "2015-01-02",
            "2016-02-12",
            "2016-06-10",
            "2016-09-16",
            "2017-02-27",
            "2017-05-29",
            "2017-10-09",
            "2018-04-06",
            "2018-12-31",
            "2019-02-08",
            "2019-03-01",
            "2019-10-11",
            "2020-01-23",
            "2020-06-26",
            "2020-10-02",
            "2021-02-10",
            "2021-09-20",
            "2022-02-04",
            "2023-01-20",
            "2023-01-27",
            "2023-02-27",
            "2023-04-03",
            "2023-06-23",
            "2023-10-09",
            "2024-02-08",
            "2025-01-27",
        )

    def test_workdays(self):
        self.assertWorkingDay(
            "2000-04-08",
            "2001-01-20",
            "2005-02-05",
            "2006-10-14",
            "2007-03-03",
            "2007-04-14",
            "2007-06-23",
            "2007-09-29",
            "2009-01-10",
            "2009-01-17",
            "2009-06-06",
            "2010-02-06",
            "2012-02-04",
            "2012-03-03",
            "2012-12-22",
            "2013-02-23",
            "2013-09-14",
            "2014-12-27",
            "2016-01-30",
            "2016-06-04",
            "2016-09-10",
            "2017-02-18",
            "2017-06-03",
            "2017-09-30",
            "2018-03-31",
            "2018-12-22",
            "2019-01-19",
            "2019-02-23",
            "2019-10-05",
            "2020-02-15",
            "2020-06-20",
            "2020-09-26",
            "2021-02-20",
            "2021-09-11",
            "2022-01-22",
            "2023-01-07",
            "2023-02-04",
            "2023-02-18",
            "2023-03-25",
            "2023-06-17",
            "2023-09-23",
            "2024-02-17",
            "2025-02-08",
        )

        for year, dts in {
            2014: ("2014-12-27",),
        }.items():
            self.assertWorkingDay(Taiwan(years=year), dts)

    def test_foundation_day_of_the_republic_of_china(self):
        name = "中華民國開國紀念日"

        # Government Holidays.
        self.assertGovernmentHolidayName(
            name, (f"{year}-01-02" for year in range(self.start_year, 2001))
        )
        self.assertNoGovernmentHolidayName(name, range(2001, self.end_year))

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dt = (
            "1999-01-02",
            "2017-01-02",
            "2021-12-31",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        # School Holidays.
        self.assertSchoolHolidayName(
            name, (f"{year}-01-02" for year in range(self.start_year, 2001))
        )
        self.assertNoSchoolHolidayName(name, range(2001, self.end_year))

    def test_chinese_new_year(self):
        name_eve = "農曆除夕"
        name = "春節"

        # Public Holidays.
        self.assertHolidayName(
            name_eve,
            "2011-02-02",
            "2012-01-22",
            "2013-02-09",
            "2014-01-30",
            "2015-02-18",
            "2016-02-07",
            "2017-01-27",
            "2018-02-15",
            "2019-02-04",
            "2020-01-24",
            "2021-02-11",
            "2022-01-31",
            "2023-01-21",
            "2024-02-09",
            "2025-01-28",
            "2026-02-15",
            "2026-02-16",
        )
        self.assertHolidayName(name_eve, self.full_range)
        # CNY itself.
        self.assertHolidayName(
            name,
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
            "2024-02-10",
        )
        # CNY Day 2.
        self.assertHolidayName(
            name,
            "2015-02-20",
            "2016-02-09",
            "2017-01-29",
            "2018-02-17",
            "2019-02-06",
            "2020-01-26",
            "2021-02-13",
            "2022-02-02",
            "2023-01-23",
            "2024-02-11",
        )
        # CNY Day 3.
        self.assertHolidayName(
            name,
            "2015-02-21",
            "2016-02-10",
            "2017-01-30",
            "2018-02-18",
            "2019-02-07",
            "2020-01-27",
            "2021-02-14",
            "2022-02-03",
            "2023-01-24",
            "2024-02-12",
        )
        self.assertHolidayName(name, self.full_range)
        obs_eve_dt = (
            "2006-02-01",
            "2007-02-21",
            "2009-01-29",
            "2010-02-17",
            "2012-01-26",
            "2013-02-13",
            "2016-02-11",
            "2023-01-25",
            "2026-02-20",
        )
        obs_dt = (
            "1998-01-31",
            "2003-02-04",
            "2003-02-05",
            "2004-01-26",
            "2006-02-02",
            "2007-02-22",
            "2008-02-11",
            "2010-02-18",
            "2011-02-07",
            "2013-02-14",
            "2014-02-03",
            "2014-02-04",
            "2015-02-23",
            "2017-01-31",
            "2017-02-01",
            "2018-02-19",
            "2018-02-20",
            "2020-01-28",
            "2020-01-29",
            "2021-02-15",
            "2021-02-16",
            "2023-01-26",
            "2024-02-13",
        )
        self.assertHolidayName(f"{name_eve}（補假）", obs_eve_dt)
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_eve_dt, obs_dt)

    def test_taoism_day(self):
        name = "道教節"

        # Workdays.
        self.assertWorkdayHolidayName(
            name,
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
            "2024-02-10",
        )
        self.assertWorkdayHolidayName(name, range(2001, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2001))
        self.assertNoHolidayName(name)

    def test_peace_memorial_day(self):
        name = "和平紀念日"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-02-28" for year in self.full_range))
        obs_dt = (
            "2015-02-27",
            "2016-02-29",
            "2021-03-01",
        )
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_arbor_day(self):
        name = "植樹節"

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-03-12" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_dr_sun_yat_sens_memorial_day(self):
        name = "國父逝世紀念日"

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-03-12" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_anti_aggression_day(self):
        name = "反侵略日"

        # Workdays.
        self.assertWorkdayHolidayName(
            name, (f"{year}-03-14" for year in range(2006, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2006))
        self.assertNoHolidayName(name)

    def test_revolutionary_martyrs_memorial_day(self):
        name = "革命先烈紀念日"

        # Government Holidays.
        self.assertGovernmentHolidayName(
            name, (f"{year}-03-29" for year in range(self.start_year, 2001))
        )
        self.assertNoGovernmentHolidayName(name, range(2001, self.end_year))

        # Workdays.
        self.assertWorkdayHolidayName(
            name, (f"{year}-03-29" for year in range(2001, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2000))
        self.assertNoHolidayName(name)

    def test_youth_day(self):
        name = "青年節"

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-03-29" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_childrens_day(self):
        name = "兒童節"

        # Optional Holidays.
        obs_dt = (
            "1998-04-04",
            "1999-04-04",
            "2000-04-03",
        )
        self.assertOptionalHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoOptionalNonObservedHoliday(obs_dt)

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-04-04" for year in range(2011, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2011))
        obs_dt = (
            "2013-04-05",
            "2015-04-03",
            "2016-04-05",
            "2017-04-03",
            "2020-04-03",
            "2021-04-02",
            "2024-04-05",
            "2025-04-03",
        )
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        # Workdays.
        self.assertWorkdayHolidayName(
            name, (f"{year}-04-04" for year in range(self.start_year, 2011))
        )
        self.assertNoWorkdayHolidayName(name, range(2011, self.end_year))

    def test_womens_day(self):
        name = "婦女節"

        # Optional Holidays.
        obs_dt = (
            "1998-04-04",
            "1999-04-04",
            "2000-04-03",
        )
        self.assertOptionalHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoOptionalNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name)

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-03-08" for year in self.full_range))

    def test_tomb_sweeping_day(self):
        name = "民族掃墓節"

        # Public Holidays.
        self.assertHolidayName(
            name,
            "2011-04-05",
            "2012-04-04",
            "2013-04-04",
            "2014-04-05",
            "2015-04-05",
            "2016-04-04",
            "2017-04-04",
            "2018-04-05",
            "2019-04-05",
            "2020-04-04",
            "2021-04-04",
            "2022-04-05",
            "2023-04-05",
        )
        self.assertNoHolidayName(name, Taiwan(years=1971))
        obs_dt = (
            "1998-04-06",
            "2015-04-06",
            "2020-04-02",
            "2021-04-05",
        )
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_late_president_chiang_kai_sheks_memorial_day(self):
        name = "先總統蔣公逝世紀念日"

        # Workdays.
        self.assertWorkdayHolidayName(
            name,
            "1998-04-05",
            "2000-04-04",
            "2001-04-05",
            "2002-04-05",
            "2003-04-05",
            "2004-04-04",
            "2005-04-05",
            "2006-04-05",
            "2007-04-05",
        )
        self.assertNoWorkdayHolidayName(name, range(2008, self.end_year))
        self.assertNoHolidayName(name)

    def test_labor_day(self):
        name = "勞動節"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2026))

        # Optional Holidays.
        self.assertOptionalHolidayName(
            name, (f"{year}-05-01" for year in range(self.start_year, 2026))
        )
        self.assertNoOptionalHolidayName(name, range(2026, self.end_year))

    def test_the_buddhas_birthday(self):
        name = "佛陀誕辰紀念日"

        # Public Holidays.
        self.assertNoHolidayName(name)
        obs_dt = ("2000-05-14",)
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        # Workdays.
        self.assertWorkdayHolidayName(
            name,
            "2011-05-10",
            "2012-04-28",
            "2013-05-17",
            "2014-05-06",
            "2015-05-25",
            "2016-05-14",
            "2017-05-03",
            "2018-05-22",
            "2019-05-12",
            "2020-04-30",
            "2021-05-19",
            "2022-05-08",
            "2023-05-26",
        )
        self.assertWorkdayHolidayName(name, range(2000, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2000))

    def test_dragon_boat_festival(self):
        name = "端午節"

        # Public Holidays.
        self.assertHolidayName(
            name,
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
        )
        obs_dt = (
            "1999-06-19",
            "2015-06-19",
            "2025-05-30",
        )
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_commemoration_day_of_the_lifting_of_martial_law(self):
        name = "解嚴紀念日"

        # Workdays.
        self.assertWorkdayHolidayName(
            name, (f"{year}-07-15" for year in range(2008, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2008))
        self.assertNoHolidayName(name)

    def test_armed_forces_day(self):
        name = "軍人節"

        # Optional Holidays.
        self.assertOptionalHolidayName(name, (f"{year}-09-03" for year in self.full_range))
        obs_dt = ("2000-09-04",)
        self.assertOptionalHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoOptionalNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name)

    def test_mid_autumn_festival(self):
        name = "中秋節"

        # Public Holidays.
        self.assertHolidayName(
            name,
            "2011-09-12",
            "2012-09-30",
            "2013-09-19",
            "2014-09-08",
            "2015-09-27",
            "2016-09-15",
            "2017-10-04",
            "2018-09-24",
            "2019-09-13",
            "2020-10-01",
            "2021-09-21",
            "2022-09-10",
            "2023-09-29",
        )
        obs_dt = (
            "2015-09-28",
            "2022-09-09",
        )
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_day(self):
        name = "國慶日"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-10-10" for year in self.full_range))
        obs_dt = (
            "2015-10-09",
            "2020-10-09",
            "2021-10-11",
        )
        self.assertHolidayName(f"{name}（補假）", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_confucius_birthday(self):
        name = "孔子誕辰紀念日"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-09-28" for year in range(2025, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2025))

        # Government Holidays.
        self.assertGovernmentHolidayName(
            name, (f"{year}-09-28" for year in range(self.start_year, 2001))
        )
        self.assertNoGovernmentHolidayName(name, range(2001, self.end_year))

        # School Holidays.
        self.assertSchoolHolidayName(
            name, (f"{year}-09-28" for year in range(self.start_year, 2001))
        )
        self.assertNoSchoolHolidayName(name, range(2001, self.end_year))

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-09-28" for year in range(2001, 2025)))
        self.assertNoWorkdayHolidayName(
            name, range(self.start_year, 2000), range(2025, self.end_year)
        )

    def test_teachers_day(self):
        name = "教師節"

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-09-28" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_taiwan_united_nations_day(self):
        name = "臺灣聯合國日"

        # Workdays.
        self.assertWorkdayHolidayName(
            name, (f"{year}-10-24" for year in range(2008, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2008))
        self.assertNoHolidayName(name)

    def test_taiwan_retrocession_day(self):
        name_old = "臺灣光復節"
        name_new = "臺灣光復暨金門古寧頭大捷紀念日"

        # Public Holidays.
        self.assertHolidayName(name_new, (f"{year}-10-25" for year in range(2025, self.end_year)))
        self.assertNoHolidayName(name_new, range(self.start_year, 2025))
        self.assertNoHolidayName(name_old)

        # Government Holidays.
        self.assertGovernmentHolidayName(
            name_old, (f"{year}-10-25" for year in range(self.start_year, 2001))
        )
        self.assertNoGovernmentHolidayName(name_old, range(2001, self.end_year))

        # School Holidays.
        self.assertSchoolHolidayName(
            name_old, (f"{year}-10-25" for year in range(self.start_year, 2001))
        )
        self.assertNoSchoolHolidayName(name_old, range(2001, self.end_year))

        # Workdays.
        self.assertWorkdayHolidayName(name_old, (f"{year}-10-25" for year in range(2001, 2025)))
        self.assertNoWorkdayHolidayName(
            name_old, range(self.start_year, 2000), range(2025, self.end_year)
        )

    def test_late_president_chiang_kai_sheks_birthday(self):
        name = "先總統　蔣公誕辰紀念日"

        # Government Holidays.
        self.assertGovernmentHolidayName(
            name, (f"{year}-10-31" for year in range(self.start_year, 2001))
        )
        self.assertNoGovernmentHolidayName(name, range(2001, self.end_year))

        # School Holidays.
        self.assertSchoolHolidayName(
            name, (f"{year}-10-31" for year in range(self.start_year, 2001))
        )
        self.assertNoSchoolHolidayName(name, range(2001, self.end_year))

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-10-31" for year in range(2001, 2007)))
        self.assertNoWorkdayHolidayName(
            name, range(self.start_year, 2000), range(2007, self.end_year)
        )
        self.assertNoHolidayName(name)

    def test_dr_sun_yat_sens_birthday(self):
        name = "國父誕辰紀念日"

        # Government Holidays.
        self.assertGovernmentHolidayName(
            name, (f"{year}-11-12" for year in range(self.start_year, 2001))
        )
        self.assertNoGovernmentHolidayName(name, range(2001, self.end_year))

        # School Holidays.
        self.assertSchoolHolidayName(
            name, (f"{year}-11-12" for year in range(self.start_year, 2001))
        )
        self.assertNoSchoolHolidayName(name, range(2001, self.end_year))

        # Workdays.
        self.assertWorkdayHolidayName(
            name, (f"{year}-11-12" for year in range(2001, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2000))
        self.assertNoHolidayName(name)

    def test_chinese_cultural_renaissance_day(self):
        name = "中華文化復興節"

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-11-12" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_constitution_day(self):
        name = "行憲紀念日"

        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2025, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2025))

        # Government Holidays.
        self.assertGovernmentHolidayName(
            name, (f"{year}-12-25" for year in range(self.start_year, 2001))
        )
        self.assertNoGovernmentHolidayName(name, range(2001, self.end_year))

        # School Holidays.
        self.assertSchoolHolidayName(
            name, (f"{year}-12-25" for year in range(self.start_year, 2001))
        )
        self.assertNoSchoolHolidayName(name, range(2001, self.end_year))

        # Workdays.
        self.assertWorkdayHolidayName(name, (f"{year}-12-25" for year in range(2001, 2025)))
        self.assertNoWorkdayHolidayName(
            name, range(self.start_year, 2000), range(2025, self.end_year)
        )

    def test_1998(self):
        self.assertHolidays(
            Taiwan(years=1998),
            ("1998-01-01", "中華民國開國紀念日"),
            ("1998-01-27", "農曆除夕"),
            ("1998-01-28", "春節"),
            ("1998-01-29", "春節"),
            ("1998-01-30", "春節"),
            ("1998-01-31", "春節（補假）"),
            ("1998-02-28", "和平紀念日"),
            ("1998-04-05", "民族掃墓節"),
            ("1998-04-06", "民族掃墓節（補假）"),
            ("1998-05-30", "端午節"),
            ("1998-10-05", "中秋節"),
            ("1998-10-10", "國慶日"),
        )

    def test_1999(self):
        self.assertHolidays(
            Taiwan(years=1999),
            ("1999-01-01", "中華民國開國紀念日"),
            ("1999-01-02", "中華民國開國紀念日（補假）"),
            ("1999-02-15", "農曆除夕"),
            ("1999-02-16", "春節"),
            ("1999-02-17", "春節"),
            ("1999-02-18", "春節"),
            ("1999-02-28", "和平紀念日"),
            ("1999-04-05", "民族掃墓節"),
            ("1999-06-18", "端午節"),
            ("1999-06-19", "端午節（補假）"),
            ("1999-09-24", "中秋節"),
            ("1999-10-10", "國慶日"),
        )

    def test_2000(self):
        self.assertHolidays(
            Taiwan(years=2000),
            ("2000-01-01", "中華民國開國紀念日"),
            ("2000-02-04", "農曆除夕"),
            ("2000-02-05", "春節"),
            ("2000-02-06", "春節"),
            ("2000-02-07", "春節"),
            ("2000-02-28", "和平紀念日"),
            ("2000-04-03", "休息日（2000-04-08日起取代）"),
            ("2000-04-04", "民族掃墓節"),
            ("2000-05-14", "佛陀誕辰紀念日（補假）"),
            ("2000-06-06", "端午節"),
            ("2000-09-12", "中秋節"),
            ("2000-10-10", "國慶日"),
        )

    def test_2001(self):
        self.assertHolidays(
            Taiwan(years=2001),
            ("2001-01-01", "中華民國開國紀念日"),
            ("2001-01-22", "休息日（2001-01-20日起取代）"),
            ("2001-01-23", "農曆除夕"),
            ("2001-01-24", "春節"),
            ("2001-01-25", "春節"),
            ("2001-01-26", "春節"),
            ("2001-02-28", "和平紀念日"),
            ("2001-04-05", "民族掃墓節"),
            ("2001-06-25", "端午節"),
            ("2001-10-01", "中秋節"),
            ("2001-10-10", "國慶日"),
        )

    def test_2002(self):
        self.assertHolidays(
            Taiwan(years=2002),
            ("2002-01-01", "中華民國開國紀念日"),
            ("2002-04-05", "民族掃墓節"),
            ("2002-02-11", "農曆除夕"),
            ("2002-02-12", "春節"),
            ("2002-02-13", "春節"),
            ("2002-02-14", "春節"),
            ("2002-02-28", "和平紀念日"),
            ("2002-06-15", "端午節"),
            ("2002-09-21", "中秋節"),
            ("2002-10-10", "國慶日"),
        )

    def test_2003(self):
        self.assertHolidays(
            Taiwan(years=2003),
            ("2003-01-01", "中華民國開國紀念日"),
            ("2003-01-31", "農曆除夕"),
            ("2003-02-01", "春節"),
            ("2003-02-02", "春節"),
            ("2003-02-03", "春節"),
            ("2003-02-04", "春節（補假）"),
            ("2003-02-05", "春節（補假）"),
            ("2003-02-28", "和平紀念日"),
            ("2003-04-05", "民族掃墓節"),
            ("2003-06-04", "端午節"),
            ("2003-09-11", "中秋節"),
            ("2003-10-10", "國慶日"),
        )

    def test_2004(self):
        self.assertHolidays(
            Taiwan(years=2004),
            ("2004-01-01", "中華民國開國紀念日"),
            ("2004-01-21", "農曆除夕"),
            ("2004-01-22", "春節"),
            ("2004-01-23", "春節"),
            ("2004-01-24", "春節"),
            ("2004-01-26", "春節（補假）"),
            ("2004-02-28", "和平紀念日"),
            ("2004-04-04", "民族掃墓節"),
            ("2004-06-22", "端午節"),
            ("2004-09-28", "中秋節"),
            ("2004-10-10", "國慶日"),
        )

    def test_2005(self):
        self.assertHolidays(
            Taiwan(years=2005),
            ("2005-01-01", "中華民國開國紀念日"),
            ("2005-02-07", "休息日（2005-02-05日起取代）"),
            ("2005-02-08", "農曆除夕"),
            ("2005-02-09", "春節"),
            ("2005-02-10", "春節"),
            ("2005-02-11", "春節"),
            ("2005-02-28", "和平紀念日"),
            ("2005-04-05", "民族掃墓節"),
            ("2005-06-11", "端午節"),
            ("2005-09-18", "中秋節"),
            ("2005-10-10", "國慶日"),
        )

    def test_2006(self):
        self.assertHolidays(
            Taiwan(years=2006),
            ("2006-01-01", "中華民國開國紀念日"),
            ("2006-01-28", "農曆除夕"),
            ("2006-01-29", "春節"),
            ("2006-01-30", "春節"),
            ("2006-01-31", "春節"),
            ("2006-02-01", "農曆除夕（補假）"),
            ("2006-02-02", "春節（補假）"),
            ("2006-02-28", "和平紀念日"),
            ("2006-04-05", "民族掃墓節"),
            ("2006-05-31", "端午節"),
            ("2006-10-06", "中秋節"),
            ("2006-10-09", "休息日（2006-10-14日起取代）"),
            ("2006-10-10", "國慶日"),
        )

    def test_2007(self):
        self.assertHolidays(
            Taiwan(years=2007),
            ("2007-01-01", "中華民國開國紀念日"),
            ("2007-02-17", "農曆除夕"),
            ("2007-02-18", "春節"),
            ("2007-02-19", "春節"),
            ("2007-02-20", "春節"),
            ("2007-02-21", "農曆除夕（補假）"),
            ("2007-02-22", "春節（補假）"),
            ("2007-02-23", "休息日（2007-03-03日起取代）"),
            ("2007-02-28", "和平紀念日"),
            ("2007-04-05", "民族掃墓節"),
            ("2007-04-06", "休息日（2007-04-14日起取代）"),
            ("2007-06-18", "休息日（2007-06-23日起取代）"),
            ("2007-06-19", "端午節"),
            ("2007-09-24", "休息日（2007-09-29日起取代）"),
            ("2007-09-25", "中秋節"),
            ("2007-10-10", "國慶日"),
        )

    def test_2008(self):
        self.assertHolidays(
            Taiwan(years=2008),
            ("2008-01-01", "中華民國開國紀念日"),
            ("2008-02-06", "農曆除夕"),
            ("2008-02-07", "春節"),
            ("2008-02-08", "春節"),
            ("2008-02-09", "春節"),
            ("2008-02-11", "春節（補假）"),
            ("2008-02-28", "和平紀念日"),
            ("2008-04-04", "民族掃墓節"),
            ("2008-06-08", "端午節"),
            ("2008-09-14", "中秋節"),
            ("2008-10-10", "國慶日"),
        )

    def test_2009(self):
        self.assertHolidays(
            Taiwan(years=2009),
            ("2009-01-01", "中華民國開國紀念日"),
            ("2009-01-02", "休息日（2009-01-10日起取代）"),
            ("2009-01-25", "農曆除夕"),
            ("2009-01-26", "春節"),
            ("2009-01-27", "春節"),
            ("2009-01-28", "春節"),
            ("2009-01-29", "農曆除夕（補假）"),
            ("2009-01-30", "休息日（2009-01-17日起取代）"),
            ("2009-02-28", "和平紀念日"),
            ("2009-04-04", "民族掃墓節"),
            ("2009-05-28", "端午節"),
            ("2009-05-29", "休息日（2009-06-06日起取代）"),
            ("2009-10-03", "中秋節"),
            ("2009-10-10", "國慶日"),
        )

    def test_2010(self):
        self.assertHolidays(
            Taiwan(years=2010),
            ("2010-01-01", "中華民國開國紀念日"),
            ("2010-02-13", "農曆除夕"),
            ("2010-02-14", "春節"),
            ("2010-02-15", "春節"),
            ("2010-02-16", "春節"),
            ("2010-02-17", "農曆除夕（補假）"),
            ("2010-02-18", "春節（補假）"),
            ("2010-02-19", "休息日（2010-02-06日起取代）"),
            ("2010-02-28", "和平紀念日"),
            ("2010-04-05", "民族掃墓節"),
            ("2010-06-16", "端午節"),
            ("2010-09-22", "中秋節"),
            ("2010-10-10", "國慶日"),
        )

    def test_2011(self):
        self.assertHolidays(
            Taiwan(years=2011),
            ("2011-01-01", "中華民國開國紀念日"),
            ("2011-02-02", "農曆除夕"),
            ("2011-02-03", "春節"),
            ("2011-02-04", "春節"),
            ("2011-02-05", "春節"),
            ("2011-02-07", "春節（補假）"),
            ("2011-02-28", "和平紀念日"),
            ("2011-04-04", "兒童節"),
            ("2011-04-05", "民族掃墓節"),
            ("2011-06-06", "端午節"),
            ("2011-09-12", "中秋節"),
            ("2011-10-10", "國慶日"),
        )

    def test_2012(self):
        self.assertHolidays(
            Taiwan(years=2012),
            ("2012-01-01", "中華民國開國紀念日"),
            ("2012-01-22", "農曆除夕"),
            ("2012-01-23", "春節"),
            ("2012-01-24", "春節"),
            ("2012-01-25", "春節"),
            ("2012-01-26", "農曆除夕（補假）"),
            ("2012-01-27", "休息日（2012-02-04日起取代）"),
            ("2012-02-27", "休息日（2012-03-03日起取代）"),
            ("2012-02-28", "和平紀念日"),
            ("2012-04-04", "兒童節; 民族掃墓節"),
            ("2012-06-23", "端午節"),
            ("2012-09-30", "中秋節"),
            ("2012-10-10", "國慶日"),
            ("2012-12-31", "休息日（2012-12-22日起取代）"),
        )

    def test_2013(self):
        self.assertHolidays(
            Taiwan(years=2013),
            ("2013-01-01", "中華民國開國紀念日"),
            ("2013-02-09", "農曆除夕"),
            ("2013-02-10", "春節"),
            ("2013-02-11", "春節"),
            ("2013-02-12", "春節"),
            ("2013-02-13", "農曆除夕（補假）"),
            ("2013-02-14", "春節（補假）"),
            ("2013-02-15", "休息日（2013-02-23日起取代）"),
            ("2013-02-28", "和平紀念日"),
            ("2013-04-04", "兒童節; 民族掃墓節"),
            ("2013-04-05", "兒童節（補假）"),
            ("2013-06-12", "端午節"),
            ("2013-09-19", "中秋節"),
            ("2013-09-20", "休息日（2013-09-14日起取代）"),
            ("2013-10-10", "國慶日"),
        )

    def test_2014(self):
        self.assertHolidays(
            Taiwan(years=2014),
            ("2014-01-01", "中華民國開國紀念日"),
            ("2014-01-30", "農曆除夕"),
            ("2014-01-31", "春節"),
            ("2014-02-01", "春節"),
            ("2014-02-02", "春節"),
            ("2014-02-03", "春節（補假）"),
            ("2014-02-04", "春節（補假）"),
            ("2014-02-28", "和平紀念日"),
            ("2014-04-04", "兒童節"),
            ("2014-04-05", "民族掃墓節"),
            ("2014-06-02", "端午節"),
            ("2014-09-08", "中秋節"),
            ("2014-10-10", "國慶日"),
        )

    def test_2015(self):
        self.assertHolidays(
            Taiwan(years=2015),
            ("2015-01-01", "中華民國開國紀念日"),
            ("2015-01-02", "休息日（2014-12-27日起取代）"),
            ("2015-02-18", "農曆除夕"),
            ("2015-02-19", "春節"),
            ("2015-02-20", "春節"),
            ("2015-02-21", "春節"),
            ("2015-02-23", "春節（補假）"),
            ("2015-02-27", "和平紀念日（補假）"),
            ("2015-02-28", "和平紀念日"),
            ("2015-04-03", "兒童節（補假）"),
            ("2015-04-04", "兒童節"),
            ("2015-04-05", "民族掃墓節"),
            ("2015-04-06", "民族掃墓節（補假）"),
            ("2015-06-19", "端午節（補假）"),
            ("2015-06-20", "端午節"),
            ("2015-09-27", "中秋節"),
            ("2015-09-28", "中秋節（補假）"),
            ("2015-10-09", "國慶日（補假）"),
            ("2015-10-10", "國慶日"),
        )

    def test_2016(self):
        self.assertHolidays(
            Taiwan(years=2016),
            ("2016-01-01", "中華民國開國紀念日"),
            ("2016-02-07", "農曆除夕"),
            ("2016-02-08", "春節"),
            ("2016-02-09", "春節"),
            ("2016-02-10", "春節"),
            ("2016-02-11", "農曆除夕（補假）"),
            ("2016-02-12", "休息日（2016-01-30日起取代）"),
            ("2016-02-28", "和平紀念日"),
            ("2016-02-29", "和平紀念日（補假）"),
            ("2016-04-04", "兒童節; 民族掃墓節"),
            ("2016-04-05", "兒童節（補假）"),
            ("2016-06-09", "端午節"),
            ("2016-06-10", "休息日（2016-06-04日起取代）"),
            ("2016-09-15", "中秋節"),
            ("2016-09-16", "休息日（2016-09-10日起取代）"),
            ("2016-10-10", "國慶日"),
        )

    def test_2017(self):
        self.assertHolidays(
            Taiwan(years=2017),
            ("2017-01-01", "中華民國開國紀念日"),
            ("2017-01-02", "中華民國開國紀念日（補假）"),
            ("2017-01-27", "農曆除夕"),
            ("2017-01-28", "春節"),
            ("2017-01-29", "春節"),
            ("2017-01-30", "春節"),
            ("2017-01-31", "春節（補假）"),
            ("2017-02-01", "春節（補假）"),
            ("2017-02-27", "休息日（2017-02-18日起取代）"),
            ("2017-02-28", "和平紀念日"),
            ("2017-04-03", "兒童節（補假）"),
            ("2017-04-04", "兒童節; 民族掃墓節"),
            ("2017-05-29", "休息日（2017-06-03日起取代）"),
            ("2017-05-30", "端午節"),
            ("2017-10-04", "中秋節"),
            ("2017-10-09", "休息日（2017-09-30日起取代）"),
            ("2017-10-10", "國慶日"),
        )

    def test_2018(self):
        self.assertHolidays(
            Taiwan(years=2018),
            ("2018-01-01", "中華民國開國紀念日"),
            ("2018-02-15", "農曆除夕"),
            ("2018-02-16", "春節"),
            ("2018-02-17", "春節"),
            ("2018-02-18", "春節"),
            ("2018-02-19", "春節（補假）"),
            ("2018-02-20", "春節（補假）"),
            ("2018-02-28", "和平紀念日"),
            ("2018-04-04", "兒童節"),
            ("2018-04-05", "民族掃墓節"),
            ("2018-04-06", "休息日（2018-03-31日起取代）"),
            ("2018-06-18", "端午節"),
            ("2018-09-24", "中秋節"),
            ("2018-10-10", "國慶日"),
            ("2018-12-31", "休息日（2018-12-22日起取代）"),
        )

    def test_2019(self):
        self.assertHolidays(
            Taiwan(years=2019),
            ("2019-01-01", "中華民國開國紀念日"),
            ("2019-02-04", "農曆除夕"),
            ("2019-02-05", "春節"),
            ("2019-02-06", "春節"),
            ("2019-02-07", "春節"),
            ("2019-02-08", "休息日（2019-01-19日起取代）"),
            ("2019-02-28", "和平紀念日"),
            ("2019-03-01", "休息日（2019-02-23日起取代）"),
            ("2019-04-04", "兒童節"),
            ("2019-04-05", "民族掃墓節"),
            ("2019-06-07", "端午節"),
            ("2019-09-13", "中秋節"),
            ("2019-10-10", "國慶日"),
            ("2019-10-11", "休息日（2019-10-05日起取代）"),
        )

    def test_2020(self):
        self.assertHolidays(
            Taiwan(years=2020),
            ("2020-01-01", "中華民國開國紀念日"),
            ("2020-01-23", "休息日（2020-02-15日起取代）"),
            ("2020-01-24", "農曆除夕"),
            ("2020-01-25", "春節"),
            ("2020-01-26", "春節"),
            ("2020-01-27", "春節"),
            ("2020-01-28", "春節（補假）"),
            ("2020-01-29", "春節（補假）"),
            ("2020-02-28", "和平紀念日"),
            ("2020-04-02", "民族掃墓節（補假）"),
            ("2020-04-03", "兒童節（補假）"),
            ("2020-04-04", "兒童節; 民族掃墓節"),
            ("2020-06-25", "端午節"),
            ("2020-06-26", "休息日（2020-06-20日起取代）"),
            ("2020-10-01", "中秋節"),
            ("2020-10-02", "休息日（2020-09-26日起取代）"),
            ("2020-10-09", "國慶日（補假）"),
            ("2020-10-10", "國慶日"),
        )

    def test_2021(self):
        self.assertHolidays(
            Taiwan(years=2021),
            ("2021-01-01", "中華民國開國紀念日"),
            ("2021-02-10", "休息日（2021-02-20日起取代）"),
            ("2021-02-11", "農曆除夕"),
            ("2021-02-12", "春節"),
            ("2021-02-13", "春節"),
            ("2021-02-14", "春節"),
            ("2021-02-15", "春節（補假）"),
            ("2021-02-16", "春節（補假）"),
            ("2021-02-28", "和平紀念日"),
            ("2021-03-01", "和平紀念日（補假）"),
            ("2021-04-02", "兒童節（補假）"),
            ("2021-04-04", "兒童節; 民族掃墓節"),
            ("2021-04-05", "民族掃墓節（補假）"),
            ("2021-06-14", "端午節"),
            ("2021-09-20", "休息日（2021-09-11日起取代）"),
            ("2021-09-21", "中秋節"),
            ("2021-10-10", "國慶日"),
            ("2021-10-11", "國慶日（補假）"),
            ("2021-12-31", "中華民國開國紀念日（補假）"),
        )

    def test_2022(self):
        self.assertHolidays(
            Taiwan(years=2022),
            ("2022-01-01", "中華民國開國紀念日"),
            ("2022-01-31", "農曆除夕"),
            ("2022-02-01", "春節"),
            ("2022-02-02", "春節"),
            ("2022-02-03", "春節"),
            ("2022-02-04", "休息日（2022-01-22日起取代）"),
            ("2022-02-28", "和平紀念日"),
            ("2022-04-04", "兒童節"),
            ("2022-04-05", "民族掃墓節"),
            ("2022-06-03", "端午節"),
            ("2022-09-09", "中秋節（補假）"),
            ("2022-09-10", "中秋節"),
            ("2022-10-10", "國慶日"),
        )

    def test_2023(self):
        self.assertHolidays(
            Taiwan(years=2023),
            ("2023-01-01", "中華民國開國紀念日"),
            ("2023-01-02", "中華民國開國紀念日（補假）"),
            ("2023-01-20", "休息日（2023-01-07日起取代）"),
            ("2023-01-21", "農曆除夕"),
            ("2023-01-22", "春節"),
            ("2023-01-23", "春節"),
            ("2023-01-24", "春節"),
            ("2023-01-25", "農曆除夕（補假）"),
            ("2023-01-26", "春節（補假）"),
            ("2023-01-27", "休息日（2023-02-04日起取代）"),
            ("2023-02-27", "休息日（2023-02-18日起取代）"),
            ("2023-02-28", "和平紀念日"),
            ("2023-04-03", "休息日（2023-03-25日起取代）"),
            ("2023-04-04", "兒童節"),
            ("2023-04-05", "民族掃墓節"),
            ("2023-06-22", "端午節"),
            ("2023-06-23", "休息日（2023-06-17日起取代）"),
            ("2023-09-29", "中秋節"),
            ("2023-10-09", "休息日（2023-09-23日起取代）"),
            ("2023-10-10", "國慶日"),
        )

    def test_2024(self):
        self.assertHolidays(
            Taiwan(years=2024),
            ("2024-01-01", "中華民國開國紀念日"),
            ("2024-02-08", "休息日（2024-02-17日起取代）"),
            ("2024-02-09", "農曆除夕"),
            ("2024-02-10", "春節"),
            ("2024-02-11", "春節"),
            ("2024-02-12", "春節"),
            ("2024-02-13", "春節（補假）"),
            ("2024-02-14", "春節（補假）"),
            ("2024-02-28", "和平紀念日"),
            ("2024-04-04", "兒童節; 民族掃墓節"),
            ("2024-04-05", "兒童節（補假）"),
            ("2024-06-10", "端午節"),
            ("2024-09-17", "中秋節"),
            ("2024-10-10", "國慶日"),
        )

    def test_2025(self):
        self.assertHolidays(
            Taiwan(years=2025),
            ("2025-01-01", "中華民國開國紀念日"),
            ("2025-01-27", "休息日（2025-02-08日起取代）"),
            ("2025-01-28", "農曆除夕"),
            ("2025-01-29", "春節"),
            ("2025-01-30", "春節"),
            ("2025-01-31", "春節"),
            ("2025-02-28", "和平紀念日"),
            ("2025-04-03", "兒童節（補假）"),
            ("2025-04-04", "兒童節; 民族掃墓節"),
            ("2025-05-30", "端午節（補假）"),
            ("2025-05-31", "端午節"),
            ("2025-09-28", "孔子誕辰紀念日"),
            ("2025-10-06", "中秋節"),
            ("2025-10-10", "國慶日"),
            ("2025-10-25", "臺灣光復暨金門古寧頭大捷紀念日"),
            ("2025-12-25", "行憲紀念日"),
        )

    def test_weekend(self):
        for dt in (
            "1998-02-01",  # SUN.
            "1998-02-08",  # SUN.
            "1998-02-14",  # 2nd SAT.
            "1998-02-15",  # SUN.
            "1998-02-22",  # SUN.
            "1998-02-28",  # 4th SAT.
            "1998-10-04",  # SUN.
            "1998-10-10",  # 2nd SAT.
            "1998-10-11",  # SUN.
            "1998-10-18",  # SUN.
            "1998-10-24",  # 4th SAT.
            "1998-10-25",  # SUN.
            "2001-02-03",  # SAT.
            "2001-02-04",  # SUN.
            "2001-02-10",  # SAT.
            "2001-02-11",  # SUN.
            "2001-02-17",  # SAT.
            "2001-02-18",  # SUN.
            "2001-02-24",  # SAT.
            "2001-02-25",  # SUN.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "1998-02-07",  # 1st SAT.
            "1998-02-21",  # 3rd SAT.
            "1998-10-03",  # 1st SAT.
            "1998-10-17",  # 3rd SAT.
            "1998-10-31",  # 5th SAT.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "中華民國開國紀念日"),
            ("2022-01-31", "農曆除夕"),
            ("2022-02-01", "春節; 道教節"),
            ("2022-02-02", "春節"),
            ("2022-02-03", "春節"),
            ("2022-02-04", "休息日（2022-01-22日起取代）"),
            ("2022-02-28", "和平紀念日"),
            ("2022-03-08", "婦女節"),
            ("2022-03-12", "國父逝世紀念日; 植樹節"),
            ("2022-03-14", "反侵略日"),
            ("2022-03-29", "青年節; 革命先烈紀念日"),
            ("2022-04-04", "兒童節"),
            ("2022-04-05", "民族掃墓節"),
            ("2022-05-01", "勞動節"),
            ("2022-05-08", "佛陀誕辰紀念日"),
            ("2022-06-03", "端午節"),
            ("2022-07-15", "解嚴紀念日"),
            ("2022-09-03", "軍人節"),
            ("2022-09-09", "中秋節（補假）"),
            ("2022-09-10", "中秋節"),
            ("2022-09-28", "孔子誕辰紀念日; 教師節"),
            ("2022-10-10", "國慶日"),
            ("2022-10-24", "臺灣聯合國日"),
            ("2022-10-25", "臺灣光復節"),
            ("2022-11-12", "中華文化復興節; 國父誕辰紀念日"),
            ("2022-12-25", "行憲紀念日"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Founding Day of the Republic of China"),
            ("2022-01-31", "Chinese New Year's Eve"),
            ("2022-02-01", "Chinese New Year; Taoism Day"),
            ("2022-02-02", "Chinese New Year"),
            ("2022-02-03", "Chinese New Year"),
            ("2022-02-04", "Day off (substituted from 01/22/2022)"),
            ("2022-02-28", "Peace Memorial Day"),
            ("2022-03-08", "Women's Day"),
            ("2022-03-12", "Arbor Day; Dr. Sun Yat-sen's Memorial Day"),
            ("2022-03-14", "Anti-Aggression Day"),
            ("2022-03-29", "Revolutionary Martyrs Memorial Day; Youth Day"),
            ("2022-04-04", "Children's Day"),
            ("2022-04-05", "Tomb-Sweeping Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "The Buddha's Birthday"),
            ("2022-06-03", "Dragon Boat Festival"),
            ("2022-07-15", "Commemoration Day of the Lifting of Martial Law"),
            ("2022-09-03", "Armed Forces Day"),
            ("2022-09-09", "Mid-Autumn Festival (observed)"),
            ("2022-09-10", "Mid-Autumn Festival"),
            ("2022-09-28", "Confucius' Birthday; Teacher's Day"),
            ("2022-10-10", "National Day"),
            ("2022-10-24", "Taiwan United Nations Day"),
            ("2022-10-25", "Taiwan Retrocession Day"),
            ("2022-11-12", "Chinese Cultural Renaissance Day; Dr. Sun Yat-sen's Birthday"),
            ("2022-12-25", "Constitution Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันสถาปนาสาธารณรัฐจีน(ไต้หวัน)"),
            ("2022-01-31", "วันก่อนวันตรุษจีน"),
            ("2022-02-01", "วันตรุษจีน; วันเต๋า"),
            ("2022-02-02", "วันตรุษจีน"),
            ("2022-02-03", "วันตรุษจีน"),
            ("2022-02-04", "วันหยุด (แทน 22/01/2022)"),
            ("2022-02-28", "วันรำลึกสันติภาพ"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-03-12", "วันปลูกต้นไม้; วันรำลึกถึงการอสัญกรรม ดร.ซุนยัตเซ็น"),
            ("2022-03-14", "วันต่อต้านการรุกราน"),
            ("2022-03-29", "วันสดุดีวีรชนแห่งการปฏิวัติ; วันเยาวชน"),
            ("2022-04-04", "วันเด็กแห่งชาติ"),
            ("2022-04-05", "วันเช็งเม้ง"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-08", "วันวิสาขบูชา"),
            ("2022-06-03", "วันไหว้บ๊ะจ่าง"),
            ("2022-07-15", "วันรำลึกการยกเลิกกฎอัยการศึก"),
            ("2022-09-03", "วันกองทัพ"),
            ("2022-09-09", "ชดเชยวันไหว้พระจันทร์"),
            ("2022-09-10", "วันไหว้พระจันทร์"),
            ("2022-09-28", "วันขงจื๊อ; วันครู"),
            ("2022-10-10", "วันชาติสาธารณรัฐจีน(ไต้หวัน)"),
            ("2022-10-24", "วันรำลึกถึงบทบาทสาธารณรัฐจีน(ไต้หวัน)ในสหประชาชาติ"),
            ("2022-10-25", "วันฉลองกลับคืนสู่มาตุภูมิของไต้หวัน"),
            ("2022-11-12", "วันคล้ายวันเกิด ดร.ซุนยัตเซ็น; วันเฉลิมฉลองวัฒนธรรมจีน"),
            ("2022-12-25", "วันรัฐธรรมนูญ"),
        )

    def test_l10n_zh_cn(self):
        self.assertLocalizedHolidays(
            "zh_CN",
            ("2022-01-01", "中华民国开国纪念日"),
            ("2022-01-31", "农历除夕"),
            ("2022-02-01", "春节; 道教节"),
            ("2022-02-02", "春节"),
            ("2022-02-03", "春节"),
            ("2022-02-04", "休息日（2022-01-22日起取代）"),
            ("2022-02-28", "和平纪念日"),
            ("2022-03-08", "妇女节"),
            ("2022-03-12", "国父逝世纪念日; 植树节"),
            ("2022-03-14", "反侵略日"),
            ("2022-03-29", "青年节; 革命先烈纪念日"),
            ("2022-04-04", "儿童节"),
            ("2022-04-05", "民族扫墓节"),
            ("2022-05-01", "劳动节"),
            ("2022-05-08", "佛陀诞辰纪念日"),
            ("2022-06-03", "端午节"),
            ("2022-07-15", "解严纪念日"),
            ("2022-09-03", "军人节"),
            ("2022-09-09", "中秋节（观察日）"),
            ("2022-09-10", "中秋节"),
            ("2022-09-28", "孔子诞辰纪念日; 教师节"),
            ("2022-10-10", "国庆日"),
            ("2022-10-24", "台湾联合国日"),
            ("2022-10-25", "台湾光复节"),
            ("2022-11-12", "中华文化复兴节; 国父诞辰纪念日"),
            ("2022-12-25", "行宪纪念日"),
        )
