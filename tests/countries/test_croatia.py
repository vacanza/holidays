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

from holidays.countries.croatia import Croatia, HR, HRV
from tests.common import TestCase


class TestCroatia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Croatia, years=range(1990, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Croatia, HR, HRV)

    def test_new_years_day(self):
        self.assertHolidayName("Nova Godina", (f"{year}-01-01" for year in range(1990, 2050)))

    def test_epiphany(self):
        name = "Bogojavljenje ili Sveta tri kralja"
        self.assertHolidayName(
            name, (f"{year}-01-06" for year in set(range(1990, 2050)).difference({2002}))
        )
        self.assertNoHoliday("2002-01-06")
        self.assertNoHolidayName(name, 2002)

    def test_easter(self):
        name = "Uskrs"
        self.assertHolidayName(
            name,
            "2009-04-12",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )
        self.assertNoHolidayName(name, range(1990, 2009))

    def test_easter_monday(self):
        self.assertHolidayName(
            "Uskrsni ponedjeljak",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_corpus_cristi(self):
        name = "Tijelovo"
        self.assertHolidayName(
            name,
            "2002-05-30",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
        )
        self.assertNoHolidayName(name, range(1990, 2002))

    def test_labor_day(self):
        self.assertHolidayName(
            "Međunarodni praznik rada", (f"{year}-05-01" for year in range(1990, 2050))
        )

    def test_statehood_day(self):
        name = "Dan državnosti"
        self.assertHolidayName(name, (f"{year}-05-30" for year in range(1996, 2002)))
        self.assertHolidayName(name, (f"{year}-06-25" for year in range(2002, 2020)))
        self.assertHolidayName(name, (f"{year}-05-30" for year in range(2020, 2050)))
        self.assertNoHolidayName(name, range(1990, 1996))

    def test_antifascist_struggle_day(self):
        self.assertHolidayName(
            "Dan antifašističke borbe", (f"{year}-06-22" for year in range(1990, 2050))
        )

    def test_victory_and_homeland_thanksgiving_day(self):
        name_1 = "Dan pobjede i domovinske zahvalnosti"
        name_2 = "Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja"
        self.assertHolidayName(name_1, (f"{year}-08-05" for year in range(1990, 2008)))
        self.assertHolidayName(name_2, (f"{year}-08-05" for year in range(2008, 2050)))
        self.assertNoHolidayName(name_1, range(2008, 2050))
        self.assertNoHolidayName(name_2, range(1990, 2008))

    def test_assumption_of_mary_day(self):
        self.assertHolidayName("Velika Gospa", (f"{year}-08-15" for year in range(1990, 2050)))

    def test_independence_day(self):
        name = "Dan neovisnosti"
        self.assertHolidayName(name, (f"{year}-10-08" for year in range(2002, 2020)))
        self.assertNoHoliday(f"{year}-10-08" for year in range(1990, 2002))
        self.assertNoHoliday(f"{year}-10-08" for year in range(2020, 2050))
        self.assertNoHolidayName(name, range(1990, 2002), range(2020, 2050))

    def test_all_saints_day(self):
        self.assertHolidayName("Svi sveti", (f"{year}-11-01" for year in range(1990, 2050)))

    def test_memorial_day(self):
        name = "Dan sjećanja"
        self.assertHolidayName(name, (f"{year}-11-18" for year in range(2020, 2050)))
        self.assertNoHoliday(f"{year}-11-18" for year in range(1990, 2020))
        self.assertNoHolidayName(name, range(1990, 2020))

    def test_christmas_day(self):
        self.assertHolidayName("Božić", (f"{year}-12-25" for year in range(1990, 2050)))

    def test_st_stephens_day(self):
        self.assertHolidayName("Sveti Stjepan", (f"{year}-12-26" for year in range(1990, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nova Godina"),
            ("2022-01-06", "Bogojavljenje ili Sveta tri kralja"),
            ("2022-04-17", "Uskrs"),
            ("2022-04-18", "Uskrsni ponedjeljak"),
            ("2022-05-01", "Međunarodni praznik rada"),
            ("2022-05-30", "Dan državnosti"),
            ("2022-06-16", "Tijelovo"),
            ("2022-06-22", "Dan antifašističke borbe"),
            ("2022-08-05", "Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja"),
            ("2022-08-15", "Velika Gospa"),
            ("2022-11-01", "Svi sveti"),
            ("2022-11-18", "Dan sjećanja"),
            ("2022-12-25", "Božić"),
            ("2022-12-26", "Sveti Stjepan"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-04-17", "Easter"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-30", "Statehood Day"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-06-22", "Anti-Fascist Struggle Day"),
            ("2022-08-05", "Victory and Homeland Thanksgiving Day and Croatian Veterans Day"),
            ("2022-08-15", "Assumption of Mary"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-18", "Memorial Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "St. Stephen's Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "Міжнародний день трудящих"),
            ("2022-05-30", "День державності"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-06-22", "День антифашистської боротьби"),
            ("2022-08-05", "День перемоги і подяки вітчизні та День хорватських захисників"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-18", "День памʼяті"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День Святого Стефана"),
        )
