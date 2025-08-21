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

from gettext import gettext as tr

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


class NationalStockExchangeOfIndia(ObservedHolidayBase):
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

    market = "XNSE"
    default_language = "en_IN"
    supported_languages = ("en_IN", "en_US", "hi")
    observed_label = "%s (observed)"
    start_year = 1994  # NSE launched in 1994

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # No fixed annual closures that apply every year on the same date.

        # Year-specific holidays and variations
        self._populate_year_specific_holidays()

    def _populate_year_specific_holidays(self):
        """Add year-specific holidays and variations."""

        year_map = {
            2023: [
                (tr("Republic Day"), JAN, 26),
                (tr("Holi"), MAR, 8),
                (tr("Ram Navami"), MAR, 30),
                (tr("Mahavir Jayanti"), APR, 4),
                (tr("Good Friday"), APR, 7),
                (tr("Dr. Baba Saheb Ambedkar Jayanti"), APR, 14),
                (tr("Maharashtra Day"), MAY, 1),
                (tr("Bakri Id"), JUN, 29),
                (tr("Muharram"), JUL, 29),
                (tr("Independence Day"), AUG, 15),
                (tr("Ganesh Chaturthi"), SEP, 19),
                (tr("Mahatma Gandhi Jayanti"), OCT, 2),
                (tr("Dussehra"), OCT, 24),
                (tr("Diwali-Balipratipada"), NOV, 14),
                (tr("Gurunanak Jayanti"), NOV, 27),
                (tr("Christmas Day"), DEC, 25),
            ],
            2024: [
                (tr("Republic Day"), JAN, 26),
                (tr("Mahashivratri"), MAR, 8),
                (tr("Holi"), MAR, 25),
                (tr("Good Friday"), MAR, 29),
                (tr("Id-Ul-Fitr (Ramadan Eid)"), APR, 11),
                (tr("Shri Ram Navmi"), APR, 17),
                (tr("Maharashtra Day"), MAY, 1),
                (tr("Bakri Id"), JUN, 17),
                (tr("Independence Day"), AUG, 15),
                (tr("Mahatma Gandhi Jayanti"), OCT, 2),
                (tr("Dussehra"), OCT, 12),
                (tr("Diwali Laxmi Pujan"), NOV, 1),  # muhurat trading was conducted
                (tr("Gurunanak Jayanti"), NOV, 15),
                (tr("Christmas Day"), DEC, 25),
            ],
            2025: [
                (tr("Mahashivratri"), FEB, 26),
                (tr("Holi"), MAR, 14),
                (tr("Id-Ul-Fitr (Ramadan Eid)"), MAR, 31),
                (tr("Shri Mahavir Jayanti"), APR, 10),
                (tr("Dr. Baba Saheb Ambedkar Jayanti"), APR, 14),
                (tr("Good Friday"), APR, 18),
                (tr("Maharashtra Day"), MAY, 1),
                (tr("Independence Day"), AUG, 15),
                (tr("Ganesh Chaturthi"), AUG, 27),
                (tr("Mahatma Gandhi Jayanti/Dussehra"), OCT, 2),
                (tr("Diwali Laxmi Pujan"), OCT, 21),  # muhurat trading was conducted
                (tr("Diwali-Balipratipada"), OCT, 22),
                (tr("Prakash Gurpurb Sri Guru Nanak Dev"), NOV, 5),
                (tr("Christmas Day"), DEC, 25),
            ],
        }

        if self._year in year_map:
            for name, month, day in year_map[self._year]:
                self._add_holiday(name, month, day)


class NSE(NationalStockExchangeOfIndia):
    """Alias of NationalStockExchangeOfIndia"""

    pass


class XNSE(NationalStockExchangeOfIndia):
    """Alias of NationalStockExchangeOfIndia"""

    pass
