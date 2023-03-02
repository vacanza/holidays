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
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC, SUN, MON
from holidays.holiday_base import HolidayBase


class Canada(HolidayBase):
    country = "CA"
    default_language = "en"
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

    def _get_nearest_monday(self, dt: date) -> date:
        return _get_nth_weekday_from(
            1 if self._is_friday(dt) or self._is_weekend(dt) else -1, MON, dt
        )

    def _populate(self, year):
        if year < 1867:
            return None

        super()._populate(year)

        # New Year's Day.
        name = self.tr("New Year's Day")
        self[date(year, JAN, 1)] = name
        if self.observed and self._is_weekend(year, JAN, 1):
            self[_get_nth_weekday_of_month(1, MON, JAN, year)] = (
                self.tr("%s (Observed)") % name
            )

        # Family Day / Louis Riel Day (MB) / Islander Day (PE)
        # / Heritage Day (NS, YT)
        if (
            (self.subdiv == "AB" and year >= 1990)
            or (self.subdiv == "SK" and year >= 2007)
            or (self.subdiv == "ON" and year >= 2008)
            or (self.subdiv == "NB" and year >= 2018)
        ):
            self[_get_nth_weekday_of_month(3, MON, FEB, year)] = self.tr(
                "Family Day"
            )
        elif self.subdiv == "BC":
            if 2013 <= year <= 2018:
                self[_get_nth_weekday_of_month(2, MON, FEB, year)] = self.tr(
                    "Family Day"
                )
            elif year > 2018:
                self[_get_nth_weekday_of_month(3, MON, FEB, year)] = self.tr(
                    "Family Day"
                )
        elif self.subdiv == "MB" and year >= 2008:
            self[_get_nth_weekday_of_month(3, MON, FEB, year)] = self.tr(
                "Louis Riel Day"
            )
        elif self.subdiv == "PE" and year >= 2010:
            self[_get_nth_weekday_of_month(3, MON, FEB, year)] = self.tr(
                "Islander Day"
            )
        elif self.subdiv == "PE" and year == 2009:
            self[_get_nth_weekday_of_month(2, MON, FEB, year)] = self.tr(
                "Islander Day"
            )
        # http://novascotia.ca/lae/employmentrights/NovaScotiaHeritageDay.asp
        elif self.subdiv == "NS" and year >= 2015:
            # Heritage Day.
            self[_get_nth_weekday_of_month(3, MON, FEB, year)] = self.tr(
                "Heritage Day"
            )
        elif self.subdiv == "YT" and year >= 1974:
            # start date?
            # https://www.britannica.com/topic/Heritage-Day-Canadian-holiday
            # Heritage Day was created in 1973
            # by the Heritage Canada Foundation
            # therefore, start date is not earlier than 1974
            # http://heritageyukon.ca/programs/heritage-day
            # https://en.wikipedia.org/wiki/Family_Day_(Canada)#Yukon_Heritage_Day
            # Friday before the last Sunday in February
            dt = _get_nth_weekday_of_month(-1, SUN, FEB, year) + td(days=-2)
            # Heritage Day.
            self[dt] = self.tr("Heritage Day")

        # St. Patrick's Day.
        if self.subdiv == "NL" and year >= 1900:
            # Nearest Monday to March 17.
            dt = self._get_nearest_monday(date(year, MAR, 17))
            # St. Patrick's Day.
            self[dt] = self.tr("St. Patrick's Day")

        easter_date = easter(year)
        # Good Friday.
        self[easter_date + td(days=-2)] = self.tr("Good Friday")
        # Easter Monday.
        self[easter_date + td(days=+1)] = self.tr("Easter Monday")

        # St. George's Day
        if self.subdiv == "NL" and year >= 1990:
            if year == 2010:
                # 4/26 is the Monday closer to 4/23 in 2010
                # but the holiday was observed on 4/19? Crazy Newfies!
                dt = date(2010, APR, 19)
            else:
                # Nearest Monday to April 23
                dt = self._get_nearest_monday(date(year, APR, 23))
            self[dt] = self.tr("St. George's Day")

        # Victoria Day / National Patriots' Day (QC)
        if year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(year, MAY, 24))
            if self.subdiv not in {"NB", "NS", "PE", "NL", "QC"}:
                self[dt] = self.tr("Victoria Day")
            elif self.subdiv == "QC":
                self[dt] = self.tr("National Patriots' Day")

        # National Aboriginal Day
        if self.subdiv == "NT" and year >= 1996:
            self[date(year, JUN, 21)] = self.tr("National Aboriginal Day")

        # St. Jean Baptiste Day
        if self.subdiv == "QC" and year >= 1925:
            name = self.tr("St. Jean Baptiste Day")
            dt = date(year, JUN, 24)
            self[dt] = name
            if self.observed and self._is_sunday(dt):
                self[dt + td(days=+1)] = self.tr("%s (Observed)") % name

        # Discovery Day
        if self.subdiv == "NL" and year >= 1997:
            # Nearest Monday to June 24
            dt = self._get_nearest_monday(date(year, JUN, 24))
            self[dt] = self.tr("Discovery Day")
        elif self.subdiv == "YT" and year >= 1912:
            self[_get_nth_weekday_of_month(3, MON, AUG, year)] = self.tr(
                "Discovery Day"
            )

        # Canada Day / Memorial Day (NL)
        if year >= 1983:
            name = (
                self.tr("Memorial Day")
                if self.subdiv == "NL"
                else self.tr("Canada Day")
            )
        else:
            name = self.tr("Dominion Day")
        dt = date(year, JUL, 1)
        self[dt] = name
        if year >= 1879 and self.observed and self._is_weekend(dt):
            self[_get_nth_weekday_from(1, MON, dt)] = (
                self.tr("%s (Observed)") % name
            )

        # Nunavut Day
        if self.subdiv == "NU":
            name = self.tr("Nunavut Day")
            if year >= 2001:
                dt = date(year, JUL, 9)
                self[dt] = name
                if self.observed and self._is_sunday(dt):
                    self[dt + td(days=+1)] = self.tr("%s (Observed)") % name
            elif year == 2000:
                self[date(2000, APR, 1)] = name

        # Civic Holiday
        if year >= 1900 and self.subdiv in {"MB", "NT", "ON"}:
            self[_get_nth_weekday_of_month(1, MON, AUG, year)] = self.tr(
                "Civic Holiday"
            )
        # https://en.wikipedia.org/wiki/Civic_Holiday#Alberta
        elif year >= 1974 and self.subdiv == "AB":
            # Heritage Day.
            self[_get_nth_weekday_of_month(1, MON, AUG, year)] = self.tr(
                "Heritage Day"
            )
        # https://en.wikipedia.org/wiki/Civic_Holiday
        elif year >= 1974 and self.subdiv == "BC":
            # British Columbia Day.
            self[_get_nth_weekday_of_month(1, MON, AUG, year)] = self.tr(
                "British Columbia Day"
            )
        # https://en.wikipedia.org/wiki/Civic_Holiday
        elif year >= 1900 and self.subdiv == "NB":
            self[_get_nth_weekday_of_month(1, MON, AUG, year)] = self.tr(
                "New Brunswick Day"
            )
        # https://en.wikipedia.org/wiki/Civic_Holiday
        elif year >= 1900 and self.subdiv == "SK":
            self[_get_nth_weekday_of_month(1, MON, AUG, year)] = self.tr(
                "Saskatchewan Day"
            )

        # Labour Day
        if year >= 1894:
            self[_get_nth_weekday_of_month(1, MON, SEP, year)] = self.tr(
                "Labour Day"
            )

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
            self[date(2022, SEP, 19)] = self.tr(
                "Funeral of Her Majesty the Queen Elizabeth II"
            )

        # National Day for Truth and Reconciliation
        if (year >= 2021 and self.subdiv in {"MB", "NS"}) or (
            year >= 2023 and self.subdiv == "BC"
        ):
            self[date(year, SEP, 30)] = self.tr(
                "National Day for Truth and Reconciliation"
            )

        # Thanksgiving
        if year >= 1931 and self.subdiv not in {"NB", "NL", "NS", "PE"}:
            # in 1935, Canadian Thanksgiving was moved due to the General
            # Election falling on the second Monday of October
            # https://books.google.ca/books?id=KcwlQsmheG4C&pg=RA1-PA1940&lpg=RA1-PA1940&dq=canada+thanksgiving+1935&source=bl&ots=j4qYrcfGuY&sig=gxXeAQfXVsOF9fOwjSMswPHJPpM&hl=en&sa=X&ved=0ahUKEwjO0f3J2PjOAhVS4mMKHRzKBLAQ6AEIRDAG#v=onepage&q=canada%20thanksgiving%201935&f=false
            if year == 1935:
                self[date(1935, OCT, 25)] = self.tr("Thanksgiving")
            else:
                self[_get_nth_weekday_of_month(2, MON, OCT, year)] = self.tr(
                    "Thanksgiving"
                )

        # Remembrance Day,
        if year >= 1931 and self.subdiv not in {"ON", "QC"}:
            name = self.tr("Remembrance Day")
            dt = date(year, NOV, 11)
            self[dt] = name
            if (
                self.observed
                and self._is_sunday(dt)
                and self.subdiv in {"NS", "NL", "NT", "PE", "SK"}
            ):
                self[_get_nth_weekday_from(1, MON, dt)] = (
                    self.tr("%s (Observed)") % name
                )

        # Christmas Day,
        name = self.tr("Christmas Day")
        dt = date(year, DEC, 25)
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            self[dt + td(days=+2)] = self.tr("%s (Observed)") % name

        # Boxing Day.
        name = self.tr("Boxing Day")
        dt = date(year, DEC, 26)
        self[dt] = name
        if self.observed and self._is_weekend(dt):
            self[dt + td(days=+2)] = self.tr("%s (Observed)") % name


class CA(Canada):
    pass


class CAN(Canada):
    pass
