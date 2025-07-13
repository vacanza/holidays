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

from holidays.calendars.gregorian import JAN, MAY, JUN, AUG, SEP
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class Gibraltar(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Gibraltar holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Gibraltar>
        * [Public Holidays 2003](https://web.archive.org/web/20250508170633/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-7023/version/12-12-2002)
        * [Public Holidays 2004](https://web.archive.org/web/20250417151549/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2003-208)
        * [Public Holidays 2005](https://web.archive.org/web/20250508201034/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2004-681/version/29-07-2004)
        * [Public Holidays 2006](https://web.archive.org/web/20250417152547/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2005-1141)
        * [Public Holidays 2007](https://web.archive.org/web/20250508195007/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2006-1667/version/09-11-2006)
        * [Public Holidays 2008](https://web.archive.org/web/20250417171642/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2007-2094)
        * [Public Holidays 2009](https://web.archive.org/web/20250507113355/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2008-2215/version/25-09-2008)
        * [Public Holidays 2010](https://web.archive.org/web/20250508191428/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2009-2359/version/17-09-2009)
        * [Public Holidays 2011](https://web.archive.org/web/20250616034613/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2010-2577)
        * [Public Holidays 2012](https://web.archive.org/web/20250513201915/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-no-2-order-2011-2988)
        * [Public Holidays 2013](https://web.archive.org/web/20250713063848/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2012-3179/download)
        * [Public Holidays 2014](https://web.archive.org/web/20250519052526/https://gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2013-3445)
        * [Public Holidays 2015](https://web.archive.org/web/20250713063847/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2014-3748/download)
        * [Public Holidays 2016](https://web.archive.org/web/20161114150646/https://www.gibraltar.gov.gi/new/sites/default/files/press/2016/Official%20Notices/Bank%20and%20Public%20Holidays%202016.pdf)
        * [Public Holidays 2017](https://web.archive.org/web/20250417213423/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2016-3555)
        * [Gibraltar National Day on 4th September, 2017](https://web.archive.org/web/20250417213423/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2016-3555)
        * [Public Holidays 2018](https://web.archive.org/web/20240331045345/https://www.gibraltar.gov.gi/new/sites/default/files/press/2017/Official%20Notices/BANK%20HOLIDAYS%202018.pdf)
        * [Public Holidays 2019](https://web.archive.org/web/20250508170408/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2018-4419/version/25-10-2018)
        * [Public Holidays 2020](https://web.archive.org/web/20250426144346/https://www.gibraltar.gov.gi/press-releases/bank-and-public-holidays-2020-5363)
        * [Public Holidays 2021](https://web.archive.org/web/20250417172202/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2020-5593)
        * [Public Holidays 2022](https://web.archive.org/web/20250508175822/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2021-6286/version/21-10-2021)
        * [Public Holidays 2023](https://web.archive.org/web/20250508180948/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2022-6735/version/22-02-2023)
        * [Public Holidays 2024](https://web.archive.org/web/20250502091333/https://gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2023-7215/version/06-11-2023)
        * [Public Holidays 2025](https://web.archive.org/web/20250402130104/https://www.gibraltar.gov.gi/press-releases/bank-and-public-holidays-2025-10243)
    """

    country = "GI"
    default_language = "en_GB"
    # %s (observed).
    observed_label = "%s (observed)"
    # First holiday info available from 2003.
    start_year = 2003
    supported_languages = ("en_GB", "en_US")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, GibraltarStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self._add_observed(
            # New Year's Day.
            self._add_new_years_day(tr("New Year's Day")),
        )

        if self._year >= 2023:
            # Winter Midterm Bank Holiday.
            name = tr("Winter Midterm Bank Holiday")
            (
                self._add_holiday_2nd_mon_of_feb(name)
                if self._year == 2024
                else self._add_holiday_3rd_mon_of_feb(name)
            )

        if self._year <= 2022:
            # Commonwealth Day.
            name = tr("Commonwealth Day")
            (
                self._add_holiday_2nd_mon_of_mar(name)
                if self._year <= 2020
                else self._add_holiday_3rd_mon_of_feb(name)
            )

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # May Day.
        name = tr("May Day")
        special_dts = {
            2007: (MAY, 7),
            2008: (MAY, 5),
            2009: (MAY, 4),
            2010: (MAY, 3),
            2011: (MAY, 2),
            2013: (MAY, 6),
            2016: (MAY, 2),
            2021: (MAY, 3),
        }
        (
            self._add_holiday(name, dt)
            if (dt := special_dts.get(self._year))
            else self._add_observed(self._add_labor_day(name))
        )

        # Spring Bank Holiday.
        name = tr("Spring Bank Holiday")
        spring_bank_dts = {
            2012: (JUN, 4),
            2022: (JUN, 2),
        }
        if dt := spring_bank_dts.get(self._year):
            self._add_holiday(name, dt)
        else:
            self._add_holiday_last_mon_of_may(name)

        name = (
            # King's Birthday.
            tr("King's Birthday")
            if self._year >= 2023
            # Queen's Birthday.
            else tr("Queen's Birthday")
        )
        sovereign_birthday_dts = {
            2006: (JUN, 19),
            2007: (JUN, 18),
            2012: (JUN, 18),
            2013: (JUN, 17),
            2017: (JUN, 19),
            2019: (JUN, 17),
        }
        if dt := sovereign_birthday_dts.get(self._year):
            self._add_holiday(name, dt)
        elif self._year <= 2022:
            self._add_holiday_2_days_past_2nd_sat_of_jun(name)
        else:
            self._add_holiday_3rd_mon_of_jun(name)

        name = (
            # Summer Bank Holiday.
            tr("Summer Bank Holiday")
            if self._year <= 2007
            # Late Summer Bank Holiday.
            else tr("Late Summer Bank Holiday")
        )
        self._add_holiday_last_mon_of_aug(name)

        # Gibraltar National Day.
        name = tr("Gibraltar National Day")
        national_day_dts = {
            2016: (SEP, 5),
            2017: (SEP, 4),
        }
        if dt := national_day_dts.get(self._year):
            self._add_holiday(name, dt)
        else:
            self._add_observed(self._add_holiday_sep_10(name))

        self._add_observed(
            # Christmas Day.
            self._add_christmas_day(tr("Christmas Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        self._add_observed(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )


class GI(Gibraltar):
    pass


class GIB(Gibraltar):
    pass


class GibraltarStaticHolidays(StaticHolidays):
    """Gibraltar Special Holidays.

    References:
        * [Tercentenary Holiday](https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2003-208)
        * [12th January, 2009](https://web.archive.org/web/20250507113355/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2008-2215/version/25-09-2008)
        * [Queen's Diamond Jubilee](https://web.archive.org/web/20250513201915/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-no-2-order-2011-2988)
        * [Evacuation Commemoration Day, 2015](https://web.archive.org/web/20250713063810/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-no-2-order-2015-3921/download)
        * [75th Anniversary of VE Day, 2020](https://web.archive.org/web/20250426144346/https://www.gibraltar.gov.gi/press-releases/bank-and-public-holidays-2020-5363)
        * [Platinum Jubilee](https://web.archive.org/web/20250508175822/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2021-6286/version/21-10-2021)
        * [Special King's Coronation Bank Holiday, 2023](https://web.archive.org/web/20250508180948/https://www.gibraltarlaws.gov.gi/legislations/bank-and-public-holidays-order-2022-6735/version/22-02-2023)
    """

    special_public_holidays = {
        # Tercentenary Holiday.
        2004: (AUG, 4, tr("Tercentenary Holiday")),
        # Bank Holiday.
        2009: (JAN, 12, tr("Bank Holiday")),
        # Queen's Diamond Jubilee.
        2012: (JUN, 5, tr("Queen's Diamond Jubilee")),
        # Evacuation Commemoration Day.
        2015: (SEP, 7, tr("Evacuation Commemoration Day")),
        # 75th Anniversary of VE Day.
        2020: (MAY, 8, tr("75th Anniversary of VE Day")),
        # Platinum Jubilee.
        2022: (JUN, 3, tr("Platinum Jubilee")),
        # Special King’s Coronation Bank Holiday.
        2023: (MAY, 8, tr("Special King's Coronation Bank Holiday")),
    }
