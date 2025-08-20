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

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.observed_holiday_base import ObservedHolidayBase


class IndiaNationalStockExchange(ObservedHolidayBase):
    """National Stock Exchange of India (NSE) holidays.

    References:
        * <https://www.nseindia.com/trade/holiday-calendar>
        * <https://archives.nseindia.com/content/circulars/CMTR54757.pdf> (2023)

    Historical data:
        * <https://nsearchives.nseindia.com/content/circulars/CMTR50560.pdf> (2022)
        * <https://nsearchives.nseindia.com/content/circulars/CMTR54757.pdf> (2023)
        * <https://nsearchives.nseindia.com/content/circulars/CMTR59722.pdf> (2024)
        * <https://nsearchives.nseindia.com/content/circulars/CMTR65587.pdf> (2025)
    """

    market = "XNSE"  # stodo
    default_language = "en_IN"
    supported_languages = ("en_IN", "en_US", "hi")
    observed_label = "%s (observed)"
    start_year = 1994  # NSE was established in 1994

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # static holidays - didnt find any.

        # Year-specific holidays and variations
        self._populate_year_specific_holidays()

    def _populate_year_specific_holidays(self):
        """Add year-specific holidays and variations."""

        if self._year == 2023:
            # https://archives.nseindia.com/content/circulars/CMTR54757.pdf
            self._add_holiday("Republic Day", JAN, 26)
            self._add_holiday("Holi", MAR, 8)
            self._add_holiday("Ram Navami", MAR, 30)
            self._add_holiday("Mahavir Jayanti", APR, 4)
            self._add_holiday("Good Friday", APR, 7)
            self._add_holiday("Dr. Baba Saheb Ambedkar Jayanti", APR, 14)
            self._add_holiday("Maharashtra Day", MAY, 1)
            self._add_holiday("Bakri Id", JUN, 29)
            self._add_holiday("Muharram", JUL, 29)
            self._add_holiday("Independence Day", AUG, 15)
            self._add_holiday("Ganesh Chaturthi", SEP, 19)
            self._add_holiday("Mahatma Gandhi Jayanti", OCT, 2)
            self._add_holiday("Dussehra", OCT, 24)
            self._add_holiday("Diwali-Balipratipada", NOV, 13)
            self._add_holiday("Gurunanak Jayanti", NOV, 27)
            self._add_holiday("Christmas", DEC, 25)

        elif self._year == 2024:
            # https://nsearchives.nseindia.com/content/circulars/CMTR59722.pdf
            self._add_holiday("Republic Day", JAN, 26)
            self._add_holiday("Mahashivratri", MAR, 8)
            self._add_holiday("Holi", MAR, 25)
            self._add_holiday("Good Friday", MAR, 29)
            self._add_holiday("Id-Ul-Fitr (Ramadan Eid)", APR, 11)
            self._add_holiday("Shri Ram Navmi", APR, 17)
            self._add_holiday("Maharashtra Day", MAY, 1)
            self._add_holiday("Bakri Id", JUN, 17)
            self._add_holiday("Independence Day", AUG, 15)
            self._add_holiday("Mahatma Gandhi Jayanti", OCT, 2)
            self._add_holiday("Dussehra", OCT, 12)
            self._add_holiday("Diwali-Balipratipada", NOV, 1)  # muhurat trading was conducted
            self._add_holiday("Gurunanak Jayanti", NOV, 15)
            self._add_holiday("Christmas", DEC, 25)

        elif self._year == 2025:
            # https://nsearchives.nseindia.com/content/circulars/CMTR65587.pdf
            self._add_holiday("Mahashivratri", FEB, 26)
            self._add_holiday("Holi", MAR, 14)
            self._add_holiday("Id-Ul-Fitr (Ramadan Eid)", MAR, 31)
            self._add_holiday("Shri Mahavir Jayanti", APR, 10)
            self._add_holiday("Dr. Baba Saheb Ambedkar Jayanti", APR, 14)
            self._add_holiday("Good Friday", APR, 18)
            self._add_holiday("Maharashtra Day", MAY, 1)
            self._add_holiday("Independence Day", AUG, 15)
            self._add_holiday("Ganesh Chaturthi", AUG, 27)
            self._add_holiday("Mahatma Gandhi Jayanti/Dussehra", OCT, 2)
            self._add_holiday("Diwali Laxmi Pujan", OCT, 21)  # muhurat trading was conducted
            self._add_holiday("Diwali Balipratipada", OCT, 22)
            self._add_holiday("Prakash Gurpurb Sri Guru Nanak Dev", NOV, 5)
            self._add_holiday("Christmas Day", DEC, 25)


class NSE(IndiaNationalStockExchange):
    """Alias of IndiaNationalStockExchange"""

    pass


class XNSE(IndiaNationalStockExchange):
    """Alias of IndiaNationalStockExchange"""

    pass
