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

from holidays.entities.ISO_3166.GL import GlHolidays
from tests.common import CommonCountryTests


class TestGlHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GlHolidays, language="da")

    def test_da(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nytårsdag"),
            ("2022-01-06", "Helligtrekongersdag"),
            ("2022-04-14", "Skærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Påskedag"),
            ("2022-04-18", "Anden påskedag"),
            ("2022-05-01", "Arbejdernes kampdag"),
            ("2022-05-13", "Store bededag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Pinsedag"),
            ("2022-06-06", "Anden pinsedag"),
            ("2022-06-21", "Nationaldag"),
            ("2022-12-24", "Juleaftensdag"),
            ("2022-12-25", "Juledag"),
            ("2022-12-26", "Anden juledag"),
            ("2022-12-31", "Nytårsaften"),
        )
