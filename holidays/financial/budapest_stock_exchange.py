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

from holidays.countries.hungary import Hungary
from holidays.helpers import tr


class BudapestStockExchange(Hungary):
    """Budapest Stock Exchange (BÉT / BSE) holidays.

    The exchange is closed on Hungarian public holidays and government-decreed
    bridged rest days falling on weekdays, as well as on Good Friday (since 2012),
    Christmas Eve, and New Year's Eve. Hungarian Saturday make-up workdays are also
    non-trading days on the exchange.

    References:
        * [CEO Resolution 514/2011 (2012 Trading Holidays)](https://web.archive.org/web/20261126141320/https://www.bse.hu/newkibdata/108984735/Kersz_nnapok_2012_ENG.pdf)
        * [CEO Resolution 362/2012 (2013 Trading Holidays)](https://web.archive.org/web/20261126141321/https://www.bse.hu/newkibdata/112185122/Kersz_nnapok_2013_ENG.pdf)
        * [CEO Resolution 485/2013 (2014 Trading Holidays)](https://web.archive.org/web/20261126141322/https://www.bse.hu/newkibdata/115651478/Kersz_nnapok_2014_ENG.pdf)
        * [CEO Resolution 542/2014 (2015 Trading Holidays)](https://web.archive.org/web/20261126141505/https://www.bse.hu/newkibdata/118128738/Kersz_nnapok_2015_ENG.pdf)
        * [CEO Resolution 474/2015 (2016 Trading Holidays)](https://web.archive.org/web/20261126141507/https://www.bse.hu/newkibdata/120228803/Trading_holidays_2016_ENG.pdf)
        * [Trading Calendar 2021](https://web.archive.org/web/20260609172020/https://www.bse.hu/Products-and-Services/Trading-information/trading-calendar-2021)
        * [CEO Resolution 325/2020 (2021 Trading Holidays)](https://web.archive.org/web/20250807034751/https://www.bse.hu/pfile/file?path=/site/Angol/Documents/Products_And_Services/Trading_holidays_2021.pdf1)
        * [CEO Resolution 311/2024 (2025 Trading Holidays)](https://web.archive.org/web/20261126175036/https://www.bse.hu/pfile/file?path=/site/Angol/Documents/Products_And_Services/trading-information/trading-holidays-2025)
        * [Trading Calendar 2026](https://web.archive.org/web/20261126165104/https://www.bse.hu/pfile/file?path=/site/Angol/Documents/Products_And_Services/trading-information/trading-calendar-2026)
        * [CEO Resolution 380/2025 (2026 Trading Holidays)](https://web.archive.org/web/20261126193538/https://www.bse.hu/pfile/file?path=/site/Angol/Documents/Products_And_Services/trading-information/trading-holidays-2026)
        * [Trading Calendar 2027](https://web.archive.org/web/20261126175042/https://www.bse.hu/pfile/file?path=/site/Angol/Documents/Products_And_Services/trading-information/trading-calendar-2027)
    """

    country = None  # type: ignore[assignment]
    market = "XBUD"
    parent_entity = Hungary
    # First full year after the re-establishment of the Budapest Stock Exchange on June 21, 1990.
    start_year = 1991

    def _add_holiday(self, name, *args):
        if self._is_weekend(*args):
            return None

        return super()._add_holiday(name, *args)

    def _populate_common_holidays(self):
        super()._populate_common_holidays()

        # BSE keeps national Saturday make-up workdays closed.
        self.weekend_workdays.clear()

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        if 2012 <= self._year <= 2016:
            # Good Friday.
            self._add_good_friday(tr("Nagypéntek"))

        if self._year <= 2025:
            # Christmas Eve.
            self._add_christmas_eve(tr("Szenteste"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Szilveszter"))


class XBUD(BudapestStockExchange):
    pass


class BET(BudapestStockExchange):
    pass
