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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Eritrea(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Eritrea holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Eritrea>
        * <https://web.archive.org/web/20230313234629/https://explore-eritrea.com/working-hours-and-holidays/>
        * <https://web.archive.org/web/20110903130335/http://www.eritrea.be/old/eritrea-religions.htm>
        * <https://web.archive.org/web/20250807083700/https://www.timeanddate.com/calendar/?year=2025&country=168>
        * <https://www.mintageworld.com/media/detail/11411-fenkil-day-in-eritrea/>
    """

    country = "ER"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # On 28 May 1993, Eritrea was admitted into the United Nations as the 182nd member state.
    start_year = 1994

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=EritreaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("New Year"))

        # Orthodox Christmas.
        self._add_christmas_day(tr("Leddet"))

        # Epiphany.
        self._add_epiphany_day(tr("Timket"))

        # Fenkil Day.
        self._add_holiday_feb_10(tr("Fenkil Day"))

        # Women's Day.
        self._add_womens_day(tr("Women's Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Orthodox Easter.
        self._add_easter_sunday(tr("Tensae"))

        # International Workers' Day.
        self._add_labor_day(tr("International Workers' Day"))

        # Independence Day.
        self._add_holiday_may_24(tr("Independence Day"))

        # Martyrs' Day.
        self._add_holiday_jun_20(tr("Martyrs' Day"))

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("Muharram"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Mawlid an-Nabi"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Eid al-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Eid al-Adha"))

        # Revolution Day.
        self._add_holiday_sep_1(tr("Revolution Day"))

        # Orthodox New Year.
        self._add_holiday_sep_11(tr("Keddus Yohannes"))

        # Finding of the True Cross.
        self._add_holiday_sep_27(tr("Meskel"))


class ER(Eritrea):
    pass


class ERI(Eritrea):
    pass


class EritreaIslamicHolidays(_CustomIslamicHolidays):
    """
    Islamic holidays for Eritrea.

    References:
        * <https://www.hijria.com/en/hijri-gregorian-calendar/eritrea/>
    """

    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (1995, 2025)
    EID_AL_ADHA_DATES = {
        1995: (MAY, 9),
        1996: (APR, 27),
        1997: (APR, 17),
        1998: (APR, 7),
        1999: (MAR, 27),
        2000: (MAR, 16),
        2001: (MAR, 5),
        2002: (FEB, 22),
        2003: (FEB, 11),
        2004: (FEB, 1),
        2005: (JAN, 21),
        2006: (DEC, 31),
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 27),
        2010: (NOV, 16),
        2011: (NOV, 6),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 23),
        2016: (SEP, 11),
        2017: (SEP, 1),
        2018: (AUG, 21),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 6),
    }
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (1995, 2025)
    EID_AL_FITR_DATES = {
        1995: (MAR, 2),
        1996: (FEB, 19),
        1997: (FEB, 8),
        1998: (JAN, 29),
        1999: (JAN, 18),
        2000: (DEC, 27),
        2001: (DEC, 16),
        2002: (DEC, 5),
        2003: (NOV, 25),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 23),
        2007: (OCT, 13),
        2008: (OCT, 1),
        2009: (SEP, 20),
        2010: (SEP, 10),
        2011: (AUG, 30),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2017: (JUN, 25),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 30),
    }
    MAWLID_DATES_CONFIRMED_YEARS = (1994, 2025)
    MAWLID_DATES = {
        1994: (AUG, 19),
        1995: (AUG, 8),
        1996: (JUL, 27),
        1997: (JUL, 16),
        1998: (JUL, 6),
        1999: (JUN, 26),
        2000: (JUN, 14),
        2001: (JUN, 4),
        2002: (MAY, 24),
        2003: (MAY, 13),
        2004: (MAY, 1),
        2005: (APR, 21),
        2006: (APR, 10),
        2007: (MAR, 31),
        2008: (MAR, 20),
        2009: (MAR, 9),
        2010: (FEB, 26),
        2011: (FEB, 15),
        2012: (FEB, 4),
        2013: (JAN, 24),
        2014: (JAN, 13),
        2015: (DEC, 23),
        2016: (DEC, 11),
        2017: (NOV, 30),
        2018: (NOV, 20),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 15),
        2025: (SEP, 4),
    }
