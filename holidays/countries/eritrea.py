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


from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Eritrea(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Eritrea holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Eritrea>
        * <https://web.archive.org/web/20250609235122/http://www.eritrea.be/old/eritrea-religions.htm>
        * <https://web.archive.org/web/20110903130335/http://www.eritrea.be/old/eritrea-religions.htm>
        * <https://web.archive.org/web/20081010180144/http://www.eritrea.be/old/eritrea-religions.htm>
    """

    country = "ER"
    # On 28 May 1993, Eritrea was admitted into the United Nations as the 182nd member state.
    start_year = 1994

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=EritreaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year")

        # Leddet.
        self._add_holiday_jan_7("Leddet")

        # Timket.
        self._add_holiday_jan_19("Timket")

        # Tensae.
        self._add_easter_sunday("Tensae")

        # Festival of Mariam Dearit.
        self._add_holiday_may_29("Festival of Mariam Dearit")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid al-Fitr")

        if self._year >= 2011:
            # Mariam Debre Sina.
            self._add_holiday_jun_28("Mariam Debre Sina")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid al-Adha")

        if self._year >= 2011:
            # Debre Bizen Abune Libanos.
            self._add_holiday_aug_11("Debre Bizen Abune Libanos")

        # Keddus Yohannes.
        self._add_holiday_sep_11("Keddus Yohannes")

        # Meskel.
        self._add_holiday_sep_27("Meskel")

        # Muharram.
        self._add_islamic_new_year_day("Muharram")

        # Mawlid an-Nabi.
        self._add_mawlid_day("Mawlid an-Nabi")

        # Christmas.
        self._add_christmas_day("Christmas")


class ER(Eritrea):
    pass


class ERI(Eritrea):
    pass


class EritreaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        1994: (MAY, 21),
        1995: (MAY, 10),
        1996: (APR, 28),
        1997: (APR, 18),
        1998: (APR, 7),
        1999: (MAR, 28),
        2000: (MAR, 16),
        2001: (MAR, 5),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 27),
        2010: (NOV, 17),
        2011: (NOV, 6),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 6),
    }

    EID_AL_FITR_DATES = {
        1994: (MAR, 14),
        1995: (MAR, 3),
        1996: (FEB, 20),
        1997: (FEB, 9),
        1998: (JAN, 30),
        1999: (JAN, 19),
        2000: ((JAN, 8), (DEC, 27)),
        2001: (DEC, 16),
        2002: (DEC, 6),
        2003: (NOV, 25),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 24),
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
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    MAWLID_DATES = {
        1994: (AUG, 20),
        1995: (AUG, 9),
        1996: (JUL, 28),
        1997: (JUL, 17),
        1998: (JUL, 6),
        1999: (JUN, 26),
        2000: (JUN, 15),
        2001: (JUN, 4),
        2002: (MAY, 25),
        2003: (MAY, 15),
        2004: (MAY, 3),
        2005: (APR, 22),
        2006: (APR, 10),
        2007: (MAR, 31),
        2008: (MAR, 20),
        2009: (MAR, 9),
        2010: (FEB, 26),
        2011: (FEB, 15),
        2012: (FEB, 5),
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 20),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 20),
        2022: (OCT, 8),
        2023: (SEP, 28),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }
