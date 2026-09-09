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

from holidays.countries.kyrgyzstan import Kyrgyzstan
from tests.common import CommonCountryTests, WorkingDayTests


class TestKyrgyzstan(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Kyrgyzstan)

    def test_special_holidays(self):
        self.assertHoliday(
            "2025-01-03",
            "2025-01-06",
        )

    def test_substituted_holidays(self):
        self.assertHoliday(
            "2006-01-09",
            "2007-01-03",
            "2007-01-04",
            "2008-01-02",
            "2008-01-03",
            "2008-01-04",
            "2009-01-02",
            "2009-01-05",
            "2009-01-06",
            "2009-03-23",
            "2009-05-04",
            "2009-12-31",
            "2010-01-04",
            "2010-01-05",
            "2010-01-06",
            "2010-01-08",
            "2010-02-22",
            "2010-08-30",
            "2010-11-15",
            "2011-03-07",
            "2011-05-06",
            "2012-01-03",
            "2012-01-04",
            "2012-01-05",
            "2012-01-06",
            "2013-01-02",
            "2013-01-03",
            "2013-01-04",
            "2013-05-10",
            "2013-08-09",
            "2013-10-14",
            "2013-11-08",
            "2014-01-02",
            "2014-01-03",
            "2014-01-06",
            "2014-07-28",
            "2014-09-05",
            "2015-01-02",
            "2015-01-05",
            "2015-01-06",
            "2016-01-08",
            "2016-05-03",
            "2016-05-04",
            "2017-03-20",
            "2017-05-08",
            "2017-11-06",
            "2018-01-02",
            "2018-01-03",
            "2018-03-09",
            "2018-04-30",
            "2018-08-20",
            "2018-09-03",
            "2018-11-09",
            "2019-01-02",
            "2019-01-03",
            "2019-01-04",
            "2019-05-10",
            "2020-01-02",
            "2020-01-03",
            "2020-01-06",
            "2020-05-04",
            "2021-01-08",
            "2021-07-19",
            "2021-08-30",
            "2022-01-04",
            "2022-01-05",
            "2022-01-06",
            "2022-05-04",
            "2022-05-06",
            "2023-01-03",
            "2023-01-04",
            "2023-01-05",
            "2023-01-06",
            "2023-03-20",
            "2023-05-08",
            "2023-11-06",
            "2024-01-02",
            "2024-01-03",
            "2024-01-04",
            "2024-01-05",
            "2024-03-22",
            "2024-05-02",
            "2024-05-03",
            "2025-01-02",
        )

    def test_workdays(self):
        self.assertWorkingDay(
            "2006-01-15",
            "2006-12-30",
            "2007-01-13",
            "2007-12-29",
            "2007-12-30",
            "2008-01-12",
            "2008-12-27",
            "2009-01-10",
            "2009-01-17",
            "2009-03-28",
            "2009-05-16",
            "2009-12-26",
            "2010-01-16",
            "2010-01-23",
            "2010-01-30",
            "2010-02-06",
            "2010-02-20",
            "2010-08-28",
            "2010-11-13",
            "2011-03-05",
            "2011-05-14",
            "2012-01-14",
            "2012-01-21",
            "2012-01-28",
            "2012-02-04",
            "2012-12-29",
            "2013-01-12",
            "2013-01-19",
            "2013-05-06",
            "2013-08-17",
            "2013-10-12",
            "2013-11-16",
            "2014-01-11",
            "2014-01-18",
            "2014-01-25",
            "2014-08-02",
            "2014-09-01",
            "2015-01-10",
            "2015-02-21",
            "2015-03-23",
            "2016-01-16",
            "2016-04-30",
            "2016-05-07",
            "2017-03-25",
            "2017-05-13",
            "2017-10-28",
            "2017-12-30",
            "2018-01-08",
            "2018-03-03",
            "2018-04-28",
            "2018-09-22",
            "2018-05-07",
            "2018-11-03",
            "2019-02-25",
            "2019-04-08",
            "2019-09-02",
            "2019-05-06",
            "2020-02-24",
            "2020-03-09",
            "2020-03-23",
            "2020-05-11",
            "2021-05-03",
            "2021-07-24",
            "2021-05-10",
            "2022-01-15",
            "2022-02-26",
            "2022-03-26",
            "2022-04-30",
            "2022-05-14",
            "2023-01-09",
            "2023-02-25",
            "2023-03-11",
            "2023-03-25",
            "2023-04-29",
            "2023-05-13",
            "2023-11-11",
            "2024-01-08",
            "2024-01-27",
            "2024-03-02",
            "2024-09-02",
            "2024-04-08",
            "2024-05-06",
            "2024-05-11",
            "2025-01-11",
        )

        for year, dts in {
            2006: (
                "2006-01-15",
                "2006-12-30",
            ),
            2007: (
                "2007-01-13",
                "2007-12-29",
                "2007-12-30",
            ),
            2008: (
                "2008-01-12",
                "2008-12-27",
            ),
            2012: (
                "2012-01-14",
                "2012-01-21",
                "2012-01-28",
                "2012-02-04",
                "2012-12-29",
            ),
            2017: (
                "2017-03-25",
                "2017-05-13",
                "2017-10-28",
                "2017-12-30",
            ),
        }.items():
            self.assertWorkingDay(Kyrgyzstan(years=year), dts)

    def test_new_years_day(self):
        name = "Жаңы жыл"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))

        obs_dts = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_new_year_holidays(self):
        name = "Жаңы жылдык каникулдар"
        self.assertHolidayName(
            name,
            (f"{year}-01-02" for year in range(2026, self.end_year)),
            (f"{year}-01-03" for year in range(2026, self.end_year)),
            (f"{year}-01-04" for year in range(2026, self.end_year)),
            (f"{year}-01-05" for year in range(2026, self.end_year)),
            (f"{year}-01-06" for year in range(2026, self.end_year)),
        )
        self.assertNoHolidayName(name, range(self.start_year, 2026))

    def test_christmas_day(self):
        name = "Ыйса Пайгамбардын туулган күнү"
        self.assertHolidayName(name, (f"{year}-01-07" for year in self.full_range))

        obs_dts = (
            "1995-01-09",
            "1996-01-08",
            "2001-01-08",
            "2007-01-05",  # special.
            "2017-01-09",
        )
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_day_of_fatherland_defenders(self):
        name_2005 = "Ата-Журтту коргоонун күнү"
        name_2025 = "Мекенди коргоочулардын күнү"
        self.assertHolidayName(name_2005, (f"{year}-02-23" for year in range(2005, 2025)))
        self.assertNoHolidayName(
            name_2005, range(self.start_year, 2005), range(2025, self.end_year)
        )
        self.assertNoHolidayName(name_2025)

        obs_dts = (
            "2013-02-25",
            "2014-02-24",
        )
        self.assertHolidayName(f"{name_2005} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        self.assertWorkdayHolidayName(
            name_2025, (f"{year}-02-23" for year in range(2025, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name_2025, range(self.start_year, 2025))
        self.assertNoWorkdayHolidayName(name_2005)

    def test_international_womens_day(self):
        name_1992 = "Аялдар күнү"
        name_2005 = "Аялдардын эл аралык күнү"
        self.assertHolidayName(
            name_1992, (f"{year}-03-08" for year in range(self.start_year, 2005))
        )
        self.assertHolidayName(name_2005, (f"{year}-03-08" for year in range(2005, self.end_year)))
        self.assertNoHolidayName(name_1992, range(2005, self.end_year))
        self.assertNoHolidayName(name_2005, range(self.start_year, 2005))

        obs_dts_1992 = (
            "1992-03-09",
            "1997-03-10",
            "1998-03-09",
            "2003-03-10",
        )
        obs_dts_2005 = (
            "2009-03-09",
            "2014-03-10",
            "2015-03-09",
        )
        self.assertHolidayName(f"{name_1992} (көрүлгөн күнү)", obs_dts_1992)
        self.assertHolidayName(f"{name_2005} (көрүлгөн күнү)", obs_dts_2005)
        self.assertNoNonObservedHoliday(obs_dts_1992, obs_dts_2005)

    def test_nooruz_holiday(self):
        name = "Элдик Нооруз майрамы"
        self.assertHolidayName(name, (f"{year}-03-21" for year in self.full_range))

        obs_dts = (
            "1998-03-23",
            "1999-03-22",
            "2004-03-22",
            "2010-03-22",
            "2021-03-22",
        )
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_day_of_the_peoples_revolution(self):
        name = "Элдик революция күнү"
        self.assertHolidayName(name, (f"{year}-03-24" for year in range(2008, 2013)))
        self.assertNoHolidayName(name, range(self.start_year, 2008), range(2013, self.end_year))

        obs_dts = ("2012-03-26",)
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_day_of_the_peoples_april_revolution(self):
        name = "Элдик Апрель революциясы күнү"
        self.assertHolidayName(name, (f"{year}-04-07" for year in range(2016, 2025)))
        self.assertNoHolidayName(name, range(self.start_year, 2016), range(2025, self.end_year))

        obs_dts = ("2018-04-09",)
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        self.assertWorkdayHolidayName(
            name, (f"{year}-04-07" for year in range(2025, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2025))

    def test_labor_day(self):
        name_1992 = "Эмгекчилердин эл аралык тилектештик күнү"
        name_1998 = "Эмгек майрамы"
        self.assertHolidayName(
            name_1992, (f"{year}-05-01" for year in range(self.start_year, 1998))
        )
        self.assertHolidayName(name_1998, (f"{year}-05-01" for year in range(1998, self.end_year)))
        self.assertNoHolidayName(name_1992, range(1998, self.end_year))
        self.assertNoHolidayName(name_1998, range(self.start_year, 1998))

        obs_dts_1992 = (
            "1993-05-03",
            "1994-05-02",
        )
        obs_dts_1998 = (
            "2005-05-02",
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name_1992} (көрүлгөн күнү)", obs_dts_1992)
        self.assertHolidayName(f"{name_1998} (көрүлгөн күнү)", obs_dts_1998)
        self.assertNoNonObservedHoliday(obs_dts_1992, obs_dts_1998)

    def test_constitution_day(self):
        name = "Кыргыз Республикасынын Конституция күнү"
        self.assertHolidayName(name, (f"{year}-05-05" for year in self.full_range))

        obs_dts = (
            "1996-05-06",
            "2001-05-07",
            "2002-05-06",
            "2012-05-07",
        )
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_may_holidays(self):
        name = "Май каникулдары"
        self.assertHolidayName(
            name,
            (f"{year}-05-02" for year in range(2025, self.end_year)),
            (f"{year}-05-03" for year in range(2025, self.end_year)),
            (f"{year}-05-04" for year in range(2025, self.end_year)),
            (f"{year}-05-06" for year in range(2025, self.end_year)),
            (f"{year}-05-07" for year in range(2025, self.end_year)),
            (f"{year}-05-08" for year in range(2025, self.end_year)),
        )
        self.assertNoHolidayName(name, range(self.start_year, 2025))

    def test_victory_day(self):
        name = "Жеңиш күнү"
        self.assertHolidayName(name, (f"{year}-05-09" for year in self.full_range))

        obs_dts = (
            "2004-05-10",
            "2009-05-11",
            "2010-05-10",
            "2015-05-11",
        )
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Кыргыз Республикасынын Көз карандысыздыгынын күнү"
        self.assertHolidayName(name, (f"{year}-08-31" for year in self.full_range))

        obs_dts = (
            "2002-09-02",
            "2003-09-01",
            "2008-09-01",
            "2013-09-02",
        )
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_days_of_history_and_commemoration_of_ancestors(self):
        name_2002 = "Улуу Октябрь социалисттик революциясынын күнү"
        name_2018 = "Тарых жана ата-бабаларды эскерүү күндөрү"

        self.assertHolidayName(name_2002, (f"{year}-11-07" for year in range(2002, 2018)))
        self.assertNoHolidayName(
            name_2002, range(self.start_year, 2002), range(2018, self.end_year)
        )
        self.assertHolidayName(
            name_2018,
            (f"{year}-11-07" for year in range(2018, 2025)),
            (f"{year}-11-08" for year in range(2018, 2025)),
        )
        self.assertNoHolidayName(
            name_2018, range(self.start_year, 2018), range(2025, self.end_year)
        )

        obs_dts_2002 = (
            "2004-11-08",
            "2009-11-09",
            "2010-11-08",
            "2015-11-09",
        )
        obs_dts_2018 = (
            "2020-11-09",
            "2020-11-10",
            "2021-11-09",
        )
        self.assertHolidayName(f"{name_2002} (көрүлгөн күнү)", obs_dts_2002)
        self.assertHolidayName(f"{name_2018} (көрүлгөн күнү)", obs_dts_2018)
        self.assertNoNonObservedHoliday(obs_dts_2002, obs_dts_2018)

        self.assertWorkdayHolidayName(
            name_2018,
            (f"{year}-11-07" for year in range(2025, self.end_year)),
            (f"{year}-11-08" for year in range(2025, self.end_year)),
        )
        self.assertNoWorkdayHolidayName(name_2002)
        self.assertNoWorkdayHolidayName(name_2018, range(self.start_year, 2025))

    def test_eid_al_fitr(self):
        name = "Орозо айт"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-03",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

        obs_dts = (
            "2012-08-20",  # special.
            "2020-05-25",
        )
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_kurman_ait(self):
        name = "Курман айт"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-17",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

        obs_dts = (
            "2007-01-02",  # special.
            "2011-11-08",  # special.
            "2014-10-06",
            "2019-08-12",
            "2022-07-11",
        )
        self.assertHolidayName(f"{name} (көрүлгөн күнү)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Жаңы жыл"),
            ("2022-01-03", "Жаңы жыл (көрүлгөн күнү)"),
            ("2022-01-04", "Эс алуу күнү (15.01.2022 күнүнөн которулган)"),
            ("2022-01-05", "Эс алуу күнү (26.02.2022 күнүнөн которулган)"),
            ("2022-01-06", "Эс алуу күнү (26.03.2022 күнүнөн которулган)"),
            ("2022-01-07", "Ыйса Пайгамбардын туулган күнү"),
            ("2022-02-23", "Ата-Журтту коргоонун күнү"),
            ("2022-03-08", "Аялдардын эл аралык күнү"),
            ("2022-03-21", "Элдик Нооруз майрамы"),
            ("2022-04-07", "Элдик Апрель революциясы күнү"),
            ("2022-05-01", "Эмгек майрамы"),
            ("2022-05-02", "Эмгек майрамы (көрүлгөн күнү)"),
            ("2022-05-03", "Орозо айт"),
            ("2022-05-04", "Эс алуу күнү (30.04.2022 күнүнөн которулган)"),
            ("2022-05-05", "Кыргыз Республикасынын Конституция күнү"),
            ("2022-05-06", "Эс алуу күнү (14.05.2022 күнүнөн которулган)"),
            ("2022-05-09", "Жеңиш күнү"),
            ("2022-07-09", "Курман айт"),
            ("2022-07-11", "Курман айт (көрүлгөн күнү)"),
            ("2022-08-31", "Кыргыз Республикасынын Көз карандысыздыгынын күнү"),
            ("2022-11-07", "Тарых жана ата-бабаларды эскерүү күндөрү"),
            ("2022-11-08", "Тарых жана ата-бабаларды эскерүү күндөрү"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Жаңы жыл"),
            ("2025-01-02", "Эс алуу күнү (11.01.2025 күнүнөн которулган)"),
            ("2025-01-03", "Кошумча эс алуу күнү"),
            ("2025-01-06", "Кошумча эс алуу күнү"),
            ("2025-01-07", "Ыйса Пайгамбардын туулган күнү"),
            ("2025-03-08", "Аялдардын эл аралык күнү"),
            ("2025-03-21", "Элдик Нооруз майрамы"),
            ("2025-03-30", "Орозо айт"),
            ("2025-05-01", "Эмгек майрамы"),
            ("2025-05-02", "Май каникулдары"),
            ("2025-05-03", "Май каникулдары"),
            ("2025-05-04", "Май каникулдары"),
            ("2025-05-05", "Кыргыз Республикасынын Конституция күнү"),
            ("2025-05-06", "Май каникулдары"),
            ("2025-05-07", "Май каникулдары"),
            ("2025-05-08", "Май каникулдары"),
            ("2025-05-09", "Жеңиш күнү"),
            ("2025-06-06", "Курман айт"),
            ("2025-08-31", "Кыргыз Республикасынын Көз карандысыздыгынын күнү"),
        )

        self.assertWorkdayHolidaysInYear(
            2025,
            ("2025-02-23", "Мекенди коргоочулардын күнү"),
            ("2025-04-07", "Элдик Апрель революциясы күнү"),
            ("2025-11-07", "Тарых жана ата-бабаларды эскерүү күндөрү"),
            ("2025-11-08", "Тарых жана ата-бабаларды эскерүү күндөрү"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Жаңы жыл"),
            ("2024-01-02", "Эс алуу күнү (08.01.2024 күнүнөн которулган)"),
            ("2024-01-03", "Эс алуу күнү (27.01.2024 күнүнөн которулган)"),
            ("2024-01-04", "Эс алуу күнү (02.03.2024 күнүнөн которулган)"),
            ("2024-01-05", "Эс алуу күнү (02.09.2024 күнүнөн которулган)"),
            ("2024-01-07", "Ыйса Пайгамбардын туулган күнү"),
            ("2024-02-23", "Ата-Журтту коргоонун күнү"),
            ("2024-03-08", "Аялдардын эл аралык күнү"),
            ("2024-03-21", "Элдик Нооруз майрамы"),
            ("2024-03-22", "Эс алуу күнү (08.04.2024 күнүнөн которулган)"),
            ("2024-04-07", "Элдик Апрель революциясы күнү"),
            ("2024-04-10", "Орозо айт"),
            ("2024-05-01", "Эмгек майрамы"),
            ("2024-05-02", "Эс алуу күнү (06.05.2024 күнүнөн которулган)"),
            ("2024-05-03", "Эс алуу күнү (11.05.2024 күнүнөн которулган)"),
            ("2024-05-05", "Кыргыз Республикасынын Конституция күнү"),
            ("2024-05-09", "Жеңиш күнү"),
            ("2024-06-17", "Курман айт"),
            ("2024-08-31", "Кыргыз Республикасынын Көз карандысыздыгынын күнү"),
            ("2024-11-07", "Тарых жана ата-бабаларды эскерүү күндөрү"),
            ("2024-11-08", "Тарых жана ата-бабаларды эскерүү күндөрү"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "Day off (substituted from 01/08/2024)"),
            ("2024-01-03", "Day off (substituted from 01/27/2024)"),
            ("2024-01-04", "Day off (substituted from 03/02/2024)"),
            ("2024-01-05", "Day off (substituted from 09/02/2024)"),
            ("2024-01-07", "Christmas Day"),
            ("2024-02-23", "Fatherland Defender's Day"),
            ("2024-03-08", "International Women's Day"),
            ("2024-03-21", "Nooruz Holiday"),
            ("2024-03-22", "Day off (substituted from 04/08/2024)"),
            ("2024-04-07", "Day of the People's April Revolution"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-02", "Day off (substituted from 05/06/2024)"),
            ("2024-05-03", "Day off (substituted from 05/11/2024)"),
            ("2024-05-05", "Constitution Day"),
            ("2024-05-09", "Victory Day"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-08-31", "Independence Day"),
            ("2024-11-07", "Days of History and Commemoration of Ancestors"),
            ("2024-11-08", "Days of History and Commemoration of Ancestors"),
        )

    def test_l10n_ru_kg(self):
        self.assertLocalizedHolidays(
            "ru_KG",
            ("2024-01-01", "Новый год"),
            ("2024-01-02", "Выходной (перенесено с 08.01.2024)"),
            ("2024-01-03", "Выходной (перенесено с 27.01.2024)"),
            ("2024-01-04", "Выходной (перенесено с 02.03.2024)"),
            ("2024-01-05", "Выходной (перенесено с 02.09.2024)"),
            ("2024-01-07", "Рождество Христово"),
            ("2024-02-23", "День защитника Отечества"),
            ("2024-03-08", "Международный женский день"),
            ("2024-03-21", "Народный праздник Нооруз"),
            ("2024-03-22", "Выходной (перенесено с 08.04.2024)"),
            ("2024-04-07", "День народной Апрельской революции"),
            ("2024-04-10", "Орозо айт"),
            ("2024-05-01", "Праздник труда"),
            ("2024-05-02", "Выходной (перенесено с 06.05.2024)"),
            ("2024-05-03", "Выходной (перенесено с 11.05.2024)"),
            ("2024-05-05", "День Конституции Кыргызской Республики"),
            ("2024-05-09", "День Победы"),
            ("2024-06-17", "Курман айт"),
            ("2024-08-31", "День независимости Кыргызской Республики"),
            ("2024-11-07", "Дни истории и памяти предков"),
            ("2024-11-08", "Дни истории и памяти предков"),
        )
