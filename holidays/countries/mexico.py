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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Mexico(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Mexico
    - https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_festivos_en_M%C3%A9xico
    - https://www.gob.mx/cms/uploads/attachment/file/156203/1044_Ley_Federal_del_Trabajo.pdf
    - http://www.diputados.gob.mx/LeyesBiblio/ref/lft/LFT_orig_01abr70_ima.pdf
    """

    country = "MX"
    default_language = "es"
    supported_languages = ("en_US", "es", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("Año Nuevo"))

        if year >= 1917:
            # Constitution Day.
            name = tr("Día de la Constitución")
            if year >= 2006:
                self._add_holiday_1st_mon_of_feb(name)
            else:
                self._add_holiday_feb_5(name)

        if year >= 1917:
            # Benito Juárez's birthday.
            name = tr("Natalicio de Benito Juárez")
            # no 2006 due to celebration of the 200th anniversary
            # of Benito Juárez in 2006
            if year >= 2007:
                self._add_holiday_3rd_mon_of_mar(name)
            else:
                self._add_holiday_mar_21(name)

        if year >= 1923:
            # Labor Day.
            self._add_labor_day(tr("Día del Trabajo"))

        # Independence Day.
        self._add_holiday_sep_16(tr("Día de la Independencia"))

        if year >= 1917:
            # Revolution Day.
            name = tr("Día de la Revolución")
            if year >= 2006:
                self._add_holiday_3rd_mon_of_nov(name)
            else:
                self._add_holiday_nov_20(name)

        if year >= 1970 and (year - 1970) % 6 == 0:
            # Change of Federal Government.
            self._add_holiday_dec_1(tr("Transmisión del Poder Ejecutivo Federal"))

        # Christmas Day.
        self._add_christmas_day(tr("Navidad"))


class MX(Mexico):
    pass


class MEX(Mexico):
    pass
