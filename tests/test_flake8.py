# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import os
import unittest
from glob import glob

from flake8.api import legacy as flake8


class TestFlake8(unittest.TestCase):

    def test_flake8(self):
        """Test that we conform to PEP-8."""
        self.style_guide = flake8.get_style_guide(ignore=['I', 'F401', 'W504'])
        self.py_files = [y for x in os.walk(os.path.abspath('holidays')) for y in glob(os.path.join(x[0], '*.py'))]
        self.report = self.style_guide.check_files(self.py_files)
        self.assertEqual(self.report.get_statistics('E'), [])
