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

from holidays.countries.namibia import Namibia
from tests.common import CommonCountryTests


class TestNamibia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1991, 2050)
        super().setUpClass(Namibia, years=years, years_non_observed=years)

    def test_special_holidays(self):
        self.assertHoliday(
            "1994-03-01",
            "1994-12-07",
            "1995-10-24",
            "1997-09-26",
            "1998-11-30",
            "1999-11-30",
            "1999-12-31",
            "2000-01-03",
            "2014-11-28",
            "2015-11-27",
            "2019-11-27",
            "2020-11-25",
            "2024-02-25",
            "2024-11-27",
            "2025-03-01",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1991, 2050)))
        obs_dt = (
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-03-21" for year in range(1991, 2050)))
        obs_dt = (
            "1993-03-22",
            "1999-03-22",
            "2004-03-22",
            "2010-03-22",
            "2021-03-22",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

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
        self.assertHolidayName(name, range(1991, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1991, 2050))

    def test_workers_day(self):
        name = "Workers' Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1991, 2050)))
        obs_dt = (
            "1994-05-02",
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_cassinga_day(self):
        name = "Cassinga Day"
        self.assertHolidayName(name, (f"{year}-05-04" for year in range(1991, 2050)))
        obs_dt = (
            "1997-05-05",
            "2003-05-05",
            "2008-05-05",
            "2014-05-05",
            "2025-05-05",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_africa_day(self):
        name = "Africa Day"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(1991, 2050)))
        obs_dt = (
            "1997-05-26",
            "2003-05-26",
            "2008-05-26",
            "2014-05-26",
            "2025-05-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_genocide_remembrance_day(self):
        name = "Genocide Remembrance Day"
        self.assertHolidayName(name, (f"{year}-05-28" for year in range(2025, 2050)))
        self.assertNoHolidayName(name, range(1991, 2025))

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, range(1991, 2050))

    def test_heroes_day(self):
        name = "Heroes' Day"
        self.assertHolidayName(name, (f"{year}-08-26" for year in range(1991, 2050)))
        obs_dt = (
            "2001-08-27",
            "2007-08-27",
            "2012-08-27",
            "2018-08-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_namibian_women_and_international_human_rights_day(self):
        name_1 = "International Human Rights Day"
        self.assertHolidayName(name_1, (f"{year}-09-10" for year in range(1991, 2005)))
        self.assertNoHolidayName(name_1, range(2005, 2050))
        obs_dt = (
            "1995-09-11",
            "2000-09-11",
        )
        self.assertHolidayName(f"{name_1} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        name_2 = "Day of the Namibian Women and International Human Rights Day"
        self.assertHolidayName(name_2, (f"{year}-09-10" for year in range(2005, 2050)))
        self.assertNoHolidayName(name_2, range(1991, 2005))
        obs_dt = (
            "2006-09-11",
            "2017-09-11",
            "2023-09-11",
        )
        self.assertHolidayName(f"{name_2} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1991, 2050)))

    def test_family_day(self):
        name = "Family Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1991, 2050)))
        obs_dt = (
            "1993-12-27",
            "1999-12-27",
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_2024(self):
        self.assertHolidays(
            Namibia(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-02-25", "Burial ceremony of Dr. Hage Gottfried Geingob"),
            ("2024-03-21", "Independence Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Workers' Day"),
            ("2024-05-04", "Cassinga Day"),
            ("2024-05-09", "Ascension Day"),
            ("2024-05-25", "Africa Day"),
            ("2024-08-26", "Heroes' Day"),
            ("2024-09-10", "Day of the Namibian Women and International Human Rights Day"),
            ("2024-11-27", "General Election Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Family Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-03-01", "Burial ceremony of Dr. Sam Shafiishuna Nujoma"),
            ("2025-03-21", "Independence Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Workers' Day"),
            ("2025-05-04", "Cassinga Day"),
            ("2025-05-05", "Cassinga Day (observed)"),
            ("2025-05-25", "Africa Day"),
            ("2025-05-26", "Africa Day (observed)"),
            ("2025-05-28", "Genocide Remembrance Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-08-26", "Heroes' Day"),
            ("2025-09-10", "Day of the Namibian Women and International Human Rights Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Family Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-01", "Burial ceremony of Dr. Sam Shafiishuna Nujoma"),
            ("2025-03-21", "Independence Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Workers' Day"),
            ("2025-05-04", "Cassinga Day"),
            ("2025-05-05", "Cassinga Day (observed)"),
            ("2025-05-25", "Africa Day"),
            ("2025-05-26", "Africa Day (observed)"),
            ("2025-05-28", "Genocide Remembrance Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-08-26", "Heroes' Day"),
            ("2025-09-10", "Day of the Namibian Women and International Human Rights Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Family Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2025-01-01", "Новий рік"),
            ("2025-03-01", "Церемонія поховання Сема Шафіішуна Нуйоми"),
            ("2025-03-21", "День незалежності"),
            ("2025-04-18", "Страсна пʼятниця"),
            ("2025-04-21", "Великодній понеділок"),
            ("2025-05-01", "День трудящих"),
            ("2025-05-04", "День Кассінги"),
            ("2025-05-05", "День Кассінги (вихідний)"),
            ("2025-05-25", "День Африки"),
            ("2025-05-26", "День Африки (вихідний)"),
            ("2025-05-28", "День памʼяті жертв геноциду"),
            ("2025-05-29", "Вознесіння Господнє"),
            ("2025-08-26", "День Героїв"),
            ("2025-09-10", "День намібійських жінок та Міжнародний день прав людини"),
            ("2025-12-25", "Різдво Христове"),
            ("2025-12-26", "День родини"),
        )
