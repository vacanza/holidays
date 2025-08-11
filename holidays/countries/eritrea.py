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
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
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

        # Revolution Day.
        self._add_holiday_sep_1(tr("Revolution Day"))

        # Orthodox New Year.
        self._add_holiday_sep_11(tr("Keddus Yohannes"))

        # Finding of the True Cross.
        self._add_holiday_sep_27(tr("Meskel"))

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("Muharram"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Mawlid an-Nabi"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Eid al-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Eid al-Adha"))


class ER(Eritrea):
    pass


class ERI(Eritrea):
    pass
