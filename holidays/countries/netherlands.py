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

from holidays.calendars.gregorian import JAN, DEC, SAT, _timedelta, _get_nth_weekday_from
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
        * School holidays:
            * [Regeling vaststelling schoolvakanties 2013-2016](https://web.archive.org/web/20261022045936/https://zoek.officielebekendmakingen.nl/stcrt-2012-27185.html)
            * [Regeling vaststelling schoolvakanties 2016-2019](https://web.archive.org/web/20261022050344/https://zoek.officielebekendmakingen.nl/stcrt-2015-35695.html)
            * [Regeling vaststelling schoolvakanties 2019-2022](https://web.archive.org/web/20261022050408/https://zoek.officielebekendmakingen.nl/stcrt-2018-11687.html)
            * [Regeling vaststelling schoolvakanties 2022-2025](https://web.archive.org/web/20261022050433/https://zoek.officielebekendmakingen.nl/stcrt-2021-25317.html)
            * [Regeling vaststelling schoolvakanties 2025-2030](https://web.archive.org/web/20261022050453/https://zoek.officielebekendmakingen.nl/stcrt-2024-19237.html)
            * [Vaststellen data schoolvakanties](https://www.rijksoverheid.nl/themas/onderwijs/schoolvakanties/vaststellen-data-schoolvakanties)
            * [Regio-indeling](https://web.archive.org/web/20261012093116/https://www.rijksoverheid.nl/themas/onderwijs/schoolvakanties/regios-schoolvakantie)

    Subdivisions are the three regions the Ministry of Education spreads the `SCHOOL` holidays
    over. The Christmas, May and Summer Breaks are binding; the Autumn and Spring Breaks are
    advisory dates schools may depart from. Every break runs from the Saturday before its first
    ISO week through the Sunday that ends its last one.
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

    # Order of the per-region ISO weeks in the school holiday tables below.
    school_regions = ("Noord", "Midden", "Zuid")

    # Advisory Autumn Break week per region.
    autumn_break_weeks = {
        2014: (42, 43, 43),
        2015: (43, 43, 44),
        2016: (42, 42, 43),
        2017: (43, 42, 42),
        2018: (43, 43, 42),
        2019: (43, 43, 42),
        2020: (42, 43, 43),
        2021: (42, 42, 43),
        2022: (42, 43, 43),
        2023: (43, 42, 42),
        2024: (44, 44, 43),
        2025: (43, 43, 42),
        2026: (42, 43, 43),
        2027: (42, 42, 43),
        2028: (42, 43, 43),
        2029: (43, 43, 42),
    }

    # Advisory Spring Break week per region.
    spring_break_weeks = {
        2014: (9, 8, 8),
        2015: (9, 9, 8),
        2016: (9, 8, 8),
        2017: (8, 9, 9),
        2018: (9, 9, 8),
        2019: (8, 9, 9),
        2020: (8, 9, 9),
        2021: (8, 8, 7),
        2022: (8, 9, 9),
        2023: (9, 9, 8),
        2024: (8, 8, 7),
        2025: (8, 9, 9),
        2026: (9, 8, 8),
        2027: (8, 8, 7),
        2028: (8, 9, 9),
        2029: (8, 8, 7),
        2030: (8, 9, 9),
    }

    # May Break week, when not week 18.
    may_break_weeks = {
        2015: 19,
        2017: 17,
        2027: 17,
    }

    # Summer Break week per region: the regions take turns starting in weeks 28, 29 and 30,
    # each being the first or the last two years in a row, in a 6-year cycle (from 2015).
    summer_break_weeks = (
        (28, 29, 30),
        (29, 28, 30),
        (30, 28, 29),
        (30, 29, 28),
        (29, 30, 28),
        (28, 30, 29),
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _add_multiday_holiday(
        self, start_date: date, duration_days: int, *, name: str | None = None
    ) -> set[date]:
        """Add a multi-day holiday starting from `start_date` (inclusive)."""
        return super()._add_multiday_holiday(
            _timedelta(start_date, -1), duration_days=duration_days, name=name
        )

    def _add_school_break(self, name: str, week: int, weeks: int = 1) -> None:
        """Add a school break of `weeks` ISO weeks starting the Saturday before `week`."""
        self._add_multiday_holiday(
            _timedelta(date.fromisocalendar(self._year, week, 1), -2), 7 * weeks + 2, name=name
        )

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
        if self.subdiv is None or self._year <= 2013:
            return None

        region = self.school_regions.index(self._normalized_subdiv)

        # Christmas Break.
        name = tr("Kerstvakantie")
        # Saturday on or before Dec 25 → 2 weeks.
        self._add_multiday_holiday(
            _get_nth_weekday_from(-1, SAT, self._christmas_day), 16, name=name
        )
        # January part of the previous year's break.
        previous_start = _get_nth_weekday_from(-1, SAT, date(self._year - 1, DEC, 25))
        self._add_multiday_holiday(
            date(self._year, JAN, 1), _timedelta(previous_start, +15).day, name=name
        )

        if weeks := self.spring_break_weeks.get(self._year):
            # Spring Break.
            self._add_school_break(tr("Voorjaarsvakantie"), weeks[region])

        # May Break.
        name = tr("Meivakantie")
        self._add_school_break(name, self.may_break_weeks.get(self._year, 18))
        if self._year == 2014:
            # Extended through Liberation Day.
            self._add_holiday_may_5(name)

        # Summer Break.
        name = tr("Zomervakantie")
        self._add_school_break(name, self.summer_break_weeks[(self._year - 2015) % 6][region], 6)

        if weeks := self.autumn_break_weeks.get(self._year):
            # Autumn Break.
            self._add_school_break(tr("Herfstvakantie"), weeks[region])


class NL(Netherlands):
    pass


class NLD(Netherlands):
    pass
