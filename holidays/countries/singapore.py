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
from typing import Dict, Iterable, List, Optional, Tuple, Union

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, FR, SA

from holidays.constants import (
    SUN,
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    SEP,
    AUG,
    OCT,
    NOV,
    DEC,
)
from holidays.holiday_base import HolidayBase
from holidays.utils import _ChineseLuniSolar, _islamic_to_gre


class Singapore(HolidayBase):
    country = "SG"

    def __init__(
        self,
        years: Optional[Union[int, Iterable[int]]] = None,
        expand: bool = True,
        observed: bool = True,
        subdiv: Optional[str] = None,
        prov: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
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

        self.cnls = _ChineseLuniSolar()
        super().__init__(years, expand, observed, subdiv, prov, state)

    def _populate(self, year) -> None:
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "New Year's Day"

        # Chinese New Year (two days)
        hol_date = self.cnls.lunar_n_y_date(year)
        self[hol_date] = "Chinese New Year"
        self[hol_date + rd(days=+1)] = "Chinese New Year"

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
            2022: ((MAY, 2),),
            2023: ((APR, 22),),
        }
        if year in dates_fixed_multiple_obs:
            for month_day in dates_fixed_multiple_obs[year]:
                hol_date = date(year, *month_day)
                self[hol_date] = "Hari Raya Puasa"
                # Second day of Hari Raya Puasa (up to and including 1968)
                # Removed since we don't have Hari Raya Puasa dates for the
                # the years <= 1968:
                # if year <= 1968:
                #     self[hol_date + rd(days=+1),
                #                  "Second day of Hari Raya Puasa")
        else:
            for date_obs in _islamic_to_gre(year, 10, 1):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Puasa* (*estimated)"
                # Second day of Hari Raya Puasa (up to and including 1968)
                if year <= 1968:
                    hol_date += rd(days=+1)
                    self[hol_date] = (
                        "Second day of Hari Raya Puasa*" " (*estimated)"
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
            2006: ((JAN, 10),),
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
            2022: ((JUL, 9),),
            2023: ((JUN, 29),),
        }
        if year in dates_fixed_multiple_obs:
            for month_day in dates_fixed_multiple_obs[year]:
                hol_date = date(year, *month_day)
                self[hol_date] = "Hari Raya Haji"
        else:
            for date_obs in _islamic_to_gre(year, 12, 10):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Haji* (*estimated)"

        # Holy Saturday (up to and including 1968)
        if year <= 1968:
            self[easter(year) + rd(weekday=SA(-1))] = "Holy Saturday"

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Easter Monday
        if year <= 1968:
            self[easter(year) + rd(weekday=MO(1))] = "Easter Monday"

        # Labour Day
        self[date(year, MAY, 1)] = "Labour Day"

        # Vesak Day
        # date of observance is announced yearly
        # https://en.wikipedia.org/wiki/Vesak#Dates_of_observance
        dates_fixed_obs: Dict[int, Tuple[int, int]] = {
            2001: (MAY, 7),
            2002: (MAY, 27),
            2003: (MAY, 15),
            2004: (JUN, 2),
            2005: (MAY, 23),
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
            2016: (MAY, 20),
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
            hol_date = date(year, *dates_fixed_obs[year])
            self[hol_date] = "Vesak Day"
        else:
            hol_date = self.cnls.vesak_date(year)
            self[hol_date] = "Vesak Day* (*estimated; ~10% chance +/- 1 day)"

        # National Day
        self[date(year, AUG, 9)] = "National Day"

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
            2009: (OCT, 17),
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
            hol_date = date(year, *dates_fixed_obs[year])
            self[hol_date] = "Deepavali"
        else:
            hol_date = self.cnls.s_diwali_date(year)
            self[hol_date] = "Deepavali* (*estimated; rarely on day after)"

        # Christmas Day
        self[date(year, DEC, 25)] = "Christmas Day"

        # Boxing day (up to and including 1968)
        if year <= 1968:
            self[date(year, DEC, 26)] = "Boxing Day"

        # Polling Day
        dates_fixed_obs = {
            2001: (NOV, 3),
            2006: (MAY, 6),
            2011: (MAY, 7),
            2015: (SEP, 11),
            2020: (JUL, 10),
        }
        if year in dates_fixed_obs:
            self[date(year, *dates_fixed_obs[year])] = "Polling Day"

        # SG50 Public holiday
        # Announced on 14 March 2015
        # https://www.mom.gov.sg/newsroom/press-releases/2015/sg50-public-holiday-on-7-august-2015
        if year == 2015:
            self[date(2015, AUG, 7)] = "SG50 Public Holiday"

        # Check for holidays that fall on a Sunday and implement Section 4(2)
        # of the Holidays Act: "if any day specified in the Schedule falls on
        # a Sunday, the day next following not being itself a public holiday
        # is declared a public holiday in Singapore."
        for (hol_date, hol_name) in list(self.items()):
            if hol_date.year == year and hol_date.weekday() == SUN:
                self[hol_date] += " [Sunday]"
                in_lieu_date = hol_date + rd(days=+1)
                while in_lieu_date in self:
                    in_lieu_date += rd(days=+1)
                self[in_lieu_date] = hol_name + " [In lieu]"


class SG(Singapore):

    # __init__ required for IDE typing and inheritance of docstring.
    def __init__(
        self,
        years: Optional[Union[int, Iterable[int]]] = None,
        expand: bool = True,
        observed: bool = True,
        subdiv: Optional[str] = None,
        prov: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        super().__init__(years, expand, observed, subdiv, prov, state)


class SGP(Singapore):

    # __init__ required for IDE typing and inheritance of docstring.
    def __init__(
        self,
        years: Optional[Union[int, Iterable[int]]] = None,
        expand: bool = True,
        observed: bool = True,
        subdiv: Optional[str] = None,
        prov: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        super().__init__(years, expand, observed, subdiv, prov, state)
