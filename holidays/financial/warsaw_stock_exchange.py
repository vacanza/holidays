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

from holidays.calendars.gregorian import APR, JAN
from holidays.countries.poland import Poland
from holidays.helpers import tr


class WarsawStockExchange(Poland):
    """Warsaw Stock Exchange (GPW) holidays.

    The exchange is closed on Polish public holidays falling on weekdays, and
    also on Good Friday, Christmas Eve and New Year's Eve. Before 2011 New Year's
    Eve was a trading day and some bridge days were closed ad hoc, so the
    calendar starts in 2011.

    References:
        * [2023](https://www.gpw.pl/pub/GPW/uchwaly/2022/509_2022.pdf)
        * [2024](https://www.gpw.pl/pub/GPW/uchwaly/2023/571_2023_DNI_BEZ_SESJI_2024_UCHW.pdf)
        * [2025](https://www.gpw.pl/pub/GPW/uchwaly/2024/701_2024.pdf)
        * [2026](https://www.gpw.pl/pub/GPW/uchwaly/2025/753_2025.pdf)
        * [2027](https://www.gpw.pl/pub/GPW/uchwaly/2025/754_2025.pdf)
        * [1991-2011](https://www.gpw.pl/pub/files/PDF/rocznik2012/363-369_GPW102_Rocznik2012_Kalendarium_GPW_1991-2011.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XWAR"
    parent_entity = Poland
    supported_languages = ("en_US", "pl")  # type: ignore[assignment]
    start_year = 2011

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, static_holidays_classes=(WarsawStockExchangeStaticHolidays,), **kwargs
        )

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        # Good Friday.
        self._add_good_friday(tr("Wielki Piątek"))

        if self._year <= 2024:
            # Christmas Eve.
            self._add_christmas_eve(tr("Wigilia Bożego Narodzenia"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Sylwester"))


class XWAR(WarsawStockExchange):
    pass


class GPW(WarsawStockExchange):
    pass


class WarsawStockExchangeStaticHolidays:
    """Warsaw Stock Exchange special holidays."""

    # Non-trading day.
    name = tr("Dzień bez sesji")

    special_public_holidays = {
        # The day after the UTP trading system went live.
        2013: (APR, 16, name),
        # MiFID II coming into force.
        2018: (JAN, 2, name),
    }
