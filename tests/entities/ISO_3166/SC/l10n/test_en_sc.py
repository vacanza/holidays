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

from holidays.entities.ISO_3166.SC import ScHolidays
from tests.common import CommonCountryTests


class TestScHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ScHolidays)

    def test_en_sc(self):
        # https://www.psb.gov.sc/public-holidays
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year Holiday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Easter Saturday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-30", "The Fete Dieu"),
            ("2024-06-18", "Constitution Day"),
            ("2024-06-29", "Independence (National) Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-11-01", "All Saints Day"),
            ("2024-12-08", "The Feast of the Immaculate Conception"),
            ("2024-12-09", "The Feast of the Immaculate Conception (observed)"),
            ("2024-12-25", "Christmas Day"),
        )
