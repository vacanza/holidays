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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

import warnings

from holidays.countries.bosnia_and_herzegovina import BosniaAndHerzegovina, BA, BIH
from tests.common import TestCase


class TestBosniaAndHerzegovina(TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2000, 2030)
        super().setUpClass(BosniaAndHerzegovina, years=years)
        cls.bih_holidays = BosniaAndHerzegovina(subdiv="BIH", years=years)
        cls.brc_holidays = BosniaAndHerzegovina(subdiv="BRC", years=years)
        cls.srp_holidays = BosniaAndHerzegovina(subdiv="SRP", years=years)
        cls.bih_holidays_non_obs = BosniaAndHerzegovina(subdiv="BIH", observed=False, years=years)
        cls.brc_holidays_non_obs = BosniaAndHerzegovina(subdiv="BRC", observed=False, years=years)
        cls.srp_holidays_non_obs = BosniaAndHerzegovina(subdiv="SRP", observed=False, years=years)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_country_aliases(self):
        self.assertCountryAliases(BosniaAndHerzegovina, BA, BIH)

    def test_new_years(self):
        name = "Nova godina"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2000, 2030)))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(2000, 2030)))

        dt = (
            "2006-01-03",
            "2012-01-03",
            "2017-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.bih_holidays, dt)
        self.assertNoNonObservedHoliday(self.bih_holidays_non_obs, dt)

        dt = (
            "2000-01-03",
            "2005-01-03",
            "2006-01-03",
            "2011-01-03",
            "2012-01-03",
            "2017-01-03",
            "2022-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.brc_holidays, dt)
        self.assertNoNonObservedHoliday(self.brc_holidays_non_obs, dt)

        dt = (
            "2000-01-03",
            "2005-01-03",
            "2011-01-03",
            "2022-01-03",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.srp_holidays, dt)
        self.assertNoNonObservedHoliday(self.srp_holidays_non_obs, dt)

    def test_orthodox_christmas_eve(self):
        name = "Badnji dan (Pravoslavni)"
        self.assertHolidayName(
            name, self.bih_holidays, (f"{year}-01-06" for year in range(2000, 2030))
        )
        self.assertHolidayName(
            name, self.srp_holidays, (f"{year}-01-06" for year in range(2000, 2030))
        )
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name)

    def test_orthodox_christmas(self):
        name = "Božić (Pravoslavni)"
        self.assertHolidayName(name, (f"{year}-01-07" for year in range(2000, 2030)))

        dt = (
            "2001-01-08",
            "2007-01-08",
            "2018-01-08",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.brc_holidays, dt)
        self.assertNoNonObservedHoliday(self.brc_holidays_non_obs, dt)
        self.assertNoHoliday(dt)

    def test_orthodox_new_year(self):
        name = "Pravoslavna Nova godina"
        self.assertHolidayName(
            name, self.srp_holidays, (f"{year}-01-14" for year in range(2000, 2030))
        )
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name, self.bih_holidays)
        self.assertNoHolidayName(name)

    def test_independence_day(self):
        name = "Dan nezavisnosti"
        self.assertHolidayName(
            name, self.bih_holidays, (f"{year}-03-01" for year in range(2000, 2030))
        )
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name, self.srp_holidays)
        self.assertNoHolidayName(name)

    def test_establishment_bd_day(self):
        name = "Dan uspostavljanja Brčko distrikta"
        self.assertHolidayName(
            name, self.brc_holidays, (f"{year}-03-08" for year in range(2000, 2030))
        )
        self.assertNoHolidayName(name, self.bih_holidays)
        self.assertNoHolidayName(name, self.srp_holidays)
        self.assertNoHolidayName(name)

        dt = (
            "2009-03-09",
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.brc_holidays, dt)
        self.assertNoNonObservedHoliday(self.brc_holidays_non_obs, dt)
        self.assertNoHoliday(dt)

    def test_catholic_easter(self):
        name = "Veliki petak (Katolički)"
        dt = (
            "2012-04-06",
            "2015-04-03",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name)

        name = "Uskrs (Katolički)"
        dt = (
            "2012-04-08",
            "2015-04-05",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name)

        name = "Uskrsni ponedjeljak (Katolički)"
        dt = (
            "2012-04-09",
            "2015-04-06",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)
        self.assertHolidayName(name, self.brc_holidays, dt)
        self.assertHolidayName(name, dt)

    def test_orthodox_easter(self):
        name = "Veliki petak (Pravoslavni)"
        dt = (
            "2012-04-13",
            "2015-04-10",
            "2018-04-06",
            "2019-04-26",
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
        )
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)
        self.assertHolidayName(name, self.brc_holidays, dt)
        self.assertHolidayName(name, dt)

        name = "Vaskrs (Pravoslavni)"
        dt = (
            "2012-04-15",
            "2015-04-12",
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2022-04-24",
            "2023-04-16",
        )
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)

        name = "Uskrsni ponedjeljak (Pravoslavni)"
        dt = (
            "2012-04-16",
            "2015-04-13",
            "2018-04-09",
            "2019-04-29",
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
        )
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name)

    def test_labor_day(self):
        name = "Međunarodni praznik rada"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2000, 2030)))
        self.assertHolidayName(name, (f"{year}-05-02" for year in range(2000, 2030)))

        dt = (
            "2011-05-03",
            "2022-05-03",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.bih_holidays, dt)
        self.assertNoNonObservedHolidayName(f"{name} (preneseno)", self.bih_holidays_non_obs, dt)

        dt = (
            "2004-05-03",
            "2005-05-03",
            "2010-05-03",
            "2011-05-03",
            "2016-05-03",
            "2021-05-03",
            "2022-05-03",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.brc_holidays, dt)
        self.assertNoNonObservedHoliday(self.brc_holidays_non_obs, dt)

        dt = (
            "2004-05-03",
            "2010-05-03",
            "2021-05-03",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.srp_holidays, dt)
        self.assertNoNonObservedHolidayName(f"{name} (preneseno)", self.srp_holidays_non_obs, dt)

    def test_victory_day(self):
        name = "Dan pobjede nad fašizmom"
        self.assertHolidayName(
            name, self.bih_holidays, (f"{year}-05-09" for year in range(2000, 2030))
        )
        self.assertHolidayName(
            name, self.srp_holidays, (f"{year}-05-09" for year in range(2000, 2030))
        )
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name)

    def test_eid_al_fitr(self):
        name = "Ramazanski Bajram"
        dt = (
            "2010-09-10",
            "2015-07-18",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.brc_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)

        dt = (
            "2010-09-11",
            "2015-07-19",
            "2018-06-16",
            "2019-06-05",
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
        )
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)
        self.assertNoHolidayName(name, self.brc_holidays, dt)
        self.assertNoHolidayName(name, dt)

    def test_eid_al_adha(self):
        name = "Kurban Bajram"
        dt = (
            "2006-01-10",
            "2006-12-31",
            "2010-11-17",
            "2015-09-24",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.brc_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)

        dt = (
            "2007-01-01",
            "2010-11-18",
            "2015-09-25",
            "2018-08-23",
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
        )
        self.assertHolidayName(name, self.bih_holidays, dt)
        self.assertHolidayName(name, self.srp_holidays, dt)
        self.assertNoHolidayName(name, self.brc_holidays, dt)
        self.assertNoHolidayName(name, dt)

    def test_dayton_agreement_day(self):
        name = "Dan uspostave Opšteg okvirnog sporazuma za mir u Bosni i Hercegovini"
        self.assertHolidayName(
            name, self.srp_holidays, (f"{year}-11-21" for year in range(2000, 2030))
        )
        self.assertNoHolidayName(name, self.bih_holidays)
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name)

    def test_statehood_day(self):
        name = "Dan državnosti"
        self.assertHolidayName(
            name, self.bih_holidays, (f"{year}-11-25" for year in range(2004, 2030))
        )
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name, self.srp_holidays)
        self.assertNoHolidayName(name)

    def test_catholic_christmas(self):
        name = "Božić (Katolički)"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2000, 2030)))

        dt = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
        )
        self.assertHolidayName(f"{name} (preneseno)", self.brc_holidays, dt)
        self.assertNoNonObservedHoliday(self.brc_holidays_non_obs, dt)
        self.assertNoHoliday(dt)

        name = "Badnji dan (Katolički)"
        self.assertHolidayName(
            name, self.bih_holidays, (f"{year}-12-24" for year in range(2000, 2030))
        )
        self.assertHolidayName(
            name, self.srp_holidays, (f"{year}-12-24" for year in range(2000, 2030))
        )
        self.assertNoHolidayName(name, self.brc_holidays)
        self.assertNoHolidayName(name)

    def test_deprecated(self):
        for subdiv1, subdiv2 in (
            ("BD", "BRC"),
            ("FBiH", "BIH"),
            ("RS", "SRP"),
        ):
            self.assertEqual(
                BosniaAndHerzegovina(subdiv=subdiv1, years=2022).keys(),
                BosniaAndHerzegovina(subdiv=subdiv2, years=2022).keys(),
            )

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

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
            ("2021-05-03", "Međunarodni praznik rada (preneseno)"),
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
                "Međunarodni praznik rada (preneseno); Uskrsni ponedjeljak (Pravoslavni)",
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
            ("2022-01-07", "Božić (Pravoslavni)"),
            ("2022-04-18", "Uskrsni ponedjeljak (Katolički)"),
            ("2022-04-22", "Veliki petak (Pravoslavni)"),
            ("2022-05-01", "Međunarodni praznik rada"),
            ("2022-05-02", "Međunarodni praznik rada; Ramazanski Bajram"),
            ("2022-07-09", "Kurban Bajram"),
            ("2022-12-25", "Božić (Katolički)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Orthodox Christmas"),
            ("2022-04-18", "Catholic Easter Monday"),
            ("2022-04-22", "Orthodox Good Friday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr; Labor Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-12-25", "Catholic Christmas"),
        )

    def test_l10n_sr(self):
        self.assertLocalizedHolidays(
            "sr",
            ("2022-01-01", "Нова година"),
            ("2022-01-02", "Нова година"),
            ("2022-01-07", "Божић (Православни)"),
            ("2022-04-18", "Ускршњи понедељак (Католички)"),
            ("2022-04-22", "Велики петак (Православни)"),
            ("2022-05-01", "Међународни празник рада"),
            ("2022-05-02", "Међународни празник рада; Рамазански Бајрам"),
            ("2022-07-09", "Курбан Бајрам"),
            ("2022-12-25", "Божић (Католички)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-02", "Новий рік"),
            ("2022-01-07", "Різдво Христове (православне)"),
            ("2022-04-18", "Великодній понеділок (католицький)"),
            ("2022-04-22", "Страсна пʼятниця (православна)"),
            ("2022-05-01", "Міжнародний день праці"),
            ("2022-05-02", "Міжнародний день праці; Рамазан-байрам"),
            ("2022-07-09", "Курбан-байрам"),
            ("2022-12-25", "Різдво Христове (католицьке)"),
        )
