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
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    THU,
    FRI,
    SAT,
    _timedelta,
)
from holidays.groups import IslamicHolidays
from holidays.holiday_base import HolidayBase


class Oman(HolidayBase, IslamicHolidays):
    """Oman holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Oman>
        * [Independence](https://www.omaninfo.om/pages/175/show/572)
        * [Weekend](https://abnnews.com/the-sultanate-of-oman-changes-weekend-days-from-01-may-2013/)
        * [Decree 56/2020](https://decree.om/2020/rd20200056/)
        * [Decree 88/2022](https://decree.om/2022/rd20220088/)
        * [Decree 15/2025 (National day is moved)](https://decree.om/2025/rd20250015/)
    """

    country = "OM"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("%s (مُقدَّر)")
    start_year = 1970
    supported_languages = ("ar", "en_US")

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        IslamicHolidays.__init__(
            self, cls=OmanIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Oman switches from THU-FRI to FRI-SAT on May 1, 2013.
        self.weekend = {THU, FRI} if self._year <= 2013 else {FRI, SAT}

        if self._year >= 2020:
            # Sultan's Accession Day.
            self._add_holiday_jan_11(tr("اليوم الوطني لتولي السلطان"))

        if self._year <= 2019:
            # Renaissance Day.
            self._add_holiday_jul_23(tr("يوم النهضة"))

        if self._year >= 2020:
            # National Day.
            name = tr("يوم وطني")
            if self._year <= 2024:
                self._add_holiday_nov_18(name)
                self._add_holiday_nov_19(name)
            else:
                self._add_holiday_nov_20(name)
                self._add_holiday_nov_21(name)

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("مولد النبي"))

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("الإسراء والمعراج"))

        # Eid al-Fitr.
        name = tr("عيد الفطر")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)
        for dt in self._add_holiday_29_ramadan(name):
            if _timedelta(dt, +1) not in self:
                self._add_eid_al_fitr_eve(name)

        # Eid al-Adha.
        name = tr("عيد الأضحى")
        self._add_arafah_day(name)
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)


class OM(Oman):
    pass


class OMN(Oman):
    pass


class OmanIslamicHolidays(_CustomIslamicHolidays):
    # https://www.timeanddate.com/holidays/oman/muharram-new-year
    HIJRI_NEW_YEAR_DATES = {
        2018: (SEP, 11),
        2019: (SEP, 1),
        2020: (AUG, 21),
        2021: (AUG, 10),
        2022: (JUL, 30),
        2023: (JUL, 20),
        2024: (JUL, 7),
    }

    # https://www.timeanddate.com/holidays/oman/prophet-birthday
    MAWLID_DATES = {
        2018: (NOV, 20),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 9),
        2023: (SEP, 28),
        2024: (SEP, 15),
    }

    # https://www.timeanddate.com/holidays/oman/isra-miraj
    ISRA_AND_MIRAJ_DATES = {
        2018: (APR, 13),
        2019: (APR, 3),
        2020: (MAR, 22),
        2021: (MAR, 11),
        2022: (MAR, 1),
        2023: (FEB, 19),
        2024: (FEB, 8),
        2025: (JAN, 27),
    }

    # https://www.timeanddate.com/holidays/oman/eid-al-adha
    EID_AL_ADHA_DATES = {
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 17),
    }

    # https://www.timeanddate.com/holidays/oman/eid-al-fitr
    EID_AL_FITR_DATES = {
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    # https://www.timeanddate.com/holidays/oman/ramadan-begins
    RAMADAN_BEGINNING_DATES = {
        2023: (MAR, 23),
        2024: (MAR, 12),
        2025: (MAR, 1),
    }
