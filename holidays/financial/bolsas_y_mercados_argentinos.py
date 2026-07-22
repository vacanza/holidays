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

from holidays.calendars.gregorian import JAN, MAR, JUN, JUL, SEP, NOV, DEC
from holidays.constants import HALF_DAY, PUBLIC, RESTRICTED_SETTLEMENT
from holidays.countries.argentina import Argentina
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    TUE_WED_TO_PREV_MON,
    THU_FRI_TO_NEXT_MON,
)


class BolsasYMercadosArgentinos(Argentina):
    """Bolsas y Mercados Argentinos (BYMA) holidays.

    BYMA follows the Argentine national public holiday calendar (including the
    statutory observance shifts), with three market-specific differences: it keeps
    trading on the tourism "bridge" holidays (feriados con fines turísticos), it is
    closed on Bankers' Day, and it adds a year-end market close on December 31st.

    References:
        * [BYMA trading calendar](https://web.archive.org/web/20260309064908/https://www.byma.com.ar/mercado/calendario-bursatil)
    """

    country = None  # type: ignore[assignment]
    market = "XBUE"
    parent_entity = Argentina
    default_language = "es"
    supported_languages = ("en_US", "es")  # type: ignore[assignment]
    supported_categories = (PUBLIC, RESTRICTED_SETTLEMENT, HALF_DAY)  # type: ignore[assignment]
    subdivisions = ()  # type: ignore[assignment]
    subdivisions_aliases: dict[str, str] = {}
    start_year = 2026

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        # `islamic_show_estimated` is accepted for parity with the Argentina base;
        # BYMA observes no Islamic holidays, so it has no effect here.
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, BolsasYMercadosArgentinosStaticHolidays)
        kwargs.setdefault("observed_rule", TUE_WED_TO_PREV_MON + THU_FRI_TO_NEXT_MON)
        kwargs.setdefault("observed_since", 1988)
        ObservedHolidayBase.__init__(self, *args, **kwargs)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        self._populate_bank_holidays()

        # Year-end market holiday.
        self._add_holiday_dec_31(tr("Feriado bursátil de fin de año"))

    def _populate_half_day_holidays(self):
        # %s (markets close at 3:00pm).
        early_close_label = tr("%s (el mercado cierra a las 15:00)")

        # Christmas Eve.
        self._add_christmas_eve(self._format_holiday_name(early_close_label, tr("Nochebuena")))


class XBUE(BolsasYMercadosArgentinos):
    pass


class BYMA(BolsasYMercadosArgentinos):
    pass


class BolsasYMercadosArgentinosStaticHolidays:
    """Bolsas y Mercados Argentinos (BYMA) special holidays.

    BYMA settlement-restricted trading days.

    On these days the market trades a full session but one settlement type is
    unavailable. The "no cable" days track U.S. Federal Reserve holidays; the
    "no local" days follow BYMA's annual calendar (bridge holidays and Christmas
    Eve). Neither is derivable from a formula, so they are listed per year.
    """

    # No local settlement.
    no_local_settlement = tr("Sin liquidación local")

    # No cable settlement.
    no_cable_settlement = tr("Sin liquidación cable")

    special_restricted_settlement_holidays = {
        2026: (
            (JAN, 19, no_cable_settlement),
            (MAR, 23, no_local_settlement),
            (JUN, 19, no_cable_settlement),
            (JUL, 10, no_local_settlement),
            (SEP, 7, no_cable_settlement),
            (NOV, 11, no_cable_settlement),
            (NOV, 26, no_cable_settlement),
            (DEC, 7, no_local_settlement),
            (DEC, 24, no_local_settlement),
        ),
    }
