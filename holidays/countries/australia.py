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
from dateutil.relativedelta import MO, TU, WE, FR
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, JUN, AUG, SEP, OCT, NOV
from holidays.constants import DEC, SAT, SUN
from holidays.holiday_base import HolidayBase


class Australia(HolidayBase):

    country = "AU"
    special_holidays = {
        2022: (
            (
                SEP,
                22,
                "National Day of Mourning for Queen Elizabeth II",
            ),
        ),
    }
    subdivisions = ["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"]

    def _populate(self, year):
        super()._populate(year)

        # ACT:  Holidays Act 1958
        # NSW:  Public Holidays Act 2010
        # NT:   Public Holidays Act 2013
        # QLD:  Holidays Act 1983
        # SA:   Holidays Act 1910
        # TAS:  Statutory Holidays Act 2000
        # VIC:  Public Holidays Act 1993
        # WA:   Public and Bank Holidays Act 1972

        # TODO do more research on history of Aus holidays

        # New Year's Day
        name = "New Year's Day"
        jan1 = date(year, JAN, 1)
        self[jan1] = name
        if self.observed and self._is_weekend(jan1):
            self[jan1 + rd(weekday=MO)] = name + " (Observed)"

        # Australia Day
        jan26 = date(year, JAN, 26)
        if year >= 1935:
            if self.subdiv == "NSW" and year < 1946:
                name = "Anniversary Day"
            else:
                name = "Australia Day"
            self[jan26] = name
            if self.observed and year >= 1946 and self._is_weekend(jan26):
                self[jan26 + rd(weekday=MO)] = name + " (Observed)"
        elif year >= 1888 and self.subdiv != "SA":
            name = "Anniversary Day"
            self[jan26] = name

        # Adelaide Cup
        if self.subdiv == "SA":
            name = "Adelaide Cup"
            if year >= 2006:
                # subject to proclamation ?!?!
                self[date(year, MAR, 1) + rd(weekday=MO(+2))] = name
            else:
                self[date(year, MAR, 1) + rd(weekday=MO(+3))] = name

        # Canberra Day
        # Info from https://www.timeanddate.com/holidays/australia/canberra-day
        # and https://en.wikipedia.org/wiki/Canberra_Day
        if self.subdiv == "ACT" and year >= 1913:
            name = "Canberra Day"
            if year >= 1913 and year <= 1957:
                self[date(year, MAR, 12)] = name
            if year >= 1958 and year <= 2007:
                self[date(year, MAR, 1) + rd(weekday=MO(+3))] = name
            if year >= 2008 and year != 2012:
                self[date(year, MAR, 1) + rd(weekday=MO(+2))] = name
            if year == 2012:
                self[date(year, MAR, 12)] = name

        # Easter
        easter_date = easter(year)
        self[easter_date + rd(days=-2)] = "Good Friday"
        if self.subdiv in {"ACT", "NSW", "NT", "QLD", "SA", "VIC"}:
            self[easter_date + rd(days=-1)] = "Easter Saturday"
        if self.subdiv in {"ACT", "NSW", "QLD", "VIC"}:
            self[easter_date] = "Easter Sunday"
        self[easter_date + rd(days=+1)] = "Easter Monday"

        # Anzac Day
        if year > 1920:
            name = "Anzac Day"
            apr25 = date(year, APR, 25)
            self[apr25] = name
            if self.observed:
                if apr25.weekday() == SAT and self.subdiv in {
                    "WA",
                    "NT",
                }:
                    self[apr25 + rd(weekday=MO)] = name + " (Observed)"
                elif apr25.weekday() == SUN and self.subdiv in {
                    "ACT",
                    "NT",
                    "QLD",
                    "SA",
                    "WA",
                }:
                    self[apr25 + rd(weekday=MO)] = name + " (Observed)"

        # Western Australia Day
        if self.subdiv == "WA" and year > 1832:
            if year >= 2015:
                name = "Western Australia Day"
            else:
                name = "Foundation Day"
            self[date(year, JUN, 1) + rd(weekday=MO(+1))] = name

        # Sovereign's Birthday
        if 1952 <= year <= 2022:
            name = "Queen's Birthday"
        elif year > 1901:
            name = "King's Birthday"
        if year >= 1936:
            if self.subdiv == "QLD":
                if year == 2012:
                    self[date(year, JUN, 11)] = "Queen's Diamond Jubilee"
                if year < 2016 and year != 2012:
                    dt = date(year, JUN, 1) + rd(weekday=MO(+2))
                    self[dt] = name
                else:
                    dt = date(year, OCT, 1) + rd(weekday=MO)
                    self[dt] = name
            elif self.subdiv == "WA":
                # by proclamation ?!?!
                self[date(year, OCT, 1) + rd(weekday=MO(-1))] = name
            elif self.subdiv in {"ACT", "NSW", "NT", "SA", "TAS", "VIC"}:
                dt = date(year, JUN, 1) + rd(weekday=MO(+2))
                self[dt] = name
        elif year > 1911:
            self[date(year, JUN, 3)] = name  # George V
        elif year > 1901:
            self[date(year, NOV, 9)] = name  # Edward VII

        # Picnic Day
        if self.subdiv == "NT":
            name = "Picnic Day"
            self[date(year, AUG, 1) + rd(weekday=MO)] = name

        # Bank Holiday
        if self.subdiv == "NSW":
            if year >= 1912:
                name = "Bank Holiday"
                self[date(year, 8, 1) + rd(weekday=MO)] = name

        # Labour Day
        name = "Labour Day"
        if self.subdiv in {"ACT", "NSW", "SA"}:
            self[date(year, OCT, 1) + rd(weekday=MO)] = name
        elif self.subdiv == "WA":
            self[date(year, MAR, 1) + rd(weekday=MO)] = name
        elif self.subdiv == "VIC":
            self[date(year, MAR, 1) + rd(weekday=MO(+2))] = name
        elif self.subdiv == "QLD":
            if 2013 <= year <= 2015:
                self[date(year, OCT, 1) + rd(weekday=MO)] = name
            else:
                self[date(year, MAY, 1) + rd(weekday=MO)] = name
        elif self.subdiv == "NT":
            name = "May Day"
            self[date(year, MAY, 1) + rd(weekday=MO)] = name
        elif self.subdiv == "TAS":
            name = "Eight Hours Day"
            self[date(year, MAR, 1) + rd(weekday=MO(+2))] = name

        # Family & Community Day
        if self.subdiv == "ACT":
            name = "Family & Community Day"
            if 2007 <= year <= 2009:
                self[date(year, NOV, 1) + rd(weekday=TU)] = name
            elif year == 2010:
                # first Monday of the September/October school holidays
                # moved to the second Monday if this falls on Labour day
                # TODO need a formula for the ACT school holidays then
                # http://www.cmd.act.gov.au/communication/holidays
                self[date(year, SEP, 26)] = name
            elif year == 2011:
                self[date(year, OCT, 10)] = name
            elif year == 2012:
                self[date(year, OCT, 8)] = name
            elif year == 2013:
                self[date(year, SEP, 30)] = name
            elif year == 2014:
                self[date(year, SEP, 29)] = name
            elif year == 2015:
                self[date(year, SEP, 28)] = name
            elif year == 2016:
                self[date(year, SEP, 26)] = name
            elif year == 2017:
                self[date(year, SEP, 25)] = name

        # Reconciliation Day
        if self.subdiv == "ACT":
            name = "Reconciliation Day"
            if year >= 2018:
                self[date(year, 5, 27) + rd(weekday=MO)] = name

        if self.subdiv == "VIC":
            # Grand Final Day
            if year == 2022:
                self[date(2022, SEP, 23)] = "Grand Final Day"
            elif year == 2020:
                # Rescheduled due to COVID-19
                self[date(year, OCT, 23)] = "Grand Final Day"
            elif year == 2021:
                # Rescheduled due to COVID-19
                self[date(year, SEP, 24)] = "Grand Final Day"
            elif year >= 2015:
                self[date(year, SEP, 24) + rd(weekday=FR)] = "Grand Final Day"

            # Melbourne Cup
            self[date(year, NOV, 1) + rd(weekday=TU)] = "Melbourne Cup"

        # The Royal Queensland Show (Ekka)
        # The Show starts on the first Friday of August - providing this is
        # not prior to the 5th - in which case it will begin on the second
        # Friday. The Wednesday during the show is a public holiday.
        if self.subdiv == "QLD":
            name = "The Royal Queensland Show"
            if year == 2020:
                self[date(year, AUG, 14)] = name
            if year == 2021:
                self[date(year, OCT, 29)] = name
            else:
                self[
                    date(year, AUG, 5) + rd(weekday=FR) + rd(weekday=WE)
                ] = name

        # Christmas Day
        name = "Christmas Day"
        dec25 = date(year, DEC, 25)
        self[dec25] = name
        if self.observed and self._is_weekend(dec25):
            self[date(year, DEC, 27)] = name + " (Observed)"

        # Boxing Day
        if self.subdiv == "SA":
            name = "Proclamation Day"
        else:
            name = "Boxing Day"
        dec26 = date(year, DEC, 26)
        self[dec26] = name
        if self.observed and self._is_weekend(dec26):
            self[date(year, DEC, 28)] = name + " (Observed)"


class AU(Australia):
    pass


class AUS(Australia):
    pass
