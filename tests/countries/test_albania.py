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

from holidays.countries.albania import Albania, AL, ALB
from tests.common import CommonCountryTests


class TestAlbania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Albania, years=range(1993, 2050))

    def test_country_aliases(self):
        self.assertAliases(Albania, AL, ALB)

    def test_no_holidays(self):
        self.assertNoHolidays(Albania(years=1992))

    def test_special_holidays(self):
        self.assertHoliday(
            "2020-01-03",
            "2022-03-21",
            "2024-03-15",
        )

    def test_new_years_day(self):
        self.assertHolidayName(
            "Festat e Vitit të Ri",
            (f"{year}-01-01" for year in range(1993, 2050)),
            (f"{year}-01-02" for year in range(1993, 2050)),
        )

    def test_summer_day(self):
        name = "Dita e Verës"
        self.assertHolidayName(name, (f"{year}-03-14" for year in range(2004, 2050)))
        self.assertNoHolidayName(name, range(1993, 2004))

    def test_nowruz_day(self):
        name = "Dita e Nevruzit"
        self.assertHolidayName(name, (f"{year}-03-22" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, range(1993, 1996))

    def test_catholic_easter_sunday(self):
        name = "E diela e Pashkëve Katolike"
        self.assertHolidayName(
            name,
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
        )
        self.assertHolidayName(name, range(1993, 2050))

    def test_orthodox_easter_sunday(self):
        name = "E diela e Pashkëve Ortodokse"
        self.assertHolidayName(
            name,
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
        )
        self.assertHolidayName(name, range(1993, 2050))

    def test_international_workers_day(self):
        self.assertHolidayName(
            "Dita Ndërkombëtare e Punëtorëve", (f"{year}-05-01" for year in range(1993, 2050))
        )

    def test_mother_teresa_day(self):
        name1 = "Dita e Lumturimit të Shenjt Terezës"
        name2 = "Dita e Shenjtërimit të Shenjt Terezës"
        self.assertHolidayName(name1, (f"{year}-10-19" for year in range(2004, 2018)))
        self.assertNoHolidayName(name1, range(1993, 2004), range(2018, 2050))
        self.assertHolidayName(name2, (f"{year}-09-05" for year in range(2018, 2050)))
        self.assertNoHolidayName(name2, range(1993, 2018))

    def test_alphabet_day(self):
        name = "Dita e Alfabetit"
        self.assertHolidayName(name, (f"{year}-11-22" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1993, 2024))

    def test_flag_and_independence_day(self):
        self.assertHolidayName(
            "Dita Flamurit dhe e Pavarësisë", (f"{year}-11-28" for year in range(1993, 2050))
        )

    def test_liberation_day(self):
        self.assertHolidayName("Dita e Çlirimit", (f"{year}-11-29" for year in range(1993, 2050)))

    def test_national_youth_day(self):
        name = "Dita Kombëtare e Rinisë"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(2009, 2050)))
        self.assertNoHolidayName(name, range(1993, 2009))

    def test_christmas_day(self):
        self.assertHolidayName("Krishtlindjet", (f"{year}-12-25" for year in range(1993, 2050)))

    def test_eid_al_fitr(self):
        name = "Dita e Bajramit të Madh"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1993, 2050)).issubset(years_found))

    def test_eid_al_adha(self):
        name = "Dita e Kurban Bajramit"
        self.assertHolidayName(
            name,
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
        )
        self.assertHoliday(
            "2006-01-10",
            "2006-12-31",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(1993, 2050)).issubset(years_found))

    def test_observed(self):
        dt = (
            # New Year's Day.
            "2012-01-03",
            "2016-01-04",
            "2017-01-03",
            "2021-01-04",
            "2022-01-03",
            "2022-01-04",
            "2023-01-03",
            # Summer Day.
            "2010-03-15",
            "2015-03-16",
            "2020-03-16",
            "2021-03-15",
            # Nowruz Day.
            "2014-03-24",
            "2015-03-23",
            "2020-03-23",
            # International Workers' Day.
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            # Mother Teresa Beatification/Canonization Day.
            "2013-10-21",
            "2014-10-20",
            "2020-09-07",
            "2021-09-06",
            # Alphabet Day.
            "2025-11-24",
            "2026-11-23",
            # Flag and Independence Day.
            "2010-11-30",
            "2015-11-30",
            "2020-11-30",
            "2021-11-30",
            # Liberation Day.
            "2014-12-01",
            "2015-12-01",
            "2020-12-01",
            # National Youth Day.
            "2012-12-10",
            "2013-12-09",
            "2018-12-10",
            "2019-12-09",
            "2024-12-09",
            # Christmas Day.
            "2010-12-27",
            "2011-12-26",
            "2016-12-26",
            "2021-12-27",
            "2022-12-26",
            # Eid al-Fitr.
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
            # Eid al-Adha.
            "2007-01-03",
            "2014-10-06",
            "2016-09-12",
            "2019-08-12",
            "2022-07-11",
            "2024-06-17",
            # special cases:
            # Catholic Easter Sunday.
            "2008-03-25",
            # Orthodox Easter Sunday.
            "2000-05-02",
            "2021-05-04",
            "2027-05-04",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            Albania(years=2022),
            ("2022-01-01", "Festat e Vitit të Ri"),
            ("2022-01-02", "Festat e Vitit të Ri"),
            ("2022-01-03", "Festat e Vitit të Ri (ditë pushimi e shtyrë)"),
            ("2022-01-04", "Festat e Vitit të Ri (ditë pushimi e shtyrë)"),
            ("2022-03-14", "Dita e Verës"),
            ("2022-03-21", "Ditë pushimi"),
            ("2022-03-22", "Dita e Nevruzit"),
            ("2022-04-17", "E diela e Pashkëve Katolike"),
            ("2022-04-18", "E diela e Pashkëve Katolike (ditë pushimi e shtyrë)"),
            ("2022-04-24", "E diela e Pashkëve Ortodokse"),
            ("2022-04-25", "E diela e Pashkëve Ortodokse (ditë pushimi e shtyrë)"),
            ("2022-05-01", "Dita Ndërkombëtare e Punëtorëve"),
            ("2022-05-02", "Dita e Bajramit të Madh"),
            ("2022-05-03", "Dita Ndërkombëtare e Punëtorëve (ditë pushimi e shtyrë)"),
            ("2022-07-09", "Dita e Kurban Bajramit"),
            ("2022-07-11", "Dita e Kurban Bajramit (ditë pushimi e shtyrë)"),
            ("2022-09-05", "Dita e Shenjtërimit të Shenjt Terezës"),
            ("2022-11-28", "Dita Flamurit dhe e Pavarësisë"),
            ("2022-11-29", "Dita e Çlirimit"),
            ("2022-12-08", "Dita Kombëtare e Rinisë"),
            ("2022-12-25", "Krishtlindjet"),
            ("2022-12-26", "Krishtlindjet (ditë pushimi e shtyrë)"),
        )

    def test_2023(self):
        self.assertHolidays(
            Albania(years=2023),
            ("2023-01-01", "Festat e Vitit të Ri"),
            ("2023-01-02", "Festat e Vitit të Ri"),
            ("2023-01-03", "Festat e Vitit të Ri (ditë pushimi e shtyrë)"),
            ("2023-03-14", "Dita e Verës"),
            ("2023-03-22", "Dita e Nevruzit"),
            ("2023-04-09", "E diela e Pashkëve Katolike"),
            ("2023-04-10", "E diela e Pashkëve Katolike (ditë pushimi e shtyrë)"),
            ("2023-04-16", "E diela e Pashkëve Ortodokse"),
            ("2023-04-17", "E diela e Pashkëve Ortodokse (ditë pushimi e shtyrë)"),
            ("2023-04-21", "Dita e Bajramit të Madh"),
            ("2023-05-01", "Dita Ndërkombëtare e Punëtorëve"),
            ("2023-06-28", "Dita e Kurban Bajramit"),
            ("2023-09-05", "Dita e Shenjtërimit të Shenjt Terezës"),
            ("2023-11-28", "Dita Flamurit dhe e Pavarësisë"),
            ("2023-11-29", "Dita e Çlirimit"),
            ("2023-12-08", "Dita Kombëtare e Rinisë"),
            ("2023-12-25", "Krishtlindjet"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Festat e Vitit të Ri"),
            ("2024-01-02", "Festat e Vitit të Ri"),
            ("2024-03-14", "Dita e Verës"),
            ("2024-03-15", "Ditë pushimi"),
            ("2024-03-22", "Dita e Nevruzit"),
            ("2024-03-31", "E diela e Pashkëve Katolike"),
            ("2024-04-01", "E diela e Pashkëve Katolike (ditë pushimi e shtyrë)"),
            ("2024-04-10", "Dita e Bajramit të Madh"),
            ("2024-05-01", "Dita Ndërkombëtare e Punëtorëve"),
            ("2024-05-05", "E diela e Pashkëve Ortodokse"),
            ("2024-05-06", "E diela e Pashkëve Ortodokse (ditë pushimi e shtyrë)"),
            ("2024-06-16", "Dita e Kurban Bajramit"),
            ("2024-06-17", "Dita e Kurban Bajramit (ditë pushimi e shtyrë)"),
            ("2024-09-05", "Dita e Shenjtërimit të Shenjt Terezës"),
            ("2024-11-22", "Dita e Alfabetit"),
            ("2024-11-28", "Dita Flamurit dhe e Pavarësisë"),
            ("2024-11-29", "Dita e Çlirimit"),
            ("2024-12-08", "Dita Kombëtare e Rinisë"),
            ("2024-12-09", "Dita Kombëtare e Rinisë (ditë pushimi e shtyrë)"),
            ("2024-12-25", "Krishtlindjet"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year's Day"),
            ("2024-03-14", "Summer Day"),
            ("2024-03-15", "Public Holiday"),
            ("2024-03-22", "Nowruz Day"),
            ("2024-03-31", "Catholic Easter Sunday"),
            ("2024-04-01", "Catholic Easter Sunday (observed)"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-01", "International Workers' Day"),
            ("2024-05-05", "Orthodox Easter Sunday"),
            ("2024-05-06", "Orthodox Easter Sunday (observed)"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-17", "Eid al-Adha (observed)"),
            ("2024-09-05", "Mother Teresa Canonization Day"),
            ("2024-11-22", "Alphabet Day"),
            ("2024-11-28", "Flag and Independence Day"),
            ("2024-11-29", "Liberation Day"),
            ("2024-12-08", "National Youth Day"),
            ("2024-12-09", "National Youth Day (observed)"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-01-02", "Новий рік"),
            ("2024-03-14", "День літа"),
            ("2024-03-15", "Вихідний день"),
            ("2024-03-22", "Свято Новруз"),
            ("2024-03-31", "Великдень (католицький)"),
            ("2024-04-01", "Великдень (католицький) (вихідний)"),
            ("2024-04-10", "Рамазан-байрам"),
            ("2024-05-01", "Міжнародний день трудящих"),
            ("2024-05-05", "Великдень (православний)"),
            ("2024-05-06", "Великдень (православний) (вихідний)"),
            ("2024-06-16", "Курбан-байрам"),
            ("2024-06-17", "Курбан-байрам (вихідний)"),
            ("2024-09-05", "День канонізації матері Терези"),
            ("2024-11-22", "День алфавіту"),
            ("2024-11-28", "День прапора та незалежності"),
            ("2024-11-29", "День визволення"),
            ("2024-12-08", "Національний день молоді"),
            ("2024-12-09", "Національний день молоді (вихідний)"),
            ("2024-12-25", "Різдво Христове"),
        )
