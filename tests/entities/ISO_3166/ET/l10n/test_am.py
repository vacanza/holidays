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

from holidays.entities.ISO_3166.ET import EtHolidays
from tests.common import CommonCountryTests


class TestEtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EtHolidays)

    def test_am(self):
        self.assertLocalizedHolidays(
            ("2022-01-07", "ገና"),
            ("2022-01-19", "ጥምቀት"),
            ("2022-03-02", "አድዋ"),
            ("2022-04-22", "ስቅለት"),
            ("2022-04-24", "ፋሲካ"),
            ("2022-05-01", "የሰራተኞች ቀን"),
            ("2022-05-02", "ኢድ አልፈጥር"),
            ("2022-05-05", "የአርበኞች ቀን"),
            ("2022-05-28", "ደርግ የወደቀበት ቀን"),
            ("2022-07-09", "አረፋ"),
            ("2022-09-11", "እንቁጣጣሽ"),
            ("2022-09-27", "መስቀል"),
            ("2022-10-08", "መውሊድ"),
        )
