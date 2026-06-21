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
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_NONE, SUN_TO_NONE


class BolsaMexicanaDeValores(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Bolsa Mexicana de Valores (BMV) holidays.

    References:
        * <https://web.archive.org/web/20260217214228/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos>

    Historical data:
        * [2014](https://web.archive.org/web/20151002034151/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2015](https://web.archive.org/web/20151002034151/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2016](https://web.archive.org/web/20161018231815/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2017](https://web.archive.org/web/20171102043000/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2018](https://web.archive.org/web/20181104081233/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2019](https://web.archive.org/web/20191113083233/http://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2020](https://web.archive.org/web/20201027043731/http://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2021](https://web.archive.org/web/20210105213246/http://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2022](https://web.archive.org/web/20220427200741/http://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2023](https://web.archive.org/web/20231205095710/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2024](https://web.archive.org/web/20241227124527/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2025](https://web.archive.org/web/20251008103743/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
        * [2026](https://web.archive.org/web/20260217214228/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos)
    """

    market = "XMEX"
    default_language = "es"
    supported_languages = ("en_US", "es", "uk")
    start_year = 2014

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_NONE + SUN_TO_NONE)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        # Constitution Day.
        self._add_holiday_1st_mon_of_feb(tr("Día de la Constitución"))

        # Benito Juárez's birthday.
        self._add_holiday_3rd_mon_of_mar(tr("Natalicio de Benito Juárez"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Jueves Santo"))

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Labor Day.
        self._move_holiday(self._add_labor_day(tr("Día del Trabajo")))

        # Independence Day.
        self._move_holiday(self._add_holiday_sep_16(tr("Día de la Independencia")))

        if (self._year - 1970) % 6 == 0:
            # Change of Federal Government.
            name = tr("Transmisión del Poder Ejecutivo Federal")
            if self._year >= 2024:
                self._move_holiday(self._add_holiday_oct_1(name))
            else:
                self._move_holiday(self._add_holiday_dec_1(name))

        # Day of the Dead.
        self._move_holiday(self._add_holiday_nov_2(tr("Día de Muertos")))

        # Revolution Day.
        self._add_holiday_3rd_mon_of_nov(tr("Día de la Revolución"))

        # Bank Employee Day.
        self._move_holiday(self._add_holiday_dec_12(tr("Día del Empleado Bancario")))

        # Christmas Day.
        self._move_holiday(self._add_christmas_day(tr("Navidad")))


class XMEX(BolsaMexicanaDeValores):
    pass


class BMV(BolsaMexicanaDeValores):
    pass
