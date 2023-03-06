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

from datetime import date
from datetime import timedelta as td

from dateutil.easter import easter

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, MAR, APR, MAY, JUN, AUG, SEP, OCT, NOV
from holidays.constants import DEC, MON, TUE, FRI
from holidays.holiday_base import HolidayBase


class Australia(HolidayBase):
    """
    References:
      - https://www.qld.gov.au/recreation/travel/holidays
    """

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
            self[_get_nth_weekday_from(1, MON, jan1)] = name + " (Observed)"

        # Australia Day
        jan26 = date(year, JAN, 26)
        if year >= 1935:
            if self.subdiv == "NSW" and year < 1946:
                name = "Anniversary Day"
            else:
                name = "Australia Day"
            self[jan26] = name
            if self.observed and year >= 1946 and self._is_weekend(jan26):
                self[_get_nth_weekday_from(1, MON, jan26)] = (
                    name + " (Observed)"
                )
        elif year >= 1888 and self.subdiv != "SA":
            name = "Anniversary Day"
            self[jan26] = name

        # Adelaide Cup
        if self.subdiv == "SA":
            name = "Adelaide Cup"
            if year >= 2006:
                # subject to proclamation ?!?!
                self[_get_nth_weekday_of_month(2, MON, MAR, year)] = name
            else:
                self[_get_nth_weekday_of_month(3, MON, MAR, year)] = name

        # Canberra Day
        # Info from https://www.timeanddate.com/holidays/australia/canberra-day
        # and https://en.wikipedia.org/wiki/Canberra_Day
        if self.subdiv == "ACT" and year >= 1913:
            name = "Canberra Day"
            if year <= 1957:
                self[date(year, MAR, 12)] = name
            elif year <= 2007:
                self[_get_nth_weekday_of_month(3, MON, MAR, year)] = name
            elif year == 2012:
                self[date(year, MAR, 12)] = name
            else:
                self[_get_nth_weekday_of_month(2, MON, MAR, year)] = name

        # Easter
        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        if self.subdiv in {"ACT", "NSW", "NT", "QLD", "SA", "VIC"}:
            self[easter_date + td(days=-1)] = "Easter Saturday"
        if self.subdiv in {"ACT", "NSW", "QLD", "VIC"}:
            self[easter_date] = "Easter Sunday"
        self[easter_date + td(days=+1)] = "Easter Monday"

        # Anzac Day
        if year > 1920:
            name = "Anzac Day"
            apr25 = date(year, APR, 25)
            self[apr25] = name
            if self.observed:
                if self._is_saturday(apr25) and self.subdiv in {
                    "WA",
                    "NT",
                }:
                    self[_get_nth_weekday_from(1, MON, apr25)] = (
                        name + " (Observed)"
                    )
                elif self._is_sunday(apr25) and self.subdiv in {
                    "ACT",
                    "NT",
                    "QLD",
                    "SA",
                    "WA",
                }:
                    self[_get_nth_weekday_from(1, MON, apr25)] = (
                        name + " (Observed)"
                    )

        # Western Australia Day
        if self.subdiv == "WA" and year > 1832:
            if year >= 2015:
                name = "Western Australia Day"
            else:
                name = "Foundation Day"
            self[_get_nth_weekday_of_month(1, MON, JUN, year)] = name

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
                    self[_get_nth_weekday_of_month(2, MON, JUN, year)] = name
                else:
                    self[_get_nth_weekday_of_month(1, MON, OCT, year)] = name
            elif self.subdiv == "WA":
                # by proclamation ?!?!
                self[_get_nth_weekday_from(-1, MON, date(year, OCT, 1))] = name
            elif self.subdiv in {"ACT", "NSW", "NT", "SA", "TAS", "VIC"}:
                self[_get_nth_weekday_of_month(2, MON, JUN, year)] = name
        elif year > 1911:
            self[date(year, JUN, 3)] = name  # George V
        elif year > 1901:
            self[date(year, NOV, 9)] = name  # Edward VII

        # Picnic Day
        if self.subdiv == "NT":
            self[_get_nth_weekday_of_month(1, MON, AUG, year)] = "Picnic Day"

        # Bank Holiday
        if self.subdiv == "NSW" and year >= 1912:
            self[_get_nth_weekday_of_month(1, MON, AUG, year)] = "Bank Holiday"

        # Labour Day
        name = "Labour Day"
        if self.subdiv in {"ACT", "NSW", "SA"}:
            self[_get_nth_weekday_of_month(1, MON, OCT, year)] = name
        elif self.subdiv == "WA":
            self[_get_nth_weekday_of_month(1, MON, MAR, year)] = name
        elif self.subdiv == "VIC":
            self[_get_nth_weekday_of_month(2, MON, MAR, year)] = name
        elif self.subdiv == "QLD":
            if 2013 <= year <= 2015:
                self[_get_nth_weekday_of_month(1, MON, OCT, year)] = name
            else:
                self[_get_nth_weekday_of_month(1, MON, MAY, year)] = name
        elif self.subdiv == "NT":
            self[_get_nth_weekday_of_month(1, MON, MAY, year)] = "May Day"
        elif self.subdiv == "TAS":
            self[
                _get_nth_weekday_of_month(2, MON, MAR, year)
            ] = "Eight Hours Day"

        # Family & Community Day
        if self.subdiv == "ACT":
            name = "Family & Community Day"
            if 2007 <= year <= 2009:
                self[_get_nth_weekday_of_month(1, TUE, NOV, year)] = name
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
        if self.subdiv == "ACT" and year >= 2018:
            self[
                _get_nth_weekday_from(1, MON, date(year, MAY, 27))
            ] = "Reconciliation Day"

        if self.subdiv == "VIC":
            # Grand Final Day
            name = "Grand Final Day"
            if year == 2022:
                self[date(2022, SEP, 23)] = name
            elif year == 2020:
                # Rescheduled due to COVID-19
                self[date(year, OCT, 23)] = name
            elif year == 2021:
                # Rescheduled due to COVID-19
                self[date(year, SEP, 24)] = name
            elif year >= 2015:
                self[_get_nth_weekday_from(1, FRI, date(year, SEP, 24))] = name

            # Melbourne Cup
            self[
                _get_nth_weekday_of_month(1, TUE, NOV, year)
            ] = "Melbourne Cup"

        # The Royal Queensland Show (Ekka)
        # The Show starts on the first Friday of August - providing this is
        # not prior to the 5th - in which case it will begin on the second
        # Friday. The Wednesday during the show is a public holiday.
        if self.subdiv == "QLD":
            ekka_dates = {
                2020: date(year, AUG, 14),
                2021: date(year, OCT, 29),
            }
            self[
                ekka_dates.get(
                    year,
                    _get_nth_weekday_from(1, FRI, date(year, AUG, 5))
                    + td(days=+5),
                )
            ] = "The Royal Queensland Show"

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
