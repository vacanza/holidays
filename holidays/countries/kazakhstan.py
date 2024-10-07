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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Kazakhstan(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """
    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan
        - https://egov.kz/cms/en/articles/holidays-calend
        - https://adilet.zan.kz/kaz/docs/Z010000267%5F/history
        - https://adilet.zan.kz/kaz/docs/Z990000493%5F#z63

    Substituted holidays:
        - `2000 <https://adilet.zan.kz/kaz/docs/P000000642%5F>`_
        - 2001: `<https://adilet.zan.kz/kaz/docs/P010000282%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P010000515%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P010001604%5F>`_
        - `2002 <https://adilet.zan.kz/kaz/docs/P020000466%5F>`_
        - 2003: `<https://adilet.zan.kz/kaz/docs/P030000338%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P030001166%5F>`_
        - 2005: `<https://adilet.zan.kz/kaz/docs/P050000142%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P050000751%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P050000949%5F>`_
        - 2006: `<https://adilet.zan.kz/kaz/docs/P050001309%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P060000277%5F>`_
        - 2007: `<https://adilet.zan.kz/kaz/docs/P070000148%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P070000165%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P070000713%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P070000925%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P070001113%5F>`_
        - `2008 <https://adilet.zan.kz/kaz/docs/P080000364%5F>`_
        - `2009 <https://adilet.zan.kz/kaz/docs/P090001936%5F>`_
        - 2010: `<https://adilet.zan.kz/kaz/docs/P090002216%5F>`_,
                `<https://adilet.zan.kz/kaz/docs/P100000637%5F>`_
        - 2011: `<https://adilet.zan.kz/kaz/docs/P1100000167>`_,
                `<https://adilet.zan.kz/kaz/docs/P1100000948>`_
        - 2012: `<https://adilet.zan.kz/kaz/docs/P1200000268>`_,
                `<https://adilet.zan.kz/kaz/docs/P1200000458>`_,
                `<https://adilet.zan.kz/kaz/docs/P1200001538>`_
        - 2013: `<https://adilet.zan.kz/kaz/docs/P1300000345>`_,
                `<https://adilet.zan.kz/kaz/docs/P1300001068>`_,
                `<https://adilet.zan.kz/kaz/docs/P1300001322>`_
        - `2014 <https://adilet.zan.kz/kaz/docs/P1400000365>`_
        - `2016 <https://adilet.zan.kz/kaz/docs/P1600000067>`_
        - `2017 <https://adilet.zan.kz/kaz/docs/P1700000005>`_
        - `2018 <https://adilet.zan.kz/kaz/docs/P1700000864>`_
        - `2019 <https://adilet.zan.kz/kaz/docs/P1800000888>`_
        - `2020 <https://adilet.zan.kz/kaz/docs/P1900000820>`_
        - `2021 <https://adilet.zan.kz/kaz/docs/P2000000930>`_
        - `2022 <https://adilet.zan.kz/kaz/docs/P2200000796>`_
        - `2023 <https://adilet.zan.kz/kaz/docs/P2300000326>`_
        - `2024 <https://adilet.zan.kz/kaz/docs/G24G0000109>`_
    """

    country = "KZ"
    default_language = "kk"
    # %s (estimated).
    estimated_label = tr("%s (бағаланған)")
    # %s (observed).
    observed_label = tr("%s (қайта белгіленген демалыс)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (қайта белгіленген демалыс, бағаланған)")
    supported_languages = ("en_US", "kk", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, KazakhstanIslamicHolidays)
        StaticHolidays.__init__(self, KazakhstanStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2002)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Kazakhstan declared its sovereignty on 25 October 1990
        if self._year <= 1990:
            return None

        dts_observed = set()

        # New Year's Day.
        name = tr("Жаңа жыл")
        dts_observed.add(self._add_new_years_day(name))
        dts_observed.add(self._add_new_years_day_two(name))

        if self._year >= 2006:
            # Orthodox Christmas.
            self._add_christmas_day(tr("Православиелік Рождество"))

        # International Women's Day.
        dts_observed.add(self._add_womens_day(tr("Халықаралық әйелдер күні")))

        if self._year >= 2002:
            # Nowruz holiday.
            name = tr("Наурыз мейрамы")
            dts_observed.add(self._add_holiday_mar_22(name))
            if self._year >= 2010:
                dts_observed.add(self._add_holiday_mar_21(name))
                dts_observed.add(self._add_holiday_mar_23(name))

        # Kazakhstan's People Solidarity Holiday.
        dts_observed.add(self._add_labor_day(tr("Қазақстан халқының бірлігі мерекесі")))

        if self._year >= 2013:
            # Defender of the Fatherland Day.
            dts_observed.add(self._add_holiday_may_7(tr("Отан Қорғаушы күні")))

        # Victory Day.
        dt = self._add_world_war_two_victory_day(tr("Жеңіс күні"))
        if self._year != 2020:
            dts_observed.add(dt)

        if self._year >= 2009:
            # Capital Day.
            dts_observed.add(self._add_holiday_jul_6(tr("Астана күні")))

        if self._year >= 1996:
            dts_observed.add(
                # Constitution Day.
                self._add_holiday_aug_30(tr("Қазақстан Республикасының Конституциясы күні"))
            )

        if 1994 <= self._year <= 2008 or self._year >= 2022:
            # Republic Day.
            dts_observed.add(self._add_holiday_oct_25(tr("Республика күні")))

        if 2012 <= self._year <= 2021:
            dts_observed.add(
                # First President Day.
                self._add_holiday_dec_1(tr("Қазақстан Республикасының Тұңғыш Президенті күні"))
            )

        # Independence Day.
        name = tr("Тəуелсіздік күні")
        dts_observed.add(self._add_holiday_dec_16(name))
        if 2002 <= self._year <= 2021:
            dts_observed.add(self._add_holiday_dec_17(name))

        if self.observed:
            self._populate_observed(dts_observed)

        if self._year >= 2006:
            # Eid al-Adha.
            self._add_eid_al_adha_day(tr("Құрбан айт"))


class KZ(Kazakhstan):
    pass


class KAZ(Kazakhstan):
    pass


class KazakhstanIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2006: (JAN, 10),
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 27),
        2010: (NOV, 16),
        2011: (NOV, 6),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 21),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
    }


class KazakhstanStaticHolidays:
    # Substituted date format.
    substituted_date_format = tr("%d.%m.%Y")
    # Day off (substituted from %s).
    substituted_label = tr("Демалыс күні (%s бастап ауыстырылды)")

    special_public_holidays = {
        2000: (MAY, 8, MAY, 6),
        2001: (
            (MAR, 9, MAR, 11),
            (MAR, 23, MAR, 25),
            (APR, 30, APR, 28),
            (DEC, 31, DEC, 29),
        ),
        2002: (MAY, 10, MAY, 12),
        2003: (
            (MAY, 2, MAY, 4),
            (DEC, 15, DEC, 13),
        ),
        2005: (
            (MAR, 7, MAR, 5),
            (MAR, 21, MAR, 19),
            (AUG, 29, AUG, 27),
            (OCT, 24, OCT, 22),
        ),
        2006: (
            (JAN, 11, JAN, 14),
            (MAY, 8, MAY, 6),
        ),
        2007: (
            (MAR, 9, MAR, 11),
            (MAR, 23, MAR, 25),
            (AUG, 31, SEP, 2),
            (OCT, 26, OCT, 28),
            (DEC, 31, DEC, 29),
        ),
        2008: (MAY, 2, MAY, 4),
        2009: (DEC, 18, DEC, 20),
        2010: (
            (JAN, 8, JAN, 10),
            (JUL, 5, JUL, 3),
        ),
        2011: (
            (MAR, 7, MAR, 5),
            (AUG, 29, AUG, 27),
        ),
        2012: (
            (MAR, 9, MAR, 11),
            (APR, 30, APR, 28),
            (DEC, 31, DEC, 29),
        ),
        2013: (
            (MAY, 10, MAY, 4),
            (OCT, 14, OCT, 12),
        ),
        2014: (
            (JAN, 3, DEC, 28, 2013),
            (MAY, 2, MAY, 4),
            (MAY, 8, MAY, 11),
        ),
        2016: (MAR, 7, MAR, 5),
        2017: (
            (MAR, 20, MAR, 18),
            (JUL, 7, JUL, 1),
        ),
        2018: (
            (MAR, 9, MAR, 3),
            (APR, 30, APR, 28),
            (MAY, 8, MAY, 5),
            (AUG, 31, AUG, 25),
            (DEC, 31, DEC, 29),
        ),
        2019: (MAY, 10, MAY, 4),
        2020: (
            (JAN, 3, JAN, 5),
            (MAY, 8, MAY, 11),
            (DEC, 18, DEC, 20),
        ),
        2021: (JUL, 5, JUL, 3),
        2022: (
            (MAR, 7, MAR, 5),
            (AUG, 29, AUG, 27),
            (OCT, 24, OCT, 22),
        ),
        2023: (JUL, 7, JUL, 1),
        2024: (MAY, 8, MAY, 4),
    }

    special_public_holidays_observed = {
        2020: (MAY, 8, MAY, 11),
    }
