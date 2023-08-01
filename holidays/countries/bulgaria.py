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

from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR
from holidays.constants import PUBLIC, SCHOOL
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Bulgaria(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Official holidays in Bulgaria in their current form. This class does not
    any return holidays before 1990, as holidays in the People's Republic of
    Bulgaria and earlier were different.

    Since 2017, it has been accepted that public holidays in Bulgaria that fall on a Saturday
    or Sunday are to be taken on the first working day after them. If there are both Saturday
    and Sunday holidays, Monday and Tuesday are rested respectively.
    The exceptions are:
    1) the Easter holidays, which are always a consecutive Friday, Saturday, and Sunday;
    2) National Awakening Day which, while an official holiday and a non-attendance day for
    schools, is still a working day.

    Sources (Bulgarian):
    - http://lex.bg/laws/ldoc/1594373121
    - https://www.parliament.bg/bg/24
    - https://kik-info.com/spravochnik/calendar/2021/

    Sources (English):
    - https://en.wikipedia.org/wiki/Public_holidays_in_Bulgaria
    """

    country = "BG"
    default_language = "bg"
    supported_categories = {PUBLIC, SCHOOL}
    supported_languages = ("bg", "en_US", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_REVISED_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1989:
            return None

        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("Нова година")))

        dts_observed.add(
            # Liberation Day.
            self._add_holiday_mar_3(tr("Ден на Освобождението на България от османско иго"))
        )

        # Good Friday.
        self._add_good_friday(tr("Велики петък"))

        # Holy Saturday.
        self._add_holy_saturday(tr("Велика събота"))

        # Easter.
        name = tr("Великден")
        self._add_easter_sunday(name)
        self._add_easter_monday(name)

        dts_observed.add(
            # International Workers' Day.
            self._add_labor_day(tr("Ден на труда и на международната работническа солидарност"))
        )

        dts_observed.add(
            # Saint George's Day.
            self._add_holiday_may_6(tr("Гергьовден, Ден на храбростта и Българската армия"))
        )

        dts_observed.add(
            self._add_holiday_may_24(
                # Bulgarian Education and Culture and Slavonic Literature Day.
                tr(
                    "Ден на светите братя Кирил и Методий, на българската азбука, "
                    "просвета и култура и на славянската книжовност"
                )
            )
        )

        # Unification Day.
        dts_observed.add(self._add_holiday_sep_6(tr("Ден на Съединението")))

        # Independence Day.
        dts_observed.add(self._add_holiday_sep_22(tr("Ден на Независимостта на България")))

        # Christmas Eve.
        dts_observed.add(self._add_christmas_eve(tr("Бъдни вечер")))

        # Christmas Day.
        name = tr("Рождество Христово")
        dts_observed.add(self._add_christmas_day(name))
        dts_observed.add(self._add_christmas_day_two(name))

        if self.observed and self._year >= 2017:
            excluded_names = {self.tr("Велика събота"), self.tr("Великден")}
            for dt in sorted(dts_observed):
                if not self._is_weekend(dt):
                    continue
                dt_observed = dt + td(days=+2 if self._is_saturday(dt) else +1)
                while dt_observed in self:
                    dt_observed += td(days=+1)
                for name in self.get_list(dt):
                    if name not in excluded_names:
                        self._add_holiday(self.tr("%s (почивен ден)") % name, dt_observed)

    def _populate_school_holidays(self):
        # National Awakening Day.
        self._add_holiday_nov_1(tr("Ден на народните будители"))


class BG(Bulgaria):
    pass


class BLG(Bulgaria):
    pass
