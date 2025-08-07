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

from holidays.countries.eritrea import Eritrea, ER, ERI
from tests.common import CommonCountryTests


class TestEritrea(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1994, 2050)
        super().setUpClass(Eritrea, years=years)
        cls.no_estimated_holidays = Eritrea(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Eritrea, ER, ERI)

    def test_new_years_day(self):
        self.assertHolidayName("New Year", (f"{year}-01-01" for year in range(1994, 2050)))

    def test_no_holidays(self):
        self.assertNoHolidays(Eritrea(years=1993))

    def test_leddet(self):
        self.assertHolidayName("Leddet", (f"{year}-01-07" for year in range(1994, 2050)))

    def test_timket(self):
        self.assertHolidayName("Timket", (f"{year}-01-19" for year in range(1994, 2050)))

    def test_tensae(self):
        name = "Tensae"
        dt = (
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1994, 2050))

    def test_festival_of_mariam_dearit(self):
        self.assertHolidayName(
            "Festival of Mariam Dearit", (f"{year}-05-29" for year in range(1994, 2050))
        )

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        dt = (
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1994, 2050))

    def test_mariam_debre_sina(self):
        self.assertHolidayName(
            "Mariam Debre Sina", (f"{year}-06-28" for year in range(2007, 2050))
        )

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        dt = (
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-06",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1994, 2050))

    def test_debre_bizen_abune_libanos(self):
        name = "Debre Bizen Abune Libanos"
        self.assertHolidayName(name, (f"{year}-08-11" for year in range(2007, 2050)))
        self.assertNoHolidayName(name, range(1994, 2007))

    def test_keddus_yohannes(self):
        self.assertHolidayName("Keddus Yohannes", (f"{year}-09-11" for year in range(1994, 2050)))

    def test_meskel(self):
        self.assertHolidayName("Meskel", (f"{year}-09-27" for year in range(1994, 2050)))

    def test_muharram(self):
        name = "Muharram"
        dt = (
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(f"{name} (estimated)", self.no_estimated_holidays, dt)
        self.assertHolidayName(
            f"{name} (estimated)", self.no_estimated_holidays, range(1994, 2050)
        )

    def test_mawlid_an_nabi(self):
        name = "Mawlid an-Nabi"

        dt = (
            "2020-10-29",
            "2021-10-20",
            "2022-10-08",
            "2023-09-28",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1994, 2050))

    def test_christmas(self):
        self.assertHolidayName("Christmas", (f"{year}-12-25" for year in range(1994, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2020-01-01", "New Year"),
            ("2020-01-07", "Leddet"),
            ("2020-01-19", "Timket"),
            ("2020-04-12", "Tensae"),
            ("2020-05-24", "Eid al-Fitr"),
            ("2020-05-29", "Festival of Mariam Dearit"),
            ("2020-06-28", "Mariam Debre Sina"),
            ("2020-07-31", "Eid al-Adha"),
            ("2020-08-11", "Debre Bizen Abune Libanos"),
            ("2020-08-20", "Muharram (estimated)"),
            ("2020-09-11", "Keddus Yohannes"),
            ("2020-09-27", "Meskel"),
            ("2020-10-29", "Mawlid an-Nabi"),
            ("2020-12-25", "Christmas"),
        )
