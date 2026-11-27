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

from holidays.calendars.gregorian import JAN
from holidays.countries.czechia import Czechia
from holidays.groups import StaticHolidays
from holidays.helpers import tr


class PragueStockExchange(Czechia, StaticHolidays):
    """Prague Stock Exchange (BCPP) holidays.

    The exchange is closed on Czech public holidays falling on weekdays, and
    also on Good Friday (since 2013) and New Year's Eve.

    References:
        * <https://web.archive.org/web/20261020195539/https://www.pse.cz/en/trading/trading-information/trading-calendar>
        * <https://web.archive.org/web/20260902191623/https://www.pse.cz/informace-o-obchodovani/kalendar-burzovnich-dni>
        * [2004-2006](https://web.archive.org/web/20060108223457/http://www.pse.cz/obchodovani/kalendar.asp#kalendarI2006)
        * [2007-2016](https://web.archive.org/web/20160807222734/http://www.pse.cz/dokument.aspx?k=Kalendar-BD-2016)
        * [2017](https://web.archive.org/web/20170906124536/https://www.pse.cz/en/trading/trading-information/trading-calendar/)
        * [2018-2019](https://web.archive.org/web/20190918224227/https://www.pse.cz/en/trading/trading-information/trading-calendar/)
        * [2020](https://web.archive.org/web/20201101013641/https://www.pse.cz/en/trading/trading-information/trading-calendar)
        * [2021](https://web.archive.org/web/20260420132537/https://www.pse.cz/userfiles/related_documents/en/trading-calendar-PSE2021.pdf)
        * [2022](https://web.archive.org/web/20260420133549/https://www.pse.cz/userfiles/related_documents/en/trading-calendar-PSE2022.pdf)
        * [2023](https://web.archive.org/web/20260420125134/https://www.pse.cz/userfiles/related_documents/en/trading-calendar-PSE-2023.pdf)
        * [2024](https://web.archive.org/web/20260420132724/https://www.pse.cz/userfiles/related_documents/en/trading-calendar-PSE-2024-eng.pdf)
        * [2025](https://web.archive.org/web/20260420132842/https://www.pse.cz/userfiles/related_documents/en/Kalendar-Calendar-PSE-2025.pdf)
        * [2026](https://web.archive.org/web/20260420131953/https://www.pse.cz/userfiles/related_documents/en/Kalendar-obchodnich-dnu-2026-Trading-callendar-2026.pdf)
        * [2027](https://web.archive.org/web/20261123034957/https://www.pse.cz/userfiles/related_documents/en/Kalendar-obchodnich-dnu-2027-Trading-callendar-2027.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XPRA"
    parent_entity = Czechia
    start_year = 2004

    def __init__(self, *args, **kwargs):
        StaticHolidays.__init__(self, PragueStockExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        if 2013 <= self._year <= 2015:
            # Good Friday.
            self._add_good_friday(tr("Velký pátek"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvestr"))


class XPRA(PragueStockExchange):
    pass


class BCPP(PragueStockExchange):
    pass


class PragueStockExchangeStaticHolidays:
    """Prague Stock Exchange (BCPP) special holidays."""

    special_public_holidays = {
        # Non-trading day.
        2004: (JAN, 2, tr("Neburzovní den")),
    }
