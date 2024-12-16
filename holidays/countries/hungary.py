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

from holidays.calendars.gregorian import JAN, MAR, APR, MAY, AUG, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Hungary(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Hungary

    Codification dates:
        - https://hvg.hu/gazdasag/20170307_Megszavaztak_munkaszuneti_nap_lett_a_nagypentek
        - https://www.tankonyvtar.hu/hu/tartalom/historia/92-10/ch01.html#id496839

    Substituted holidays official sources:
      - `2010 <https://njt.hu/jogszabaly/2009-20-20-1X>`_
      - `2011 <https://njt.hu/jogszabaly/2010-7-20-2X>`_
      - `2012 <https://njt.hu/jogszabaly/2011-39-20-2X>`_
      - `2012-2013 <https://njt.hu/jogszabaly/2012-28-20-2X>`_
      - `2014 <https://njt.hu/jogszabaly/2013-33-20-2X>`_
      - `2015 <https://njt.hu/jogszabaly/2014-28-20-2X>`_
      - `2016 <https://njt.hu/jogszabaly/2015-18-20-2X>`_
      - `2018 <https://njt.hu/jogszabaly/2017-61-B0-15>`_
      - `2019 <https://njt.hu/jogszabaly/2018-6-20-53>`_
      - `2020 <https://njt.hu/jogszabaly/2019-7-20-53>`_
      - `2021 <https://njt.hu/jogszabaly/2020-14-20-7Q>`_
      - `2022 <https://njt.hu/jogszabaly/2021-23-20-7Q>`_
      - `2024 <https://njt.hu/jogszabaly/2023-15-20-8P>`_
      - `2025 <https://njt.hu/jogszabaly/2024-11-20-2X>`_
    """

    country = "HU"
    default_language = "hu"
    supported_languages = ("en_US", "hu", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, HungaryStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Újév"))

        if 1945 <= self._year <= 1950 or self._year >= 1989:
            # National Day.
            self._add_holiday_mar_15(tr("Nemzeti ünnep"))

        if self._year >= 2017:
            # Good Friday.
            self._add_good_friday(tr("Nagypéntek"))

        # Easter.
        self._add_easter_sunday(tr("Húsvét"))

        if self._year != 1955:
            # Easter Monday.
            self._add_easter_monday(tr("Húsvét Hétfő"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Pünkösd"))

        if self._year <= 1952 or self._year >= 1992:
            # Whit Monday.
            self._add_whit_monday(tr("Pünkösdhétfő"))

        if self._year >= 1946:
            # Labor Day.
            name = tr("A Munka ünnepe")
            self._add_labor_day(name)
            if 1950 <= self._year <= 1953:
                self._add_labor_day_two(name)

        self._add_holiday_aug_20(
            # Bread Day.
            tr("A kenyér ünnepe")
            if 1950 <= self._year <= 1989
            # State Foundation Day.
            else tr("Az államalapítás ünnepe")
        )

        if self._year >= 1991:
            # National Day.
            self._add_holiday_oct_23(tr("Nemzeti ünnep"))

        if self._year >= 1999:
            # All Saints' Day.
            self._add_all_saints_day(tr("Mindenszentek"))

        # Christmas Day.
        self._add_christmas_day(tr("Karácsony"))

        if self._year != 1955:
            # Second Day of Christmas.
            self._add_christmas_day_two(tr("Karácsony másnapja"))

        # Soviet era.
        if 1950 <= self._year <= 1989:
            # Proclamation of Soviet Republic Day.
            self._add_holiday_mar_21(tr("A Tanácsköztársaság kikiáltásának ünnepe"))

            # Liberation Day.
            self._add_holiday_apr_4(tr("A felszabadulás ünnepe"))

            if self._year not in {1956, 1989}:
                # Great October Socialist Revolution Day.
                self._add_holiday_nov_7(tr("A nagy októberi szocialista forradalom ünnepe"))


class HU(Hungary):
    pass


class HUN(Hungary):
    pass


class HungaryStaticHolidays:
    # Substituted date format.
    substituted_date_format = tr("%Y. %m. %d.")
    # Day off (substituted from %s).
    substituted_label = tr("Pihenőnap (%s-től helyettesítve)")
    special_public_holidays = {
        2010: (DEC, 24, DEC, 11),
        2011: (
            (MAR, 14, MAR, 19),
            (OCT, 31, NOV, 5),
        ),
        2012: (
            (MAR, 16, MAR, 24),
            (APR, 30, APR, 21),
            (OCT, 22, OCT, 27),
            (NOV, 2, NOV, 10),
            (DEC, 24, DEC, 15),
            (DEC, 31, DEC, 1),
        ),
        2013: (
            (AUG, 19, AUG, 24),
            (DEC, 24, DEC, 7),
            (DEC, 27, DEC, 21),
        ),
        2014: (
            (MAY, 2, MAY, 10),
            (OCT, 24, OCT, 18),
            (DEC, 24, DEC, 13),
        ),
        2015: (
            (JAN, 2, JAN, 10),
            (AUG, 21, AUG, 8),
            (DEC, 24, DEC, 12),
        ),
        2016: (
            (MAR, 14, MAR, 5),
            (OCT, 31, OCT, 15),
        ),
        2018: (
            (MAR, 16, MAR, 10),
            (APR, 30, APR, 21),
            (OCT, 22, OCT, 13),
            (NOV, 2, NOV, 10),
            (DEC, 24, DEC, 1),
            (DEC, 31, DEC, 15),
        ),
        2019: (
            (AUG, 19, AUG, 10),
            (DEC, 24, DEC, 7),
            (DEC, 27, DEC, 14),
        ),
        2020: (
            (AUG, 21, AUG, 29),
            (DEC, 24, DEC, 12),
        ),
        2021: (DEC, 24, DEC, 11),
        2022: (
            (MAR, 14, MAR, 26),
            (OCT, 31, OCT, 15),
        ),
        2024: (
            (AUG, 19, AUG, 3),
            (DEC, 24, DEC, 7),
            (DEC, 27, DEC, 14),
        ),
        2025: (
            (MAY, 2, MAY, 17),
            (OCT, 24, OCT, 18),
            (DEC, 24, DEC, 13),
        ),
    }
