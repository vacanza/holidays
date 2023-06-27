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

from holidays.countries.malta import Malta, MT, MLT
from tests.common import TestCase


class TestMalta(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Malta, years=range(1980, 2077))

    def test_country_aliases(self):
        self.assertCountryAliases(Malta, MT, MLT)

    def test_no_holidays(self):
        self.assertNoHolidays(Malta(years=1979))

    def test_1980(self):
        self.assertHolidays(
            Malta(years=1980),
            ("1980-01-01", "New Year's Day"),
            ("1980-03-31", "Freedom Day"),
            ("1980-04-04", "Good Friday"),
            ("1980-05-01", "Worker's Day"),
            ("1980-08-15", "Feast of the Assumption"),
            ("1980-12-13", "Republic Day"),
            ("1980-12-25", "Christmas Day"),
        )

    def test_1987(self):
        self.assertHolidays(
            Malta(years=1987),
            ("1987-01-01", "New Year's Day"),
            ("1987-02-10", "Feast of St. Paul's Shipwreck"),
            ("1987-03-19", "Feast of St. Joseph"),
            ("1987-04-17", "Good Friday"),
            ("1987-05-01", "Worker's Day"),
            ("1987-06-29", "Feast of St. Peter and St. Paul"),
            ("1987-08-15", "Feast of the Assumption"),
            ("1987-09-08", "Feast of Our Lady of Victories"),
            ("1987-09-21", "Independence Day"),
            ("1987-12-08", "Feast of the Immaculate Conception"),
            ("1987-12-13", "Republic Day"),
            ("1987-12-25", "Christmas Day"),
        )

    def test_1989(self):
        self.assertHolidays(
            Malta(years=1989),
            ("1989-01-01", "New Year's Day"),
            ("1989-02-10", "Feast of St. Paul's Shipwreck"),
            ("1989-03-19", "Feast of St. Joseph"),
            ("1989-03-24", "Good Friday"),
            ("1989-03-31", "Freedom Day"),
            ("1989-05-01", "Worker's Day"),
            ("1989-06-07", "Sette Giugno"),
            ("1989-06-29", "Feast of St. Peter and St. Paul"),
            ("1989-08-15", "Feast of the Assumption"),
            ("1989-09-08", "Feast of Our Lady of Victories"),
            ("1989-09-21", "Independence Day"),
            ("1989-12-08", "Feast of the Immaculate Conception"),
            ("1989-12-13", "Republic Day"),
            ("1989-12-25", "Christmas Day"),
        )

    def test_2022(self):
        self.assertHolidays(
            Malta(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-02-10", "Feast of St. Paul's Shipwreck"),
            ("2022-03-19", "Feast of St. Joseph"),
            ("2022-03-31", "Freedom Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Worker's Day"),
            ("2022-06-07", "Sette Giugno"),
            ("2022-06-29", "Feast of St. Peter and St. Paul"),
            ("2022-08-15", "Feast of the Assumption"),
            ("2022-09-08", "Feast of Our Lady of Victories"),
            ("2022-09-21", "Independence Day"),
            ("2022-12-08", "Feast of the Immaculate Conception"),
            ("2022-12-13", "Republic Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
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

    def test_l10n_mt(self):
        self.assertLocalizedHolidays(
            "mt",
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
