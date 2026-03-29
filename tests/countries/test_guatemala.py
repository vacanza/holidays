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

from holidays.countries.guatemala import Guatemala
from tests.common import CommonCountryTests


class TestGuatemala(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Guatemala)

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))

    def test_maundy_thursday(self):
        name = "Jueves Santo"
        self.assertHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_holy_saturday(self):
        name = "Sábado Santo"
        self.assertHolidayName(
            name,
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Día del Trabajo"
        self.assertNonObservedHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        self.assertHolidayName(name, "2019-04-29")

    def test_army_day(self):
        name = "Día del Ejército"
        self.assertNonObservedHolidayName(name, (f"{year}-06-30" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2020-06-29",
            "2021-06-28",
            "2022-07-04",
            "2023-07-03",
            "2024-07-01",
            "2025-06-30",
        )

    def test_assumption_day(self):
        self.assertHolidayName("Día de la Asunción", (f"{year}-08-15" for year in self.full_range))

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-09-15" for year in self.full_range)
        )

    def test_revolution_day(self):
        name = "Día de la Revolución"
        self.assertNonObservedHolidayName(name, (f"{year}-10-20" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2018-10-22",
            "2019-10-21",
        )

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Día de Todos los Santos", (f"{year}-11-01" for year in self.full_range)
        )

    def test_christmas_day(self):
        self.assertHolidayName("Día de Navidad", (f"{year}-12-25" for year in self.full_range))

    def test_2016(self):
        # https://calendariohispanohablante.com/2016/calendario-guatemala-2016.html
        self.assertHolidayDates(
            Guatemala(years=2016),
            "2016-01-01",
            "2016-03-24",
            "2016-03-25",
            "2016-03-26",
            "2016-05-01",
            "2016-06-30",
            "2016-08-15",
            "2016-09-15",
            "2016-10-20",
            "2016-11-01",
            "2016-12-25",
        )

    def test_2017(self):
        # https://calendariohispanohablante.com/2017/calendario-guatemala-2017.html
        self.assertHolidayDates(
            Guatemala(years=2017),
            "2017-01-01",
            "2017-04-13",
            "2017-04-14",
            "2017-04-15",
            "2017-05-01",
            "2017-06-30",
            "2017-08-15",
            "2017-09-15",
            "2017-10-20",
            "2017-11-01",
            "2017-12-25",
        )

    def test_2018(self):
        # https://calendariohispanohablante.com/2018/calendario-guatemala-2018.html
        self.assertHolidayDates(
            Guatemala(years=2018),
            "2018-01-01",
            "2018-03-29",
            "2018-03-30",
            "2018-03-31",
            "2018-05-01",
            "2018-06-30",
            "2018-08-15",
            "2018-09-15",
            "2018-10-22",
            "2018-11-01",
            "2018-12-25",
        )

    def test_2019(self):
        # https://calendariohispanohablante.com/2019/calendario-guatemala-2019.html
        self.assertHolidayDates(
            Guatemala(years=2019),
            "2019-01-01",
            "2019-04-18",
            "2019-04-19",
            "2019-04-20",
            "2019-04-29",
            "2019-07-01",
            "2019-08-15",
            "2019-09-15",
            "2019-10-21",
            "2019-11-01",
            "2019-12-25",
        )

    def test_2020(self):
        # https://calendariohispanohablante.com/2020/calendario-guatemala-2020.html
        self.assertHolidayDates(
            Guatemala(years=2020),
            "2020-01-01",
            "2020-04-09",
            "2020-04-10",
            "2020-04-11",
            "2020-05-01",
            "2020-06-29",
            "2020-08-15",
            "2020-09-15",
            "2020-10-20",
            "2020-11-01",
            "2020-12-25",
        )

    def test_2021(self):
        # https://calendariohispanohablante.com/2021/calendario-guatemala-2021.html
        self.assertHolidayDates(
            Guatemala(years=2021),
            "2021-01-01",
            "2021-04-01",
            "2021-04-02",
            "2021-04-03",
            "2021-05-01",
            "2021-06-28",
            "2021-08-15",
            "2021-09-15",
            "2021-10-20",
            "2021-11-01",
            "2021-12-25",
        )

    def test_2022(self):
        # https://publicholidays.la/guatemala/es/2022-dates/
        self.assertHolidayDates(
            Guatemala(years=2022),
            "2022-01-01",
            "2022-04-14",
            "2022-04-15",
            "2022-04-16",
            "2022-05-01",
            "2022-07-04",
            "2022-08-15",
            "2022-09-15",
            "2022-10-20",
            "2022-11-01",
            "2022-12-25",
        )

    def test_2023(self):
        # https://publicholidays.la/guatemala/es/2023-dates/
        self.assertHolidayDates(
            Guatemala(years=2023),
            "2023-01-01",
            "2023-04-06",
            "2023-04-07",
            "2023-04-08",
            "2023-05-01",
            "2023-07-03",
            "2023-08-15",
            "2023-09-15",
            "2023-10-20",
            "2023-11-01",
            "2023-12-25",
        )

    def test_2024(self):
        # https://publicholidays.la/guatemala/es/2024-dates/
        self.assertHolidayDates(
            Guatemala(years=2024),
            "2024-01-01",
            "2024-03-28",
            "2024-03-29",
            "2024-03-30",
            "2024-05-01",
            "2024-07-01",
            "2024-08-15",
            "2024-09-15",
            "2024-10-20",
            "2024-11-01",
            "2024-12-25",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Año Nuevo"),
            ("2024-03-28", "Jueves Santo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-03-30", "Sábado Santo"),
            ("2024-05-01", "Día del Trabajo"),
            ("2024-07-01", "Día del Ejército"),
            ("2024-08-15", "Día de la Asunción"),
            ("2024-09-15", "Día de la Independencia"),
            ("2024-10-20", "Día de la Revolución"),
            ("2024-11-01", "Día de Todos los Santos"),
            ("2024-12-25", "Día de Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Holy Saturday"),
            ("2024-05-01", "Labor Day"),
            ("2024-07-01", "Army Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-09-15", "Independence Day"),
            ("2024-10-20", "Revolution Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-12-25", "Christmas Day"),
        )
