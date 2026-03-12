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


class Kosovo(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Kosovo holidays.

    References:
        * <https://bqk-kos.org/kalendari-i-festave/>
        * Law No. 03/L-064 on Public Holidays in the Republic of Kosovo.
    """

    country = "XK"
    default_language = "sq"
    # %s (estimated).
    estimated_label = tr("%s (e vlerësuar)")
    supported_languages = ("en_US", "sq", "sr")
    # Independence declared on 2008-02-17.
    start_year = 2008

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
        name = tr("Viti i Ri")
        self._add_new_years_day(name)
        self._add_new_years_day_two(name)

        # Orthodox Christmas Day.
        self._add_christmas_day(tr("Krishtlindjet Ortodokse"), JULIAN_CALENDAR)

        # Independence Day.
        self._add_holiday_feb_17(tr("Dita e Pavarësisë së Republikës së Kosovës"))

        # Constitution Day.
        self._add_holiday_apr_9(tr("Dita e Kushtetutës së Republikës së Kosovës"))

        # International Workers' Day.
        self._add_labor_day(tr("Dita Ndërkombëtare e Punës"))

        # Europe Day.
        self._add_europe_day(tr("Dita e Evropës"))

        # Catholic Easter.
        name = tr("Pashkët Katolike")
        self._add_easter_sunday(name)
        self._add_easter_monday(name)

        # Orthodox Easter.
        name = tr("Pashkët Ortodokse")
        self._add_easter_sunday(name, JULIAN_CALENDAR)
        self._add_easter_monday(name, JULIAN_CALENDAR)

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Bajrami i Madh, dita e parë"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Bajrami i Vogël, dita e parë"))

        # Catholic Christmas Day.
        self._add_christmas_day(tr("Krishtlindjet Katolike"))


class XK(Kosovo):
    pass


class XKK(Kosovo):
    pass
