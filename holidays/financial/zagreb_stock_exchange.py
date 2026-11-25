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

from holidays.calendars.gregorian import APR, DEC
from holidays.countries.croatia import Croatia
from holidays.groups import StaticHolidays
from holidays.helpers import tr


class ZagrebStockExchange(Croatia, StaticHolidays):
    """Zagreb Stock Exchange (ZSE) holidays.

    The exchange is closed on Croatian public holidays falling on weekdays, and
    also on Good Friday, Christmas Eve, and New Year's Eve. Before 2015, Good
    Friday and New Year's Eve were shortened trading sessions rather than full
    non-trading days, so the calendar starts in 2015.

    References:
        * [2015](https://web.archive.org/web/20141207040742/http://zse.hr/default.aspx?id=32821)
        * [2016](https://web.archive.org/web/20160205062546/http://zse.hr:80/default.aspx?id=32821)
        * [2017](https://web.archive.org/web/20170722105658/http://zse.hr/default.aspx?id=32821)
        * [2018](https://web.archive.org/web/20181216085617/http://zse.hr:80/default.aspx?id=32821)
        * [2019](https://web.archive.org/web/20191210043919/https://www.zse.hr/default.aspx?id=32821)
        * [2020-2021](https://web.archive.org/web/20201106221235/https://zse.hr/en/non-trading-days/110)
        * [2022](https://web.archive.org/web/20221209194143/https://zse.hr/hr/neradni-dani/110)
        * [2023](https://web.archive.org/web/20230326125439/https://zse.hr/en/non-trading-days/110)
        * [2024](https://web.archive.org/web/20240415000000/https://zse.hr/hr/neradni-dani/110)
        * [2025-2026](https://web.archive.org/web/20250907023700/https://zse.hr/en/non-trading-days/110)
        * [2026-2027](https://web.archive.org/web/20261010121354/https://zse.hr/en/non-trading-days/110)
    """

    country = None  # type: ignore[assignment]
    market = "XZAG"
    parent_entity = Croatia
    start_year = 2015

    def __init__(self, *args, **kwargs):
        StaticHolidays.__init__(self, ZagrebStockExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        # Good Friday.
        self._add_good_friday(tr("Veliki petak"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Badnjak"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Stara godina"))


class XZAG(ZagrebStockExchange):
    pass


class ZSE(ZagrebStockExchange):
    pass


class ZagrebStockExchangeStaticHolidays:
    """Zagreb Stock Exchange (ZSE) special holidays.

    References:
        * [2022 Euro Adoption](https://web.archive.org/web/20221209194143/https://zse.hr/hr/neradni-dani/110)
        * [2024 Parliamentary Election Day](https://web.archive.org/web/20240415000000/https://zse.hr/hr/neradni-dani/110)
    """

    # Euro adoption.
    euro_adoption = tr("Uvođenje eura")

    special_public_holidays = {
        2022: (
            (DEC, 29, euro_adoption),
            (DEC, 30, euro_adoption),
        ),
        # Parliamentary Election Day.
        2024: (APR, 17, tr("Dan izbora zastupnika u Hrvatski sabor")),
    }
