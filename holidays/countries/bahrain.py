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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JUN, JUL, AUG, SEP, FRI, SAT
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Bahrain(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Bahrain holidays.

    References:
        * <https://web.archive.org/web/20250415063947/https://www.cbb.gov.bh/official-bank-holidays>
        * Ashura:
            * [2020](https://web.archive.org/web/20200825180619/http://www.gdnonline.com/Details/850724/Crown-Prince-issues-circular-on-Ashura-holiday)
            * [2021](https://web.archive.org/web/20210926225239/https://www.qppstudio.net/publicholidays2021/bahrain.htm)
            * [2022](https://web.archive.org/web/20220817092557/https://pmo.gov.bh/en/article/hrh-the-crown-prince-and-prime-minister-issues-ashura-holiday-circular-2022)
            * [2023](https://web.archive.org/web/20230720172259/https://pmo.gov.bh/en/article/hrh-the-crown-prince-and-prime-minister-issues-ashura-holiday-circular-2023)
            * [2024](https://web.archive.org/web/20250420073702/https://www.timeanddate.com/holidays/bahrain/2024)
            * [2025](https://web.archive.org/web/20250705230332/https://www.cbb.gov.bh/wp-content/uploads/2025/07/Ashoora-Holiday-2025.pdf)
            * [2026](https://www.cbb.gov.bh/wp-content/uploads/2026/06/Ashura-Holiday-2026.pdf)
        * [2026](https://web.archive.org/web/20260517204154/https://www.cbb.gov.bh/official-bank-holidays/)
    """

    country = "BH"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("%s (تقديري)")
    # Independence declared on August 15, 1971.
    start_year = 1972
    supported_languages = ("ar", "en_US", "ur_PK")
    weekend = {FRI, SAT}

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=BahrainIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("رأس السنة الميلادية"))

        # Labor Day.
        self._add_labor_day(tr("عيد العمال"))

        # National Day.
        national_day = tr("العيد الوطني")
        self._add_holiday_dec_16(national_day)
        self._add_holiday_dec_17(national_day)

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # Ashura.
        ashura = tr("عاشوراء")
        self._add_ashura_eve(ashura)
        self._add_ashura_day(ashura)

        # Prophet's Birthday.
        self._add_mawlid_day(tr("المولد النبوي الشريف"))

        # Eid al-Fitr.
        eid_al_fitr = tr("عيد الفطر")
        self._add_eid_al_fitr_day(eid_al_fitr)
        self._add_eid_al_fitr_day_two(eid_al_fitr)
        self._add_eid_al_fitr_day_three(eid_al_fitr)

        # Eid al-Adha.
        eid_al_adha = tr("عيد الأضحى")
        self._add_eid_al_adha_day(eid_al_adha)
        self._add_eid_al_adha_day_two(eid_al_adha)
        self._add_eid_al_adha_day_three(eid_al_adha)


class BH(Bahrain):
    pass


class BAH(Bahrain):
    pass


class BahrainIslamicHolidays(_CustomIslamicHolidays):
    ASHURA_DATES_CONFIRMED_YEARS = (2019, 2026)
    ASHURA_DATES = {
        2019: (SEP, 10),
        2020: (AUG, 30),
        2021: (AUG, 19),
        2022: (AUG, 9),
        2023: (JUL, 29),
        2024: (JUL, 17),
        2025: (JUL, 6),
        2026: (JUN, 26),
    }

    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2019, 2026)
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2019, 2026)
    HIJRI_NEW_YEAR_DATES_CONFIRMED_YEARS = (2019, 2026)
    MAWLID_DATES_CONFIRMED_YEARS = (2019, 2026)
