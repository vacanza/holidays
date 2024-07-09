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

from holidays.entities.ISO_3166.IL import IlHolidays
from tests.common import CommonCountryTests


class TestIlHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IlHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2021-02-25", "Ta'anit Ester"),
            ("2021-02-26", "Purim"),
            ("2021-03-28", "Pesach"),
            ("2021-03-29", "Pesach holiday"),
            ("2021-03-30", "Pesach holiday"),
            ("2021-03-31", "Pesach holiday"),
            ("2021-04-01", "Pesach holiday"),
            ("2021-04-02", "Pesach holiday"),
            ("2021-04-03", "Seventh day of Pesach"),
            ("2021-04-14", "Remembrance Day (observed)"),
            ("2021-04-15", "Independence Day (observed)"),
            ("2021-04-30", "Lag BaOmer"),
            ("2021-05-10", "Jerusalem Day"),
            ("2021-05-17", "Shavuot"),
            ("2021-07-18", "Tisha B'Av"),
            ("2021-09-07", "Rosh Hashanah"),
            ("2021-09-08", "Rosh Hashanah"),
            ("2021-09-16", "Yom Kippur"),
            ("2021-09-21", "Sukkot"),
            ("2021-09-22", "Sukkot holiday"),
            ("2021-09-23", "Sukkot holiday"),
            ("2021-09-24", "Sukkot holiday"),
            ("2021-09-25", "Sukkot holiday"),
            ("2021-09-26", "Sukkot holiday"),
            ("2021-09-28", "Simchat Torah / Shemini Atzeret"),
            ("2021-11-04", "Sigd"),
            ("2021-11-29", "Hanukkah"),
            ("2021-11-30", "Hanukkah"),
            ("2021-12-01", "Hanukkah"),
            ("2021-12-02", "Hanukkah"),
            ("2021-12-03", "Hanukkah"),
            ("2021-12-04", "Hanukkah"),
            ("2021-12-05", "Hanukkah"),
            ("2021-12-06", "Hanukkah"),
        )
