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

from holidays.countries.honduras import Honduras, HN, HND
from tests.common import CommonCountryTests


class TestHonduras(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Honduras)

    def test_country_aliases(self):
        self.assertAliases(Honduras, HN, HND)

    def test_2014(self):
        self.assertHolidayDates(
            "2014-01-01",
            "2014-04-14",
            "2014-04-17",
            "2014-04-18",
            "2014-04-19",
            "2014-05-01",
            "2014-09-15",
            "2014-10-03",
            "2014-10-12",
            "2014-10-21",
            "2014-12-25",
        )

    def test_2016(self):
        # https://www.officeholidays.com/countries/honduras/2016
        self.assertHolidayDates(
            "2016-01-01",
            "2016-03-24",
            "2016-03-25",
            "2016-03-26",
            "2016-04-14",
            "2016-05-01",
            "2016-09-15",
            "2016-10-05",
            "2016-10-06",
            "2016-10-07",
            "2016-12-25",
        )

    def test_2021(self):
        # https://www.officeholidays.com/countries/honduras/2021
        self.assertHolidayDates(
            "2021-01-01",
            "2021-04-01",
            "2021-04-02",
            "2021-04-03",
            "2021-04-14",
            "2021-05-01",
            "2021-09-15",
            "2021-10-06",
            "2021-10-07",
            "2021-10-08",
            "2021-12-25",
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Día de las Américas; Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Sábado de Gloria"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-09-15", "Día de la Independencia"),
            ("2022-10-05", "Semana Morazánica"),
            ("2022-10-06", "Semana Morazánica"),
            ("2022-10-07", "Semana Morazánica"),
            ("2022-12-25", "Navidad"),
        )

    def test_2025(self):
        self.assertHolidayDates(
            "2025-01-01",
            "2025-04-14",
            "2025-04-17",
            "2025-04-18",
            "2025-04-19",
            "2025-05-01",
            "2025-09-15",
            "2025-10-01",
            "2025-10-02",
            "2025-10-03",
            "2025-12-25",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Día de las Américas; Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Sábado de Gloria"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-09-15", "Día de la Independencia"),
            ("2022-10-05", "Semana Morazánica"),
            ("2022-10-06", "Semana Morazánica"),
            ("2022-10-07", "Semana Morazánica"),
            ("2022-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday; Panamerican Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-05-01", "Labor Day"),
            ("2022-09-15", "Independence Day"),
            ("2022-10-05", "Morazan Weekend"),
            ("2022-10-06", "Morazan Weekend"),
            ("2022-10-07", "Morazan Weekend"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер; День Америки"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-16", "Велика субота"),
            ("2022-05-01", "День праці"),
            ("2022-09-15", "День незалежності"),
            ("2022-10-05", "Тиждень Морасана"),
            ("2022-10-06", "Тиждень Морасана"),
            ("2022-10-07", "Тиждень Морасана"),
            ("2022-12-25", "Різдво Христове"),
        )
