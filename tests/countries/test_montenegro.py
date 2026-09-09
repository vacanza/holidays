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

from holidays.constants import CATHOLIC, HEBREW, ISLAMIC, ORTHODOX, WORKDAY
from holidays.countries.montenegro import Montenegro
from tests.common import CommonCountryTests


class TestMontenegro(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2007, 2050)
        super().setUpClass(Montenegro, years=years, years_non_observed=years)
        cls.catholic_holidays = Montenegro(categories=CATHOLIC, years=years)
        cls.hebrew_holidays = Montenegro(categories=HEBREW, years=years)
        cls.islamic_holidays = Montenegro(categories=ISLAMIC, years=years)
        cls.orthodox_holidays = Montenegro(categories=ORTHODOX, years=years)

    def test_new_years_day(self):
        name = "Nova godina"
        self.assertHolidayName(
            name,
            (f"{year}-01-01" for year in range(2007, 2050)),
            (f"{year}-01-02" for year in range(2007, 2050)),
        )
        dt = (
            "2011-01-03",
            "2012-01-03",
            "2017-01-03",
            "2022-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (neradni dan)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_labor_day(self):
        name = "Praznik rada"
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in range(2007, 2050)),
            (f"{year}-05-02" for year in range(2007, 2050)),
        )
        dt = (
            "2010-05-03",
            "2011-05-03",
            "2016-05-03",
            "2021-05-03",
            "2022-05-03",
        )
        self.assertHolidayName(f"{name} (neradni dan)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Dan nezavisnosti"
        self.assertHolidayName(
            name,
            (f"{year}-05-21" for year in range(2007, 2050)),
            (f"{year}-05-22" for year in range(2007, 2050)),
        )
        dt = (
            "2011-05-23",
            "2016-05-23",
            "2017-05-23",
            "2022-05-23",
            "2023-05-23",
        )
        self.assertHolidayName(f"{name} (neradni dan)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_statehood_day(self):
        name = "Dan državnosti"
        self.assertHolidayName(
            name,
            (f"{year}-07-13" for year in range(2007, 2050)),
            (f"{year}-07-14" for year in range(2007, 2050)),
        )
        dt = (
            "2008-07-15",
            "2013-07-15",
            "2014-07-15",
            "2019-07-15",
            "2024-07-15",
        )
        self.assertHolidayName(f"{name} (neradni dan)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_njegos_day(self):
        name = "Njegošev dan"
        self.assertHolidayName(name, (f"{year}-11-13" for year in range(2022, 2050)))
        self.assertNoHolidayName(name, range(2007, 2022))
        dt = (
            "2022-11-14",
            "2033-11-14",
        )
        self.assertHolidayName(f"{name} (neradni dan)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday_catholic(self):
        name = "Veliki petak"
        self.assertNoHolidayName(name)
        dt = (
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
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(2007, 2050))

    def test_easter_monday_catholic(self):
        name = "Uskrs"
        self.assertNoHolidayName(name)
        dt = (
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(2007, 2050))

    def test_all_saints_day_catholic(self):
        name = "Svi Sveti"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.catholic_holidays, (f"{year}-11-01" for year in range(2007, 2050))
        )

    def test_christmas_eve_catholic(self):
        name = "Badnji dan"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.catholic_holidays, (f"{year}-12-24" for year in range(2007, 2050))
        )

    def test_christmas_day_catholic(self):
        name = "Božić"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.catholic_holidays,
            (f"{year}-12-25" for year in range(2007, 2050)),
            (f"{year}-12-26" for year in range(2007, 2050)),
        )

    def test_pesach(self):
        name = "Pasha"
        self.assertNoHolidayName(name)
        dt = (
            "2015-04-05",
            "2015-04-04",
            "2016-04-23",
            "2016-04-24",
            "2017-04-11",
            "2024-04-24",
            "2017-04-12",
            "2018-03-31",
            "2018-04-01",
            "2019-04-20",
            "2019-04-21",
            "2020-04-09",
            "2020-04-10",
            "2021-03-28",
            "2021-03-29",
            "2022-04-16",
            "2022-04-17",
            "2023-04-06",
            "2023-04-07",
            "2024-04-23",
        )
        self.assertHolidayName(name, self.hebrew_holidays, dt)
        self.assertHolidayName(name, self.hebrew_holidays, range(2007, 2050))

    def test_yom_kippur(self):
        name = "Jom Kipur"
        self.assertNoHolidayName(name)
        dt = (
            "2015-09-23",
            "2015-09-24",
            "2016-10-12",
            "2016-10-13",
            "2017-09-30",
            "2017-10-01",
            "2018-09-19",
            "2018-09-20",
            "2019-10-09",
            "2019-10-10",
            "2020-09-28",
            "2020-09-29",
            "2021-09-16",
            "2021-09-17",
            "2022-10-05",
            "2022-10-06",
            "2023-09-25",
            "2023-09-26",
            "2024-10-12",
            "2024-10-13",
        )
        self.assertHolidayName(name, self.hebrew_holidays, dt)
        self.assertHolidayName(name, self.hebrew_holidays, range(2007, 2050))

    def test_eid_al_fitr(self):
        name = "Ramazanski bajram"
        self.assertNoHolidayName(name)
        dt = (
            "2015-07-18",
            "2015-07-19",
            "2015-07-20",
            "2016-07-07",
            "2016-07-08",
            "2016-07-09",
            "2017-06-26",
            "2017-06-27",
            "2017-06-28",
            "2018-06-15",
            "2018-06-16",
            "2018-06-17",
            "2019-06-04",
            "2019-06-05",
            "2019-06-06",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
        )
        self.assertHolidayName(name, self.islamic_holidays, dt)

    def test_eid_al_adha(self):
        name = "Kurbanski bajram"
        self.assertNoHolidayName(name)
        dt = (
            "2015-09-24",
            "2015-09-25",
            "2015-09-26",
            "2016-09-13",
            "2016-09-14",
            "2016-09-15",
            "2017-09-02",
            "2017-09-03",
            "2017-09-04",
            "2018-08-22",
            "2018-08-23",
            "2018-08-24",
            "2019-08-11",
            "2019-08-12",
            "2019-08-13",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
        )
        self.assertHolidayName(name, self.islamic_holidays, dt)

    def test_good_friday_orthodox(self):
        name = "Veliki petak"
        self.assertNoHolidayName(name)
        dt = (
            "2015-04-10",
            "2016-04-29",
            "2017-04-14",
            "2018-04-06",
            "2019-04-26",
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(2007, 2050))

    def test_easter_monday_orthodox(self):
        name = "Uskrs"
        self.assertNoHolidayName(name)
        dt = (
            "2015-04-13",
            "2016-05-02",
            "2017-04-17",
            "2018-04-09",
            "2019-04-29",
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
            "2024-05-06",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(2007, 2050))

    def test_christmas_eve_orthodox(self):
        name = "Badnji dan"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.orthodox_holidays, (f"{year}-01-06" for year in range(2007, 2050))
        )

    def test_christmas_day_orthodox(self):
        name = "Božić"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.orthodox_holidays,
            (f"{year}-01-07" for year in range(2007, 2050)),
            (f"{year}-01-08" for year in range(2007, 2050)),
        )

    def test_ecological_state_day(self):
        name = "Dan Ekološke države"
        self.assertNoHolidayName(name)
        workday_holidays = Montenegro(categories=WORKDAY, years=range(2007, 2050))
        self.assertHolidayName(
            name, workday_holidays, (f"{year}-09-20" for year in range(2022, 2050))
        )
        self.assertNoHolidayName(name, workday_holidays, range(2007, 2022))

    def test_2022(self):
        self.assertHolidays(
            Montenegro(categories=self.holidays.supported_categories, years=2022),
            ("2022-01-01", "Nova godina"),
            ("2022-01-02", "Nova godina"),
            ("2022-01-03", "Nova godina (neradni dan)"),
            ("2022-01-06", "Badnji dan"),
            ("2022-01-07", "Božić"),
            ("2022-01-08", "Božić"),
            ("2022-04-15", "Veliki petak"),
            ("2022-04-16", "Pasha"),
            ("2022-04-17", "Pasha"),
            ("2022-04-18", "Uskrs"),
            ("2022-04-22", "Veliki petak"),
            ("2022-04-25", "Uskrs"),
            ("2022-05-01", "Praznik rada"),
            ("2022-05-02", "Praznik rada; Ramazanski bajram"),
            ("2022-05-03", "Praznik rada (neradni dan); Ramazanski bajram"),
            ("2022-05-04", "Ramazanski bajram"),
            ("2022-05-21", "Dan nezavisnosti"),
            ("2022-05-22", "Dan nezavisnosti"),
            ("2022-05-23", "Dan nezavisnosti (neradni dan)"),
            ("2022-07-09", "Kurbanski bajram"),
            ("2022-07-10", "Kurbanski bajram"),
            ("2022-07-11", "Kurbanski bajram"),
            ("2022-07-13", "Dan državnosti"),
            ("2022-07-14", "Dan državnosti"),
            ("2022-09-20", "Dan Ekološke države"),
            ("2022-10-05", "Jom Kipur"),
            ("2022-10-06", "Jom Kipur"),
            ("2022-11-01", "Svi Sveti"),
            ("2022-11-13", "Njegošev dan"),
            ("2022-11-14", "Njegošev dan (neradni dan)"),
            ("2022-12-24", "Badnji dan"),
            ("2022-12-25", "Božić"),
            ("2022-12-26", "Božić"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Nova godina"),
            ("2023-01-02", "Nova godina"),
            ("2023-01-03", "Nova godina (neradni dan)"),
            ("2023-01-06", "Badnji dan"),
            ("2023-01-07", "Božić"),
            ("2023-01-08", "Božić"),
            ("2023-04-06", "Pasha"),
            ("2023-04-07", "Pasha; Veliki petak"),
            ("2023-04-10", "Uskrs"),
            ("2023-04-14", "Veliki petak"),
            ("2023-04-17", "Uskrs"),
            ("2023-04-21", "Ramazanski bajram"),
            ("2023-04-22", "Ramazanski bajram"),
            ("2023-04-23", "Ramazanski bajram"),
            ("2023-05-01", "Praznik rada"),
            ("2023-05-02", "Praznik rada"),
            ("2023-05-21", "Dan nezavisnosti"),
            ("2023-05-22", "Dan nezavisnosti"),
            ("2023-05-23", "Dan nezavisnosti (neradni dan)"),
            ("2023-06-28", "Kurbanski bajram"),
            ("2023-06-29", "Kurbanski bajram"),
            ("2023-06-30", "Kurbanski bajram"),
            ("2023-07-13", "Dan državnosti"),
            ("2023-07-14", "Dan državnosti"),
            ("2023-09-20", "Dan Ekološke države"),
            ("2023-09-25", "Jom Kipur"),
            ("2023-09-26", "Jom Kipur"),
            ("2023-11-01", "Svi Sveti"),
            ("2023-11-13", "Njegošev dan"),
            ("2023-12-24", "Badnji dan"),
            ("2023-12-25", "Božić"),
            ("2023-12-26", "Božić"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day"),
            ("2023-01-03", "New Year's Day (observed)"),
            ("2023-01-06", "Christmas Eve"),
            ("2023-01-07", "Christmas"),
            ("2023-01-08", "Christmas"),
            ("2023-04-06", "Pesach"),
            ("2023-04-07", "Good Friday; Pesach"),
            ("2023-04-10", "Easter"),
            ("2023-04-14", "Good Friday"),
            ("2023-04-17", "Easter"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-02", "Labor Day"),
            ("2023-05-21", "Independence Day"),
            ("2023-05-22", "Independence Day"),
            ("2023-05-23", "Independence Day (observed)"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-13", "Statehood Day"),
            ("2023-07-14", "Statehood Day"),
            ("2023-09-20", "Ecological State Day"),
            ("2023-09-25", "Yom Kippur"),
            ("2023-09-26", "Yom Kippur"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-11-13", "Njegos Day"),
            ("2023-12-24", "Christmas Eve"),
            ("2023-12-25", "Christmas"),
            ("2023-12-26", "Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-01-02", "Новий рік"),
            ("2023-01-03", "Новий рік (вихідний)"),
            ("2023-01-06", "Святий вечір"),
            ("2023-01-07", "Різдво Христове"),
            ("2023-01-08", "Різдво Христове"),
            ("2023-04-06", "Песах"),
            ("2023-04-07", "Песах; Страсна пʼятниця"),
            ("2023-04-10", "Великдень"),
            ("2023-04-14", "Страсна пʼятниця"),
            ("2023-04-17", "Великдень"),
            ("2023-04-21", "Рамазан-байрам"),
            ("2023-04-22", "Рамазан-байрам"),
            ("2023-04-23", "Рамазан-байрам"),
            ("2023-05-01", "День праці"),
            ("2023-05-02", "День праці"),
            ("2023-05-21", "День незалежності"),
            ("2023-05-22", "День незалежності"),
            ("2023-05-23", "День незалежності (вихідний)"),
            ("2023-06-28", "Курбан-байрам"),
            ("2023-06-29", "Курбан-байрам"),
            ("2023-06-30", "Курбан-байрам"),
            ("2023-07-13", "День державності"),
            ("2023-07-14", "День державності"),
            ("2023-09-20", "День екологічної держави"),
            ("2023-09-25", "Йом Кіпур"),
            ("2023-09-26", "Йом Кіпур"),
            ("2023-11-01", "День усіх святих"),
            ("2023-11-13", "День Нєґоша"),
            ("2023-12-24", "Святий вечір"),
            ("2023-12-25", "Різдво Христове"),
            ("2023-12-26", "Різдво Христове"),
        )
