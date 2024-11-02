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

from holidays.calendars import _CustomChineseHolidays, _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import PUBLIC, WORKDAY
from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class Philippines(
    HolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    """
    Philippines holidays.

    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_the_Philippines
      - `Revised Administrative Code of 1987 <https://www.officialgazette.gov.ph/1987/07/25/executive-order-no-292-book-ichapter-7-regular-holidays-and-nationwide-special-days/>`_
      - `Republic Act No. 9177 <https://www.officialgazette.gov.ph/2002/11/13/republic-act-no-9177/>`_
      - `Republic Act No. 9256 <https://www.officialgazette.gov.ph/2004/02/25/republic-act-no-9256/>`_
      - `Republic Act No. 9492 <https://www.officialgazette.gov.ph/2007/07/24/republic-act-no-9492/>`_
      - `Republic Act No. 9645 <https://www.officialgazette.gov.ph/2009/06/12/republic-act-no-9645/>`_
      - `Republic Act No. 9849 <https://www.officialgazette.gov.ph/2009/12/11/republic-act-no-9849/>`_
      - `Republic Act No. 10966 <https://www.officialgazette.gov.ph/2017/12/28/republic-act-no-10966/>`_
      - `Proclamation No. 944/2020` <https://www.officialgazette.gov.ph/2020/05/19/proclamation-no-944-s-2020/>`_
      - `Proclamation No. 985/2020` <https://www.officialgazette.gov.ph/2020/07/29/proclamation-no-985-s-2020/>`_
      - `Proclamation No. 665/2024` <https://www.officialgazette.gov.ph/2024/08/15/proclamation-no-665-s-2024/>`_
      - `Proclamation No. 729/2024` <https://www.officialgazette.gov.ph/2024/10/30/proclamation-no-729-s-2024/>`_
      - `Nationwide holidays 2018-2025 <https://www.officialgazette.gov.ph/nationwide-holidays/2018/>`_
    """

    country = "PH"
    supported_categories = (PUBLIC, WORKDAY)
    default_language = "en_PH"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    supported_languages = ("en_PH", "en_US", "fil", "th")

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self, cls=PhilippinesChineseHolidays)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=PhilippinesIslamicHolidays)
        StaticHolidays.__init__(self, cls=PhilippinesStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1987:
            return None

        # New Year's Day.
        self._add_new_years_day(tr("New Year's Day"))

        if self._year >= 2012 and self._year != 2023:
            # Chinese New Year.
            self._add_chinese_new_years_day(tr("Chinese New Year"))

        if 2016 <= self._year <= 2023 and self._year != 2017:
            dates_obs = {
                2023: (FEB, 24),
            }
            self._add_holiday(
                # EDSA People Power Revolution Anniversary.
                tr("EDSA People Power Revolution Anniversary"),
                dates_obs.get(self._year, (FEB, 25)),
            )

        # Maundy Thursday.
        self._add_holy_thursday(tr("Maundy Thursday"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 2013:
            # Black Saturday.
            self._add_holy_saturday(tr("Black Saturday"))

        dates_obs = {
            2008: (APR, 7),
            2009: (APR, 6),
            2023: (APR, 10),
        }
        # Day of Valor.
        self._add_holiday(tr("Araw ng Kagitingan"), dates_obs.get(self._year, (APR, 9)))

        # Labor Day.
        self._add_labor_day(tr("Labor Day"))

        dates_obs = {
            2007: (JUN, 11),
            2008: (JUN, 9),
            2010: (JUN, 14),
        }
        # Independence Day.
        self._add_holiday(tr("Independence Day"), dates_obs.get(self._year, (JUN, 12)))

        if self._year >= 2004:
            dates_obs = {
                2007: (AUG, 20),
                2008: (AUG, 18),
                2010: (AUG, 23),
                2024: (AUG, 23),
            }
            # Ninoy Aquino Day.
            self._add_holiday(tr("Ninoy Aquino Day"), dates_obs.get(self._year, (AUG, 21)))

        # National Heroes Day.
        name = tr("National Heroes Day")
        if self._year >= 2007:
            self._add_holiday_last_mon_of_aug(name)
        else:
            self._add_holiday_last_sun_of_aug(name)

        # All Saints' Day.
        self._add_all_saints_day(tr("All Saints' Day"))

        dates_obs = {
            2008: (DEC, 1),
            2010: (NOV, 29),
        }
        # Bonifacio Day.
        self._add_holiday(tr("Bonifacio Day"), dates_obs.get(self._year, (NOV, 30)))

        if self._year >= 2019:
            # Immaculate Conception.
            self._add_immaculate_conception_day(tr("Feast of the Immaculate Conception of Mary"))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        dates_obs = {
            2010: (DEC, 27),
        }
        # Rizal Day.
        self._add_holiday(tr("Rizal Day"), dates_obs.get(self._year, (DEC, 30)))

        if self._year not in {2021, 2022}:
            # New Year's Eve.
            self._add_new_years_eve(tr("Last Day of the Year"))

        if self._year >= 2002:
            # Eid al-Fitr.
            self._add_eid_al_fitr_day(tr("Eid'l Fitr"))

        if self._year >= 2010:
            # Eid al-Adha.
            self._add_eid_al_adha_day(tr("Eid'l Adha"))

    def _populate_workday_holidays(self):
        # Added in 2009, get special non-working day status in 2025:
        if self._year >= 2009 and self._year != 2025:
            # Founding Anniversary of Iglesia ni Cristo.
            self._add_holiday_jul_27(tr("Founding Anniversary of Iglesia ni Cristo"))

        # Added from 2025 onwards as first decreed in
        # https://www.officialgazette.gov.ph/downloads/2024/10oct/20241030-PROC-727-FRM.pdf
        if self._year >= 2025:
            # EDSA People Power Revolution Anniversary.
            self._add_holiday_feb_25(tr("EDSA People Power Revolution Anniversary"))


class PH(Philippines):
    pass


class PHL(Philippines):
    pass


class PhilippinesChineseHolidays(_CustomChineseHolidays):
    LUNAR_NEW_YEAR_DATES = {
        2012: (JAN, 23),
        2013: (FEB, 10),
        2014: (JAN, 31),
        2015: (FEB, 19),
        2016: (FEB, 8),
        2017: (JAN, 28),
        2018: (FEB, 16),
        2019: (FEB, 5),
        2020: (JAN, 25),
        2021: (FEB, 12),
        2022: (FEB, 1),
        2023: (JAN, 22),
        2024: (FEB, 10),
    }


class PhilippinesIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 6),
        2015: (SEP, 25),
        2016: (SEP, 10),
        2017: (SEP, 2),
        2018: (AUG, 21),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 17),
    }

    EID_AL_FITR_DATES = {
        2002: (DEC, 6),
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 12),
        2008: (OCT, 1),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2011: (AUG, 30),
        2012: (AUG, 20),
        2013: (AUG, 9),
        2014: (JUL, 29),
        2015: (JUL, 17),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 25),
        2021: (MAY, 13),
        2022: (MAY, 3),
        2023: (APR, 21),
        2024: (APR, 10),
    }


class PhilippinesStaticHolidays:
    # Additional special (non-working) day.
    additional_special = tr("Additional special (non-working) day")
    # Elections special (non-working) day.
    election_special = tr("Elections special (non-working) day")

    special_public_holidays = {
        2008: (
            (DEC, 26, additional_special),
            (DEC, 29, additional_special),
        ),
        2009: (
            (NOV, 2, additional_special),
            (DEC, 24, additional_special),
        ),
        2010: ((DEC, 24, additional_special),),
        2012: ((NOV, 2, additional_special),),
        2013: (
            (NOV, 2, additional_special),
            (DEC, 24, additional_special),
        ),
        2014: (
            (DEC, 24, additional_special),
            (DEC, 26, additional_special),
        ),
        2015: (
            (JAN, 2, additional_special),
            (DEC, 24, additional_special),
        ),
        2016: (
            (JAN, 2, additional_special),
            (OCT, 31, additional_special),
            (DEC, 24, additional_special),
        ),
        2017: (
            (JAN, 2, additional_special),
            (OCT, 31, additional_special),
        ),
        2018: (
            (MAY, 14, election_special),
            (NOV, 2, additional_special),
            (DEC, 24, additional_special),
        ),
        2019: (
            (MAY, 13, election_special),
            (NOV, 2, additional_special),
            (DEC, 24, additional_special),
        ),
        2020: (
            (NOV, 2, additional_special),
            (DEC, 24, additional_special),
        ),
        2022: (
            (MAY, 9, election_special),
            (OCT, 31, additional_special),
        ),
        2023: (
            (JAN, 2, additional_special),
            (OCT, 30, election_special),
            (NOV, 2, additional_special),
            (DEC, 26, additional_special),
        ),
        2024: (
            (FEB, 9, additional_special),
            (NOV, 2, additional_special),
            (DEC, 24, additional_special),
        ),
        2025: (
            (JUL, 27, additional_special),
            # All Saints' Day Eve.
            (OCT, 31, tr("All Saints' Day Eve")),
            # Christmas Eve.
            (DEC, 24, tr("Christmas Eve")),
        ),
    }
