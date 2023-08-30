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
from gettext import gettext as tr

from holidays.calendars.gregorian import JUN, TUE, WED, THU, FRI, SUN
from holidays.groups import ChristianHolidays, InternationalHolidays, ObservedHolidays
from holidays.holiday_base import HolidayBase


class DominicanRepublic(HolidayBase, ChristianHolidays, InternationalHolidays, ObservedHolidays):
    """
    http://ojd.org.do/Normativas/LABORAL/Leyes/Ley%20No.%20%20139-97.pdf
    https://es.wikipedia.org/wiki/Rep%C3%BAblica_Dominicana#D%C3%ADas_festivos_nacionales
    """

    country = "DO"
    default_language = "es"
    supported_languages = ("en_US", "es", "uk")

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        ObservedHolidays.__init__(self, rule={TUE: -1, WED: -2, THU: +4, FRI: +3})
        super().__init__(*args, **kwargs)

    def _is_observed_applicable(self, dt: date) -> bool:
        # Law No. 139-97 - Holidays Dominican Republic - Jun 27, 1997
        return dt >= date(1997, JUN, 27)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("Año Nuevo"))

        # Epiphany.
        self._move_holiday(self._add_epiphany_day(tr("Día de los Santos Reyes")))

        # Lady of Altagracia.
        self._add_holiday_jan_21(tr("Día de la Altagracia"))

        # Juan Pablo Duarte Day.
        self._move_holiday(self._add_holiday_jan_26(tr("Día de Duarte")))

        # Independence Day.
        self._add_holiday_feb_27(tr("Día de Independencia"))

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        self._move_holiday(
            # Labor Day.
            self._add_labor_day(tr("Día del Trabajo")),
            rule={TUE: -1, WED: -2, THU: +4, FRI: +3, SUN: +1},
        )

        # Feast of Corpus Christi.
        self._add_corpus_christi_day(tr("Corpus Christi"))

        # Restoration Day.
        name = tr("Día de la Restauración")
        # Judgment No. 14 of Feb 20, 2008 of the Supreme Court of Justice
        if year <= 2007 and year % 4 == 0:
            self._add_holiday_aug_16(name)
        else:
            self._move_holiday(self._add_holiday_aug_16(name))

        # Our Lady of Mercedes Day.
        self._add_holiday_sep_24(tr("Día de las Mercedes"))

        # Constitution Day.
        self._move_holiday(self._add_holiday_nov_6(tr("Día de la Constitución")))

        # Christmas Day.
        self._add_christmas_day(tr("Día de Navidad"))


class DO(DominicanRepublic):
    pass


class DOM(DominicanRepublic):
    pass
