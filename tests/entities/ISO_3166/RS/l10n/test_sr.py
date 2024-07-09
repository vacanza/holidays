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

from holidays.entities.ISO_3166.RS import RsHolidays
from tests.common import CommonCountryTests


class TestRsHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(RsHolidays)

    def test_sr(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Нова година"),
            ("2022-01-02", "Нова година"),
            ("2022-01-03", "Нова година (слободан дан)"),
            ("2022-01-07", "Божић"),
            ("2022-02-15", "Дан државности Србије"),
            ("2022-02-16", "Дан државности Србије"),
            ("2022-04-22", "Велики петак"),
            ("2022-04-23", "Велика субота"),
            ("2022-04-24", "Васкрс"),
            ("2022-04-25", "Други дан Васкрса"),
            ("2022-05-01", "Празник рада"),
            ("2022-05-02", "Празник рада"),
            ("2022-05-03", "Празник рада (слободан дан)"),
            ("2022-11-11", "Дан примирја у Првом светском рату"),
        )
