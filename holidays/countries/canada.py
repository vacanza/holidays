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
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, FR, SU

from holidays.constants import (
    FRI,
    SUN,
    WEEKEND,
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
        HolidayBase.__init__(self, locale_filename="canada", **kwargs)

    @staticmethod
    def _get_nearest_monday(d: date) -> date:
        if d.weekday() < FRI:
            return d + rd(weekday=MO(-1))
        else:
            return d + rd(weekday=MO)

    def _populate(self, year):
        super()._populate(year)

        if year < 1867:
            return

        # New Year's Day
        name = self.translate("New Year's Day")
        self[date(year, JAN, 1)] = name
        if self.observed and date(year, JAN, 1).weekday() == SUN:
            self[date(year, JAN, 1) + rd(days=+1)] = f"{name} {self.translate('(Observed)')}"
        # The following year's observed New Year's Day can be in this year
        # when it falls on a Friday (Jan 1st is a Saturday).
        if self.observed and date(year, DEC, 31).weekday() == FRI:
            self[date(year, DEC, 31)] = f"{name} {self.translate('(Observed)')}"

        # Family Day / Louis Riel Day (MB) / Islander Day (PE)
        # / Heritage Day (NS, YT)
        if (
            (self.subdiv == "AB" and year >= 1990)
            or (self.subdiv == "SK" and year >= 2007)
            or (self.subdiv == "ON" and year >= 2008)
            or (self.subdiv == "NB" and year >= 2018)
        ):
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self.translate("Family Day")
        elif self.subdiv == "BC":
            if 2013 <= year <= 2018:
                self[date(year, FEB, 1) + rd(weekday=MO(+2))] = self.translate("Family Day")
            elif year > 2018:
                self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self.translate("Family Day")
        elif self.subdiv == "MB" and year >= 2008:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self.translate("Louis Riel Day")
        elif self.subdiv == "PE" and year >= 2010:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self.translate("Islander Day")
        elif self.subdiv == "PE" and year == 2009:
            self[date(year, FEB, 1) + rd(weekday=MO(+2))] = self.translate("Islander Day")
        elif self.subdiv == "NS" and year >= 2015:
            # http://novascotia.ca/lae/employmentrights/NovaScotiaHeritageDay.asp
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self.translate("Heritage Day")
        elif self.subdiv == "YT" and year >= 1974:
            # start date?
            # https://www.britannica.com/topic/Heritage-Day-Canadian-holiday
            # Heritage Day was created in 1973
            # by the Heritage Canada Foundation
            # therefore, start date is not earlier than 1974
            # http://heritageyukon.ca/programs/heritage-day
            # https://en.wikipedia.org/wiki/Family_Day_(Canada)#Yukon_Heritage_Day
            # Friday before the last Sunday in February
            dt = (
                date(year, MAR, 1)
                + rd(days=-1)
                + rd(weekday=SU(-1))
                + rd(days=-2)
            )
            self[dt] = self.translate("Heritage Day")

        # St. Patrick's Day
        if self.subdiv == "NL" and year >= 1900:
            # Nearest Monday to March 17
            dt = self._get_nearest_monday(date(year, MAR, 17))
            self[dt] = self.translate("St. Patrick's Day")

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = self.translate("Good Friday")
        # Easter Monday
        self[easter(year) + rd(weekday=MO)] = self.translate("Easter Monday")

        # St. George's Day
        if self.subdiv == "NL" and year >= 1990:
            if year == 2010:
                # 4/26 is the Monday closer to 4/23 in 2010
                # but the holiday was observed on 4/19? Crazy Newfies!
                dt = date(2010, APR, 19)
            else:
                # Nearest Monday to April 23
                dt = self._get_nearest_monday(date(year, APR, 23))
            self[dt] = self.translate("St. George's Day")

        # Victoria Day / National Patriots' Day (QC)
        if year >= 1953:
            dt = date(year, MAY, 24) + rd(weekday=MO(-1))
            if self.subdiv not in {"NB", "NS", "PE", "NL", "QC"}:
                self[dt] = self.translate("Victoria Day")
            elif self.subdiv == "QC":
                self[dt] = self.translate("National Patriots' Day")

        # National Aboriginal Day
        if self.subdiv == "NT" and year >= 1996:
            self[date(year, JUN, 21)] = self.translate("National Aboriginal Day")

        # St. Jean Baptiste Day
        if self.subdiv == "QC" and year >= 1925:
            name = self.translate("St. Jean Baptiste Day")
            dt = date(year, JUN, 24)
            self[dt] = name
            if self.observed and dt.weekday() == SUN:
                self[dt + rd(days=1)] = f"{name} {self.translate('(Observed)')}"

        # Discovery Day
        if self.subdiv == "NL" and year >= 1997:
            # Nearest Monday to June 24
            dt = self._get_nearest_monday(date(year, JUN, 24))
            self[dt] = self.translate("Discovery Day")
        elif self.subdiv == "YT" and year >= 1912:
            self[date(year, AUG, 1) + rd(weekday=MO(+3))] = self.translate("Discovery Day")

        # Canada Day / Memorial Day (NL)
        if year >= 1983:
            name = self.translate("Memorial Day") if self.subdiv == "NL" else self.translate("Canada Day")
        else:
            name = self.translate("Dominion Day")
        dt = date(year, JUL, 1)
        self[dt] = name
        if year >= 1879 and self.observed and dt.weekday() in WEEKEND:
            self[dt + rd(weekday=MO)] = f"{name} {self.translate('(Observed)')}"

        # Nunavut Day
        if self.subdiv == "NU":
            name = self.translate("Nunavut Day")
            if year >= 2001:
                dt = date(year, JUL, 9)
                self[dt] = name
                if self.observed and dt.weekday() == SUN:
                    self[dt + rd(days=1)] = f"{name} {self.translate('(Observed)')}"
            elif year == 2000:
                self[date(2000, APR, 1)] = name

        # Civic Holiday
        if year >= 1900 and self.subdiv in {"MB", "NT", "ON"}:
            self[date(year, AUG, 1) + rd(weekday=MO)] = self.translate("Civic Holiday")
        elif year >= 1974 and self.subdiv == "AB":
            # https://en.wikipedia.org/wiki/Civic_Holiday#Alberta
            self[date(year, AUG, 1) + rd(weekday=MO)] = self.translate("Heritage Day")
        elif year >= 1974 and self.subdiv == "BC":
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = self.translate("British Columbia Day")
        elif year >= 1900 and self.subdiv == "NB":
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = self.translate("New Brunswick Day")
        elif year >= 1900 and self.subdiv == "SK":
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = self.translate("Saskatchewan Day")

        # Labour Day
        if year >= 1894:
            self[date(year, SEP, 1) + rd(weekday=MO)] = self.translate("Labour Day")

        # Funeral of Queen Elizabeth II
        # https://www.narcity.com/provinces-territories-will-have-a-day-off-monday-mourn-queen
        # TODO: the territories holiday status (NT, NU, YT) is still tentative
        if year == 2022 and self.subdiv in {
            "BC",
            "NB",
            "NL",
            "NS",
            "PE",
            "YT",
        }:
            self[
                date(2022, SEP, 19)
            ] = self.translate("Funeral of Her Majesty the Queen Elizabeth II")

        # National Day for Truth and Reconciliation
        if year >= 2021 and self.subdiv in {"MB", "NS"}:
            self[
                date(year, SEP, 30)
            ] = self.translate("National Day for Truth and Reconciliation")

        # Thanksgiving
        if year >= 1931 and self.subdiv not in {"NB", "NL", "NS", "PE"}:
            if year == 1935:
                # in 1935, Canadian Thanksgiving was moved due to the General
                # Election falling on the second Monday of October
                # https://books.google.ca/books?id=KcwlQsmheG4C&pg=RA1-PA1940&lpg=RA1-PA1940&dq=canada+thanksgiving+1935&source=bl&ots=j4qYrcfGuY&sig=gxXeAQfXVsOF9fOwjSMswPHJPpM&hl=en&sa=X&ved=0ahUKEwjO0f3J2PjOAhVS4mMKHRzKBLAQ6AEIRDAG#v=onepage&q=canada%20thanksgiving%201935&f=false
                self[date(1935, OCT, 25)] = self.translate("Thanksgiving")
            else:
                self[date(year, OCT, 1) + rd(weekday=MO(+2))] = self.translate("Thanksgiving")

        # Remembrance Day
        if year >= 1931 and self.subdiv not in {"ON", "QC"}:
            name = self.translate("Remembrance Day")
            dt = date(year, NOV, 11)
            self[dt] = name
            if (
                self.observed
                and dt.weekday() == SUN
                and self.subdiv in {"NS", "NL", "NT", "PE", "SK"}
            ):
                self[dt + rd(weekday=MO)] = f"{name} {self.translate('(Observed)')}"

        # Christmas Day
        name = self.translate("Christmas Day")
        dt = date(year, DEC, 25)
        self[dt] = name
        if self.observed and dt.weekday() in WEEKEND:
            self[dt + rd(days=2)] = f"{name} {self.translate('(Observed)')}"

        # Boxing Day
        name = self.translate("Boxing Day")
        dt = date(year, DEC, 26)
        self[dt] = name
        if self.observed and dt.weekday() in WEEKEND:
            self[dt + rd(days=2)] = f"{name} {self.translate('(Observed)')}"


class CA(Canada):
    pass


class CAN(Canada):
    pass
