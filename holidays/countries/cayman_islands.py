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

from holidays import APR, MAY, JUN, SEP, NOV
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class CaymanIslands(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Cayman Islands holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Cayman_Islands>
        * <https://web.archive.org/web/20250212214050/https://www.timeanddate.com/holidays/cayman-islands/2025>
        * [Public Holidays Law (2007 Revision)](https://web.archive.org/web/20250227060525/https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0140/PublicHolidaysAct_2007%20Revision_g.pdf)
        * [Public Holidays Order, 2024](https://web.archive.org/web/20240518181823/https://legislation.gov.ky/cms/images/LEGISLATION/AMENDING/2024/2024-O004/PublicHolidaysOrder2024SL4of2024.pdf)
        * [Public Holidays Order, 2025](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0015/PublicHolidaysOrder2025_SL%2015%20of%202025.pdf)
        * [2021](https://www.gov.ky/news/press-release-details/public-holidays-for-2021)
        * [2022](https://www.gov.ky/news/press-release-details/public-holidays-2022)
        * [2025](https://www.gov.ky/calendar/public-holidays)
    """

    country = "KY"
    default_language = "en_GB"
    # %s observed.
    observed_label = tr("%s (observed)")
    # Public Holidays Law (2007 Revision).
    start_year = 2008
    supported_languages = ("en_GB", "en_US")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=CaymanIslandsStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # National Heroes Day.
        self._add_holiday_4th_mon_of_jan(tr("National Heroes Day"))

        # Ash Wednesday.
        self._add_ash_wednesday(tr("Ash Wednesday"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        general_election_dates = {
            2009: (MAY, 20),
            2017: (MAY, 24),
            2021: (APR, 14),
            2025: (APR, 30),
        }
        if self._year in general_election_dates:
            # General Election Day.
            self._add_holiday(tr("General Election Day"), general_election_dates[self._year])

        if self._year >= 2024:
            # Emancipation Day.
            self._add_holiday_1st_mon_of_may(tr("Emancipation Day"))

        # Discovery Day.
        self._add_holiday_3rd_mon_of_may(tr("Discovery Day"))

        if self._year <= 2022:
            queens_birthday_dates = {
                2008: (JUN, 16),
                2009: (JUN, 15),
                2010: (JUN, 14),
                2011: (JUN, 13),
                2012: (JUN, 18),
                2013: (JUN, 17),
                2014: (JUN, 16),
                2015: (JUN, 15),
                2016: (JUN, 13),
                2017: (JUN, 19),
                2018: (JUN, 11),
                2019: (JUN, 10),
                2020: (JUN, 15),
                2021: (JUN, 14),
                2022: (JUN, 6),
            }
            # Queen's Birthday.
            name = tr("Queen's Birthday")
            self._add_holiday(name, queens_birthday_dates[self._year])

        if self._year >= 2023 and self._year <= 2025:
            kings_birthday_dates = {
                2023: (JUN, 19),
                2024: (JUN, 17),
                2025: (JUN, 23),
            }
            # King's Birthday.
            self._add_holiday(tr("King's Birthday"), kings_birthday_dates[self._year])

        # Constitution Day.
        self._add_holiday_1st_mon_of_jul(tr("Constitution Day"))

        # Remembrance Day.
        self._add_holiday_2nd_mon_of_nov(tr("Remembrance Day"))

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


class KY(CaymanIslands):
    pass


class CYM(CaymanIslands):
    pass


class CaymanIslandsStaticHolidays:
    """Cayman Islands special holidays.

    References:
        * [2009 Cayman Islands Constitution Day](https://web.archive.org/web/20250320152628/https://www.constitutionalcommission.ky/the-cayman-islands-constitution-2009)
        * [UK Royal Wedding](https://en.wikipedia.org/wiki/Wedding_of_Prince_William_and_Catherine_Middleton)
        * [Queen Elizabeth II's Diamond Jubilee](https://web.archive.org/web/20250708170324/https://calendarific.com/holiday/cayman-islands/queen-diamond-jubilee)
        * [Queen Elizabeth II's Funeral](https://www.gov.ky/queen-elizabeth-ii/faqs)
        * [King Charles III's Coronation](https://web.archive.org/web/20250601214328/https://www.radiocayman.gov.ky/news/public-holidays-for-2023-unconfirmed)
    """

    special_public_holidays = {
        # 2009 Cayman Islands Constitution Day.
        2009: (NOV, 6, tr("2009 Cayman Islands Constitution Day")),
        # UK Royal Wedding.
        2011: (APR, 29, tr("UK Royal Wedding")),
        # Queen Elizabeth II's Diamond Jubilee.
        2012: (JUN, 4, tr("Queen Elizabeth II's Diamond Jubilee")),
        # Queen Elizabeth II's Funeral.
        2022: (SEP, 19, tr("Queen Elizabeth II's Funeral")),
        # King Charles III's Coronation.
        2023: (MAY, 8, tr("Coronation of His Majesty King Charles III")),
    }
