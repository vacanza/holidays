#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date, datetime

from dateutil import rrule
from dateutil.easter import easter
from dateutil.relativedelta import SU
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, DEC
from holidays.holiday_base import HolidayBase


class Norway(HolidayBase):
    """
    Norwegian holidays.
    Note that holidays falling on a sunday is "lost",
    it will not be moved to another day to make up for the collision.

    In Norway, ALL sundays are considered a holiday (https://snl.no/helligdag).
    Initialize this class with include_sundays=False
    to not include sundays as a holiday.

    Primary sources:
    https://lovdata.no/dokument/NL/lov/1947-04-26-1
    https://no.wikipedia.org/wiki/Helligdager_i_Norge
    https://www.timeanddate.no/merkedag/norge/
    """

    country = "NO"

    def __init__(self, include_sundays=False, **kwargs):
        """

        :param include_sundays: Whether to consider sundays as a holiday
        (which they are in Norway)
        :param kwargs:
        """
        self.include_sundays = include_sundays
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        if self.include_sundays:  # Optionally add all Sundays of the year.
            year_first_day = datetime(year, JAN, 1)
            year_last_day = datetime(year, DEC, 31)

            # Get all Sundays including first/last day of the year cases.
            sundays = rrule.rrule(
                rrule.WEEKLY, byweekday=SU, dtstart=year_first_day
            ).between(year_first_day, year_last_day, inc=True)
            for sunday in sundays:
                self[sunday.date()] = "Søndag"

        # ========= Static holidays =========
        self[date(year, JAN, 1)] = "Første nyttårsdag"

        # Source: https://lovdata.no/dokument/NL/lov/1947-04-26-1
        if year >= 1947:
            self[date(year, MAY, 1)] = "Arbeidernes dag"
            self[date(year, MAY, 17)] = "Grunnlovsdag"

        # According to https://no.wikipedia.org/wiki/F%C3%B8rste_juledag,
        # these dates are only valid from year > 1700
        # Wikipedia has no source for the statement, so leaving this be for now
        self[date(year, DEC, 25)] = "Første juledag"
        self[date(year, DEC, 26)] = "Andre juledag"

        # ========= Moving holidays =========
        # NOTE: These are probably subject to the same > 1700
        # restriction as the above dates. The only source I could find for how
        # long Easter has been celebrated in Norway was
        # https://www.hf.uio.no/ikos/tjenester/kunnskap/samlinger/norsk-folkeminnesamling/livs-og-arshoytider/paske.html
        # which says
        # "(...) has been celebrated for over 1000 years (...)" (in Norway)

        easter_date = easter(year)
        self[easter_date + rd(days=-3)] = "Skjærtorsdag"
        self[easter_date + rd(days=-2)] = "Langfredag"
        self[easter_date] = "Første påskedag"
        self[easter_date + rd(days=+1)] = "Andre påskedag"
        self[easter_date + rd(days=+39)] = "Kristi himmelfartsdag"
        self[easter_date + rd(days=+49)] = "Første pinsedag"
        self[easter_date + rd(days=+50)] = "Andre pinsedag"


class NO(Norway):
    pass


class NOR(Norway):
    pass
