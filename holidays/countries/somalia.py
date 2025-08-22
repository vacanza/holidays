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
from holidays.calendars.gregorian import JAN, APR, MAY, JUN, JUL, AUG, SEP, NOV, FEB, MAR, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Somalia(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Somalia holidays.

    References:
        * <https://usa.mfa.gov.so/about-somalia/>
        * <https://web.archive.org/web/20220607190753/https://aip.scaa.gov.so/eAIP/HC-GEN-2.1-en-GB.html>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Somalia>
        * <https://www.hijria.com/en/hijri-gregorian-calendar/somalia/>
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
    ASHURA_DATES_CONFIRMED_YEARS = (1960, 2025)
    ASHURA_DATES = {
        1965: (MAY, 11),
        1967: (APR, 19),
        1968: (APR, 7),
        1970: (MAR, 17),
        1976: (DEC, 31),
        1980: (NOV, 17),
        2009: (JAN, 7),
    }

    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (1960, 2025)
    EID_AL_ADHA_DATES = {
        1961: (MAY, 24),
        1965: (APR, 12),
        1969: (FEB, 26),
        1971: (FEB, 5),
        1974: (DEC, 23),
        2006: (DEC, 31),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (1960, 2025)
    EID_AL_FITR_DATES = {
        1961: (MAR, 17),
        1963: (FEB, 25),
        1967: (JAN, 11),
        1968: (DEC, 20),
        1970: (NOV, 29),
        1980: (AUG, 11),
        2000: (DEC, 27),
    }

    HIJRI_NEW_YEAR_DATES_CONFIRMED_YEARS = (1960, 2025)
    HIJRI_NEW_YEAR_DATES = {
        1965: (MAY, 2),
        1967: (APR, 10),
        1968: (MAR, 29),
        1970: (MAR, 8),
        1976: (DEC, 22),
        1980: (NOV, 8),
        2008: (JAN, 10),
    }

    ISRA_AND_MIRAJ_DATES_CONFIRMED_YEARS = (1960, 2025)
    ISRA_AND_MIRAJ_DATES = {
        1960: (JAN, 25),
        1962: (DEC, 24),
        1970: (SEP, 27),
        1971: (SEP, 16),
        1994: (DEC, 29),
    }

    MAWLID_DATES_CONFIRMED_YEARS = (1960, 2025)
    MAWLID_DATES = {
        1963: (AUG, 1),
        1965: (JUL, 11),
        1966: (JUN, 30),
        1967: (JUN, 20),
        1970: (MAY, 17),
        1980: (JAN, 29),
        1982: (DEC, 27),
        2015: (JAN, 3),
    }
