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

from holidays import OPTIONAL, PUBLIC
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    SUN,
)
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Niger(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Niger holidays.

    References:
        * [Law No. 59-22 of December 24, 1959](https://web.archive.org/web/20241106023958/https://www.impots.gouv.ne/media/loi/1960.pdf)
        * <https://web.archive.org/web/20110721063839/http://www.ais-asecna.org/pdf/gen/gen-2-1/12gen2-1-01.pdf>
        * <https://web.archive.org/web/20250531032502/https://wageindicator.org/documents/decentworkcheck/africa/niger-french-2021.pdf>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Niger>
        * <https://web.archive.org/web/20250531032604/https://wageindicator.org/fr-ne/droit-du-travail/les-conges-et-les-jours-de-repos>
        * <https://web.archive.org/web/20250206194155/https://www.rivermate.com/guides/niger/leave>
        * [Eid al-Adha](https://web.archive.org/web/20250117013558/https://www.timeanddate.com/holidays/niger/eid-al-adha)
        * [Eid al-Fitr](https://web.archive.org/web/20250114130118/https://www.timeanddate.com/holidays/niger/eid-al-fitr)
        * [Laylat al-Qadr](https://web.archive.org/web/20250531033137/https://www.timeanddate.com/holidays/niger/laylat-al-qadr)
        * [Islamic New Year](https://web.archive.org/web/20240723135601/https://www.timeanddate.com/holidays/niger/muharram-new-year)
        * [Prophet's Birthday](https://web.archive.org/web/20250124122731/https://www.timeanddate.com/holidays/niger/prophet-birthday)

    Notes:
        After Law No. 97-020 of June 20, 1997 establishing public holidays came into
        effect, holidays that fell on the mandatory weekly rest day (Sunday) were
        observed on the next Monday.
    """

    country = "NE"
    default_language = "fr_NE"
    supported_languages = ("en_US", "fr_NE")
    supported_categories = (OPTIONAL, PUBLIC)
    # %s (observed).
    observed_label = tr("%s (observé)")
    # %s (estimated).
    estimated_label = tr("%s (estimé)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observé, estimé)")
    # Law No. 59-22.
    start_year = 1960
    weekend = {SUN}

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
            self, cls=NigerIslamicHolidays, show_estimated=islamic_show_estimated
        )
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        kwargs.setdefault("observed_since", 1998)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("Jour de l'An")))

        # Easter Monday.
        self._add_easter_monday(tr("Lundi de Pâques"))

        if self._year >= 1995:
            # National Concord Day.
            self._add_observed(self._add_holiday_apr_24(tr("Fête nationale de la Concorde")))

        # International Labor Day.
        self._add_observed(self._add_labor_day(tr("Journée internationale du travail")))

        if self._year >= 2024:
            # Anniversary of the CNSP Coup.
            self._add_observed(self._add_holiday_jul_26(tr("Anniversaire du coup d'État du CNSP")))

        self._add_observed(
            self._add_holiday_aug_3(
                # Anniversary of the Proclamation of Independence.
                tr("L'anniversaire de la proclamation de l'indépendance")
                if self._year >= 1961
                # Independence Day.
                else tr("Jour de l'indépendance")
            )
        )

        # National Day.
        self._add_observed(self._add_holiday_dec_18(tr("Fête nationale")))

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Noël")))

        # Islamic New Year.
        for dt in self._add_islamic_new_year_day(tr("Jour de l'An musulman")):
            self._add_observed(dt)

        # Prophet's Birthday.
        for dt in self._add_mawlid_day(tr("Mouloud")):
            self._add_observed(dt)

        # Laylat al-Qadr.
        for dt in self._add_laylat_al_qadr_day(tr("Laylat al-Qadr")):
            self._add_observed(dt)

        # Eid al-Fitr.
        for dt in self._add_eid_al_fitr_day(tr("Korité")):
            self._add_observed(dt)

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Tabaski"))

        # Day after Eid al-Adha.
        for dt in self._add_eid_al_adha_day_two(tr("Lendemain de la Tabaski")):
            self._add_observed(dt)

    def _populate_optional_holidays(self):
        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension"))

        # Whit Monday.
        self._add_whit_monday(tr("Lundi de Pentecôte"))

        # Assumption Day.
        self._add_observed(self._add_assumption_of_mary_day(tr("Assomption")))

        # All Saints' Day.
        self._add_observed(self._add_all_saints_day(tr("Toussaint")))


class NigerIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        1998: (APR, 8),
        1999: (MAR, 28),
        2000: (MAR, 16),
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 10),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES = {
        1998: (JAN, 30),
        1999: (JAN, 19),
        2000: ((JAN, 8), (DEC, 28)),
        2001: (DEC, 17),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 23),
        2021: (MAY, 12),
        2022: (MAY, 1),
        2023: (APR, 21),
        2024: (APR, 9),
        2025: (MAR, 30),
    }

    HIJRI_NEW_YEAR_DATES = {
        1998: (APR, 28),
        1999: (APR, 17),
        2000: (APR, 6),
        2001: (MAR, 26),
        2002: (MAR, 15),
        2003: (MAR, 5),
        2004: (FEB, 22),
        2005: (FEB, 10),
        2006: (JAN, 31),
        2007: (JAN, 20),
        2008: ((JAN, 10), (DEC, 29)),
        2009: (DEC, 18),
        2010: (DEC, 8),
        2011: (NOV, 27),
        2012: (NOV, 15),
        2013: (NOV, 5),
        2014: (OCT, 25),
        2015: (OCT, 15),
        2016: (OCT, 3),
        2017: (SEP, 22),
        2018: (SEP, 12),
        2019: (AUG, 31),
        2020: (AUG, 21),
        2021: (AUG, 10),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 6),
        2025: (JUN, 27),
    }

    LAYLAT_AL_QADR_DATES = {
        1998: (JAN, 26),
        1999: (JAN, 15),
        2000: ((JAN, 4), (DEC, 24)),
        2001: (DEC, 13),
        2002: (DEC, 2),
        2003: (NOV, 22),
        2004: (NOV, 11),
        2005: (OCT, 31),
        2006: (OCT, 20),
        2007: (OCT, 9),
        2008: (SEP, 28),
        2009: (SEP, 17),
        2010: (SEP, 6),
        2011: (AUG, 27),
        2012: (AUG, 15),
        2013: (AUG, 4),
        2014: (JUL, 25),
        2015: (JUL, 14),
        2016: (JUL, 2),
        2017: (JUN, 22),
        2018: (JUN, 11),
        2019: (JUN, 1),
        2020: (MAY, 20),
        2021: (MAY, 9),
        2022: (APR, 28),
        2023: (APR, 18),
        2024: (APR, 6),
        2025: (MAR, 27),
    }

    MAWLID_DATES = {
        1998: (JUL, 7),
        1999: (JUN, 26),
        2000: (JUN, 15),
        2001: (JUN, 4),
        2002: (MAY, 24),
        2003: (MAY, 14),
        2004: (MAY, 2),
        2005: (APR, 21),
        2006: (APR, 11),
        2007: (MAR, 31),
        2008: (MAR, 20),
        2009: (MAR, 9),
        2010: (FEB, 26),
        2011: (FEB, 16),
        2012: (FEB, 5),
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }


class NE(Niger):
    pass


class NER(Niger):
    pass
