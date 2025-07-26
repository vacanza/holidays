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

from holidays.countries.turkmenistan import Turkmenistan, TM, TKM
from tests.common import CommonCountryTests


class TestTurkmenistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1992, 2050)
        super().setUpClass(Turkmenistan, years=years)
        cls.no_estimated_holidays = Turkmenistan(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Turkmenistan, TM, TKM)

    def test_no_holidays(self):
        self.assertNoHolidays(Turkmenistan(years=1991))

    def test_new_years_day(self):
        name = "Täze ýyl"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1992, 2050)))
        obs_dt = (
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_state_flag_day(self):
        name = "Türkmenistanyň Döwlet baýdagynyň güni"
        self.assertHolidayName(name, (f"{year}-02-19" for year in range(1992, 2018)))
        self.assertNoHolidayName(name, range(2019, 2050))
        obs_dt = (
            "1995-02-20",
            "2006-02-20",
            "2012-02-20",
            "2017-02-20",
        )
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_womens_day(self):
        name = "Halkara zenanlar güni"
        self.assertHolidayName(
            name, (f"{year}-03-08" for year in (*range(1992, 2001), *range(2008, 2050)))
        )
        self.assertNoHolidayName(name, range(2001, 2008))
        obs_dt = (
            "1992-03-09",
            "1998-03-09",
            "2009-03-09",
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_womens_and_spring_day(self):
        name = "Milli bahar baýramy"
        self.assertHolidayName(name, (f"{year}-03-20" for year in range(2001, 2008)))
        self.assertNoHolidayName(name, range(1992, 2001), range(2009, 2050))
        obs_dt = ("2005-03-23",)
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_nowruz(self):
        name = "Nowruz"
        self.assertHolidayName(name, (f"{year}-03-21" for year in range(1992, 2050)))
        self.assertHolidayName(name, (f"{year}-03-22" for year in range(1992, 2050)))
        obs_dt = ("2009-03-23", "2010-03-23", "2015-03-23", "2020-03-23", "2021-03-23")
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_state_flag_and_constitution_day(self):
        name = "Türkmenistanyň Konstitusiýasynyň we Döwlet baýdagynyň güni"
        self.assertHolidayName(name, (f"{year}-05-18" for year in range(2018, 2050)))
        self.assertNoHolidayName(name, range(1992, 2018))
        obs_dt = ("2025-05-19",)
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        name = "Garaşsyzlyk baýramy"
        self.assertHolidayName(name, (f"{year}-10-27" for year in range(1992, 2018)))
        self.assertHolidayName(name, (f"{year}-09-27" for year in range(2018, 2050)))
        obs_dt = (
            "1996-10-28",
            "2002-10-28",
            "2013-10-28",
            "2020-09-28",
        )
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_remembrance_day(self):
        name = "Hatyra güni"
        self.assertHolidayName(name, (f"{year}-10-06" for year in range(1995, 2050)))
        self.assertNoHolidayName(name, range(1992, 1995))
        obs_dt = (
            "1996-10-07",
            "2002-10-07",
            "2013-10-07",
            "2019-10-07",
            "2014-10-07",
        )
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_neutrality_day(self):
        name = "Bitaraplyk baýramy"
        self.assertHolidayName(name, (f"{year}-12-12" for year in range(1995, 2050)))
        self.assertNoHolidayName(name, range(1992, 1995))
        obs_dt = (
            "1999-12-13",
            "2004-12-13",
            "2010-12-13",
            "2021-12-13",
        )
        self.assertHolidayName(f"{name} (syn edildi)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_fitr(self):
        name = "Uraza Bayram"
        dts = (
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1992, 2050))
        obs_dt = ("2009-09-21", "2012-08-20", "2017-06-06", "2020-05-25", "2025-03-31")
        self.assertHolidayName(f"{name} (syn edildi)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_adha(self):
        name = "Kurban Bayram"
        dts = (
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1992, 2050))
        obs_dt = (
            "2004-02-02",
            "2011-11-07",
            "2016-09-12",
            "2019-08-12",
            "2024-06-17",
        )
        self.assertHolidayName(f"{name} (syn edildi)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Täze ýyl"),
            ("2024-03-08", "Halkara zenanlar güni"),
            ("2024-03-21", "Nowruz"),
            ("2024-03-22", "Nowruz"),
            ("2024-04-10", "Uraza Bayram"),
            ("2024-05-18", "Türkmenistanyň Konstitusiýasynyň we Döwlet baýdagynyň güni"),
            ("2024-06-16", "Kurban Bayram"),
            ("2024-06-17", "Kurban Bayram (syn edildi)"),
            ("2024-09-27", "Garaşsyzlyk baýramy"),
            ("2024-10-06", "Hatyra güni"),
            ("2024-10-07", "Hatyra güni (syn edildi)"),
            ("2024-12-12", "Bitaraplyk baýramy"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-08", "International Women's Day"),
            ("2024-03-21", "Nowruz"),
            ("2024-03-22", "Nowruz"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-18", "State Flag and Constitution Day"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-17", "Eid al-Adha (observed)"),
            ("2024-09-27", "Independence Day"),
            ("2024-10-06", "Remembrance Day"),
            ("2024-10-07", "Remembrance Day (observed)"),
            ("2024-12-12", "International Neutrality Day"),
        )

    def test_l10n_ru(self):
        self.assertLocalizedHolidays(
            "ru",
            ("2024-01-01", "Новый год"),
            ("2024-03-08", "Международный женский день"),
            ("2024-03-21", "Навруз"),
            ("2024-03-22", "Навруз"),
            ("2024-04-10", "Ид аль-Фитр"),
            ("2024-05-18", "Государственный флаг и День Конституции"),
            ("2024-06-16", "Ид аль-Адха"),
            ("2024-06-17", "Ид аль-Адха (наблюдал)"),
            ("2024-09-27", "День независимости"),
            ("2024-10-06", "День памяти"),
            ("2024-10-07", "День памяти (наблюдал)"),
            ("2024-12-12", "Международный день нейтралитета"),
        )
