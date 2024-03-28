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

from holidays.countries.kyrgyzstan import Kyrgyzstan, KG, KGZ
from tests.common import CommonCountryTests


class TestKyrgyzstan(CommonCountryTests, TestCase):
    def setUp(self):
        self.holidays = Kyrgyzstan()

    def test_country_aliases(self):
        self.assertAliases(Kyrgyzstan, KG, KGZ)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-07", "Christmas Day"),
            ("2022-02-23", "Fatherland Defender's Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-03-21", "Nooruz Mairamy"),
            ("2022-04-07", "Day of the People's April Revolution"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-02", "Orozo Ait (estimated)"),
            ("2022-05-03", "Orozo Ait (estimated)"),
            ("2022-05-05", "Constitution Day"),
            ("2022-05-09", "Victory Day"),
            ("2022-07-09", "Kurman Ait (estimated)"),
            ("2022-08-31", "Independence Day"),
            ("2022-11-07", "Days of History and Commemoration of Ancestors"),
            ("2022-11-08", "Days of History and Commemoration of Ancestors"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-07", "Christmas Day"),
            ("2023-02-23", "Fatherland Defender's Day"),
            ("2023-03-08", "International Women's Day"),
            ("2023-03-21", "Nooruz Mairamy"),
            ("2023-04-07", "Day of the People's April Revolution"),
            ("2023-04-21", "Orozo Ait (estimated)"),
            ("2023-04-22", "Orozo Ait (estimated)"),
            ("2023-05-01", "International Workers' Day"),
            ("2023-05-05", "Constitution Day"),
            ("2023-05-09", "Victory Day"),
            ("2023-06-28", "Kurman Ait (estimated)"),
            ("2023-08-31", "Independence Day"),
            ("2023-11-07", "Days of History and Commemoration of Ancestors"),
            ("2023-11-08", "Days of History and Commemoration of Ancestors"),
            ("2023-12-31", "New Year's Eve"),
        )

    def test_day_of_peoples_revolution(self):
        self.assertNoHoliday("2015-04-07")
        self.assertHoliday("2016-04-07", "2017-04-07")
