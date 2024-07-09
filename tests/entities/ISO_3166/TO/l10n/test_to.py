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
        super().setUpClass(ToHolidays)

    def test_l10n_default(self):
        # https://www.gov.to/press-release/tonga-public-holidays-for-2023/
        self.assertLocalizedHolidays(
            ("2023-01-01", "'Uluaki 'Aho 'o e Ta'u Fo'ou"),
            ("2023-04-07", "Falaite Lelei"),
            ("2023-04-10", "Monite 'o e Toetu'u"),
            ("2023-04-25", "'Aho Anzac"),
            ("2023-06-05", "'Aho Tau'ataina (fakatokanga'i)"),
            ("2023-07-04", "'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule"),
            ("2023-09-17", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga"),
            ("2023-09-18", "'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga (fakatokanga'i)"),
            ("2023-11-06", "'Aho Konisitutone (fakatokanga'i)"),
            (
                "2023-12-04",
                "'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko Siaosi Tupou I",
            ),
            ("2023-12-25", "'Aho Kilisimasi"),
            ("2023-12-26", "'Aho 2 'o e Kilisimasi"),
        )
