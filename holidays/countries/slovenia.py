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

from gettext import gettext as tr

from holidays.calendars.gregorian import AUG
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Slovenia(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    Contains all work-free public holidays in Slovenia.
    No holidays are returned before year 1991 when Slovenia became independent
    country. Before that Slovenia was part of Socialist federal republic of
    Yugoslavia.

    List of holidays (including those that are not work-free:
    https://en.wikipedia.org/wiki/Public_holidays_in_Slovenia
    """

    country = "SI"
    default_language = "sl"
    supported_languages = ("en_US", "sl", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, SloveniaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1990:
            return None

        super()._populate(year)

        # New Year's Day.
        name = tr("novo leto")
        self._add_new_years_day(name)
        if year <= 2012 or year >= 2017:
            self._add_new_years_day_two(name)

        # Preseren's Day.
        self._add_holiday_feb_8(tr("Prešernov dan"))

        # Easter Monday.
        self._add_easter_monday(tr("Velikonočni ponedeljek"))

        # Day of Uprising Against Occupation.
        self._add_holiday_apr_27(tr("dan upora proti okupatorju"))

        # Labor Day.
        name = tr("praznik dela")
        self._add_labor_day(name)
        self._add_labor_day_two(name)

        # Statehood Day.
        self._add_holiday_jun_25(tr("dan državnosti"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Marijino vnebovzetje"))

        if year >= 1992:
            # Reformation Day.
            self._add_holiday_oct_31(tr("dan reformacije"))

        # Remembrance Day.
        self._add_all_saints_day(tr("dan spomina na mrtve"))

        # Christmas Day.
        self._add_christmas_day(tr("Božič"))

        # Independence and Unity Day.
        self._add_holiday_dec_26(tr("dan samostojnosti in enotnosti"))


class SI(Slovenia):
    pass


class SVN(Slovenia):
    pass


class SloveniaStaticHolidays:
    special_holidays = {
        # Solidarity Day.
        2023: (AUG, 14, tr("dan solidarnosti")),
    }
