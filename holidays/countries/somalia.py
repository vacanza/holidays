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
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # Independence Day.
        self._add_holiday_jun_26("Independence Day")

        # Republic Day.
        self._add_holiday_jul_1("Republic Day")

        # Ashura.
        self._add_ashura_day("Ashura")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid al-Adha")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid al-Fitr")

        # Islamic New Year.
        self._add_islamic_new_year_day("Islamic New Year")

        # Muhammad's Ascension to Heaven.
        self._add_isra_and_miraj_day("Muhammad's Ascension to Heaven")

        # Birthday of Muhammad.
        self._add_mawlid_day("Birthday of Muhammad")


class SO(Somalia):
    pass


class SOM(Somalia):
    pass
