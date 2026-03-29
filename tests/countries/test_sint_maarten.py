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

from holidays.countries.sint_maarten import SintMaarten
from tests.common import CommonCountryTests


class TestSintMaarten(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SintMaarten, years=range(2011, 2050))

    def test_new_years_day(self):
        self.assertHolidayName("Nieuwjaarsdag", (f"{year}-01-01" for year in range(2011, 2050)))

    def test_good_friday(self):
        name = "Goede Vrijdag"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_easter_sunday(self):
        name = "Eerste paasdag"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_easter_monday(self):
        name = "Tweede paasdag"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_kings_day(self):
        name_queen = "Koninginnedag"
        name_king = "Koningsdag"
        self.assertHolidayName(name_queen, (f"{year}-04-30" for year in range(2011, 2014)))
        self.assertNoHolidayName(name_queen, range(2014, 2050))
        self.assertHolidayName(
            name_king,
            "2014-04-26",
            "2015-04-27",
            "2020-04-27",
            "2021-04-27",
            "2022-04-27",
            "2023-04-27",
            "2024-04-27",
            "2025-04-26",
        )
        self.assertNoHoliday(
            "2014-04-27",
            "2025-04-27",
        )
        self.assertHolidayName(name_king, range(2014, 2050))
        self.assertNoHolidayName(name_king, range(2011, 2014))

    def test_carnival_day(self):
        name = "Carnavalsdag"
        self.assertHolidayName(name, (f"{year}-04-29" for year in range(2011, 2014)))
        self.assertHolidayName(
            name,
            "2020-04-30",
            "2021-04-30",
            "2022-04-29",
            "2023-05-02",
            "2024-04-30",
            "2025-04-30",
        )
        self.assertNoHoliday(
            "2016-04-30",
            "2017-04-30",
            "2022-04-30",
            "2023-04-30",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_labor_day(self):
        self.assertHolidayName(
            "Dag van de Arbeid", (f"{year}-05-01" for year in range(2011, 2050))
        )

    def test_ascension_day(self):
        name = "Hemelvaartsdag"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_whit_sunday(self):
        name = "Eerste Pinksterdag"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_emancipation_day(self):
        name = "Dag van de Bevrijding"
        self.assertHolidayName(
            name,
            "2018-07-02",
            "2019-07-01",
            "2020-07-01",
            "2021-07-01",
            "2022-07-01",
            "2023-07-01",
            "2024-07-01",
            "2025-07-01",
        )
        self.assertNoHoliday(
            "2012-08-01",
            "2018-08-01",
        )
        self.assertHolidayName(name, range(2012, 2050))
        self.assertNoHolidayName(name, 2011)

    def test_constitution_day(self):
        name = "Dag van de Constitutie"
        self.assertHolidayName(
            name,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, range(2015, 2050))
        self.assertNoHolidayName(name, range(2011, 2015))

    def test_sint_maarten_day(self):
        self.assertHolidayName("Sint-Maartensdag", (f"{year}-11-11" for year in range(2011, 2050)))

    def test_kingdom_day(self):
        name = "Koninkrijksdag"
        self.assertHolidayName(
            name,
            "2011-12-15",
            "2012-12-15",
            "2013-12-16",
            "2014-12-15",
        )
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_christmas(self):
        self.assertHolidayName("Eerste Kerstdag", (f"{year}-12-25" for year in range(2011, 2050)))
        self.assertHolidayName("Tweede Kerstdag", (f"{year}-12-26" for year in range(2011, 2050)))

    def test_2017(self):
        self.assertHolidaysInYear(
            2017,
            ("2017-01-01", "Nieuwjaarsdag"),
            ("2017-04-14", "Goede Vrijdag"),
            ("2017-04-16", "Eerste paasdag"),
            ("2017-04-17", "Tweede paasdag"),
            ("2017-04-27", "Koningsdag"),
            ("2017-05-02", "Carnavalsdag"),
            ("2017-05-01", "Dag van de Arbeid"),
            ("2017-05-25", "Hemelvaartsdag"),
            ("2017-06-04", "Eerste Pinksterdag"),
            ("2017-07-01", "Dag van de Bevrijding"),
            ("2017-10-09", "Dag van de Constitutie"),
            ("2017-11-11", "Sint-Maartensdag"),
            ("2017-12-25", "Eerste Kerstdag"),
            ("2017-12-26", "Tweede Kerstdag"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nieuwjaarsdag"),
            ("2022-04-15", "Goede Vrijdag"),
            ("2022-04-17", "Eerste paasdag"),
            ("2022-04-18", "Tweede paasdag"),
            ("2022-04-27", "Koningsdag"),
            ("2022-04-29", "Carnavalsdag"),
            ("2022-05-01", "Dag van de Arbeid"),
            ("2022-05-26", "Hemelvaartsdag"),
            ("2022-06-05", "Eerste Pinksterdag"),
            ("2022-07-01", "Dag van de Bevrijding"),
            ("2022-10-10", "Dag van de Constitutie"),
            ("2022-11-11", "Sint-Maartensdag"),
            ("2022-12-25", "Eerste Kerstdag"),
            ("2022-12-26", "Tweede Kerstdag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "King's Day"),
            ("2022-04-29", "Carnival Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-07-01", "Emancipation Day"),
            ("2022-10-10", "Constitution Day"),
            ("2022-11-11", "Sint Maarten Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )
