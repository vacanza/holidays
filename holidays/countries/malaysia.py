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
from typing import Iterable, Optional, Union

from dateutil.easter import easter
from dateutil.relativedelta import FR, MO, SA, SU
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC, FRI, SAT, SUN
from holidays.holiday_base import HolidayBase
from holidays.utils import _ChineseLuniSolar, _islamic_to_gre


class Malaysia(HolidayBase):
    country = "MY"
    special_holidays = {
        # The years 1955 1959 1995 seems to have the elections
        # one weekday but I am not sure if they were marked as
        # holidays.
        1999: ((NOV, 29, "Malaysia General Election Holiday"),),
        2018: ((MAY, 9, "Malaysia General Election Holiday"),),
        2019: ((JUL, 30, "Installation of New King"),),
    }
    subdivisions = [
        "JHR",
        "KDH",
        "KTN",
        "KUL",
        "LBN",
        "MLK",
        "NSN",
        "PHG",
        "PJY",
        "PLS",
        "PNG",
        "PRK",
        "SBH",
        "SGR",
        "SWK",
        "TRG",
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
        def _add_holiday(dt: date, hol: str) -> None:
            if dt.year == year:
                self[dt] = hol

        super()._populate(year)

        estimated_suffix = "* (*estimated)"

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
            2004: (MAY, 3),
            2005: (MAY, 23),
            2006: (MAY, 12),
            2007: (MAY, 1),
            2008: (MAY, 19),
            2009: (MAY, 9),
            2010: (MAY, 28),
            2011: (MAY, 17),
            2012: (MAY, 5),
            2013: (MAY, 24),
            2014: (MAY, 13),
            2015: (MAY, 3),
            2016: (MAY, 21),
            2017: (MAY, 10),
            2018: (MAY, 29),
            2019: (MAY, 19),
            2020: (MAY, 7),
            2021: (MAY, 26),
            2022: (MAY, 15),
        }
        name = "Vesak Day"
        if year in dates_obs:
            hol_date = date(year, *dates_obs[year])
        else:
            hol_date = self.cnls.vesak_may_date(year)
            name += estimated_suffix
        self[hol_date] = name

        # Labour Day.
        self[date(year, MAY, 1)] = "Labour Day"

        # Birthday of [His Majesty] the Yang di-Pertuan Agong.
        if year <= 2017:
            hol_date = date(year, JUN, 1) + rd(weekday=SA)
        elif year == 2018:
            hol_date = date(2018, SEP, 9)
        elif year == 2020:
            # https://www.nst.com.my/news/nation/2020/03/571660/agongs-birthday-moved-june-6-june-8
            hol_date = date(2020, JUN, 8)
        else:
            hol_date = date(year, JUN, 1) + rd(weekday=MO)
        self[hol_date] = "Birthday of SPB Yang di-Pertuan Agong"

        # Hari Kebangsaan or National Day.
        self[date(year, AUG, 31)] = "National Day"

        # Malaysia Day.
        if year >= 2010:
            self[date(year, SEP, 16)] = "Malaysia Day"

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
            name = "Deepavali"
            if year in dates_obs:
                hol_date = date(year, *dates_obs[year])
            else:
                hol_date = self.cnls.s_diwali_date(year)
                name += estimated_suffix
            self[hol_date] = name

        # Christmas day.
        self[date(year, DEC, 25)] = "Christmas Day"

        # Birthday of the Prophet Muhammad (s.a.w.).
        # a.k.a. Hari Keputeraan Nabi Muhammad (Sabah Act)
        dates_obs = {
            2001: ((JUN, 4),),
            2002: ((MAY, 24),),
            2003: ((MAY, 14),),
            2004: ((MAY, 2),),
            2005: ((APR, 21),),
            2006: ((APR, 11),),
            2007: ((MAR, 31),),
            2008: ((MAR, 20),),
            2009: ((MAR, 9),),
            2010: ((FEB, 26),),
            2011: ((FEB, 16),),
            2012: ((FEB, 5),),
            2013: ((JAN, 24),),
            2014: ((JAN, 14),),
            2015: (
                (JAN, 3),
                (DEC, 24),
            ),
            2016: ((DEC, 12),),
            2017: ((DEC, 1),),
            2018: ((NOV, 20),),
            2019: ((NOV, 9),),
            2020: ((OCT, 29),),
            2021: ((OCT, 19),),
            2022: ((OCT, 10),),
        }
        name = "Maulidur Rasul (Birthday of the Prophet Muhammad)"
        if year in dates_obs:
            hol_dates = [
                (date(year, *date_obs), "") for date_obs in dates_obs[year]
            ]
        else:
            hol_dates = [
                (date_obs, estimated_suffix)
                for date_obs in _islamic_to_gre(year, 3, 12)
            ]
        for hol_date, hol_suffix in hol_dates:
            self[hol_date] = name + hol_suffix

        # Hari Raya Puasa (2 days).
        # aka Eid al-Fitr;
        # exact date of observance is announced yearly
        dates_obs = {
            2001: ((DEC, 17),),
            2002: ((DEC, 6),),
            2003: ((NOV, 26),),
            2004: ((NOV, 14),),
            2005: ((NOV, 3),),
            2006: ((OCT, 24),),
            2007: ((OCT, 13),),
            2008: ((OCT, 1),),
            2009: ((SEP, 20),),
            2010: ((SEP, 10),),
            2011: ((AUG, 31),),
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
        }
        name = "Hari Raya Puasa"
        hol_dates = []
        for yr in (year - 1, year):
            if yr in dates_obs:
                for date_obs in dates_obs[yr]:
                    hol_dates.append((date(yr, *date_obs), ""))
            else:
                for date_obs in _islamic_to_gre(year, 10, 1):
                    hol_dates.append((date_obs, estimated_suffix))
        for hol_date, hol_suffix in hol_dates:
            _add_holiday(hol_date, f"{name}{hol_suffix}")
            _add_holiday(
                hol_date + rd(days=+1), f"Second day of {name}{hol_suffix}"
            )

        # Hari Raya Haji and Arafat Day.
        # Date of observance is announced yearly.
        dates_obs = {
            2001: ((MAR, 6),),
            2002: ((FEB, 23),),
            2003: ((FEB, 12),),
            2004: ((FEB, 2),),
            2005: ((JAN, 21),),
            2006: (
                (JAN, 10),
                (DEC, 31),
            ),
            2007: ((DEC, 20),),
            2008: ((DEC, 9),),
            2009: ((NOV, 28),),
            2010: ((NOV, 17),),
            2011: ((NOV, 7),),
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
        }
        name = "Hari Raya Haji"
        hol_dates = []
        for yr in (year - 1, year):
            if yr in dates_obs:
                for date_obs in dates_obs[yr]:
                    hol_dates.append((date(yr, *date_obs), ""))
            else:
                for date_obs in _islamic_to_gre(year, 12, 10):
                    hol_dates.append((date_obs, estimated_suffix))
        for hol_date, hol_suffix in hol_dates:
            _add_holiday(hol_date, f"{name}{hol_suffix}")
            if self.subdiv == "TRG":
                # Arafat Day is one day before Eid al-Adha
                _add_holiday(hol_date + rd(days=-1), f"Arafat Day{hol_suffix}")
            if self.subdiv in {"KDH", "KTN", "PLS", "TRG"}:
                # Second day
                _add_holiday(
                    hol_date + rd(days=+1), f"{name} Holiday{hol_suffix}"
                )

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
            second_sat_oct = date(year, OCT, 1) + rd(weekday=SA(+2))
            self[second_sat_oct] = "Birthday of the Governor of Sarawak"

            # Sarawak Independence Day
            if year >= 2017:
                self[date(year, JUL, 22)] = "Sarawak Day"

        # New Year's Day
        if self.subdiv in {
            "KUL",
            "LBN",
            "MLK",
            "NSN",
            "PHG",
            "PJY",
            "PNG",
            "PRK",
            "SBH",
            "SGR",
            "SWK",
        }:
            self[date(year, JAN, 1)] = "New Year's Day"

        # Isra and Mi'raj.
        if self.subdiv in {"KDH", "NSN", "PLS"} or (
            self.subdiv == "TRG" and year >= 2020
        ):
            dates_obs = {
                2001: ((OCT, 15),),
                2002: ((OCT, 4),),
                2003: ((SEP, 24),),
                2004: ((SEP, 12),),
                2005: ((SEP, 1),),
                2006: ((AUG, 22),),
                2007: ((AUG, 11),),
                2008: ((JUL, 31),),
                2009: ((JUL, 20),),
                2010: ((JUL, 9),),
                2011: ((JUN, 29),),
                2012: ((JUN, 17),),
                2013: ((JUN, 6),),
                2014: ((MAY, 27),),
                2015: ((MAY, 16),),
                2016: ((MAY, 5),),
                2017: ((APR, 24),),
                2018: ((APR, 14),),
                2019: ((APR, 3),),
                2020: ((MAR, 22),),
                2021: ((MAR, 11),),
                2022: ((MAR, 1),),
            }
            name = "Isra and Mi'raj"
            if year in dates_obs:
                hol_dates = [
                    (date(year, *date_obs), "") for date_obs in dates_obs[year]
                ]
            else:
                hol_dates = [
                    (date_obs, estimated_suffix)
                    for date_obs in _islamic_to_gre(year, 7, 27)
                ]
            for hol_date, hol_suffix in hol_dates:
                self[hol_date] = name + hol_suffix

        # Beginning of Ramadan.
        if self.subdiv in {"JHR", "KDH", "MLK"}:
            dates_obs = {
                2001: ((NOV, 17),),
                2002: ((NOV, 6),),
                2003: ((OCT, 27),),
                2004: ((OCT, 16),),
                2005: ((OCT, 5),),
                2006: ((SEP, 24),),
                2007: ((SEP, 13),),
                2008: ((SEP, 2),),
                2009: ((AUG, 22),),
                2010: ((AUG, 11),),
                2011: ((AUG, 1),),
                2012: ((JUL, 20),),
                2013: ((JUL, 9),),
                2014: ((JUN, 29),),
                2015: ((JUN, 18),),
                2016: ((JUN, 7),),
                2017: ((MAY, 27),),
                2018: ((MAY, 17),),
                2019: ((MAY, 6),),
                2020: ((APR, 24),),
                2021: ((APR, 13),),
                2022: ((APR, 3),),
            }
            name = "Beginning of Ramadan"
            if year in dates_obs:
                hol_dates = [
                    (date(year, *date_obs), "") for date_obs in dates_obs[year]
                ]
            else:
                hol_dates = [
                    (date_obs, estimated_suffix)
                    for date_obs in _islamic_to_gre(year, 9, 1)
                ]
            for hol_date, hol_suffix in hol_dates:
                self[hol_date] = name + hol_suffix

        # Nuzul Al-Quran Day.
        if self.subdiv in {
            "KTN",
            "KUL",
            "LBN",
            "PHG",
            "PNG",
            "PRK",
            "PLS",
            "PJY",
            "SGR",
            "TRG",
        }:
            dates_obs = {
                2001: ((DEC, 3),),
                2002: ((NOV, 22),),
                2003: ((NOV, 12),),
                2004: ((NOV, 1),),
                2005: ((OCT, 21),),
                2006: ((OCT, 10),),
                2007: ((SEP, 29),),
                2008: ((SEP, 18),),
                2009: ((SEP, 7),),
                2010: ((AUG, 27),),
                2011: ((AUG, 17),),
                2012: ((AUG, 5),),
                2013: ((JUL, 25),),
                2014: ((JUL, 15),),
                2015: ((JUL, 4),),
                2016: ((JUN, 22),),
                2017: ((JUN, 12),),
                2018: ((JUN, 2),),
                2019: ((MAY, 22),),
                2020: ((MAY, 10),),
                2021: ((APR, 29),),
                2022: ((APR, 19),),
            }
            name = "Nuzul Al-Quran Day"
            if year in dates_obs:
                hol_dates = [
                    (date(year, *date_obs), "") for date_obs in dates_obs[year]
                ]
            else:
                hol_dates = [
                    (date_obs, estimated_suffix)
                    for date_obs in _islamic_to_gre(year, 9, 17)
                ]
            for hol_date, hol_suffix in hol_dates:
                self[hol_date] = name + hol_suffix

        # Thaipusam.
        # An annual Hindu festival observed on the day of the first full moon
        # during the Tamil month of Thai
        if self.subdiv in {"JHR", "KUL", "NSN", "PJY", "PNG", "PRK", "SGR"}:
            dates_obs = {
                2018: (JAN, 31),
                2019: (JAN, 21),
                2020: (FEB, 8),
                2021: (JAN, 28),
                2022: (JAN, 18),
                2023: (FEB, 5),
                2024: (JAN, 25),
                2025: (FEB, 11),
                2026: (FEB, 1),
                2027: (JAN, 22),
            }
            name = "Thaipusam"
            if year in dates_obs:
                hol_date = date(year, *dates_obs[year])
            else:
                hol_date = self.cnls.thaipusam_date(year)
                name += estimated_suffix
            self[hol_date] = name

        # Federal Territory Day.
        if self.subdiv in {"KUL", "LBN", "PJY"} and year >= 1974:
            self[date(year, FEB, 1)] = "Federal Territory Day"

        # State holidays (single state)

        if self.subdiv == "MLK":
            if year >= 1989:
                self[
                    date(year, APR, 15)
                ] = "Declaration of Malacca as a Historical City"
            if year >= 2020:
                hol_date = date(year, AUG, 24)
            else:
                hol_date = date(year, OCT, 1) + rd(weekday=FR(+2))
            self[hol_date] = "Birthday of the Governor of Malacca"

        elif self.subdiv == "NSN":
            if year >= 2009:
                self[
                    date(year, JAN, 14)
                ] = "Birthday of the Sultan of Negeri Sembilan"

        elif self.subdiv == "PHG":
            if year >= 2020:
                hol_date = date(year, MAY, 22)
            else:
                hol_date = date(year, MAY, 7)
            self[hol_date] = "Hari Hol of Pahang"

            if year >= 2019:
                hol_date = date(year, JUL, 30)
            elif 1975 <= year <= 2018:
                hol_date = date(year, OCT, 24)
            self[hol_date] = "Birthday of the Sultan of Pahang"

        elif self.subdiv == "PNG":
            if year >= 2009:
                self[date(year, JUL, 7)] = "George Town Heritage Day"
            second_sat_jul = date(year, JUL, 1) + rd(weekday=SA(+2))
            self[second_sat_jul] = "Birthday of the Governor of Penang"

        elif self.subdiv == "PLS":
            if year >= 2018:
                hol_date = date(year, JUL, 17)
            elif year >= 2000:
                hol_date = date(year, MAY, 17)
            self[hol_date] = "Birthday of The Raja of Perlis"

        elif self.subdiv == "SGR":
            self[date(year, DEC, 11)] = "Birthday of The Sultan of Selangor"

        elif self.subdiv == "TRG":
            if year >= 2000:
                self[date(year, MAR, 4)] = (
                    "Anniversary of the Installation "
                    "of the Sultan of Terengganu"
                )
                self[
                    date(year, APR, 26)
                ] = "Birthday of the Sultan of Terengganu"

        # Check for holidays that fall on a Sunday and
        # implement Section 3 of Malaysian Holidays Act:
        # "if any day specified in the Schedule falls on
        # Sunday then the day following shall be a public
        # holiday and if such day is already a public holiday,
        # then the day following shall be a public holiday"
        # In Johor and Kedah it's Friday -> Sunday,
        # in Kelantan and Terengganu it's Saturday -> Sunday
        for hol_date, hol_name in list(self.items()):
            if hol_date.year != year:
                continue
            in_lieu_date = None
            if hol_date.weekday() == FRI and self.subdiv in {"JHR", "KDH"}:
                in_lieu_date = hol_date + rd(days=+2)
            elif hol_date.weekday() == SAT and self.subdiv in {
                "KTN",
                "TRG",
            }:
                in_lieu_date = hol_date + rd(days=+1)
            elif hol_date.weekday() == SUN and self.subdiv not in {
                "JHR",
                "KDH",
                "KTN",
                "TRG",
            }:
                in_lieu_date = hol_date + rd(days=+1)
            if not in_lieu_date:
                continue
            while in_lieu_date.year == year and in_lieu_date in self:
                in_lieu_date += rd(days=+1)
            _add_holiday(in_lieu_date, f"{hol_name} [In lieu]")

        # The last two days in May (Pesta Kaamatan).
        # (Sarawak Act)
        # Day following a Sunday is not a holiday
        if self.subdiv in {"LBN", "SBH"}:
            self[date(year, MAY, 30)] = "Pesta Kaamatan"
            self[date(year, MAY, 31)] = "Pesta Kaamatan (Second day)"

        # ------------------------------#
        # Other holidays (decrees etc.) #
        # ------------------------------#

        # Awal Muharram.
        dates_obs = {
            2001: ((MAR, 26),),
            2002: ((MAR, 15),),
            2003: ((MAR, 5),),
            2004: ((FEB, 22),),
            2005: ((FEB, 10),),
            2006: ((JAN, 31),),
            2007: ((JAN, 20),),
            2008: (
                (JAN, 10),
                (DEC, 29),
            ),
            2009: ((DEC, 18),),
            2010: ((DEC, 8),),
            2011: ((NOV, 27),),
            2012: ((NOV, 15),),
            2013: ((NOV, 5),),
            2014: ((OCT, 25),),
            2015: ((OCT, 14),),
            2016: ((OCT, 2),),
            2017: ((SEP, 22),),
            2018: ((SEP, 11),),
            2019: ((SEP, 1),),
            2020: ((AUG, 20),),
            2021: ((AUG, 10),),
            2022: ((JUL, 30),),
        }
        name = "Awal Muharram (Hijri New Year)"
        if year in dates_obs:
            hol_dates = [
                (date(year, *date_obs), "") for date_obs in dates_obs[year]
            ]
        else:
            hol_dates = [
                (date_obs, estimated_suffix)
                for date_obs in _islamic_to_gre(year, 1, 1)
            ]
        for hol_date, hol_suffix in hol_dates:
            self[hol_date] = name + hol_suffix

        # Special holidays (states)
        if year == 2021 and self.subdiv in {"KUL", "LBN", "PJY"}:
            self[date(2021, DEC, 3)] = "Malaysia Cup Holiday"

        if year == 2022 and self.subdiv == "KDH":
            self[date(2022, JAN, 18)] = "Thaipusam"

        if year == 2022 and self.subdiv in {
            "JHR",
            "KDH",
            "KTN",
            "TRG",
        }:
            self[date(2022, MAY, 4)] = "Labour Day Holiday"

        # ---------------------------------#
        # State holidays (multiple states) #
        # ---------------------------------#

        # Good Friday.
        if self.subdiv in {"SBH", "SWK"}:
            self[easter(year) + rd(days=-2)] = "Good Friday"

        # -----------------------------
        # State holidays (single state)
        # -----------------------------

        if self.subdiv == "JHR":
            if year >= 2015:
                self[date(year, MAR, 23)] = "Birthday of the Sultan of Johor"
            if year >= 2011:
                dates_obs = {
                    2011: ((JAN, 12),),
                    2012: ((JAN, 1), (DEC, 20)),
                    2013: ((DEC, 10),),
                    2014: ((NOV, 29),),
                    2015: ((NOV, 19),),
                    2016: ((NOV, 7),),
                    2017: ((OCT, 27),),
                    2018: ((OCT, 15),),
                    2019: ((OCT, 5),),
                    2020: ((SEP, 24),),
                    2021: ((SEP, 13),),
                    2022: ((SEP, 3),),
                }
                name = "Hari Hol of Sultan Iskandar of Johor"
                if year in dates_obs:
                    hol_dates = [
                        (date(year, *date_obs), "")
                        for date_obs in dates_obs[year]
                    ]
                else:
                    hol_dates = [
                        (date_obs, estimated_suffix)
                        for date_obs in _islamic_to_gre(year, 2, 6)
                    ]
                for hol_date, hol_suffix in hol_dates:
                    self[hol_date] = name + hol_suffix

        elif self.subdiv == "KDH":
            if year >= 2020:
                third_sun_jun = date(year, JUN, 1) + rd(weekday=SU(+3))
                self[third_sun_jun] = "Birthday of The Sultan of Kedah"

        elif self.subdiv == "KTN":
            if year >= 2010:
                name = "Birthday of the Sultan of Kelantan"
                self[date(year, NOV, 11)] = name
                self[date(year, NOV, 12)] = name

        elif self.subdiv == "PRK":
            # This Holiday used to be on 27th until 2017
            # https://www.officeholidays.com/holidays/malaysia/birthday-of-the-sultan-of-perak  # noqa: E501
            if year >= 2018:
                first_fri_nov = date(year, NOV, 1) + rd(weekday=FR)
                self[first_fri_nov] = "Birthday of the Sultan of Perak"
            else:
                self[date(year, NOV, 27)] = "Birthday of the Sultan of Perak"

        elif self.subdiv == "SBH":
            first_sat_oct = date(year, OCT, 1) + rd(weekday=SA)
            self[first_sat_oct] = "Birthday of the Governor of Sabah"
            if year >= 2019:
                self[date(year, DEC, 24)] = "Christmas Eve"


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
