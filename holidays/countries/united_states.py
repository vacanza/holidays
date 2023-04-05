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
from holidays.constants import OCT, NOV, DEC, MON, TUE, THU, FRI
from holidays.holiday_base import HolidayBase


class UnitedStates(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_the_United_States

    For Northern Mariana Islands (subdivision MP):
    https://governor.gov.mp/archived-news/executive-actions-archive/memorandum-2022-legal-holidays/
    https://webcache.googleusercontent.com/search?q=cache:C17_7FBgPtQJ:https://governor.gov.mp/archived-news/executive-actions-archive/memorandum-2022-legal-holidays/&hl=en&gl=sg&strip=1&vwsrc=0
    """

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
        "UM",
        "UT",
        "VT",
        "VA",
        "VI",
        "WA",
        "WV",
        "WI",
        "WY",
    ]

    def _add_with_observed(
        self, dt: date, name: str, before: bool = True, after: bool = True
    ) -> None:
        self[dt] = name
        if not self.observed:
            return None

        if self._is_saturday(dt) and before:
            self[dt + td(days=-1)] = f"{name} (Observed)"
        elif self._is_sunday(dt) and after:
            self[dt + td(days=+1)] = f"{name} (Observed)"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        if year >= 1871:
            name = "New Year's Day"
            self._add_with_observed(date(year, JAN, 1), name, before=False)
            # The following year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday).
            if self.observed and self._is_friday(date(year, DEC, 31)):
                self[date(year, DEC, 31)] = f"{name} (Observed)"

        # Epiphany
        if self.subdiv == "PR":
            self[date(year, JAN, 6)] = "Epiphany"

        # Three King's Day
        if self.subdiv == "VI":
            self[date(year, JAN, 6)] = "Three King's Day"

        # Lee Jackson Day
        if self.subdiv == "VA" and year <= 2020:
            name = "Lee Jackson Day"
            if year >= 2000:
                dt = _get_nth_weekday_of_month(3, MON, JAN, year) + td(days=-3)
                self[dt] = name
            elif year >= 1983:
                self[_get_nth_weekday_of_month(3, MON, JAN, year)] = name
            elif year >= 1889:
                self[date(year, JAN, 19)] = name

        # Inauguration Day
        if (
            self.subdiv in {"DC", "LA", "MD", "VA"}
            and year >= 1789
            and (year - 1789) % 4 == 0
        ):
            if year >= 1937:
                dt = date(year, JAN, 20)
            else:
                dt = date(year, MAR, 4)
            self._add_with_observed(dt, "Inauguration Day", before=False)

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
            elif self.subdiv in {"AZ", "NH"}:
                name = "Dr. Martin Luther King Jr./Civil Rights Day"
            elif self.subdiv == "GA" and year <= 2011:
                name = "Robert E. Lee's Birthday"
            elif self.subdiv == "ID" and year >= 2006:
                name = "Martin Luther King Jr. - Idaho Human Rights Day"
            self[_get_nth_weekday_of_month(3, MON, JAN, year)] = name

        # Lincoln's Birthday
        if (
            self.subdiv in {"CT", "IA", "IL", "NJ", "NY"} and year >= 1971
        ) or (self.subdiv == "CA" and 1971 <= year <= 2009):
            self._add_with_observed(date(year, FEB, 12), "Lincoln's Birthday")

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
        elif self.subdiv in {"PR", "VI"}:
            name = "Presidents' Day"
        if self.subdiv not in {"DE", "FL", "GA", "NM", "PR"}:
            if year >= 1971:
                self[_get_nth_weekday_of_month(3, MON, FEB, year)] = name
            elif year >= 1879:
                self[date(year, FEB, 22)] = name
        elif self.subdiv == "GA":
            if not self._is_wednesday(year, DEC, 24):
                self[date(year, DEC, 24)] = name
            else:
                self[date(year, DEC, 26)] = name
        elif self.subdiv in {"PR", "VI"}:
            self[_get_nth_weekday_of_month(3, MON, FEB, year)] = name

        easter_date = easter(year)
        # Mardi Gras
        if self.subdiv == "LA" and year >= 1857:
            self[easter_date + td(days=-47)] = "Mardi Gras"

        # Guam Discovery Day
        if self.subdiv == "GU" and year >= 1970:
            self[
                _get_nth_weekday_of_month(1, MON, MAR, year)
            ] = "Guam Discovery Day"

        # Casimir Pulaski Day
        if self.subdiv == "IL" and year >= 1978:
            self[
                _get_nth_weekday_of_month(1, MON, MAR, year)
            ] = "Casimir Pulaski Day"

        # Texas Independence Day
        if self.subdiv == "TX" and year >= 1874:
            self[date(year, MAR, 2)] = "Texas Independence Day"

        # Town Meeting Day
        if self.subdiv == "VT" and year >= 1800:
            self[
                _get_nth_weekday_of_month(1, TUE, MAR, year)
            ] = "Town Meeting Day"

        # Evacuation Day
        if self.subdiv == "MA" and year >= 1901:
            name = "Evacuation Day"
            dt = date(year, MAR, 17)
            self[dt] = name
            if self.observed and self._is_weekend(dt):
                self[_get_nth_weekday_from(1, MON, dt)] = f"{name} (Observed)"

        # Emancipation Day
        if self.subdiv == "PR":
            self._add_with_observed(
                date(year, MAR, 22), "Emancipation Day", before=False
            )

        # Commonwealth Covenant Day in Northern Mariana Islands
        if self.subdiv == "MP":
            self._add_with_observed(
                date(year, MAR, 24), "Commonwealth Covenant Day"
            )

        # Prince Jonah Kuhio Kalanianaole Day
        if self.subdiv == "HI" and year >= 1949:
            self._add_with_observed(
                date(year, MAR, 26), "Prince Jonah Kuhio Kalanianaole Day"
            )

        # Seward's Day
        if self.subdiv == "AK":
            name = "Seward's Day"
            if year >= 1955:
                self[_get_nth_weekday_of_month(-1, MON, MAR, year)] = name
            elif year >= 1918:
                self[date(year, MAR, 30)] = name

        # César Chávez Day
        name = "César Chávez Day"
        dt = date(year, MAR, 31)
        if self.subdiv == "CA" and year >= 1995:
            self._add_with_observed(dt, name, before=False)
        elif self.subdiv == "TX" and year >= 2000:
            self[dt] = name

        # Transfer Day
        if self.subdiv == "VI":
            self[date(year, MAR, 31)] = "Transfer Day"

        # Emancipation Day
        if self.subdiv == "DC" and year >= 2005:
            self._add_with_observed(date(year, APR, 16), "Emancipation Day")

        # Patriots' Day
        if self.subdiv in {"MA", "ME"}:
            name = "Patriots' Day"
            if year >= 1969:
                self[_get_nth_weekday_of_month(3, MON, APR, year)] = name
            elif year >= 1894:
                self[date(year, APR, 19)] = name

        # Holy Thursday
        if self.subdiv == "VI":
            self[easter_date + td(days=-3)] = "Holy Thursday"

        # Good Friday
        if self.subdiv in {
            "CT",
            "DE",
            "GU",
            "IN",
            "KY",
            "LA",
            "MP",
            "NC",
            "NJ",
            "PR",
            "TN",
            "TX",
            "VI",
        }:
            self[easter_date + td(days=-2)] = "Good Friday"

        # Easter Monday
        if self.subdiv == "VI":
            self[easter_date + td(days=+1)] = "Easter Monday"

        # Confederate Memorial Day
        name = "Confederate Memorial Day"
        if self.subdiv in {"AL", "GA", "MS", "SC"} and year >= 1866:
            if self.subdiv == "GA" and year >= 2016:
                name = "State Holiday"
            if self.subdiv == "GA" and year == 2020:
                self[date(year, APR, 10)] = name
            else:
                self[_get_nth_weekday_of_month(4, MON, APR, year)] = name
        elif self.subdiv == "TX" and year >= 1931:
            self[date(year, JAN, 19)] = name

        # San Jacinto Day
        if self.subdiv == "TX" and year >= 1875:
            self[date(year, APR, 21)] = "San Jacinto Day"

        # Arbor Day
        if self.subdiv == "NE":
            name = "Arbor Day"
            if year >= 1989:
                self[_get_nth_weekday_of_month(-1, FRI, APR, year)] = name
            elif year >= 1875:
                self[date(year, APR, 22)] = name

        # Primary Election Day
        if self.subdiv == "IN" and (
            (year >= 2006 and year % 2 == 0) or year >= 2015
        ):
            self[
                _get_nth_weekday_of_month(1, MON, MAY, year) + td(days=+1)
            ] = "Primary Election Day"

        # Truman Day
        if self.subdiv == "MO" and year >= 1949:
            self._add_with_observed(date(year, MAY, 8), "Truman Day")

        # Memorial Day
        if year >= 1971:
            self[
                _get_nth_weekday_of_month(-1, MON, MAY, year)
            ] = "Memorial Day"
        elif year >= 1888:
            self[date(year, MAY, 30)] = "Memorial Day"

        # Juneteenth Day
        if year >= 2021:
            self._add_with_observed(
                date(year, JUN, 19), "Juneteenth National Independence Day"
            )

        # Jefferson Davis Birthday
        name = "Jefferson Davis Birthday"
        if self.subdiv == "AL" and year >= 1890:
            self[_get_nth_weekday_of_month(1, MON, JUN, year)] = name

        # Kamehameha Day
        if self.subdiv == "HI" and year >= 1872:
            name = "Kamehameha Day"
            dt = date(year, JUN, 11)
            if year >= 2011:
                self._add_with_observed(dt, name)
            else:
                self[dt] = name

        # Emancipation Day In Texas
        if self.subdiv == "TX" and year >= 1980:
            self[date(year, JUN, 19)] = "Emancipation Day In Texas"

        # West Virginia Day
        if self.subdiv == "WV" and year >= 1927:
            self._add_with_observed(date(year, JUN, 20), "West Virginia Day")

        # Emancipation Day in US Virgin Islands
        if self.subdiv == "VI":
            self[date(year, JUL, 3)] = "Emancipation Day"

        # Independence Day
        if year >= 1871:
            self._add_with_observed(date(year, JUL, 4), "Independence Day")

        # Liberation Day (Guam)
        if self.subdiv == "GU" and year >= 1945:
            self[date(year, JUL, 21)] = "Liberation Day (Guam)"

        # Pioneer Day
        if self.subdiv == "UT" and year >= 1849:
            self._add_with_observed(date(year, JUL, 24), "Pioneer Day")

        # Constitution Day
        if self.subdiv == "PR":
            self._add_with_observed(
                date(year, JUL, 25), "Constitution Day", before=False
            )

        # Victory Day
        if self.subdiv == "RI" and year >= 1948:
            self[_get_nth_weekday_of_month(2, MON, AUG, year)] = "Victory Day"

        # Statehood Day (Hawaii)
        if self.subdiv == "HI" and year >= 1959:
            self[
                _get_nth_weekday_of_month(3, FRI, AUG, year)
            ] = "Statehood Day"

        # Bennington Battle Day
        if self.subdiv == "VT" and year >= 1778:
            self._add_with_observed(
                date(year, AUG, 16), "Bennington Battle Day"
            )

        # Lyndon Baines Johnson Day
        if self.subdiv == "TX" and year >= 1973:
            self[date(year, AUG, 27)] = "Lyndon Baines Johnson Day"

        # Labor Day
        if year >= 1894:
            self[_get_nth_weekday_of_month(1, MON, SEP, year)] = "Labor Day"

        # Columbus Day
        if self.subdiv not in {"AK", "AR", "DE", "FL", "HI", "NV"}:
            if self.subdiv == "SD":
                name = "Native American Day"
            elif self.subdiv == "VI":
                name = "Columbus Day and Puerto Rico Friendship Day"
            else:
                name = "Columbus Day"
            if year >= 1970:
                self[_get_nth_weekday_of_month(2, MON, OCT, year)] = name
            elif year >= 1937:
                self[date(year, OCT, 12)] = name

        # Commonwealth Cultural Day in Northern Mariana Islands
        if self.subdiv == "MP":
            self[
                _get_nth_weekday_of_month(2, MON, OCT, year)
            ] = "Commonwealth Cultural Day"

        # Alaska Day
        if self.subdiv == "AK" and year >= 1867:
            self._add_with_observed(date(year, OCT, 18), "Alaska Day")

        # Nevada Day
        if self.subdiv == "NV" and year >= 1933:
            dt = date(year, OCT, 31)
            if year >= 2000:
                dt = _get_nth_weekday_of_month(-1, FRI, OCT, year)
            self._add_with_observed(dt, "Nevada Day")

        # Liberty Day
        if self.subdiv == "VI":
            self[date(year, NOV, 1)] = "Liberty Day"

        # Election Day
        if (
            self.subdiv
            in {
                "DE",
                "HI",
                "IL",
                "IN",
                "LA",
                "MP",
                "MT",
                "NH",
                "NJ",
                "NY",
                "WV",
            }
            and year >= 2008
            and year % 2 == 0
        ) or (self.subdiv in {"IN", "NY"} and year >= 2015):
            self[
                _get_nth_weekday_of_month(1, MON, NOV, year) + td(days=+1)
            ] = "Election Day"

        # All Souls' Day
        if self.subdiv == "GU":
            self[date(year, NOV, 2)] = "All Souls' Day"

        # Citizenship Day in Northern Mariana Islands
        if self.subdiv == "MP":
            self._add_with_observed(date(year, NOV, 4), "Citizenship Day")

        # Veterans Day
        if year >= 1954:
            name = "Veterans Day"
        else:
            name = "Armistice Day"
        if 1971 <= year <= 1977:
            self[_get_nth_weekday_of_month(4, MON, OCT, year)] = name
        elif year >= 1938:
            self._add_with_observed(date(year, NOV, 11), name)

        # Discovery Day
        if self.subdiv == "PR":
            self._add_with_observed(
                date(year, NOV, 19), "Discovery Day", before=False
            )

        # Thanksgiving
        if year >= 1871:
            self[_get_nth_weekday_of_month(4, THU, NOV, year)] = "Thanksgiving"

        # Day After Thanksgiving
        # Friday After Thanksgiving
        # Lincoln's Birthday
        # American Indian Heritage Day
        # Family Day
        # New Mexico Presidents' Day
        if (
            (
                self.subdiv in {"CA", "DE", "FL", "NC", "NH", "OK", "TX", "WV"}
                and year >= 1975
            )
            or (self.subdiv == "IN" and year >= 2010)
            or (self.subdiv == "MD" and year >= 2008)
            or self.subdiv in {"NM", "NV", "PA"}
        ):
            if self.subdiv in {"CA", "DE", "NC", "NH", "OK", "PA", "WV"}:
                name = "Day After Thanksgiving"
            if self.subdiv in {"FL", "TX"}:
                name = "Friday After Thanksgiving"
            if self.subdiv == "IN":
                name = "Lincoln's Birthday"
            if self.subdiv == "MD":
                name = "American Indian Heritage Day"
            if self.subdiv == "NV":
                name = "Family Day"
            if self.subdiv == "NM":
                name = "Presidents' Day"
            self[
                _get_nth_weekday_of_month(4, THU, NOV, year) + td(days=+1)
            ] = name

        # Robert E. Lee's Birthday
        if self.subdiv == "GA" and year >= 1986:
            if year >= 2016:
                name = "State Holiday"
            else:
                name = "Robert E. Lee's Birthday"
            self[
                _get_nth_weekday_of_month(4, THU, NOV, year) + td(days=+1)
            ] = name

        # Lady of Camarin Day
        if self.subdiv == "GU":
            self[date(year, DEC, 8)] = "Lady of Camarin Day"

        # Constitution Day in Northern Mariana Islands
        if self.subdiv == "MP":
            self._add_with_observed(date(year, DEC, 8), "Constitution Day")

        # Christmas Eve
        if (
            self.subdiv == "AS"
            or (self.subdiv in {"KS", "MI", "NC"} and year >= 2013)
            or (self.subdiv == "TX" and year >= 1981)
            or (self.subdiv == "WI" and year >= 2012)
        ):
            name = "Christmas Eve"
            dt = date(year, DEC, 24)
            self[dt] = name
            # If on Friday, observed on Thursday
            if self.observed and self._is_friday(dt):
                self[dt + td(days=-1)] = f"{name} (Observed)"
            # If on Saturday or Sunday, observed on Friday
            elif self.observed and self._is_weekend(dt):
                self[_get_nth_weekday_from(-1, FRI, dt)] = f"{name} (Observed)"

        # Christmas Day
        if year >= 1871:
            self._add_with_observed(date(year, DEC, 25), "Christmas Day")

        # Day After Christmas
        dt = date(year, DEC, 26)
        if self.subdiv == "NC" and year >= 2013:
            name = "Day After Christmas"
            self[dt] = name
            # If on Saturday or Sunday, observed on Monday
            if self.observed and self._is_weekend(dt):
                self[_get_nth_weekday_from(1, MON, dt)] = f"{name} (Observed)"
            # If on Monday, observed on Tuesday
            elif self.observed and self._is_monday(dt):
                self[dt + td(days=+1)] = f"{name} (Observed)"
        elif self.subdiv == "TX" and year >= 1981:
            self[dt] = "Day After Christmas"
        elif self.subdiv == "VI":
            self[dt] = "Christmas Second Day"

        # New Year's Eve
        if (self.subdiv in {"KY", "MI"} and year >= 2013) or (
            self.subdiv == "WI" and year >= 2012
        ):
            self._add_with_observed(
                date(year, DEC, 31), "New Year's Eve", before=True, after=False
            )


class US(UnitedStates):
    pass


class USA(UnitedStates):
    pass
