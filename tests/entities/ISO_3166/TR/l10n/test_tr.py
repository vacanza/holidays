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

from holidays.entities.ISO_3166.TR import TrHolidays
from tests.common import CommonCountryTests


class TestTrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TrHolidays)

    def test_tr(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Yılbaşı"),
            ("2023-04-20", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2023-04-21", "Ramazan Bayramı"),
            ("2023-04-22", "Ramazan Bayramı"),
            ("2023-04-23", "Ramazan Bayramı; Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2023-05-01", "Emek ve Dayanışma Günü"),
            ("2023-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2023-06-27", "Kurban Bayramı (saat 13.00'ten)"),
            ("2023-06-28", "Kurban Bayramı"),
            ("2023-06-29", "Kurban Bayramı"),
            ("2023-06-30", "Kurban Bayramı"),
            ("2023-07-01", "Kurban Bayramı"),
            ("2023-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2023-08-30", "Zafer Bayramı"),
            ("2023-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
            ("2023-10-29", "Cumhuriyet Bayramı"),
        )
