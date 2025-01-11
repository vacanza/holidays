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
from holidays.calendars.gregorian import (
    JAN,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    FRI,
    SAT,
)
from holidays.groups import InternationalHolidays, IslamicHolidays, PersianCalendarHolidays
from holidays.holiday_base import HolidayBase


class Afghanistan(HolidayBase, InternationalHolidays, IslamicHolidays, PersianCalendarHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Afghanistan
    https://www.timeanddate.com/holidays/afghanistan/
    https://en.wikipedia.org/wiki/Workweek_and_weekend
    """

    country = "AF"
    default_language = "fa_AF"
    # %s (estimated).
    estimated_label = tr("%s (برآورد شده)")
    supported_languages = ("en_US", "fa_AF", "ps_AF")
    # Afghanistan's regaining of full independence from British influence.
    start_year = 1919
    weekend = {FRI, SAT}

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, AfghanistanIslamicHolidays)
        PersianCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1989:
            # Liberation Day.
            self._add_holiday_feb_15(tr("روز آزادی"))

        # Afghanistan Independence Day.
        self._add_holiday_aug_19(tr("روز استقلال افغانستان"))

        if self._year <= 1996 or 2001 <= self._year <= 2020:
            # Nowruz.
            self._add_nowruz_day(tr("نوروز"))

        if self._year >= 1992:
            # Mojahedin's Victory Day.
            self._add_holiday_apr_28(tr("روز پیروزی مجاهدین"))

        if 1974 <= self._year <= 1996 or 2002 <= self._year <= 2021:
            # International Workers' Day.
            self._add_labor_day(tr("روز جهانی کارگر"))

        if 1978 <= self._year <= 1988:
            # Soviet Victory Day.
            self._add_holiday_may_9(tr("روز پیروزی شوروی"))

        if self._year >= 2022:
            # Islamic Emirate Victory Day.
            self._add_islamic_emirat_victory_day(tr("روز پیروزی امارت اسلامی"))

            # American Withdrawal Day.
            self._add_holiday_aug_31(tr("روز خروج آمریکایی ها"))

        if 2012 <= self._year <= 2020:
            # Martyrs' Day.
            self._add_holiday_sep_9(tr("روز شهیدان"))

        if self._year <= 2021:
            # Ashura.
            self._add_ashura_day(tr("عاشورا"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("میلاد پیامبر"))

        # First Day of Ramadan.
        self._add_ramadan_beginning_day(tr("اول رمضان"))

        # Eid al-Fitr.
        name = tr("عید فطر")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Day of Arafah.
        self._add_arafah_day(tr("روز عرفه"))

        # Eid al-Adha.
        name = tr("عید قربانی")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)


class AF(Afghanistan):
    pass


class AFG(Afghanistan):
    pass


class AfghanistanIslamicHolidays(_CustomIslamicHolidays):
    ASHURA_DATES = {
        2014: (NOV, 3),
        2015: (OCT, 24),
        2016: (OCT, 12),
        2017: (OCT, 1),
        2018: (SEP, 21),
        2019: (SEP, 10),
        2020: (AUG, 30),
        2021: (AUG, 19),
    }

    EID_AL_ADHA_DATES = {
        2014: (OCT, 5),
        2015: (SEP, 23),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 17),
    }

    EID_AL_FITR_DATES = {
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 1),
        2023: (APR, 22),
        2024: (APR, 10),
    }

    MAWLID_DATES = {
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 16),
    }

    RAMADAN_BEGINNING_DATES = {
        2014: (JUN, 29),
        2015: (JUN, 18),
        2016: (JUN, 7),
        2017: (MAY, 27),
        2018: (MAY, 16),
        2019: (MAY, 6),
        2020: (APR, 24),
        2021: (APR, 13),
        2022: (APR, 2),
        2023: (MAR, 23),
        2024: (MAR, 11),
    }
