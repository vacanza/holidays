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

from holidays.calendars.gregorian import JAN, APR, MAY, JUN, JUL, SEP, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_MON


class Latvia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Latvia holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Latvia>
        * <https://web.archive.org/web/20250210170838/https://www.information.lv/>
        * [Law "On Public Holidays, Commemoration Days, and Celebration Days" of Oct 3, 1990](https://web.archive.org/web/20260308023501/https://likumi.lv/doc.php?id=72608)
        * [Law of Sep 21, 1995](https://web.archive.org/web/20251217210932/https://likumi.lv/ta/id/37110-grozijumi-likuma-par-svetku-un-atceres-dienam-)
        * [Law of Dec 18, 1996](https://web.archive.org/web/20251120000352/https://likumi.lv/ta/id/41773-grozijumi-likuma-par-svetku-un-atceres-dienam-)
        * [Law of Mar 21, 2002](https://web.archive.org/web/20250918022517/https://likumi.lv/ta/id/60998-grozijumi-likuma-par-svetku-un-atceres-dienam-)
        * [Law of May 24, 2007](https://web.archive.org/web/20251217210804/https://likumi.lv/ta/id/158621-grozijumi-likuma-par-svetku-atceres-un-atzimejamam-dienam-)
        * [Law of Apr 7, 2011](https://web.archive.org/web/20250918032827/https://likumi.lv/ta/id/229236-grozijumi-likuma-par-svetku-atceres-un-atzimejamam-dienam-)

    Regarding observed holidays start year: the law entered into force on May 24, 2007,
    but since May 4 (Restoration of Independence Day) fell on a Friday, starting in 2007 has
    no extra impact.
    """

    country = "LV"
    default_language = "lv"
    # %s (observed).
    observed_label = tr("%s (brīvdiena)")
    supported_languages = ("en_US", "lv", "uk")
    # Law of Oct 3, 1990.
    start_year = 1991

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, LatviaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        # Law of May 24, 2007.
        kwargs.setdefault("observed_since", 2007)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Jaungada diena"))

        # Good Friday.
        self._add_good_friday(tr("Lielā Piektdiena"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Pirmās Lieldienas"))

        # Established by Law of Dec 18, 1996.
        if self._year >= 1997:
            # Easter Monday.
            self._add_easter_monday(tr("Otrās Lieldienas"))

        # Labor Day.
        self._add_labor_day(tr("Darba svētki"))

        # Constitutional Assembly Convocation Day.
        self._add_holiday_may_1(tr("Latvijas Republikas Satversmes sapulces sasaukšanas diena"))

        # Established by Law of Mar 21, 2002.
        # Renamed by Law of Apr 7, 2011 (came into force on May 11, 2011).
        if self._year >= 2002:
            self._add_observed(
                self._add_holiday_may_4(
                    # Restoration of Independence Day.
                    tr("Latvijas Republikas Neatkarības atjaunošanas diena")
                    if self._year >= 2012
                    # Proclamation of Declaration of Independence Day.
                    else tr("Latvijas Republikas Neatkarības deklarācijas pasludināšanas diena")
                )
            )

        # Mother's Day.
        self._add_holiday_2nd_sun_of_may(tr("Mātes diena"))

        # Established by Law of Sep 21, 1995.
        if self._year >= 1996:
            # Whit Sunday.
            self._add_whit_sunday(tr("Vasarsvētki"))

        # Midsummer Eve.
        self._add_holiday_jun_23(tr("Līgo diena"))

        # Midsummer Day.
        self._add_saint_johns_day(tr("Jāņu diena"))

        # Republic of Latvia Proclamation Day.
        self._add_observed(self._add_holiday_nov_18(tr("Latvijas Republikas Proklamēšanas diena")))

        # Established by Law of May 24, 2007.
        if self._year >= 2007:
            # Christmas Eve.
            self._add_christmas_eve(tr("Ziemassvētku vakars"))

        # Christmas Day.
        self._add_christmas_day(tr("Pirmie Ziemassvētki"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Otrie Ziemassvētki"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Vecgada diena"))


class LV(Latvia):
    pass


class LVA(Latvia):
    pass


class LatviaStaticHolidays:
    """Latvia special holidays.

    References:
        * [Law of Oct 2, 2014](https://web.archive.org/web/20251217210815/https://likumi.lv/ta/id/269373-grozijumi-likuma-par-svetku-atceres-un-atzimejamam-dienam-)
        * [Law of Jun 21, 2018](https://web.archive.org/web/20251217210926/https://likumi.lv/ta/id/299942-grozijums-likuma-par-svetku-atceres-un-atzimejamam-dienam-)
        * [Law of May 28, 2023](https://web.archive.org/web/20251217210837/https://likumi.lv/ta/id/342196-grozijumi-likuma-par-svetku-atceres-un-atzimejamam-dienam-)
        * <https://lv.wikipedia.org/wiki/Vispārējie_latviešu_Dziesmu_un_deju_svētki>

    Substituted holidays references:
        * [2001](https://web.archive.org/web/20260403134810/https://likumi.lv/ta/id/56308-par-darbadienas-parcelsanu)
        * [2002](https://web.archive.org/web/20260403134822/https://likumi.lv/ta/id/60769-par-darbdienas-parcelsanu)
        * [2003-2004](https://web.archive.org/web/20260403134847/https://likumi.lv/ta/id/80562-par-darbdienu-parcelsanu)
        * [2004](https://web.archive.org/web/20210506000821/https://likumi.lv/ta/id/83431-par-darbdienu-parcelsanu)
        * [2006](https://web.archive.org/web/20260403134627/https://likumi.lv/ta/id/145144-par-darbdienas-parcelsanu)
        * [2007](https://web.archive.org/web/20260403134617/https://likumi.lv/ta/id/131354-par-darbdienu-parcelsanu)
        * [2008](https://web.archive.org/web/20260403134715/https://likumi.lv/ta/id/173689-par-darbdienu-parcelsanu)
        * [2009](https://web.archive.org/web/20260403134723/https://likumi.lv/ta/id/185051-par-darbdienu-parcelsanu-2009gada)
        * [2010](https://web.archive.org/web/20241104205338/https://likumi.lv/ta/id/203023-par-darbdienu-parcelsanu-2010gada)
        * [2012](https://web.archive.org/web/20250914121202/https://likumi.lv/ta/id/228399-par-darba-dienas-parcelsanu-2012-gada)
        * [2013](https://web.archive.org/web/20260403134736/https://likumi.lv/ta/id/247102-par-darba-dienu-parcelsanu-2013gada)
        * [2014](https://web.archive.org/web/20251113151841/https://likumi.lv/ta/id/257810-par-darba-dienu-parcelsanu-2014-gada)
        * [2015](https://web.archive.org/web/20260403135250/https://likumi.lv/ta/id/266487-par-darba-dienu-parcelsanu-2015gada)
        * [2017](https://web.archive.org/web/20191122133007/https://likumi.lv/ta/id/282928-par-darbadienas-parcelsanu-2017-gada)
        * [2018](https://web.archive.org/web/20260208223051/https://likumi.lv/ta/id/290413-par-darbadienas-parcelsanu-2018-gada)
        * [2020](https://web.archive.org/web/20250620050822/https://likumi.lv/ta/id/308097-par-darbadienas-parcelsanu-2020-gada)
        * [2021](https://web.archive.org/web/20250328150433/https://likumi.lv/ta/id/315837-par-darba-dienu-parcelsanu-2021-gada)
        * [2023](https://web.archive.org/web/20250620155625/https://likumi.lv/ta/id/333470-par-darba-dienas-parcelsanu-2023-gada)
        * [2024](https://web.archive.org/web/20250813123009/https://likumi.lv/ta/id/342680-par-darba-dienu-parcelsanu-2024-gada)
        * [2025](https://web.archive.org/web/20260121064654/https://likumi.lv/ta/id/351684-par-darba-dienu-parcelsanu-2025-gada)
        * [2026](https://web.archive.org/web/20251219143100/https://likumi.lv/ta/id/361161-par-darba-dienu-parcelsanu-2026-gada)
    """

    # Substituted date format.
    substituted_date_format = tr("%d.%m.%Y")

    # Day off (substituted from %s).
    substituted_label = tr("Brīvdiena (pārcelta no %s)")

    #  Nationwide Latvian Song and Dance Celebration Final Day.
    song_and_dance_festival_final_day = tr(
        "Vispārējo latviešu Dziesmu un deju svētku noslēguma diena"
    )

    # Day of the Pastoral Visit of His Holiness Pope Francis to Latvia.
    pope_francis_pastoral_visit_day = tr(
        "Viņa Svētības pāvesta Franciska pastorālās vizītes Latvijā diena"
    )

    # Day of the Latvian Ice Hockey Team's Bronze Medal Win at the 2023 IIHF World Championship.
    hockey_team_win_bronze_medal_day = tr(
        "Diena, kad Latvijas hokeja komanda ieguva bronzas medaļu 2023. gada "
        "Pasaules hokeja čempionātā"
    )

    special_public_holidays = {
        2001: (DEC, 24, DEC, 22),
        2002: (DEC, 30, DEC, 28),
        2003: (NOV, 17, NOV, 15),
        2004: (
            (JAN, 2, JAN, 10),
            (MAY, 3, MAY, 8),
            (JUN, 25, JUN, 19),
            (NOV, 19, NOV, 13),
        ),
        2006: (NOV, 27, DEC, 2),
        2007: (APR, 30, APR, 14),
        2008: (
            (MAY, 2, MAY, 10),
            (NOV, 17, NOV, 22),
        ),
        2009: (
            (JAN, 2, JAN, 10),
            (JUN, 22, JUN, 27),
        ),
        2010: (
            (MAY, 3, MAY, 29),
            (JUN, 25, JUN, 19),
            (NOV, 19, NOV, 13),
        ),
        2012: (APR, 30, APR, 28),
        2013: (
            (DEC, 23, DEC, 14),
            (DEC, 30, DEC, 28),
        ),
        2014: (
            (MAY, 2, MAY, 10),
            (NOV, 17, NOV, 22),
        ),
        2015: (
            (JAN, 2, JAN, 10),
            (JUN, 22, JUN, 27),
        ),
        2017: (MAY, 5, MAY, 13),
        2018: (
            (APR, 30, APR, 21),
            (JUL, 9, song_and_dance_festival_final_day),
            (SEP, 24, pope_francis_pastoral_visit_day),
        ),
        2020: (JUN, 22, JUN, 13),
        2021: (
            (MAY, 3, MAY, 8),
            (JUN, 25, JUN, 19),
            (NOV, 19, NOV, 13),
        ),
        2023: (
            (MAY, 5, MAY, 20),
            (MAY, 29, hockey_team_win_bronze_medal_day),
            (JUL, 10, song_and_dance_festival_final_day),
        ),
        2024: (
            (DEC, 23, DEC, 14),
            (DEC, 30, DEC, 28),
        ),
        2025: (
            (MAY, 2, MAY, 10),
            (NOV, 17, NOV, 8),
        ),
        2026: (
            (JAN, 2, JAN, 17),
            (JUN, 22, JUN, 27),
        ),
    }
