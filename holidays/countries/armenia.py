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
    Armenia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Armenia
     - http://www.parliament.am/legislation.php?sel=show&ID=1274&lang=arm&enc=utf8  # noqa: E501
     - https://www.arlis.am/documentview.aspx?docid=259
    """

    country = "AM"
    default_language = "hy"

    def _populate(self, year):
        if year <= 1990:
            return None

        super()._populate(year)

        # New Year's Day.
        name = self.tr("Նոր տարվա օր")
        self[date(year, JAN, 1)] = name
        self[date(year, JAN, 2)] = name

        # Christmas and Epiphany Day.
        self[date(year, JAN, 6)] = self.tr("Սուրբ Ծնունդ եւ Հայտնություն")

        if 2010 <= year <= 2021:
            # New Year's holidays and Christmas Eve.
            self[date(year, JAN, 3)] = name
            self[date(year, JAN, 4)] = name
            # Christmas Eve.
            self[date(year, JAN, 5)] = self.tr("Սուրբ Ծննդյան տոներ")

            # The Day of Remembrance of the Dead.
            self[date(year, JAN, 7)] = self.tr("Մեռելոց հիշատակի օր")

        if year >= 2003:
            # Army Day.
            self[date(year, JAN, 28)] = self.tr("Բանակի օր")

        # Women's Day.
        self[date(year, MAR, 8)] = self.tr("Կանանց տոն")

        if 1994 <= year <= 2001:
            # Motherhood and Beauty Day.
            self[date(year, APR, 7)] = self.tr("Մայրության և գեղեցկության տոն")

        # Armenian Genocide Remembrance Day,
        self[date(year, APR, 24)] = self.tr("Եղեռնի զոհերի հիշատակի օր")

        if year >= 2001:
            # International Day of Workers' Solidarity.
            name = self.tr("Աշխատավորների համերաշխության միջազգային օր")
            if year >= 2002:
                # Labor Day.
                name = self.tr("Աշխատանքի օր")
            self[date(year, MAY, 1)] = name

        if year >= 1995:
            # Victory and Peace Day.
            self[date(year, MAY, 9)] = self.tr("Հաղթանակի և Խաղաղության տոն")

        # Republic Day.
        self[date(year, MAY, 28)] = self.tr("Հանրապետության օր")

        if year >= 1996:
            # Constitution Day.
            self[date(year, JUL, 5)] = self.tr("Սահմանադրության օր")

        if year >= 1992:
            # Independence Day.
            self[date(year, SEP, 21)] = self.tr("Անկախության օր")

        # New Year's Eve.
        self[date(year, DEC, 31)] = self.tr("Նոր տարվա գիշեր")


class AM(Armenia):
    pass


class ARM(Armenia):
    pass
