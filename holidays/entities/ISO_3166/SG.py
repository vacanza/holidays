#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

"""
References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Singapore>
    - https://sso.agc.gov.sg/Act/HA1998>
    - https://www.mom.gov.sg/employment-practices/public-holidays>

Limitations:
    - Prior to 1969: holidays are estimated.
    - Prior to 2000: holidays may not be accurate.
    - 2024 and later: the following four moving date holidays (whose exact
      date is announced yearly) are estimated, and so denoted: Hari Raya Puasa,
      Hari Raya Haji, Vesak Day, Deepavali.

"""

from holidays.calendars import (
    _CustomBuddhistHolidays,
    _CustomChineseHolidays,
    _CustomIslamicHolidays,
    _CustomHinduHolidays,
)
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import (
    BuddhistCalendarHolidays,
    ChineseCalendarHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_WORKDAY


class SgHolidays(
    ObservedHolidayBase,
    BuddhistCalendarHolidays,
    ChineseCalendarHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    """A class to represent holidays for ."""

    country = "SG"
    name = "Singapore"
    observed_label = "%s (observed)"

    def __init__(self, *args, **kwargs):
        BuddhistCalendarHolidays.__init__(self, cls=SgBuddhistHolidays, show_estimated=True)
        ChineseCalendarHolidays.__init__(self, cls=SgChineseHolidays, show_estimated=True)
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self, cls=SgHinduHolidays)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=SgIslamicHolidays)
        StaticHolidays.__init__(self, cls=SgStaticHolidays)

        # Implement Section 4(2) of the Holidays Act:
        # "if any day specified in the Schedule falls on a Sunday,
        # the day next following not being itself a public holiday
        # is declared a public holiday in Singapore."
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 1998)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self) -> None:
        dts_observed = set()

        # New Year's Day
        dts_observed.add(self._add_new_years_day("New Year's Day"))

        # Chinese New Year (two days)
        name = "Chinese New Year"
        dts_observed.add(self._add_chinese_new_years_day(name))  # type: ignore[arg-type]
        dts_observed.add(self._add_chinese_new_years_day_two(name))  # type: ignore[arg-type]

        # Hari Raya Puasa (Eid al-Fitr)
        dts_observed.update(self._add_eid_al_fitr_day("Hari Raya Puasa"))
        if self._year <= 1968:
            self._add_eid_al_fitr_day_two("Second day of Hari Raya Puasa")

        # Hari Raya Haji (Eid al-Adha)
        dts_observed.update(self._add_eid_al_adha_day("Hari Raya Haji"))

        # Good Friday
        self._add_good_friday("Good Friday")

        if self._year <= 1968:
            # Holy Saturday
            self._add_holy_saturday("Holy Saturday")

            # Easter Monday
            self._add_easter_monday("Easter Monday")

        # Labour Day
        dts_observed.add(self._add_labor_day("Labour Day"))

        # Vesak Day
        dts_observed.add(self._add_vesak("Vesak Day"))  # type: ignore[arg-type]

        # National Day
        dts_observed.add(self._add_holiday_aug_9("National Day"))

        # Deepavali (Diwali)
        dts_observed.add(self._add_diwali("Deepavali"))  # type: ignore[arg-type]

        # Christmas Day
        dts_observed.add(self._add_christmas_day("Christmas Day"))

        # Boxing day (up to and including 1968)
        if self._year <= 1968:
            self._add_christmas_day_two("Boxing Day")

        if self.observed:
            self._populate_observed(dts_observed)


class SgBuddhistHolidays(_CustomBuddhistHolidays):
    VESAK_DATES = {
        2001: (MAY, 7),
        2002: (MAY, 26),
        2003: (MAY, 15),
        2004: (JUN, 2),
        2005: (MAY, 22),
        2006: (MAY, 12),
        2007: (MAY, 31),
        2008: (MAY, 19),
        2009: (MAY, 9),
        2010: (MAY, 28),
        2011: (MAY, 17),
        2012: (MAY, 5),
        2013: (MAY, 24),
        2014: (MAY, 13),
        2015: (JUN, 1),
        2016: (MAY, 21),
        2017: (MAY, 10),
        2018: (MAY, 29),
        2019: (MAY, 19),
        2020: (MAY, 7),
        2021: (MAY, 26),
        2022: (MAY, 15),
        2023: (JUN, 2),
        2024: (MAY, 22),
    }


class SgChineseHolidays(_CustomChineseHolidays):
    LUNAR_NEW_YEAR_DATES = {
        2001: (JAN, 24),
        2002: (FEB, 12),
        2003: (FEB, 1),
        2004: (JAN, 22),
        2005: (FEB, 9),
        2006: (JAN, 30),
        2007: (FEB, 19),
        2008: (FEB, 7),
        2009: (JAN, 26),
        2010: (FEB, 14),
        2011: (FEB, 3),
        2012: (JAN, 23),
        2013: (FEB, 10),
        2014: (JAN, 31),
        2015: (FEB, 19),
        2016: (FEB, 8),
        2017: (JAN, 28),
        2018: (FEB, 16),
        2019: (FEB, 5),
        2020: (JAN, 25),
        2021: (FEB, 12),
        2022: (FEB, 1),
        2023: (JAN, 22),
        2024: (FEB, 10),
    }


class SgHinduHolidays(_CustomHinduHolidays):
    DIWALI_DATES = {
        2001: (NOV, 14),
        2002: (NOV, 3),
        2003: (OCT, 23),
        2004: (NOV, 11),
        2005: (NOV, 1),
        2006: (OCT, 21),
        2007: (NOV, 8),
        2008: (OCT, 27),
        2009: (NOV, 15),
        2010: (NOV, 5),
        2011: (OCT, 26),
        2012: (NOV, 13),
        2013: (NOV, 2),
        2014: (OCT, 22),
        2015: (NOV, 10),
        2016: (OCT, 29),
        2017: (OCT, 18),
        2018: (NOV, 6),
        2019: (OCT, 27),
        2020: (NOV, 14),
        2021: (NOV, 4),
        2022: (OCT, 24),
        2023: (NOV, 12),
        2024: (OCT, 31),
    }


class SgIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 1),
        2005: (JAN, 21),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 27),
        2010: (NOV, 17),
        2011: (NOV, 6),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
    }

    EID_AL_FITR_DATES = {
        2001: (DEC, 16),
        2002: (DEC, 6),
        2003: (NOV, 25),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 1),
        2009: (SEP, 20),
        2010: (SEP, 10),
        2011: (AUG, 30),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2017: (JUN, 25),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 10),
    }


class SgStaticHolidays:
    special_public_holidays = {
        2001: (NOV, 3, "Polling Day"),
        2006: (MAY, 6, "Polling Day"),
        2011: (MAY, 7, "Polling Day"),
        2015: (
            # SG50 Public holiday
            # Announced on 14 March 2015
            # https://www.mom.gov.sg/newsroom/press-releases/2015/sg50-public-holiday-on-7-august-2015
            (AUG, 7, "SG50 Public Holiday"),
            (SEP, 11, "Polling Day"),
        ),
        2020: (JUL, 10, "Polling Day"),
        # Announced in state-associated press on 12 August 2023
        # https://www.straitstimes.com/singapore/politics/singapore-presidential-election-2023-polling-day-on-sept-1-nomination-day-on-aug-22
        2023: (SEP, 1, "Polling Day"),
    }

    special_public_holidays_observed = {
        2007: (JAN, 2, "Hari Raya Haji"),
    }
