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

from holidays.financial.us_new_york import USNewYork


class USGovernmentSecurities(USNewYork):
    """US Government Securities (USGS) bond market holidays.

    The US Government Securities market follows SIFMA (Securities Industry and Financial Markets
    Association) recommendations for full and early market closures. These recommendations apply
    to the trading of U.S. dollar-denominated government securities, mortgage- and asset-backed
    securities, over-the-counter investment-grade and high-yield corporate bonds, municipal bonds,
    and secondary money market trading.

    This calendar includes both full market closures (PUBLIC holidays) and early closes at
    2:00 PM Eastern Time (HALF_DAY holidays) as recommended by SIFMA.

    The USGS calendar is referenced by the 2006 ISDA definitions 1.11 and is used for
    instruments such as SOFR (Secured Overnight Financing Rate) fixings.

    Key difference from USNY:
        - USGS observes Good Friday as a full closure (USNY does not)

    References:
        * <https://www.sifma.org/resources/general/holiday-schedule/>
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/holiday-schedule/>
        * [2015-2024](https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/us-holiday-archive/)
        * [1996-2017](https://web.archive.org/web/20221206175502/https://www.sifma.org/wp-content/uploads/2017/06/misc-us-historical-holiday-market-recommendations-sifma.pdf)
    """

    market = "USGS"

    def _populate_public_holidays(self):
        # Get all USNY holidays first
        super()._populate_public_holidays()

        # Note: Some SIFMA markets may treat this as an early close instead of full closure.

        # Good Friday.
        self._add_good_friday("Good Friday")

    def _populate_half_day_holidays(self):
        # Get all USNY early closes first
        super()._populate_half_day_holidays()

        # Add Good Friday early close.
        # Day before Good Friday (Maundy Thursday).
        begin_time_label = "Markets close at 2:00 PM ET (%s)"
        self._add_holy_thursday(begin_time_label % "Good Friday")


class USGS(USGovernmentSecurities):
    pass


class USBondMarket(USGovernmentSecurities):
    pass
