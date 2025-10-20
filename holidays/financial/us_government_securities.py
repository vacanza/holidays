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

from holidays.financial._sifma import SIFMAHolidays


class USGovernmentSecurities(SIFMAHolidays):
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

    References:
        * <https://www.sifma.org/resources/general/holiday-schedule/>
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/holiday-schedule/>

    Historical references:
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/us-holiday-archive/>
    """

    market = "USGS"


class USGS(USGovernmentSecurities):
    pass


class USBondMarket(USGovernmentSecurities):
    pass
