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

from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_NONE,
    SUN_TO_NONE,
)


class BolsasYMercadosEspanoles(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Bolsas y Mercados Españoles (BME) holidays.

    References:
        [2012](https://web.archive.org/web/20121114140924/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2013](https://web.archive.org/web/20131220023431/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2014](https://web.archive.org/web/20141224194955/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2015](https://web.archive.org/web/20150320055500/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2016](https://web.archive.org/web/20160422163937/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2017](https://web.archive.org/web/20170508172001/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2018](https://web.archive.org/web/20180731072453/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2019](https://web.archive.org/web/20190825063749/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2020](https://web.archive.org/web/20200929043214/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2021](https://web.archive.org/web/20211006222059/http://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2022](https://web.archive.org/web/20220519151137/https://www.bolsamadrid.es/ing/aspx/Inversores/Agenda/Calendario.aspx)
        [2023](https://web.archive.org/web/20230401165323/https://www.bolsasymercados.es/bme-exchange/es/Negociar/Calendario-Mercado)
        [2024](https://web.archive.org/web/20240530063923/https://www.bolsasymercados.es/bme-exchange/es/Negociar/Calendario-Mercado)
        [2025](https://web.archive.org/web/20250804221451/https://www.bolsasymercados.es/bme-exchange/es/Negociar/Calendario-Mercado)
        [2026](https://web.archive.org/web/20260217165615/https://www.bolsasymercados.es/bme-exchange/es/Negociar/Calendario-Mercado)
    """

    market = "XMAD"
    default_language = "es"
    supported_languages = ("en_US", "es")
    start_year = 2000
    supported_categories = (HALF_DAY, PUBLIC)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_NONE + SUN_TO_NONE)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._move_holiday(self._add_new_years_day(tr("Año Nuevo")))

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Easter Monday.
        self._add_easter_monday(tr("Lunes de Pascua"))

        # Labor Day.
        self._move_holiday(self._add_labor_day(tr("Día del Trabajo")))

        # Christmas Day.
        self._move_holiday(self._add_christmas_day(tr("Navidad")))

        # Boxing Day & Saint Stephen's Day.
        self._move_holiday(self._add_christmas_day_two(tr("Boxing Day & San Esteban")))

    def _populate_half_day_holidays(self):
        # %s (markets close at 14:00 CET).
        pause_label = tr("%s (los mercados cierran a las 14:00 CET)")

        self._move_holiday(
            # Christmas Eve.
            self._add_christmas_eve(self._format_holiday_name(pause_label, tr("Nochebuena")))
        )

        self._move_holiday(
            # New Year's Eve.
            self._add_new_years_eve(self._format_holiday_name(pause_label, tr("Nochevieja")))
        )


class XMAD(BolsasYMercadosEspanoles):
    pass


class BME(BolsasYMercadosEspanoles):
    pass
