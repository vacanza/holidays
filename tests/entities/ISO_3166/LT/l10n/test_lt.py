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

from holidays.entities.ISO_3166.LT import LtHolidays
from tests.common import CommonCountryTests


class TestLithuania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LtHolidays)

    def test_lt(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Naujųjų metų diena"),
            ("2022-02-16", "Lietuvos valstybės atkūrimo diena"),
            ("2022-03-11", "Lietuvos nepriklausomybės atkūrimo diena"),
            ("2022-04-17", "Šv. Velykos"),
            ("2022-04-18", "Antroji šv. Velykų diena"),
            ("2022-05-01", "Motinos diena; Tarptautinė darbo diena"),
            ("2022-06-05", "Tėvo diena"),
            ("2022-06-24", "Rasos ir Joninių diena"),
            (
                "2022-07-06",
                "Valstybės (Lietuvos karaliaus Mindaugo karūnavimo) ir Tautiškos giesmės diena",
            ),
            ("2022-08-15", "Žolinė (Švč. Mergelės Marijos ėmimo į dangų diena)"),
            ("2022-11-01", "Visų Šventųjų diena"),
            ("2022-11-02", "Mirusiųjų atminimo (Vėlinių) diena"),
            ("2022-12-24", "Kūčių diena"),
            ("2022-12-25", "Šv. Kalėdų pirma diena"),
            ("2022-12-26", "Šv. Kalėdų antra diena"),
        )
