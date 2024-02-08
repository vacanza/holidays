#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, FRI, SAT
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class UnitedArabEmirates(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Holidays are regulated by the Article 74 of Federal Law No. 08 for the year 1980:
    https://www.ilo.org/dyn/natlex/docs/ELECTRONIC/11956/69376/F417089305/ARE11956.pdf
    However the law is not applied literally, and was amended often in the past few years.
    Sources:
    2017: https://www.khaleejtimes.com/nation/uae-official-public-holidays-list-2017
    2018: https://www.thenational.ae/uae/government/uae-public-holidays-2018-announced-by-abu-dhabi-government-1.691393  # noqa: E501
    2019: https://www.thenational.ae/uae/government/uae-public-holidays-for-2019-and-2020-announced-by-cabinet-1.833425  # noqa: E501
    2020: https://u.ae/en/information-and-services/public-holidays-and-religious-affairs/public-holidays  # noqa: E501
    """

    country = "AE"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("(تقدير) %s")
    supported_languages = ("ar", "en_US")
    weekend = {FRI, SAT}

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=UnitedArabEmiratesIslamicHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("رأس السنة الميلادية"))

        if 2015 <= self._year <= 2022:
            # Commemoration Day.
            name = tr("يوم الشهيد")
            if self._year >= 2019:
                self._add_holiday_dec_1(name)
            else:
                self._add_holiday_nov_30(name)

        # National Day.
        national_day = tr("اليوم الوطني")
        self._add_holiday_dec_2(national_day)
        self._add_holiday_dec_3(national_day)

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("عيد الفطر"))

        # Eid al-Fitr Holiday.
        eid_al_fitr_holiday = tr("عطلة عيد الفطر")
        self._add_eid_al_fitr_day_two(eid_al_fitr_holiday)
        self._add_eid_al_fitr_day_three(eid_al_fitr_holiday)
        if self._year >= 2019:
            self._add_eid_al_fitr_eve(eid_al_fitr_holiday)

        # Arafat Day.
        self._add_arafah_day(tr("وقفة عرفة"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("عيد الأضحى"))

        # Eid al-Adha Holiday.
        eid_al_adha_holiday = tr("عطلة عيد الأضحى")
        self._add_eid_al_adha_day_two(eid_al_adha_holiday)
        self._add_eid_al_adha_day_three(eid_al_adha_holiday)

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        if self._year <= 2018:
            # Isra' and Mi'raj.
            self._add_isra_and_miraj_day(tr("ليلة المعراج"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("عيد المولد النبوي"))


class AE(UnitedArabEmirates):
    pass


class ARE(UnitedArabEmirates):
    pass


class UnitedArabEmiratesIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2017: (SEP, 1),
        2018: (AUG, 21),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
    }

    EID_AL_FITR_DATES = {
        2017: (JUN, 25),
        2018: (JUN, 14),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
    }

    HIJRI_NEW_YEAR_DATES = {
        2017: (SEP, 22),
        2018: (SEP, 11),
        2019: (AUG, 31),
        2020: (AUG, 23),
        2021: (AUG, 12),
        2022: (JUL, 30),
        2023: (JUL, 21),
    }

    ISRA_AND_MIRAJ_DATES = {
        2017: (APR, 23),
        2018: (APR, 13),
    }

    MAWLID_DATES = {
        2017: (NOV, 30),
        2018: (NOV, 19),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 21),
        2022: (OCT, 8),
        2023: (SEP, 29),
    }
