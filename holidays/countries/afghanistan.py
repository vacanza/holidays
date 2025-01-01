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
    # Afghanistan's regaining of full independence from British influence.
    start_year = 1919

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1989:
            # Liberation Day.
            self._add_holiday_feb_15(tr("روز آزادی"))

        if self._year <= 1996 or 2001 <= self._year <= 2020:
            # Nowruz.
            self._add_holiday_mar_21(tr("نوروز"))

        if self._year >= 1992:
            # Defeat of Mujahideen Day.
            self._add_holiday_apr_28(tr("روز شکست مجاهدین"))

        if 1968 <= self._year <= 1996 or 2002 <= self._year <= 2021:
            # International Workers' Day.
            self._add_labor_day(tr("روز جهانی کارگر"))

        if 1978 <= self._year <= 1989:
            # Soviet Victory over Afghanistan Day.
            self._add_holiday_may_9(tr("روز پیروزی شوروی"))

        if self._year >= 2022:
            # American Withdrawal Day.
            self._add_holiday_aug_31(tr("روز خروج آمریکایی‌ها"))

        # Afghan Independence Day.
        name = tr("روز استقلال")
        if self._year >= 1974:
            self._add_holiday_jul_17(name)
        else:
            self._add_holiday_aug_19(name)

        if self._year >= 2012:
            # Martyrs' Day.
            self._add_holiday_sep_9(tr("روز شهیدان"))

        if self._year >= 2001:
            # First Day of Eid al-Fitr.
            self._add_eid_al_fitr_day(tr("روز اول عید فطر"))
            # Second Day of Eid al-Fitr.
            self._add_eid_al_fitr_day_two(tr("روز دوم عید فطر"))
            # Third Day of Eid al-Fitr.
            self._add_eid_al_fitr_day_three(tr("سومین روز عید فطر"))

        # Day of Arafah.
        self._add_arafah_day(tr("روز عرفه"))

        # First Day of Eid al-Adha.
        self._add_eid_al_adha_day(tr("اول روز عید قربان"))
        # Second Day of Eid al-Adha.
        self._add_eid_al_adha_day_two(tr("روز دوم عید قربان"))
        # Third Day of Eid al-Adha.
        self._add_eid_al_adha_day_three(tr("سومین روز عید قربان"))

        # Ashura.
        self._add_ashura_day(tr("عاشورا"))

        # First Day of Ramadan.
        self._add_ramadan_beginning_day(tr("اول رمضان"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("میلاد پیامبر"))


class AF(Afghanistan):
    pass


class AFG(Afghanistan):
    pass
