#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.constants import PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SUN_TO_NEXT_MON,
    SAT_TO_PREV_FRI,
)


class SaoTomeAndPrincipe(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """São Tomé and Príncipe holidays.

    References:
        * https://en.wikipedia.org/wiki/Public_holidays_in_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe
        * https://www.timeanddate.com/holidssays/sao-tome-and-principe/
        * https://www.saotomeexpert.pt/en/sao-tome-public-holidays/
        * https://www.qppstudio.net/publicholidays2025/sao_tome_and_principe.htm
    """

    country = "ST"
    subdivisions = (
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "PR",
    )

    subdivisions_aliases = {
        "Agua Grande": "01",
        "Cantagalo": "02",
        "Caue": "03",
        "Lemba": "04",
        "Lobata": "05",
        "Me-Zochi": "06",
        "Principe": "PR",  # Autonomous region
    }

    default_language = "pt"
    supported_categories = (PUBLIC,)
    observed_label = tr("%s (observed)")
    supported_languages = ("en_US", "pt")
    start_year = 1975  # Independence year
    observed_start_year = 2020  # Year when observed holidays began

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=SaoTomeAndPrincipeStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON + SAT_TO_PREV_FRI)
        super().__init__(*args, **kwargs)
        # Set the correct observed suffix based on language
        if self.language == "en_US":
            self.observed_suffix = "%s (observed)"
        else:
            self.observed_suffix = "%s (observado)"

    def _add_observed(self, holiday_date):
        """Add observed holidays only if the year is >= observed_start_year."""
        if self._year >= self.observed_start_year:
            super()._add_observed(holiday_date)

    def _populate_public_holidays(self):
        """Populate holidays - national for all, plus extras for Príncipe."""
        if self._year < self.start_year:
            return None

        # National holidays (observed everywhere)
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("Ano Novo")))

        # Day of King Amador (January 4).
        # Commemorates King Amador, leader of 16th century slave rebellion.
        self._add_observed(self._add_holiday_jan_4(tr("Dia do Rei Amador")))

        # Martyrs' Day (February 3).
        # Commemorates the 1953 Batepá massacre.
        self._add_observed(self._add_holiday_feb_3(tr("Dia dos Mártires")))

        # Labor Day (May 1).
        self._add_observed(self._add_labor_day(tr("Dia do Trabalhador")))

        # Independence Day (July 12).
        # From Portugal in 1975.
        self._add_observed(self._add_holiday_jul_12(tr("Dia da Independência")))

        # Armed Forces Day (September 6).
        self._add_observed(self._add_holiday_sep_6(tr("Dia das Forças Armadas")))

        # Agricultural Reform Day (September 30).
        # Nationalization of plantations in 1975.
        self._add_observed(self._add_holiday_sep_30(tr("Dia da Reforma Agrária")))

        # São Tomé Day only from 2019 onwards.
        if self._year >= 2019:
            self._add_observed(self._add_holiday_dec_21(tr("Dia de São Tomé")))

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Natal")))

        # Príncipe-specific holidays
        if self.subdiv == "PR":
            # Discovery of Príncipe Island (January 17).
            self._add_observed(self._add_holiday_jan_17(tr("Descobrimento da Ilha do Príncipe")))

            # Autonomy Day (April 29).
            # Príncipe gained autonomy in 1995.
            if self._year >= 1995:
                self._add_observed(self._add_holiday_apr_29(tr("Dia da Autonomia do Príncipe")))

            # São Lourenço Day (August 15).
            self._add_observed(self._add_holiday_aug_15(tr("Dia de São Lourenço")))


class ST(SaoTomeAndPrincipe):
    """Alias for São Tomé and Príncipe national holidays (no subdivision)."""

    pass


class STP(SaoTomeAndPrincipe):
    """Alias for São Tomé and Príncipe (allows subdivision specification)."""

    pass


class SaoTomeAndPrincipeStaticHolidays:
    """Placeholder for future special holidays."""

    pass
