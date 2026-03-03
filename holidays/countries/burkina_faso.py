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
from holidays.calendars.gregorian import JAN, JUN, JUL, SEP, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class BurkinaFaso(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Burkina Faso holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Burkina_Faso>
        * <https://web.archive.org/web/20250909124634/https://www.officeholidays.com/countries/burkina-faso>
        * [Law 079-2015/CNT](https://web.archive.org/web/20250717095711/https://academiedepolice.bf/index.php/telechargement/category/51-autres-textes-legislatifs-et-reglementaires?download=83:loi-portant-de-fetes-legales-et-evenements-a-caractere-historique-au-burkina-faso)
    """

    country = "BF"
    # English is the official language since 2024; French remains widely used.
    default_language = "en_BF"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observed, estimated)")
    # %s (observed).
    observed_label = tr("%s (observed)")
    # On 5 August 1960, Burkina Faso (Republic of Upper Volta at that time)
    # gained independence from France.
    start_year = 1961
    supported_languages = ("en_BF", "en_US", "fr")

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
            self, cls=BurkinaFasoIslamicHolidays, show_estimated=islamic_show_estimated
        )
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        if self._year >= 1967:
            # Revolution Day.
            self._add_observed(self._add_holiday_jan_3(tr("Revolution Day")))

        # International Women's Day.
        self._add_observed(self._add_womens_day(tr("International Women's Day")))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Labour Day")))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        # Independence Day.
        self._add_observed(self._add_holiday_aug_5(tr("Independence Day")))

        # Assumption Day.
        self._add_observed(self._add_assumption_of_mary_day(tr("Assumption Day")))

        if self._year >= 2016:
            # Martyrs' Day.
            self._add_observed(self._add_holiday_oct_31(tr("Martyrs' Day")))

        # All Saints' Day.
        self._add_observed(self._add_all_saints_day(tr("All Saints' Day")))

        # Proclamation of Independence Day.
        self._add_observed(self._add_holiday_dec_11(tr("Proclamation of Independence Day")))

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Eid al-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Eid al-Adha"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Mawlid"))


class BF(BurkinaFaso):
    pass


class BFA(BurkinaFaso):
    pass


class BurkinaFasoIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2014, 2023)
    EID_AL_ADHA_DATES = {
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2014, 2024)
    EID_AL_FITR_DATES = {
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
    }

    MAWLID_DATES_CONFIRMED_YEARS = (2014, 2022)
    MAWLID_DATES = {
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2021: (OCT, 19),
        2022: (OCT, 9),
    }
