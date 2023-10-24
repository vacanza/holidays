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

from holidays.calendars.gregorian import DEC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, TUE_TO_PREV_MON, THU_TO_NEXT_FRI


class Hungary(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Hungary
    Codification dates:
      - https://hvg.hu/gazdasag/20170307_Megszavaztak_munkaszuneti_nap_lett_a_nagypentek  # noqa
      - https://www.tankonyvtar.hu/hu/tartalom/historia/92-10/ch01.html#id496839
    """

    country = "HU"
    default_language = "hu"
    # Day off before
    observed_label_before = tr("%s előtti pihenőnap")
    # Day off after
    observed_label = tr("%s utáni pihenőnap")
    supported_languages = ("en_US", "hu", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", TUE_TO_PREV_MON + THU_TO_NEXT_FRI)
        kwargs.setdefault("observed_since", 2010)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        name = self.tr("Újév")
        jan_1 = self._add_new_years_day(name)
        if year >= 2014:
            self._add_observed(jan_1)

            # The last day of the year is an observed day off if New Year's Day
            # falls on a Tuesday.
            if self.observed and self._is_monday(DEC, 31):
                self._add_holiday_dec_31(self.tr(self.observed_label_before) % name)

        if 1945 <= year <= 1950 or year >= 1989:
            # National Day.
            self._add_observed(self._add_holiday_mar_15(tr("Nemzeti ünnep")))

        if year >= 2017:
            # Good Friday.
            self._add_good_friday(tr("Nagypéntek"))

        # Easter.
        self._add_easter_sunday(tr("Húsvét"))

        if year != 1955:
            # Easter Monday.
            self._add_easter_monday(tr("Húsvét Hétfő"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pünkösd"))

        if year <= 1952 or year >= 1992:
            # Whit Monday.
            self._add_whit_monday(tr("Pünkösdhétfő"))

        if year >= 1946:
            # Labor Day.
            name = tr("A Munka ünnepe")
            self._add_observed(self._add_labor_day(name))
            if 1950 <= year <= 1953:
                self._add_labor_day_two(name)

        self._add_observed(
            self._add_holiday_aug_20(
                # Bread Day.
                tr("A kenyér ünnepe")
                if 1950 <= year <= 1989
                else
                # State Foundation Day.
                tr("Az államalapítás ünnepe"),
            )
        )

        if year >= 1991:
            # National Day.
            self._add_observed(self._add_holiday_oct_23(tr("Nemzeti ünnep")))

        if year >= 1999:
            # All Saints' Day.
            self._add_observed(self._add_all_saints_day(tr("Mindenszentek")))

        # Christmas Day.
        self._add_christmas_day(tr("Karácsony"))

        if year != 1955:
            # Second Day of Christmas.
            dec_26 = self._add_christmas_day_two(tr("Karácsony másnapja"))
            if year >= 2013:
                self._add_observed(dec_26, rule=THU_TO_NEXT_FRI)

        # Soviet era.
        if 1950 <= year <= 1989:
            # Proclamation of Soviet Republic Day.
            self._add_holiday_mar_21(tr("A Tanácsköztársaság kikiáltásának ünnepe"))

            # Liberation Day.
            self._add_holiday_apr_4(tr("A felszabadulás ünnepe"))

            if year not in {1956, 1989}:
                # Great October Socialist Revolution Day.
                self._add_holiday_nov_7(tr("A nagy októberi szocialista forradalom ünnepe"))


class HU(Hungary):
    pass


class HUN(Hungary):
    pass
