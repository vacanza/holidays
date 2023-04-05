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

from holidays.countries.bosnia_and_herzegovina import BosniaAndHerzegovina, BA
from holidays.countries.bosnia_and_herzegovina import BIH
from tests.common import TestCase


class TestBosniaAndHerzegovina(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass(BosniaAndHerzegovina)

    def setUp(self):
        super().setUp()

        self.bd_holidays = BosniaAndHerzegovina(subdiv="BD")
        self.rs_holidays = BosniaAndHerzegovina(subdiv="RS")
        self.fbih_holidays = BosniaAndHerzegovina(subdiv="FBiH")

    def test_country_aliases(self):
        self.assertCountryAliases(BosniaAndHerzegovina, BA, BIH)

    def test_new_years(self):
        self.assertHolidaysName(
            "Nova Godina", (f"{year}-01-01" for year in range(2000, 2030))
        )
        self.assertHolidaysName(
            "Drugi dan Nove Godine",
            (f"{year}-01-02" for year in range(2000, 2030)),
        )

        name = "Treći dan Nove Godine"
        dt = (
            "2006-01-03",
            "2012-01-03",
            "2017-01-03",
            "2023-01-03",
        )
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.bd_holidays, dt)
        self.assertNoHoliday(dt)
        self.assertNoNonObservedHoliday(
            BosniaAndHerzegovina(subdiv="FBiH", observed=False), dt
        )
        self.assertNoNonObservedHoliday(
            BosniaAndHerzegovina(subdiv="BD", observed=False), dt
        )

    def test_orthodox_christmas_eve(self):
        name = "Pravoslavno Badnje veče"
        dt = (f"{year}-01-06" for year in range(2000, 2030))
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)

    def test_orthodox_christmas(self):
        self.assertHolidaysName(
            "Božić (Божић)", (f"{year}-01-07" for year in range(2000, 2030))
        )

    def test_orthodox_new_year(self):
        self.assertHolidaysName(
            "Pravoslavna Nova Godina",
            self.rs_holidays,
            (f"{year}-01-14" for year in range(2000, 2030)),
        )

    def test_independence_day(self):
        self.assertHolidaysName(
            "Dan nezavisnosti",
            self.fbih_holidays,
            (f"{year}-03-01" for year in range(2000, 2030)),
        )

    def test_establishment_bd_day(self):
        self.assertHolidaysName(
            "Dan uspostavljanja Brčko distrikta",
            self.bd_holidays,
            (f"{year}-03-08" for year in range(2000, 2030)),
        )

    def test_catholic_easter(self):
        name = "Veliki Petak (Katolički)"
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
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)

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
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)

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
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)
        self.assertHolidaysName(name, self.bd_holidays, dt)
        self.assertHolidaysName(name, dt)

    def test_orthodox_easter(self):
        name = "Veliki Petak (Pravoslavni)"
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
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)
        self.assertHolidaysName(name, self.bd_holidays, dt)
        self.assertHolidaysName(name, dt)

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
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)

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
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)

    def test_labor_day(self):
        self.assertHolidaysName(
            "Dan rada",
            (f"{year}-05-01" for year in range(2000, 2030)),
        )
        name = "Drugi dan Dana rada"
        self.assertHolidaysName(
            name,
            (f"{year}-05-02" for year in range(2000, 2022)),
        )
        self.assertIn(name, self.holidays_non_observed.get("2022-05-02"))
        self.assertHolidaysName(
            name,
            (f"{year}-05-02" for year in range(2023, 2030)),
        )

        name = "Treći dan Dana rada"
        dt = (
            "2011-05-03",
            "2016-05-03",
            "2022-05-03",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoNonObservedHoliday(dt)

    def test_victory_day(self):
        name = "Dan pobjede nad fašizmom"
        dt = (f"{year}-05-09" for year in range(2000, 2030))
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)

    def test_eid_al_fitr(self):
        dt = (
            "2010-09-10",
            "2015-07-17",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2023-04-21",
        )
        self.assertHolidaysName("Ramazanski Bajram", dt)

        name = "Drugi Dan Ramazanski Bajram"
        dt = (
            "2010-09-11",
            "2015-07-18",
            "2018-06-16",
            "2019-06-05",
            "2020-05-25",
            "2021-05-14",
            "2023-04-22",
        )
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)

    def test_eid_ul_adha(self):
        dt = (
            "2006-01-10",
            "2006-12-31",
            "2010-11-16",
            "2015-09-23",
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
        )
        self.assertHolidaysName("Kurban Bajram", dt)

        name = "Drugi Dan Kurban Bajram"
        dt = (
            "2010-11-17",
            "2015-09-24",
            "2018-08-22",
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
        )
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)
        self.assertIn(name, self.fbih_holidays.get("2007-01-01"))
        self.assertIn(name, self.rs_holidays.get("2007-01-01"))

    def test_dayton_agreement_day(self):
        self.assertHolidaysName(
            "Dan uspostave Opšteg okvirnog sporazuma za mir u "
            "Bosni i Hercegovini",
            self.rs_holidays,
            (f"{year}-11-21" for year in range(2000, 2030)),
        )

    def test_statehood_day(self):
        self.assertHolidaysName(
            "Dan državnosti",
            self.fbih_holidays,
            (f"{year}-11-25" for year in range(2004, 2030)),
        )

    def test_catholic_christmas(self):
        for year in range(2010, 2025):
            self.assertEqual(
                self.holidays_non_observed.get(f"{year}-12-25"),
                "Božić (Katolički)",
            )
        name = "Badnji dan (Katolički)"
        dt = (f"{year}-12-24" for year in range(2000, 2030))
        self.assertHolidaysName(name, self.fbih_holidays, dt)
        self.assertHolidaysName(name, self.rs_holidays, dt)

        self.assertHolidaysName(
            "Božić (Katolički)",
            (f"{year}-12-25" for year in range(2000, 2030)),
        )
