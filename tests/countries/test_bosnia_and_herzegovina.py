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

from holidays.countries.bosnia_and_herzegovina import BosniaAndHerzegovina, BA, BIH
from tests.common import CommonCountryTests


class TestBosniaAndHerzegovina(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(2000, 2050)
        super().setUpClass(BosniaAndHerzegovina, years=cls.full_range)

    def test_country_aliases(self):
        self.assertAliases(BosniaAndHerzegovina, BA, BIH)

    def test_new_years_day(self):
        name = "Nova godina"
        name_observed = f"{name} (slobodan dan)"
        self.assertHolidayName(
            name,
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in self.full_range),
        )

        obs_dates = {
            "BIH": (
                "2006-01-03",
                "2012-01-03",
                "2017-01-03",
                "2023-01-03",
            ),
            "BRC": (
                "2000-01-03",
                "2005-01-03",
                "2006-01-03",
                "2011-01-03",
                "2012-01-03",
                "2017-01-03",
                "2022-01-03",
                "2023-01-03",
            ),
            "SRP": (
                "2000-01-03",
                "2005-01-03",
                "2011-01-03",
                "2022-01-03",
            ),
        }
        for subdiv, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name_observed, holidays, obs_dates[subdiv])
            self.assertNoNonObservedHoliday(
                self.subdiv_holidays_non_observed[subdiv], obs_dates[subdiv]
            )

    def test_orthodox_christmas_eve(self):
        name = "Badnji dan (Pravoslavni)"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-06" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_orthodox_christmas(self):
        name = "Božić (Pravoslavni)"
        self.assertHolidayName(name, (f"{year}-01-07" for year in self.full_range))

        name_observed = f"{name} (slobodan dan)"
        obs_dt = (
            "2001-01-08",
            "2007-01-08",
            "2018-01-08",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BRC":
                self.assertHolidayName(name_observed, holidays, obs_dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], obs_dt)
            else:
                self.assertNoHoliday(holidays, obs_dt)
        self.assertNoHoliday(obs_dt)

    def test_orthodox_new_year(self):
        name = "Pravoslavna Nova godina"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SRP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-14" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_independence_day(self):
        name = "Dan nezavisnosti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BIH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_establishment_bd_day(self):
        name = "Dan uspostavljanja Brčko distrikta"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BRC":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-08" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

        name_observed = f"{name} (slobodan dan)"
        obs_dt = (
            "2009-03-09",
            "2015-03-09",
            "2020-03-09",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BRC":
                self.assertHolidayName(name_observed, holidays, obs_dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], obs_dt)
            else:
                self.assertNoHoliday(holidays, obs_dt)
        self.assertNoHoliday(obs_dt)

    def test_catholic_easter(self):
        name = "Veliki petak (Katolički)"
        self.assertNoHolidayName(name)
        dt = (
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(name, holidays, dt)
            else:
                self.assertNoHolidayName(name, holidays)

        name = "Uskrs (Katolički)"
        self.assertNoHolidayName(name)
        dt = (
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(name, holidays, dt)
            else:
                self.assertNoHolidayName(name, holidays)

        name = "Uskrsni ponedjeljak (Katolički)"
        dt = (
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )
        self.assertHolidayName(name, dt)
        for subdiv, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name, holidays, dt)

    def test_orthodox_easter(self):
        name = "Veliki petak (Pravoslavni)"
        dt = (
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
        )
        self.assertHolidayName(name, dt)
        for subdiv, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name, holidays, dt)

        name = "Vaskrs (Pravoslavni)"
        self.assertNoHolidayName(name)
        dt = (
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(name, holidays, dt)
            else:
                self.assertNoHolidayName(name, holidays)

        name = "Uskrsni ponedjeljak (Pravoslavni)"
        self.assertNoHolidayName(name)
        dt = (
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(name, holidays, dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_labor_day(self):
        name = "Međunarodni praznik rada"
        name_observed = f"{name} (slobodan dan)"
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in self.full_range),
            (f"{year}-05-02" for year in self.full_range),
        )

        obs_dates = {
            "BIH": (
                "2011-05-03",
                "2022-05-03",
            ),
            "BRC": (
                "2004-05-03",
                "2005-05-03",
                "2010-05-03",
                "2011-05-03",
                "2016-05-03",
                "2021-05-03",
                "2022-05-03",
            ),
            "SRP": (
                "2004-05-03",
                "2010-05-03",
                "2021-05-03",
            ),
        }
        for subdiv, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name_observed, holidays, obs_dates[subdiv])

    def test_victory_day(self):
        name = "Dan pobjede nad fašizmom"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-09" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_eid_al_fitr(self):
        name = "Ramazanski Bajram"
        dt_1 = (
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
        )
        dt_2 = (
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
        )
        self.assertHolidayName(name, dt_1)
        self.assertNoHolidayName(name, dt_2)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(name, holidays, dt_1, dt_2)
            else:
                self.assertHolidayName(name, holidays, dt_1)
                self.assertNoHolidayName(name, holidays, dt_2)

    def test_eid_al_adha(self):
        name = "Kurban Bajram"
        dt_1 = (
            "2006-01-10",
            "2006-12-31",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
        )
        dt_2 = (
            "2007-01-01",
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
        )
        self.assertHolidayName(name, dt_1)
        self.assertNoHolidayName(name, dt_2)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(name, holidays, dt_1, dt_2)
            else:
                self.assertHolidayName(name, holidays, dt_1)
                self.assertNoHolidayName(name, holidays, dt_2)

    def test_dayton_agreement_day(self):
        name = "Dan uspostave Opšteg okvirnog sporazuma za mir u Bosni i Hercegovini"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SRP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-21" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_statehood_day(self):
        name = "Dan državnosti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BIH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-25" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_catholic_christmas_eve(self):
        name = "Badnji dan (Katolički)"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv != "BRC":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-24" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_catholic_christmas(self):
        name = "Božić (Katolički)"
        name_observed = f"{name} (slobodan dan)"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))

        obs_dt = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BRC":
                self.assertHolidayName(name_observed, holidays, obs_dt)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], obs_dt)
            else:
                self.assertNoHoliday(holidays, obs_dt)
        self.assertNoHoliday(obs_dt)

    def test_2021(self):
        self.assertHolidays(
            BosniaAndHerzegovina(years=2021),
            ("2021-01-01", "Nova godina"),
            ("2021-01-02", "Nova godina"),
            ("2021-01-07", "Božić (Pravoslavni)"),
            ("2021-04-05", "Uskrsni ponedjeljak (Katolički)"),
            ("2021-04-30", "Veliki petak (Pravoslavni)"),
            ("2021-05-01", "Međunarodni praznik rada"),
            ("2021-05-02", "Međunarodni praznik rada"),
            ("2021-05-13", "Ramazanski Bajram"),
            ("2021-07-20", "Kurban Bajram"),
            ("2021-12-25", "Božić (Katolički)"),
        )

        self.assertHolidays(
            BosniaAndHerzegovina(subdiv="BIH", years=2021),
            ("2021-01-01", "Nova godina"),
            ("2021-01-02", "Nova godina"),
            ("2021-01-06", "Badnji dan (Pravoslavni)"),
            ("2021-01-07", "Božić (Pravoslavni)"),
            ("2021-03-01", "Dan nezavisnosti"),
            ("2021-04-02", "Veliki petak (Katolički)"),
            ("2021-04-04", "Uskrs (Katolički)"),
            ("2021-04-05", "Uskrsni ponedjeljak (Katolički)"),
            ("2021-04-30", "Veliki petak (Pravoslavni)"),
            ("2021-05-01", "Međunarodni praznik rada"),
            ("2021-05-02", "Međunarodni praznik rada; Vaskrs (Pravoslavni)"),
            ("2021-05-03", "Uskrsni ponedjeljak (Pravoslavni)"),
            ("2021-05-09", "Dan pobjede nad fašizmom"),
            ("2021-05-13", "Ramazanski Bajram"),
            ("2021-05-14", "Ramazanski Bajram"),
            ("2021-07-20", "Kurban Bajram"),
            ("2021-07-21", "Kurban Bajram"),
            ("2021-11-25", "Dan državnosti"),
            ("2021-12-24", "Badnji dan (Katolički)"),
            ("2021-12-25", "Božić (Katolički)"),
        )

        self.assertHolidays(
            BosniaAndHerzegovina(subdiv="BRC", years=2021),
            ("2021-01-01", "Nova godina"),
            ("2021-01-02", "Nova godina"),
            ("2021-01-07", "Božić (Pravoslavni)"),
            ("2021-03-08", "Dan uspostavljanja Brčko distrikta"),
            ("2021-04-05", "Uskrsni ponedjeljak (Katolički)"),
            ("2021-04-30", "Veliki petak (Pravoslavni)"),
            ("2021-05-01", "Međunarodni praznik rada"),
            ("2021-05-02", "Međunarodni praznik rada"),
            ("2021-05-03", "Međunarodni praznik rada (slobodan dan)"),
            ("2021-05-13", "Ramazanski Bajram"),
            ("2021-07-20", "Kurban Bajram"),
            ("2021-12-25", "Božić (Katolički)"),
        )

        self.assertHolidays(
            BosniaAndHerzegovina(subdiv="SRP", years=2021),
            ("2021-01-01", "Nova godina"),
            ("2021-01-02", "Nova godina"),
            ("2021-01-06", "Badnji dan (Pravoslavni)"),
            ("2021-01-07", "Božić (Pravoslavni)"),
            ("2021-01-14", "Pravoslavna Nova godina"),
            ("2021-04-02", "Veliki petak (Katolički)"),
            ("2021-04-04", "Uskrs (Katolički)"),
            ("2021-04-05", "Uskrsni ponedjeljak (Katolički)"),
            ("2021-04-30", "Veliki petak (Pravoslavni)"),
            ("2021-05-01", "Međunarodni praznik rada"),
            ("2021-05-02", "Međunarodni praznik rada; Vaskrs (Pravoslavni)"),
            (
                "2021-05-03",
                "Međunarodni praznik rada (slobodan dan); Uskrsni ponedjeljak (Pravoslavni)",
            ),
            ("2021-05-09", "Dan pobjede nad fašizmom"),
            ("2021-05-13", "Ramazanski Bajram"),
            ("2021-05-14", "Ramazanski Bajram"),
            ("2021-07-20", "Kurban Bajram"),
            ("2021-07-21", "Kurban Bajram"),
            ("2021-11-21", "Dan uspostave Opšteg okvirnog sporazuma za mir u Bosni i Hercegovini"),
            ("2021-12-24", "Badnji dan (Katolički)"),
            ("2021-12-25", "Božić (Katolički)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nova godina"),
            ("2022-01-02", "Nova godina"),
            ("2022-01-03", "Nova godina (slobodan dan)"),
            ("2022-01-06", "Badnji dan (Pravoslavni)"),
            ("2022-01-07", "Božić (Pravoslavni)"),
            ("2022-01-14", "Pravoslavna Nova godina"),
            ("2022-03-01", "Dan nezavisnosti"),
            ("2022-03-08", "Dan uspostavljanja Brčko distrikta"),
            ("2022-04-15", "Veliki petak (Katolički)"),
            ("2022-04-17", "Uskrs (Katolički)"),
            ("2022-04-18", "Uskrsni ponedjeljak (Katolički)"),
            ("2022-04-22", "Veliki petak (Pravoslavni)"),
            ("2022-04-24", "Vaskrs (Pravoslavni)"),
            ("2022-04-25", "Uskrsni ponedjeljak (Pravoslavni)"),
            ("2022-05-01", "Međunarodni praznik rada"),
            ("2022-05-02", "Međunarodni praznik rada; Ramazanski Bajram"),
            ("2022-05-03", "Međunarodni praznik rada (slobodan dan); Ramazanski Bajram"),
            ("2022-05-09", "Dan pobjede nad fašizmom"),
            ("2022-07-09", "Kurban Bajram"),
            ("2022-07-10", "Kurban Bajram"),
            ("2022-11-21", "Dan uspostave Opšteg okvirnog sporazuma za mir u Bosni i Hercegovini"),
            ("2022-11-25", "Dan državnosti"),
            ("2022-12-24", "Badnji dan (Katolički)"),
            ("2022-12-25", "Božić (Katolički)"),
            ("2022-12-26", "Božić (Katolički) (slobodan dan)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-06", "Orthodox Christmas Eve"),
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-01-14", "Orthodox New Year"),
            ("2022-03-01", "Independence Day"),
            ("2022-03-08", "Day of establishment of Brčko District"),
            ("2022-04-15", "Catholic Good Friday"),
            ("2022-04-17", "Catholic Easter Sunday"),
            ("2022-04-18", "Catholic Easter Monday"),
            ("2022-04-22", "Orthodox Good Friday"),
            ("2022-04-24", "Orthodox Easter Sunday"),
            ("2022-04-25", "Orthodox Easter Monday"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "Eid al-Fitr; International Labor Day"),
            ("2022-05-03", "Eid al-Fitr; International Labor Day (observed)"),
            ("2022-05-09", "Victory Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-11-21", "Dayton Agreement Day"),
            ("2022-11-25", "Statehood Day"),
            ("2022-12-24", "Catholic Christmas Eve"),
            ("2022-12-25", "Catholic Christmas Day"),
            ("2022-12-26", "Catholic Christmas Day (observed)"),
        )

    def test_l10n_sr(self):
        self.assertLocalizedHolidays(
            "sr",
            ("2022-01-01", "Нова година"),
            ("2022-01-02", "Нова година"),
            ("2022-01-03", "Нова година (слободан дан)"),
            ("2022-01-06", "Бадњи дан (Православни)"),
            ("2022-01-07", "Божић (Православни)"),
            ("2022-01-14", "Православна Нова година"),
            ("2022-03-01", "Дан независности"),
            ("2022-03-08", "Дан успостављања Брчко дистрикта"),
            ("2022-04-15", "Велики петак (Католички)"),
            ("2022-04-17", "Ускрс (Католички)"),
            ("2022-04-18", "Ускршњи понедељак (Католички)"),
            ("2022-04-22", "Велики петак (Православни)"),
            ("2022-04-24", "Васкрс (Православни)"),
            ("2022-04-25", "Ускршњи понедељак (Православни)"),
            ("2022-05-01", "Међународни празник рада"),
            ("2022-05-02", "Међународни празник рада; Рамазански Бајрам"),
            ("2022-05-03", "Међународни празник рада (слободан дан); Рамазански Бајрам"),
            ("2022-05-09", "Дан побједе над фашизмом"),
            ("2022-07-09", "Курбан Бајрам"),
            ("2022-07-10", "Курбан Бајрам"),
            ("2022-11-21", "Дан успоставе Општег оквирног споразума за мир у Босни и Херцеговини"),
            ("2022-11-25", "Дан државности"),
            ("2022-12-24", "Бадњи дан (Католички)"),
            ("2022-12-25", "Божић (Католички)"),
            ("2022-12-26", "Божић (Католички) (слободан дан)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-02", "Новий рік"),
            ("2022-01-03", "Новий рік (вихідний)"),
            ("2022-01-06", "Святий вечір (православний)"),
            ("2022-01-07", "Різдво Христове (православне)"),
            ("2022-01-14", "Православний Новий рік"),
            ("2022-03-01", "День незалежності"),
            ("2022-03-08", "День заснування округу Брчко"),
            ("2022-04-15", "Страсна пʼятниця (католицька)"),
            ("2022-04-17", "Великдень (католицький)"),
            ("2022-04-18", "Великодній понеділок (католицький)"),
            ("2022-04-22", "Страсна пʼятниця (православна)"),
            ("2022-04-24", "Великдень (православний)"),
            ("2022-04-25", "Великодній понеділок (православний)"),
            ("2022-05-01", "Міжнародний день праці"),
            ("2022-05-02", "Міжнародний день праці; Рамазан-байрам"),
            ("2022-05-03", "Міжнародний день праці (вихідний); Рамазан-байрам"),
            ("2022-05-09", "День перемоги над фашизмом"),
            ("2022-07-09", "Курбан-байрам"),
            ("2022-07-10", "Курбан-байрам"),
            (
                "2022-11-21",
                "День укладання Загальної рамкової угоди про мир у Боснії та Герцеговині",
            ),
            ("2022-11-25", "День державності"),
            ("2022-12-24", "Святий вечір (католицький)"),
            ("2022-12-25", "Різдво Христове (католицьке)"),
            ("2022-12-26", "Різдво Христове (католицьке) (вихідний)"),
        )
