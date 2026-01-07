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

from holidays.countries.north_macedonia import NorthMacedonia
from tests.common import CommonCountryTests


class TestNorthMacedonia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NorthMacedonia)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoAlbanianHoliday(range(self.start_year, 2007))
        self.assertNoBosnianHoliday(range(self.start_year, 2007))
        self.assertNoIslamicHoliday(range(self.start_year, 2007))
        self.assertNoRomaHoliday(range(self.start_year, 2007))
        self.assertNoSerbianHoliday(range(self.start_year, 2008))
        self.assertNoTurkishHoliday(range(self.start_year, 2007))
        self.assertNoVlachHoliday(range(self.start_year, 2007))

    def test_special_holidays(self):
        self.assertHoliday(
            "2024-04-24",
            "2024-05-08",
        )

    def test_new_years_day(self):
        name = "Нова Година"
        self.assertHolidayName(
            name,
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in range(self.start_year, 2008)),
        )
        self.assertNoNonObservedHolidayName(
            name, (f"{year}-01-02" for year in range(2008, self.end_year))
        )
        obs_dts = (
            "2000-01-03",
            "2005-01-03",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)

    def test_christmas_day(self):
        name = "Божиќ"
        self.assertHolidayName(name, (f"{year}-01-07" for year in range(2008, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2008))
        obs_dts = (
            "2018-01-08",
            "2024-01-08",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_easter_monday(self):
        name = "Велигден"
        self.assertHolidayName(
            name,
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
            "2024-05-06",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(2007, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2007))

    def test_labor_day(self):
        name = "Ден на трудот"
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in self.full_range),
            (f"{year}-05-02" for year in range(self.start_year, 2007)),
        )
        self.assertNoNonObservedHolidayName(
            name, (f"{year}-05-02" for year in range(2007, self.end_year))
        )
        obs_dts = (
            "1999-05-03",
            "2004-05-03",
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)

    def test_saints_cyril_and_methodius_day(self):
        name = "Светите Кирил и Методиј - Ден на сесловенските просветители"
        self.assertHolidayName(name, (f"{year}-05-24" for year in range(2007, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2007))
        obs_dts = (
            "2009-05-25",
            "2015-05-25",
            "2020-05-25",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_republic_day(self):
        name = "Ден на Републиката"
        self.assertHolidayName(name, (f"{year}-08-02" for year in self.full_range))
        obs_dts = (
            "2009-08-03",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Ден на независноста"
        self.assertHolidayName(name, (f"{year}-09-08" for year in self.full_range))
        obs_dts = (
            "2002-09-09",
            "2013-09-09",
            "2019-09-09",
            "2024-09-09",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_uprising_day(self):
        name = "Ден на народното востание"
        self.assertHolidayName(name, (f"{year}-10-11" for year in self.full_range))
        obs_dts = (
            "2009-10-12",
            "2015-10-12",
            "2020-10-12",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_revolutionary_struggle_day(self):
        name = "Ден на македонската револуционерна борба"
        self.assertHolidayName(name, (f"{year}-10-23" for year in range(2007, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2007))
        obs_dts = (
            "2011-10-24",
            "2016-10-24",
            "2022-10-24",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_saint_clement_of_ohrid_day(self):
        name = "Свети Климент Охридски"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(2007, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2007))
        obs_dts = (
            "2013-12-09",
            "2019-12-09",
            "2024-12-09",
        )
        self.assertHolidayName(f"{name} (неработен ден)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Рамазан Бајрам"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(2007, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 2007))
        obs_dts = (
            "2009-09-21",
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (неработен ден)", obs_dts)

    def test_albanian_alphabet_day(self):
        name = "Ден на Албанската азбука"
        self.assertNoHolidayName(name)
        self.assertAlbanianHolidayName(
            name, (f"{year}-11-22" for year in range(2007, self.end_year))
        )
        self.assertNoAlbanianHolidayName(name, range(self.start_year, 2007))

    def test_international_bosniaks_day(self):
        name = "Меѓународен ден на Бошњаците"
        self.assertNoHolidayName(name)
        self.assertBosnianHolidayName(
            name, (f"{year}-09-28" for year in range(2007, self.end_year))
        )
        self.assertNoBosnianHolidayName(name, range(self.start_year, 2007))

    def test_easter_monday_catholic(self):
        name = "Велигден"
        self.assertCatholicHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertCatholicHolidayName(name, self.full_range)

    def test_all_saints_day_catholic(self):
        name = "Сите Светци"
        self.assertNoHolidayName(name)
        self.assertCatholicHolidayName(
            name, (f"{year}-11-01" for year in range(2007, self.end_year))
        )
        self.assertNoCatholicHolidayName(name, range(self.start_year, 2007))

    def test_christmas_day_catholic(self):
        self.assertCatholicHolidayName("Божиќ", (f"{year}-12-25" for year in self.full_range))

    def test_yom_kippur(self):
        name = "Јом Кипур"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "2020-09-28",
            "2021-09-16",
            "2022-10-05",
            "2023-09-25",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertHebrewHolidayName(name, self.full_range)

    def test_eid_al_adha_islamic(self):
        name = "Курбан Бајрам"
        self.assertNoHolidayName(name)
        self.assertIslamicHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicIslamicNoEstimatedHolidayName(name, range(2007, self.end_year))
        self.assertNoIslamicIslamicNoEstimatedHolidayName(name, range(self.start_year, 2007))

    def test_christmas_day_orthodox(self):
        name = "Божиќ"
        self.assertOrthodoxHolidayName(
            name, (f"{year}-01-07" for year in range(self.start_year, 2008))
        )
        self.assertNoOrthodoxHolidayName(name, range(2008, self.end_year))

    def test_easter_monday_orthodox(self):
        name = "Велигден"
        self.assertOrthodoxHolidayName(
            name,
            "1999-04-12",
            "2000-05-01",
            "2001-04-16",
            "2002-05-06",
            "2003-04-28",
            "2004-04-12",
            "2005-05-02",
            "2006-04-24",
        )
        self.assertNoOrthodoxHolidayName(name, range(2007, self.end_year))

    def test_christmas_eve_orthodox(self):
        name = "Бадник"
        self.assertNoHolidayName(name)
        self.assertOrthodoxHolidayName(
            name, (f"{year}-01-06" for year in range(2007, self.end_year))
        )
        self.assertNoOrthodoxHolidayName(name, range(self.start_year, 2007))

    def test_epiphany_orthodox(self):
        name = "Богојавление"
        self.assertNoHolidayName(name)
        self.assertOrthodoxHolidayName(
            name, (f"{year}-01-19" for year in range(2007, self.end_year))
        )
        self.assertNoOrthodoxHolidayName(name, range(self.start_year, 2007))

    def test_good_friday_orthodox(self):
        name = "Велики Петок"
        self.assertNoHolidayName(name)
        self.assertOrthodoxHolidayName(
            name,
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertOrthodoxHolidayName(name, range(2007, self.end_year))
        self.assertNoOrthodoxHolidayName(name, range(self.start_year, 2007))

    def test_assumption_of_mary_orthodox(self):
        name = "Успение на Пресвета Богородица"
        self.assertNoHolidayName(name)
        self.assertOrthodoxHolidayName(
            name, (f"{year}-08-28" for year in range(2007, self.end_year))
        )
        self.assertNoOrthodoxHolidayName(name, range(self.start_year, 2007))

    def test_pentecost_orthodox(self):
        name = "Духовден"
        self.assertNoHolidayName(name)
        self.assertOrthodoxHolidayName(
            name,
            "2020-06-05",
            "2021-06-18",
            "2022-06-10",
            "2023-06-02",
            "2024-06-21",
            "2025-06-06",
        )
        self.assertOrthodoxHolidayName(name, range(2007, self.end_year))
        self.assertNoOrthodoxHolidayName(name, range(self.start_year, 2007))

    def test_international_romani_day(self):
        name = "Меѓународен ден на Ромите"
        self.assertNoHolidayName(name)
        self.assertRomaHolidayName(name, (f"{year}-04-08" for year in range(2007, self.end_year)))
        self.assertNoRomaHolidayName(name, range(self.start_year, 2007))

    def test_saint_savas_day(self):
        name = "Свети Сава"
        self.assertNoHolidayName(name)
        self.assertSerbianHolidayName(
            name, (f"{year}-01-27" for year in range(2008, self.end_year))
        )
        self.assertNoSerbianHolidayName(name, range(self.start_year, 2008))

    def test_turkish_language_teaching_day(self):
        name = "Ден на настава на турски јазик"
        self.assertNoHolidayName(name)
        self.assertTurkishHolidayName(
            name, (f"{year}-12-21" for year in range(2007, self.end_year))
        )
        self.assertNoTurkishHolidayName(name, range(self.start_year, 2007))

    def test_vlachs_national_day(self):
        name = "Национален ден на Власите"
        self.assertNoHolidayName(name)
        self.assertVlachHolidayName(name, (f"{year}-05-23" for year in range(2007, self.end_year)))
        self.assertNoVlachHolidayName(name, range(self.start_year, 2007))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Нова Година"),
            ("2024-01-06", "Бадник"),
            ("2024-01-07", "Божиќ"),
            ("2024-01-08", "Божиќ (неработен ден)"),
            ("2024-01-19", "Богојавление"),
            ("2024-01-27", "Свети Сава"),
            ("2024-04-01", "Велигден"),
            ("2024-04-08", "Меѓународен ден на Ромите"),
            ("2024-04-10", "Рамазан Бајрам"),
            ("2024-04-24", "Ден на изборите"),
            ("2024-05-01", "Ден на трудот"),
            ("2024-05-03", "Велики Петок"),
            ("2024-05-06", "Велигден"),
            ("2024-05-08", "Ден на изборите"),
            ("2024-05-23", "Национален ден на Власите"),
            ("2024-05-24", "Светите Кирил и Методиј - Ден на сесловенските просветители"),
            ("2024-06-16", "Курбан Бајрам"),
            ("2024-06-21", "Духовден"),
            ("2024-08-02", "Ден на Републиката"),
            ("2024-08-28", "Успение на Пресвета Богородица"),
            ("2024-09-08", "Ден на независноста"),
            ("2024-09-09", "Ден на независноста (неработен ден)"),
            ("2024-09-28", "Меѓународен ден на Бошњаците"),
            ("2024-10-11", "Ден на народното востание"),
            ("2024-10-12", "Јом Кипур"),
            ("2024-10-23", "Ден на македонската револуционерна борба"),
            ("2024-11-01", "Сите Светци"),
            ("2024-11-22", "Ден на Албанската азбука"),
            ("2024-12-08", "Свети Климент Охридски"),
            ("2024-12-09", "Свети Климент Охридски (неработен ден)"),
            ("2024-12-21", "Ден на настава на турски јазик"),
            ("2024-12-25", "Божиќ"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-06", "Christmas Eve"),
            ("2024-01-07", "Christmas Day"),
            ("2024-01-08", "Christmas Day (observed)"),
            ("2024-01-19", "Epiphany"),
            ("2024-01-27", "Saint Sava's Day"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-08", "International Romani Day"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-24", "Election Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-03", "Good Friday"),
            ("2024-05-06", "Easter Monday"),
            ("2024-05-08", "Election Day"),
            ("2024-05-23", "Vlachs National Day"),
            ("2024-05-24", "Saints Cyril and Methodius Day"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-21", "Pentecost"),
            ("2024-08-02", "Republic Day"),
            ("2024-08-28", "Dormition of the Mother of God"),
            ("2024-09-08", "Independence Day"),
            ("2024-09-09", "Independence Day (observed)"),
            ("2024-09-28", "International Bosniaks Day"),
            ("2024-10-11", "National Uprising Day"),
            ("2024-10-12", "Yom Kippur"),
            ("2024-10-23", "Macedonian Revolutionary Struggle Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-22", "Albanian Alphabet Day"),
            ("2024-12-08", "Saint Clement of Ohrid Day"),
            ("2024-12-09", "Saint Clement of Ohrid Day (observed)"),
            ("2024-12-21", "Turkish Language Teaching Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-01-06", "Святий вечір"),
            ("2024-01-07", "Різдво Христове"),
            ("2024-01-08", "Різдво Христове (вихідний)"),
            ("2024-01-19", "Богоявлення"),
            ("2024-01-27", "День Святого Сави"),
            ("2024-04-01", "Великодній понеділок"),
            ("2024-04-08", "Міжнародний день ромів"),
            ("2024-04-10", "Рамазан-байрам"),
            ("2024-04-24", "День виборів"),
            ("2024-05-01", "День праці"),
            ("2024-05-03", "Страсна пʼятниця"),
            ("2024-05-06", "Великодній понеділок"),
            ("2024-05-08", "День виборів"),
            ("2024-05-23", "Національний день влахів"),
            ("2024-05-24", "День Святих Кирила та Мефодія, всесловʼянських просвітителів"),
            ("2024-06-16", "Курбан-байрам"),
            ("2024-06-21", "Трійця"),
            ("2024-08-02", "День Республіки"),
            ("2024-08-28", "Успіння Пресвятої Богородиці"),
            ("2024-09-08", "День незалежності"),
            ("2024-09-09", "День незалежності (вихідний)"),
            ("2024-09-28", "Міжнародний день босняків"),
            ("2024-10-11", "День народного повстання"),
            ("2024-10-12", "Йом Кіпур"),
            ("2024-10-23", "День македонської революційної боротьби"),
            ("2024-11-01", "День усіх святих"),
            ("2024-11-22", "День албанського алфавіту"),
            ("2024-12-08", "День Святого Климента Охридського"),
            ("2024-12-09", "День Святого Климента Охридського (вихідний)"),
            ("2024-12-21", "День викладання турецької мови"),
            ("2024-12-25", "Різдво Христове"),
        )
