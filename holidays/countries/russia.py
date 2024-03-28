#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, FEB, MAY
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Russia(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Russia
    """

    country = "RU"
    default_language = "ru"
    supported_languages = ("en_US", "ru")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, RussiaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1990:
            return None

        if self._year <= 2004:
            # New Year's Day.
            name = tr("Новый год")
            self._add_new_years_day(name)
            if self._year >= 1993:
                self._add_new_years_day_two(name)
        else:
            # New Year Holidays.
            name = tr("Новогодние каникулы")
            for day in range(1, 6):
                self._add_holiday(name, JAN, day)
            if self._year >= 2013:
                self._add_holiday_jan_6(name)
                self._add_holiday_jan_8(name)

        # Christmas Day.
        self._add_christmas_day(tr("Рождество Христово"))

        if self._year >= 2002:
            # Defender of the Fatherland Day.
            self._add_holiday_feb_23(tr("День защитника Отечества"))

        # International Women's Day.
        self._add_womens_day(tr("Международный женский день"))

        name = (
            # Holiday of Spring and Labor.
            tr("Праздник Весны и Труда")
            if self._year >= 1992
            # International Workers' Solidarity Day.
            else tr("День международной солидарности трудящихся")
        )
        self._add_labor_day(name)
        if self._year <= 2004:
            self._add_labor_day_two(name)

        # Victory Day.
        self._add_world_war_two_victory_day(tr("День Победы"))

        if self._year >= 1992:
            self._add_holiday_jun_12(
                # Russia Day.
                tr("День России")
                if self._year >= 2002
                # Day of the Adoption of the Declaration of Sovereignty of the Russian Federation.
                else tr(
                    "День принятия Декларации о государственном суверенитете Российской Федерации"
                )
            )

        if self._year >= 2005:
            # Unity Day.
            self._add_holiday_nov_4(tr("День народного единства"))

        if self._year <= 2004:
            name = (
                # Day of consent and reconciliation.
                tr("День согласия и примирения")
                if self._year >= 1996
                # Anniversary of the Great October Socialist Revolution.
                else tr("Годовщина Великой Октябрьской социалистической революции")
            )
            self._add_holiday_nov_7(name)
            if self._year <= 1991:
                self._add_holiday_nov_8(name)


class RU(Russia):
    pass


class RUS(Russia):
    pass


class RussiaStaticHolidays:
    special_public_holidays = {
        # Bridge days for 01/01/2023 and 08/01/2023.
        # src: https://www.consultant.ru/document/cons_doc_LAW_425407/
        2023: (
            (FEB, 24, tr("День защитника Отечества")),
            (MAY, 8, tr("День Победы")),
        ),
    }
