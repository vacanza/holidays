#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import datetime

from holidays.utils import _AstroMeeusAlgorithms


class TestMeeus(unittest.TestCase):
    def setUp(self):
        self.meeus = _AstroMeeusAlgorithms()

    def test_jd2date(self):
        self.assertEqual(self.meeus.jd2date(2299161.5), datetime(1582, 10, 16))
        self.assertEqual(self.meeus.jd2date(2299159.5), datetime(1582, 10, 4))
        self.assertEqual(
            self.meeus.jd2date(2459929.187962963),
            datetime(2022, 12, 15, 16, 30, 40),
        )
        for mon, jd in enumerate(
            (
                2459580.5,
                2459611.5,
                2459639.5,
                2459670.5,
                2459700.5,
                2459731.5,
                2459761.5,
                2459792.5,
                2459823.5,
                2459853.5,
                2459884.5,
                2459914.5,
            ),
            1,
        ):
            self.assertEqual(self.meeus.jd2date(jd), datetime(2022, mon, 1))

    def test_spring(self):
        for year, jd in (
            (1900, 2415099.568834656),
            (1999, 2451258.574303147),
            (2000, 2451623.8169943923),
            (2022, 2459659.1489671636),
            (2100, 2488148.04620865),
        ):
            self.assertEqual(self.meeus.spring(year), jd)

    def test_summer(self):
        for year, jd in (
            (1900, 2415192.402799466),
            (1999, 2451351.3265471067),
            (2000, 2451716.5755480495),
            (2022, 2459751.885369888),
            (2100, 2488240.732588952),
        ):
            self.assertEqual(self.meeus.summer(year), jd)

    def test_autumn(self):
        for year, jd in (
            (1900, 2415286.014353473),
            (1999, 2451444.9809955703),
            (2000, 2451810.2284056335),
            (2022, 2459845.545352313),
            (2100, 2488334.4188107965),
        ):
            self.assertEqual(self.meeus.autumn(year), jd)

    def test_winter(self):
        for year, jd in (
            (1900, 2415375.778977786),
            (1999, 2451534.823134119),
            (2000, 2451900.068568985),
            (2022, 2459935.409147782),
            (2100, 2488424.3291470846),
        ):
            self.assertEqual(self.meeus.winter(year), jd)
