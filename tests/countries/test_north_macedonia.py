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

from holidays.countries.north_macedonia import NorthMacedonia, MK, MKD
from tests.common import CommonCountryTests


class TestNorthMacedonia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NorthMacedonia)

    def test_country_aliases(self):
        self.assertAliases(NorthMacedonia, MK, MKD)

    def test_2019(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_North_Macedonia
        self.assertHolidays(
            ("2019-01-01", "New Year's Day"),
            ("2019-01-07", "Christmas Day (Orthodox)"),
            ("2019-04-29", "Easter Monday (Orthodox)"),
            ("2019-05-01", "Labour Day"),
            ("2019-05-24", "Saints Cyril and Methodius Day"),
            ("2019-06-04", "Eid al-Fitr (estimated)"),
            ("2019-08-02", "Republic Day"),
            ("2019-09-08", "Independence Day"),
            ("2019-10-11", "Day of Macedonian Uprising in 1941"),
            ("2019-10-23", "Day of the Macedonian Revolutionary Struggle"),
            ("2019-12-08", "Saint Clement of Ohrid Day"),
        )
