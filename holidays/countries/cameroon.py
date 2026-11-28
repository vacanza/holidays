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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.helpers import tr
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_WORKDAY


class Cameroon(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Cameroon holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Cameroon>
        * <https://web.archive.org/web/20250408001410/https://www.timeanddate.com/holidays/cameroon/>
        * <https://web.archive.org/web/20231004010829/https://www.officeholidays.com/countries/cameroon>
        * [Eid al-Adha 2024](https://web.archive.org/web/20260722203123/https://fr.journalducameroun.com/cameroun-paul-biya-declare-la-journee-du-17-juin-feriee/)
        * [Eid al-Fitr 2025](https://web.archive.org/web/20260612082941/https://www.237online.com/cameroun-2025-laid-officiellement-fixe-au-31-mars/)
        * [Eid al-Adha 2025](https://web.archive.org/web/20260713001724/https://www.bvm-ac.org/echos-du-marche/avis-n034-2025-bvmac-dg-relatif-a-la-journee-du-vendredi-06-juin-2025/)
        * [Eid al-Fitr 2026](https://web.archive.org/web/20260410160706/https://www.bvm-ac.org/echos-du-marche/avis-n009-2026-bvmac-dg-relatif-a-la-journee-du-vendredi-20-mars-2026/)
        * [Eid al-Adha 2026](https://web.archive.org/web/20260618014344/https://www.bvm-ac.org/echos-du-marche/avis-n035-2026-bvmac-dg-relatif-a-la-journee-du-mercredi-27-mai-2026/)
    """

    country = "CM"
    default_language = "en_CM"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observed, estimated)")
    # %s (observed).
    observed_label = tr("%s (observed)")
    # On 1 January 1960, French Cameroun gained independence from France.
    start_year = 1960
    supported_languages = ("en_CM", "en_US", "fr")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=CameroonIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=CameroonStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("New Year's Day")))

        if self._year >= 1966:
            # Youth Day.
            dts_observed.add(self._add_holiday_feb_11(tr("Youth Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Labor Day.
        dts_observed.add(self._add_labor_day(tr("Labour Day")))

        if self._year >= 1972:
            # National Day.
            dts_observed.add(self._add_holiday_may_20(tr("National Day")))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        # Assumption Day.
        dts_observed.add(self._add_assumption_of_mary_day(tr("Assumption Day")))

        # Christmas Day.
        dts_observed.add(self._add_christmas_day(tr("Christmas Day")))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day(tr("Eid al-Fitr")))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day(tr("Eid al-Adha")))

        # Prophet's Birthday.
        dts_observed.update(self._add_mawlid_day(tr("Mawlid")))

        if self.observed:
            self._populate_observed(dts_observed)


class CM(Cameroon):
    pass


class CMR(Cameroon):
    pass


class CameroonIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2001, 2026)
    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2001, 2026)
    EID_AL_FITR_DATES = {
        2001: (DEC, 17),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2011: (AUG, 31),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2025: (MAR, 31),
    }

    MAWLID_DATES_CONFIRMED_YEARS = (2001, 2022)
    MAWLID_DATES = {
        2003: (MAY, 14),
        2004: (MAY, 2),
        2006: (APR, 11),
        2011: (FEB, 16),
        2012: (FEB, 5),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2021: (OCT, 19),
    }


class CameroonStaticHolidays:
    # Public Holiday.
    public_holiday = tr("Public Holiday")

    special_public_holidays = {
        2021: (
            (MAY, 14, public_holiday),
            (JUL, 19, public_holiday),
        ),
    }

    special_public_holidays_observed = {
        # Eid al-Adha.
        2007: (JAN, 2, tr("Eid al-Adha")),
    }
