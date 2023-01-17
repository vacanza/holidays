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

from holidays.constants import JAN, MAR, APR, MAY, JUL, SEP, DEC
from holidays.holiday_base import HolidayBase


class Armenia(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Armenia
    http://www.parliament.am/legislation.php?sel=show&ID=1274&lang=arm&enc=utf8
    https://www.arlis.am/documentview.aspx?docid=259
    """

    country = "AM"

    def _populate(self, year):

        if year <= 1990:
            return
        super()._populate(year)

        # New Year's Day
        name = "Ամանոր [New Year's Day]"
        self[date(year, JAN, 1)] = name
        self[date(year, JAN, 2)] = name

        # Christmas and Epiphany Day
        self[
            date(year, JAN, 6)
        ] = "Սուրբ Ծնունդ եւ Հայտնություն [Christmas and Epiphany Day]"

        if 2010 <= year <= 2021:
            # New Year's holidays and Christmas Eve
            self[date(year, JAN, 3)] = name
            self[date(year, JAN, 4)] = name
            self[date(year, JAN, 5)] = "նախածննդյան տոներ [Christmas Eve]"

            # The Day of Remembrance of the Dead
            self[
                date(year, JAN, 7)
            ] = "Մեռելոց հիշատակի օր [The Day of Remembrance of the Dead]"

        # Army Day
        if year >= 2003:
            self[date(year, JAN, 28)] = "Բանակի օր [Army Day]"

        # Women's Day
        self[date(year, MAR, 8)] = "Կանանց տոն [Women's Day]"

        # Motherhood and Beauty Day
        if 1994 <= year <= 2001:
            self[
                date(year, APR, 7)
            ] = "Մայրության և գեղեցկության տոն [Motherhood and Beauty Day]"

        # Armenian Genocide Remembrance Day
        self[
            date(year, APR, 24)
        ] = "Եղեռնի զոհերի հիշատակի օր [Armenian Genocide Remembrance Day]"

        # Labour Day
        if year >= 2001:
            name = (
                "Աշխատավորների համերաշխության միջազգային օր "
                "[International Day of Workers' Solidarity]"
            )
            if year >= 2002:
                name = "Աշխատանքի օր [Labour Day]"
            self[date(year, MAY, 1)] = name

        # Victory and Peace Day
        if year >= 1995:
            self[
                date(year, MAY, 9)
            ] = "Հաղթանակի և Խաղաղության տոն [Victory and Peace Day]"

        # Republic Day
        self[date(year, MAY, 28)] = "Հանրապետության օր [Republic Day]"

        # Constitution Day
        if year >= 1996:
            self[date(year, JUL, 5)] = "Սահմանադրության օր [Constitution Day]"

        # Independence Day
        if year >= 1992:
            self[date(year, SEP, 21)] = "Անկախության օր [Independence Day]"

        # New Year's Eve
        self[date(year, DEC, 31)] = "Ամանոր [New Year's Eve]"


class AM(Armenia):
    pass


class ARM(Armenia):
    pass
