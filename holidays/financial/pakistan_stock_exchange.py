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

    PSX follows the Pakistan public holiday calendar and is also closed on Jumu'atul-Wida,
    the last Friday of Ramadan, which isn't a federal public holiday.

    References:
        * [PSX/N-351 Holiday Calendar 2016](https://dps.psx.com.pk/download/attachment/75591-1.pdf)
        * [PSX/N-458 Holiday Calendar 2018](https://dps.psx.com.pk/download/attachment/108910-1.pdf)
        * [PSX/N-88 Holiday Calendar 2019](https://dps.psx.com.pk/download/attachment/125038-1.pdf)
        * [PSX/N-1596 Holiday Calendar 2020](https://dps.psx.com.pk/download/attachment/140396-1.pdf)
        * [PSX/N-1381 Holiday Calendar 2021](https://dps.psx.com.pk/download/attachment/158530-1.pdf)
        * [PSX/N-59 Holiday Calendar 2022](https://dps.psx.com.pk/download/attachment/180241-1.pdf)
        * [PSX/N-1313 Holiday Calendar 2023](https://dps.psx.com.pk/download/attachment/199827-1.pdf)
        * [PSX/N-1311 Holiday Calendar 2024](https://dps.psx.com.pk/download/attachment/222892-1.pdf)
        * [PSX/N-1268 Holiday Calendar 2025](https://dps.psx.com.pk/download/attachment/244903-1.pdf)
        * [PSX/N-89 Holiday Calendar 2026](https://dps.psx.com.pk/download/attachment/268947-1.pdf)

    Historical data (Jumu'atul-Wida):
        * [2016](https://dps.psx.com.pk/download/attachment/83332-1.pdf)
        * [2017](https://dps.psx.com.pk/download/attachment/100101-1.pdf)
        * [2018](https://dps.psx.com.pk/download/attachment/115114-1.pdf)
        * [2019](https://dps.psx.com.pk/download/attachment/131307-1.pdf)
        * [2020](https://dps.psx.com.pk/download/attachment/148004-1.pdf)
        * [2021](https://dps.psx.com.pk/download/attachment/166699-1.pdf)
        * [2022](https://dps.psx.com.pk/download/attachment/185742-1.pdf)
        * [2023](https://dps.psx.com.pk/download/attachment/205531-1.pdf)
        * [2024](https://dps.psx.com.pk/download/attachment/228365-1.pdf)
        * [2025](https://dps.psx.com.pk/download/attachment/249862-1.pdf)
        * [2026](https://dps.psx.com.pk/download/attachment/272674-1.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XKAR"
    parent_entity = Pakistan
    start_year = 2016

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        # Jumu'atul-Wida.
        self._add_jumuatul_wida(tr("Juma-tul-Wida"))


class XKAR(PakistanStockExchange):
    pass


class PSX(PakistanStockExchange):
    pass
