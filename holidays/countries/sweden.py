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
from dateutil.relativedelta import FR, SA, SU
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, MAY, JUN, OCT, DEC
from holidays.holiday_base import HolidayBase


class Sweden(HolidayBase):
    """
    Swedish holidays.
    Note that holidays falling on a sunday are "lost",
    it will not be moved to another day to make up for the collision.
    In Sweden, ALL sundays are considered a holiday
    (https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige).
    Initialize this class with include_sundays=False
    to not include sundays as a holiday.
    Primary sources:
    https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige and
    http://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-1989253-om-allmanna-helgdagar_sfs-1989-253
    """

    country = "SE"

    def __init__(self, include_sundays=True, **kwargs):
        """
        :param include_sundays: Whether to consider sundays as a holiday
        (which they are in Sweden)
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
                self[sunday.date()] = "Söndag"

        # ========= Static holidays =========
        self[date(year, JAN, 1)] = "Nyårsdagen"

        self[date(year, JAN, 6)] = "Trettondedag jul"

        # Source: https://sv.wikipedia.org/wiki/F%C3%B6rsta_maj
        if year >= 1939:
            self[date(year, MAY, 1)] = "Första maj"

        # Source: https://sv.wikipedia.org/wiki/Sveriges_nationaldag
        if year >= 2005:
            self[date(year, JUN, 6)] = "Sveriges nationaldag"

        self[date(year, DEC, 24)] = "Julafton"
        self[date(year, DEC, 25)] = "Juldagen"
        self[date(year, DEC, 26)] = "Annandag jul"
        self[date(year, DEC, 31)] = "Nyårsafton"

        # ========= Moving holidays =========
        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Långfredagen"
        self[easter_date] = "Påskdagen"
        self[easter_date + rd(days=+1)] = "Annandag påsk"
        self[easter_date + rd(days=+39)] = "Kristi himmelsfärdsdag"
        self[easter_date + rd(days=+49)] = "Pingstdagen"
        if year <= 2004:
            self[easter_date + rd(days=+50)] = "Annandag pingst"

        # Source:
        # https://sv.wikipedia.org/wiki/Midsommarafton
        # https://www.nordiskamuseet.se/aretsdagar/midsommarafton
        if year >= 1953:
            # Midsummer evening. Friday between June 19th and June 25th
            self[date(year, JUN, 19) + rd(weekday=FR)] = "Midsommarafton"
            # Midsummer day. Saturday between June 20th and June 26th
            self[date(year, JUN, 20) + rd(weekday=SA)] = "Midsommardagen"
        else:
            self[date(year, JUN, 23)] = "Midsommarafton"
            self[date(year, JUN, 24)] = "Midsommardagen"

        # All saints day. Saturday between October 31th and November 6th
        self[date(year, OCT, 31) + rd(weekday=SA)] = "Alla helgons dag"

        if year <= 1953:
            self[date(year, MAR, 25)] = "Jungfru Marie bebådelsedag"


class SE(Sweden):
    pass


class SWE(Sweden):
    pass
