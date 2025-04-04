#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import FRI, SAT, MAY, JUL, AUG, OCT
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Bahrain(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Bahrain holidays.

    References:
        * <https://www.cbb.gov.bh/official-bank-holidays/>
        * <https://www.officeholidays.com/countries/bahrain/>
    """

    country = "BH"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("(تقدير) %s")
    supported_languages = ("ar", "en_US")
    weekend = {FRI, SAT}

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
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

        # Eid al-Fitr.
        eid_al_fitr = tr("عيد الفطر")
        self._add_eid_al_fitr_day(eid_al_fitr)
        self._add_eid_al_fitr_day_two(tr("عطلة عيد الفطر"))
        # Eid al-Fitr Holiday.
        self._add_eid_al_fitr_day_three(tr("عطلة عيد الفطر"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("عيد الأضحى"))
        # Eid al-Adha Holiday.
        self._add_eid_al_adha_day_two(tr("عطلة عيد الأضحى"))
        self._add_eid_al_adha_day_three(tr("عطلة عيد الأضحى"))

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # Ashura Eve.
        self._add_ashura_eve(tr("ليلة عاشورة"))
        # Ashura.
        self._add_ashura_day(tr("عاشورة"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("عيد المولد النبوي"))

        # National Day.
        national_day = tr("اليوم الوطني")
        self._add_holiday_dec_16(national_day)
        self._add_holiday_dec_17(national_day)


class BH(Bahrain):
    pass


class BAH(Bahrain):
    pass


class BahrainIslamicHolidays(_CustomIslamicHolidays):
    ASHURA_DATES = {
        2022: (AUG, 8),
    }

    EID_AL_ADHA = {
        2022: (JUL, 9),
    }

    EID_AL_FITR_DATES = {
        2022: (MAY, 2),
    }

    HIJRI_NEW_YEAR_DATES = {
        2022: (JUL, 30),
    }

    MAWLID_DATES = {
        2022: (OCT, 8),
    }
