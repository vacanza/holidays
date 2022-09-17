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

from holidays.constants import FRI, SUN, WEEKEND
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
from holidays.utils import translate


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

    def _(self, key):
        return translate("canada", key, self.language)

    def _populate(self, year):
        # New Year's Day
        if year >= 1867:
            self[date(year, JAN, 1)] = self._("new_years_day")
            if self.observed and date(year, JAN, 1).weekday() == SUN:
                self[date(year, JAN, 1) + rd(days=+1)] = self._(
                    "new_years_day_observed"
                )
            # The following year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday).
            if self.observed and date(year, DEC, 31).weekday() == FRI:
                self[date(year, DEC, 31)] = self._("new_years_day_observed")

        # Family Day / Louis Riel Day (MB) / Islander Day (PE)
        # / Heritage Day (NS, YT)
        if self.subdiv in ("AB", "SK", "ON") and year >= 2008:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self._(
                "family_day"
            )
        elif self.subdiv in ("AB", "SK") and year >= 2007:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self._(
                "family_day"
            )
        elif self.subdiv == "AB" and year >= 1990:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self._(
                "family_day"
            )
        elif self.subdiv == "NB" and year >= 2018:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self._(
                "family_day"
            )
        elif self.subdiv == "BC":
            if 2013 <= year <= 2018:
                self[date(year, FEB, 1) + rd(weekday=MO(+2))] = self._(
                    "family_day"
                )
            elif year > 2018:
                self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self._(
                    "family_day"
                )
        elif self.subdiv == "MB" and year >= 2008:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self._(
                "louis_riel_day"
            )
        elif self.subdiv == "PE" and year >= 2010:
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self._(
                "islander_day"
            )
        elif self.subdiv == "PE" and year == 2009:
            self[date(year, FEB, 1) + rd(weekday=MO(+2))] = self._(
                "islander_day"
            )
        elif self.subdiv == "NS" and year >= 2015:
            # http://novascotia.ca/lae/employmentrights/NovaScotiaHeritageDay.asp
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = self._(
                "heritage_day"
            )
        elif self.subdiv == "YT":
            # start date?
            # http://heritageyukon.ca/programs/heritage-day
            # https://en.wikipedia.org/wiki/Family_Day_(Canada)#Yukon_Heritage_Day
            # Friday before the last Sunday in February
            dt = date(year, MAR, 1) + rd(weekday=SU(-1)) + rd(weekday=FR(-1))
            self[dt] = self._(
                "heritage_day"
            )

        # St. Patrick's Day
        if self.subdiv == "NL" and year >= 1900:
            dt = date(year, MAR, 17)
            # Nearest Monday to March 17
            dt1 = date(year, MAR, 17) + rd(weekday=MO(-1))
            dt2 = date(year, MAR, 17) + rd(weekday=MO(+1))
            if dt2 - dt <= dt - dt1:
                self[dt2] = self._("st_patricks_day")
            else:
                self[dt1] = self._("st_patricks_day")

        if year >= 1867:
            # Good Friday
            self[easter(year) + rd(weekday=FR(-1))] = self._("good_friday")
            # Easter Monday
            self[easter(year) + rd(weekday=MO)] = self._("easter_monday")

        # St. George's Day
        if self.subdiv == "NL" and year == 2010:
            # 4/26 is the Monday closer to 4/23 in 2010
            # but the holiday was observed on 4/19? Crazy Newfies!
            self[date(2010, 4, 19)] = self._("st_georges_day")
        elif self.subdiv == "NL" and year >= 1990:
            dt = date(year, APR, 23)
            # Nearest Monday to April 23
            dt1 = dt + rd(weekday=MO(-1))
            dt2 = dt + rd(weekday=MO(+1))
            if dt2 - dt < dt - dt1:
                self[dt2] = self._("st_georges_day")
            else:
                self[dt1] = self._("st_georges_day")

        # Victoria Day / National Patriots' Day (QC)
        if self.subdiv not in ("NB", "NS", "PE", "NL", "QC") and year >= 1953:
            self[date(year, MAY, 24) + rd(weekday=MO(-1))] = self._(
                "victoria_day"
            )
        elif self.subdiv == "QC" and year >= 1953:
            name = self._("national_patriots_day")
            self[date(year, MAY, 24) + rd(weekday=MO(-1))] = name

        # National Aboriginal Day
        if self.subdiv == "NT" and year >= 1996:
            self[date(year, JUN, 21)] = self._("national_aboriginal_day")

        # St. Jean Baptiste Day
        if self.subdiv == "QC" and year >= 1925:
            self[date(year, JUN, 24)] = self._("st_jean_baptiste_day")
            if self.observed and date(year, JUN, 24).weekday() == SUN:
                self[date(year, JUN, 25)] = self._(
                    "st_jean_baptiste_day_observed"
                )

        # Discovery Day
        if self.subdiv == "NL" and year >= 1997:
            dt = date(year, JUN, 24)
            # Nearest Monday to June 24
            dt1 = dt + rd(weekday=MO(-1))
            dt2 = dt + rd(weekday=MO(+1))
            if dt2 - dt <= dt - dt1:
                self[dt2] = self._("discovery_day")
            else:
                self[dt1] = self._("discovery_day")
        elif self.subdiv == "YT" and year >= 1912:
            self[date(year, AUG, 1) + rd(weekday=MO(+3))] = self._(
                "discovery_day"
            )

        # Canada Day / Memorial Day (NL)
        if self.subdiv != "NL" and year >= 1867:
            if year >= 1983:
                i18n_name = "canada_day"
            else:
                i18n_name = "dominion_day"
            self[date(year, JUL, 1)] = self._(i18n_name)
            if (
                year >= 1879
                and self.observed
                and date(year, JUL, 1).weekday() in WEEKEND
            ):
                self[date(year, JUL, 1) + rd(weekday=MO)] = self._(
                    i18n_name + "_observed"
                )
        elif year >= 1867:
            if year >= 1983:
                i18n_name = "memorial_day"
            else:
                i18n_name = "dominion_day"
            self[date(year, JUL, 1)] = self._(i18n_name)
            if (
                year >= 1879
                and self.observed
                and date(year, JUL, 1).weekday() in WEEKEND
            ):
                self[date(year, JUL, 1) + rd(weekday=MO)] = self._(
                    i18n_name + "_observed"
                )

        # Nunavut Day
        if self.subdiv == "NU" and year >= 2001:
            self[date(year, JUL, 9)] = self._("nunavut_day")
            if self.observed and date(year, JUL, 9).weekday() == SUN:
                self[date(year, JUL, 10)] = self._("nunavut_day_observed")
        elif self.subdiv == "NU" and year == 2000:
            self[date(2000, 4, 1)] = self._("nunavut_day")

        # Civic Holiday
        if self.subdiv in ("ON", "MB", "NT") and year >= 1900:
            self[date(year, AUG, 1) + rd(weekday=MO)] = self._(
                'civic_holiday'
            )
        elif self.subdiv == "AB" and year >= 1974:
            # https://en.wikipedia.org/wiki/Civic_Holiday#Alberta
            self[date(year, AUG, 1) + rd(weekday=MO)] = self._(
                "heritage_day"
            )
        elif self.subdiv == "BC" and year >= 1974:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = self._(
                "british_columbia_day"
            )
        elif self.subdiv == "NB" and year >= 1900:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = self._(
                "new_brunswick_day"
            )
        elif self.subdiv == "SK" and year >= 1900:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, AUG, 1) + rd(weekday=MO)] = self._(
                "saskatchewan_day"
            )

        # Labour Day
        if year >= 1894:
            self[date(year, SEP, 1) + rd(weekday=MO)] = self._("labour_day")

        # Funeral of Queen Elizabeth II
        # https://www.narcity.com/provinces-territories-will-have-a-day-off-monday-mourn-queen
        # TODO: the territories holiday status (NT, NU, YT) is still tentative
        queen_funeral_observers = ("BC", "NB", "NL", "NS", "PE", "YT")
        if self.subdiv in queen_funeral_observers and year == 2022:
            self[date(year, SEP, 19)] = self._("queen_funeral")

        # National Day for Truth and Reconciliation
        if self.subdiv in ("MB", "NS") and year >= 2021:
            self[
                date(year, SEP, 30)
            ] = self._("national_day_for_truth_and_reconciliation")

        # Thanksgiving
        if self.subdiv not in ("NB", "NS", "PE", "NL") and year >= 1931:
            if year == 1935:
                # in 1935, Canadian Thanksgiving was moved due to the General
                # Election falling on the second Monday of October
                # https://books.google.ca/books?id=KcwlQsmheG4C&pg=RA1-PA1940&lpg=RA1-PA1940&dq=canada+thanksgiving+1935&source=bl&ots=j4qYrcfGuY&sig=gxXeAQfXVsOF9fOwjSMswPHJPpM&hl=en&sa=X&ved=0ahUKEwjO0f3J2PjOAhVS4mMKHRzKBLAQ6AEIRDAG#v=onepage&q=canada%20thanksgiving%201935&f=false
                self[date(1935, 10, 25)] = self._("thanksgiving")
            else:
                self[date(year, OCT, 1) + rd(weekday=MO(+2))] = self._(
                    "thanksgiving"
                )

        # Remembrance Day
        if (
            self.subdiv not in ("ON", "QC", "NS", "NL", "NT", "PE", "SK")
            and year >= 1931
        ):
            self[date(year, NOV, 11)] = self._("remembrance_day")
        elif self.subdiv in ("NS", "NL", "NT", "PE", "SK") and year >= 1931:
            self[date(year, NOV, 11)] = self._("remembrance_day")
            if self.observed and date(year, NOV, 11).weekday() == SUN:
                name = self._("remembrance_day_observed")
                self[date(year, NOV, 11) + rd(weekday=MO)] = name

        # Christmas Day
        if year >= 1867:
            self[date(year, DEC, 25)] = self._("christmas_day")
            if self.observed and date(year, DEC, 25).weekday() in WEEKEND:
                self[date(year, DEC, 27)] = self._("christmas_day_observed")

        # Boxing Day
        if year >= 1867:
            self[date(year, DEC, 26)] = self._("boxing_day")
            if self.observed and date(year, DEC, 26).weekday() in WEEKEND:
                self[date(year, DEC, 28)] = self._("boxing_day_observed")


class CA(Canada):
    pass


class CAN(Canada):
    pass
