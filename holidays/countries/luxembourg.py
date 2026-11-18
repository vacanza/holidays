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

from holidays.calendars.gregorian import (
    APR,
    JUL,
    SEP,
    OCT,
    DEC,
    SAT,
    _get_nth_weekday_from,
    _timedelta,
)
from holidays.constants import BANK, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Luxembourg(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Luxembourg holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Luxembourg>
        * <https://web.archive.org/web/20250625132138/https://www.bcl.lu/en/About/Opening-days/index.html>
        * School holidays:
            * [Règlement grand-ducal du 31 juillet 1980](https://web.archive.org/web/20260406050409/https://legilux.public.lu/eli/etat/leg/rgd/1980/07/31/n1/jo)
            * [Règlement grand-ducal du 18 novembre 2015](https://legilux.public.lu/eli/etat/leg/rgd/2015/11/18/n1/jo)
            * [Règlement grand-ducal du 18 juillet 2025](https://legilux.public.lu/eli/etat/leg/rgd/2025/07/18/a330/jo)
            * [Règlement grand-ducal du 3 juin 2026](https://legilux.public.lu/eli/etat/leg/rgd/2026/06/03/a281/jo)
            * [Vacances et congés scolaires](https://web.archive.org/web/20260325100918/https://men.public.lu/fr/vacances-scolaires.html)

    School holidays are available from the 1980/81 school year.
    """

    country = "LU"
    default_language = "lb"
    supported_categories = (BANK, PUBLIC, SCHOOL)
    supported_languages = ("de", "en_US", "fr", "lb", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_school_break(self, start_date: date, duration_days: int, *, name: str) -> set[date]:
        """Add a multi-day school break starting from `start_date` (inclusive)."""
        return self._add_multiday_holiday(
            _timedelta(start_date, -1), duration_days=duration_days, name=name
        )

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Neijoerschdag"))

        # Easter Monday.
        self._add_easter_monday(tr("Ouschterméindeg"))

        # Labor Day.
        self._add_labor_day(tr("Dag vun der Aarbecht"))

        if self._year >= 2019:
            # Europe Day.
            self._add_europe_day(tr("Europadag"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Christi Himmelfaart"))

        # Pentecost Monday.
        self._add_pentecost_monday(tr("Péngschtméindeg"))

        # National Day.
        self._add_holiday_jun_23(tr("Nationalfeierdag"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Léiffrawëschdag"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerhellgen"))

        # Christmas Day.
        self._add_christmas_day(tr("Chrëschtdag"))

        # Saint Stephen's Day.
        self._add_christmas_day_two(tr("Stiefesdag"))

    def _populate_bank_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Karfreideg"))

        # Christmas Eve (afternoon).
        self._add_christmas_eve(tr("Hellegowend (nomëtteg)"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Silvester"))

    def _populate_school_holidays(self):
        if not 1980 <= self._year <= 2029:
            return None

        # Christmas Break.
        christmas_break_name = tr("Chrëschtvakanz")
        christmas_overrides = {
            1983: (0, 16),
            1988: (-6, 16),
            1999: (6, 17),
            2011: (-7, 16),
            2017: (-7, 17),
            2028: (-7, 16),
        }

        # Saturday (Sunday in 1980-1982 and 1984-1992) on or before Dec 24 → 2 weeks.
        for year in (self._year - 1, self._year):
            if 1980 <= year <= 2028:
                is_sun_christmas = year <= 1992
                start_offset, duration = christmas_overrides.get(
                    year, (int(is_sun_christmas), 16 - is_sun_christmas)
                )
                self._add_school_break(
                    _timedelta(_get_nth_weekday_from(-1, SAT, date(year, DEC, 24)), start_offset),
                    duration,
                    name=christmas_break_name,
                )

        if self._year <= 2028:
            # 1 week around All Saints' Day (Nov 1).
            all_saints_sat = _get_nth_weekday_from(
                -1,
                SAT,
                _timedelta(date(self._year, OCT, 31), int(self._year in {1986, 2008, 2025})),
            )
            sun_offset = int(self._year <= 1999 and self._year != 1986)
            self._add_school_break(
                _timedelta(all_saints_sat, sun_offset),
                9 - sun_offset,
                # All Saints' Break.
                name=tr("Allerhellegevakanz"),
            )

        if self._year == 1980:
            return None

        easter_sunday = self._easter_sunday

        # Quinquagesima Sunday (1981-1989) or the Saturday before it (from 1990) → 1 week,
        # shifted 1-2 weeks earlier when Easter falls in mid/late April so the break stays
        # in February.
        carnival_overrides = {
            1984: (-56, 9),
            2000: (-57, 10),
            2003: (-64, 9),
            2011: (-64, 9),
            2014: (-64, 9),
        }
        is_sun_carnival = self._year <= 1989
        carnival_weeks_earlier = int(
            self._year >= 2017 and easter_sunday >= date(self._year, APR, 9)
        ) + int(self._year >= 2018 and easter_sunday >= date(self._year, APR, 16))
        carnival_offset, carnival_duration = carnival_overrides.get(
            self._year,
            (-50 - 7 * carnival_weeks_earlier + is_sun_carnival, 9 - is_sun_carnival),
        )
        self._add_school_break(
            _timedelta(easter_sunday, carnival_offset),
            carnival_duration,
            # Carnival Break.
            name=tr("Fuesvakanz"),
        )

        # 2 weeks around Easter (Sunday-to-Sunday in 1981-1995, Saturday-to-Sunday from 1996,
        # extended through Easter Monday when starting 2 weeks before Easter prior to 2025).
        easter_overrides = {
            1984: (-7, 17),
            1986: (0, 15),
            1988: (0, 15),
            1989: (0, 15),
            1991: (0, 15),
            1992: (-14, 16),
            2000: (-15, 17),
            2002: (-8, 16),
            2003: (-15, 17),
            2013: (-8, 16),
            2015: (-1, 16),
            2017: (-8, 16),
            2021: (-1, 16),
        }
        is_sun_easter = self._year <= 1995
        easter_weeks_earlier = int(
            self._year >= 2001 and easter_sunday >= date(self._year, APR, 4)
        ) + int(self._year >= 2011 and easter_sunday >= date(self._year, APR, 16))
        easter_offset, easter_duration = easter_overrides.get(
            self._year,
            (
                -1 - 7 * easter_weeks_earlier - 6 * is_sun_easter,
                16 - is_sun_easter + int(easter_weeks_earlier == 2 and self._year <= 2024),
            ),
        )
        self._add_school_break(
            _timedelta(easter_sunday, easter_offset),
            easter_duration,
            # Easter Break.
            name=tr("Ouschtervakanz"),
        )

        # 1 week starting on Pentecost (1981-1996) or the Saturday before it (from 1997),
        # shifted to the last full week of May when Easter is very early or very late.
        pentecost_overrides = {
            1984: (42, 10),
            1992: (42, 10),
            1995: (42, 10),
            2000: (41, 11),
            2009: (41, 11),
            2013: (55, 9),
            2014: (48, 9),
            2024: (55, 9),
            2027: (62, 9),
            2028: (41, 9),
        }
        is_sun_pentecost = self._year <= 1996
        is_early_pentecost = self._year >= 2003 and easter_sunday >= date(self._year, APR, 17)
        pentecost_offset, pentecost_duration = pentecost_overrides.get(
            self._year,
            (
                +48 - 14 * is_early_pentecost + is_sun_pentecost,
                9 - is_sun_pentecost,
            ),
        )
        self._add_school_break(
            _timedelta(easter_sunday, pentecost_offset),
            pentecost_duration,
            # Pentecost Break.
            name=tr("Päischtvakanz"),
        )

        # Jul 16 (or the preceding weekend in some years) → Sep 14 (or the following Sunday).
        summer_overrides = {
            1985: (16, 15),
            1990: (15, 16),
            1991: (14, 15),
            1996: (14, 15),
            1997: (13, 14),
            1998: (12, 13),
            2001: (15, 16),
            2002: (14, 15),
            2018: (14, 16),
            2019: (13, 15),
            2024: (16, 15),
            2029: (14, 16),
        }
        is_jul_16_sun = self._year >= 2006 and self._is_sunday(date(self._year, JUL, 16))
        start_day, end_day = summer_overrides.get(self._year, (16 - is_jul_16_sun, 14))
        summer_start = date(self._year, JUL, start_day)
        summer_end = date(self._year, SEP, end_day)
        self._add_school_break(
            summer_start,
            (summer_end - summer_start).days + 1,
            # Summer Break.
            name=tr("Summervakanz"),
        )


class LU(Luxembourg):
    pass


class LUX(Luxembourg):
    pass
