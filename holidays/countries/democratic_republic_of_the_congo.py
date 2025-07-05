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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class DemocraticRepublicOfTheCongo(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Democratic Republic of the Congo holidays.

    References:
        * [Democratic Republic of the Congo](https://web.archive.org/web/20220428223822/https://www.eac.int/eac-partner-states/drcongo)
        * [Independence Day in DR Congo in 2020](https://web.archive.org/web/20200607141425/https://www.officeholidays.com/holidays/dr-congo/dr-congo-independence-day)

    Cross-Checked With:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Democratic_Republic_of_the_Congo>
    """

    country = "CD"
    default_language = "fr"
    supported_languages = ("en_US", "fr")
    # Democratic Republic of the Congo marks independence from Belgium in June 1960.
    start_year = 1960

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jour de l'An"))

        # Martyrs' Day.
        self._add_holiday_jan_4(tr("Journée des Martyrs"))

        if self._year >= 2001:
            # Laurent-Désiré Kabila Assassination.
            self._add_holiday_jan_16(tr("Assassinat de Laurent-Désiré Kabila"))

        if self._year >= 1961:
            # Patrice Lumumba Assassination.
            self._add_holiday_jan_16(tr("Assassinat de Patrice Lumumba"))

        if self._year >= 2023:
            # Kimbangu's Day.
            self._add_holiday_apr_6(tr("Journée de Kimbangu"))

        # Labor Day.
        self._add_labor_day(tr("Fête du Travail"))

        if 1997 <= self._year < 2019:
            # Liberation Day.
            self._add_holiday_may_17(tr("Jour de la Libération"))
        elif self._year >= 2019:
            # Armed Forces Day.
            self._add_holiday_may_17(tr("Journée des forces armées"))

        # Independence Day.
        self._add_holiday_jun_30(tr("Jour de l'indépendance"))

        # Parents' Day.
        self._add_holiday_aug_1(tr("Journée des parents"))

        if self._year >= 2024:
            # Congolese Genocide Day.
            self._add_holiday_aug_2(tr("Journée du génocide congolais"))

        # Christmas Day.
        self._add_christmas_day(tr("Noël"))


class CD(DemocraticRepublicOfTheCongo):
    pass


class COD(DemocraticRepublicOfTheCongo):
    pass
