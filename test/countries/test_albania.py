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

from holidays.countries.albania import AL, ALB, Albania
from test.common import TestCase


class TestAlbania(TestCase):
    def setUp(self):
        self.holidays = Albania()

    def test_country_aliases(self):
        self.assertCountryAliases(Albania, AL, ALB)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-03", "New Year's Day (Observed)"),
            ("2022-01-04", "New Year's Day (Observed)"),
            ("2022-03-14", "Summer Day"),
            ("2022-03-22", "Nevruz"),
            ("2022-04-17", "Catholic Easter"),
            ("2022-04-18", "Catholic Easter (Observed)"),
            ("2022-04-24", "Orthodox Easter"),
            ("2022-04-25", "Orthodox Easter (Observed)"),
            ("2022-05-01", "May Day"),
            ("2022-05-02", "Eid al-Fitr* (*estimated), May Day (Observed)"),
            ("2022-07-09", "Eid al-Adha* (*estimated)"),
            ("2022-07-11", "Eid al-Adha* (*estimated) (Observed)"),
            ("2022-09-05", "Mother Teresa Day"),
            ("2022-11-28", "Independence Day"),
            ("2022-11-29", "Liberation Day"),
            ("2022-12-08", "National Youth Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (Observed)"),
        )

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day, New Year's Day (Observed)"),
            ("2023-03-14", "Summer Day"),
            ("2023-03-22", "Nevruz"),
            ("2023-04-09", "Catholic Easter"),
            ("2023-04-10", "Catholic Easter (Observed)"),
            ("2023-04-16", "Orthodox Easter"),
            ("2023-04-17", "Orthodox Easter (Observed)"),
            ("2023-04-21", "Eid al-Fitr* (*estimated)"),
            ("2023-05-01", "May Day"),
            ("2023-06-28", "Eid al-Adha* (*estimated)"),
            ("2023-09-05", "Mother Teresa Day"),
            ("2023-11-28", "Independence Day"),
            ("2023-11-29", "Liberation Day"),
            ("2023-12-08", "National Youth Day"),
            ("2023-12-25", "Christmas Day"),
        )
