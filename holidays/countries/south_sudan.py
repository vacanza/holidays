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

from holidays.constants import ISLAMIC, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class SouthSudan(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """South Sudan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_South_Sudan>
        * <https://web.archive.org/web/20250716011243/https://mogei.gov.ss/super/assets/documents/calendar/2024_MoGEI_Academic%20calendar%20and%20implemention%20guidelines_%20South%20Sudan_A5_final_Approved%20and%20signed%20-%203.pdf>
        * <https://web.archive.org/web/20241211222746/http://www.doitinafrica.com/south-sudan/events/public-holidays.htm>
    """

    country = "SS"
    # %s (estimated).
    estimated_label = "%s (estimated)"
    # South Sudan became independent on 9 July 2011.
    start_year = 2012
    supported_categories = (ISLAMIC, PUBLIC)

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Holy Saturday.
        self._add_holy_saturday("Holy Saturday")

        # Easter Sunday.
        self._add_easter_sunday("Easter Sunday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # SPLA Day.
        self._add_holiday_may_16("SPLA Day")

        # Independence Day.
        self._add_holiday_jul_9("Independence Day")

        # Martyrs' Day.
        self._add_holiday_jul_30("Martyrs' Day")

        # Christmas Eve.
        self._add_christmas_eve("Christmas Eve")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Second Day of Christmas.
        self._add_christmas_day_two("Second Day of Christmas")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid al-Fitr")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid al-Adha")

    def _populate_islamic_holidays(self):
        # Eid al-Fitr Holiday.
        self._add_eid_al_fitr_day_two("Eid al-Fitr Holiday")

        # Eid al-Adha Holiday.
        self._add_eid_al_adha_day_two("Eid al-Adha Holiday")


class SS(SouthSudan):
    pass


class SSD(SouthSudan):
    pass
