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

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import (
    APR,
    AUG,
    FEB,
    FRI,
    JUN,
    JUL,
    MAR,
    MAY,
    SAT,
    SEP,
    OCT,
)
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Bangladesh(HolidayBase, InternationalHolidays, ChristianHolidays, IslamicHolidays):
    """Bangladesh holidays.

    References:
        * <https://web.archive.org/web/20241109215908/https://mopa.gov.bd/sites/default/files/files/mopa.gov.bd/public_holiday/61c35b73_e335_462a_9bcf_4695b23b6d82/reg4-2019-212.PDF>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Bangladesh>
        * <https://cgbdsydney.gov.bd/about-us/holidays/>
        * <https://publicholidays.com.bd/>
    """

    country = "BD"
    default_language = "bn"
    # %s (estimated).
    estimated_label = tr("%s (আনুমানিক)")

    supported_languages = ("ar", "bn", "en_US")
    weekend = {FRI, SAT}

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        InternationalHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=BangladeshIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _add_mid_shaban_day(self, name):
        # Mid-Sha'ban Day.
        return self._add_islamic_calendar_holiday_set(
            name, self._islamic_calendar._get_holiday("MID_SHABAN", self._year)
        )

    def _add_jumuatul_wida(self, name):
        # Jumu'atul-Wida is the last Friday of Ramadan.
        return self._add_islamic_calendar_holiday_set(
            name, self._islamic_calendar._get_holiday("JUMATUL_WIDA", self._year)
        )

    def _populate_public_holidays(self):
        # Martyrs' Day and International Mother Language Day.
        self._add_holiday_feb_21(tr("শহীদ দিবস ও আন্তর্জাতিক মাতৃভাষা দিবস"))

        if self._year <= 2024:
            # Sheikh Mujibur Rahman's Birthday.
            self._add_holiday_mar_17(tr("জাতির পিতা বঙ্গবন্ধু শেখ মুজিবুর রহমান এর জন্মদিবস"))

        # Independence Day.
        self._add_holiday_mar_26(tr("স্বাধীনতা দিবস"))

        # Bengali New Year's Day.
        self._add_holiday_apr_14(tr("পহেলা বৈশাখ"))

        # May Day.
        self._add_labor_day(tr("মে দিবস"))

        if self._year >= 2025:
            # July Mass Uprising Day.
            self._add_holiday_aug_5(tr("জুলাই গণ-অভ্যুত্থান দিবস"))

        if self._year <= 2024:
            # National Mourning Day.
            self._add_holiday_aug_15(tr("জাতীয় শোক দিবস"))

        # Victory Day.
        self._add_holiday_dec_16(tr("বিজয় দিবস"))

        # Christmas Day.
        self._add_christmas_day(tr("বড়দিন"))

        # Ashura Day.
        self._add_ashura_day(tr("আশুরা"))

        # Eid-e-Milad un-Nabi.
        self._add_mawlid_day(tr("ঈদে মিলাদুন্নবী"))

        # Mid-Sha'ban.
        self._add_mid_shaban_day(tr("শবে বরাত"))

        # Laylat al-Qadr.
        self._add_laylat_al_qadr_day(tr("শবে কদর"))

        # Jumu'atul-Wida.
        self._add_jumuatul_wida(tr("জুমাতুল বিদা"))

        # Eid al-Fitr.
        name = tr("ঈদুল ফিতর")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("ঈদুল আজহা")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)


class BD(Bangladesh):
    pass


class BGD(Bangladesh):
    pass


class BangladeshIslamicHolidays(_CustomIslamicHolidays):
    # https://www.timeanddate.com/holidays/bangladesh/ashura
    ASHURA_DATES_CONFIRMED_YEARS = (2022, 2025)
    ASHURA_DATES = {
        2022: (AUG, 9),
        2023: (JUL, 29),
        2024: (JUL, 17),
        2025: (JUL, 6),
    }

    # https://www.timeanddate.com/holidays/bangladesh/eid-ul-adha-holiday-1
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2022, 2025)
    EID_AL_ADHA_DATES = {
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    # https://www.timeanddate.com/holidays/bangladesh/eid-ul-fitr
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2022, 2025)
    EID_AL_FITR_DATES = {
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    # https://www.timeanddate.com/holidays/bangladesh/jumatul-bidah
    JUMATUL_WIDA_DATES_CONFIRMED_YEARS = (2022, 2026)
    JUMATUL_WIDA_DATES = {
        2022: (APR, 29),
        2023: (APR, 21),
        2024: (APR, 5),
        2025: (),
        2026: (MAR, 20),
    }

    # https://www.timeanddate.com/holidays/bangladesh/shab-e-qadr
    LAYLAT_AL_QADR_DATES_CONFIRMED_YEARS = (2022, 2025)
    LAYLAT_AL_QADR_DATES = {
        2022: (APR, 29),
        2023: (APR, 19),
        2024: (APR, 7),
        2025: (MAR, 28),
    }

    # https://www.timeanddate.com/holidays/bangladesh/eid-e-milad-un-nabi
    MAWLID_DATES_CONFIRMED_YEARS = (2022, 2025)
    MAWLID_DATES = {
        2022: (OCT, 9),
        2023: (SEP, 28),
        2024: (SEP, 16),
        2025: (SEP, 6),
    }

    # https://www.timeanddate.com/holidays/bangladesh/shab-e-barat
    MID_SHABAN_DATES_CONFIRMED_YEARS = (2022, 2025)
    MID_SHABAN_DATES = {
        2022: (MAR, 19),
        2023: (MAR, 8),
        2024: (FEB, 26),
        2025: (FEB, 15),
    }
