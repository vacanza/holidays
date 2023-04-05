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

from holidays.calendars import _get_nth_weekday_of_month
from holidays.constants import FEB, MAR, MAY, JUN, JUL, SUN
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Lithuania(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Lithuania holidays.

    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Lithuania
    - https://www.kalendorius.today/
    """

    country = "LT"

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year) -> None:
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day("Naujieji metai")

        # Day of Restoration of the State of Lithuania (1918).
        if year >= 1918:
            self._add_holiday("Lietuvos valstybės atkūrimo diena", FEB, 16)

        # Day of Restoration of Independence of Lithuania
        # (from the Soviet Union, 1990).
        if year >= 1990:
            self._add_holiday(
                "Lietuvos nepriklausomybės atkūrimo diena", MAR, 11
            )

        # Easter.
        self._add_easter_sunday("Velykos")

        # Easter Monday.
        self._add_easter_monday("Velykų antroji diena")

        # International Workers' Day.
        self._add_labour_day("Tarptautinė darbo diena")

        # Mother's day. First Sunday in May.
        self._add_holiday(
            "Motinos diena", _get_nth_weekday_of_month(1, SUN, MAY, year)
        )

        # Fathers's day. First Sunday in June.
        self._add_holiday(
            "Tėvo diena", _get_nth_weekday_of_month(1, SUN, JUN, year)
        )

        # St. John's Day (Christian name).
        # Day of Dew (original pagan name).
        if year >= 2003:
            self._add_saint_johns_day("Joninės, Rasos")

        # Statehood Day.
        if year >= 1991:
            self._add_holiday(
                "Valstybės (Lietuvos karaliaus Mindaugo karūnavimo) diena",
                JUL,
                6,
            )

        # Assumption Day.
        self._add_assumption_of_mary_day(
            "Žolinė (Švč. Mergelės Marijos ėmimo į dangų diena)"
        )

        # All Saints' Day.
        self._add_all_saints_day("Visų šventųjų diena (Vėlinės)")

        # All Souls' Day.
        if year >= 2020:
            self._add_all_souls_day("Mirusiųjų atminimo diena (Vėlinės)")

        # Christmas Eve.
        self._add_christmas_eve("Šv. Kūčios")

        # Christmas Day.
        self._add_christmas_day("Šv. Kalėdų pirma diena")

        # Christmas Day Two.
        self._add_christmas_day_two("Šv. Kalėdų antra diena")


class LT(Lithuania):
    pass


class LTU(Lithuania):
    pass
