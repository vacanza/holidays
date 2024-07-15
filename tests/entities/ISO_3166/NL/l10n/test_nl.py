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

from holidays.entities.ISO_3166.NL import NlHolidays
from tests.common import CommonCountryTests


class TestNlHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NlHolidays)

    def test_nl(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nieuwjaarsdag"),
            ("2022-04-15", "Goede Vrijdag"),
            ("2022-04-17", "Eerste paasdag"),
            ("2022-04-18", "Tweede paasdag"),
            ("2022-04-27", "Koningsdag"),
            ("2022-05-05", "Bevrijdingsdag"),
            ("2022-05-26", "Hemelvaartsdag"),
            ("2022-06-05", "Eerste Pinksterdag"),
            ("2022-06-06", "Tweede Pinksterdag"),
            ("2022-12-25", "Eerste Kerstdag"),
            ("2022-12-26", "Tweede Kerstdag"),
        )
