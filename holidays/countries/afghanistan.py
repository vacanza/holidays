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

from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase


class Afghanistan(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Afghanistan
    https://www.timeanddate.com/holidays/afghanistan/
    """

    country = "AF"
    default_language = "fa"
    supported_languages = ("fa", "ps_AF")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1989:
            self._add_holiday_feb_15(tr("روز آزادی"))  # Liberation Day

        self._add_holiday_mar_21(tr("نوروز"))  # Nowruz

        if 1992 <= self._year <= 1996:
            self._add_holiday_apr_28(tr("روز شکست مجاهدین"))  # Defeat of Mujahideen Day

        if self._year >= 1889:
            self._add_labor_day(tr("روز جهانی کارگر"))  # International Workers' Day

        if 1989 <= self._year <= 2021:
            self._add_holiday_aug_15(tr("روز پیروزی شوروی بر افغانستان"))  # Soviet Victory Day

        if self._year >= 1919:
            self._add_holiday_aug_19(tr("روز استقلال"))  # Afghan Independence Day

        if 2020 <= self._year <= 2021:
            self._add_holiday_aug_31(tr("روز خروج آمریکایی‌ها"))  # American Withdrawal Day

        if self._year >= 2001:
            self._add_holiday_sep_9(tr("روز شهیدان"))  # Martyrs' Day

        if self._year >= 2014:
            self._add_eid_al_fitr_day(tr("عید فطر"))  # Eid al-Fitr

        self._add_arafah_day(tr("روز عرفه"))  # Day of Arafah

        self._add_eid_al_adha_day(tr("عید قربانی"))  # Eid al-Adha

        self._add_ashura_day(tr("عاشورا"))  # Ashura

        self._add_mawlid_day(tr("میلاد پیامبر"))  # Mawlid

        if self._year >= 1800:
            self._add_ramadan_beginning_day(tr("اول رمضان"))  # First Day of Ramadan

        if self._year >= 1900:
            self._add_holiday_mar_20(tr("اعتدال مارس"))  # March Equinox

        if self._year >= 1989:
            self._add_holiday_apr_28(tr("روز پیروزی افغان‌ها"))  # Afghan Victory Day

        if self._year >= 1800:
            self._add_arafah_day(tr("روز عرفه"))  # Day of Arafat

        if self._year >= 1800:
            self._add_isra_and_miraj_day(tr("میلاد پیامبر"))  # The Prophet's Birthday


class AF(Afghanistan):
    pass


class AFG(Afghanistan):
    pass
