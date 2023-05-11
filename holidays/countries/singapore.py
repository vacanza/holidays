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

from datetime import timedelta as td
from typing import Dict, Tuple

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChineseCalendarHolidays, ChristianHolidays
from holidays.holiday_groups import InternationalHolidays, IslamicHolidays


class Singapore(
    HolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
):
    country = "SG"
    special_holidays = {
        2001: ((NOV, 3, "Polling Day"),),
        2006: ((MAY, 6, "Polling Day"),),
        2011: ((MAY, 7, "Polling Day"),),
        2015: (
            # SG50 Public holiday
            # Announced on 14 March 2015
            # https://www.mom.gov.sg/newsroom/press-releases/2015/sg50-public-holiday-on-7-august-2015
            (AUG, 7, "SG50 Public Holiday"),
            (SEP, 11, "Polling Day"),
        ),
        2020: ((JUL, 10, "Polling Day"),),
    }

    def __init__(self, *args, **kwargs) -> None:
        """
        A subclass of :py:class:`HolidayBase` representing public holidays in
        Singapore.

        Limitations:

        - Prior to 1969: holidays are estimated.
        - Prior to 2000: holidays may not be accurate.
        - 2024 and later: the following four moving date holidays (whose exact
          date is announced yearly) are estimated, and so denoted:

          - Hari Raya Puasa
          - Hari Raya Haji
          - Vesak Day
          - Deepavali

        Sources:

        - `Holidays Act <https://sso.agc.gov.sg/Act/HA1998>`__ (Act 24 of
          1968—Holidays (Amendment) Act 1968)
        - `Ministry of Manpower
          <https://www.mom.gov.sg/employment-practices/public-holidays>`__

        References:

        - `Wikipedia
          <https://en.wikipedia.org/wiki/Public_holidays_in_Singapore>`__

        Country created and maintained by: `Mike Borsetti
        <https://github.com/mborsetti>`__

        See parameters and usage in :py:class:`HolidayBase`.
        """
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year) -> None:
        super()._populate(year)
        observed_dates = set()

        # New Year's Day
        observed_dates.add(self._add_new_years_day("New Year's Day"))

        # Chinese New Year (two days)
        name = "Chinese New Year"
        observed_dates.add(self._add_chinese_new_years_day(name))
        observed_dates.add(self._add_chinese_new_years_day_two(name))

        # Hari Raya Puasa
        # aka Eid al-Fitr
        # Date of observance is announced yearly.
        # An Islamic holiday could fall twice in the same Gregorian year.
        dates_fixed_multiple_obs: Dict[int, Tuple[Tuple[int, int], ...]] = {
            2001: ((DEC, 16),),
            2002: ((DEC, 6),),
            2003: ((NOV, 25),),
            2004: ((NOV, 14),),
            2005: ((NOV, 3),),
            2006: ((OCT, 24),),
            2007: ((OCT, 13),),
            2008: ((OCT, 1),),
            2009: ((SEP, 20),),
            2010: ((SEP, 10),),
            2011: ((AUG, 30),),
            2012: ((AUG, 19),),
            2013: ((AUG, 8),),
            2014: ((JUL, 28),),
            2015: ((JUL, 17),),
            2016: ((JUL, 6),),
            2017: ((JUN, 25),),
            2018: ((JUN, 15),),
            2019: ((JUN, 5),),
            2020: ((MAY, 24),),
            2021: ((MAY, 13),),
            2022: ((MAY, 3),),
            2023: ((APR, 22),),
        }
        if year in dates_fixed_multiple_obs:
            for hol_date in dates_fixed_multiple_obs[year]:
                observed_dates.add(
                    self._add_holiday(  # type: ignore[arg-type]
                        "Hari Raya Puasa", *hol_date
                    )
                )
                # Second day of Hari Raya Puasa (up to and including 1968)
                # Removed since we don't have Hari Raya Puasa dates for the
                # the years <= 1968.
        else:
            observed_dates.update(
                self._add_eid_al_fitr_day("Hari Raya Puasa* (*estimated)")
            )
            # Second day of Hari Raya Puasa (up to and including 1968)
            if year <= 1968:
                self._add_eid_al_fitr_day_two(
                    "Second day of Hari Raya Puasa* (*estimated)"
                )

        # Hari Raya Haji
        # aka Eid al-Adha
        # Date of observance is announced yearly.
        # An Islamic holiday could fall twice in the same Gregorian year.
        dates_fixed_multiple_obs = {
            2001: ((MAR, 6),),
            2002: ((FEB, 23),),
            2003: ((FEB, 12),),
            2004: ((FEB, 1),),
            2005: ((JAN, 21),),
            2006: ((JAN, 10), (DEC, 31)),
            2007: ((DEC, 20),),
            2008: ((DEC, 8),),
            2009: ((NOV, 27),),
            2010: ((NOV, 17),),
            2011: ((NOV, 6),),
            2012: ((OCT, 26),),
            2013: ((OCT, 15),),
            2014: ((OCT, 5),),
            2015: ((SEP, 24),),
            2016: ((SEP, 12),),
            2017: ((SEP, 1),),
            2018: ((AUG, 22),),
            2019: ((AUG, 11),),
            2020: ((JUL, 31),),
            2021: ((JUL, 20),),
            2022: ((JUL, 10),),
            2023: ((JUN, 29),),
        }
        if year in dates_fixed_multiple_obs:
            for hol_date in dates_fixed_multiple_obs[year]:
                observed_dates.add(
                    self._add_holiday(  # type: ignore[arg-type]
                        "Hari Raya Haji", *hol_date
                    )
                )
        else:
            observed_dates.update(
                self._add_eid_al_adha_day("Hari Raya Haji* (*estimated)")
            )

        # Good Friday
        self._add_good_friday("Good Friday")

        if year <= 1968:
            # Holy Saturday
            self._add_holy_saturday("Holy Saturday")

            # Easter Monday
            self._add_easter_monday("Easter Monday")

        # Labour Day
        observed_dates.add(self._add_labor_day("Labour Day"))

        # Vesak Day
        # date of observance is announced yearly
        # https://en.wikipedia.org/wiki/Vesak#Dates_of_observance
        dates_fixed_obs: Dict[int, Tuple[int, int]] = {
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
            # 2023 date revised by MOM on 29-sep-22
            # https://www.mom.gov.sg/newsroom/press-releases/2022/0929-revised-date-for-vesak-day-2023
            2023: (JUN, 2),
        }
        if year in dates_fixed_obs:
            observed_dates.add(
                self._add_holiday(  # type: ignore[arg-type]
                    "Vesak Day", *dates_fixed_obs[year]
                )
            )
        else:
            observed_dates.add(
                self._add_chinese_calendar_holiday(
                    "Vesak Day* (*estimated)", 4, 15
                )
            )

        # National Day
        observed_dates.add(
            self._add_holiday("National Day", AUG, 9)  # type: ignore[arg-type]
        )

        # Deepavali
        # aka Diwali
        # date of observance is announced yearly
        dates_fixed_obs = {
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
        }
        if year in dates_fixed_obs:
            observed_dates.add(
                self._add_holiday(  # type: ignore[arg-type]
                    "Deepavali", *dates_fixed_obs[year]
                )
            )
        else:
            observed_dates.add(
                self._add_holiday(  # type: ignore[arg-type]
                    "Deepavali* (*estimated)",
                    self._convert_chinese_to_gre(10, 1) + td(days=-2),
                )
            )

        # Christmas Day
        observed_dates.add(self._add_christmas_day("Christmas Day"))

        # Boxing day (up to and including 1968)
        if year <= 1968:
            self._add_christmas_day_two("Boxing Day")

        # Implement Section 4(2) of the Holidays Act:
        # "if any day specified in the Schedule falls on a Sunday,
        # the day next following not being itself a public holiday
        # is declared a public holiday in Singapore."
        if not self.observed:
            return None
        if year >= 1998:
            for dt in sorted(observed_dates):
                if not self._is_sunday(dt):
                    continue
                self._add_holiday(
                    "%s (Observed)" % self[dt],
                    dt
                    + td(days=2 if dt + td(days=+1) in observed_dates else 1),
                )

        # special case (observed from previous year)
        if year == 2007:
            self._add_holiday("Hari Raya Haji (Observed)", JAN, 2)


class SG(Singapore):
    pass


class SGP(Singapore):
    pass
