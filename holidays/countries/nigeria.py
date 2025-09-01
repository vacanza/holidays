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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Nigeria(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Nigeria holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Nigeria>
        * [Public Holidays Decree 1979](https://web.archive.org/web/20240616072641/https://archive.gazettes.africa/archive/ng/1979/ng-government-gazette-supplement-dated-1979-02-01-no-5.pdf)
        * [Public Holidays (Amendment) Decree 1984](https://web.archive.org/web/20240615185836/https://archive.gazettes.africa/archive/ng/1984/ng-government-gazette-supplement-dated-1984-08-30-no-52-part-a.pdf)
        * [Public Holidays Act (2004 Consolidated Version)](https://web.archive.org/web/20250822094939/https://placng.org/lawsofnigeria/view2.php?sn=467)
        * <https://web.archive.org/web/20250829024504/https://fmino.gov.ng/may-29th-in-nigerias-history/>
        * <https://web.archive.org/web/20250829084254/https://www.iita.org/wp-content/uploads/2017/01/The-Bulletin-23-27-May-2011-No.-2070.pdf>
        * <https://web.archive.org/web/20170618031224/http://pulse.ng/local/inauguration-day-fg-declares-may-29-public-holiday-id3795830.html>
        * <https://web.archive.org/web/20250829081956/https://dailypost.ng/2019/05/27/fg-declares-may-29-public-holiday/>
        * <https://web.archive.org/web/20230620060859/https://interior.gov.ng/fg-declares-monday-may-29th-2023-work-free-day-for-presidential-inauguration/>
        * <https://web.archive.org/web/20250829060151/https://statehouse.gov.ng/news/president-buhari-declares-june-12-the-new-democracy-day/>
        * <https://web.archive.org/web/20250829085227/https://www.nairaland.com/4548139/may-29-remains-inauguration-day>
        * <https://web.archive.org/web/20250829030023/https://www.timeanddate.com/holidays/nigeria/2025?hol=9>

    In-lieu holidays have been in effect since at least 2010:
        * <http://archive.today/2025.08.30-142719/https://www.vanguardngr.com/2010/05/fg-declares-may-31-public-holiday-for-democracy/>
    """

    country = "NG"
    default_language = "en_NG"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observed, estimated)")
    # %s (observed).
    observed_label = tr("%s (observed)")
    # Public Holidays Decree 1979, in effect from January 1st, 1979.
    start_year = 1979
    supported_languages = ("en_NG", "en_US")

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
            self, cls=NigeriaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, NigeriaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2010)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("New Year's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Added via Public Holidays (Amendment) Decree 1984 on August 28th, 1984.
        if self._year >= 1985:
            # Workers' Day.
            dts_observed.add(self._add_labor_day(tr("Workers' Day")))

        # Added via Public Holidays (Amendment) Decree 2000.
        # Changed to June 12th for 2019 onwards on July 6th, 2018.
        if self._year >= 2000:
            # Democracy Day.
            name = tr("Democracy Day")
            dts_observed.add(
                self._add_holiday_jun_12(name)
                if self._year >= 2019
                else self._add_holiday_may_29(name)
            )

        if self._year >= 1999 and self._year % 4 == 3:
            # Presidential Inauguration Day.
            self._add_holiday_may_29(tr("Presidential Inauguration Day"))

        # National Day.
        dts_observed.add(self._add_holiday_oct_1(tr("National Day")))

        # Christmas Day.
        dts_observed.add(self._add_christmas_day(tr("Christmas Day")))

        # Boxing Day.
        dts_observed.add(self._add_christmas_day_two(tr("Boxing Day")))

        # Prophet's Birthday.
        dts_observed.update(self._add_mawlid_day(tr("Id el Maulud")))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day(tr("Id el Fitr")))

        # Eid al-Fitr Holiday.
        dts_observed.update(self._add_eid_al_fitr_day_two(tr("Id el Fitr Holiday")))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day(tr("Id el Kabir")))

        # Eid al-Adha Holiday.
        dts_observed.update(self._add_eid_al_adha_day_two(tr("Id el Kabir Holiday")))

        if self.observed:
            self._populate_observed(dts_observed)


class NG(Nigeria):
    pass


class NGA(Nigeria):
    pass


class NigeriaIslamicHolidays(_CustomIslamicHolidays):
    # https://web.archive.org/web/20250829051803/https://www.timeanddate.com/holidays/nigeria/id-el-kabir
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (1979, 2025)
    EID_AL_ADHA_DATES = {
        1979: (NOV, 1),
        1980: (OCT, 20),
        1981: (OCT, 9),
        1982: (SEP, 29),
        1983: (SEP, 18),
        1984: (SEP, 6),
        1985: (AUG, 27),
        1986: (AUG, 16),
        1987: (AUG, 6),
        1988: (JUL, 25),
        1989: (JUL, 14),
        1990: (JUL, 4),
        1991: (JUN, 23),
        1993: (JUN, 1),
        1994: (MAY, 21),
        1995: (MAY, 10),
        1996: (APR, 29),
        1997: (APR, 18),
        1998: (APR, 8),
        1999: (MAR, 28),
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2007: (DEC, 19),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2014: (OCT, 6),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 12),
    }

    # https://web.archive.org/web/20250829052410/https://www.timeanddate.com/holidays/nigeria/id-el-fitr
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (1979, 2025)
    EID_AL_FITR_DATES = {
        1979: (AUG, 25),
        1980: (AUG, 13),
        1981: (AUG, 2),
        1982: (JUL, 23),
        1983: (JUL, 12),
        1985: (JUN, 20),
        1986: (JUN, 9),
        1987: (MAY, 30),
        1988: (MAY, 18),
        1989: (MAY, 7),
        1990: (APR, 27),
        1991: (APR, 16),
        1993: (MAR, 25),
        1994: (MAR, 14),
        1995: (MAR, 3),
        1996: (FEB, 21),
        1997: (FEB, 9),
        1998: (JAN, 30),
        1999: (JAN, 19),
        2000: ((JAN, 8), (DEC, 28)),
        2001: (DEC, 17),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 12),
        2008: (SEP, 29),
        2009: (SEP, 21),
        2010: (SEP, 9),
        2012: (AUG, 20),
        2017: (JUN, 26),
    }

    # https://web.archive.org/web/20250829053435/https://www.timeanddate.com/holidays/nigeria/id-el-maulud
    # https://web.archive.org/web/20250829054319/https://pmnewsnigeria.com/2012/02/03/fg-declares-6-feb-public-holiday/
    MAWLID_DATES_CONFIRMED_YEARS = (1979, 2025)
    MAWLID_DATES = {
        1979: (FEB, 10),
        1982: ((JAN, 8), (DEC, 28)),
        1983: (DEC, 17),
        1984: (DEC, 6),
        1985: (NOV, 25),
        1986: (NOV, 15),
        1987: (NOV, 4),
        1988: (OCT, 23),
        1989: (OCT, 13),
        1990: (OCT, 2),
        1991: (SEP, 21),
        1992: (SEP, 10),
        1993: (AUG, 30),
        1995: (AUG, 9),
        1996: (JUL, 28),
        1997: (JUL, 18),
        1998: (JUL, 7),
        2000: (JUN, 15),
        2003: (MAY, 14),
        2004: (MAY, 2),
        2006: (APR, 11),
        2011: (FEB, 16),
        2012: (FEB, 6),
        2015: ((JAN, 2), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2021: (OCT, 19),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }


class NigeriaStaticHolidays:
    """Nigeria special holidays.

    References:
        * <https://web.archive.org/web/20250829090324/https://www.pambazuka.org/governance/nigeria-holiday-blow-presidential-hopeful>
        * <https://web.archive.org/web/20250829084913/https://www.nbcnews.com/id/wbna36974655>
        * <https://web.archive.org/web/20250829081641/https://businessday.ng/uncategorized/article/2019-elections-fg-declares-friday-public-holiday-excludes-banksothers/>
        * <https://web.archive.org/web/20250829024209/https://statehouse.gov.ng/news/new-date-for-special-federal-executive-council-session-in-honour-of-president-muhammadu-buhari-to-be-announced/>
    """

    # Public Holiday for Elections.
    name_elections = tr("Public Holiday for Elections")

    special_public_holidays = {
        2007: (
            (APR, 12, name_elections),
            (APR, 13, name_elections),
        ),
        # Day of Mourning for President Umaru Yar'Adua.
        2010: (MAY, 6, tr("Day of Mourning for President Umaru Yar'Adua")),
        2019: (FEB, 22, name_elections),
        # Day of Mourning for President Muhammadu Buhari.
        2025: (JUL, 15, tr("Day of Mourning for President Muhammadu Buhari")),
    }
