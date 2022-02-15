# -*- coding: utf-8 -*-

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
from dateutil.relativedelta import relativedelta as rd, MO, FR, TH, TU

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
from holidays.constants import MON, WED, FRI, SAT, SUN, WEEKEND
from holidays.holiday_base import HolidayBase


class UnitedStates(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_the_United_States

    country = "US"
    subdivisions = [
        "AL",
        "AK",
        "AS",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "DC",
        "FL",
        "GA",
        "GU",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MH",
        "MA",
        "MI",
        "FM",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "MP",
        "OH",
        "OK",
        "OR",
        "PW",
        "PA",
        "PR",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "VI",
        "WA",
        "WV",
        "WI",
        "WY",
    ]

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if year > 1870:
            name = "New Year's Day"
            self[date(year, JAN, 1)] = name
            if self.observed and date(year, JAN, 1).weekday() == SUN:
                self[date(year, JAN, 1) + rd(days=+1)] = name + " (Observed)"
            # The following year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday).
            if self.observed and date(year, DEC, 31).weekday() == FRI:
                self[date(year, DEC, 31)] = name + " (Observed)"

        # Epiphany
        if self.subdiv == "PR":
            self[date(year, JAN, 6)] = "Epiphany"

        # Three King's Day
        if self.subdiv == "VI":
            self[date(year, JAN, 6)] = "Three King's Day"

        # Lee Jackson Day
        name = "Lee Jackson Day"
        if self.subdiv == "VA":
            if 2000 <= year <= 2020:
                dt = (
                    date(year, JAN, 1)
                    + rd(weekday=MO(+3))
                    + rd(weekday=FR(-1))
                )
                self[dt] = name
            elif 1983 <= year <= 2020:
                self[date(year, JAN, 1) + rd(weekday=MO(+3))] = name
            elif 1889 <= year <= 2020:
                self[date(year, JAN, 19)] = name

        # Inauguration Day
        if self.subdiv in ("DC", "LA", "MD", "VA") and year >= 1789:
            name = "Inauguration Day"
            if (year - 1789) % 4 == 0 and year >= 1937:
                self[date(year, JAN, 20)] = name
                if date(year, JAN, 20).weekday() == SUN:
                    self[date(year, JAN, 21)] = name + " (Observed)"
            elif (year - 1789) % 4 == 0:
                self[date(year, MAR, 4)] = name
                if date(year, MAR, 4).weekday() == SUN:
                    self[date(year, MAR, 5)] = name + " (Observed)"

        # Martin Luther King Jr. Day
        if year >= 1986:
            name = "Martin Luther King Jr. Day"
            if self.subdiv == "AL":
                name = "Robert E. Lee/Martin Luther King Birthday"
            elif (self.subdiv == "MS") or (
                (self.subdiv == "AR") and (year <= 2017)
            ):
                name = (
                    "Dr. Martin Luther King Jr. "
                    "and Robert E. Lee's Birthdays"
                )
            elif self.subdiv in ("AZ", "NH"):
                name = "Dr. Martin Luther King Jr./Civil Rights Day"
            elif self.subdiv == "GA" and year < 2012:
                name = "Robert E. Lee's Birthday"
            elif self.subdiv == "ID" and year >= 2006:
                name = "Martin Luther King Jr. - Idaho Human Rights Day"
            self[date(year, JAN, 1) + rd(weekday=MO(+3))] = name

        # Lincoln's Birthday
        name = "Lincoln's Birthday"
        if (
            self.subdiv in ("CT", "IL", "IA", "NJ", "NY") and year >= 1971
        ) or (self.subdiv == "CA" and 1971 <= year <= 2009):
            self[date(year, FEB, 12)] = name
            if self.observed and date(year, FEB, 12).weekday() == SAT:
                self[date(year, FEB, 11)] = name + " (Observed)"
            elif self.observed and date(year, FEB, 12).weekday() == SUN:
                self[date(year, FEB, 13)] = name + " (Observed)"

        # Susan B. Anthony Day
        if (
            (self.subdiv == "CA" and year >= 2014)
            or (self.subdiv == "FL" and year >= 2011)
            or (self.subdiv == "NY" and year >= 2004)
            or (self.subdiv == "WI" and year >= 1976)
        ):
            self[date(year, FEB, 15)] = "Susan B. Anthony Day"

        # Washington's Birthday
        name = "Washington's Birthday"
        if self.subdiv == "AL":
            name = "George Washington/Thomas Jefferson Birthday"
        elif self.subdiv == "AR":
            name = "George Washington's Birthday and Daisy Gatson Bates Day"
        elif self.subdiv in ("PR", "VI"):
            name = "Presidents' Day"
        if self.subdiv not in ("DE", "FL", "GA", "NM", "PR"):
            if year > 1970:
                self[date(year, FEB, 1) + rd(weekday=MO(+3))] = name
            elif year >= 1879:
                self[date(year, FEB, 22)] = name
        elif self.subdiv == "GA":
            if date(year, DEC, 24).weekday() != WED:
                self[date(year, DEC, 24)] = name
            else:
                self[date(year, DEC, 26)] = name
        elif self.subdiv in ("PR", "VI"):
            self[date(year, FEB, 1) + rd(weekday=MO(+3))] = name

        # Mardi Gras
        if self.subdiv == "LA" and year >= 1857:
            self[easter(year) + rd(days=-47)] = "Mardi Gras"

        # Guam Discovery Day
        if self.subdiv == "GU" and year >= 1970:
            self[date(year, MAR, 1) + rd(weekday=MO)] = "Guam Discovery Day"

        # Casimir Pulaski Day
        if self.subdiv == "IL" and year >= 1978:
            self[date(year, MAR, 1) + rd(weekday=MO)] = "Casimir Pulaski Day"

        # Texas Independence Day
        if self.subdiv == "TX" and year >= 1874:
            self[date(year, MAR, 2)] = "Texas Independence Day"

        # Town Meeting Day
        if self.subdiv == "VT" and year >= 1800:
            self[date(year, MAR, 1) + rd(weekday=TU)] = "Town Meeting Day"

        # Evacuation Day
        if self.subdiv == "MA" and year >= 1901:
            name = "Evacuation Day"
            self[date(year, MAR, 17)] = name
            if date(year, MAR, 17).weekday() in WEEKEND:
                self[date(year, MAR, 17) + rd(weekday=MO)] = (
                    name + " (Observed)"
                )

        # Emancipation Day
        if self.subdiv == "PR":
            self[date(year, MAR, 22)] = "Emancipation Day"
            if self.observed and date(year, MAR, 22).weekday() == SUN:
                self[date(year, MAR, 23)] = "Emancipation Day (Observed)"

        # Prince Jonah Kuhio Kalanianaole Day
        if self.subdiv == "HI" and year >= 1949:
            name = "Prince Jonah Kuhio Kalanianaole Day"
            self[date(year, MAR, 26)] = name
            if self.observed and date(year, MAR, 26).weekday() == SAT:
                self[date(year, MAR, 25)] = name + " (Observed)"
            elif self.observed and date(year, MAR, 26).weekday() == SUN:
                self[date(year, MAR, 27)] = name + " (Observed)"

        # Steward's Day
        name = "Steward's Day"
        if self.subdiv == "AK" and year >= 1955:
            self[date(year, APR, 1) + rd(days=-1, weekday=MO(-1))] = name
        elif self.subdiv == "AK" and year >= 1918:
            self[date(year, MAR, 30)] = name

        # César Chávez Day
        name = "César Chávez Day"
        if self.subdiv == "CA" and year >= 1995:
            self[date(year, MAR, 31)] = name
            if self.observed and date(year, MAR, 31).weekday() == SUN:
                self[date(year, APR, 1)] = name + " (Observed)"
        elif self.subdiv == "TX" and year >= 2000:
            self[date(year, MAR, 31)] = name

        # Transfer Day
        if self.subdiv == "VI":
            self[date(year, MAR, 31)] = "Transfer Day"

        # Emancipation Day
        if self.subdiv == "DC" and year >= 2005:
            name = "Emancipation Day"
            self[date(year, APR, 16)] = name
            if self.observed and date(year, APR, 16).weekday() == SAT:
                self[date(year, APR, 15)] = name + " (Observed)"
            elif self.observed and date(year, APR, 16).weekday() == SUN:
                self[date(year, APR, 17)] = name + " (Observed)"

        # Patriots' Day
        if self.subdiv in ("ME", "MA") and year >= 1969:
            self[date(year, APR, 1) + rd(weekday=MO(+3))] = "Patriots' Day"
        elif self.subdiv in ("ME", "MA") and year >= 1894:
            self[date(year, APR, 19)] = "Patriots' Day"

        # Holy Thursday
        if self.subdiv == "VI":
            self[easter(year) + rd(weekday=TH(-1))] = "Holy Thursday"

        # Good Friday
        if self.subdiv in (
            "CT",
            "DE",
            "GU",
            "IN",
            "KY",
            "LA",
            "NJ",
            "NC",
            "PR",
            "TN",
            "TX",
            "VI",
        ):
            self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Easter Monday
        if self.subdiv == "VI":
            self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # Confederate Memorial Day
        name = "Confederate Memorial Day"
        if self.subdiv in ("AL", "GA", "MS", "SC") and year >= 1866:
            if self.subdiv == "GA" and year >= 2016:
                name = "State Holiday"
            if self.subdiv == "GA" and year == 2020:
                self[date(year, APR, 10)] = name
            else:
                self[date(year, APR, 1) + rd(weekday=MO(+4))] = name
        elif self.subdiv == "TX" and year >= 1931:
            self[date(year, JAN, 19)] = name

        # San Jacinto Day
        if self.subdiv == "TX" and year >= 1875:
            self[date(year, APR, 21)] = "San Jacinto Day"

        # Arbor Day
        if self.subdiv == "NE" and year >= 1989:
            self[date(year, APR, 30) + rd(weekday=FR(-1))] = "Arbor Day"
        elif self.subdiv == "NE" and year >= 1875:
            self[date(year, APR, 22)] = "Arbor Day"

        # Primary Election Day
        if self.subdiv == "IN" and (
            (year >= 2006 and year % 2 == 0) or year >= 2015
        ):
            dt = date(year, MAY, 1) + rd(weekday=MO)
            self[dt + rd(days=+1)] = "Primary Election Day"

        # Truman Day
        if self.subdiv == "MO" and year >= 1949:
            name = "Truman Day"
            self[date(year, MAY, 8)] = name
            if self.observed and date(year, MAY, 8).weekday() == SAT:
                self[date(year, MAY, 7)] = name + " (Observed)"
            elif self.observed and date(year, MAY, 8).weekday() == SUN:
                self[date(year, MAY, 10)] = name + " (Observed)"

        # Memorial Day
        if year > 1970:
            self[date(year, MAY, 31) + rd(weekday=MO(-1))] = "Memorial Day"
        elif year >= 1888:
            self[date(year, MAY, 30)] = "Memorial Day"

        # Juneteenth Day
        if year > 2020:
            name = "Juneteenth National Independence Day"
            self[date(year, JUN, 19)] = name
            if self.observed and date(year, JUN, 19).weekday() == SAT:
                self[date(year, JUN, 18)] = name + " (Observed)"
            elif self.observed and date(year, JUN, 19).weekday() == SUN:
                self[date(year, JUN, 20)] = name + " (Observed)"

        # Jefferson Davis Birthday
        name = "Jefferson Davis Birthday"
        if self.subdiv == "AL" and year >= 1890:
            self[date(year, JUN, 1) + rd(weekday=MO)] = name

        # Kamehameha Day
        if self.subdiv == "HI" and year >= 1872:
            name = "Kamehameha Day"
            self[date(year, JUN, 11)] = name
            if self.observed and year >= 2011:
                if date(year, JUN, 11).weekday() == SAT:
                    self[date(year, JUN, 10)] = name + " (Observed)"
                elif date(year, JUN, 11).weekday() == SUN:
                    self[date(year, JUN, 12)] = name + " (Observed)"
        # Emancipation Day In Texas
        if self.subdiv == "TX" and year >= 1980:
            self[date(year, JUN, 19)] = "Emancipation Day In Texas"

        # West Virginia Day
        name = "West Virginia Day"
        if self.subdiv == "WV" and year >= 1927:
            self[date(year, JUN, 20)] = name
            if self.observed and date(year, JUN, 20).weekday() == SAT:
                self[date(year, JUN, 19)] = name + " (Observed)"
            elif self.observed and date(year, JUN, 20).weekday() == SUN:
                self[date(year, JUN, 21)] = name + " (Observed)"

        # Emancipation Day in US Virgin Islands
        if self.subdiv == "VI":
            self[date(year, JUL, 3)] = "Emancipation Day"

        # Independence Day
        if year > 1870:
            name = "Independence Day"
            self[date(year, JUL, 4)] = name
            if self.observed and date(year, JUL, 4).weekday() == SAT:
                self[date(year, JUL, 4) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, JUL, 4).weekday() == SUN:
                self[date(year, JUL, 4) + rd(days=+1)] = name + " (Observed)"

        # Liberation Day (Guam)
        if self.subdiv == "GU" and year >= 1945:
            self[date(year, JUL, 21)] = "Liberation Day (Guam)"

        # Pioneer Day
        if self.subdiv == "UT" and year >= 1849:
            name = "Pioneer Day"
            self[date(year, JUL, 24)] = name
            if self.observed and date(year, JUL, 24).weekday() == SAT:
                self[date(year, JUL, 24) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, JUL, 24).weekday() == SUN:
                self[date(year, JUL, 24) + rd(days=+1)] = name + " (Observed)"

        # Constitution Day
        if self.subdiv == "PR":
            self[date(year, JUL, 25)] = "Constitution Day"
            if self.observed and date(year, JUL, 25).weekday() == SUN:
                self[date(year, JUL, 26)] = "Constitution Day (Observed)"

        # Victory Day
        if self.subdiv == "RI" and year >= 1948:
            self[date(year, AUG, 1) + rd(weekday=MO(+2))] = "Victory Day"

        # Statehood Day (Hawaii)
        if self.subdiv == "HI" and year >= 1959:
            self[date(year, AUG, 1) + rd(weekday=FR(+3))] = "Statehood Day"

        # Bennington Battle Day
        if self.subdiv == "VT" and year >= 1778:
            name = "Bennington Battle Day"
            self[date(year, AUG, 16)] = name
            if self.observed and date(year, AUG, 16).weekday() == SAT:
                self[date(year, AUG, 15)] = name + " (Observed)"
            elif self.observed and date(year, AUG, 16).weekday() == SUN:
                self[date(year, AUG, 17)] = name + " (Observed)"

        # Lyndon Baines Johnson Day
        if self.subdiv == "TX" and year >= 1973:
            self[date(year, AUG, 27)] = "Lyndon Baines Johnson Day"

        # Labor Day
        if year >= 1894:
            self[date(year, SEP, 1) + rd(weekday=MO)] = "Labor Day"

        # Columbus Day
        if self.subdiv not in ("AK", "AR", "DE", "FL", "HI", "NV"):
            if self.subdiv == "SD":
                name = "Native American Day"
            elif self.subdiv == "VI":
                name = "Columbus Day and Puerto Rico Friendship Day"
            else:
                name = "Columbus Day"
            if year >= 1970:
                self[date(year, OCT, 1) + rd(weekday=MO(+2))] = name
            elif year >= 1937:
                self[date(year, OCT, 12)] = name

        # Alaska Day
        if self.subdiv == "AK" and year >= 1867:
            name = "Alaska Day"
            self[date(year, OCT, 18)] = name
            if self.observed and date(year, OCT, 18).weekday() == SAT:
                self[date(year, OCT, 18) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, OCT, 18).weekday() == SUN:
                self[date(year, OCT, 18) + rd(days=+1)] = name + " (Observed)"

        # Nevada Day
        if self.subdiv == "NV" and year >= 1933:
            dt = date(year, OCT, 31)
            if year >= 2000:
                dt += rd(weekday=FR(-1))
            self[dt] = "Nevada Day"
            if self.observed and dt.weekday() == SAT:
                self[dt + rd(days=-1)] = "Nevada Day (Observed)"
            elif self.observed and dt.weekday() == SUN:
                self[dt + rd(days=+1)] = "Nevada Day (Observed)"

        # Liberty Day
        if self.subdiv == "VI":
            self[date(year, NOV, 1)] = "Liberty Day"

        # Election Day
        if (
            self.subdiv
            in ("DE", "HI", "IL", "IN", "LA", "MT", "NH", "NJ", "NY", "WV")
            and year >= 2008
            and year % 2 == 0
        ) or (self.subdiv in ("IN", "NY") and year >= 2015):
            dt = date(year, NOV, 1) + rd(weekday=MO)
            self[dt + rd(days=+1)] = "Election Day"

        # All Souls' Day
        if self.subdiv == "GU":
            self[date(year, NOV, 2)] = "All Souls' Day"

        # Veterans Day
        if year > 1953:
            name = "Veterans Day"
        else:
            name = "Armistice Day"
        if 1978 > year > 1970:
            self[date(year, OCT, 1) + rd(weekday=MO(+4))] = name
        elif year >= 1938:
            self[date(year, NOV, 11)] = name
            if self.observed and date(year, NOV, 11).weekday() == SAT:
                self[date(year, NOV, 11) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, NOV, 11).weekday() == SUN:
                self[date(year, NOV, 11) + rd(days=+1)] = name + " (Observed)"

        # Discovery Day
        if self.subdiv == "PR":
            self[date(year, NOV, 19)] = "Discovery Day"
            if self.observed and date(year, NOV, 19).weekday() == SUN:
                self[date(year, NOV, 20)] = "Discovery Day (Observed)"

        # Thanksgiving
        if year > 1870:
            self[date(year, NOV, 1) + rd(weekday=TH(+4))] = "Thanksgiving"

        # Day After Thanksgiving
        # Friday After Thanksgiving
        # Lincoln's Birthday
        # American Indian Heritage Day
        # Family Day
        # New Mexico Presidents' Day
        if (
            (
                self.subdiv in ("CA", "DE", "FL", "NH", "NC", "OK", "TX", "WV")
                and year >= 1975
            )
            or (self.subdiv == "IN" and year >= 2010)
            or (self.subdiv == "MD" and year >= 2008)
            or self.subdiv in ("NV", "NM")
        ):
            if self.subdiv in ("CA", "DE", "NH", "NC", "OK", "WV"):
                name = "Day After Thanksgiving"
            elif self.subdiv in ("FL", "TX"):
                name = "Friday After Thanksgiving"
            elif self.subdiv == "IN":
                name = "Lincoln's Birthday"
            elif self.subdiv == "MD" and year >= 2008:
                name = "American Indian Heritage Day"
            elif self.subdiv == "NV":
                name = "Family Day"
            elif self.subdiv == "NM":
                name = "Presidents' Day"
            dt = date(year, NOV, 1) + rd(weekday=TH(+4))
            self[dt + rd(days=+1)] = name

        # Robert E. Lee's Birthday
        if self.subdiv == "GA" and year >= 1986:
            if year >= 2016:
                name = "State Holiday"
            else:
                name = "Robert E. Lee's Birthday"
            self[date(year, NOV, 29) + rd(weekday=FR(-1))] = name

        # Lady of Camarin Day
        if self.subdiv == "GU":
            self[date(year, DEC, 8)] = "Lady of Camarin Day"

        # Christmas Eve
        if (
            self.subdiv == "AS"
            or (self.subdiv in ("KS", "MI", "NC") and year >= 2013)
            or (self.subdiv == "TX" and year >= 1981)
            or (self.subdiv == "WI" and year >= 2012)
        ):
            name = "Christmas Eve"
            self[date(year, DEC, 24)] = name
            name = name + " (Observed)"
            # If on Friday, observed on Thursday
            if self.observed and date(year, DEC, 24).weekday() == FRI:
                self[date(year, DEC, 24) + rd(days=-1)] = name
            # If on Saturday or Sunday, observed on Friday
            elif self.observed and date(year, DEC, 24).weekday() in WEEKEND:
                self[date(year, DEC, 24) + rd(weekday=FR(-1))] = name

        # Christmas Day
        if year > 1870:
            name = "Christmas Day"
            self[date(year, DEC, 25)] = "Christmas Day"
            if self.observed and date(year, DEC, 25).weekday() == SAT:
                self[date(year, DEC, 25) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, DEC, 25).weekday() == SUN:
                self[date(year, DEC, 25) + rd(days=+1)] = name + " (Observed)"

        # Day After Christmas
        if self.subdiv == "NC" and year >= 2013:
            name = "Day After Christmas"
            self[date(year, DEC, 26)] = name
            name = name + " (Observed)"
            # If on Saturday or Sunday, observed on Monday
            if self.observed and date(year, DEC, 26).weekday() in WEEKEND:
                self[date(year, DEC, 26) + rd(weekday=MO)] = name
            # If on Monday, observed on Tuesday
            elif self.observed and date(year, DEC, 26).weekday() == MON:
                self[date(year, DEC, 26) + rd(days=+1)] = name
        elif self.subdiv == "TX" and year >= 1981:
            self[date(year, DEC, 26)] = "Day After Christmas"
        elif self.subdiv == "VI":
            self[date(year, DEC, 26)] = "Christmas Second Day"

        # New Year's Eve
        if (self.subdiv in ("KY", "MI") and year >= 2013) or (
            self.subdiv == "WI" and year >= 2012
        ):
            name = "New Year's Eve"
            self[date(year, DEC, 31)] = name
            if self.observed and date(year, DEC, 31).weekday() == SAT:
                self[date(year, DEC, 30)] = name + " (Observed)"


class US(UnitedStates):
    pass


class USA(UnitedStates):
    pass
