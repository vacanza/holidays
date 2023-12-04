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
from gettext import gettext as tr

from holidays.calendars.gregorian import MAY, SUN, _get_nth_weekday_of_month
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Madagascar(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
        - https://www.officeholidays.com/countries/madagascar
        - https://www.timeanddate.com/holidays/madagascar/
    """

    country = "MG"
    default_language = "mg"
    supported_languages = ("en_US", "mg", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # Observed since 1947
        if year <= 1946:
            return None

        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("Taom-baovao"))

        # Women's Day.
        self._add_womens_day(tr("Fetin'ny vehivavy"))

        # Martyrs' Day.
        self._add_holiday_mar_29(tr("Fetin'ny mahery fo"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Fetin'ny paska"))

        # Easter Monday.
        self._add_easter_monday(tr("Alatsinain'ny paska"))

        # Labor Day.
        self._add_labor_day(tr("Fetin'ny asa"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Fiakaran'ny Jesosy kristy tany an-danitra"))

        # Whit Sunday.
        whit_sunday = self._add_whit_sunday(tr("Pentekosta"))

        # Whit Monday.
        self._add_whit_monday(tr("Alatsinain'ny pentekosta"))

        last_sun_of_may = _get_nth_weekday_of_month(-1, SUN, MAY, self._year)
        # Mother's Day.
        self._add_holiday(
            tr("Fetin'ny reny"),
            last_sun_of_may + td(days=+7) if last_sun_of_may == whit_sunday else last_sun_of_may,
        )

        # Father's Day.
        self._add_holiday_3rd_sun_of_jun(tr("Fetin'ny ray"))

        if year >= 1960:
            # Independence Day.
            self._add_holiday_jun_26(tr("Fetin'ny fahaleovantena"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Fiakaran'ny Masina Maria tany an-danitra"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Fetin'ny olo-masina"))

        if year >= 2011:
            # Republic Day.
            self._add_holiday_dec_11(tr("Fetin'ny Repoblika"))

        # Christmas Day.
        self._add_christmas_day(tr("Fetin'ny noely"))


class MG(Madagascar):
    pass


class MDG(Madagascar):
    pass
