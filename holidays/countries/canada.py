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

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO, SU, FR

from holidays.constants import FRI, SAT, SUN, WEEKEND
from holidays.constants import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.holiday_base import HolidayBase


class Canada(HolidayBase):
    country = "CA"
    subdivisions = [
        "AB",
        "BC",
        "MB",
        "NB",
        "NL",
        "NS",
        "NT",
        "NU",
        "ON",
        "PE",
        "QC",
        "SK",
        "YT",
    ]

    def __init__(self, **kwargs):
        # Default subdivision to ON; prov for backwards compatibility
        if not kwargs.get("subdiv", kwargs.get("prov")):
            kwargs["subdiv"] = "ON"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if year >= 1867:
            name = "New Year's Day"
            self[date(year, JAN, 1)] = name
            if self.observed and date(year, JAN, 1).weekday() == SUN:
                self[date(year, JAN, 1) + rd(days=+1)] = name + " (Observed)"
            # The following year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday).
            if self.observed and date(year, DEC, 31).weekday() == FRI:
                self[date(year, DEC, 31)] = name + " (Observed)"

        # Family Day / Louis Riel Day (MB) / Islander Day (PE)
        # / Heritage Day (NS, YT)
        if self.subdiv in ("AB", "SK", "ON") and year >= 2008:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.subdiv in ("AB", "SK") and year >= 2007:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.subdiv == "AB" and year >= 1990:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.subdiv == "NB" and year >= 2018:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.subdiv == "BC":
            if 2013 <= year <= 2018:
                self[date(year, FEB, 1) + rd(weekday=MO(+2))] = "Family Day"
            elif year > 2018:
                self[date(year, FEB, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.subdiv == "MB" and year >= 2008:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = "Louis Riel Day"
        elif self.subdiv == "PE" and year >= 2010:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = "Islander Day"
        elif self.subdiv == "PE" and year == 2009:
            self[date(year, FEB, 1) + rd(weekday=MO(+2))] = "Islander Day"
        elif self.subdiv == "NS" and year >= 2015:
            # http://novascotia.ca/lae/employmentrights/NovaScotiaHeritageDay.asp
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = "Heritage Day"
        elif self.subdiv == "YT":
            # start date?
            # http://heritageyukon.ca/programs/heritage-day
            # https://en.wikipedia.org/wiki/Family_Day_(Canada)#Yukon_Heritage_Day
            # Friday before the last Sunday in February
            dt = date(year, MAR, 1) + rd(weekday=SU(-1)) + rd(weekday=FR(-1))
            self[dt] = "Heritage Day"

        # St. Patrick's Day
        if self.subdiv == "NL" and year >= 1900:
            dt = date(year, MAR, 17)
            # Nearest Monday to March 17
            dt1 = date(year, MAR, 17) + rd(weekday=MO(-1))
            dt2 = date(year, MAR, 17) + rd(weekday=MO(+1))
            if dt2 - dt <= dt - dt1:
                self[dt2] = "St. Patrick's Day"
            else:
                self[dt1] = "St. Patrick's Day"

        if year >= 1867:
            # Good Friday
            self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"
            # Easter Monday
            self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # St. George's Day
        if self.subdiv == "NL" and year == 2010:
            # 4/26 is the Monday closer to 4/23 in 2010
            # but the holiday was observed on 4/19? Crazy Newfies!
            self[date(2010, 4, 19)] = "St. George's Day"
        elif self.subdiv == "NL" and year >= 1990:
            dt = date(year, APR, 23)
            # Nearest Monday to April 23
            dt1 = dt + rd(weekday=MO(-1))
            dt2 = dt + rd(weekday=MO(+1))
            if dt2 - dt < dt - dt1:
                self[dt2] = "St. George's Day"
            else:
                self[dt1] = "St. George's Day"

        # Victoria Day / National Patriots' Day (QC)
        if self.subdiv not in ("NB", "NS", "PE", "NL", "QC") and year >= 1953:
            self[date(year, MAY, 24) + rd(weekday=MO(-1))] = "Victoria Day"
        elif self.subdiv == "QC" and year >= 1953:
            name = "National Patriots' Day"
            self[date(year, MAY, 24) + rd(weekday=MO(-1))] = name

        # National Aboriginal Day
        if self.subdiv == "NT" and year >= 1996:
            self[date(year, JUN, 21)] = "National Aboriginal Day"

        # St. Jean Baptiste Day
        if self.subdiv == "QC" and year >= 1925:
            self[date(year, JUN, 24)] = "St. Jean Baptiste Day"
            if self.observed and date(year, JUN, 24).weekday() == SUN:
                self[date(year, JUN, 25)] = "St. Jean Baptiste Day (Observed)"

        # Discovery Day
        if self.subdiv == "NL" and year >= 1997:
            dt = date(year, JUN, 24)
            # Nearest Monday to June 24
            dt1 = dt + rd(weekday=MO(-1))
            dt2 = dt + rd(weekday=MO(+1))
            if dt2 - dt <= dt - dt1:
                self[dt2] = "Discovery Day"
            else:
                self[dt1] = "Discovery Day"
        elif self.subdiv == "YT" and year >= 1912:
            self[date(year, AUG, 1) + rd(weekday=MO(+3))] = "Discovery Day"

        # Canada Day / Memorial Day (NL)
        if self.subdiv != "NL" and year >= 1867:
            if year >= 1983:
                name = "Canada Day"
            else:
                name = "Dominion Day"
            self[date(year, JUL, 1)] = name
            if (
                year >= 1879
                and self.observed
                and date(year, JUL, 1).weekday() in WEEKEND
            ):
                self[date(year, JUL, 1) + rd(weekday=MO)] = (
                    name + " (Observed)"
                )
        elif year >= 1867:
            if year >= 1983:
                name = "Memorial Day"
            else:
                name = "Dominion Day"
            self[date(year, JUL, 1)] = name
            if (
                year >= 1879
                and self.observed
                and date(year, JUL, 1).weekday() in WEEKEND
            ):
                self[date(year, JUL, 1) + rd(weekday=MO)] = (
                    name + " (Observed)"
                )

        # Nunavut Day
        if self.subdiv == "NU" and year >= 2001:
            self[date(year, JUL, 9)] = "Nunavut Day"
            if self.observed and date(year, JUL, 9).weekday() == SUN:
                self[date(year, JUL, 10)] = "Nunavut Day (Observed)"
        elif self.subdiv == "NU" and year == 2000:
            self[date(2000, 4, 1)] = "Nunavut Day"

        # Civic Holiday
        if self.subdiv in ("ON", "MB", "NT") and year >= 1900:
            self[date(year, AUG, 1) + rd(weekday=MO)] = "Civic Holiday"
        elif self.subdiv == "AB" and year >= 1974:
            # https://en.wikipedia.org/wiki/Civic_Holiday#Alberta
            self[date(year, AUG, 1) + rd(weekday=MO)] = "Heritage Day"
        elif self.subdiv == "BC" and year >= 1974:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = "British Columbia Day"
        elif self.subdiv == "NB" and year >= 1900:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = "New Brunswick Day"
        elif self.subdiv == "SK" and year >= 1900:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = "Saskatchewan Day"

        # Labour Day
        if year >= 1894:
            self[date(year, SEP, 1) + rd(weekday=MO)] = "Labour Day"

        # Funeral of Queen Elizabeth II
        # https://www.narcity.com/provinces-territories-will-have-a-day-off-monday-mourn-queen
        # TODO: the territories holiday status (NT, NU, YT) is still tentative
        queen_funeral_observers = ("BC", "NB", "NL", "NS", "PE", "YT")
        if self.subdiv in queen_funeral_observers and year == 2022:
            self[
                date(year, SEP, 19)
            ] = "Funeral of Her Majesty the Queen Elizabeth II"

        # National Day for Truth and Reconciliation
        if self.subdiv in ("MB", "NS") and year >= 2021:
            self[
                date(year, SEP, 30)
            ] = "National Day for Truth and Reconciliation"

        # Thanksgiving
        if self.subdiv not in ("NB", "NS", "PE", "NL") and year >= 1931:
            if year == 1935:
                # in 1935, Canadian Thanksgiving was moved due to the General
                # Election falling on the second Monday of October
                # https://books.google.ca/books?id=KcwlQsmheG4C&pg=RA1-PA1940&lpg=RA1-PA1940&dq=canada+thanksgiving+1935&source=bl&ots=j4qYrcfGuY&sig=gxXeAQfXVsOF9fOwjSMswPHJPpM&hl=en&sa=X&ved=0ahUKEwjO0f3J2PjOAhVS4mMKHRzKBLAQ6AEIRDAG#v=onepage&q=canada%20thanksgiving%201935&f=false
                self[date(1935, 10, 25)] = "Thanksgiving"
            else:
                self[date(year, OCT, 1) + rd(weekday=MO(+2))] = "Thanksgiving"

        # Remembrance Day
        name = "Remembrance Day"
        if (
            self.subdiv not in ("ON", "QC", "NS", "NL", "NT", "PE", "SK")
            and year >= 1931
        ):
            self[date(year, NOV, 11)] = name
        elif self.subdiv in ("NS", "NL", "NT", "PE", "SK") and year >= 1931:
            self[date(year, NOV, 11)] = name
            if self.observed and date(year, NOV, 11).weekday() == SUN:
                name = name + " (Observed)"
                self[date(year, NOV, 11) + rd(weekday=MO)] = name

        # Christmas Day
        if year >= 1867:
            name = "Christmas Day"
            name_observed = name + " (Observed)"
            if self.observed and date(year, DEC, 25).weekday() in WEEKEND:
                self[date(year, DEC, 27)] = name_observed
            else:
                self[date(year, DEC, 25)] = name

        # Boxing Day
        if year >= 1867:
            name = "Boxing Day"
            name_observed = name + " (Observed)"
            if self.observed and date(year, DEC, 26).weekday() in WEEKEND:
                self[date(year, DEC, 28)] = name_observed
            else:
                self[date(year, DEC, 26)] = name


class CA(Canada):
    pass


class CAN(Canada):
    pass
