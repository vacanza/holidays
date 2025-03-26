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

from holidays.calendars.gregorian import _timedelta, _get_all_sundays
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Sweden(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Sweden holidays.

    References:
        * <https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige>
        * <http://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-1989253-om-allmanna-helgdagar_sfs-1989-253>
        * <https://sv.wikipedia.org/wiki/F%C3%B6rsta_maj>
        * <https://sv.wikipedia.org/wiki/Sveriges_nationaldag>
        * <https://sv.wikipedia.org/wiki/Midsommarafton>


    Note that holidays falling on a sunday is "lost", it will not be moved
    to another day to make up for the collision.

    In Sweden, ALL sundays are considered a holiday.
    Initialize this class with `include_sundays=False` to not include sundays as a holiday.
    """

    country = "SE"
    default_language = "sv"
    supported_languages = ("en_US", "sv", "th", "uk")

    def __init__(self, include_sundays: bool = True, *args, **kwargs):
        """
        Args:
            include_sundays:
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

        if self._year >= 1939:
            # May Day.
            self._add_labor_day(tr("Första maj"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Kristi himmelsfärdsdag"))

        if self._year >= 2005:
            # National Day of Sweden.
            self._add_holiday_jun_6(tr("Sveriges nationaldag"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pingstdagen"))

        if self._year <= 2004:
            # Whit Monday.
            self._add_whit_monday(tr("Annandag pingst"))

        # Midsummer Eve.
        name = tr("Midsommarafton")
        dt = (
            self._add_holiday_1st_fri_from_jun_19(name)
            if self._year >= 1953
            else self._add_holiday_jun_23(name)
        )

        # Midsummer Day.
        self._add_holiday(tr("Midsommardagen"), _timedelta(dt, +1))

        if self._year >= 1953:
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
