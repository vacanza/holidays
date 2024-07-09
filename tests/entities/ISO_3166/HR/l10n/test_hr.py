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

from holidays.entities.ISO_3166.HR import HrHolidays
from tests.common import CommonCountryTests


class TestHrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HrHolidays)

    def test_hr(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nova godina"),
            ("2022-01-06", "Bogojavljenje ili Sveta tri kralja"),
            ("2022-04-17", "Uskrs"),
            ("2022-04-18", "Uskrsni ponedjeljak"),
            ("2022-05-01", "Praznik rada"),
            ("2022-05-30", "Dan državnosti"),
            ("2022-06-16", "Tijelovo"),
            ("2022-06-22", "Dan antifašističke borbe"),
            ("2022-08-05", "Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja"),
            ("2022-08-15", "Velika Gospa"),
            ("2022-11-01", "Svi sveti"),
            (
                "2022-11-18",
                "Dan sjećanja na žrtve Domovinskog rata i "
                "Dan sjećanja na žrtvu Vukovara i Škabrnje",
            ),
            ("2022-12-25", "Božić"),
            ("2022-12-26", "Sveti Stjepan"),
        )
