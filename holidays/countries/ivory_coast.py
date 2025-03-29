#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)

from gettext import gettext as tr

from holidays.constants import PUBLIC
from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class IvoryCoast(ObservedHolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays):
    """
    Ivory Coast holidays.

    References:
        * <https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=44374>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Ivory_Coast>
        * <https://www.timeanddate.com/holidays/ivory-coast/>
        * <https://holidayapi.com/countries/ci/>
    """

    country = "CI"
    estimated_label = tr("%s (estimated)")
    observed_label = tr("%s (observed)")
    observed_estimated_label = tr("%s (observed, estimated)")
    supported_categories = (PUBLIC,)
    # Ivory Coast gained independence in 1960.
    start_year = 1960

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Secular Holidays
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")), rule=SUN_TO_NEXT_MON)
        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Labor Day")), rule=SUN_TO_NEXT_MON)
        # Independence Day
        self._add_holiday_aug_7(tr("Independence Day"))
        if self._year >= 1996:
            # National Peace Day - November 15.
            # Introduced in 1996. See details: https://en.wikipedia.org/wiki/C%C3%B4te_d%27Ivoire#History
            self._add_holiday_nov_15(tr("National Peace Day"))

        # Christan Holidays
        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))
        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))
        # Pentecost Monday (Whit Monday).
        self._add_whit_monday(tr("Pentecost Monday"))
        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Assumption Day"))
        # All Saints' Day - November 1.
        self._add_all_saints_day(tr("All Saints' Day"))
        # Christmas Day - December 25.
        self._add_christmas_day(tr("Christmas Day"))

        # Islamic Holidays
        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Eid al-Fitr"))
        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Eid al-Adha"))
        # Prophet's Birthday
        self._add_mawlid_day(tr("Prophet's Birthday"))

        # todo: Day After Laila tou-Kadr
        # self._add_laylat_al_qadr_day(tr("Night of Destiny"))


# Aliases.
class CI(IvoryCoast):
    pass


class CIV(IvoryCoast):
    pass
