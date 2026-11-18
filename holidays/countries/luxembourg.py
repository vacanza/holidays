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
    NOV,
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

    def _add_multiday_holiday(
        self, start_date: date, duration_days: int, *, name: str | None = None
    ) -> set[date]:
        """Add a multi-day holiday starting from `start_date` (inclusive)."""
        return super()._add_multiday_holiday(
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

        # Saturday (Sunday in 1980-1982 and 1984-1992) on or before Dec 24 → 2 weeks
        # (starts 1 week earlier in 1988, 2011, 2017, and 2028; starts on Dec 24 in 1999).
        for year in (self._year - 1, self._year):
            if 1980 <= year <= 2028:
                if year == 1999:
                    start, duration = date(year, DEC, 24), 17
                else:
                    sat = _get_nth_weekday_from(-1, SAT, date(year, DEC, 24))
                    if year in {1988, 2011, 2017, 2028}:
                        sat = _timedelta(sat, -7)
                    is_sun_start = year <= 1992 and year != 1983
                    start = _timedelta(sat, +1) if is_sun_start else sat
                    duration = (
                        (16 if is_sun_start else 17)
                        if year in {1988, 2017}
                        else (15 if is_sun_start else 16)
                    )
                self._add_multiday_holiday(start, duration, name=christmas_break_name)

        if self._year >= 1981:
            easter_sunday = self._easter_sunday

            # Quinquagesima Sunday (1981-1989) or the Saturday before it (from 1990) → 1 week,
            # shifted 1-2 weeks earlier when Easter falls in mid/late April so the break stays
            # in February.
            carnival_offsets = {1984: -56, 2000: -57, 2006: -50, 2017: -57}
            if self._year in carnival_offsets:
                carnival_offset = carnival_offsets[self._year]
            elif self._year <= 1989:
                carnival_offset = -49
            elif self._year >= 2003 and easter_sunday >= date(self._year, APR, 16):
                carnival_offset = -64
            elif self._year >= 2017 and easter_sunday >= date(self._year, APR, 9):
                carnival_offset = -57
            else:
                carnival_offset = -50
            self._add_multiday_holiday(
                _timedelta(easter_sunday, carnival_offset),
                10
                if self._year == 2000
                else (8 if self._year <= 1989 and self._year != 1984 else 9),
                # Carnival Break.
                name=tr("Fuesvakanz"),
            )

            # 2 weeks around Easter (Sunday-to-Sunday in 1981-1995, Saturday-to-Sunday from 1996,
            # extended through Easter Monday when starting 2 weeks before Easter prior to 2025).
            if self._year == 1992:
                easter_offset, easter_duration = -14, 16
            elif self._year <= 1995:
                easter_offset = 0 if self._year in {1986, 1988, 1989, 1991} else -7
                easter_duration = 17 if self._year == 1984 else 15
            elif (
                easter_sunday >= date(self._year, APR, 16)
                and self._year != 2017
                and (self._year >= 2011 or self._year in {2000, 2003})
            ):
                easter_offset = -15
                easter_duration = 16 if self._year >= 2025 else 17
            elif (
                self._year >= 2001
                and easter_sunday >= date(self._year, APR, 4)
                and self._year not in {2015, 2021}
            ) or self._year in {2002, 2013}:
                easter_offset, easter_duration = -8, 16
            else:
                easter_offset, easter_duration = -1, 16
            self._add_multiday_holiday(
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
            if self._year in pentecost_overrides:
                pentecost_offset, pentecost_duration = pentecost_overrides[self._year]
            elif self._year <= 1996:
                pentecost_offset, pentecost_duration = +49, 8
            elif self._year >= 2003 and easter_sunday >= date(self._year, APR, 17):
                pentecost_offset, pentecost_duration = +34, 9
            else:
                pentecost_offset, pentecost_duration = +48, 9
            self._add_multiday_holiday(
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
            if self._year in summer_overrides:
                start_day, end_day = summer_overrides[self._year]
                summer_start = date(self._year, JUL, start_day)
                summer_end = date(self._year, SEP, end_day)
            else:
                summer_start = date(
                    self._year,
                    JUL,
                    15
                    if self._year >= 2006 and self._is_sunday(date(self._year, JUL, 16))
                    else 16,
                )
                summer_end = date(self._year, SEP, 14)
            self._add_multiday_holiday(
                summer_start,
                (summer_end - summer_start).days + 1,
                # Summer Break.
                name=tr("Summervakanz"),
            )

        if self._year <= 2028:
            # 1 week around All Saints' Day (Nov 1).
            all_saints_sat = (
                date(self._year, NOV, 1)
                if self._year in {1986, 2008, 2025}
                else _get_nth_weekday_from(-1, SAT, date(self._year, OCT, 31))
            )
            is_sun_all_saints = self._year <= 1999 and self._year != 1986
            self._add_multiday_holiday(
                _timedelta(all_saints_sat, +1) if is_sun_all_saints else all_saints_sat,
                8 if is_sun_all_saints else 9,
                # All Saints' Break.
                name=tr("Allerhellegevakanz"),
            )


class LU(Luxembourg):
    pass


class LUX(Luxembourg):
    pass
