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

from datetime import date, timedelta
from typing import Iterable, Optional, Union

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, FR, SA, SU
from dateutil.rrule import MONTHLY, rrule

from holidays.constants import (
    SUN,
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.holiday_base import HolidayBase
from holidays.utils import _ChineseLuniSolar, _islamic_to_gre


class Malaysia(HolidayBase):
    country = "MY"
    subdivisions = [
        "JHR",
        "KDH",
        "KTN",
        "MLK",
        "NSN",
        "PHG",
        "PRK",
        "PLS",
        "PNG",
        "SBH",
        "SWK",
        "SGR",
        "TRG",
        "KUL",
        "LBN",
        "PJY",
    ]

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
        An subclass of :py:class:`HolidayBase` representing public holidays in
        Malaysia.

        If ``subdiv`` for a state is not supplied, only nationwide holidays are
        returned. The following ``subdiv`` state codes are used (ISO 3166-2
        subdivision codes are not yet supported):

        - JHR: Johor
        - KDH: Kedah
        - KTN: Kelantan
        - MLK: Melaka
        - NSN: Negeri Sembilan
        - PHG: Pahang
        - PRK: Perak
        - PLS: Perlis
        - PNG: Pulau Pinang
        - SBH: Sabah
        - SWK: Sarawak
        - SGR: Selangor
        - TRG: Terengganu
        - KUL: FT Kuala Lumpur
        - LBN: FT Labuan
        - PJY: FT Putrajaya

        Limitations:

        - Prior to 2021: holidays are not accurate.
        - 2027 and later: Thaipusam dates are are estimated, and so denoted.

        Reference: `Wikipedia
        <https://en.wikipedia.org/wiki/Public_holidays_in_Malaysia>`__

        Country created by: `Eden <https://github.com/jusce17>`__

        Country maintained by: `Mike Borsetti <https://github.com/mborsetti>`__

        See parameters and usage in :py:class:`HolidayBase`.
        """
        self.cnls = _ChineseLuniSolar()
        super().__init__(years, expand, observed, subdiv, prov, state)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        if self.subdiv not in ("JHR", "KDH", "KTN", "PLS", "TRG"):
            self[date(year, JAN, 1)] = "New Year's Day"

        # Birthday of the Prophet Muhammad (s.a.w.).
        # a.k.a. Hari Keputeraan Nabi Muhammad (Sabah Act)
        for hol_date in self.my_islamic_to_gre(year, 3, 12):
            self[
                hol_date
            ] = "Maulidur Rasul (Birthday of the Prophet Muhammad)"

        # Hari Kebangsaan or National Day.
        self[date(year, AUG, 31)] = "National Day"

        # Chinese New Year (one day in the States of Kelantan and Terengganu,
        # two days in the other States).
        hol_date = self.cnls.lunar_n_y_date(year)
        self[hol_date] = "Chinese New Year"
        # The second day of Chinese New Year is not a federal holiday in
        # Kelantan and Terengganu. However, it is gazetted as a state holiday
        # in both states, effectively making it a nationwide holiday.
        self[hol_date + rd(days=+1)] = "Chinese New Year Holiday"

        # Wesak Day.
        # Date of observance is announced yearly
        # https://en.wikipedia.org/wiki/Vesak#Dates_of_observance
        dates_obs = {
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
        }
        if year in dates_obs:
            hol_date = date(year, *dates_obs[year])
            self[hol_date] = "Vesak Day"
        else:
            hol_date = self.cnls.vesak_may_date(year)
            self[hol_date] = "Vesak Day* (*estimated; ~10% chance +/- 1 day)"

        # Birthday of [His Majesty] the Yang di-Pertuan Agong.
        if year <= 2017:
            hol_date = rrule(
                MONTHLY,
                dtstart=date(year, JUN, 1),
                count=1,
                bysetpos=1,
                byweekday=SA,
            )[0]
        elif year == 2018:
            hol_date = date(2018, SEP, 9)
        else:
            hol_date = rrule(
                MONTHLY,
                dtstart=date(year, JUN, 1),
                count=1,
                bysetpos=1,
                byweekday=MO,
            )[0]
        self[hol_date] = "Birthday of SPB Yang di-Pertuan Agong"

        # Hari Raya Puasa (2 days).
        # aka Eid al-Fitr;
        # exact date of observance is announced yearly
        dates_obs = {
            2001: [(DEC, 17)],
            2002: [(DEC, 6)],
            2003: [(NOV, 25)],
            2004: [(NOV, 14)],
            2005: [(NOV, 3)],
            2006: [(OCT, 24)],
            2007: [(OCT, 13)],
            2008: [(OCT, 1)],
            2009: [(SEP, 20)],
            2010: [(SEP, 10)],
            2011: [(AUG, 30)],
            2012: [(AUG, 19)],
            2013: [(AUG, 8)],
            2014: [(JUL, 28)],
            2015: [(JUL, 17)],
            2016: [(JUL, 6)],
            2017: [(JUN, 25)],
            2018: [(JUN, 15)],
            2019: [(JUN, 5)],
            2020: [(MAY, 24)],
            2021: [(MAY, 13)],
            2022: [(MAY, 2)],
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Puasa"
                self[hol_date + rd(days=+1)] = "Second day of Hari Raya Puasa"
        else:
            for date_obs in _islamic_to_gre(year, 10, 1):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Puasa* (*estimated)"
                self[hol_date + rd(days=+1)] = (
                    "Second day of Hari Raya Puasa*" " (*estimated)"
                )

        # Hari Raya Haji and Arafat Day.
        # Date of observance is announced yearly.
        dates_obs = {
            2001: [(MAR, 6)],
            2002: [(FEB, 23)],
            2003: [(FEB, 12)],
            2004: [(FEB, 1)],
            2005: [(JAN, 21)],
            2006: [(JAN, 10)],
            2007: [(DEC, 20)],
            2008: [(DEC, 8)],
            2009: [(NOV, 27)],
            2010: [(NOV, 17)],
            2011: [(NOV, 6)],
            2012: [(OCT, 26)],
            2013: [(OCT, 15)],
            2014: [(OCT, 5)],
            2015: [(SEP, 24)],
            2016: [(SEP, 12)],
            2017: [(SEP, 1)],
            2018: [(AUG, 22)],
            2019: [(AUG, 11)],
            2020: [(JUL, 31)],
            2021: [(JUL, 20)],
            2022: [(JUL, 9)],
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Haji"
                if self.subdiv == "TRG":
                    # Arafat Day is one day before Eid al-Adha
                    self[hol_date - rd(days=1)] = "Arafat Day"
                if self.subdiv in ("KDH", "KTN", "PLS", "TRG"):
                    # Second day
                    self[hol_date + rd(days=1)] = "Hari Raya Haji Holiday"
        else:
            for date_obs in _islamic_to_gre(year, 12, 10):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Haji* (*estimated)"
                if self.subdiv == "TRG":
                    # Arafat Day is one day before Eid al-Adha
                    self[hol_date - rd(days=1)] = "Arafat Day* (*estimated)"
                if self.subdiv in ("KDH", "KTN", "PLS", "TRG"):
                    # Second day
                    self[
                        hol_date + rd(days=1)
                    ] = "Hari Raya Haji Holiday* (*estimated)"

        # Deepavali.
        # aka Diwali;
        # date of observance is announced yearly
        if self.subdiv != "SWK":
            dates_obs = {
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
            }
            if year in dates_obs:
                hol_date = date(year, *dates_obs[year])
                self[hol_date] = "Deepavali"
            else:
                hol_date = self.cnls.s_diwali_date(year)
                self[hol_date] = "Deepavali* (*estimated; rarely on day after)"

        # Christmas day.
        self[date(year, DEC, 25)] = "Christmas Day"

        # Malaysia Day.
        self[date(year, SEP, 16)] = "Malaysia Day"

        # ---------------------------------------------------------#
        # Holidays from the Sarawak Ordinance (not included above) #
        # ---------------------------------------------------------#
        if self.subdiv == "SWK":
            # Dayak Festival Day (the first day of June) and the following day.
            self[date(year, JUN, 1)] = "Gawai Dayak"
            self[date(year, JUN, 2)] = "Gawai Dayak (Second day)"

            # The first day of May—Worker’s Celebration Day.

            # Birthday of Tuan Yang Terutama Yang di-Pertua Negeri Sarawak (the
            # second Saturday of September).
            second_sat_oct = rrule(
                MONTHLY,
                dtstart=date(year, OCT, 1),
                count=1,
                bysetpos=2,
                byweekday=SA,
            )[0]
            self[second_sat_oct] = "Birthday of the Governor of Sarawak"

            # Sarawak Independence Day
            if year > 2016:
                self[date(year, JUL, 22)] = "Sarawak Day"

        # Check for holidays that fall on a Sunday and
        # implement Section 3 of Malaysian Holidays Act:
        # "if any day specified in the Schedule falls on
        # Sunday then the day following shall be a public
        # holiday and if such day is already a public holiday,
        # then the day following shall be a public holiday"
        for (hol_date, hol_name) in list(self.items()):
            if hol_date.year == year and hol_date.weekday() == SUN:
                self[hol_date] += " [Sunday]"
                in_lieu_date = hol_date + rd(days=+1)
                while in_lieu_date in self:
                    in_lieu_date += rd(days=+1)
                self[in_lieu_date] = hol_name + " [In lieu]"

        # The last two days in May (Pesta Kaamatan).
        # (Sarawak Act)
        # Day following a Sunday is not a holiday
        if self.subdiv in ("LBN", "SBH"):
            self[date(year, MAY, 30)] = "Pesta Kaamatan"
            self[date(year, MAY, 31)] = "Pesta Kaamatan (Second day)"

        # ------------------------------#
        # Other holidays (decrees etc.) #
        # ------------------------------#

        # Malaysia General Election Holiday.
        dates_obs = {
            # The years 1955 1959 1995 seems to have the elections
            # one weekday but I am not sure if they were marked as
            # holidays.
            1999: (NOV, 29),
            2018: (MAY, 9),
        }
        if year in dates_obs:
            self[
                date(year, *dates_obs[year])
            ] = "Malaysia General Election Holiday"

        # Awal Muharram.
        for hol_date in self.my_islamic_to_gre(year, 1, 1):
            self[hol_date] = "Awal Muharram (Hijri New Year)"

        # Labour Day.
        self[date(year, MAY, 1)] = "Labour Day"

        # ---------------------------------#
        # State holidays (multiple states) #
        # ---------------------------------#

        # 1 January (or the following day if the 1 January should fall on a
        # weekly holiday in any State or in the Federal Territory).
        if self.subdiv in (
            "KUL",
            "LBN",
            "MLK",
            "NSN",
            "PHG",
            "PNG",
            "PRK",
            "PJY",
            "SBH",
            "SWK",
            "SGR",
        ):
            hol_date = date(year, JAN, 1)
            self[hol_date] = "New Year's Day"
            if hol_date.weekday() == SUN:
                self[hol_date] += " [Sunday]"
                self[date(year, JAN, 2)] = "New Year's Day [In lieu]"

        # Isra and Mi'raj.
        if self.subdiv in ("KDH", "NSN", "PLS", "TRG"):
            for hol_date in _islamic_to_gre(year, 7, 27):
                self[hol_date] = "Isra and Mi'raj"

        # Beginning of Ramadan.
        if self.subdiv in ("JHR", "KDH", "MLK"):
            for hol_date in _islamic_to_gre(year, 9, 1):
                self[hol_date] = "Begining of Ramadan"

        # Nuzul Al-Quran Day.
        if self.subdiv not in (
            "JHR",
            "KDH",
            "MLK",
            "NSN",
            "SBH",
            "SWK",
        ):
            for hol_date in _islamic_to_gre(year, 9, 17):
                self[hol_date] = "Nuzul Al-Quran Day"

        # Hari Raya Aidilfitri.
        # aka Eid al-Fitr;
        # date of observance is announced yearly
        dates_obs = {
            2001: [(DEC, 16)],
            2002: [(DEC, 6)],
            2003: [(NOV, 25)],
            2004: [(NOV, 14)],
            2005: [(NOV, 3)],
            2006: [(OCT, 24)],
            2007: [(OCT, 13)],
            2008: [(OCT, 1)],
            2009: [(SEP, 20)],
            2010: [(SEP, 10)],
            2011: [(AUG, 30)],
            2012: [(AUG, 19)],
            2013: [(AUG, 8)],
            2014: [(JUL, 28)],
            2015: [(JUL, 17)],
            2016: [(JUL, 6)],
            2017: [(JUN, 25)],
            2018: [(JUN, 15)],
            2019: [(JUN, 5)],
            2020: [(MAY, 24)],
            2021: [(MAY, 13)],
            2022: [(MAY, 2)],
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Aidilfitri"
                hol_date += rd(days=+1)
                self[hol_date] = "Hari Raya Aidilfitri Holiday"
        else:
            for date_obs in _islamic_to_gre(year, 10, 1):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Aidilfitri* (*estimated)"
                hol_date += rd(days=+1)
                self[hol_date] = "Hari Raya Aidilfitri Holiday* (*estimated)"

        # Good Friday.
        if self.subdiv in ("SBH", "SWK"):
            self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Thaipusam.
        # An annual Hindu festival observed on the day of the first full moon
        # during the Tamil month of Thai
        if self.subdiv in ("JHR", "KUL", "NSN", "PJY", "PNG", "PRK", "SGR"):
            dates_obs = {
                2018: [(JAN, 31)],
                2019: [(JAN, 21)],
                2020: [(FEB, 8)],
                2021: [(JAN, 28)],
                2022: [(JAN, 18)],
                2023: [(FEB, 4)],
                2024: [(JAN, 25)],
                2025: [(FEB, 11)],
                2026: [(FEB, 1)],
                2027: [(JAN, 22)],
            }
            if year in dates_obs:
                for date_obs in dates_obs[year]:
                    hol_date = date(year, *date_obs)
                    self[hol_date] = "Thaipusam"
            else:
                hol_date = self.cnls.thaipusam_date(year)
                self[hol_date] = "Thaipusam* (*estimated)"

        # Federal Territory Day.
        if self.subdiv in ("KUL", "LBN", "PJY"):
            if year > 1973:
                self[date(year, FEB, 1)] = "Federal Territory Day"

        # State holidays (single state)
        # -----------------------------

        if self.subdiv == "JHR":
            if year > 2014:
                self[date(year, MAR, 23)] = "Birthday of the Sultan of Johor"
            for date_obs in _islamic_to_gre(year, 2, 6):
                self[date_obs] = "Hari Hol of Sultan Iskandar of Johor"

        elif self.subdiv == "KDH":
            third_sun_jun = rrule(
                MONTHLY,
                dtstart=date(year, JUN, 1),
                count=1,
                bysetpos=3,
                byweekday=SU,
            )[0]
            self[third_sun_jun] = "Birthday of The Sultan of Kedah"

        elif self.subdiv == "KTN":
            self[date(year, NOV, 11)] = "Birthday of the Sultan of Kelantan"
            self[
                date(year, NOV, 12)
            ] = "Birthday of the Sultan of Kelantan Holiday"

        elif self.subdiv == "MLK":
            self[
                date(year, APR, 15)
            ] = "Declaration of Malacca as a Historical City in Melaka"
            self[
                date(year, AUG, 24)
            ] = "Birthday of the Governor of the State of Melaka"

        elif self.subdiv == "NSN":
            self[
                date(year, JAN, 14)
            ] = "Birthday of the Sultan of Negeri Sembilan"

        elif self.subdiv == "PHG":
            self[date(year, MAY, 22)] = "Hari Hol of Pahang"
            self[date(year, JUL, 30)] = "Birthday of the Sultan of Pahang"

        elif self.subdiv == "PNG":
            self[date(year, JUL, 7)] = "George Town Heritage Day"
            second_sat_jul = rrule(
                MONTHLY,
                dtstart=date(year, JUL, 1),
                count=1,
                bysetpos=2,
                byweekday=SA,
            )[0]
            self[second_sat_jul] = "Birthday of the Governor of Penang"

        elif self.subdiv == "PRK":
            if year > 2016:
                first_fri_nov = rrule(
                    MONTHLY,
                    dtstart=date(year, NOV, 1),
                    count=1,
                    bysetpos=1,
                    byweekday=FR,
                )[0]
                self[first_fri_nov] = "Birthday of the Sultan of Perak"
            else:
                # This Holiday used to be on 27th until 2017
                # https://www.officeholidays.com/holidays/malaysia/birthday-of-the-sultan-of-perak  # noqa: E501
                self[date(year, NOV, 27)] = "Birthday of the Sultan of Perak"

        elif self.subdiv == "PLS":
            self[date(year, JUL, 17)] = "Birthday of The Raja of Perlis"

        elif self.subdiv == "SGR":
            self[date(year, DEC, 11)] = "Birthday of The Sultan of Selangor"

        elif self.subdiv == "SBH":
            first_sat_oct = rrule(
                MONTHLY,
                dtstart=date(year, OCT, 1),
                count=1,
                bysetpos=1,
                byweekday=SA,
            )[0]
            self[first_sat_oct] = "Birthday of the Governor of Sabah"
            if year > 2018:
                self[date(year, DEC, 24)] = "Christmas Eve"

        elif self.subdiv == "TRG":
            self[
                date(year, MAR, 4)
            ] = "Anniversary of the Installation of the Sultan of Terengganu"
            self[date(year, APR, 26)] = "Birthday of the Sultan of Terengganu"

    def my_islamic_to_gre(self, year: int, month: int, day: int):
        """
        Malaysia seems to have a slightly different Hijri calendar. This
        function returns the adjusted date.

        Only knows years 2000 to 2030.

        :param year: The Gregorian year.
        :param Hmonth: The Hijri (Islamic) month.
        :param Hday: The Hijri (Islamic) day.
        :return: List of Gregorian dates within the year matching the hijri day
           month, adjusted for Malaysia.
        """
        hol_dates = _islamic_to_gre(year, month, day)
        if year in (
            2003,
            2004,
            2010,
            2011,
            2013,
            2017,
            2019,
            2021,
            2024,
            2025,
            2027,
        ):
            hol_dates = [
                hol_date + timedelta(days=1) for hol_date in hol_dates
            ]
        return hol_dates


class MY(Malaysia):

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


class MYS(Malaysia):

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
