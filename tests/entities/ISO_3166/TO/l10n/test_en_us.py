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

from holidays.entities.ISO_3166.TO import ToHolidays
from tests.common import CommonCountryTests


class TestToHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ToHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-25", "Anzac Day"),
            ("2023-06-05", "Emancipation Day (observed)"),
            ("2023-07-04", "Birthday of the Reigning Sovereign of Tonga"),
            ("2023-09-17", "Birthday of the Heir to the Crown of Tonga"),
            ("2023-09-18", "Birthday of the Heir to the Crown of Tonga (observed)"),
            ("2023-11-06", "Constitution Day (observed)"),
            ("2023-12-04", "Anniversary of the Coronation of HM King George Tupou I"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
