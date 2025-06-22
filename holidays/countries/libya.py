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
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Libya(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Libya holidays.

    References:
        * [Law No. 5 of 2012](https://web.archive.org/web/20250505012423/https://security-legislation.ly/wp-content/uploads/2021/07/57-Law-No.-5-of-2012_ORG.pdf)
    """

    country = "LY"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("(تقدير) %s")
    start_year = 2012
    supported_languages = ("ar", "en_US")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=LibyaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Anniversary of the February 17 Revolution.
        self._add_holiday_feb_17(tr("ثورة 17 فبراير"))

        # Labor Day.
        self._add_labor_day(tr("عيد العمال"))

        # Martyrs' Day.
        self._add_holiday_sep_16(tr("يوم الشهيد"))

        # Liberation Day.
        self._add_holiday_oct_23(tr("يوم التحرير"))

        # Independence Day.
        self._add_holiday_dec_24(tr("عيد الاستقلال"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("ذكرى المولد النبوي الشريف"))

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("ليلة المعراج"))

        # Eid al-Fitr.
        name = tr("عيد الفطر")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Day of Arafah.
        self._add_arafah_day(tr("يوم عرفة"))

        # Eid al-Adha.
        name = tr("عيد الأضحى")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)


class LY(Libya):
    pass


class LBY(Libya):
    pass


class LibyaIslamicHolidays(_CustomIslamicHolidays):
    # https://web.archive.org/web/20240908234803/https://www.timeanddate.com/holidays/libya/eid-al-adha
    EID_AL_ADHA_DATES = {
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 23),
        2016: (SEP, 11),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 6),
    }

    # https://web.archive.org/web/20241012125707/https://www.timeanddate.com/holidays/libya/eid-al-fitr
    EID_AL_FITR_DATES = {
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    # https://web.archive.org/web/20241213175353/https://www.timeanddate.com/holidays/libya/prophet-birthday
    MAWLID_DATES = {
        2012: (FEB, 5),
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 23)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 15),
    }
