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

from holidays.entities.ISO_3166.PY import PyHolidays
from tests.common import CommonCountryTests


class TestPyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PyHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Patriots Day"),
            ("2022-04-13", "Public sector holiday"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Public sector holiday"),
            ("2022-05-14", "Independence Day"),
            ("2022-05-15", "Independence Day"),
            ("2022-06-12", "Chaco Armistice Day"),
            ("2022-08-15", "Asuncion Foundation's Day"),
            ("2022-10-03", "Boqueron Battle Day"),
            ("2022-12-08", "Caacupe Virgin Day"),
            ("2022-12-25", "Christmas Day"),
        )
