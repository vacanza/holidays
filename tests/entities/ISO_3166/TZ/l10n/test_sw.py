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

from holidays.entities.ISO_3166.TZ import TzHolidays
from tests.common import CommonCountryTests


class TestTanzania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TzHolidays)

    def test_sw(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Mwaka Mpya"),
            ("2023-01-12", "Mapinduzi ya Zanzibar"),
            (
                "2023-04-07",
                (
                    "Ijumaa Kuu; Siku ya kumbukumbu ya Rais wa Kwanza wa Serikali "
                    "ya Mapinduzi Zanzibar Sheikh Abeid Amani Karume"
                ),
            ),
            ("2023-04-09", "Sikukuu ya Pasaka"),
            ("2023-04-10", "Jumatatu ya Pasaka"),
            ("2023-04-22", "Eid El-Fitry"),
            ("2023-04-26", "Muungano wa Tanganyika na Zanzibar"),
            ("2023-05-01", "Sikukuu ya Wafanyakazi"),
            ("2023-06-29", "Eid El-Hajj"),
            ("2023-07-07", "Sabasaba"),
            ("2023-08-08", "Siku ya Wakulima"),
            ("2023-09-28", "Maulidi"),
            ("2023-10-14", "Kumbukumbu ya Mwalimu Nyerere"),
            ("2023-12-09", "Uhuru na Jamhuri"),
            ("2023-12-25", "Kuzaliwa Kristo"),
            ("2023-12-26", "Siku ya Kupeana Zawadi"),
        )
