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

from holidays.calendars.gregorian import SEP
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_NONE, SUN_TO_NONE


class BolsaMexicanaDeValores(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """Bolsa Mexicana de Valores (BMV) holidays.

    References:
        * <https://web.archive.org/web/20260217214228/https://www.bmv.com.mx/es/grupo-bmv/calendario-de-dias-festivos>

    Historical data:
        * [2001](https://web.archive.org/web/20010609142152/http://www.bmv.com.mx/bmv/calendario.html)
        * [2002](https://web.archive.org/web/20021210142656/http://bmv.com.mx/BMV/HTML/sec1_diasnolabora.html)
        * [2003](https://web.archive.org/web/20031203014342/http://bmv.com.mx/BMV/HTML/sec1_diasnolabora.html)
        * [2004](https://web.archive.org/web/20041208225025/http://bmv.com.mx/BMV/HTML/sec1_diasnolabora.html)
        * [2005](https://web.archive.org/web/20051210114324/http://bmv.com.mx/BMV/HTML/sec1_diasnolabora.html)
        * [2006](https://web.archive.org/web/20060219160628/http://bmv.com.mx/BMV/HTML/sec1_diasnolabora.html)
        * [2007](https://web.archive.org/web/20071111015732/http://bmv.com.mx/wb3/wb/BMV/BMV_calendario_de_dias_festivos)
        * [2008](https://web.archive.org/web/20081206060322/http://bmv.com.mx/wb3/wb/BMV/BMV_calendario_de_dias_festivos)
        * [2009](https://web.archive.org/web/20091001053822/http://bmv.com.mx/wb3/wb/BMV/BMV_calendario_de_dias_festivos)
        * [2010](https://web.archive.org/web/20101018003727/http://bmv.com.mx/wb3/wb/BMV/BMV_calendario_de_dias_festivos)
        * [2011](https://web.archive.org/web/20111030174959/http://bmv.com.mx/wb3/wb/BMV/BMV_calendario_de_dias_festivos)
        * [2012](https://web.archive.org/web/20121124175114/http://bmv.com.mx/wb3/wb/BMV/BMV_calendario_de_dias_festivos)
        * [2013](https://web.archive.org/web/20131125224718/http://bmv.com.mx/wb3/wb/BMV/BMV_calendario_de_dias_festivos)
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
    start_year = 2001

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, BolsaMexicanaDeValoresStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_TO_NONE + SUN_TO_NONE)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        # Constitution Day.
        name = tr("Día de la Constitución")
        if self._year >= 2006:
            self._add_holiday_1st_mon_of_feb(name)
        else:
            self._move_holiday(self._add_holiday_feb_5(name))

        # Benito Juárez's birthday.
        name = tr("Natalicio de Benito Juárez")
        # no 2006 due to celebration of the 200th anniversary
        # of Benito Juárez in 2006
        if self._year >= 2007:
            self._add_holiday_3rd_mon_of_mar(name)
        else:
            self._move_holiday(self._add_holiday_mar_21(name))

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
        name = tr("Día de la Revolución")
        if self._year >= 2006:
            self._add_holiday_3rd_mon_of_nov(name)
        else:
            self._move_holiday(self._add_holiday_nov_20(name))

        # Bank Employee Day.
        self._move_holiday(self._add_holiday_dec_12(tr("Día del Empleado Bancario")))

        # Christmas Day.
        self._move_holiday(self._add_christmas_day(tr("Navidad")))


class XMEX(BolsaMexicanaDeValores):
    pass


class BMV(BolsaMexicanaDeValores):
    pass


class BolsaMexicanaDeValoresStaticHolidays:
    """Bolsa Mexicana de Valores (BMV) special holidays.

    References:
        * [Bicentennial of Mexican Independence](https://web.archive.org/web/20260622174254/https://www.eleconomista.com.mx/mercados/BMV-cerrara-16-y-17-de-septiembre-20100913-0030.html)
    """

    special_public_holidays = {
        # Bicentennial of Mexican Independence (Bridge day).
        2010: (SEP, 17, tr("Bicentenario de la Independencia de México (Día Puente)")),
    }
