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

from datetime import timedelta as td
from gettext import gettext as tr

from holidays.calendars.gregorian import _get_all_sundays
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Sweden(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Swedish holidays.
    Note that holidays falling on a sunday are "lost",
    it will not be moved to another day to make up for the collision.
    In Sweden, ALL sundays are considered a holiday
    (https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige).
    Initialize this class with include_sundays=False
    to not include sundays as a holiday.

    Primary sources:
        - https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige
        - http://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-1989253-om-allmanna-helgdagar_sfs-1989-253  # noqa: E501
    """

    country = "SE"
    default_language = "sv"
    supported_languages = ("en_US", "sv", "uk")

    def __init__(self, include_sundays=True, *args, **kwargs):
        """
        :param include_sundays:
            Whether to consider sundays as a holiday (which they are in Sweden)
        """
        self.include_sundays = include_sundays
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Nyårsdagen"))

        # Epiphany.
        self._add_epiphany_day(tr("Trettondedag jul"))

        if self._year <= 1953:
            # Feast of the Annunciation.
            self._add_holiday_mar_25(tr("Jungfru Marie bebådelsedag"))

        # Good Friday.
        self._add_good_friday(tr("Långfredagen"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Påskdagen"))

        # Easter Monday.
        self._add_easter_monday(tr("Annandag påsk"))

        # Source: https://sv.wikipedia.org/wiki/F%C3%B6rsta_maj
        if self._year >= 1939:
            # May Day.
            self._add_labor_day(tr("Första maj"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Kristi himmelsfärdsdag"))

        # Source: https://sv.wikipedia.org/wiki/Sveriges_nationaldag
        if self._year >= 2005:
            # National Day of Sweden.
            self._add_holiday_jun_6(tr("Sveriges nationaldag"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pingstdagen"))

        if self._year <= 2004:
            # Whit Monday.
            self._add_whit_monday(tr("Annandag pingst"))

        # Source:
        # https://sv.wikipedia.org/wiki/Midsommarafton
        # https://www.nordiskamuseet.se/aretsdagar/midsommarafton
        # Midsummer evening. Friday between June 19th and June 25th

        # Midsummer Eve.
        name = tr("Midsommarafton")
        dt = (
            self._add_holiday_1st_fri_from_jun_19(name)
            if self._year >= 1953
            else self._add_holiday_jun_23(name)
        )

        # Midsummer Day.
        self._add_holiday(tr("Midsommardagen"), dt + td(days=+1))

        # All Saints' Day.
        self._add_holiday_1st_sat_from_oct_31(tr("Alla helgons dag"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Julafton"))

        # Christmas Day.
        self._add_christmas_day(tr("Juldagen"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Annandag jul"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Nyårsafton"))

        # Optionally add all Sundays of the year.
        if self.include_sundays:
            for dt in _get_all_sundays(self._year):
                # Sunday.
                self._add_holiday(tr("Söndag"), dt)


class SE(Sweden):
    pass


class SWE(Sweden):
    pass
