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

from holidays.countries.latvia import Latvia, LV, LVA
from tests.common import CommonCountryTests


class TestLatvia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Latvia, years=range(1990, 2050))

    def test_country_aliases(self):
        self.assertAliases(Latvia, LV, LVA)

    def test_no_holidays(self):
        self.assertNoHolidays(Latvia(years=1989))

    def test_special_holidays(self):
        self.assertHoliday(
            "2018-07-09",
            "2018-09-24",
            "2023-05-29",
            "2023-07-10",
        )

    def test_new_years(self):
        self.assertHolidayName("Jaunais Gads", (f"{year}-01-01" for year in range(1990, 2050)))

    def test_good_friday(self):
        self.assertHolidayName(
            "Lielā Piektdiena",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_easter(self):
        self.assertHolidayName(
            "Lieldienas",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Otrās Lieldienas",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labor_day(self):
        self.assertHolidayName("Darba svētki", (f"{year}-05-01" for year in range(1990, 2050)))

    def test_restoration_of_independence_day(self):
        name = "Latvijas Republikas Neatkarības atjaunošanas diena"
        self.assertHolidayName(name, (f"{year}-05-04" for year in range(2002, 2050)))
        self.assertNoHoliday(f"{year}-05-04" for year in range(1990, 2002))
        self.assertNoHolidayName(name, range(1990, 2002))

        dt = (
            "2008-05-05",
            "2013-05-06",
            "2014-05-05",
            "2019-05-06",
        )
        self.assertHolidayName(f"{name} (brīvdiena)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_mothers_day(self):
        self.assertHolidayName(
            "Mātes diena",
            "2019-05-12",
            "2020-05-10",
            "2021-05-09",
            "2022-05-08",
            "2023-05-14",
        )

    def test_midsummer_eve(self):
        self.assertHolidayName("Līgo diena", (f"{year}-06-23" for year in range(1990, 2050)))

    def test_midsummer_day(self):
        self.assertHolidayName("Jāņu diena", (f"{year}-06-24" for year in range(1990, 2050)))

    def test_republic_proclamation_day(self):
        name = "Latvijas Republikas proklamēšanas diena"
        self.assertHolidayName(name, (f"{year}-11-18" for year in range(1990, 2050)))

        dt = (
            "2007-11-19",
            "2012-11-19",
            "2017-11-20",
            "2018-11-19",
            "2023-11-20",
        )
        self.assertHolidayName(f"{name} (brīvdiena)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_eve(self):
        name = "Ziemassvētku vakars"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(2007, 2050)))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1990, 2007))
        self.assertNoHolidayName(name, range(1990, 2007))

    def test_christmas_day(self):
        self.assertHolidayName("Ziemassvētki", (f"{year}-12-25" for year in range(1990, 2050)))

    def test_second_christmas_day(self):
        self.assertHolidayName(
            "Otrie Ziemassvētki", (f"{year}-12-26" for year in range(1990, 2050))
        )

    def test_new_years_eve(self):
        self.assertHolidayName("Vecgada vakars", (f"{year}-12-31" for year in range(1990, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jaunais Gads"),
            ("2022-04-15", "Lielā Piektdiena"),
            ("2022-04-17", "Lieldienas"),
            ("2022-04-18", "Otrās Lieldienas"),
            ("2022-05-01", "Darba svētki"),
            ("2022-05-04", "Latvijas Republikas Neatkarības atjaunošanas diena"),
            ("2022-05-08", "Mātes diena"),
            ("2022-06-23", "Līgo diena"),
            ("2022-06-24", "Jāņu diena"),
            ("2022-11-18", "Latvijas Republikas proklamēšanas diena"),
            ("2022-12-24", "Ziemassvētku vakars"),
            ("2022-12-25", "Ziemassvētki"),
            ("2022-12-26", "Otrie Ziemassvētki"),
            ("2022-12-31", "Vecgada vakars"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-04", "Restoration of Independence Day"),
            ("2022-05-08", "Mother's Day"),
            ("2022-06-23", "Midsummer Eve"),
            ("2022-06-24", "Midsummer Day"),
            ("2022-11-18", "Republic of Latvia Proclamation Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-04", "День відновлення незалежности Латвійської Республіки"),
            ("2022-05-08", "День матері"),
            ("2022-06-23", "Ліго"),
            ("2022-06-24", "Янів день"),
            ("2022-11-18", "День проголошення Латвійської Республіки"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
            ("2022-12-31", "Переддень Нового року"),
        )
