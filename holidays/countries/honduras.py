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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Honduras(HolidayBase, ChristianHolidays, InternationalHolidays):
    # Artículo 339 del Código del Trabajo:
    # https://www.ilo.org/dyn/natlex/docs/WEBTEXT/29076/64849/S59HND01.htm

    country = "HN"
    default_language = "es"
    supported_languages = ("en_US", "es", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Año Nuevo"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Jueves Santo"))

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Holy Saturday.
        self._add_holy_saturday(tr("Sábado de Gloria"))

        # Panamerican Day.
        self._add_holiday_apr_14(tr("Día de las Américas"))

        # Labor Day.
        self._add_labor_day(tr("Día del Trabajo"))

        # Independence Day.
        self._add_holiday_sep_15(tr("Día de la Independencia"))

        # https://www.tsc.gob.hn/web/leyes/Decreto_78-2015_Traslado_de_Feriados_Octubre.pdf
        if self._year <= 2014:
            # Morazan's Day.
            self._add_holiday_oct_3(tr("Día de Morazán"))

            # Columbus Day.
            self._add_columbus_day(tr("Día de la Raza"))

            # Army Day.
            self._add_holiday_oct_21(tr("Día de las Fuerzas Armadas"))
        else:
            # Morazan Weekend.
            name = tr("Semana Morazánica")
            # First Wednesday of October from 12 noon to Saturday 12 noon.
            first_wed_of_oct = self._add_holiday_1st_wed_of_oct(name)
            self._add_holiday(name, first_wed_of_oct + td(days=+1))
            self._add_holiday(name, first_wed_of_oct + td(days=+2))

        # Christmas Day.
        self._add_christmas_day(tr("Navidad"))


class HN(Honduras):
    pass


class HND(Honduras):
    pass
