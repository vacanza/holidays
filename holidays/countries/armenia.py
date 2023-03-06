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

from holidays.calendars import JULIAN_CALENDAR
from holidays.constants import JAN, APR, MAY, JUL, SEP
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Armenia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Armenia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Armenia
     - http://www.parliament.am/legislation.php?sel=show&ID=1274&lang=arm&enc=utf8  # noqa: E501
     - https://www.arlis.am/documentview.aspx?docid=259
    """

    country = "AM"
    default_language = "hy"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1990:
            return None

        super()._populate(year)

        # New Year's Day.
        name = _("Նոր տարվա օր")
        self._add_new_years_day(name)
        self._add_new_years_day_two(name)

        # Christmas. Epiphany Day.
        self._add_holiday(_("Սուրբ Ծնունդ եւ Հայտնություն"), JAN, 6)

        if 2010 <= year <= 2021:
            self._add_new_years_day_three(name)
            self._add_new_years_day_four(name)

            # Christmas Eve.
            self._add_holiday(_("Սուրբ Ծննդյան տոներ"), JAN, 5)

            # The Day of Remembrance of the Dead.
            self._add_holiday(_("Մեռելոց հիշատակի օր"), JAN, 7)

        if year >= 2003:
            # Army Day.
            self._add_holiday(_("Բանակի օր"), JAN, 28)

        # Women's Day.
        self._add_womens_day(_("Կանանց տոն"))

        if 1994 <= year <= 2001:
            # Motherhood and Beauty Day.
            self._add_holiday(_("Մայրության և գեղեցկության տոն"), APR, 7)

        # Armenian Genocide Remembrance Day,
        self._add_holiday(_("Եղեռնի զոհերի հիշատակի օր"), APR, 24)

        if year >= 2001:
            self._add_labour_day(
                # Labor Day.
                _("Աշխատանքի օր")
                if year >= 2002
                # International Day of Workers' Solidarity.
                else _("Աշխատավորների համերաշխության միջազգային օր")
            )

        if year >= 1995:
            # Victory and Peace Day.
            self._add_holiday(_("Հաղթանակի և Խաղաղության տոն"), MAY, 9)

        # Republic Day.
        self._add_holiday(_("Հանրապետության օր"), MAY, 28)

        if year >= 1996:
            # Constitution Day.
            self._add_holiday(_("Սահմանադրության օր"), JUL, 5)

        if year >= 1992:
            # Independence Day.
            self._add_holiday(_("Անկախության օր"), SEP, 21)

        # New Year's Eve.
        self._add_new_years_eve(_("Նոր տարվա գիշեր"))


class AM(Armenia):
    pass


class ARM(Armenia):
    pass
