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
from holidays.calendars.gregorian import JAN, APR, MAY, JUN, JUL, OCT, AUG, SEP, NOV, FEB, MAR, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Somalia(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Somalia holidays.

    References:
        * <https://usa.mfa.gov.so/about-somalia/>
        * <https://web.archive.org/web/20220607190753/https://aip.scaa.gov.so/eAIP/HC-GEN-2.1-en-GB.html>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Somalia>
    """

    country = "SO"
    # July 1, 1960, the State of Somaliland united with the Trust Territory of Somaliland
    # (formerly Italian Somaliland) to form the Somali Republic
    start_year = 1960

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=SomaliaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # Restoration of Somaliland Sovereignty Day.
        name = "Restoration of Somaliland Sovereignty Day"
        self._add_holiday_may_18(name)
        self._add_holiday_may_19(name)

        # Independence Day.
        self._add_holiday_jun_26("Independence Day")

        # Republic Day.
        self._add_holiday_jul_1("Republic Day")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid al-Fitr")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid al-Adha")

        # Birthday of Muhammad.
        self._add_mawlid_day("Birthday of Muhammad")

        # Muhammad's Ascension to Heaven.
        self._add_isra_and_miraj_day("Muhammad's Ascension to Heaven")

        # Islamic New Year.
        self._add_islamic_new_year_day("Islamic New Year")

        # Ashura.
        self._add_ashura_day("Ashura")


class SO(Somalia):
    pass


class SOM(Somalia):
    pass


class SomaliaIslamicHolidays(_CustomIslamicHolidays):
    """Islamic holidays specific to Somalia

    Reference:
        * <https://www.hijria.com/en/hijri-gregorian-calendar/somalia/>
    """

    ASHURA_DATES_CONFIRMED_YEARS = (1960, 2025)
    ASHURA_DATES = {
        1960: (JUL, 4),
        1961: (JUN, 23),
        1962: (JUN, 12),
        1963: (JUN, 2),
        1964: (MAY, 21),
        1965: (MAY, 11),
        1966: (APR, 30),
        1967: (APR, 19),
        1968: (APR, 7),
        1969: (MAR, 28),
        1970: (MAR, 17),
        1971: (MAR, 7),
        1972: (FEB, 25),
        1973: (FEB, 13),
        1974: (FEB, 2),
        1975: (JAN, 22),
        1976: (DEC, 31),
        1977: (DEC, 20),
        1978: (DEC, 10),
        1979: (NOV, 29),
        1980: (NOV, 17),
        1981: (NOV, 6),
        1982: (OCT, 27),
        1983: (OCT, 16),
        1984: (OCT, 5),
        1985: (SEP, 24),
        1986: (SEP, 14),
        1987: (SEP, 3),
        1988: (AUG, 22),
        1989: (AUG, 11),
        1990: (AUG, 1),
        1991: (JUL, 21),
        1992: (JUL, 10),
        1993: (JUN, 30),
        1994: (JUN, 19),
        1995: (JUN, 8),
        1996: (MAY, 27),
        1997: (MAY, 16),
        1998: (MAY, 6),
        1999: (APR, 26),
        2000: (APR, 15),
        2001: (APR, 4),
        2002: (MAR, 24),
        2003: (MAR, 13),
        2004: (MAR, 1),
        2005: (FEB, 19),
        2006: (FEB, 9),
        2007: (JAN, 29),
        2008: (JAN, 19),
        2009: (JAN, 7),
        2010: (DEC, 16),
        2011: (DEC, 5),
        2012: (NOV, 24),
        2013: (NOV, 13),
        2014: (NOV, 3),
        2015: (OCT, 23),
        2016: (OCT, 11),
        2017: (SEP, 30),
        2018: (SEP, 20),
        2019: (SEP, 9),
        2020: (AUG, 29),
        2021: (AUG, 18),
        2022: (AUG, 8),
        2023: (JUL, 28),
        2024: (JUL, 16),
        2025: (JUL, 5),
    }

    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (1960, 2025)
    EID_AL_ADHA_DATES = {
        1960: (JUN, 4),
        1961: (MAY, 24),
        1962: (MAY, 14),
        1963: (MAY, 3),
        1964: (APR, 22),
        1965: (APR, 12),
        1966: (APR, 1),
        1967: (MAR, 21),
        1968: (MAR, 9),
        1969: (FEB, 26),
        1970: (FEB, 16),
        1971: (FEB, 5),
        1972: (JAN, 26),
        1973: (JAN, 14),
        1974: (DEC, 23),
        1975: (DEC, 13),
        1976: (DEC, 1),
        1977: (NOV, 21),
        1978: (NOV, 10),
        1979: (OCT, 31),
        1980: (OCT, 19),
        1981: (OCT, 8),
        1982: (SEP, 27),
        1983: (SEP, 17),
        1984: (SEP, 5),
        1985: (AUG, 26),
        1986: (AUG, 15),
        1987: (AUG, 4),
        1988: (JUL, 23),
        1989: (JUL, 13),
        1990: (JUL, 2),
        1991: (JUN, 22),
        1992: (JUN, 11),
        1993: (MAY, 31),
        1994: (MAY, 20),
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

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (1960, 2025)
    EID_AL_FITR_DATES = {
        1960: (MAR, 28),
        1961: (MAR, 17),
        1962: (MAR, 7),
        1963: (FEB, 25),
        1964: (FEB, 14),
        1965: (FEB, 2),
        1966: (JAN, 22),
        1967: (JAN, 11),
        1968: (DEC, 20),
        1969: (DEC, 10),
        1970: (NOV, 29),
        1971: (NOV, 19),
        1972: (NOV, 7),
        1973: (OCT, 27),
        1974: (OCT, 16),
        1975: (OCT, 6),
        1976: (SEP, 24),
        1977: (SEP, 14),
        1978: (SEP, 3),
        1979: (AUG, 23),
        1980: (AUG, 11),
        1981: (AUG, 1),
        1982: (JUL, 21),
        1983: (JUL, 11),
        1984: (JUN, 30),
        1985: (JUN, 19),
        1986: (JUN, 8),
        1987: (MAY, 28),
        1988: (MAY, 16),
        1989: (MAY, 6),
        1990: (APR, 26),
        1991: (APR, 15),
        1992: (APR, 4),
        1993: (MAR, 24),
        1994: (MAR, 13),
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

    MAWLID_DATES_CONFIRMED_YEARS = (1960, 2025)
    MAWLID_DATES = {
        1960: (SEP, 3),
        1961: (AUG, 23),
        1962: (AUG, 12),
        1963: (AUG, 1),
        1964: (JUL, 21),
        1965: (JUL, 11),
        1966: (JUN, 30),
        1967: (JUN, 20),
        1968: (JUN, 8),
        1969: (MAY, 28),
        1970: (MAY, 17),
        1971: (MAY, 7),
        1972: (APR, 25),
        1973: (APR, 15),
        1974: (APR, 4),
        1975: (MAR, 24),
        1976: (MAR, 12),
        1977: (MAR, 2),
        1978: (FEB, 19),
        1979: (FEB, 9),
        1980: (JAN, 29),
        1981: (JAN, 18),
        1982: (DEC, 27),
        1983: (DEC, 16),
        1984: (DEC, 4),
        1985: (NOV, 24),
        1986: (NOV, 14),
        1987: (NOV, 3),
        1988: (OCT, 22),
        1989: (OCT, 11),
        1990: (OCT, 1),
        1991: (SEP, 20),
        1992: (SEP, 9),
        1993: (AUG, 29),
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
        2015: (JAN, 3),
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

    ISRA_AND_MIRAJ_DATES_CONFIRMED_YEARS = (1960, 2025)
    ISRA_AND_MIRAJ_DATES = {
        1960: (JAN, 25),
        1961: (JAN, 14),
        1962: (DEC, 24),
        1963: (DEC, 13),
        1964: (DEC, 1),
        1965: (NOV, 20),
        1966: (NOV, 10),
        1967: (OCT, 30),
        1968: (OCT, 19),
        1969: (OCT, 8),
        1970: (SEP, 27),
        1971: (SEP, 16),
        1972: (SEP, 5),
        1973: (AUG, 25),
        1974: (AUG, 15),
        1975: (AUG, 5),
        1976: (JUL, 24),
        1977: (JUL, 13),
        1978: (JUL, 2),
        1979: (JUN, 22),
        1980: (JUN, 10),
        1981: (MAY, 31),
        1982: (MAY, 20),
        1983: (MAY, 10),
        1984: (APR, 28),
        1985: (APR, 17),
        1986: (APR, 6),
        1987: (MAR, 27),
        1988: (MAR, 15),
        1989: (MAR, 5),
        1990: (FEB, 22),
        1991: (FEB, 11),
        1992: (JAN, 31),
        1993: (JAN, 20),
        1994: (DEC, 29),
        1995: (DEC, 19),
        1996: (DEC, 8),
        1997: (NOV, 27),
        1998: (NOV, 16),
        1999: (NOV, 5),
        2000: (OCT, 24),
        2001: (OCT, 14),
        2002: (OCT, 4),
        2003: (SEP, 24),
        2004: (SEP, 12),
        2005: (SEP, 1),
        2006: (AUG, 21),
        2007: (AUG, 10),
        2008: (JUL, 30),
        2009: (JUL, 20),
        2010: (JUL, 9),
        2011: (JUN, 29),
        2012: (JUN, 17),
        2013: (JUN, 6),
        2014: (MAY, 26),
        2015: (MAY, 16),
        2016: (MAY, 4),
        2017: (APR, 24),
        2018: (APR, 13),
        2019: (APR, 3),
        2020: (MAR, 22),
        2021: (MAR, 11),
        2022: (FEB, 28),
        2023: (FEB, 18),
        2024: (FEB, 8),
        2025: (JAN, 27),
    }

    ISLAMIC_NEW_YEAR_DATES_CONFIRMED_YEARS = (1960, 2025)
    ISLAMIC_NEW_YEAR_DATES = {
        1960: (JUN, 25),
        1961: (JUN, 14),
        1962: (JUN, 3),
        1963: (MAY, 24),
        1964: (MAY, 12),
        1965: (MAY, 2),
        1966: (APR, 21),
        1967: (APR, 10),
        1968: (MAR, 29),
        1969: (MAR, 19),
        1970: (MAR, 8),
        1971: (FEB, 26),
        1972: (FEB, 16),
        1973: (FEB, 4),
        1974: (JAN, 24),
        1975: (JAN, 13),
        1976: (DEC, 22),
        1977: (DEC, 11),
        1978: (DEC, 1),
        1979: (NOV, 20),
        1980: (NOV, 8),
        1981: (OCT, 28),
        1982: (OCT, 18),
        1983: (OCT, 7),
        1984: (SEP, 26),
        1985: (SEP, 15),
        1986: (SEP, 5),
        1987: (AUG, 25),
        1988: (AUG, 13),
        1989: (AUG, 2),
        1990: (JUL, 23),
        1991: (JUL, 12),
        1992: (JUL, 1),
        1993: (JUN, 21),
        1994: (JUN, 10),
        1995: (MAY, 30),
        1996: (MAY, 18),
        1997: (MAY, 7),
        1998: (APR, 27),
        1999: (APR, 17),
        2000: (APR, 6),
        2001: (MAR, 26),
        2002: (MAR, 15),
        2003: (MAR, 4),
        2004: (FEB, 21),
        2005: (FEB, 10),
        2006: (JAN, 31),
        2007: (JAN, 20),
        2008: (JAN, 10),
        2009: (DEC, 18),
        2010: (DEC, 7),
        2011: (NOV, 26),
        2012: (NOV, 15),
        2013: (NOV, 4),
        2014: (OCT, 25),
        2015: (OCT, 14),
        2016: (OCT, 2),
        2017: (SEP, 21),
        2018: (SEP, 11),
        2019: (AUG, 31),
        2020: (AUG, 20),
        2021: (AUG, 9),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 7),
        2025: (JUN, 26),
    }
