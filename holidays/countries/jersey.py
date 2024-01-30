#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: vacanza team (https://github.com/orgs/vacanza/teams) (c) 2023-2024
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from typing import Tuple

from holidays.calendars.gregorian import JAN, APR, MAY, JUN, JUL, SEP, OCT, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_WORKDAY,
    SUN_TO_NEXT_WORKDAY,
)


class Jersey(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Jersey
      - https://www.jerseylaw.je/laws/current/Pages/15.560.20.aspx # 2010 Revision
      - https://www.jerseylaw.je/laws/superseded/Pages/2006/15.560.20.aspx # 1952 Revision
      - https://www.jerseylaw.je/laws/enacted/Pages/RO-3038.aspx # 1952 as enacted
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%205331.aspx # Bank Holidays
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%206795.aspx # May Day
    Checked with:
      - https://www.gov.je/Leisure/Events/WhatsOn/pages/bankholidaydates.aspx # From 2010 onwards

    This has only been cross-checked with the official source from 2010 onwards.

    Jersey has the same public holidays as the United Kingdom (England Subdivision)
    - plus an extra day on 9 May, to mark Liberation Day (ignoring special holidays
    like the Corn Riots Anniversary in 2021).

    If a bank holiday is on a sunday, a substitute weekday becomes a bank holiday,
    normally the following Monday. From 2004 onwards this also applies to saturday.
    """

    country = "JE"
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, JerseyStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        ObservedHolidayBase.__init__(self, *args, **kwargs)

    def _add_observed(self, dt: date, **kwargs) -> Tuple[bool, date]:
        # Prior to 2004, in-lieu are only given for Sundays.
        # https://www.jerseylaw.je/laws/enacted/Pages/RO-123-2004.aspx
        kwargs.setdefault(
            "rule", SUN_TO_NEXT_WORKDAY if dt < date(2004, OCT, 12) else self._observed_rule
        )
        return super()._add_observed(dt, **kwargs)

    def _populate_public_holidays(self) -> None:
        # Earliest available piece of law available is from 1952.
        if self._year <= 1951:
            return None

        # New Year's Day.
        # Available online source shown that this was celebrated since at least 1952.
        # Was briefly removed in 1983 only to be added back again before that came to effect.

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # May Day
        # This only starts in 1980 (instead of 1978) for Jersey.
        # The date is not moved in 2020 (unlike in the UK) as there's already VE Day Celebrations.

        # May Day bank holiday (first Monday in May)
        if self._year >= 1980:
            name = "May Day"
            if self._year == 1995:
                self._add_holiday_may_8(name)
            else:
                self._add_holiday_1st_mon_of_may(name)

        # Spring bank holiday
        # Current Pattern started in 1970 for Jersey.

        # Spring bank holiday (last Monday in May)
        if self._year >= 1970:
            spring_bank_dates = {
                2002: (JUN, 4),
                2012: (JUN, 4),
                2022: (JUN, 2),
            }
            name = "Spring Bank Holiday"
            if self._year in spring_bank_dates:
                self._add_holiday(name, spring_bank_dates[self._year])
            else:
                self._add_holiday_last_mon_of_may(name)

        # Whit Monday.
        # Was in-use prior to Spring bank holiday adoption.

        if self._year <= 1969:
            # Whit Monday.
            self._add_whit_monday("Whit Monday")

        # Late Summer Bank Holiday
        # Current Pattern started in 1970. Was previously first Monday of September for Jersey.

        # Late Summer bank holiday (last Monday in August)
        summer_bank_holiday = "Late Summer Bank Holiday"
        if self._year >= 1970:
            self._add_holiday_last_mon_of_aug(summer_bank_holiday)
        else:
            self._add_holiday_1st_mon_of_sep(summer_bank_holiday)

        # Christmas Day
        christmas_day = self._add_christmas_day("Christmas Day")

        # Boxing Day
        boxing_day = self._add_christmas_day_two("Boxing Day")

        self._add_observed(christmas_day)
        self._add_observed(boxing_day)

        # Jersey exclusive holidays

        # Liberation Day.
        # Started in 1952. This has no in-lieus.
        # Counts as Public Holiday when fall on the weekdays, also on Saturday from 2010 onwards.
        # Specially held in 2010 on Sunday for the 65th Anniversary.

        # Liberation Day
        liberation_day = self._add_holiday_may_9("Liberation Day")
        if (self._is_sunday(liberation_day) and self._year != 2010) or (
            self._is_saturday(liberation_day) and self._year <= 2010
        ):
            self.pop(liberation_day)


class JE(Jersey):
    pass


class JEY(Jersey):
    pass


class JerseyStaticHolidays:
    """
    References:
      - https://www.gov.je/News/2019/pages/vedaypublicholiday8may.aspx
      - https://www.gov.je/news/2021/pages/cornriots.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20R%20%20O%209288.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20R%20%20O%209317.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%2042-2001.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%206350.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%206514.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%206924.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%207689.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%207877.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%208451.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/Jersey%20RO%208596.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/RO-050-2021.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/RO-108-2009.aspx
      - https://www.jerseylaw.je/laws/enacted/Pages/RO-3038.aspx
    """

    # Mostly a direct copy of UnitedKingdomStaticHolidays.

    # Jersey Specifics:
    #   - Queen Elizabeth II's Royal Visit (1957, 1978, 1989, 2001)*
    #        *2004 one falls on existing Liberation Day.
    #   - 75th VE Day Anniversary (2020)
    #   - 250th Corn Riots/Code of 1771 Anniversary (2021).

    # Jersey-specific Special Observance
    #   - New Year's Day (1977, 1983, 1994, 2000)
    #   - Boxing Day (1976, 1981, 1982, 1987, 1992, 1993, 1994, 1998, 1999, 2009)

    # New Year's Day
    new_years_day_in_lieu = "New Year's Day"

    # Boxing Day
    boxing_day_in_lieu = "Boxing Day"

    # Elizabeth II's Royal Visit.
    elizabeth_2_royal_visit = "Elizabeth II's Royal Visit"

    special_public_holidays = {
        1957: (JUL, 26, elizabeth_2_royal_visit),
        1977: (JUN, 7, "Silver Jubilee of Elizabeth II"),
        1978: (JUN, 27, elizabeth_2_royal_visit),
        1981: (JUL, 29, "Wedding of Charles and Diana"),
        1989: (MAY, 25, elizabeth_2_royal_visit),
        1999: (DEC, 31, "Millennium Celebrations"),
        2001: (JUL, 13, elizabeth_2_royal_visit),
        2002: (JUN, 3, "Golden Jubilee of Elizabeth II"),
        2011: (APR, 29, "Wedding of William and Catherine"),
        2012: (JUN, 5, "Diamond Jubilee of Elizabeth II"),
        2020: (MAY, 8, "75th Anniversary of VE Day"),
        2021: (SEP, 27, "250th Anniversary of the 1769 Corn Riots"),
        2022: (
            (JUN, 3, "Platinum Jubilee of Elizabeth II"),
            (SEP, 19, "State Funeral of Queen Elizabeth II"),
        ),
        2023: (MAY, 8, "Coronation of Charles III"),
    }
    special_public_holidays_observed = {
        1976: (DEC, 28, boxing_day_in_lieu),
        1977: (JAN, 3, new_years_day_in_lieu),
        1981: (DEC, 28, boxing_day_in_lieu),
        1982: (DEC, 28, boxing_day_in_lieu),
        1983: (JAN, 3, new_years_day_in_lieu),
        1987: (DEC, 28, boxing_day_in_lieu),
        1992: (DEC, 28, boxing_day_in_lieu),
        1993: (DEC, 28, boxing_day_in_lieu),
        1994: (JAN, 3, new_years_day_in_lieu),
        1998: (DEC, 28, boxing_day_in_lieu),
        1999: (DEC, 28, boxing_day_in_lieu),
        2000: (JAN, 3, new_years_day_in_lieu),
        2009: (DEC, 28, boxing_day_in_lieu),
    }
