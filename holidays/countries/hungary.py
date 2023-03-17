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

from holidays.constants import JAN, MAR, APR, MAY, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Hungary(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Hungary
    Codification dates:
      - https://hvg.hu/gazdasag/20170307_Megszavaztak_munkaszuneti_nap_lett_a_nagypentek  # noqa
      - https://www.tankonyvtar.hu/hu/tartalom/historia/92-10/ch01.html#id496839
    """

    country = "HU"

    def _add_with_observed_day_off(
        self,
        dt: date,
        name: str,
        since: int = 2010,
        before: bool = True,
        after: bool = True,
    ) -> None:
        # Swapped days off were in place earlier but
        # I haven't found official record yet.
        self._add_holiday(name, dt)
        # TODO: should it be a separate flag?
        if self.observed and since <= dt.year:
            if self._is_tuesday(dt) and before:
                self._add_holiday(f"{name} előtti pihenőnap", dt + td(days=-1))
            elif self._is_thursday(dt) and after:
                self._add_holiday(f"{name} utáni pihenőnap", dt + td(days=+1))

    def _populate(self, year: int) -> None:
        super()._populate(year)

        # New year's Day.
        self._add_with_observed_day_off(
            date(year, JAN, 1), "Újév", before=False, since=2014
        )

        # National Day.
        if 1945 <= year <= 1950 or 1989 <= year:
            self._add_with_observed_day_off(
                date(year, MAR, 15), "Nemzeti ünnep"
            )

        # Soviet era.
        if 1950 <= year <= 1989:
            # Proclamation of Soviet socialist governing system.
            self._add_holiday(
                "A Tanácsköztársaság kikiáltásának ünnepe", MAR, 21
            )

            # Liberation Day.
            self._add_holiday("A felszabadulás ünnepe", APR, 4)

            # Memorial day of The Great October Soviet Socialist Revolution.
            if year not in {1956, 1989}:
                self._add_holiday(
                    "A nagy októberi szocialista forradalom ünnepe", NOV, 7
                )

        easter_date = easter(year)

        # Good Friday.
        if 2017 <= year:
            self._add_holiday("Nagypéntek", easter_date + td(days=-2))

        # Easter.
        self._add_holiday("Húsvét", easter_date)

        # Second Easter Day.
        if year != 1955:
            self._add_holiday("Húsvét Hétfő", easter_date + td(days=+1))

        # Pentecost.
        self._add_holiday("Pünkösd", easter_date + td(days=+49))

        # Pentecost Monday.
        if year <= 1952 or 1992 <= year:
            self._add_holiday("Pünkösdhétfő", easter_date + td(days=+50))

        # International Workers' Day.
        if 1946 <= year:
            self._add_with_observed_day_off(
                date(year, MAY, 1), "A Munka ünnepe"
            )
        if 1950 <= year <= 1953:
            self._add_holiday("A Munka ünnepe", MAY, 2)

        # State Foundation Day.
        if 1950 <= year <= 1989:
            self._add_holiday("A kenyér ünnepe", AUG, 20)
        else:
            self._add_with_observed_day_off(
                date(year, AUG, 20), "Az államalapítás ünnepe"
            )

        # National Day.
        if 1991 <= year:
            self._add_with_observed_day_off(
                date(year, OCT, 23), "Nemzeti ünnep"
            )

        # All Saints' Day.
        if 1999 <= year:
            self._add_with_observed_day_off(
                date(year, NOV, 1), "Mindenszentek"
            )

        # Christmas Eve is not endorsed officially
        # but nowadays it is usually a day off work
        if self.observed and 2010 <= year and not self._is_weekend(DEC, 24):
            self._add_holiday("Szenteste", DEC, 24)

        # Christmas First Day.
        self._add_holiday("Karácsony", DEC, 25)

        # Christmas Second Day.
        if year != 1955:
            self._add_with_observed_day_off(
                date(year, DEC, 26),
                "Karácsony másnapja",
                since=2013,
                before=False,
            )

        # New Year's Eve.
        # Since 2014, the last day of the year is an observed day off if New
        # Year's Day falls on a Tuesday.
        dec_31 = date(year, DEC, 31)
        if self.observed and 2014 <= year and self._is_monday(dec_31):
            self._add_holiday("Szilveszter", dec_31)


class HU(Hungary):
    pass


class HUN(Hungary):
    pass
