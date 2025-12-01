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

from holidays.countries.suriname import Suriname
from tests.common import CommonCountryTests


class TestSuriname(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1972, 2050)
        super().setUpClass(Suriname, years=years)
        cls.no_estimated_holidays = Suriname(years=years, islamic_show_estimated=False)

    def test_new_years_day(self):
        self.assertHolidayName("Nieuwjaarsdag", (f"{year}-01-01" for year in range(1972, 2050)))

    def test_day_of_liberation_and_renewal(self):
        name = "Dag van Bevrijding en Vernieuwing"
        self.assertHolidayName(
            name, (f"{year}-02-25" for year in (*range(1981, 1993), *range(2012, 2021)))
        )
        self.assertNoHolidayName(name, range(1993, 2012), range(2021, 2050))

    def test_holi(self):
        name = "Holi-Phagwa"
        self.assertHolidayName(
            name,
            "2019-03-21",
            "2020-03-09",
            "2021-03-28",
            "2022-03-18",
            "2023-03-07",
            "2024-03-25",
            "2025-03-14",
        )
        self.assertHolidayName(name, range(2015, 2031))

    def test_good_friday(self):
        name = "Goede Vrijdag"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1972, 2050))

    def test_easter_monday(self):
        name = "Tweede Paasdag"
        self.assertHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1972, 2050))

    def test_queens_birthday(self):
        name = "Verjaardag van H.M. de Koningin"
        self.assertHolidayName(name, (f"{year}-04-30" for year in range(1972, 1976)))
        self.assertNoHolidayName(name, range(1976, 2050))

    def test_labor_day(self):
        self.assertHolidayName(
            "Dag van de Arbeid", (f"{year}-05-01" for year in range(1972, 2050))
        )

    def test_day_of_freedoms(self):
        name_1 = "Dag der Vrijheden"
        name_2 = "Keti Koti Dey"
        self.assertHolidayName(
            name_1, (f"{year}-07-01" for year in (*range(1972, 2008), *range(2025, 2050)))
        )
        self.assertHolidayName(name_2, (f"{year}-07-01" for year in range(2008, 2025)))
        self.assertNoHolidayName(name_1, range(2008, 2025))
        self.assertNoHolidayName(name_2, range(1972, 2008), range(2025, 2050))

    def test_indigenous_people_day(self):
        name = "Dag der Inheemsen"
        self.assertHolidayName(name, (f"{year}-08-09" for year in range(2007, 2050)))
        self.assertNoHolidayName(name, range(1972, 2007))

    def test_day_of_the_maroons(self):
        name = "Dag der Marrons"
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1972, 2012))

    def test_diwali(self):
        name = "Divali"
        self.assertHolidayName(
            name,
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self.assertHolidayName(name, range(2012, 2050))
        self.assertNoHolidayName(name, range(1972, 2012))

    def test_republic_day(self):
        name_old = "Dag van de Republiek"
        name_new = "Onafhankelijkheidsdag"
        self.assertHolidayName(name_old, (f"{year}-11-25" for year in range(1976, 2008)))
        self.assertHolidayName(name_new, (f"{year}-11-25" for year in range(2008, 2050)))
        self.assertNoHolidayName(name_old, range(1972, 1976))
        self.assertNoHolidayName(name_new, range(1972, 2008))

    def test_christmas_day(self):
        self.assertHolidayName("Eerste Kerstdag", (f"{year}-12-25" for year in range(1972, 2050)))

    def test_second_day_of_christmas(self):
        self.assertHolidayName("Tweede Kerstdag", (f"{year}-12-26" for year in range(1972, 2050)))

    def test_eid_al_fitr(self):
        name = "Ied-Ul-Fitre"
        self.assertHolidayName(
            name,
            "2019-06-05",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1972, 2050))

    def test_eid_al_adha(self):
        name = "Ied-Ul-Adha"
        self.assertHolidayName(
            name,
            "2019-08-12",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-29",
            "2024-06-16",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2012, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(1972, 2012))

    def test_chinese_new_year(self):
        name = "Chinees Nieuwjaar"
        self.assertHolidayName(
            name,
            "2022-02-01",
            "2023-01-22",
            "2024-02-10",
            "2025-01-29",
        )
        self.assertHolidayName(name, range(2022, 2050))
        self.assertNoHolidayName(name, range(1972, 2022))

    def test_2024(self):
        self.assertHolidays(
            Suriname(years=2024),
            ("2024-01-01", "Nieuwjaarsdag"),
            ("2024-02-10", "Chinees Nieuwjaar"),
            ("2024-03-25", "Holi-Phagwa"),
            ("2024-03-29", "Goede Vrijdag"),
            ("2024-04-01", "Tweede Paasdag"),
            ("2024-04-10", "Ied-Ul-Fitre"),
            ("2024-05-01", "Dag van de Arbeid"),
            ("2024-06-16", "Ied-Ul-Adha"),
            ("2024-07-01", "Keti Koti Dey"),
            ("2024-08-09", "Dag der Inheemsen"),
            ("2024-10-10", "Dag der Marrons"),
            ("2024-10-31", "Divali"),
            ("2024-11-25", "Onafhankelijkheidsdag"),
            ("2024-12-25", "Eerste Kerstdag"),
            ("2024-12-26", "Tweede Kerstdag"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Nieuwjaarsdag"),
            ("2025-01-29", "Chinees Nieuwjaar"),
            ("2025-03-14", "Holi-Phagwa"),
            ("2025-03-31", "Ied-Ul-Fitre"),
            ("2025-04-18", "Goede Vrijdag"),
            ("2025-04-21", "Tweede Paasdag"),
            ("2025-05-01", "Dag van de Arbeid"),
            ("2025-06-07", "Ied-Ul-Adha"),
            ("2025-07-01", "Dag der Vrijheden"),
            ("2025-08-09", "Dag der Inheemsen"),
            ("2025-10-10", "Dag der Marrons"),
            ("2025-10-20", "Divali"),
            ("2025-11-25", "Onafhankelijkheidsdag"),
            ("2025-12-25", "Eerste Kerstdag"),
            ("2025-12-26", "Tweede Kerstdag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-29", "Chinese New Year"),
            ("2025-03-14", "Holi"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-07-01", "Day of Freedoms"),
            ("2025-08-09", "Indigenous People Day"),
            ("2025-10-10", "Day of the Maroons"),
            ("2025-10-20", "Diwali"),
            ("2025-11-25", "Independence Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Second Day of Christmas"),
        )
