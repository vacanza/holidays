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

from holidays.entities.ISO_3166.TL import TlHolidays
from tests.common import CommonCountryTests


class TestTlHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TlHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "National Holidays (Special)"),
            ("2023-01-23", "National Holidays (Special)"),
            ("2023-02-22", "Ash Wednesday; National Holidays (Special)"),
            ("2023-03-03", "Veteran's Day"),
            ("2023-04-06", "Holy Thursday"),
            ("2023-04-07", "Holy Friday"),
            ("2023-04-22", "Idul Fitri"),
            ("2023-05-01", "World Labor Day"),
            ("2023-05-18", "The Day of Ascension of Jesus Christ into Heaven"),
            ("2023-05-20", "Restoration of Independence Day"),
            ("2023-06-01", "World Children's Day"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-29", "Idul Adha"),
            (
                "2023-08-20",
                "Day of the Armed Forces for the National Liberation of Timor-Leste (FALINTIL)",
            ),
            ("2023-08-30", "Popular Consultation Day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-11-02", "All Souls' Day"),
            ("2023-11-03", "National Women's Day"),
            ("2023-11-12", "National Youth Day"),
            ("2023-11-28", "Proclamation of Independence Day"),
            ("2023-12-07", "Memorial Day"),
            ("2023-12-08", "Day of Our Lady of Immaculate Conception and Timor-Leste Patroness"),
            ("2023-12-10", "World Human Rights Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-31", "National Heroes Day"),
        )
