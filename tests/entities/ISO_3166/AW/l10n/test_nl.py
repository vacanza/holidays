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

from holidays.entities.ISO_3166.AW import AwHolidays
from tests.common import CommonCountryTests


class TestAwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AwHolidays, language="nl")

    def test_nl(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Nieuwjaarsdag"),
            ("2023-01-25", "Beticodag"),
            ("2023-02-20", "Maandag voor Aswoensdag"),
            ("2023-03-18", "Nationale vlag en volkslied"),
            ("2023-04-07", "Goede vrijdag"),
            ("2023-04-10", "Tweede paasdag"),
            ("2023-04-27", "Koningsdag"),
            ("2023-05-01", "Dag van de arbeid"),
            ("2023-05-18", "Hemelvaartsdag"),
            ("2023-12-25", "Kerst"),
            ("2023-12-26", "Tweede kerstdag"),
        )
