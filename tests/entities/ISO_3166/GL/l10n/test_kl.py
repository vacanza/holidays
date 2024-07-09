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
        super().setUpClass(GlHolidays)

    def test_kl(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Ukioq nutaaq"),
            ("2022-01-06", "Mitaarneq"),
            ("2022-04-14", "Sisamanngornermi illernartumi"),
            ("2022-04-15", "Tallimanngorneq ajortorsiorneq"),
            ("2022-04-17", "Poorskimi"),
            ("2022-04-18", "Poorskimi ullut aappaat"),
            ("2022-05-01", "Sulisartut ulluat"),
            ("2022-05-13", "Ulloq qinuffiusoq"),
            ("2022-05-26", "Ulloq Kristusip qilaliarnera"),
            ("2022-06-05", "Piinsip ullua"),
            ("2022-06-06", "Piinsip ulluisa aappaanni"),
            ("2022-06-21", "Ullortuneq"),
            ("2022-12-24", "Juulliaqqami"),
            ("2022-12-25", "Juulli"),
            ("2022-12-26", "Juullip aappaa"),
            ("2022-12-31", "Ukiortaami"),
        )
