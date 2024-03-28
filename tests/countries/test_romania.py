#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.romania import Romania, RO, ROU
from tests.common import CommonCountryTests


class TestRomania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Romania)

    def test_country_aliases(self):
        self.assertAliases(Romania, RO, ROU)

    def test_from_2024(self):
        self.assertHoliday("2024-01-06", "2024-01-07")
        self.assertNoHoliday("2023-01-06", "2023-01-07")
        self.assertNoHolidayName("Bobotează", Romania(years=2023))
        self.assertNoHolidayName("Sfântul Ion", Romania(years=2023))

    def test_unification_day(self):
        self.assertHoliday("2016-01-24")
        self.assertNoHoliday("2015-01-24")
        self.assertNoHolidayName("Ziua Unirii Principatelor Române", Romania(years=2015))

    def test_easter(self):
        self.assertHoliday(
            "2017-04-16",
            "2017-04-17",
            "2018-04-06",
            "2018-04-08",
            "2018-04-09",
        )
        self.assertNoHoliday("2016-04-29", "2017-04-14")

    def test_childrens_day(self):
        self.assertHoliday("2017-06-01")
        self.assertNoHoliday("2016-06-01")
        self.assertNoHolidayName("Ziua Copilului", Romania(years=2016))

    def test_assumption_day(self):
        self.assertHoliday("2009-08-15")
        self.assertNoHoliday("2008-08-15")
        self.assertNoHolidayName("Adormirea Maicii Domnului", Romania(years=2008))

    def test_saint_andrews_day(self):
        self.assertHoliday("2012-11-30")
        self.assertNoHoliday("2011-11-30")
        self.assertNoHolidayName("Sfantul Apostol Andrei cel Intai chemat", Romania(years=2011))

    def test_2020(self):
        # https://publicholidays.ro/2020-dates/
        self.assertHolidayDates(
            Romania(years=2020),
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
        self.assertHolidayDates(
            Romania(years=2022),
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
        self.assertHolidayDates(
            Romania(years=2023),
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
            ("2018-01-01", "Anul Nou"),
            ("2018-01-02", "Anul Nou"),
            ("2018-01-24", "Ziua Unirii Principatelor Române"),
            ("2018-04-06", "Paștele"),
            ("2018-04-08", "Paștele"),
            ("2018-04-09", "Paștele"),
            ("2018-05-01", "Ziua Muncii"),
            ("2018-05-27", "Rusaliile"),
            ("2018-05-28", "Rusaliile"),
            ("2018-06-01", "Ziua Copilului"),
            ("2018-08-15", "Adormirea Maicii Domnului"),
            ("2018-11-30", "Sfantul Apostol Andrei cel Intai chemat"),
            ("2018-12-01", "Ziua Națională a României"),
            ("2018-12-25", "Crăciunul"),
            ("2018-12-26", "Crăciunul"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-01-02", "New Year's Day"),
            ("2018-01-24", "Unification of the Romanian Principalities Day"),
            ("2018-04-06", "Easter"),
            ("2018-04-08", "Easter"),
            ("2018-04-09", "Easter"),
            ("2018-05-01", "Labor Day"),
            ("2018-05-27", "Pentecost"),
            ("2018-05-28", "Pentecost"),
            ("2018-06-01", "Children's Day"),
            ("2018-08-15", "Dormition of the Mother of God"),
            ("2018-11-30", "Saint Andrew's Day"),
            ("2018-12-01", "National Day"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2018-01-01", "Новий рік"),
            ("2018-01-02", "Новий рік"),
            ("2018-01-24", "День обʼєднання Дунайських князівств"),
            ("2018-04-06", "Великдень"),
            ("2018-04-08", "Великдень"),
            ("2018-04-09", "Великдень"),
            ("2018-05-01", "День праці"),
            ("2018-05-27", "Трійця"),
            ("2018-05-28", "Трійця"),
            ("2018-06-01", "День захисту дітей"),
            ("2018-08-15", "Успіння Пресвятої Богородиці"),
            ("2018-11-30", "День святого Андрія Первозваного"),
            ("2018-12-01", "Національний день Румунії"),
            ("2018-12-25", "Різдво Христове"),
            ("2018-12-26", "Різдво Христове"),
        )
