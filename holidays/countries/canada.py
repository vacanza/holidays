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
from gettext import gettext as tr

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.constants import SUN, MON
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Canada(HolidayBase, ChristianHolidays, InternationalHolidays):
    country = "CA"
    default_language = "en"
    subdivisions = (
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
    )

    def __init__(self, *args, **kwargs):
        # Default subdivision to ON; prov for backwards compatibility
        if not kwargs.get("subdiv", kwargs.get("prov")):
            kwargs["subdiv"] = "ON"
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _get_nearest_monday(self, dt: date) -> date:
        return _get_nth_weekday_from(
            1 if self._is_friday(dt) or self._is_weekend(dt) else -1, MON, dt
        )

    def _add_observed(self, hol_date: date, include_sat: bool = True) -> None:
        if not self.observed:
            return None
        if self._is_sunday(hol_date) or (
            self._is_saturday(hol_date) and include_sat
        ):
            obs_date = _get_nth_weekday_from(1, MON, hol_date)
            if obs_date in self:
                obs_date += td(days=+1)
            self._add_holiday(
                self.tr("%s (Observed)") % self[hol_date], obs_date
            )

    def _populate(self, year):
        if year <= 1866:
            return None

        super()._populate(year)

        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))
        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        if year <= 1982:
            # Dominion Day.
            self._add_observed(self._add_holiday(tr("Dominion Day"), JUL, 1))

        if self._year >= 1894:
            self._add_holiday(
                # Labour Day.
                tr("Labour Day"),
                _get_nth_weekday_of_month(1, MON, SEP, self._year),
            )

        # Christmas Day.
        dec_25 = self._add_christmas_day(tr("Christmas Day"))

        # Boxing Day.
        dec_26 = self._add_christmas_day_two(tr("Boxing Day"))

        self._add_observed(dec_25)
        self._add_observed(dec_26)

    def _add_family_day(self):
        self._add_holiday(
            # Family Day.
            tr("Family Day"),
            _get_nth_weekday_of_month(3, MON, FEB, self._year),
        )

    def _add_thanksgiving(self):
        if self._year >= 1931:
            dt = (
                # in 1935, Canadian Thanksgiving was moved due to the General
                # Election falling on the second Monday of October
                # http://tiny.cc/can_thkgvg
                date(1935, OCT, 25)
                if self._year == 1935
                else _get_nth_weekday_of_month(2, MON, OCT, self._year)
            )
            # Thanksgiving.
            self._add_holiday(tr("Thanksgiving"), dt)

    def _add_queens_funeral(self):
        if self._year == 2022:
            self._add_holiday(
                # Funeral of Queen Elizabeth II.
                tr("Funeral of Her Majesty the Queen Elizabeth II"),
                SEP,
                19,
            )

    def _add_subdiv_holidays(self):
        if self._year >= 1983:
            self._add_observed(
                self._add_holiday(
                    (
                        # Memorial Day.
                        tr("Memorial Day")
                        if self.subdiv == "NL"
                        # Canada Day.
                        else tr("Canada Day")
                    ),
                    JUL,
                    1,
                )
            )

        super()._add_subdiv_holidays()

    def _add_subdiv_ab_holidays(self):
        if self._year >= 1990:
            self._add_family_day()

        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        # https://en.wikipedia.org/wiki/Civic_Holiday#Alberta
        if self._year >= 1974:
            self._add_holiday(
                # Heritage Day.
                tr("Heritage Day"),
                _get_nth_weekday_of_month(1, MON, AUG, self._year),
            )

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_bc_holidays(self):
        if self._year >= 2013:
            dt = _get_nth_weekday_of_month(
                3 if self._year >= 2019 else 2, MON, FEB, self._year
            )
            self._add_holiday(tr("Family Day"), dt)

        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        # https://en.wikipedia.org/wiki/Civic_Holiday#British_Columbia
        if self._year >= 1974:
            self._add_holiday(
                # British Columbia Day.
                tr("British Columbia Day"),
                _get_nth_weekday_of_month(1, MON, AUG, self._year),
            )

        self._add_queens_funeral()

        if self._year >= 2023:
            self._add_holiday(
                # National Day for Truth and Reconciliation.
                tr("National Day for Truth and Reconciliation"),
                SEP,
                30,
            )

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_mb_holidays(self):
        if self._year >= 2008:
            self._add_holiday(
                # Louis Riel Day.
                tr("Louis Riel Day"),
                _get_nth_weekday_of_month(3, MON, FEB, self._year),
            )

        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        if self._year >= 1900:
            name = (
                # Terry Fox Day.
                tr("Terry Fox Day")
                if self._year >= 2015
                # Civic Holiday.
                else tr("Civic Holiday")
            )
            self._add_holiday(
                name, _get_nth_weekday_of_month(1, MON, AUG, self._year)
            )

        if self._year >= 2021:
            self._add_holiday(
                # National Day for Truth and Reconciliation.
                tr("National Day for Truth and Reconciliation"),
                SEP,
                30,
            )

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_nb_holidays(self):
        if self._year >= 2018:
            self._add_family_day()

        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        # https://en.wikipedia.org/wiki/Civic_Holiday#New_Brunswick
        if self._year >= 1900:
            self._add_holiday(
                # New Brunswick Day.
                tr("New Brunswick Day"),
                _get_nth_weekday_of_month(1, MON, AUG, self._year),
            )

        self._add_queens_funeral()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_nl_holidays(self):
        if self._year >= 1900:
            # Nearest Monday to March 17.
            self._add_holiday(
                # St. Patrick's Day.
                tr("St. Patrick's Day"),
                self._get_nearest_monday(date(self._year, MAR, 17)),
            )

        if self._year >= 1990:
            dt = (
                # Nearest Monday to April 23
                # 4/26 is the Monday closer to 4/23 in 2010
                # but the holiday was observed on 4/19? Crazy Newfies!
                date(2010, APR, 19)
                if self._year == 2010
                else self._get_nearest_monday(date(self._year, APR, 23))
            )
            # St. George's Day.
            self._add_holiday(tr("St. George's Day"), dt)

        if self._year >= 1997:
            self._add_holiday(
                # Discovery Day.
                tr("Discovery Day"),
                self._get_nearest_monday(date(self._year, JUN, 24)),
            )

        self._add_queens_funeral()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(
                self._add_remembrance_day(tr("Remembrance Day")),
                include_sat=False,
            )

    def _add_subdiv_ns_holidays(self):
        # http://novascotia.ca/lae/employmentrights/NovaScotiaHeritageDay.asp
        if self._year >= 2015:
            self._add_holiday(
                # Heritage Day.
                tr("Heritage Day"),
                _get_nth_weekday_of_month(3, MON, FEB, self._year),
            )

        self._add_queens_funeral()

        if self._year >= 2021:
            self._add_holiday(
                # National Day for Truth and Reconciliation.
                tr("National Day for Truth and Reconciliation"),
                SEP,
                30,
            )

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(
                self._add_remembrance_day(tr("Remembrance Day")),
                include_sat=False,
            )

    def _add_subdiv_nt_holidays(self):
        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        if self._year >= 1996:
            # National Aboriginal Day.
            self._add_holiday(tr("National Aboriginal Day"), JUN, 21)

        if self._year >= 1900:
            self._add_holiday(
                # Civic Holiday.
                tr("Civic Holiday"),
                _get_nth_weekday_of_month(1, MON, AUG, self._year),
            )

        self._add_thanksgiving()

        if self._year >= 1931:
            self._add_observed(
                # Remembrance Day.
                self._add_remembrance_day(tr("Remembrance Day")),
                include_sat=False,
            )

    def _add_subdiv_nu_holidays(self):
        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        if self._year >= 2000:
            dt = (APR, 1) if self._year == 2000 else (JUL, 9)
            self._add_observed(
                # Nunavut Day.
                self._add_holiday(tr("Nunavut Day"), *dt),
                include_sat=False,
            )

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _add_subdiv_on_holidays(self):
        if self._year >= 2008:
            self._add_family_day()

        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        if self._year >= 1900:
            self._add_holiday(
                # Civic Holiday.
                tr("Civic Holiday"),
                _get_nth_weekday_of_month(1, MON, AUG, self._year),
            )

        self._add_thanksgiving()

    def _add_subdiv_pe_holidays(self):
        if self._year >= 2009:
            dt = _get_nth_weekday_of_month(
                3 if self._year >= 2010 else 2, MON, FEB, self._year
            )
            # Islander Day.
            self._add_holiday(tr("Islander Day"), dt)

        self._add_queens_funeral()

        if self._year >= 1931:
            self._add_observed(
                # Remembrance Day.
                self._add_remembrance_day(tr("Remembrance Day")),
                include_sat=False,
            )

    def _add_subdiv_qc_holidays(self):
        if self._year >= 2003:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # National Patriots' Day.
            self._add_holiday(tr("National Patriots' Day"), dt)

        if self._year >= 1925:
            self._add_observed(
                # St. Jean Baptiste Day.
                self._add_saint_johns_day(tr("St. Jean Baptiste Day")),
                include_sat=False,
            )

        self._add_thanksgiving()

    def _add_subdiv_sk_holidays(self):
        if self._year >= 2007:
            self._add_family_day()

        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        # https://en.wikipedia.org/wiki/Civic_Holiday#Saskatchewan
        if self._year >= 1900:
            self._add_holiday(
                # Saskatchewan Day.
                tr("Saskatchewan Day"),
                _get_nth_weekday_of_month(1, MON, AUG, self._year),
            )

        self._add_thanksgiving()

        if self._year >= 1931:
            self._add_observed(
                # Remembrance Day.
                self._add_remembrance_day(tr("Remembrance Day")),
                include_sat=False,
            )

    def _add_subdiv_yt_holidays(self):
        # start date?
        # https://www.britannica.com/topic/Heritage-Day-Canadian-holiday
        # Heritage Day was created in 1973
        # by the Heritage Canada Foundation
        # therefore, start date is not earlier than 1974
        # http://heritageyukon.ca/programs/heritage-day
        # https://en.wikipedia.org/wiki/Family_Day_(Canada)#Yukon_Heritage_Day
        # Friday before the last Sunday in February
        if self._year >= 1974:
            self._add_holiday(
                tr("Heritage Day"),
                _get_nth_weekday_of_month(-1, SUN, FEB, self._year)
                + td(days=-2),
            )

        if self._year >= 1953:
            dt = _get_nth_weekday_from(-1, MON, date(self._year, MAY, 24))
            # Victoria Day.
            self._add_holiday(tr("Victoria Day"), dt)

        if self._year >= 1912:
            self._add_holiday(
                # Discovery Day.
                tr("Discovery Day"),
                _get_nth_weekday_of_month(3, MON, AUG, self._year),
            )

        self._add_queens_funeral()

        self._add_thanksgiving()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))


class CA(Canada):
    pass


class CAN(Canada):
    pass
