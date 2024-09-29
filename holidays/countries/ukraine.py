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

from datetime import date
from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR
from holidays.constants import PUBLIC, WORKDAY
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Ukraine(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    Ukraine holidays.

    Current holidays list:
        - https://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454
    """

    country = "UA"
    default_language = "uk"
    # %s (observed).
    observed_label = tr("%s (вихідний)")
    supported_categories = (PUBLIC, WORKDAY)
    supported_languages = ("ar", "en_US", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_REVISED_CALENDAR)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, UkraineStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _is_observed(self, dt: date) -> bool:
        # 27.01.1995: holiday on weekend move to next workday
        # https://zakon.rada.gov.ua/laws/show/35/95-вр
        # 10.01.1998: cancelled
        # https://zakon.rada.gov.ua/laws/show/785/97-вр
        # 23.04.1999: holiday on weekend move to next workday
        # https://zakon.rada.gov.ua/laws/show/576-14
        return date(1995, JAN, 27) <= dt <= date(1998, JAN, 9) or dt >= date(1999, APR, 23)

    def _populate_common(self, is_martial_law: bool = False):
        # The current set of holidays came into force in 1991
        if self._year <= 1990:
            return None

        # There is no public holidays in Ukraine during the period of martial law
        # https://zakon.rada.gov.ua/laws/show/2136-20#n26
        # law is in force from March 15, 2022
        dts_observed = set()

        if (self._year >= 2023) == is_martial_law:
            # New Year's Day.
            dts_observed.add(self._add_new_years_day(tr("Новий рік")))

            if self._year <= 2023:
                # Christmas Day.
                dts_observed.add(self._add_christmas_day(tr("Різдво Христове"), JULIAN_CALENDAR))

            # International Women's Day.
            dts_observed.add(self._add_womens_day(tr("Міжнародний жіночий день")))

        if (self._year >= 2022) == is_martial_law:
            if self._year >= 1992:
                # Easter Sunday (Pascha).
                dts_observed.add(self._add_easter_sunday(tr("Великдень (Пасха)")))

            # Holy Trinity Day.
            dts_observed.add(self._add_whit_sunday(tr("Трійця")))

            name = (
                # Labor Day.
                tr("День праці")
                if self._year >= 2018
                # International Workers' Solidarity Day.
                else tr("День міжнародної солідарності трудящих")
            )
            dts_observed.add(self._add_labor_day(name))
            if self._year <= 2017:
                dts_observed.add(self._add_labor_day_two(name))

            name = (
                # Day of Remembrance and Victory over Nazism in World War II 1939-1945.
                tr("День памʼяті та перемоги над нацизмом у Другій світовій війні 1939-1945 років")
                if self._year >= 2024
                # Day of Victory over Nazism in World War II (Victory Day).
                else tr("День перемоги над нацизмом у Другій світовій війні (День перемоги)")
                if self._year >= 2016
                # Victory Day.
                else tr("День перемоги")
            )
            dts_observed.add(
                self._add_holiday_may_8(name)
                if self._year >= 2024
                else self._add_world_war_two_victory_day(name)
            )

            if self._year >= 1997:
                # Day of the Constitution of Ukraine.
                dts_observed.add(self._add_holiday_jun_28(tr("День Конституції України")))

            if self._year >= 2022:
                # Ukrainian Statehood Day.
                name = tr("День Української Державності")
                dts_observed.add(
                    self._add_holiday_jul_15(name)
                    if self._year >= 2024
                    else self._add_holiday_jul_28(name)
                )

            # Independence Day.
            name = tr("День незалежності України")
            if self._year >= 1992:
                dts_observed.add(self._add_holiday_aug_24(name))
            else:
                self._add_holiday_jul_16(name)

            if self._year >= 2015:
                name = (
                    # Day of defenders of Ukraine.
                    tr("День захисників і захисниць України")
                    if self._year >= 2021
                    # Defender of Ukraine Day.
                    else tr("День захисника України")
                )
                dts_observed.add(
                    self._add_holiday_oct_1(name)
                    if self._year >= 2023
                    else self._add_holiday_oct_14(name)
                )

            if self._year <= 1999:
                # Anniversary of the Great October Socialist Revolution.
                name = tr("Річниця Великої Жовтневої соціалістичної революції")
                dts_observed.add(self._add_holiday_nov_7(name))
                dts_observed.add(self._add_holiday_nov_8(name))

            if self._year >= 2017:
                # Christmas Day.
                dts_observed.add(self._add_christmas_day(tr("Різдво Христове")))

        if self.observed and not is_martial_law:
            self._populate_observed(dts_observed)

    def _populate_public_holidays(self):
        self._populate_common()

    def _populate_workday_holidays(self):
        self._populate_common(is_martial_law=True)


class UA(Ukraine):
    pass


class UKR(Ukraine):
    pass


class UkraineStaticHolidays:
    """
        Substituted holidays:
            - `1992 [1] <https://zakon.rada.gov.ua/laws/show/202-92-%D0%BF>`_
            - `1992 [2] <https://zakon.rada.gov.ua/laws/show/377-91-%D0%BF>`_
            - `1993 [1] <https://zakon.rada.gov.ua/laws/show/563-93-%D0%BF>`_
            - `1993 [2] <https://zakon.rada.gov.ua/laws/show/725-92-%D0%BF>`_
            - `1994 <https://zakon.rada.gov.ua/laws/show/98-94-%D0%BF>`_
            - `1995 [1] <https://zakon.rada.gov.ua/laws/show/852-95-%D0%BF>`_
            - `1995 [2] <https://zakon.rada.gov.ua/laws/show/634-95-%D0%BF>`_
            - `1995 [3] <https://zakon.rada.gov.ua/laws/show/266-95-%D0%BF>`_
            - `1996 <https://zakon.rada.gov.ua/laws/show/424-96-%D0%BF>`_
            - `1997[1] <https://zakon.rada.gov.ua/laws/show/326-97-%D0%BF>`_
            - `1997[2] <https://zakon.rada.gov.ua/laws/show/1547-96-%D0%BF>`_
            - `1999 [1] <https://zakon.rada.gov.ua/laws/show/1433-99-%D0%BF>`_,
            - `1999 [2] <https://zakon.rada.gov.ua/laws/show/558-99-%D0%BF>`_,
            - `1999 [3] <https://zakon.rada.gov.ua/laws/show/2070-98-%D0%BF>`_
            - `2000 [1] <https://zakon.rada.gov.ua/laws/show/1251-2000-%D0%BF>`_
            - `2000 [2] <https://zakon.rada.gov.ua/laws/show/717-2000-%D0%BF>`_
            - `2001 [1] <https://zakon.rada.gov.ua/laws/show/138-2001-%D1%80>`_
            - `2001 [2] <https://zakon.rada.gov.ua/laws/show/210-2001-%D0%BF>`_
            - `2002 <https://zakon.rada.gov.ua/laws/show/202-2002-%D1%80>`_
            - `2002 - 2003 <https:/zakon.rada.gov.ua/laws/show/705-2002-%D1%80>`_
            - `2004 <https://zakon.rada.gov.ua/laws/show/773-2003-%D1%80>`_
            - `2005 [1] <https://zakon.rada.gov.ua/laws/show/936-2004-%D1%80>`_
            - `2005 [2] <https://zakon.rada.gov.ua/laws/show/133-2005-%D1%80>`_
            - `2006 [1] <https://zakon.rada.gov.ua/laws/show/490-2005-%D1%80>`_
            - `2006 [2] <https://zakon.rada.gov.ua/laws/show/562-2005-%D1%80>`_
            - `2007 <https://zakon.rada.gov.ua/laws/show/612-2006-%D1%80>`_
            - `2008 [1] <https://zakon.rada.gov.ua/laws/show/1059-2007-%D1%80>`_
            - `2008 [2] <https://zakon.rada.gov.ua/laws/show/538-2008-%D1%80>`_
            - `2009 <https://zakon.rada.gov.ua/laws/show/1458-2008-%D1%80>`_
            - `2010 <https://zakon.rada.gov.ua/laws/show/1412-2009-%D1%80>`_
            - `2011 <https://zakon.rada.gov.ua/laws/show/2130-2010-%D1%80>`_
            - `2012 <https://zakon.rada.gov.ua/laws/show/1210-2011-%D1%80>`_
            - `2013 <https://zakon.rada.gov.ua/laws/show/1043-2012-%D1%80>`_
            - `2014 <https://zakon.rada.gov.ua/laws/show/920-2013-%D1%80>`_
            - `2015 <https://zakon.rada.gov.ua/laws/show/1084-2014-%D1%80>`_
            - `2016 <https://zakon.rada.gov.ua/laws/show/1155-2015-%D1%80>`_
            - `2017 <https://zakon.rada.gov.ua/laws/show/850-2016-%D1%80>`_
            - `2018 <https://zakon.rada.gov.ua/laws/show/1-2018-%D1%80>`_
            - `2019 <https://zakon.rada.gov.ua/laws/show/7-2019-%D1%80>`_
            - `2020 <https://zakon.rada.gov.ua/laws/show/995-2019-%D1%80>`_
            - `2021 <https://zakon.rada.gov.ua/laws/show/1191-2020-%D1%80>`_
            - `2022 <https://zakon.rada.gov.ua/laws/show/1004-2021-%D1%80>`_

    Special holidays:
        - `1995 <https://zakon.rada.gov.ua/laws/show/13/95>`_
    """

    # Date format (see strftime() Format Codes)
    substituted_date_format = tr("%d.%m.%Y")
    # Day off (substituted from %s).
    substituted_label = tr("Вихідний день (перенесено з %s)")
    special_public_holidays = {
        1992: (
            (JAN, 6, JAN, 4),
            (APR, 27, MAY, 16),
        ),
        1993: (
            (JAN, 8, JAN, 10),
            (AUG, 23, AUG, 21),
        ),
        1994: (MAR, 7, MAR, 5),
        1995: (
            # Presidential decree holiday.
            (JAN, 9, tr("Вихідний згідно указу Президента")),
            (MAY, 8, MAY, 6),
            (AUG, 25, AUG, 27),
            (NOV, 6, NOV, 4),
        ),
        1996: (
            (MAY, 3, MAY, 5),
            (MAY, 10, MAY, 12),
        ),
        1997: (
            (JAN, 2, DEC, 28, 1996),
            (JAN, 6, JAN, 4),
            (APR, 29, APR, 19),
            (APR, 30, MAY, 17),
        ),
        1999: (
            (JAN, 8, JAN, 10),
            (APR, 12, APR, 24),
            (AUG, 23, AUG, 21),
        ),
        2000: (
            (MAY, 8, MAY, 6),
            (AUG, 25, AUG, 27),
        ),
        2001: (
            (MAR, 9, MAR, 11),
            (APR, 30, APR, 28),
            (MAY, 10, MAY, 5),
            (MAY, 11, MAY, 6),
            (JUN, 29, JUN, 23),
            (DEC, 31, DEC, 29),
        ),
        2002: (
            (MAY, 3, MAY, 11),
            (DEC, 30, DEC, 28),
            (DEC, 31, DEC, 29),
        ),
        2003: (JAN, 6, JAN, 4),
        2004: (
            (JAN, 2, JAN, 10),
            (JAN, 5, JAN, 17),
            (JAN, 6, JAN, 31),
            (AUG, 23, AUG, 21),
        ),
        2005: (
            (MAR, 7, MAR, 5),
            (MAY, 10, MAY, 14),
            (JUN, 27, JUN, 25),
        ),
        2006: (
            (JAN, 3, JAN, 21),
            (JAN, 4, FEB, 4),
            (JAN, 5, FEB, 18),
            (JAN, 6, MAR, 11),
            (MAY, 8, MAY, 6),
            (AUG, 25, SEP, 9),
        ),
        2007: (
            (JAN, 2, JAN, 20),
            (JAN, 3, JAN, 27),
            (JAN, 4, FEB, 10),
            (JAN, 5, FEB, 24),
            (MAR, 9, MAR, 3),
            (APR, 30, APR, 28),
            (JUN, 29, JUN, 16),
            (DEC, 31, DEC, 29),
        ),
        2008: (
            (JAN, 2, JAN, 12),
            (JAN, 3, JAN, 26),
            (JAN, 4, FEB, 9),
            (APR, 29, MAY, 17),
            (APR, 30, MAY, 31),
        ),
        2009: (
            (JAN, 2, JAN, 10),
            (JAN, 5, JAN, 24),
            (JAN, 6, FEB, 7),
        ),
        2010: (
            (JAN, 4, JAN, 30),
            (JAN, 5, FEB, 13),
            (JAN, 6, FEB, 27),
            (JAN, 8, MAR, 13),
            (AUG, 23, AUG, 21),
        ),
        2011: (
            (MAR, 7, MAR, 12),
            (JUN, 27, JUN, 25),
        ),
        2012: (
            (MAR, 9, MAR, 3),
            (APR, 20, APR, 28),
            (JUN, 29, JUL, 7),
            (DEC, 31, DEC, 29),
        ),
        2013: (
            (MAY, 3, MAY, 18),
            (MAY, 10, JUN, 1),
        ),
        2014: (
            (JAN, 2, JAN, 11),
            (JAN, 3, JAN, 25),
            (JAN, 6, FEB, 8),
        ),
        2015: (
            (JAN, 2, JAN, 17),
            (JAN, 8, JAN, 31),
            (JAN, 9, FEB, 14),
        ),
        2016: (
            (JAN, 8, JAN, 16),
            (MAR, 7, MAR, 12),
            (JUN, 27, JUL, 2),
        ),
        2017: (
            (MAY, 8, MAY, 13),
            (AUG, 25, AUG, 19),
        ),
        2018: (
            (MAR, 9, MAR, 3),
            (APR, 30, MAY, 5),
            (JUN, 29, JUN, 23),
            (DEC, 24, DEC, 22),
            (DEC, 31, DEC, 29),
        ),
        2019: (
            (APR, 30, MAY, 11),
            (DEC, 30, DEC, 21),
            (DEC, 31, DEC, 28),
        ),
        2020: (JAN, 6, JAN, 11),
        2021: (
            (JAN, 8, JAN, 16),
            (AUG, 23, AUG, 28),
            (OCT, 15, OCT, 23),
        ),
        2022: (MAR, 7, MAR, 12),
    }
