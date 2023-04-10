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

from holidays.calendars import GREGORIAN_CALENDAR, JULIAN_CALENDAR
from holidays.constants import JUN, AUG
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Moldova(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Moldova
    https://www.legis.md/cautare/getResults?doc_id=133686
    """

    country = "MD"
    default_language = "ro"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1990:
            return None
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("Anul Nou"))

        name = (
            # Christmas (by old style).
            tr("Naşterea lui Iisus Hristos (Crăciunul pe stil vechi)")
            if year >= 2014
            # Christmas.
            else tr("Naşterea lui Iisus Hristos (Crăciunul)")
        )
        self._add_christmas_day(name)
        self._add_christmas_day_two(name)

        # International Women's Day.
        self._add_womens_day(tr("Ziua internatională a femeii"))

        # Easter.
        name = tr("Paştele")
        self._add_easter_sunday(name)
        self._add_easter_monday(name)

        self._add_holiday(
            # Day of Rejoicing.
            tr("Paştele blajinilor"),
            self._easter_sunday + td(days=+8),
        )

        self._add_labour_day(
            # International Workers' Solidarity Day.
            tr("Ziua internaţională a solidarităţii oamenilor muncii")
        )

        may_9 = self._add_world_war_two_victory_day(
            # Victory Day and Commemoration of the heroes fallen for
            # Independence of Fatherland.
            tr(
                "Ziua Victoriei şi a comemorării eroilor căzuţi pentru "
                "Independenţa Patriei"
            )
        )

        if year >= 2017:
            # Europe Day.
            self._add_holiday(tr("Ziua Europei"), may_9)

        if year >= 2016:
            # International Children's Day
            self._add_holiday(tr("Ziua Ocrotirii Copilului"), JUN, 1)

        # Republic of Moldova Independence Day
        self._add_holiday(tr("Ziua independenţei Republicii Moldova"), AUG, 27)

        # National Language Day.
        self._add_holiday(tr("Limba noastră"), AUG, 31)

        if year >= 2013:
            self._add_christmas_day(
                # Christmas (by new style).
                tr("Naşterea lui Iisus Hristos (Crăciunul pe stil nou)"),
                GREGORIAN_CALENDAR,
            )


class MD(Moldova):
    pass


class MDA(Moldova):
    pass
