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


from holidays.countries.czechia import Czechia
from holidays.helpers import tr


class PragueStockExchange(Czechia):
    """Prague Stock Exchange (BCPP) holidays.

    The exchange is closed on Czech public holidays falling on weekdays, and
    also on New Year's Eve. Official PSE trading calendars are available starting
    from 2017; earlier years are excluded due to lack of verifiable official
    exchange calendar records.

    References:
        * <https://www.pse.cz/en/trading/trading-information/trading-calendar>
        * <https://www.pse.cz/informace-o-obchodovani/kalendar-burzovnich-dni>
        * [2017](https://web.archive.org/web/20170906124536/https://www.pse.cz/en/trading/trading-information/trading-calendar/)
        * [2018-2019](https://web.archive.org/web/20190918224227/https://www.pse.cz/en/trading/trading-information/trading-calendar/)
        * [2020](https://web.archive.org/web/20201101013641/https://www.pse.cz/en/trading/trading-information/trading-calendar)
        * [2021](https://www.pse.cz/userfiles/related_documents/en/trading-calendar-PSE2021.pdf)
        * [2022](https://www.pse.cz/userfiles/related_documents/en/trading-calendar-PSE2022.pdf)
        * [2023](https://www.pse.cz/userfiles/related_documents/en/trading-calendar-PSE-2023.pdf)
        * [2024](https://www.pse.cz/userfiles/related_documents/en/trading-calendar-PSE-2024-eng.pdf)
        * [2025](https://www.pse.cz/userfiles/related_documents/en/Kalendar-Calendar-PSE-2025.pdf)
        * [2026](https://www.pse.cz/userfiles/related_documents/en/Kalendar-obchodnich-dnu-2026-Trading-callendar-2026.pdf)
        * [2027](https://www.pse.cz/userfiles/related_documents/en/Kalendar-obchodnich-dnu-2027-Trading-callendar-2027.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XPRA"
    parent_entity = Czechia
    # Earliest year with an accessible official PSE trading calendar record.
    start_year = 2017

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvestr"))


class XPRA(PragueStockExchange):
    pass


class BCPP(PragueStockExchange):
    pass
