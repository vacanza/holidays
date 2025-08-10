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
    default_language = "en_ER"
    supported_languages = ("en_ER", "en_US")
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

        # Fenkil Day.
        self._add_holiday_feb_10(tr("Fenkil Day"))

        # Women's Day.
        self._add_holiday_mar_8(tr("Women's Day"))

        # Orthodox Christmas.
        self._add_christmas_day(tr("Leddet"))

        # Epiphany.
        self._add_epiphany_day(tr("Timket"))

        # Orthodox Easter.
        self._add_easter_sunday(tr("Tensae"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # International Workers' Day.
        self._add_labor_day(tr("International Workers' Day"))

        # Independence Day.
        self._add_holiday_may_24(tr("Independence Day"))

        # Festival of Mariam Dearit.
        self._add_holiday_may_29(tr("Festival of Mariam Dearit"))

        # Martyrs' Day.
        self._add_holiday_jun_20(tr("Martyrs' Day"))

        if self._year >= 2011:
            # Mariam Debre Sina.
            self._add_holiday_jun_28(tr("Mariam Debre Sina"))

        if self._year >= 2011:
            # Debre Bizen Abune Libanos.
            self._add_holiday_aug_11(tr("Debre Bizen Abune Libanos"))

        # Revolution Day.
        self._add_holiday_sep_1(tr("Revolution Day"))

        # Orthodox New Year.
        self._add_holiday_sep_11(tr("Keddus Yohannes"))

        # Finding of the True Cross.
        self._add_holiday_sep_27(tr("Meskel"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Eid al-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Eid al-Adha"))

        # Muharram.
        self._add_islamic_new_year_day(tr("Muharram"))

        # Mawlid an-Nabi.
        self._add_mawlid_day(tr("Mawlid an-Nabi"))


class ER(Eritrea):
    pass


class ERI(Eritrea):
    pass


class EritreaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (1994, 2025)
    EID_AL_ADHA_DATES = {
        1994: (MAY, 21),
        1995: (MAY, 10),
        1996: (APR, 28),
        1997: (APR, 18),
        1999: (MAR, 28),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2010: (NOV, 17),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2018: (AUG, 22),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
    }
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (1994, 2025)
    EID_AL_FITR_DATES = {
        1994: (MAR, 14),
        1995: (MAR, 3),
        1996: (FEB, 20),
        1997: (FEB, 9),
        1998: (JAN, 30),
        1999: (JAN, 19),
        2002: (DEC, 6),
        2006: (OCT, 24),
        2019: (JUN, 5),
        2023: (APR, 22),
        2025: (MAR, 31),
    }
    MAWLID_DATES_CONFIRMED_YEARS = (1994, 2025)
    MAWLID_DATES = {
        1994: (AUG, 20),
        1995: (AUG, 9),
        1996: (JUL, 28),
        1997: (JUL, 17),
        2000: (JUN, 15),
        2002: (MAY, 25),
        2003: (MAY, 15),
        2004: (MAY, 3),
        2005: (APR, 22),
        2012: (FEB, 5),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2021: (OCT, 20),
        2023: (SEP, 28),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }
