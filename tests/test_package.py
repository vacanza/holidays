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

from importlib_metadata import metadata

import holidays


class TestPackage(TestCase):
    def test_metadata(self):
        ph_metadata = metadata("holidays")

        for attr_name, attr_value in {
            "name": "holidays",
            "summary": "Generate and work with holidays in Python",
            "version": holidays.__version__,
        }.items():
            self.assertIn(attr_name, ph_metadata)
            self.assertEqual(ph_metadata[attr_name], attr_value, attr_name)

        for attr_name in (
            "author-email",
            "classifier",
            "description",
            "keywords",
            "license",
            "license-file",
            "maintainer-email",
            "project-url",
            "requires-python",
        ):
            self.assertIn(attr_name, ph_metadata)
            self.assertTrue(ph_metadata[attr_name], attr_name)
