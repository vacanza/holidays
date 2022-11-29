from dateutil.parser import parse
from dateutil.relativedelta import SU


class SundayHolidays:
    """Common class to test countries with Sundays as a holidays."""

    def test_sundays(self, cls):
        h = cls(years=1989, include_sundays=True)
        self.assertIn("1989-12-31", h)
        self.assertEqual(53, len([s for s in h if s.weekday() == SU.weekday]))

        h = cls(years=2032, include_sundays=True)
        self.assertIn("2032-01-04", h)
        self.assertEqual(52, len([s for s in h if s.weekday() == SU.weekday]))

        h = cls(include_sundays=True)
        self.assertEqual(0, len(h))

        for sunday in ("1989-12-31", "2017-02-05", "2017-02-12", "2032-02-29"):
            self.assertEqual(parse(sunday).weekday(), SU.weekday)
            self.assertIn(sunday, h)

        for non_sunday in (
            "2001-05-16",
            "2001-05-18",
            "2016-12-27",
            "2016-12-28",
            "2017-02-06",
            "2017-02-07",
            "2017-02-08",
            "2017-02-09",
            "2017-02-10",
        ):
            self.assertNotEqual(parse(non_sunday).weekday(), SU.weekday)
            self.assertNotIn(non_sunday, h)
