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

from datetime import date

from holidays.calendars.gregorian import _timedelta
from holidays.calendars.netherlands_school import (
    AUTUMN_BREAK,
    CHRISTMAS_BREAK,
    SPRING_BREAK,
    MAY_BREAK,
    SUMMER_BREAK,
    NETHERLANDS_SCHOOL_HOLIDAYS,
)
from holidays.constants import OPTIONAL, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_PREV_SAT, SUN_TO_NEXT_MON


class Netherlands(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Netherlands holidays.

    Easter Sunday and Whit Sunday are always on Sunday and are therefore not mentioned separately
    in the Algemene termijnenwet (Atw).

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Netherlands>
        * <https://nl.wikipedia.org/wiki/Feestdagen_in_Nederland>
        * <https://nl.wikipedia.org/wiki/Algemene_termijnenwet>
        * <https://web.archive.org/web/20251015082530/https://business.gov.nl/regulation/holiday-entitlement/>
        * <https://web.archive.org/save/https://wetten.overheid.nl/BWBR0002448/2010-10-10>
        * <https://web.archive.org/web/20250123145153/https://repository.overheid.nl/frbr/sgd/19811982/0000151909/1/pdf/SGD_19811982_0002862.pdf>
        * <https://web.archive.org/web/20251015082056/https://www.facebook.com/photo.php?fbid=5357926707591435&id=190259871024837&set=a.342400825810740>

    Dutch school holidays are subdivision-specific. The subdivisions are the three regions
    the Ministry of Education spreads the holidays over, not provinces: the official split
    cuts through Gelderland, leaves Zeewolde out of Noord and Woudrichem out of Zuid.
    See [`netherlands_school`][holidays.calendars.netherlands_school] for the dataset.
    """

    country = "NL"
    default_language = "nl"
    subdivisions = (
        "Midden",  # Central region.
        "Noord",  # Northern region.
        "Zuid",  # Southern region.
    )
    supported_categories = (OPTIONAL, PUBLIC, SCHOOL)
    supported_languages = ("en_US", "fy", "nl", "th", "uk")
    # Algemene termijnenwet (Atw) entered into force on April 1st, 1965.
    start_year = 1966

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    @staticmethod
    def _get_school_holiday_names() -> dict[int, str]:
        return {
            # Autumn Break.
            AUTUMN_BREAK: tr("Herfstvakantie"),
            # Christmas Break.
            CHRISTMAS_BREAK: tr("Kerstvakantie"),
            # Spring Break.
            SPRING_BREAK: tr("Voorjaarsvakantie"),
            # May Break.
            MAY_BREAK: tr("Meivakantie"),
            # Summer Break.
            SUMMER_BREAK: tr("Zomervakantie"),
        }

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nieuwjaarsdag"))

        # Good Friday.
        self._add_good_friday(tr("Goede vrijdag"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Eerste paasdag"))

        # Easter Monday.
        self._add_easter_monday(tr("Tweede paasdag"))

        self._move_holiday(
            # King's Day.
            self._add_holiday_apr_27(tr("Koningsdag"))
            if self._year >= 2014
            # Queen's Day.
            else self._add_holiday_apr_30(tr("Koninginnedag")),
            rule=SUN_TO_PREV_SAT if self._year >= 1980 else SUN_TO_NEXT_MON,
        )

        # Officially adopted as an annual national holiday in the Atw on January 5th, 1982.
        # In practice, many collective labor agreements (CAOs) stipulate that May 5th is
        # a day off only once every five years (e.g., 2030, 2035, etc.).
        if self._year % 5 == 0:
            # Liberation Day.
            self._add_holiday_may_5(tr("Bevrijdingsdag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Hemelvaartsdag"))

        # Pentecost.
        self._add_pentecost(tr("Eerste pinksterdag"))

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Tweede pinksterdag"))

        # Christmas Day.
        self._add_christmas_day(tr("Eerste kerstdag"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Tweede kerstdag"))

    def _populate_optional_holidays(self):
        if self._year >= 1982:
            # Liberation Day.
            self._add_holiday_may_5(tr("Bevrijdingsdag"))

    def _populate_school_holidays(self):
        if self.subdiv is None:
            return None

        school_holiday_names = self._get_school_holiday_names()
        for (
            start_year_offset,
            start_month,
            start_day,
            end_year_offset,
            end_month,
            end_day,
            holiday_id,
        ) in NETHERLANDS_SCHOOL_HOLIDAYS.get(self._year, {}).get(self._normalized_subdiv, ()):
            start_date = date(self._year + start_year_offset, start_month, start_day)
            end_date = date(self._year + end_year_offset, end_month, end_day)
            # The anchor is the day before the break, as the days are counted from the one
            # after it. A break spanning New Year is listed under both years; the dates
            # outside the year being populated are dropped on add.
            self._add_multiday_holiday(
                _timedelta(start_date, -1),
                (end_date - start_date).days + 1,
                name=school_holiday_names[holiday_id],
            )


class NL(Netherlands):
    pass


class NLD(Netherlands):
    pass
