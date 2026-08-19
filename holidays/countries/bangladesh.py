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
from holidays.calendars.gregorian import JAN, MAR, APR, AUG, SEP, FRI, SAT
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class Bangladesh(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Bangladesh holidays.

    References:
        * <https://web.archive.org/web/20241109215908/https://mopa.gov.bd/sites/default/files/files/mopa.gov.bd/public_holiday/61c35b73_e335_462a_9bcf_4695b23b6d82/reg4-2019-212.PDF>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Bangladesh>
        * <https://web.archive.org/web/20260427032339/https://cgbdsydney.gov.bd/about-us/holidays/>
        * <https://web.archive.org/web/20251118113843/https://publicholidays.com.bd/>
        * [2024 Aug 15 cancellation](https://web.archive.org/web/20260509172057/https://mopa.gov.bd/pages/public-holiday/১৫-আগস্ট-এর-সাধারণ-ছুটি-বাতিল-d058d4-694139b3a31054345f0e63ec)
        * [2025](https://web.archive.org/web/20260509170842/https://mopa.gov.bd/pages/public-holiday/২০২৫-খ্রিষ্টাব্দের-ছুটির-তালিকার-প্রজ্ঞাপন-db46da-694139b2a31054345f0e63a5)
        * [2025 Prophet's Birthday](https://web.archive.org/web/20260509171151/https://mopa.gov.bd/pages/public-holiday/পবিত্র-ঈদ-ই-মিলাদুন্নবী-সা-উপলক্ষ্যে-সাধারণ-ছুটির-নির্ধারিত-2540c3-694139b2a31054345f0e6348)
        * [2026](https://web.archive.org/web/20260509164251/https://mopa.gov.bd/pages/public-holiday/২০২৬-খ্রিষ্টাব্দের-ছুটির-তালিকার-প্রজ্ঞাপন-2c48e0-694139b2a31054345f0e6346)
    """

    country = "BD"
    default_language = "bn"
    # %s (estimated).
    estimated_label = tr("%s (আনুমানিক)")

    supported_languages = ("ar", "bn", "en_BD", "en_US")
    weekend = {FRI, SAT}

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.

        In Bangladesh, the dates of the Islamic calendar usually fall a day later than
        the corresponding dates in the Umm al-Qura calendar.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self,
            cls=BangladeshIslamicHolidays,
            show_estimated=islamic_show_estimated,
            calendar_delta_days=+1,
        )
        StaticHolidays.__init__(self, cls=BangladeshStaticHolidays)
        super().__init__(*args, **kwargs)

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

        # Ashura.
        self._add_ashura_day(tr("আশুরা"))

        # Prophet's Birthday.
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
    ASHURA_DATES_CONFIRMED_YEARS = (2022, 2026)

    # https://www.timeanddate.com/holidays/bangladesh/eid-ul-adha-holiday-1
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2022, 2026)

    # https://www.timeanddate.com/holidays/bangladesh/eid-ul-fitr
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2022, 2026)
    EID_AL_FITR_DATES = {
        2024: (APR, 10),
    }

    # https://www.timeanddate.com/holidays/bangladesh/jumatul-bidah
    JUMUATUL_WIDA_DATES_CONFIRMED_YEARS = (2022, 2026)
    JUMUATUL_WIDA_DATES = {
        2023: (APR, 21),
        2026: (MAR, 20),
    }

    # https://www.timeanddate.com/holidays/bangladesh/shab-e-qadr
    LAYLAT_AL_QADR_DATES_CONFIRMED_YEARS = (2022, 2026)

    # https://www.timeanddate.com/holidays/bangladesh/eid-e-milad-un-nabi
    MAWLID_DATES_CONFIRMED_YEARS = (2022, 2026)
    MAWLID_DATES = {
        2025: (SEP, 6),
    }

    # https://www.timeanddate.com/holidays/bangladesh/shab-e-barat
    IMAM_MAHDI_BIRTHDAY_DATES_CONFIRMED_YEARS = (2022, 2026)


class BangladeshStaticHolidays:
    """Bangladesh special holidays.

    References:
        * [2024 Jan 7 Election Day](https://web.archive.org/web/20260509181553/https://mopa.gov.bd/pages/public-holiday/দ্বাদশ-জাতীয়-সংসদ-নির্বাচন-উপলক্ষ্যে-০৭-জানুয়ারি-২০২৪-তারিখ-331623-694139b3a31054345f0e63e8)
        * [2024 Aug 5-7 holidays](https://web.archive.org/web/20260509180928/https://mopa.gov.bd/pages/public-holiday/০৫-আগস্ট-২০২৪-০৬-আগস্ট-২০২৪-ও-০৭-আগস্ট-২০২৪-তারিখ-নির্বাহী-আদেশে-58d844-694139b3a31054345f0e6400)
    """

    # Public Holiday.
    public_holiday_name = tr("সাধারণ ছুটি")

    special_public_holidays = {
        2024: (
            (JAN, 7, public_holiday_name),
            (AUG, 5, public_holiday_name),
            (AUG, 6, public_holiday_name),
            (AUG, 7, public_holiday_name),
        ),
    }
