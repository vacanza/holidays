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

from holidays.countries.malta import Malta, MT, MLT
from tests.common import CommonCountryTests


class TestMalta(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Malta)

    def test_country_aliases(self):
        self.assertAliases(Malta, MT, MLT)

    def test_no_holidays(self):
        self.assertNoHolidays(Malta(years=1979))

    def test_1980(self):
        self.assertHolidays(
            Malta(years=1980),
            ("1980-01-01", "L-Ewwel tas-Sena"),
            ("1980-03-31", "Jum il-Ħelsien"),
            ("1980-04-04", "Il-Ġimgħa l-Kbira"),
            ("1980-05-01", "Jum il-Ħaddiem"),
            ("1980-08-15", "Il-Festa ta' Santa Marija"),
            ("1980-12-13", "Jum ir-Repubblika"),
            ("1980-12-25", "Il-Milied"),
        )

    def test_1987(self):
        self.assertHolidays(
            Malta(years=1987),
            ("1987-01-01", "L-Ewwel tas-Sena"),
            ("1987-02-10", "Il-Festa tan-Nawfraġju ta' San Pawl"),
            ("1987-03-19", "Il-Festa ta' San Ġużepp"),
            ("1987-04-17", "Il-Ġimgħa l-Kbira"),
            ("1987-05-01", "Jum il-Ħaddiem"),
            ("1987-06-29", "Il-Festa ta' San Pietru u San Pawl"),
            ("1987-08-15", "Il-Festa ta' Santa Marija"),
            ("1987-09-08", "Jum il-Vitorja"),
            ("1987-09-21", "Jum l-Indipendenza"),
            ("1987-12-08", "Il-Festa tal-Immakulata Kunċizzjoni"),
            ("1987-12-13", "Jum ir-Repubblika"),
            ("1987-12-25", "Il-Milied"),
        )

    def test_1989(self):
        self.assertHolidays(
            Malta(years=1989),
            ("1989-01-01", "L-Ewwel tas-Sena"),
            ("1989-02-10", "Il-Festa tan-Nawfraġju ta' San Pawl"),
            ("1989-03-19", "Il-Festa ta' San Ġużepp"),
            ("1989-03-24", "Il-Ġimgħa l-Kbira"),
            ("1989-03-31", "Jum il-Ħelsien"),
            ("1989-05-01", "Jum il-Ħaddiem"),
            ("1989-06-07", "Sette Giugno"),
            ("1989-06-29", "Il-Festa ta' San Pietru u San Pawl"),
            ("1989-08-15", "Il-Festa ta' Santa Marija"),
            ("1989-09-08", "Jum il-Vitorja"),
            ("1989-09-21", "Jum l-Indipendenza"),
            ("1989-12-08", "Il-Festa tal-Immakulata Kunċizzjoni"),
            ("1989-12-13", "Jum ir-Repubblika"),
            ("1989-12-25", "Il-Milied"),
        )

    def test_2022(self):
        self.assertHolidays(
            Malta(years=2022),
            ("2022-01-01", "L-Ewwel tas-Sena"),
            ("2022-02-10", "Il-Festa tan-Nawfraġju ta' San Pawl"),
            ("2022-03-19", "Il-Festa ta' San Ġużepp"),
            ("2022-03-31", "Jum il-Ħelsien"),
            ("2022-04-15", "Il-Ġimgħa l-Kbira"),
            ("2022-05-01", "Jum il-Ħaddiem"),
            ("2022-06-07", "Sette Giugno"),
            ("2022-06-29", "Il-Festa ta' San Pietru u San Pawl"),
            ("2022-08-15", "Il-Festa ta' Santa Marija"),
            ("2022-09-08", "Jum il-Vitorja"),
            ("2022-09-21", "Jum l-Indipendenza"),
            ("2022-12-08", "Il-Festa tal-Immakulata Kunċizzjoni"),
            ("2022-12-13", "Jum ir-Repubblika"),
            ("2022-12-25", "Il-Milied"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "L-Ewwel tas-Sena"),
            ("2023-02-10", "Il-Festa tan-Nawfraġju ta' San Pawl"),
            ("2023-03-19", "Il-Festa ta' San Ġużepp"),
            ("2023-03-31", "Jum il-Ħelsien"),
            ("2023-04-07", "Il-Ġimgħa l-Kbira"),
            ("2023-05-01", "Jum il-Ħaddiem"),
            ("2023-06-07", "Sette Giugno"),
            ("2023-06-29", "Il-Festa ta' San Pietru u San Pawl"),
            ("2023-08-15", "Il-Festa ta' Santa Marija"),
            ("2023-09-08", "Jum il-Vitorja"),
            ("2023-09-21", "Jum l-Indipendenza"),
            ("2023-12-08", "Il-Festa tal-Immakulata Kunċizzjoni"),
            ("2023-12-13", "Jum ir-Repubblika"),
            ("2023-12-25", "Il-Milied"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-02-10", "Feast of St. Paul's Shipwreck"),
            ("2023-03-19", "Feast of St. Joseph"),
            ("2023-03-31", "Freedom Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "Worker's Day"),
            ("2023-06-07", "Sette Giugno"),
            ("2023-06-29", "Feast of St. Peter and St. Paul"),
            ("2023-08-15", "Feast of the Assumption"),
            ("2023-09-08", "Feast of Our Lady of Victories"),
            ("2023-09-21", "Independence Day"),
            ("2023-12-08", "Feast of the Immaculate Conception"),
            ("2023-12-13", "Republic Day"),
            ("2023-12-25", "Christmas Day"),
        )
