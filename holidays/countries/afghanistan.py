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

from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Afghanistan(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Afghanistan
    https://www.timeanddate.com/holidays/afghanistan/
    """

    country = "AF"
    default_language = "fa"
    # %s (estimated).
    estimated_label = tr("%s (برآورد شده)")
    # %s (observed).
    observed_label = tr("%s (مشاهده شده)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (مشاهده شده، برآورد شده)")
    supported_languages = ("en_US", "fa", "ps_AF")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1989:
            self._add_holiday_feb_15(tr("روز آزادی"))  # Liberation Day

        if self._year < 1996 or 2001 <= self._year <= 2020:
            self._add_holiday_mar_21(tr("نوروز"))  # Nowruz

        if self._year >= 1992:
            self._add_holiday_apr_28(tr("روز شکست مجاهدین"))  # Defeat of Mujahideen Day

        if 1889 <= self._year <= 1996 or 2002 <= self._year <= 2021:
            self._add_labor_day(tr("روز جهانی کارگر"))  # International Workers' Day

        if 1978 <= self._year <= 1989:
            self._add_holiday_may_9(tr("روز پیروزی شوروی"))  # Soviet Victory Day

        if self._year >= 2022:
            self._add_holiday_aug_31(tr("روز خروج آمریکایی‌ها"))  # American Withdrawal Day

        if 1919 <= self._year <= 1973:
            self._add_holiday_aug_19(tr("روز استقلال"))  # Afghan Independence Day
        if self._year > 1973:
            self._add_holiday_jul_17(tr("روز استقلال"))  # Afghan Independence Day

        if self._year >= 2012:
            self._add_holiday_sep_9(tr("روز شهیدان"))  # Martyrs' Day

        if self._year >= 2001:
            self._add_eid_al_fitr_day(tr("روز اول عید فطر"))  # The first day of Eid al-Fitr
            self._add_eid_al_fitr_day_two(tr("روز دوم عید فطر"))  # The second day of Eid al-Fitr
            self._add_eid_al_fitr_day_three(
                tr("سومین روز عید فطر")
            )  # The third day of Eid al-Fitr

        self._add_arafah_day(tr("روز عرفه"))  # Day of Arafah

        self._add_eid_al_adha_day(tr("اول روز عید قربان"))  # The first day of Eid al-Adha
        self._add_eid_al_adha_day_two(tr("روز دوم عید قربان"))  # The second day of Eid al-Adha
        self._add_eid_al_adha_day_three(tr("سومین روز عید قربان"))  # The third day of Eid al-Adha

        self._add_ashura_day(tr("عاشورا"))  # Ashura

        self._add_mawlid_day(tr("میلاد پیامبر"))  # Mawlid

        self._add_ramadan_beginning_day(tr("اول رمضان"))  # First Day of Ramadan

        self._add_mawlid_day(tr("میلاد پیامبر"))  # The Prophet's Birthday


class AF(Afghanistan):
    pass


class AFG(Afghanistan):
    pass
