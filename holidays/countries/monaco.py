#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Monaco(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Monaco
    https://en.service-public-entreprises.gouv.mc/Employment-and-social-affairs/Employment-regulations/Leave/Public-Holidays  # noqa: E501
    """

    country = "MC"
    default_language = "fr"
    # %s (Observed).
    observed_label = tr("%s (Observé)")
    supported_languages = ("en_US", "fr", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, MonacoStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("Le jour de l'An")))

        # Saint Devote's Day.
        self._add_holiday_jan_27(tr("La Sainte Dévote"))

        # Easter Monday.
        self._add_easter_monday(tr("Le lundi de Pâques"))

        # Labour Day.
        self._add_observed(self._add_labor_day(tr("Fête de la Travaille")))

        # Ascension's Day.
        self._add_ascension_thursday(tr("L'Ascension"))

        # Whit Monday.
        self._add_whit_monday(tr("Le lundi de Pentecôte"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("La Fête Dieu"))

        # Assumption's Day.
        self._add_observed(self._add_assumption_of_mary_day(tr("L'Assomption de Marie")))

        # All Saints' Day.
        self._add_observed(self._add_all_saints_day(tr("La Toussaint")))

        # Prince's Day.
        self._add_observed(self._add_holiday_nov_19(tr("La Fête du Prince")))

        # Immaculate Conception Day.
        name = tr("L'Immaculée Conception")
        if year >= 2019 and self._is_sunday(DEC, 8):
            self._add_holiday_dec_9(name)
        else:
            self._add_holiday_dec_8(name)

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Noël")))


class MC(Monaco):
    pass


class MCO(Monaco):
    pass


class MonacoStaticHolidays:
    special_holidays = {
        # Public holiday.
        2015: (JAN, 7, tr("Jour férié")),
    }
