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

#  holidays
#  --------
#  Rwanda holidays.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           prateekshit.jaiswal (c) 2024
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Rwanda(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Rwanda holidays.
    References:
        - https://www.timeanddate.com/holidays/rwanda/
        - https://en.wikipedia.org/wiki/Public_holidays_in_Rwanda
        - https://web.archive.org/web/20220626143357/https://www.ngoma.gov.rw/index.php?eID=dumpFile&t=f&f=44336&token=fc82c76109af7950f8895d40ddd3e15bd8c57e8c
    """

    country = "RW"
    default_language = "rw"
    supported_languages = ("en_US", "fr", "rw")
    # Official Gazette nᵒ11 of 13/03/2017.
    start_year = 2018
    # %s (observed).
    observed_label = tr("%s (observed)")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=EritreaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("Ubunani")))

        # Day after New Year's Day.
        self._add_observed(self._add_holiday_jan_2(tr("Umunsi ukurikira Ubunani")))

        # National Heroes' Day.
        self._add_holiday_feb_1(tr("Umunsi w'Intwari"))

        # Genocide perpetrated against the Tutsi Memorial Day.
        self._add_holiday_apr_7(tr("Umunsi wo Kwibuka Jenoside yakorewe Abatutsi"))

        # Good Friday.
        self._add_good_friday(tr("Umunsi wa Gatanu Mutagatifu"))

        # Easter Monday.
        self._add_easter_monday(tr("Ku wa mbere wa Pasika"))

        # Labour Day.
        self._add_labor_day(tr("Umunsi Mukuru w'Umurimo"))

        # EID EL FITR.
        self._add_eid_al_fitr_day(tr("EID EL FITR"))

        # EID AL-ADHA.
        self._add_eid_al_adha_day(tr("EID AL-ADHA"))

        # Independence Day.
        self._add_holiday_jul_1(tr("Umunsi w'Ubwigenge"))

        # Liberation Day.
        self._add_holiday_jul_4(tr("Umunsi wo Kwibohora"))

        # Umuganura Day.
        self._add_holiday_aug_6(tr("Umunsi w'Umuganura"))

        # Assumption Day.
        self._add_holiday_aug_15(tr("Ijyanwa mu Ijuru rya Bikiramariya"))

        # Christmas Day.
        self._add_christmas_day(tr("Noheli"))

        # Boxing Day.
        self._add_christmas_day_two(tr("Umunsi ukurikira Noheli"))


class RW(Rwanda):
    pass


class RWA(Rwanda):
    pass


class EritreaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2018, 2025)
    EID_AL_ADHA_DATES = {
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 6),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2018, 2025)
    EID_AL_FITR_DATES = {
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }
