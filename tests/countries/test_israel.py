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

from holidays.constants import OPTIONAL, SCHOOL
from holidays.countries.israel import Israel, IL, ISR
from tests.common import TestCase


class TestIsrael(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Israel, years=range(1948, 2050))
        cls.opt_holidays = Israel(categories=(OPTIONAL,), years=range(2000, 2024))
        cls.opt_holidays_non_observed = Israel(
            observed=False, categories=(OPTIONAL,), years=range(2000, 2024)
        )

    def test_country_aliases(self):
        self.assertCountryAliases(Israel, IL, ISR)

    def test_not_implemented(self):
        self.assertRaises(NotImplementedError, lambda: Israel(years=2101))
        self.assertRaises(NotImplementedError, lambda: Israel(categories=(OPTIONAL,), years=2101))
        self.assertRaises(NotImplementedError, lambda: Israel(categories=(SCHOOL,), years=2101))

    def test_no_holidays(self):
        self.assertNoHolidays(Israel(years=1947))
        self.assertNoHolidays(Israel(categories=(OPTIONAL,), years=1947))
        self.assertNoHolidays(Israel(categories=(SCHOOL,), years=1947))

    def test_independence_day(self):
        name = "Independence Day"
        name_observed = f"{name} (Observed)"
        common_dt = (
            "2000-05-10",
            "2002-04-17",
            "2003-05-07",
            "2006-05-03",
            "2009-04-29",
            "2020-04-29",
            "2023-04-26",
        )
        obs_dt = (
            "2001-04-26",
            "2004-04-27",
            "2005-05-12",
            "2007-04-24",
            "2008-05-08",
            "2010-04-20",
            "2011-05-10",
            "2012-04-26",
            "2013-04-16",
            "2014-05-06",
            "2015-04-23",
            "2016-05-12",
            "2017-05-02",
            "2018-04-19",
            "2019-05-09",
            "2021-04-15",
            "2022-05-05",
        )
        non_obs_dt = (
            "2001-04-28",
            "2004-04-26",
            "2005-05-14",
            "2007-04-23",
            "2008-05-10",
            "2010-04-19",
            "2011-05-09",
            "2012-04-27",
            "2013-04-15",
            "2014-05-05",
            "2015-04-24",
            "2016-05-13",
            "2017-05-01",
            "2018-04-20",
            "2019-05-10",
            "2021-04-17",
            "2022-05-06",
        )
        self.assertHolidayName(name, common_dt)
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNonObservedHolidayName(name, common_dt, non_obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_memorial_day(self):
        name = "Memorial Day"
        name_observed = f"{name} (Observed)"
        common_dt = (
            "2000-05-09",
            "2002-04-16",
            "2003-05-06",
            "2006-05-02",
            "2009-04-28",
            "2020-04-28",
            "2023-04-25",
        )
        obs_dt = (
            "2001-04-25",
            "2004-04-26",
            "2005-05-11",
            "2007-04-23",
            "2008-05-07",
            "2010-04-19",
            "2011-05-09",
            "2012-04-25",
            "2013-04-15",
            "2014-05-05",
            "2015-04-22",
            "2016-05-11",
            "2017-05-01",
            "2018-04-18",
            "2019-05-08",
            "2021-04-14",
            "2022-05-04",
        )
        non_obs_dt = (
            "2001-04-27",
            "2004-04-25",
            "2005-05-13",
            "2007-04-22",
            "2008-05-09",
            "2010-04-18",
            "2011-05-08",
            "2012-04-26",
            "2013-04-14",
            "2014-05-04",
            "2015-04-23",
            "2016-05-12",
            "2017-04-30",
            "2018-04-19",
            "2019-05-09",
            "2021-04-16",
            "2022-05-05",
        )
        self.assertHolidayName(name, self.opt_holidays, common_dt)
        self.assertHolidayName(name_observed, self.opt_holidays, obs_dt)
        self.assertNonObservedHolidayName(
            name, self.opt_holidays_non_observed, common_dt, non_obs_dt
        )
        self.assertNoNonObservedHoliday(self.opt_holidays_non_observed, obs_dt)
        self.assertNoHolidayName(name, Israel(categories=(OPTIONAL,), years=range(1948, 1963)))
        self.assertNoHolidayName(name)

    def test_sigd(self):
        name = "Sigd"
        dt = (
            "2008-11-27",
            "2009-11-16",
            "2010-11-06",
            "2011-11-26",
            "2012-11-14",
            "2013-11-02",
            "2014-11-22",
            "2015-11-11",
            "2016-11-30",
            "2017-11-18",
            "2018-11-07",
            "2019-11-27",
            "2020-11-16",
            "2021-11-04",
            "2022-11-23",
            "2023-11-13",
        )
        self.assertHolidayName(name, self.opt_holidays, dt)
        self.assertNoHolidayName(name, self.opt_holidays, range(2000, 2008))
        self.assertNoHolidayName(name)

    def test_tisha_bav(self):
        name = "Tisha B'Av"
        name_observed = f"{name} (Observed)"
        common_dt = (
            "2000-08-10",
            "2001-07-29",
            "2002-07-18",
            "2003-08-07",
            "2004-07-27",
            "2005-08-14",
            "2006-08-03",
            "2007-07-24",
            "2008-08-10",
            "2009-07-30",
            "2010-07-20",
            "2011-08-09",
            "2013-07-16",
            "2014-08-05",
            "2017-08-01",
            "2020-07-30",
            "2021-07-18",
            "2023-07-27",
        )
        obs_dt = (
            "2012-07-29",
            "2015-07-26",
            "2016-08-14",
            "2018-07-22",
            "2019-08-11",
            "2022-08-07",
        )
        non_obs_dt = (
            "2012-07-28",
            "2015-07-25",
            "2016-08-13",
            "2018-07-21",
            "2019-08-10",
            "2022-08-06",
        )
        self.assertHolidayName(name, self.opt_holidays, common_dt)
        self.assertHolidayName(name_observed, self.opt_holidays, obs_dt)
        self.assertNonObservedHolidayName(
            name, self.opt_holidays_non_observed, common_dt, non_obs_dt
        )
        self.assertNoNonObservedHoliday(self.opt_holidays_non_observed, obs_dt)
        self.assertNoHolidayName(name)

    def test_taanit_ester(self):
        name = "Fast of Esther"
        name_observed = f"{name} (Observed)"
        common_dt = (
            "2000-03-20",
            "2001-03-08",
            "2002-02-25",
            "2003-03-17",
            "2005-03-24",
            "2006-03-13",
            "2008-03-20",
            "2009-03-09",
            "2012-03-07",
            "2015-03-04",
            "2016-03-23",
            "2018-02-28",
            "2019-03-20",
            "2020-03-09",
            "2021-02-25",
            "2022-03-16",
            "2023-03-06",
        )
        obs_dt = (
            "2004-03-04",
            "2007-03-01",
            "2010-02-25",
            "2011-03-17",
            "2013-02-21",
            "2014-03-13",
            "2017-03-09",
        )
        non_obs_dt = (
            "2004-03-06",
            "2007-03-03",
            "2010-02-27",
            "2011-03-19",
            "2013-02-23",
            "2014-03-15",
            "2017-03-11",
        )
        school_holidays = Israel(categories=(SCHOOL,), years=range(2000, 2024))
        school_holidays_non_observed = Israel(
            observed=False, categories=(SCHOOL,), years=range(2000, 2024)
        )
        self.assertHolidayName(name, school_holidays, common_dt)
        self.assertHolidayName(name_observed, school_holidays, obs_dt)
        self.assertNonObservedHolidayName(
            name, school_holidays_non_observed, common_dt, non_obs_dt
        )
        self.assertNoNonObservedHoliday(school_holidays_non_observed, obs_dt)
        self.assertNoHolidayName(name)

    def test_2021(self):
        self.assertHolidays(
            Israel(years=2021),
            ("2021-03-28", "Passover"),
            ("2021-04-03", "Seventh day of Passover"),
            ("2021-04-15", "Independence Day (Observed)"),
            ("2021-05-17", "Shavuot"),
            ("2021-09-07", "Rosh Hashanah"),
            ("2021-09-08", "Rosh Hashanah"),
            ("2021-09-16", "Yom Kippur"),
            ("2021-09-21", "Sukkot"),
            ("2021-09-28", "Simchat Torah / Shemini Atzeret"),
        )

    def test_2022(self):
        self.assertHolidays(
            Israel(years=2022),
            ("2022-04-16", "Passover"),
            ("2022-04-22", "Seventh day of Passover"),
            ("2022-05-05", "Independence Day (Observed)"),
            ("2022-06-05", "Shavuot"),
            ("2022-09-26", "Rosh Hashanah"),
            ("2022-09-27", "Rosh Hashanah"),
            ("2022-10-05", "Yom Kippur"),
            ("2022-10-10", "Sukkot"),
            ("2022-10-17", "Simchat Torah / Shemini Atzeret"),
        )

    def test_2023(self):
        self.assertHolidays(
            Israel(years=2023),
            ("2023-04-06", "Passover"),
            ("2023-04-12", "Seventh day of Passover"),
            ("2023-04-26", "Independence Day"),
            ("2023-05-26", "Shavuot"),
            ("2023-09-16", "Rosh Hashanah"),
            ("2023-09-17", "Rosh Hashanah"),
            ("2023-09-25", "Yom Kippur"),
            ("2023-09-30", "Sukkot"),
            ("2023-10-07", "Simchat Torah / Shemini Atzeret"),
        )

    def test_2021_optional(self):
        self.assertHolidays(
            Israel(categories=(OPTIONAL,), years=2021),
            ("2021-02-26", "Purim"),
            ("2021-03-29", "Passover"),
            ("2021-03-30", "Passover"),
            ("2021-03-31", "Passover"),
            ("2021-04-01", "Passover"),
            ("2021-04-02", "Passover"),
            ("2021-04-14", "Memorial Day (Observed)"),
            ("2021-05-10", "Jerusalem Day"),
            ("2021-07-18", "Tisha B'Av"),
            ("2021-09-22", "Sukkot"),
            ("2021-09-23", "Sukkot"),
            ("2021-09-24", "Sukkot"),
            ("2021-09-25", "Sukkot"),
            ("2021-09-26", "Sukkot"),
            ("2021-11-04", "Sigd"),
        )

    def test_2022_optional(self):
        self.assertHolidays(
            Israel(categories=(OPTIONAL,), years=2022),
            ("2022-03-17", "Purim"),
            ("2022-04-17", "Passover"),
            ("2022-04-18", "Passover"),
            ("2022-04-19", "Passover"),
            ("2022-04-20", "Passover"),
            ("2022-04-21", "Passover"),
            ("2022-05-04", "Memorial Day (Observed)"),
            ("2022-05-29", "Jerusalem Day"),
            ("2022-08-07", "Tisha B'Av (Observed)"),
            ("2022-10-11", "Sukkot"),
            ("2022-10-12", "Sukkot"),
            ("2022-10-13", "Sukkot"),
            ("2022-10-14", "Sukkot"),
            ("2022-10-15", "Sukkot"),
            ("2022-11-23", "Sigd"),
        )

    def test_2023_optional(self):
        self.assertHolidays(
            Israel(categories=(OPTIONAL,), years=2023),
            ("2023-03-07", "Purim"),
            ("2023-04-07", "Passover"),
            ("2023-04-08", "Passover"),
            ("2023-04-09", "Passover"),
            ("2023-04-10", "Passover"),
            ("2023-04-11", "Passover"),
            ("2023-04-25", "Memorial Day"),
            ("2023-05-19", "Jerusalem Day"),
            ("2023-07-27", "Tisha B'Av"),
            ("2023-10-01", "Sukkot"),
            ("2023-10-02", "Sukkot"),
            ("2023-10-03", "Sukkot"),
            ("2023-10-04", "Sukkot"),
            ("2023-10-05", "Sukkot"),
            ("2023-11-13", "Sigd"),
        )

    def test_2021_school(self):
        self.assertHolidays(
            Israel(categories=(SCHOOL,), years=2021),
            ("2021-02-25", "Fast of Esther"),
            ("2021-02-26", "Purim"),
            ("2021-03-29", "Passover"),
            ("2021-03-30", "Passover"),
            ("2021-03-31", "Passover"),
            ("2021-04-01", "Passover"),
            ("2021-04-02", "Passover"),
            ("2021-04-30", "Lag BaOmer"),
            ("2021-09-22", "Sukkot"),
            ("2021-09-23", "Sukkot"),
            ("2021-09-24", "Sukkot"),
            ("2021-09-25", "Sukkot"),
            ("2021-09-26", "Sukkot"),
            ("2021-11-29", "Hanukkah"),
            ("2021-11-30", "Hanukkah"),
            ("2021-12-01", "Hanukkah"),
            ("2021-12-02", "Hanukkah"),
            ("2021-12-03", "Hanukkah"),
            ("2021-12-04", "Hanukkah"),
            ("2021-12-05", "Hanukkah"),
            ("2021-12-06", "Hanukkah"),
        )

    def test_2022_school(self):
        self.assertHolidays(
            Israel(categories=(SCHOOL,), years=2022),
            ("2022-03-16", "Fast of Esther"),
            ("2022-03-17", "Purim"),
            ("2022-04-17", "Passover"),
            ("2022-04-18", "Passover"),
            ("2022-04-19", "Passover"),
            ("2022-04-20", "Passover"),
            ("2022-04-21", "Passover"),
            ("2022-05-19", "Lag BaOmer"),
            ("2022-10-11", "Sukkot"),
            ("2022-10-12", "Sukkot"),
            ("2022-10-13", "Sukkot"),
            ("2022-10-14", "Sukkot"),
            ("2022-10-15", "Sukkot"),
            ("2022-12-19", "Hanukkah"),
            ("2022-12-20", "Hanukkah"),
            ("2022-12-21", "Hanukkah"),
            ("2022-12-22", "Hanukkah"),
            ("2022-12-23", "Hanukkah"),
            ("2022-12-24", "Hanukkah"),
            ("2022-12-25", "Hanukkah"),
            ("2022-12-26", "Hanukkah"),
        )

    def test_2023_school(self):
        self.assertHolidays(
            Israel(categories=(SCHOOL,), years=2023),
            ("2023-03-06", "Fast of Esther"),
            ("2023-03-07", "Purim"),
            ("2023-04-07", "Passover"),
            ("2023-04-08", "Passover"),
            ("2023-04-09", "Passover"),
            ("2023-04-10", "Passover"),
            ("2023-04-11", "Passover"),
            ("2023-05-09", "Lag BaOmer"),
            ("2023-10-01", "Sukkot"),
            ("2023-10-02", "Sukkot"),
            ("2023-10-03", "Sukkot"),
            ("2023-10-04", "Sukkot"),
            ("2023-10-05", "Sukkot"),
            ("2023-12-08", "Hanukkah"),
            ("2023-12-09", "Hanukkah"),
            ("2023-12-10", "Hanukkah"),
            ("2023-12-11", "Hanukkah"),
            ("2023-12-12", "Hanukkah"),
            ("2023-12-13", "Hanukkah"),
            ("2023-12-14", "Hanukkah"),
            ("2023-12-15", "Hanukkah"),
        )
