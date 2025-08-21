#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import sys

if sys.version_info >= (3, 10):
    from importlib.metadata import metadata
else:
    from importlib_metadata import metadata

from unittest import TestCase

import holidays


class TestPackage(TestCase):
    def test_metadata(self):
        ph_metadata = metadata("holidays")

        for attr_name, attr_value in {
            "name": "holidays",
            "summary": "Open World Holidays Framework",
            "version": holidays.__version__,
        }.items():
            with self.subTest(attr=attr_name):
                self.assertIn(attr_name, ph_metadata)
                self.assertEqual(
                    ph_metadata[attr_name],
                    attr_value,
                    msg="You may need to run `make package` to update the metadata."
                    if attr_name == "version"
                    else None,
                )

        for attr_name in (
            "classifier",
            "description",
            "keywords",
            "license-expression",
            "license-file",
            "maintainer",
            "project-url",
            "requires-python",
        ):
            self.assertIn(attr_name, ph_metadata)
            self.assertTrue(ph_metadata[attr_name], attr_name)

            if attr_name == "maintainer":
                for maintainer in ("Arkadii Yakovets", "Panpakorn Siripanich", "Serhii Murza"):
                    self.assertIn(maintainer, ph_metadata["maintainer"])
