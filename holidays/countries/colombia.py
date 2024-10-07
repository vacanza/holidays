#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, ALL_TO_NEXT_MON


class Colombia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Colombia has 18 holidays. The establishing of these are by:
    Ley 35 de 1939 (DEC 4): https://bit.ly/3PJwk7B
    Decreto 2663 de 1950 (AUG 5): https://bit.ly/3PJcut8
    Decreto 3743 de 1950 (DEC 20): https://bit.ly/3B9Otr3
    Ley 51 de 1983 (DEC 6): https://bit.ly/3aSobiB

    On the 6th of December 1983, the government of Colombia declared which
    holidays are to take effect, and also clarified that a subset of them
    are to take place the next Monday if they do not fall on a Monday.
    This law is "Ley 51 de 1983" which translates to law 51 of 1983.
    Link: https://bit.ly/3PtPi2e
    A few links below to calendars from the 1980s to demonstrate this law
    change. In 1984 some calendars still use the old rules, presumably
    because they were printed prior to the declaration of law change.
    1981: https://bit.ly/3BbgKOc
    1982: https://bit.ly/3BdbhWW
    1984: https://bit.ly/3PqGxWU
    1984: https://bit.ly/3B7ogt8
    """

    country = "CO"
    default_language = "es"
    # %s (observed).
    observed_label = tr("%s (observado)")
    supported_languages = ("en_US", "es", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", ALL_TO_NEXT_MON)
        kwargs.setdefault("observed_since", 1984)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Año Nuevo"))

        if self._year >= 1951:
            # Epiphany.
            self._move_holiday(self._add_epiphany_day(tr("Día de los Reyes Magos")))

            # Saint Joseph's Day.
            self._move_holiday(self._add_saint_josephs_day(tr("Día de San José")))

            # Maundy Thursday.
            self._add_holy_thursday(tr("Jueves Santo"))

            # Good Friday.
            self._add_good_friday(tr("Viernes Santo"))

            # Ascension Day.
            self._move_holiday(self._add_ascension_thursday(tr("Ascensión del señor")))

            # Corpus Christi.
            self._move_holiday(self._add_corpus_christi_day(tr("Corpus Christi")))

        # Labor Day.
        self._add_labor_day(tr("Día del Trabajo"))

        if self._year >= 1984:
            self._move_holiday(
                # Sacred Heart.
                self._add_holiday_68_days_past_easter(tr("Sagrado Corazón"))
            )

        if self._year >= 1951:
            # Saint Peter and Saint Paul's Day.
            self._move_holiday(self._add_saints_peter_and_paul_day(tr("San Pedro y San Pablo")))

        # Independence Day.
        self._add_holiday_jul_20(tr("Día de la Independencia"))

        # Battle of Boyaca.
        self._add_holiday_aug_7(tr("Batalla de Boyacá"))

        if self._year >= 1951:
            # Assumption Day.
            self._move_holiday(self._add_assumption_of_mary_day(tr("La Asunción")))

        # Columbus Day.
        self._move_holiday(self._add_columbus_day(tr("Día de la Raza")))

        if self._year >= 1951:
            # All Saints' Day.
            self._move_holiday(self._add_all_saints_day(tr("Día de Todos los Santos")))

        self._move_holiday(
            # Independence of Cartagena.
            self._add_holiday_nov_11(tr("Independencia de Cartagena"))
        )

        if self._year >= 1951:
            # Immaculate Conception.
            self._add_immaculate_conception_day(tr("La Inmaculada Concepción"))

        # Christmas Day.
        self._add_christmas_day(tr("Navidad"))


class CO(Colombia):
    pass


class COL(Colombia):
    pass
