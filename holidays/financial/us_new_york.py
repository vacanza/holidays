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


class USNewYork(SIFMAHolidays):
    """US New York (USNY) financial market holidays.

    The USNY calendar represents general "New York business days" used in financial contracts
    (ISDA derivatives, OTC instruments). While it follows SIFMA (Securities Industry and
    Financial Markets Association) recommendations for most holidays, it differs from both
    USGS (US Government Securities) and NYSE calendars.

    Key differences:
        - vs USGS: USNY does NOT observe Good Friday (USGS does)
        - vs NYSE: USNY DOES observe Columbus Day and Veterans Day (NYSE does not in modern times)
        - vs NYSE: USNY does NOT include special one-off closures (NYSE does)

    This calendar includes both full market closures (PUBLIC holidays) and early closes at
    2:00 PM Eastern Time (HALF_DAY holidays) as recommended by SIFMA, with the exceptions
    noted above.

    The USNY identifier is used for compatibility with systems that reference New York
    market holidays specifically, such as OpenGamma Strata and other financial libraries.

    References:
        * <https://www.sifma.org/resources/general/holiday-schedule/>
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/holiday-schedule/>
        * <https://strata.opengamma.io/apidocs/com/opengamma/strata/basics/date/HolidayCalendarIds.html>
        * <https://github.com/OpenGamma/Strata/blob/main/modules/basics/src/main/java/com/opengamma/strata/basics/date/GlobalHolidayCalendars.java>

    Historical references:
        * <https://web.archive.org/web/20250210040000/https://www.sifma.org/resources/general/us-holiday-archive/>
    """

    market = "USNY"

    def _populate_public_holidays(self):
        # Call parent to get all SIFMA holidays
        super()._populate_public_holidays()

        # Remove Good Friday from USNY calendar.
        # USNY includes Columbus Day and Veterans Day (unlike NYSE which doesn't observe these
        # in modern times), but does NOT include Good Friday (unlike both NYSE and USGS which do).
        # This follows the OpenGamma Strata implementation for general New York business days.
        self._remove_holiday_by_name("Good Friday")

    def _remove_holiday_by_name(self, name):
        """Remove all holidays with the given name."""
        dates_to_remove = [dt for dt, holiday_name in self.items() if holiday_name == name]
        for dt in dates_to_remove:
            self.pop(dt)


class USNY(USNewYork):
    pass


class USNewYorkFinancial(USNewYork):
    pass
