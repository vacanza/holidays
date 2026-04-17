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

from holidays.countries.romania import Romania
from tests.common import CommonCountryTests


class TestRomania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Romania)

    def test_new_years_day(self):
        self.assertHolidayName(
            "Anul Nou",
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in self.full_range),
        )

    def test_epiphany_day(self):
        name = "Botezul Domnului - Boboteaza"
        self.assertHolidayName(name, (f"{year}-01-06" for year in range(2024, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2024))

    def test_saint_john_baptist(self):
        name = "Soborul Sfântului Proroc Ioan Botezătorul"
        self.assertHolidayName(name, (f"{year}-01-07" for year in range(2024, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2024))

    def test_unification_of_romanian_principalities_day(self):
        name = "Ziua Unirii Principatelor Române"
        self.assertHolidayName(name, (f"{year}-01-24" for year in range(2017, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2017))

    def test_good_friday(self):
        name = "Vinerea Mare"
        self.assertHolidayName(
            name,
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2018, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2018))

    def test_easter(self):
        name = "Paștele"
        self.assertHolidayName(
            name,
            "2020-04-19",
            "2020-04-20",
            "2021-05-02",
            "2021-05-03",
            "2022-04-24",
            "2022-04-25",
            "2023-04-16",
            "2023-04-17",
            "2024-05-05",
            "2024-05-06",
            "2025-04-20",
            "2025-04-21",
        )
        self.assertHolidayNameCount(name, 2, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Ziua Muncii", (f"{year}-05-01" for year in self.full_range))

    def test_childrens_day(self):
        name = "Ziua Copilului"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2017, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2017))

    def test_pentecost(self):
        name = "Rusaliile"
        self.assertHolidayName(
            name,
            "2020-06-07",
            "2020-06-08",
            "2021-06-20",
            "2021-06-21",
            "2022-06-12",
            "2022-06-13",
            "2023-06-04",
            "2023-06-05",
            "2024-06-23",
            "2024-06-24",
            "2025-06-08",
            "2025-06-09",
        )
        self.assertHolidayNameCount(name, 2, range(2009, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2009))

    def test_dormition_of_mother_of_god(self):
        name = "Adormirea Maicii Domnului"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(2009, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2009))

    def test_saint_andrews_day(self):
        name = "Sfântul Apostol Andrei, cel Întâi chemat, Ocrotitorul României"
        self.assertHolidayName(name, (f"{year}-11-30" for year in range(2012, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2012))

    def test_national_day(self):
        self.assertHolidayName(
            "Ziua Națională a României", (f"{year}-12-01" for year in self.full_range)
        )

    def test_christmas_day(self):
        self.assertHolidayName(
            "Crăciunul",
            (f"{year}-12-25" for year in self.full_range),
            (f"{year}-12-26" for year in self.full_range),
        )

    def test_2020(self):
        # https://publicholidays.ro/2020-dates/
        self.assertHolidayDatesInYear(
            2020,
            "2020-01-01",
            "2020-01-02",
            "2020-01-24",
            "2020-04-17",
            "2020-04-19",
            "2020-04-20",
            "2020-05-01",
            "2020-06-01",
            "2020-06-07",
            "2020-06-08",
            "2020-08-15",
            "2020-11-30",
            "2020-12-01",
            "2020-12-25",
            "2020-12-26",
        )

    def test_2022(self):
        # https://publicholidays.ro/2022-dates/
        self.assertHolidayDatesInYear(
            2022,
            "2022-01-01",
            "2022-01-02",
            "2022-01-24",
            "2022-04-22",
            "2022-04-24",
            "2022-04-25",
            "2022-05-01",
            "2022-06-01",
            "2022-06-12",
            "2022-06-13",
            "2022-08-15",
            "2022-11-30",
            "2022-12-01",
            "2022-12-25",
            "2022-12-26",
        )

    def test_2023(self):
        # https://publicholidays.ro/2023-dates/
        self.assertHolidayDatesInYear(
            2023,
            "2023-01-01",
            "2023-01-02",
            "2023-01-24",
            "2023-04-14",
            "2023-04-16",
            "2023-04-17",
            "2023-05-01",
            "2023-06-01",
            "2023-06-04",
            "2023-06-05",
            "2023-08-15",
            "2023-11-30",
            "2023-12-01",
            "2023-12-25",
            "2023-12-26",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Anul Nou"),
            ("2025-01-02", "Anul Nou"),
            ("2025-01-06", "Botezul Domnului - Boboteaza"),
            ("2025-01-07", "Soborul Sfântului Proroc Ioan Botezătorul"),
            ("2025-01-24", "Ziua Unirii Principatelor Române"),
            ("2025-04-18", "Vinerea Mare"),
            ("2025-04-20", "Paștele"),
            ("2025-04-21", "Paștele"),
            ("2025-05-01", "Ziua Muncii"),
            ("2025-06-01", "Ziua Copilului"),
            ("2025-06-08", "Rusaliile"),
            ("2025-06-09", "Rusaliile"),
            ("2025-08-15", "Adormirea Maicii Domnului"),
            ("2025-11-30", "Sfântul Apostol Andrei, cel Întâi chemat, Ocrotitorul României"),
            ("2025-12-01", "Ziua Națională a României"),
            ("2025-12-25", "Crăciunul"),
            ("2025-12-26", "Crăciunul"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "New Year's Day"),
            ("2025-01-06", "Epiphany"),
            ("2025-01-07", "Saint John the Baptist"),
            ("2025-01-24", "Unification of the Romanian Principalities Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter"),
            ("2025-04-21", "Easter"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-01", "Children's Day"),
            ("2025-06-08", "Pentecost"),
            ("2025-06-09", "Pentecost"),
            ("2025-08-15", "Dormition of the Mother of God"),
            ("2025-11-30", "Saint Andrew's Day"),
            ("2025-12-01", "National Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2025-01-01", "Новий рік"),
            ("2025-01-02", "Новий рік"),
            ("2025-01-06", "Богоявлення"),
            ("2025-01-07", "День Івана Хрестителя"),
            ("2025-01-24", "День обʼєднання Дунайських князівств"),
            ("2025-04-18", "Страсна пʼятниця"),
            ("2025-04-20", "Великдень"),
            ("2025-04-21", "Великдень"),
            ("2025-05-01", "День праці"),
            ("2025-06-01", "День захисту дітей"),
            ("2025-06-08", "Трійця"),
            ("2025-06-09", "Трійця"),
            ("2025-08-15", "Успіння Пресвятої Богородиці"),
            ("2025-11-30", "День Святого Андрія Первозваного, захисника Румунії"),
            ("2025-12-01", "Національний день Румунії"),
            ("2025-12-25", "Різдво Христове"),
            ("2025-12-26", "Різдво Христове"),
        )
