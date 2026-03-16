#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Peru(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Peru
    """

    country = "PE"
    default_language = "es"
    # Supported languages
    supported_languages = ("en_US", "es")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_new_years_day(tr("Año Nuevo"))

        # Maundy Thursday
        self._add_holy_thursday(tr("Jueves Santo"))

        # Good Friday
        self._add_good_friday(tr("Viernes Santo"))

        # Labor Day
        self._add_labor_day(tr("Día del Trabajador"))

        # Battle of Arica and Flag Day
        self._add_holiday_jun_7(tr("Día de la Batalla de Arica y Día de la Bandera"))

        # Saint Peter and Saint Paul
        self._add_saints_peter_and_paul_day(tr("Día de San Pedro y San Pablo"))

        # Peruvian Air Force Day
        self._add_holiday_jul_23(tr("Día de la Fuerza Aérea del Perú"))

        # Independence Day
        self._add_holiday_jul_28(tr("Día de la Independencia"))

        # Independence Day Holiday
        self._add_holiday_jul_29(tr("Fiestas Patrias"))

        # Battle of Junín
        self._add_holiday_aug_6(tr("Batalla de Junín"))

        # Santa Rosa de Lima
        self._add_holiday_aug_30(tr("Santa Rosa de Lima"))

        # Battle of Angamos
        self._add_holiday_oct_8(tr("Combate de Angamos"))

        # All Saints' Day
        self._add_all_saints_day(tr("Día de Todos los Santos"))

        # Immaculate Conception
        self._add_immaculate_conception_day(tr("Inmaculada Concepción"))

        # Battle of Ayacucho
        self._add_holiday_dec_9(tr("Batalla de Ayacucho"))

        # Christmas Day
        self._add_christmas_day(tr("Navidad"))


class PE(Peru):
    pass


class PER(Peru):
    pass
