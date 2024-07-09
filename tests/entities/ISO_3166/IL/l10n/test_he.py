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
        super().setUpClass(IlHolidays)

    def test_he(self):
        self.assertLocalizedHolidays(
            ("2021-02-25", "תענית אסתר"),
            ("2021-02-26", "פורים"),
            ("2021-03-28", "פסח"),
            ("2021-03-29", "חול המועד פסח"),
            ("2021-03-30", "חול המועד פסח"),
            ("2021-03-31", "חול המועד פסח"),
            ("2021-04-01", "חול המועד פסח"),
            ("2021-04-02", "חול המועד פסח"),
            ("2021-04-03", "שביעי של פסח"),
            ("2021-04-14", "(נצפה) יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"),
            ("2021-04-15", "(נצפה) יום העצמאות"),
            ("2021-04-30", 'ל"ג בעומר'),
            ("2021-05-10", "יום ירושלים"),
            ("2021-05-17", "שבועות"),
            ("2021-07-18", "תשעה באב"),
            ("2021-09-07", "ראש השנה"),
            ("2021-09-08", "ראש השנה"),
            ("2021-09-16", "יום כיפור"),
            ("2021-09-21", "סוכות"),
            ("2021-09-22", "חול המועד סוכות"),
            ("2021-09-23", "חול המועד סוכות"),
            ("2021-09-24", "חול המועד סוכות"),
            ("2021-09-25", "חול המועד סוכות"),
            ("2021-09-26", "חול המועד סוכות"),
            ("2021-09-28", "שמחת תורה/שמיני עצרת"),
            ("2021-11-04", "סיגד"),
            ("2021-11-29", "חנוכה"),
            ("2021-11-30", "חנוכה"),
            ("2021-12-01", "חנוכה"),
            ("2021-12-02", "חנוכה"),
            ("2021-12-03", "חנוכה"),
            ("2021-12-04", "חנוכה"),
            ("2021-12-05", "חנוכה"),
            ("2021-12-06", "חנוכה"),
        )
