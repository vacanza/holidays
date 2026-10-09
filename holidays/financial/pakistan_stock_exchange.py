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

from holidays.countries.pakistan import Pakistan
from holidays.helpers import tr


class PakistanStockExchange(Pakistan):
    """Pakistan Stock Exchange (PSX) holidays.

    PSX follows the Pakistan public holiday calendar and is also closed on Juma-tul-Wida,
    the last Friday of Ramadan, which isn't a federal public holiday.

    References:
        * [Calendar Holidays](https://web.archive.org/web/20261009171342/https://www.psx.com.pk/psx/exchange/general/calendar-holidays)
        * [PSX/N-59 Holiday Calendar 2022](https://dps.psx.com.pk/download/attachment/180241-1.pdf)
        * [PSX/N-89 Holiday Calendar 2026](https://dps.psx.com.pk/download/attachment/268947-1.pdf)

    Historical data (Juma-tul-Wida):
        * [2020](https://web.archive.org/web/20261009171650/https://profit.pakistantoday.com.pk/2020/05/22/psx-to-remain-closed-from-friday-to-wednesday)
        * [2021](https://web.archive.org/web/20261009171807/https://pkrevenue.com/holiday-notice/)
        * [2023](https://web.archive.org/web/20261009172257/https://www.thenews.com.pk/latest/1059325-psx-to-remain-closed-on-juma-tul-wida)
        * [2024](https://web.archive.org/web/20261009171937/https://mettisglobal.news/psx-to-remain-close-on-april-5-on-account-of-juma-tul-wida/)
        * [2025](https://web.archive.org/web/20261009172003/https://profit.pakistantoday.com.pk/2025/03/20/psx-announces-eid-ul-fitr-holiday-schedule)
    """

    country = None  # type: ignore[assignment]
    market = "XKAR"
    parent_entity = Pakistan
    start_year = 2020

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        # Jumu'atul-Wida.
        self._add_jumuatul_wida(tr("Juma-tul-Wida"))


class XKAR(PakistanStockExchange):
    pass


class PSX(PakistanStockExchange):
    pass
