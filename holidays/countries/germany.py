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

from holidays.calendars import _get_nth_weekday_from
from holidays.constants import JAN, MAR, MAY, AUG, SEP, OCT, NOV, DEC, WED
from holidays.holiday_base import HolidayBase


class Germany(HolidayBase):
    """Official holidays for Germany in its current form.

    This class doesn't return any holidays before 1990-10-03.

    Before that date the current Germany was separated into the "German
    Democratic Republic" and the "Federal Republic of Germany" which both had
    somewhat different holidays. Since this class is called "Germany" it
    doesn't really make sense to include the days from the two former
    countries.

    Note that Germany doesn't have rules for holidays that happen on a
    Sunday. Those holidays are still holiday days but there is no additional
    day to make up for the "lost" day.

    Also note that German holidays are partly declared by each province there
    are some weired edge cases:

        - "Mariä Himmelfahrt" is only a holiday in Bavaria (BY) if your
          municipality is mostly catholic which in term depends on census data.
          Since we don't have this data but most municipalities in Bavaria
          *are* mostly catholic, we count that as holiday for whole Bavaria.
          We added BYP for the municipality in Bavaria with more protestants.
          Here this is excluded.
        - There is an "Augsburger Friedensfest" which only exists in the town
          Augsburg. This is excluded for Bavaria.
        - "Gründonnerstag" (Thursday before easter) is not a holiday but pupils
           don't have to go to school (but only in Baden Württemberg) which is
           solved by adjusting school holidays to include this day. It is
           excluded from our list.
        - "Fronleichnam" is a holiday in certain, explicitly defined
          municipalities in Saxony (SN) and Thuringia (TH). We exclude it from
          both provinces.
    """

    country = "DE"
    subdivisions = [
        "BB",
        "BE",
        "BW",
        "BY",
        "BYP",
        "HB",
        "HE",
        "HH",
        "MV",
        "NI",
        "NW",
        "RP",
        "SH",
        "SL",
        "SN",
        "ST",
        "TH",
    ]

    def _populate(self, year):
        if year <= 1989:
            return None

        super()._populate(year)

        if year > 1990:
            self[date(year, JAN, 1)] = "Neujahr"

            if self.subdiv in {"BW", "BY", "BYP", "ST"}:
                self[date(year, JAN, 6)] = "Heilige Drei Könige"

            easter_date = easter(year)

            self[easter_date + td(days=-2)] = "Karfreitag"

            if self.subdiv == "BB":
                # will always be a Sunday and we have no "observed" rule so
                # this is pretty pointless but it's nonetheless an official
                # holiday by law
                self[easter_date] = "Ostersonntag"

            self[easter_date + td(days=+1)] = "Ostermontag"

            self[date(year, MAY, 1)] = "Erster Mai"

            if self.subdiv == "BE" and year == 2020:
                self[date(year, MAY, 8)] = (
                    "75. Jahrestag der Befreiung vom Nationalsozialismus "
                    "und der Beendigung des Zweiten Weltkriegs in Europa"
                )

            self[easter_date + td(days=+39)] = "Christi Himmelfahrt"

            if self.subdiv == "BB":
                # will always be a Sunday and we have no "observed" rule so
                # this is pretty pointless but it's nonetheless an official
                # holiday by law
                self[easter_date + td(days=+49)] = "Pfingstsonntag"

            self[easter_date + td(days=+50)] = "Pfingstmontag"

            if self.subdiv in {"BW", "BY", "BYP", "HE", "NW", "RP", "SL"}:
                self[easter_date + td(days=+60)] = "Fronleichnam"

            if self.subdiv in {"BY", "SL"}:
                self[date(year, AUG, 15)] = "Mariä Himmelfahrt"

        self[date(year, OCT, 3)] = "Tag der Deutschen Einheit"

        if (
            self.subdiv in {"BB", "MV", "SN", "ST", "TH"}
            or (self.subdiv in {"HB", "HH", "NI", "SH"} and year >= 2018)
            or year == 2017
        ):
            self[date(year, OCT, 31)] = "Reformationstag"

        if self.subdiv in {"BW", "BY", "BYP", "NW", "RP", "SL"}:
            self[date(year, NOV, 1)] = "Allerheiligen"

        if year <= 1994 or self.subdiv == "SN":
            # last wednesday before year-11-23
            self[
                _get_nth_weekday_from(-1, WED, date(year, NOV, 22))
            ] = "Buß- und Bettag"

        if year >= 2019:
            if self.subdiv == "TH":
                self[date(year, SEP, 20)] = "Weltkindertag"

            if self.subdiv == "BE":
                self[date(year, MAR, 8)] = "Internationaler Frauentag"

        if year >= 2023:
            if self.subdiv == "MV":
                self[date(year, MAR, 8)] = "Internationaler Frauentag"

        self[date(year, DEC, 25)] = "Erster Weihnachtstag"
        self[date(year, DEC, 26)] = "Zweiter Weihnachtstag"


class DE(Germany):
    pass


class DEU(Germany):
    pass
