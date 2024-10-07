#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import OPTIONAL, SCHOOL
from holidays.countries.israel import Israel, IL, ISR
from tests.common import CommonCountryTests


class TestIsrael(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Israel, years=range(1948, 2050))
        cls.opt_holidays = Israel(categories=(OPTIONAL,), years=range(2000, 2024))
        cls.opt_holidays_non_observed = Israel(
            observed=False, categories=(OPTIONAL,), years=range(2000, 2024)
        )

    def test_country_aliases(self):
        self.assertAliases(Israel, IL, ISR)

    def test_not_implemented(self):
        self.assertRaises(NotImplementedError, lambda: Israel(years=2101))
        self.assertRaises(NotImplementedError, lambda: Israel(categories=(OPTIONAL,), years=2101))
        self.assertRaises(NotImplementedError, lambda: Israel(categories=(SCHOOL,), years=2101))

    def test_no_holidays(self):
        self.assertNoHolidays(Israel(years=1947))
        self.assertNoHolidays(Israel(categories=(OPTIONAL,), years=1947))
        self.assertNoHolidays(Israel(categories=(SCHOOL,), years=1947))

    def test_independence_day(self):
        name = "יום העצמאות"
        name_observed = f"(נצפה) {name}"
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
        name = "יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"
        name_observed = f"(נצפה) {name}"
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

    def test_optional_holidays(self):
        name = "סיגד"
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
        name = "תשעה באב"
        name_observed = f"(נצפה) {name}"
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
        name = "תענית אסתר"
        name_observed = f"(נצפה) {name}"
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
            ("2021-03-28", "פסח"),
            ("2021-04-03", "שביעי של פסח"),
            ("2021-04-15", "(נצפה) יום העצמאות"),
            ("2021-05-17", "שבועות"),
            ("2021-09-07", "ראש השנה"),
            ("2021-09-08", "ראש השנה"),
            ("2021-09-16", "יום כיפור"),
            ("2021-09-21", "סוכות"),
            ("2021-09-28", "שמחת תורה/שמיני עצרת"),
        )

    def test_2022(self):
        self.assertHolidays(
            Israel(years=2022),
            ("2022-04-16", "פסח"),
            ("2022-04-22", "שביעי של פסח"),
            ("2022-05-05", "(נצפה) יום העצמאות"),
            ("2022-06-05", "שבועות"),
            ("2022-09-26", "ראש השנה"),
            ("2022-09-27", "ראש השנה"),
            ("2022-10-05", "יום כיפור"),
            ("2022-10-10", "סוכות"),
            ("2022-10-17", "שמחת תורה/שמיני עצרת"),
        )

    def test_2023(self):
        self.assertHolidays(
            Israel(years=2023),
            ("2023-04-06", "פסח"),
            ("2023-04-12", "שביעי של פסח"),
            ("2023-04-26", "יום העצמאות"),
            ("2023-05-26", "שבועות"),
            ("2023-09-16", "ראש השנה"),
            ("2023-09-17", "ראש השנה"),
            ("2023-09-25", "יום כיפור"),
            ("2023-09-30", "סוכות"),
            ("2023-10-07", "שמחת תורה/שמיני עצרת"),
        )

    def test_2021_optional(self):
        self.assertHolidays(
            Israel(categories=(OPTIONAL,), years=2021),
            ("2021-02-26", "פורים"),
            ("2021-03-29", "חול המועד פסח"),
            ("2021-03-30", "חול המועד פסח"),
            ("2021-03-31", "חול המועד פסח"),
            ("2021-04-01", "חול המועד פסח"),
            ("2021-04-02", "חול המועד פסח"),
            ("2021-04-14", "(נצפה) יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"),
            ("2021-05-10", "יום ירושלים"),
            ("2021-07-18", "תשעה באב"),
            ("2021-09-22", "חול המועד סוכות"),
            ("2021-09-23", "חול המועד סוכות"),
            ("2021-09-24", "חול המועד סוכות"),
            ("2021-09-25", "חול המועד סוכות"),
            ("2021-09-26", "חול המועד סוכות"),
            ("2021-11-04", "סיגד"),
        )

    def test_2022_optional(self):
        self.assertHolidays(
            Israel(categories=(OPTIONAL,), years=2022),
            ("2022-03-17", "פורים"),
            ("2022-04-17", "חול המועד פסח"),
            ("2022-04-18", "חול המועד פסח"),
            ("2022-04-19", "חול המועד פסח"),
            ("2022-04-20", "חול המועד פסח"),
            ("2022-04-21", "חול המועד פסח"),
            ("2022-05-04", "(נצפה) יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"),
            ("2022-05-29", "יום ירושלים"),
            ("2022-08-07", "(נצפה) תשעה באב"),
            ("2022-10-11", "חול המועד סוכות"),
            ("2022-10-12", "חול המועד סוכות"),
            ("2022-10-13", "חול המועד סוכות"),
            ("2022-10-14", "חול המועד סוכות"),
            ("2022-10-15", "חול המועד סוכות"),
            ("2022-11-23", "סיגד"),
        )

    def test_2023_optional(self):
        self.assertHolidays(
            Israel(categories=(OPTIONAL,), years=2023),
            ("2023-03-07", "פורים"),
            ("2023-04-07", "חול המועד פסח"),
            ("2023-04-08", "חול המועד פסח"),
            ("2023-04-09", "חול המועד פסח"),
            ("2023-04-10", "חול המועד פסח"),
            ("2023-04-11", "חול המועד פסח"),
            ("2023-04-25", "יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"),
            ("2023-05-19", "יום ירושלים"),
            ("2023-07-27", "תשעה באב"),
            ("2023-10-01", "חול המועד סוכות"),
            ("2023-10-02", "חול המועד סוכות"),
            ("2023-10-03", "חול המועד סוכות"),
            ("2023-10-04", "חול המועד סוכות"),
            ("2023-10-05", "חול המועד סוכות"),
            ("2023-11-13", "סיגד"),
        )

    def test_2021_school(self):
        self.assertHolidays(
            Israel(categories=(SCHOOL,), years=2021),
            ("2021-02-25", "תענית אסתר"),
            ("2021-02-26", "פורים"),
            ("2021-03-29", "חול המועד פסח"),
            ("2021-03-30", "חול המועד פסח"),
            ("2021-03-31", "חול המועד פסח"),
            ("2021-04-01", "חול המועד פסח"),
            ("2021-04-02", "חול המועד פסח"),
            ("2021-04-30", 'ל"ג בעומר'),
            ("2021-09-22", "חול המועד סוכות"),
            ("2021-09-23", "חול המועד סוכות"),
            ("2021-09-24", "חול המועד סוכות"),
            ("2021-09-25", "חול המועד סוכות"),
            ("2021-09-26", "חול המועד סוכות"),
            ("2021-11-29", "חנוכה"),
            ("2021-11-30", "חנוכה"),
            ("2021-12-01", "חנוכה"),
            ("2021-12-02", "חנוכה"),
            ("2021-12-03", "חנוכה"),
            ("2021-12-04", "חנוכה"),
            ("2021-12-05", "חנוכה"),
            ("2021-12-06", "חנוכה"),
        )

    def test_2022_school(self):
        self.assertHolidays(
            Israel(categories=(SCHOOL,), years=2022),
            ("2022-03-16", "תענית אסתר"),
            ("2022-03-17", "פורים"),
            ("2022-04-17", "חול המועד פסח"),
            ("2022-04-18", "חול המועד פסח"),
            ("2022-04-19", "חול המועד פסח"),
            ("2022-04-20", "חול המועד פסח"),
            ("2022-04-21", "חול המועד פסח"),
            ("2022-05-19", 'ל"ג בעומר'),
            ("2022-10-11", "חול המועד סוכות"),
            ("2022-10-12", "חול המועד סוכות"),
            ("2022-10-13", "חול המועד סוכות"),
            ("2022-10-14", "חול המועד סוכות"),
            ("2022-10-15", "חול המועד סוכות"),
            ("2022-12-19", "חנוכה"),
            ("2022-12-20", "חנוכה"),
            ("2022-12-21", "חנוכה"),
            ("2022-12-22", "חנוכה"),
            ("2022-12-23", "חנוכה"),
            ("2022-12-24", "חנוכה"),
            ("2022-12-25", "חנוכה"),
            ("2022-12-26", "חנוכה"),
        )

    def test_2023_school(self):
        self.assertHolidays(
            Israel(categories=(SCHOOL,), years=2023),
            ("2023-03-06", "תענית אסתר"),
            ("2023-03-07", "פורים"),
            ("2023-04-07", "חול המועד פסח"),
            ("2023-04-08", "חול המועד פסח"),
            ("2023-04-09", "חול המועד פסח"),
            ("2023-04-10", "חול המועד פסח"),
            ("2023-04-11", "חול המועד פסח"),
            ("2023-05-09", 'ל"ג בעומר'),
            ("2023-10-01", "חול המועד סוכות"),
            ("2023-10-02", "חול המועד סוכות"),
            ("2023-10-03", "חול המועד סוכות"),
            ("2023-10-04", "חול המועד סוכות"),
            ("2023-10-05", "חול המועד סוכות"),
            ("2023-12-08", "חנוכה"),
            ("2023-12-09", "חנוכה"),
            ("2023-12-10", "חנוכה"),
            ("2023-12-11", "חנוכה"),
            ("2023-12-12", "חנוכה"),
            ("2023-12-13", "חנוכה"),
            ("2023-12-14", "חנוכה"),
            ("2023-12-15", "חנוכה"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2021-02-25", "Ta'anit Ester"),
            ("2021-02-26", "Purim"),
            ("2021-03-28", "Pesach"),
            ("2021-03-29", "Pesach holiday"),
            ("2021-03-30", "Pesach holiday"),
            ("2021-03-31", "Pesach holiday"),
            ("2021-04-01", "Pesach holiday"),
            ("2021-04-02", "Pesach holiday"),
            ("2021-04-03", "Seventh day of Pesach"),
            ("2021-04-14", "Remembrance Day (observed)"),
            ("2021-04-15", "Independence Day (observed)"),
            ("2021-04-30", "Lag BaOmer"),
            ("2021-05-10", "Jerusalem Day"),
            ("2021-05-17", "Shavuot"),
            ("2021-07-18", "Tisha B'Av"),
            ("2021-09-07", "Rosh Hashanah"),
            ("2021-09-08", "Rosh Hashanah"),
            ("2021-09-16", "Yom Kippur"),
            ("2021-09-21", "Sukkot"),
            ("2021-09-22", "Sukkot holiday"),
            ("2021-09-23", "Sukkot holiday"),
            ("2021-09-24", "Sukkot holiday"),
            ("2021-09-25", "Sukkot holiday"),
            ("2021-09-26", "Sukkot holiday"),
            ("2021-09-28", "Simchat Torah / Shemini Atzeret"),
            ("2021-11-04", "Sigd"),
            ("2021-11-29", "Hanukkah"),
            ("2021-11-30", "Hanukkah"),
            ("2021-12-01", "Hanukkah"),
            ("2021-12-02", "Hanukkah"),
            ("2021-12-03", "Hanukkah"),
            ("2021-12-04", "Hanukkah"),
            ("2021-12-05", "Hanukkah"),
            ("2021-12-06", "Hanukkah"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2021-02-25", "Тааніт-Естер"),
            ("2021-02-26", "Пурім"),
            ("2021-03-28", "Песах"),
            ("2021-03-29", "Свято Песах"),
            ("2021-03-30", "Свято Песах"),
            ("2021-03-31", "Свято Песах"),
            ("2021-04-01", "Свято Песах"),
            ("2021-04-02", "Свято Песах"),
            ("2021-04-03", "Сьомий день Песаха"),
            ("2021-04-14", "День памʼяті (вихідний)"),
            ("2021-04-15", "День незалежності (вихідний)"),
            ("2021-04-30", "Лаг ба-Омер"),
            ("2021-05-10", "День Єрусалиму"),
            ("2021-05-17", "Шавуот"),
            ("2021-07-18", "Тиша Бе-Ав"),
            ("2021-09-07", "Рош га-Шана"),
            ("2021-09-08", "Рош га-Шана"),
            ("2021-09-16", "Йом Кіпур"),
            ("2021-09-21", "Суккот"),
            ("2021-09-22", "Свято Суккот"),
            ("2021-09-23", "Свято Суккот"),
            ("2021-09-24", "Свято Суккот"),
            ("2021-09-25", "Свято Суккот"),
            ("2021-09-26", "Свято Суккот"),
            ("2021-09-28", "Сімхат Тора / Шміні Ацерет"),
            ("2021-11-04", "Сігд"),
            ("2021-11-29", "Ханука"),
            ("2021-11-30", "Ханука"),
            ("2021-12-01", "Ханука"),
            ("2021-12-02", "Ханука"),
            ("2021-12-03", "Ханука"),
            ("2021-12-04", "Ханука"),
            ("2021-12-05", "Ханука"),
            ("2021-12-06", "Ханука"),
        )
