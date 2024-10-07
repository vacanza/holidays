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

from holidays.countries.philippines import Philippines, PH, PHL
from tests.common import CommonCountryTests


class TestPhilippines(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Philippines, years=range(1988, 2051))

    def test_country_aliases(self):
        self.assertAliases(Philippines, PH, PHL)

    def test_no_holidays(self):
        self.assertNoHolidays(Philippines(years=1987))

    def test_special_holidays(self):
        self.assertHoliday(
            "2008-12-26",
            "2008-12-29",
            "2009-11-02",
            "2009-12-24",
            "2010-12-24",
            "2012-11-02",
            "2013-11-02",
            "2013-12-24",
            "2014-12-24",
            "2014-12-26",
            "2015-01-02",
            "2015-12-24",
            "2016-01-02",
            "2016-10-31",
            "2016-12-24",
            "2017-01-02",
            "2017-10-31",
            "2018-05-14",
            "2018-11-02",
            "2018-12-24",
            "2019-05-13",
            "2019-11-02",
            "2019-12-24",
            "2020-11-02",
            "2020-12-24",
            "2022-05-09",
            "2022-10-31",
            "2023-01-02",
            "2023-10-30",
            "2023-11-02",
            "2023-12-26",
            "2024-02-09",
            "2024-11-02",
            "2024-12-24",
        )

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1988, 2051)))

    def test_chinese_new_year(self):
        name = "Chinese New Year"
        self.assertHolidayName(
            name,
            "2012-01-23",
            "2013-02-10",
            "2014-01-31",
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2024-02-10",
        )
        self.assertNoHolidayName(name, range(1988, 2012), 2023)

    def test_edsa_revolution(self):
        name = "EDSA People Power Revolution Anniversary"
        self.assertHolidayName(
            name,
            "2016-02-25",
            (f"{year}-02-25" for year in range(2018, 2023)),
            "2023-02-24",
            (f"{year}-02-25" for year in range(2025, 2051)),
        )

    def test_maundy_thursday(self):
        name = "Maundy Thursday"
        self.assertHolidayName(
            name,
            "2016-03-24",
            "2017-04-13",
            "2018-03-29",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
        )
        self.assertHolidayName(name, range(1988, 2051))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
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
        self.assertHolidayName(name, range(1988, 2051))

    def test_black_saturday(self):
        name = "Black Saturday"
        self.assertHolidayName(
            name,
            "2016-03-26",
            "2017-04-15",
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
        )
        self.assertHolidayName(name, range(2013, 2051))
        self.assertNoHolidayName(name, range(1988, 2013))

    def test_day_of_valor(self):
        name = "Araw ng Kagitingan (Day of Valor)"
        self.assertHolidayName(
            name,
            (f"{year}-04-09" for year in range(1988, 2008)),
            "2008-04-07",
            "2009-04-06",
            (f"{year}-04-09" for year in range(2010, 2051)),
        )

    def test_labor_day(self):
        self.assertHolidayName("Labor Day", (f"{year}-05-01" for year in range(1988, 2051)))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(
            name,
            (f"{year}-06-12" for year in range(1988, 2007)),
            "2007-06-11",
            "2008-06-09",
            "2009-06-12",
            "2010-06-14",
            (f"{year}-06-12" for year in range(2011, 2051)),
        )

    def test_ninoy_aquino_day(self):
        name = "Ninoy Aquino Day"
        self.assertHolidayName(
            name,
            (f"{year}-08-21" for year in range(1988, 2007)),
            "2007-08-20",
            "2008-08-18",
            "2009-08-21",
            "2010-08-23",
            (f"{year}-08-21" for year in range(2011, 2051)),
        )

    def test_national_heroes_day(self):
        name = "National Heroes Day"
        self.assertHolidayName(
            name,
            "2004-08-29",
            "2005-08-28",
            "2006-08-27",
            "2007-08-27",
            "2008-08-25",
            "2016-08-29",
            "2017-08-28",
            "2018-08-27",
            "2019-08-26",
            "2020-08-31",
            "2021-08-30",
            "2022-08-29",
            "2023-08-28",
            "2024-08-26",
        )
        self.assertHolidayName(name, range(1988, 2051))

    def test_all_saints_day(self):
        self.assertHolidayName("All Saints' Day", (f"{year}-11-01" for year in range(1988, 2051)))

    def test_bonifacio_day(self):
        name = "Bonifacio Day"
        self.assertHolidayName(
            name,
            (f"{year}-11-30" for year in range(1988, 2008)),
            "2008-12-01",
            "2009-11-30",
            "2010-11-29",
            (f"{year}-11-30" for year in range(2011, 2051)),
        )

    def test_immaculate_conception_day(self):
        name = "Feast of the Immaculate Conception of Mary"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(2019, 2051)))
        self.assertNoHolidayName(name, range(1988, 2019))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1988, 2051)))

    def test_rizal_day(self):
        name = "Rizal Day"
        self.assertHolidayName(
            name,
            (f"{year}-12-30" for year in range(1988, 2010)),
            "2010-12-27",
            (f"{year}-12-30" for year in range(2011, 2051)),
        )

    def test_last_day_of_year(self):
        name = "Last Day of the Year"
        self.assertHolidayName(
            name,
            (f"{year}-12-31" for year in range(1988, 2021)),
            (f"{year}-12-31" for year in range(2023, 2051)),
        )
        self.assertNoHolidayName(name, 2021, 2022)

    def test_eid_al_fitr(self):
        name = "Eid'l Fitr (Feast of Ramadhan)"
        self.assertHolidayName(
            name,
            "2016-07-07",
            "2017-06-26",
            "2018-06-15",
            "2019-06-05",
            "2020-05-25",
            "2021-05-13",
            "2022-05-03",
            "2023-04-21",
            "2024-04-10",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(2002, 2051)).issubset(years_found))
        self.assertFalse(set(range(1988, 2002)).intersection(years_found))

    def test_eid_al_adha(self):
        name = "Eid'l Adha (Feast of Sacrifice)"
        self.assertHolidayName(
            name,
            "2016-09-10",
            "2017-09-02",
            "2018-08-21",
            "2019-08-12",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-17",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertTrue(set(range(2010, 2051)).issubset(years_found))
        self.assertFalse(set(range(1988, 2010)).intersection(years_found))

    def test_2023(self):
        self.assertHolidays(
            Philippines(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "Additional special (non-working) day"),
            ("2023-02-24", "EDSA People Power Revolution Anniversary"),
            ("2023-04-06", "Maundy Thursday"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-08", "Black Saturday"),
            ("2023-04-09", "Araw ng Kagitingan (Day of Valor)"),
            ("2023-04-21", "Eid'l Fitr (Feast of Ramadhan)"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-12", "Independence Day"),
            ("2023-06-28", "Eid'l Adha (Feast of Sacrifice)"),
            ("2023-08-21", "Ninoy Aquino Day"),
            ("2023-08-28", "National Heroes Day"),
            ("2023-10-30", "Elections special (non-working) day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-11-02", "Additional special (non-working) day"),
            ("2023-11-30", "Bonifacio Day"),
            ("2023-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Additional special (non-working) day"),
            ("2023-12-30", "Rizal Day"),
            ("2023-12-31", "Last Day of the Year"),
        )

    def test_2024(self):
        self.assertHolidays(
            Philippines(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Additional special (non-working) day"),
            ("2024-02-10", "Chinese New Year"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Black Saturday"),
            ("2024-04-09", "Araw ng Kagitingan (Day of Valor)"),
            ("2024-04-10", "Eid'l Fitr (Feast of Ramadhan)"),
            ("2024-05-01", "Labor Day"),
            ("2024-06-12", "Independence Day"),
            ("2024-06-17", "Eid'l Adha (Feast of Sacrifice)"),
            ("2024-08-21", "Ninoy Aquino Day"),
            ("2024-08-26", "National Heroes Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-02", "Additional special (non-working) day"),
            ("2024-11-30", "Bonifacio Day"),
            ("2024-12-08", "Feast of the Immaculate Conception of Mary"),
            ("2024-12-24", "Additional special (non-working) day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-30", "Rizal Day"),
            ("2024-12-31", "Last Day of the Year"),
        )
