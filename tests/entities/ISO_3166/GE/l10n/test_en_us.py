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

from holidays.entities.ISO_3166.GE import GeHolidays
from tests.common import CommonCountryTests


class TestGeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GeHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Christmas Day"),
            ("2022-01-19", "Epiphany"),
            ("2022-03-03", "Mother's Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-09", "National Unity Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-23", "Holy Saturday"),
            ("2022-04-24", "Easter Sunday"),
            ("2022-04-25", "Easter Monday"),
            ("2022-05-09", "Day of Victory over Fascism"),
            ("2022-05-12", "Saint Andrew's Day"),
            ("2022-05-26", "Independence Day"),
            ("2022-08-28", "Dormition of the Mother of God"),
            ("2022-10-14", "Holiday of Svetitskhovloba, Robe of Jesus"),
            ("2022-11-23", "Saint George's Day"),
        )
