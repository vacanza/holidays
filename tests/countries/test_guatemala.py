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

from holidays.countries.guatemala import Guatemala, GT, GUA
from tests.common import TestCase


class TestGuatemala(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Guatemala)

    def test_country_aliases(self):
        self.assertCountryAliases(Guatemala, GT, GUA)

    def test_2016(self):
        # https://calendariohispanohablante.com/2016/calendario-guatemala-2016.html
        dt = (
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
        self.assertHoliday(dt)

    def test_2017(self):
        # https://calendariohispanohablante.com/2017/calendario-guatemala-2017.html
        dt = (
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
        self.assertHoliday(dt)

    def test_2018(self):
        # https://calendariohispanohablante.com/2018/calendario-guatemala-2018.html
        dt = (
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
        self.assertHoliday(dt)

    def test_2019(self):
        # https://calendariohispanohablante.com/2019/calendario-guatemala-2019.html
        dt = (
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
        self.assertHoliday(dt)

    def test_2020(self):
        # https://calendariohispanohablante.com/2020/calendario-guatemala-2020.html
        dt = (
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
        self.assertHoliday(dt)

    def test_2021(self):
        # https://calendariohispanohablante.com/2021/calendario-guatemala-2021.html
        dt = (
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
        self.assertHoliday(dt)

    def test_2022(self):
        # https://publicholidays.la/guatemala/es/2022-dates/
        dt = (
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
        self.assertHoliday(dt)

    def test_2023(self):
        # https://publicholidays.la/guatemala/es/2023-dates/
        dt = (
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
        self.assertHoliday(dt)

    def test_2024(self):
        # https://publicholidays.la/guatemala/es/2024-dates/
        dt = (
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
        self.assertHoliday(dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Año Nuevo"),
            ("2024-03-28", "Jueves Santo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-03-30", "Sabado Santo"),
            ("2024-05-01", "Dia del Trabajo"),
            ("2024-07-01", "Dia del Ejército"),
            ("2024-08-15", "Dia de la Asunción"),
            ("2024-09-15", "Día de la Independencia"),
            ("2024-10-20", "Dia de la Revolución"),
            ("2024-11-01", "Dia de Todos los Santos"),
            ("2024-12-25", "Dia de Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-28", "Good Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Good Saturday"),
            ("2024-05-01", "Labor Day"),
            ("2024-07-01", "Army Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-09-15", "Independence Day"),
            ("2024-10-20", "Revolution Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-12-25", "Christmas Day"),
        )
