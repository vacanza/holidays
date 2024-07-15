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

from holidays.entities.ISO_3166.IR import IrHolidays
from tests.common import CommonCountryTests


class TestIrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IrHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-02-04", "Birthday of Ali (estimated)"),
            ("2023-02-11", "Islamic Revolution Day"),
            ("2023-02-18", "Ascension of Muhammad (estimated)"),
            ("2023-03-07", "Birthday of Mahdi (estimated)"),
            ("2023-03-20", "Iranian Oil Industry Nationalization Day"),
            ("2023-03-21", "Persian New Year"),
            ("2023-03-22", "Persian New Year"),
            ("2023-03-23", "Persian New Year"),
            ("2023-03-24", "Persian New Year"),
            ("2023-04-01", "Islamic Republic Day"),
            ("2023-04-02", "Nature's Day"),
            ("2023-04-12", "Martyrdom of Ali (estimated)"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-04-22", "Eid al-Fitr (estimated)"),
            ("2023-05-15", "Martyrdom of Ja'far al-Sadiq (estimated)"),
            ("2023-06-04", "Death of Khomeini"),
            ("2023-06-05", "Khordad National Uprising"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-07-06", "Eid al-Ghadeer (estimated)"),
            ("2023-07-27", "Tasua (estimated)"),
            ("2023-07-28", "Ashura (estimated)"),
            ("2023-09-05", "Arbaeen (estimated)"),
            ("2023-09-13", "Demise of Prophet Muhammad and Hasan ibn Ali (estimated)"),
            ("2023-09-15", "Martyrdom of Ali al-Rida (estimated)"),
            ("2023-09-23", "Martyrdom of Hasan al-Askari (estimated)"),
            ("2023-10-02", "Birthday of Muhammad and Ja'far al-Sadiq (estimated)"),
            ("2023-12-16", "Martyrdom of Fatima (estimated)"),
        )
