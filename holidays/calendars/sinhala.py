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

from collections.abc import Iterable
from datetime import date, datetime, timedelta, timezone
from functools import cache
import math

from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.helpers import _normalize_tuple

BAK_POYA = "BAK_POYA"
BINARA_POYA = "BINARA_POYA"
DURUTHU_POYA = "DURUTHU_POYA"
ESALA_POYA = "ESALA_POYA"
IL_POYA = "IL_POYA"
MEDIN_POYA = "MEDIN_POYA"
NAWAM_POYA = "NAWAM_POYA"
NIKINI_POYA = "NIKINI_POYA"
POSON_POYA = "POSON_POYA"
UNDUVAP_POYA = "UNDUVAP_POYA"
VAP_POYA = "VAP_POYA"
VESAK_POYA = "VESAK_POYA"


def _full_moon_jde(k: float) -> float:
    """Calculate the Julian Ephemeris Day (JDE) of a Full Moon phase (Meeus Chapter 49)."""
    t = k / 1236.85
    t2 = t * t
    t3 = t2 * t
    t4 = t3 * t

    jde = (
        2451550.09766 + 29.530588861 * k + 0.00015437 * t2 - 0.000000150 * t3 + 0.00000000073 * t4
    )

    e = 1.0 - 0.002516 * t - 0.0000074 * t2

    m = math.radians(2.5534 + 29.10535670 * k - 0.0000014 * t2 - 0.00000011 * t3)
    mprime = math.radians(
        201.5643 + 385.81693528 * k + 0.0107538 * t2 + 0.00001238 * t3 - 0.000000058 * t4
    )
    f = math.radians(
        160.7108 + 390.67050284 * k - 0.0016118 * t2 - 0.00000227 * t3 + 0.0000011 * t4
    )
    omega = math.radians(124.97 - 1.9337 * k + 0.00206 * t2 + 0.00000215 * t3)

    # Periodic corrections for Full Moon (Meeus Table 49.B)
    corr = (
        -0.40614 * math.sin(mprime)
        + 0.17302 * e * math.sin(m)
        + 0.01614 * math.sin(2 * mprime)
        + 0.01043 * math.sin(2 * f)
        - 0.00734 * e * math.sin(mprime - m)
        - 0.00515 * e * math.sin(mprime + m)
        + 0.00209 * e * e * math.sin(2 * m)
        - 0.00111 * math.sin(mprime - 2 * f)
        - 0.00057 * math.sin(mprime + 2 * f)
        + 0.00056 * e * math.sin(2 * mprime + m)
        - 0.00042 * math.sin(3 * mprime)
        + 0.00042 * e * math.sin(m + 2 * f)
        + 0.00038 * e * math.sin(m - 2 * f)
        - 0.00024 * e * math.sin(2 * mprime - m)
        - 0.00017 * math.sin(omega)
        - 0.00007 * math.sin(mprime + 2 * m)
        + 0.00004 * math.sin(2 * mprime - 2 * f)
        + 0.00004 * math.sin(3 * m)
        + 0.00003 * math.sin(mprime + m - 2 * f)
        + 0.00003 * math.sin(2 * mprime + 2 * f)
        - 0.00003 * math.sin(mprime + m + 2 * f)
        + 0.00003 * math.sin(mprime - m + 2 * f)
        - 0.00002 * math.sin(mprime - m - 2 * f)
        - 0.00002 * math.sin(3 * mprime + m)
        + 0.00002 * math.sin(4 * mprime)
    )

    # Planetary corrections
    a1 = math.radians(299.77 + 0.107408 * k - 0.009173 * t2)
    a2 = math.radians(251.88 + 0.016321 * k)
    a3 = math.radians(251.83 + 26.651886 * k)
    a4 = math.radians(349.42 + 36.412478 * k)
    a5 = math.radians(84.66 + 18.206239 * k)
    a6 = math.radians(141.74 + 53.303771 * k)
    a7 = math.radians(207.14 + 2.453732 * k)
    a8 = math.radians(154.84 + 7.306860 * k)
    a9 = math.radians(34.52 + 27.261239 * k)
    a10 = math.radians(207.19 + 0.121824 * k)
    a11 = math.radians(291.34 + 1.844379 * k)
    a12 = math.radians(161.72 + 24.198154 * k)
    a13 = math.radians(239.56 + 25.513099 * k)
    a14 = math.radians(331.55 + 3.592518 * k)

    planetary_corr = (
        0.000325 * math.sin(a1)
        + 0.000165 * math.sin(a2)
        + 0.000164 * math.sin(a3)
        + 0.000126 * math.sin(a4)
        + 0.000110 * math.sin(a5)
        + 0.000062 * math.sin(a6)
        + 0.000060 * math.sin(a7)
        + 0.000056 * math.sin(a8)
        + 0.000047 * math.sin(a9)
        + 0.000042 * math.sin(a10)
        + 0.000040 * math.sin(a11)
        + 0.000037 * math.sin(a12)
        + 0.000035 * math.sin(a13)
        + 0.000023 * math.sin(a14)
    )

    t_poly = (jde - 2451545.0) / 365.25
    delta_t = 62.92 + 0.32217 * t_poly + 0.005589 * t_poly * t_poly
    return jde + corr + planetary_corr - (delta_t / 86400.0)


@cache
def _get_slst_full_moons(year: int) -> tuple[date, ...]:
    """Calculate all Full Moon calendar dates for a year in Sri Lanka Standard Time (UTC+5:30)."""
    dt_base = datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    slst_tz = timezone(timedelta(hours=5, minutes=30))
    k_start = int((year - 2000) * 12.3685) - 2
    fms = []
    for k_int in range(k_start, k_start + 18):
        k = k_int + 0.5
        jde_utc = _full_moon_jde(k)
        dt_utc = dt_base + timedelta(days=(jde_utc - 2451545.0))
        dt_slst = dt_utc.astimezone(slst_tz)
        if dt_slst.year == year:
            fms.append(dt_slst.date())
    return tuple(sorted(set(fms)))


POYA_NAMES = (
    DURUTHU_POYA,
    NAWAM_POYA,
    MEDIN_POYA,
    BAK_POYA,
    VESAK_POYA,
    POSON_POYA,
    ESALA_POYA,
    NIKINI_POYA,
    BINARA_POYA,
    VAP_POYA,
    IL_POYA,
    UNDUVAP_POYA,
)


@cache
def _calculate_poya_dates(year: int) -> dict[str, date]:
    """Map Full Moons to the 12 traditional Sinhala Poya days for a future year."""
    fms = list(_get_slst_full_moons(year))
    if len(fms) == 13:
        feb_has_fm = any(d.month == 2 for d in fms)
        extra_idx = None
        for i in range(len(fms) - 1):
            if fms[i].month == fms[i + 1].month:
                if fms[i].month == 1 and not feb_has_fm:
                    continue
                extra_idx = i + 1
                break
        if extra_idx is None:
            extra_idx = len(fms) - 1
        fms.pop(extra_idx)

    return dict(zip(POYA_NAMES, fms))


class _SinhalaLunar:
    """Sinhala Lunar calendar.

    Confirmed Poya dates for 2003-2026 are based on official government gazettes.
    Dates for subsequent years are calculated astronomically based on Full Moon
    instants converted to Sri Lanka Standard Time (UTC+5:30).
    """

    START_YEAR = 2003
    END_YEAR = 2100

    BAK_POYA_DATES = {
        2003: (APR, 16),
        2004: (APR, 5),
        2005: (APR, 23),
        2006: (APR, 13),
        2007: (APR, 2),
        2008: (APR, 19),
        2009: (APR, 9),
        2010: (MAR, 29),
        2011: (APR, 17),
        2012: (APR, 6),
        2013: (APR, 25),
        2014: (APR, 14),
        2015: (APR, 3),
        2016: (APR, 21),
        2017: (APR, 10),
        2018: (MAR, 31),
        2019: (APR, 19),
        2020: (APR, 7),
        2021: (APR, 26),
        2022: (APR, 16),
        2023: (APR, 5),
        2024: (APR, 23),
        2025: (APR, 12),
        2026: (APR, 1),
    }

    BINARA_POYA_DATES = {
        2003: (SEP, 10),
        2004: (SEP, 28),
        2005: (SEP, 17),
        2006: (SEP, 7),
        2007: (SEP, 26),
        2008: (SEP, 14),
        2009: (SEP, 4),
        2010: (SEP, 22),
        2011: (SEP, 11),
        2012: (SEP, 29),
        2013: (SEP, 19),
        2014: (SEP, 8),
        2015: (SEP, 27),
        2016: (SEP, 16),
        2017: (SEP, 5),
        2018: (SEP, 24),
        2019: (SEP, 13),
        2020: (SEP, 1),
        2021: (SEP, 20),
        2022: (SEP, 10),
        2023: (SEP, 29),
        2024: (SEP, 17),
        2025: (SEP, 7),
        2026: (SEP, 26),
    }

    DURUTHU_POYA_DATES = {
        2003: (JAN, 17),
        2004: (JAN, 7),
        2005: (JAN, 24),
        2006: (JAN, 13),
        2007: (JAN, 3),
        2008: (JAN, 22),
        2009: ((JAN, 10), (DEC, 31)),
        2011: (JAN, 19),
        2012: (JAN, 8),
        2013: (JAN, 26),
        2014: (JAN, 15),
        2015: (JAN, 4),
        2016: (JAN, 23),
        2017: (JAN, 12),
        2018: (JAN, 1),
        2019: (JAN, 20),
        2020: (JAN, 10),
        2021: (JAN, 28),
        2022: (JAN, 17),
        2023: (JAN, 6),
        2024: (JAN, 25),
        2025: (JAN, 13),
        2026: (JAN, 3),
    }

    ESALA_POYA_DATES = {
        2003: (JUL, 13),
        2004: (JUL, 2),
        2005: (JUL, 21),
        2006: (JUL, 10),
        2007: (JUL, 29),
        2008: (JUL, 17),
        2009: (JUL, 6),
        2010: (JUL, 25),
        2011: (JUL, 14),
        2012: (JUL, 3),
        2013: (JUL, 22),
        2014: (JUL, 12),
        2015: (JUL, 31),
        2016: (JUL, 19),
        2017: (JUL, 8),
        2018: (JUL, 27),
        2019: (JUL, 16),
        2020: (JUL, 4),
        2021: (JUL, 23),
        2022: (JUL, 13),
        2023: (AUG, 1),
        2024: (JUL, 20),
        2025: (JUL, 10),
        2026: (JUL, 29),
    }

    IL_POYA_DATES = {
        2003: (NOV, 8),
        2004: (NOV, 26),
        2005: (NOV, 15),
        2006: (NOV, 5),
        2007: (NOV, 24),
        2008: (NOV, 12),
        2009: (NOV, 2),
        2010: (NOV, 21),
        2011: (NOV, 10),
        2012: (NOV, 27),
        2013: (NOV, 17),
        2014: (NOV, 6),
        2015: (NOV, 25),
        2016: (NOV, 14),
        2017: (NOV, 3),
        2018: (NOV, 22),
        2019: (NOV, 12),
        2020: (NOV, 29),
        2021: (NOV, 18),
        2022: (NOV, 7),
        2023: (NOV, 26),
        2024: (NOV, 15),
        2025: (NOV, 5),
        2026: (NOV, 24),
    }

    MEDIN_POYA_DATES = {
        2003: (MAR, 18),
        2004: (MAR, 6),
        2005: (MAR, 25),
        2006: (MAR, 14),
        2007: (MAR, 3),
        2008: (MAR, 21),
        2009: (MAR, 10),
        2010: (FEB, 28),
        2011: (MAR, 19),
        2012: (MAR, 7),
        2013: (MAR, 26),
        2014: (MAR, 16),
        2015: (MAR, 5),
        2016: (MAR, 22),
        2017: (MAR, 12),
        2018: (MAR, 1),
        2019: (MAR, 20),
        2020: (MAR, 9),
        2021: (MAR, 28),
        2022: (MAR, 17),
        2023: (MAR, 6),
        2024: (MAR, 24),
        2025: (MAR, 13),
        2026: (MAR, 2),
    }

    NAWAM_POYA_DATES = {
        2003: (FEB, 16),
        2004: (FEB, 5),
        2005: (FEB, 23),
        2006: (FEB, 12),
        2007: (FEB, 1),
        2008: (FEB, 20),
        2009: (FEB, 9),
        2010: (JAN, 29),
        2011: (FEB, 17),
        2012: (FEB, 7),
        2013: (FEB, 25),
        2014: (FEB, 14),
        2015: (FEB, 3),
        2016: (FEB, 22),
        2017: (FEB, 10),
        2018: (JAN, 31),
        2019: (FEB, 19),
        2020: (FEB, 8),
        2021: (FEB, 26),
        2022: (FEB, 16),
        2023: (FEB, 5),
        2024: (FEB, 23),
        2025: (FEB, 12),
        2026: (FEB, 1),
    }

    NIKINI_POYA_DATES = {
        2003: (AUG, 11),
        2004: (AUG, 29),
        2005: (AUG, 19),
        2006: (AUG, 9),
        2007: (AUG, 28),
        2008: (AUG, 16),
        2009: (AUG, 5),
        2010: (AUG, 24),
        2011: (AUG, 13),
        2012: (AUG, 1),
        2013: (AUG, 20),
        2014: (AUG, 10),
        2015: (AUG, 29),
        2016: (AUG, 17),
        2017: (AUG, 7),
        2018: (AUG, 25),
        2019: (AUG, 14),
        2020: (AUG, 3),
        2021: (AUG, 22),
        2022: (AUG, 11),
        2023: (AUG, 30),
        2024: (AUG, 19),
        2025: (AUG, 8),
        2026: (AUG, 27),
    }

    POSON_POYA_DATES = {
        2003: (JUN, 14),
        2004: (JUN, 2),
        2005: (JUN, 21),
        2006: (JUN, 11),
        2007: (JUN, 30),
        2008: (JUN, 18),
        2009: (JUN, 7),
        2010: (JUN, 25),
        2011: (JUN, 15),
        2012: (JUN, 4),
        2013: (JUN, 23),
        2014: (JUN, 12),
        2015: (JUN, 2),
        2016: (JUN, 19),
        2017: (JUN, 8),
        2018: (JUN, 27),
        2019: (JUN, 16),
        2020: (JUN, 5),
        2021: (JUN, 24),
        2022: (JUN, 14),
        2023: (JUN, 3),
        2024: (JUN, 21),
        2025: (JUN, 10),
        2026: (JUN, 29),
    }

    UNDUVAP_POYA_DATES = {
        2003: (DEC, 8),
        2004: (DEC, 26),
        2005: (DEC, 15),
        2006: (DEC, 4),
        2007: (DEC, 23),
        2008: (DEC, 12),
        2009: (DEC, 1),
        2010: (DEC, 20),
        2011: (DEC, 10),
        2012: (DEC, 27),
        2013: (DEC, 16),
        2014: (DEC, 6),
        2015: (DEC, 24),
        2016: (DEC, 13),
        2017: (DEC, 3),
        2018: (DEC, 22),
        2019: (DEC, 11),
        2020: (DEC, 29),
        2021: (DEC, 18),
        2022: (DEC, 7),
        2023: (DEC, 26),
        2024: (DEC, 14),
        2025: (DEC, 4),
        2026: (DEC, 23),
    }

    VAP_POYA_DATES = {
        2003: (OCT, 9),
        2004: (OCT, 27),
        2005: (OCT, 17),
        2006: (OCT, 6),
        2007: (OCT, 25),
        2008: (OCT, 14),
        2009: (OCT, 3),
        2010: (OCT, 22),
        2011: (OCT, 11),
        2012: (OCT, 29),
        2013: (OCT, 18),
        2014: (OCT, 8),
        2015: (OCT, 27),
        2016: (OCT, 15),
        2017: (OCT, 5),
        2018: (OCT, 24),
        2019: (OCT, 13),
        2020: (OCT, 30),
        2021: (OCT, 20),
        2022: (OCT, 9),
        2023: (OCT, 28),
        2024: (OCT, 17),
        2025: (OCT, 6),
        2026: (OCT, 25),
    }

    VESAK_POYA_DATES = {
        2003: (MAY, 15),
        2004: (MAY, 4),
        2005: (MAY, 23),
        2006: (MAY, 12),
        2007: (MAY, 1),
        2008: (MAY, 19),
        2009: (MAY, 8),
        2010: (MAY, 27),
        2011: (MAY, 17),
        2012: (MAY, 5),
        2013: (MAY, 24),
        2014: (MAY, 14),
        2015: (MAY, 3),
        2016: (MAY, 21),
        2017: (MAY, 10),
        2018: (APR, 29),
        2019: (MAY, 18),
        2020: (MAY, 7),
        2021: (MAY, 26),
        2022: (MAY, 15),
        2023: (MAY, 5),
        2024: (MAY, 23),
        2025: (MAY, 12),
        2026: (MAY, 1),
    }

    def _get_holiday(self, holiday: str, year: int) -> tuple[date | None, bool]:
        exact_dates = getattr(self, f"{holiday}_DATES_{_CustomCalendar.CUSTOM_ATTR_POSTFIX}", {})
        if year in exact_dates:
            dt = exact_dates[year]
            return date(year, *dt), False

        confirmed_dates = getattr(self, f"{holiday}_DATES", {})
        if year in confirmed_dates:
            dt = confirmed_dates[year]
            return date(year, *dt), False

        if year <= 2026:
            return None, False

        calc_date = _calculate_poya_dates(year).get(holiday)
        return (calc_date if isinstance(calc_date, date) else None, True)

    def _get_holiday_set(self, holiday: str, year: int) -> Iterable[tuple[date, bool]]:
        exact_dates = getattr(self, f"{holiday}_DATES_{_CustomCalendar.CUSTOM_ATTR_POSTFIX}", {})
        if year in exact_dates:
            for dt in _normalize_tuple(exact_dates[year]):
                yield date(year, *dt), False
            return

        confirmed_dates = getattr(self, f"{holiday}_DATES", {})
        if year in confirmed_dates:
            for dt in _normalize_tuple(confirmed_dates[year]):
                yield date(year, *dt), False
            return

        if year <= 2026:
            return

        calc_date = _calculate_poya_dates(year).get(holiday)
        if calc_date:
            yield calc_date, True

    def bak_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BAK_POYA, year)

    def binara_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(BINARA_POYA, year)

    def duruthu_poya_date(self, year: int) -> Iterable[tuple[date, bool]]:
        return self._get_holiday_set(DURUTHU_POYA, year)

    def esala_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(ESALA_POYA, year)

    def il_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(IL_POYA, year)

    def medin_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(MEDIN_POYA, year)

    def nawam_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(NAWAM_POYA, year)

    def nikini_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(NIKINI_POYA, year)

    def poson_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(POSON_POYA, year)

    def unduvap_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(UNDUVAP_POYA, year)

    def vap_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(VAP_POYA, year)

    def vesak_poya_date(self, year: int) -> tuple[date | None, bool]:
        return self._get_holiday(VESAK_POYA, year)


class _CustomSinhalaHolidays(_CustomCalendar, _SinhalaLunar):
    pass
