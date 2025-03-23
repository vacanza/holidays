#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.calendars import _CustomHinduHolidays, _CustomIslamicHolidays
from holidays.calendars.gregorian import SEP, OCT, NOV
from holidays.constants import PUBLIC, WORKDAY
from holidays.groups import (
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    ALL_TO_NEAREST_MON,
)


class Fiji(
    ObservedHolidayBase,
    HinduCalendarHolidays,
    InternationalHolidays,
    ChristianHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    """
    References:
    - https://laws.gov.fj/Acts/DisplayAct/2910#
    - https://laws.gov.fj/LawsAsMade
    - https://www.fiji.gov.fj/About-Fiji/Public-Holidays
    - https://www.timeanddate.com/holidays/fiji/
    - https://en.wikipedia.org/wiki/List_of_festivals_in_Fiji
    - https://www.rnz.co.nz/international/pacific-news/249514/new-public-holiday-for-fiji
    - https://www.fijitimes.com.fj/constitution-day-public-holiday-removed-cabinet/
    - https://fijivillage.com/news/National-Sports-Day-celebrated-5krs29/
    - https://fijivillage.com/news/Cabinet-approves-Ratu-Sir-Lala-Sukuna-Day-and-Girmit-Day-and-removes-Constitution-Day-as-a-public-holiday-f48r5x/
    """

    country = "FJ"
    supported_categories = (PUBLIC, WORKDAY)
    # %s (estimated).
    estimated_label = "%s (estimated)"
    # %s (observed).
    observed_label = "%s (observed)"
    # %s (observed, estimated).
    observed_estimated_label = "%s (observed, estimated)"
    # Act No. 13 of 2015
    start_year = 2016

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self, cls=FijiHinduHolidays, show_estimated=True)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=FijiIslamicHolidays, show_estimated=True)
        StaticHolidays.__init__(self, FijiStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # National Sports Day.
        if self._year <= 2018:
            self._add_holiday_last_fri_of_jun("National Sports Day")

        if self._year <= 2022:
            # Constitution Day.
            self._add_observed(self._add_holiday_sep_7("Constitution Day"))

        if self._year >= 2023:
            # Girmit Day.
            self._move_holiday(
                self._add_holiday_may_14("Girmit Day"),
                rule=ALL_TO_NEAREST_MON,
                show_observed_label=False,
            )

        # Ratu Sir Lala Sukuna Day.
        name = "Ratu Sir Lala Sukuna Day"
        if self._year == 2023:
            self._add_holiday_last_mon_of_may(name)
        elif self._year >= 2024:
            self._add_holiday_last_fri_of_may(name)

        # Fiji Day.
        self._add_holiday_oct_10("Fiji Day")

        # Prophet Mohammed's Birthday
        self._populate_observed(self._add_mawlid_day("Prophet Mohammed's Birthday"))

        # Diwali
        self._add_observed(self._add_diwali_india("Diwali"))

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

    def _populate_workday_holidays(self):
        if self._year >= 2023:
            # Constitution Day.
            self._add_holiday_sep_7("Constitution Day")


class FJ(Fiji):
    pass


class FJI(Fiji):
    pass


class FijiHinduHolidays(_CustomHinduHolidays):
    # https://www.timeanddate.com/holidays/fiji/diwali
    DIWALI_INDIA_DATES = {
        2016: (OCT, 31),
        2017: (OCT, 19),
        2018: (NOV, 7),
        2019: (OCT, 28),
        2020: (NOV, 14),
        2021: (NOV, 4),
        2022: (OCT, 25),
        2023: (NOV, 13),
        2024: (NOV, 1),
        2025: (OCT, 21),
    }


class FijiIslamicHolidays(_CustomIslamicHolidays):
    MAWLID_DATES = {
        2019: (NOV, 11),
        2020: (NOV, 2),
        2021: (OCT, 18),
        2022: (OCT, 7),
        2023: (OCT, 2),
        2024: (SEP, 16),
        2025: (SEP, 8),
    }


class FijiStaticHolidays:
    """
    Official Fiji Public Holidays Calendar:
    - `2016 <https://www.fiji.gov.fj/Media-Center/Press-Releases/GOVERNMENT-APPROVES-2016-PUBLIC-HOLIDAYS.aspx>`_
    - `2017 <https://www.fiji.gov.fj/Media-Centre/News/GOVERNMENT-APPROVES-2017-PUBLIC-HOLIDAYS>`_
    - `2018 <https://web.archive.org/web/20180727205733/http://www.employment.gov.fj/images/Laws/Press%20Release%20-%20Government%20Approves%202018%20Public%20Holidays.pdf>`_
    - `2019 <https://web.archive.org/web/20191018023027/https://www.fiji.gov.fj/About-Fiji/Public-Holidays>`_
    - `2020 <https://web.archive.org/web/20210103183942/https://www.fiji.gov.fj/About-Fiji/Public-Holidays>`_
    - `2021-2022 <https://web.archive.org/web/20221223004409/https://www.fiji.gov.fj/About-Fiji/Public-Holidays>`_
    - `2023 <https://web.archive.org/web/20231129154609/https://www.fiji.gov.fj/About-Fiji/Public-Holidays>`_
    -` 2024 <https://web.archive.org/web/20250121185434/https://www.fiji.gov.fj/About-Fiji/Public-Holidays>`_
    - `2025 <https://web.archive.org/web/20250318092311/https://www.fiji.gov.fj/About-Fiji/Public-Holidays>`_
    """

    special_public_holidays_observed = {
        # Constitution Day.
        2019: (SEP, 9, "Constitution Day"),
    }
