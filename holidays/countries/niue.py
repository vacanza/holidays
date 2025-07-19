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

from holidays import SEP
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_MON_TUE


class Niue(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Niue holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Niue>
        * <https://en.wikipedia.org/wiki/Niue_Constitution_Act>
        * [Public Holidays Ordinance 1961](https://web.archive.org/web/20250102100637/http://www.paclii.org/nu/legis/num_act/nipho1961314.pdf)
        * <https://www.gov.nu/public-service-circulars>
        * <http://archive.today/2025.07.14-145535/https://www.wipo.int/wipolex/en/text/427817>
        * <https://web.archive.org/web/20250223114854/https://niuepocketguide.com/public-holidays-in-niue-other-important-dates/>
        * [Queen's Birthday](https://web.archive.org/web/20220928145826/https://publicholidays.asia/niue/queens-birthday/)
        * [2018](https://web.archive.org/web/20230322165612/https://publicholidays.asia/niue/2018-dates/)
        * [2025](https://web.archive.org/web/20241208034202/https://www.qppstudio.net/publicholidays2025/niue.htm)
    """

    country = "NU"
    default_language = "en_NU"
    # %s observed.
    observed_label = tr("%s (observed)")
    # Public Holidays Ordinance 1961.
    start_year = 1962
    supported_languages = ("en_NU", "en_US")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=NiueStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON_TUE)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Takai Commission Holiday.
        self._add_observed(self._add_new_years_day_two(tr("Takai Commission Holiday")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        self._add_holiday_1st_mon_of_jun(
            # Queen's Birthday.
            tr("Queen's Birthday")
            if self._year <= 2022
            # King's Birthday.
            else tr("King's Birthday")
        )

        if self._year >= 1974:
            # Constitution Day.
            self._add_observed(self._add_holiday_oct_19(tr("Constitution Day")))

            # Constitution Day Holiday.
            self._add_observed(self._add_holiday_oct_20(tr("Constitution Day Holiday")))
        else:
            # Annexation Day.
            self._add_holiday_3rd_mon_of_oct(tr("Annexation Day"))

        # Peniamina Gospel Day.
        self._add_holiday_4th_mon_of_oct(tr("Peniamina Gospel Day"))

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two(tr("Boxing Day")))


class NU(Niue):
    pass


class NIU(Niue):
    pass


class NiueStaticHolidays:
    """Niue special holidays.

    References:
        * [Queen Elizabeth II's Funeral](https://web.archive.org/web/20250617174022/https://tvniue.com/2022/09/premier-will-attend-hm-the-queens-funeral-while-monday-19th-is-declared-one-off-public-holiday/)
    """

    special_public_holidays = {
        # Queen Elizabeth II's Funeral.
        2022: (SEP, 19, tr("Queen Elizabeth II's Funeral")),
    }
