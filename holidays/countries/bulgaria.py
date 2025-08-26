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

from __future__ import annotations

from gettext import gettext as tr
from typing import TYPE_CHECKING

from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR
from holidays.constants import HALF_DAY, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY

if TYPE_CHECKING:
    from datetime import date


class Bulgaria(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Bulgaria holidays.

    References:
        * [Labor Code](https://web.archive.org/web/20250402193136/https://lex.bg/laws/ldoc/1594373121)
        * [Labor Code changes - State Gazette, Issue 30, 13.04.1990](https://archive.org/details/30-1990)
        * [Labor Code changes - State Gazette, Issue 27, 05.04.1991](https://archive.org/details/27-1991_202511)
        * [Labor Code changes - State Gazette, Issue 104, 17.12.1991](https://archive.org/details/104-1991)
        * [Labor Code changes - State Gazette, Issue 88, 30.10.1992](https://archive.org/details/88-1992)
        * [Labor Code changes - State Gazette, Issue 2, 05.01.1996](https://archive.org/details/2-1996_202511)
        * [Labor Code changes - State Gazette, Issue 22, 24.02.1998](https://archive.org/details/22-1998)
        * [Labor Code changes - State Gazette, Issue 56, 19.05.1998](https://archive.org/details/56-1998)
        * [Labor Code changes - State Gazette, Issue 108, 15.09.1998](https://archive.org/details/108-1998)
        * [Labor Code changes - State Gazette, Issue 15, 23.02.2010](https://web.archive.org/web/20250515130122/https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=29936)
        * [Labor Code changes - State Gazette, Issue 105, 30.12.2016](https://web.archive.org/web/20220509103925/https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=110584)
        * [Labor Code changes - State Gazette, Issue 107, 18.12.2020](https://web.archive.org/web/20210410181539/https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=154367)
        * [Bulgarian public holidays](https://web.archive.org/web/20240814165123/https://www.parliament.bg/bg/24)
        * [Working days and weekends calendar](https://web.archive.org/web/20250916112151/https://kik-info.com/spravochnik/calendar/2025/)
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Bulgaria>
    """

    country = "BG"
    default_language = "bg"
    # %s (observed).
    observed_label = tr("%s (почивен ден)")
    supported_categories = (HALF_DAY, PUBLIC, SCHOOL)
    supported_languages = ("bg", "en_US", "uk")
    # Labor Code changes - State Gazette, Issue 30, 13.04.1990.
    start_year = 1991

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_REVISED_CALENDAR)
        InternationalHolidays.__init__(self)
        # Labor Code changes - State Gazette, Issue 105, 30.12.2016.
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2017)
        super().__init__(*args, **kwargs)

    def _populate_observed(self, dts: set[date], *, multiple: bool = False) -> None:
        excluded_names = {
            # Holy Saturday.
            self.tr("Велика събота"),
            # Easter.
            self.tr("Великден"),
        }

        for dt in sorted(dts):
            for name in self.get_list(dt):
                if name not in excluded_names:
                    self._add_observed(dt, name)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("Нова година")))

        dts_observed.add(
            # Liberation Day.
            self._add_holiday_mar_3(tr("Ден на Освобождението на България от османско иго"))
        )

        # Labor Code changes - State Gazette, Issue 15, 23.02.2010.
        if self._year >= 2010:
            # Good Friday.
            self._add_good_friday(tr("Велики петък"))

            # Holy Saturday.
            self._add_holy_saturday(tr("Велика събота"))

        # Easter.
        name = tr("Великден")
        self._add_easter_sunday(name)
        # Labor Code changes - State Gazette, Issue 27, 05.04.1991.
        self._add_easter_monday(name)

        dts_observed.add(
            # Labor Day and International Workers' Solidarity Day.
            self._add_labor_day(tr("Ден на труда и на международната работническа солидарност"))
        )

        # Labor Code changes - State Gazette, Issue 56, 19.05.1998.
        if self._year >= 1999:
            dts_observed.add(
                # Saint George's Day, Day of the Bulgarian Army.
                self._add_holiday_may_6(tr("Гергьовден, Ден на храбростта и Българската армия"))
            )

        # Renamed by Labor Code changes - State Gazette, Issue 107, 18.12.2020.
        name = (
            # Day of the Holy Brothers Cyril and Methodius, Bulgarian Alphabet,
            # Enlightenment, Culture and Slavonic Literature.
            tr(
                "Ден на светите братя Кирил и Методий, на българската азбука, "
                "просвета и култура и на славянската книжовност"
            )
            if self._year >= 2021
            # Day of Bulgarian Enlightenment and Culture and Slavonic Alphabet.
            else tr("Ден на българската просвета и култура и на славянската писменост")
        )
        dts_observed.add(self._add_holiday_may_24(name))

        # Labor Code changes - State Gazette, Issue 22, 24.02.1998.
        if self._year >= 1998:
            # Unification Day.
            dts_observed.add(self._add_holiday_sep_6(tr("Ден на Съединението")))

        # Abandoned by Labor Code changes - State Gazette, Issue 104, 17.12.1991.
        if self._year <= 1991:
            # Freedom Day.
            self._add_holiday_sep_9(tr("Ден на свободата"))

        # Labor Code changes - State Gazette, Issue 108, 15.09.1998.
        if self._year >= 1998:
            # Independence Day.
            dts_observed.add(self._add_holiday_sep_22(tr("Ден на Независимостта на България")))

        # Labor Code changes - State Gazette, Issue 2, 05.01.1996.
        if self._year >= 1996:
            # Christmas Eve.
            dts_observed.add(self._add_christmas_eve(tr("Бъдни вечер")))

        # Labor Code changes - State Gazette, Issue 104, 17.12.1991.

        # Christmas Day.
        name = tr("Рождество Христово")
        dts_observed.add(self._add_christmas_day(name))
        dts_observed.add(self._add_christmas_day_two(name))

        if self.observed:
            self._populate_observed(dts_observed)

    def _populate_half_day_holidays(self):
        # Established as half-day by Labor Code changes - State Gazette, Issue 104, 17.12.1991.
        # Changed to full-day by Labor Code changes - State Gazette, Issue 2, 05.01.1996.
        if self._year <= 1995:
            # %s (from 2pm).
            begin_time_label = self.tr("%s (след 14 ч.)")

            # Christmas Eve.
            self._add_christmas_eve(begin_time_label % self.tr("Бъдни вечер"))

    def _populate_school_holidays(self):
        # Labor Code changes - State Gazette, Issue 88, 30.10.1992.
        if self._year >= 1992:
            # The Day of the People's Awakeners.
            self._add_holiday_nov_1(tr("Ден на народните будители"))


class BG(Bulgaria):
    pass


class BLG(Bulgaria):
    pass
