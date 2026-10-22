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

from holidays.constants import OPTIONAL, PUBLIC, SCHOOL
from holidays.countries.netherlands import Netherlands
from tests.common import CommonCountryTests


class TestNetherlands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            Netherlands, with_subdiv_categories=True, years_all_subdivs=range(2013, 2031)
        )

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Netherlands(categories=OPTIONAL, years=range(self.start_year, 1982)))

        self.assertNoHolidays(Netherlands(categories=SCHOOL, years=self.full_range))
        for subdiv in Netherlands.subdivisions:
            self.assertNoHolidays(
                Netherlands(subdiv=subdiv, categories=SCHOOL, years=range(self.start_year, 2013))
            )

    def test_new_years_day(self):
        self.assertHolidayName("Nieuwjaarsdag", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Goede vrijdag"
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
        self.assertHolidayName(name, self.full_range)

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
        self.assertHolidayName(name, self.full_range)

    def test_queens_day(self):
        name = "Koninginnedag"
        self.assertHolidayName(
            name,
            "1967-05-01",
            "1972-05-01",
            "1978-05-01",
            "1989-04-29",
            "1995-04-29",
            "2000-04-29",
            "2006-04-29",
            "2013-04-30",
        )
        self.assertHolidayName(name, range(self.start_year, 2014))
        self.assertNoHolidayName(
            name,
            "1967-04-30",
            "1972-04-30",
            "1978-04-30",
            "1995-04-30",
            "1989-04-30",
            "2000-04-30",
            "2006-04-30",
        )
        self.assertNoHolidayName(name, range(2014, self.end_year))

    def test_king_day(self):
        name = "Koningsdag"
        self.assertHolidayName(
            name,
            "2016-04-27",
            "2017-04-27",
            "2018-04-27",
            "2019-04-27",
            "2020-04-27",
            "2021-04-27",
            "2022-04-27",
            "2023-04-27",
            "2024-04-27",
            "2025-04-26",
            "2031-04-26",
            "2036-04-26",
        )
        self.assertHolidayName(name, range(2014, self.end_year))
        self.assertNoHolidayName(
            name,
            "2014-04-27",
            "2025-04-27",
            "2031-04-27",
            "2036-04-27",
        )
        self.assertNoHolidayName(name, range(self.start_year, 2014))

    def test_liberation_day(self):
        name = "Bevrijdingsdag"
        # PUBLIC.
        self.assertHolidayName(
            name, (f"{year}-05-05" for year in self.full_range if year % 5 == 0)
        )
        self.assertNoHolidayName(
            name, (f"{year}-05-05" for year in self.full_range if year % 5 != 0)
        )
        # OPTIONAL.
        self.assertOptionalHolidayName(
            name, (f"{year}-05-05" for year in range(1982, self.end_year))
        )
        self.assertNoOptionalHolidayName(name, range(self.start_year, 1982))

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
        self.assertHolidayName(name, self.full_range)

    def test_whit_sunday(self):
        name = "Eerste pinksterdag"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Tweede pinksterdag"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        self.assertHolidayName("Eerste kerstdag", (f"{year}-12-25" for year in self.full_range))

    def test_second_day_of_christmas(self):
        self.assertHolidayName("Tweede kerstdag", (f"{year}-12-26" for year in self.full_range))

    def test_school_autumn_break(self):
        name = "Herfstvakantie"
        self.assertNoHolidayName(name)

        self.assertSubdivNoordSchoolHolidayName(
            name,
            "2013-10-19",
            "2013-10-27",
            "2017-10-21",
            "2017-10-29",
            "2022-10-15",
            "2022-10-23",
            "2026-10-10",
            "2026-10-18",
            "2029-10-20",
            "2029-10-28",
        )
        self.assertNoSubdivNoordSchoolHoliday(
            "2013-10-18",
            "2013-10-28",
            "2017-10-20",
            "2017-10-30",
            "2022-10-14",
            "2022-10-24",
            "2026-10-09",
            "2026-10-19",
            "2029-10-19",
            "2029-10-29",
        )
        self.assertSubdivNoordSchoolHolidayName(name, range(2013, 2030))
        self.assertSubdivNoordSchoolHolidayNameCount(name, 9, range(2013, 2030))

        self.assertSubdivMiddenSchoolHolidayName(
            name,
            "2013-10-19",
            "2013-10-27",
            "2017-10-14",
            "2017-10-22",
            "2022-10-22",
            "2022-10-30",
            "2026-10-17",
            "2026-10-25",
            "2029-10-20",
            "2029-10-28",
        )
        self.assertNoSubdivMiddenSchoolHoliday(
            "2013-10-18",
            "2013-10-28",
            "2017-10-13",
            "2017-10-23",
            "2022-10-21",
            "2022-10-31",
            "2026-10-16",
            "2026-10-26",
            "2029-10-19",
            "2029-10-29",
        )
        self.assertSubdivMiddenSchoolHolidayName(name, range(2013, 2030))
        self.assertSubdivMiddenSchoolHolidayNameCount(name, 9, range(2013, 2030))

        self.assertSubdivZuidSchoolHolidayName(
            name,
            "2013-10-12",
            "2013-10-20",
            "2017-10-14",
            "2017-10-22",
            "2022-10-22",
            "2022-10-30",
            "2026-10-17",
            "2026-10-25",
            "2029-10-13",
            "2029-10-21",
        )
        self.assertNoSubdivZuidSchoolHoliday(
            "2013-10-11",
            "2013-10-21",
            "2017-10-13",
            "2017-10-23",
            "2022-10-21",
            "2022-10-31",
            "2026-10-16",
            "2026-10-26",
            "2029-10-12",
            "2029-10-22",
        )
        self.assertSubdivZuidSchoolHolidayName(name, range(2013, 2030))
        self.assertSubdivZuidSchoolHolidayNameCount(name, 9, range(2013, 2030))

    def test_school_spring_break(self):
        name = "Voorjaarsvakantie"
        self.assertNoHolidayName(name)

        self.assertSubdivNoordSchoolHolidayName(
            name,
            "2014-02-22",
            "2014-03-02",
            "2019-02-16",
            "2019-02-24",
            "2023-02-25",
            "2023-03-05",
            "2027-02-20",
            "2027-02-28",
            "2030-02-16",
            "2030-02-24",
        )
        self.assertNoSubdivNoordSchoolHoliday(
            "2014-02-21",
            "2014-03-03",
            "2019-02-15",
            "2019-02-25",
            "2023-02-24",
            "2023-03-06",
            "2027-02-19",
            "2027-03-01",
            "2030-02-15",
            "2030-02-25",
        )
        self.assertSubdivNoordSchoolHolidayName(name, range(2014, 2031))
        self.assertSubdivNoordSchoolHolidayNameCount(name, 9, range(2014, 2031))

        self.assertSubdivMiddenSchoolHolidayName(
            name,
            "2014-02-15",
            "2014-02-23",
            "2019-02-23",
            "2019-03-03",
            "2023-02-25",
            "2023-03-05",
            "2027-02-20",
            "2027-02-28",
            "2030-02-23",
            "2030-03-03",
        )
        self.assertNoSubdivMiddenSchoolHoliday(
            "2014-02-14",
            "2014-02-24",
            "2019-02-22",
            "2019-03-04",
            "2023-02-24",
            "2023-03-06",
            "2027-02-19",
            "2027-03-01",
            "2030-02-22",
            "2030-03-04",
        )
        self.assertSubdivMiddenSchoolHolidayName(name, range(2014, 2031))
        self.assertSubdivMiddenSchoolHolidayNameCount(name, 9, range(2014, 2031))

        self.assertSubdivZuidSchoolHolidayName(
            name,
            "2014-02-15",
            "2014-02-23",
            "2019-02-23",
            "2019-03-03",
            "2023-02-18",
            "2023-02-26",
            "2027-02-13",
            "2027-02-21",
            "2030-02-23",
            "2030-03-03",
        )
        self.assertNoSubdivZuidSchoolHoliday(
            "2014-02-14",
            "2014-02-24",
            "2019-02-22",
            "2019-03-04",
            "2023-02-17",
            "2023-02-27",
            "2027-02-12",
            "2027-02-22",
            "2030-02-22",
            "2030-03-04",
        )
        self.assertSubdivZuidSchoolHolidayName(name, range(2014, 2031))
        self.assertSubdivZuidSchoolHolidayNameCount(name, 9, range(2014, 2031))

    def test_school_may_break(self):
        name = "Meivakantie"
        self.assertNoHolidayName(name)

        self.assertSubdivNoordSchoolHolidayName(
            name,
            "2014-04-26",
            "2014-05-05",
            "2017-04-22",
            "2017-04-30",
            "2021-05-01",
            "2021-05-09",
            "2026-04-25",
            "2026-05-03",
            "2030-04-27",
            "2030-05-05",
        )
        self.assertNoSubdivNoordSchoolHoliday(
            "2014-04-25",
            "2014-05-06",
            "2017-04-21",
            "2017-05-01",
            "2021-04-30",
            "2021-05-10",
            "2026-04-24",
            "2026-05-04",
            "2030-04-26",
            "2030-05-06",
        )
        self.assertSubdivNoordSchoolHolidayName(name, range(2014, 2031))
        # Extended to Liberation Day in 2014.
        self.assertSubdivNoordSchoolHolidayNameCount(name, 10, 2014)
        self.assertSubdivNoordSchoolHolidayNameCount(name, 9, range(2015, 2031))

        self.assertSubdivMiddenSchoolHolidayName(
            name,
            "2014-04-26",
            "2014-05-05",
            "2017-04-22",
            "2017-04-30",
            "2021-05-01",
            "2021-05-09",
            "2026-04-25",
            "2026-05-03",
            "2030-04-27",
            "2030-05-05",
        )
        self.assertNoSubdivMiddenSchoolHoliday(
            "2014-04-25",
            "2014-05-06",
            "2017-04-21",
            "2017-05-01",
            "2021-04-30",
            "2021-05-10",
            "2026-04-24",
            "2026-05-04",
            "2030-04-26",
            "2030-05-06",
        )
        self.assertSubdivMiddenSchoolHolidayName(name, range(2014, 2031))
        # Extended to Liberation Day in 2014.
        self.assertSubdivMiddenSchoolHolidayNameCount(name, 10, 2014)
        self.assertSubdivMiddenSchoolHolidayNameCount(name, 9, range(2015, 2031))

        self.assertSubdivZuidSchoolHolidayName(
            name,
            "2014-04-26",
            "2014-05-05",
            "2017-04-22",
            "2017-04-30",
            "2021-05-01",
            "2021-05-09",
            "2026-04-25",
            "2026-05-03",
            "2030-04-27",
            "2030-05-05",
        )
        self.assertNoSubdivZuidSchoolHoliday(
            "2014-04-25",
            "2014-05-06",
            "2017-04-21",
            "2017-05-01",
            "2021-04-30",
            "2021-05-10",
            "2026-04-24",
            "2026-05-04",
            "2030-04-26",
            "2030-05-06",
        )
        self.assertSubdivZuidSchoolHolidayName(name, range(2014, 2031))
        # Extended to Liberation Day in 2014.
        self.assertSubdivZuidSchoolHolidayNameCount(name, 10, 2014)
        self.assertSubdivZuidSchoolHolidayNameCount(name, 9, range(2015, 2031))

    def test_school_summer_break(self):
        name = "Zomervakantie"
        self.assertNoHolidayName(name)

        self.assertSubdivNoordSchoolHolidayName(
            name,
            "2014-07-05",
            "2014-08-17",
            "2018-07-21",
            "2018-09-02",
            "2022-07-16",
            "2022-08-28",
            "2026-07-04",
            "2026-08-16",
            "2030-07-20",
            "2030-09-01",
        )
        self.assertNoSubdivNoordSchoolHoliday(
            "2014-07-04",
            "2014-08-18",
            "2018-07-20",
            "2018-09-03",
            "2022-07-15",
            "2022-08-29",
            "2026-07-03",
            "2026-08-17",
            "2030-07-19",
            "2030-09-02",
        )
        self.assertSubdivNoordSchoolHolidayName(name, range(2014, 2031))
        self.assertSubdivNoordSchoolHolidayNameCount(name, 44, range(2014, 2031))

        self.assertSubdivMiddenSchoolHolidayName(
            name,
            "2014-07-19",
            "2014-08-31",
            "2018-07-14",
            "2018-08-26",
            "2022-07-09",
            "2022-08-21",
            "2026-07-18",
            "2026-08-30",
            "2030-07-13",
            "2030-08-25",
        )
        self.assertNoSubdivMiddenSchoolHoliday(
            "2014-07-18",
            "2014-09-01",
            "2018-07-13",
            "2018-08-27",
            "2022-07-08",
            "2022-08-22",
            "2026-07-17",
            "2026-08-31",
            "2030-07-12",
            "2030-08-26",
        )
        self.assertSubdivMiddenSchoolHolidayName(name, range(2014, 2031))
        self.assertSubdivMiddenSchoolHolidayNameCount(name, 44, range(2014, 2031))

        self.assertSubdivZuidSchoolHolidayName(
            name,
            "2014-07-12",
            "2014-08-24",
            "2018-07-07",
            "2018-08-19",
            "2022-07-23",
            "2022-09-04",
            "2026-07-11",
            "2026-08-23",
            "2030-07-06",
            "2030-08-18",
        )
        self.assertNoSubdivZuidSchoolHoliday(
            "2014-07-11",
            "2014-08-25",
            "2018-07-06",
            "2018-08-20",
            "2022-07-22",
            "2022-09-05",
            "2026-07-10",
            "2026-08-24",
            "2030-07-05",
            "2030-08-19",
        )
        self.assertSubdivZuidSchoolHolidayName(name, range(2014, 2031))
        self.assertSubdivZuidSchoolHolidayNameCount(name, 44, range(2014, 2031))

    def test_school_christmas_break(self):
        name = "Kerstvakantie"
        self.assertNoHolidayName(name)
        # Nationwide, so the dates are the same in every region.
        for region in Netherlands.subdivisions:
            holidays = Netherlands(subdiv=region, categories=SCHOOL, years=range(2013, 2031))
            self.assertHolidayName(
                name,
                holidays,
                "2013-12-21",
                "2014-01-05",
                "2017-12-23",
                "2018-01-07",
                "2021-12-25",
                "2022-01-09",
                "2026-12-19",
                "2027-01-03",
                "2029-12-22",
                "2030-01-06",
            )
            self.assertNoHoliday(
                holidays,
                "2013-12-20",
                "2014-01-06",
                "2017-12-22",
                "2018-01-08",
                "2021-12-24",
                "2022-01-10",
                "2026-12-18",
                "2027-01-04",
                "2029-12-21",
                "2030-01-07",
            )
            self.assertHolidayName(name, holidays, range(2013, 2031))
            # Two weeks and two weekends, split between the calendar years it spans.
            self.assertHolidayNameCount(name, 6, holidays, 2030)
            self.assertHolidayNameCount(name, 10, holidays, 2021, 2027)
            self.assertHolidayNameCount(name, 11, holidays, 2013, 2016)
            self.assertHolidayNameCount(
                name,
                17,
                holidays,
                range(2014, 2016),
                range(2017, 2020),
                range(2022, 2024),
                range(2025, 2027),
                2029,
            )
            self.assertHolidayNameCount(name, 18, holidays, 2020, 2024, 2028)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nieuwjaarsdag"),
            ("2022-04-15", "Goede vrijdag"),
            ("2022-04-17", "Eerste paasdag"),
            ("2022-04-18", "Tweede paasdag"),
            ("2022-04-27", "Koningsdag"),
            ("2022-05-05", "Bevrijdingsdag"),
            ("2022-05-26", "Hemelvaartsdag"),
            ("2022-06-05", "Eerste pinksterdag"),
            ("2022-06-06", "Tweede pinksterdag"),
            ("2022-12-25", "Eerste kerstdag"),
            ("2022-12-26", "Tweede kerstdag"),
            categories=(OPTIONAL, PUBLIC),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "King's Day"),
            ("2022-05-05", "Liberation Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Pentecost"),
            ("2022-06-06", "Pentecost Monday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            categories=(OPTIONAL, PUBLIC),
        )

    def test_l10n_fy(self):
        self.assertLocalizedHolidays(
            "fy",
            ("2022-01-01", "Nijjiersdei"),
            ("2022-04-15", "Goedfreed"),
            ("2022-04-17", "Peaskesnein"),
            ("2022-04-18", "Peaskemoandei"),
            ("2022-04-27", "Keningsdei"),
            ("2022-05-05", "Befrijingsdei"),
            ("2022-05-26", "Himelfeartsdei"),
            ("2022-06-05", "Pinkstersnein"),
            ("2022-06-06", "Pinkstermoandei"),
            ("2022-12-25", "Eerste Krystdei"),
            ("2022-12-26", "Twadde Krystdei"),
            categories=(OPTIONAL, PUBLIC),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-04-27", "วันเฉลิมพระชนมพรรษาสมเด็จพระราชาธิบดี"),
            ("2022-05-05", "วันประกาศอิสรภาพ"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-12-25", "วันคริสต์มาสวันแรก"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
            categories=(OPTIONAL, PUBLIC),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-27", "День короля"),
            ("2022-05-05", "День визволення"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Пʼятидесятниця"),
            ("2022-06-06", "Другий день Пʼятидесятниці"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
            categories=(OPTIONAL, PUBLIC),
        )

    def _assert_school_l10n(self, language, *expected):
        for subdiv, dt, name in expected:
            self.assertHolidayName(
                name,
                Netherlands(subdiv=subdiv, years=2026, language=language, categories=SCHOOL),
                dt,
            )

    def test_l10n_default_school(self):
        self._assert_school_l10n(
            None,
            ("Noord", "2026-01-01", "Kerstvakantie"),
            ("Noord", "2026-02-21", "Voorjaarsvakantie"),
            ("Noord", "2026-04-25", "Meivakantie"),
            ("Noord", "2026-07-04", "Zomervakantie"),
            ("Midden", "2026-07-18", "Zomervakantie"),
            ("Zuid", "2026-07-11", "Zomervakantie"),
            ("Noord", "2026-10-10", "Herfstvakantie"),
        )

    def test_l10n_en_us_school(self):
        self._assert_school_l10n(
            "en_US",
            ("Noord", "2026-01-01", "Christmas Break"),
            ("Noord", "2026-02-21", "Spring Break"),
            ("Noord", "2026-04-25", "May Break"),
            ("Noord", "2026-07-04", "Summer Break"),
            ("Midden", "2026-07-18", "Summer Break"),
            ("Zuid", "2026-07-11", "Summer Break"),
            ("Noord", "2026-10-10", "Autumn Break"),
        )

    def test_l10n_fy_school(self):
        self._assert_school_l10n(
            "fy",
            ("Noord", "2026-01-01", "Krystfakânsje"),
            ("Noord", "2026-02-21", "Foarjiersfakânsje"),
            ("Noord", "2026-04-25", "Maaiefakânsje"),
            ("Noord", "2026-07-04", "Simmerfakânsje"),
            ("Midden", "2026-07-18", "Simmerfakânsje"),
            ("Zuid", "2026-07-11", "Simmerfakânsje"),
            ("Noord", "2026-10-10", "Hjerstfakânsje"),
        )

    def test_l10n_th_school(self):
        self._assert_school_l10n(
            "th",
            ("Noord", "2026-01-01", "ปิดเทอมคริสต์มาส"),
            ("Noord", "2026-02-21", "ปิดเทอมฤดูใบไม้ผลิ"),
            ("Noord", "2026-04-25", "ปิดเทอมเดือนพฤษภาคม"),
            ("Noord", "2026-07-04", "ปิดเทอมฤดูร้อน"),
            ("Midden", "2026-07-18", "ปิดเทอมฤดูร้อน"),
            ("Zuid", "2026-07-11", "ปิดเทอมฤดูร้อน"),
            ("Noord", "2026-10-10", "ปิดเทอมฤดูใบไม้ร่วง"),
        )

    def test_l10n_uk_school(self):
        self._assert_school_l10n(
            "uk",
            ("Noord", "2026-01-01", "Різдвяні канікули"),
            ("Noord", "2026-02-21", "Весняні канікули"),
            ("Noord", "2026-04-25", "Травневі канікули"),
            ("Noord", "2026-07-04", "Літні канікули"),
            ("Midden", "2026-07-18", "Літні канікули"),
            ("Zuid", "2026-07-11", "Літні канікули"),
            ("Noord", "2026-10-10", "Осінні канікули"),
        )
