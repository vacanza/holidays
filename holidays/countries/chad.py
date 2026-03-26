#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly.

from holidays.translation import tr
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, APR, JUN, JUL, AUG, SEP, NOV, DEC
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Chad(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Chad holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Chad>
        * <https://web.archive.org/web/20240619220557/https://www.ilo.org/dyn/natlex/docs/ELECTRONIC/97323/115433/F-316075167/TCD-97323.pdf>
    """

    country = "TD"

    default_language = "fr"
    supported_languages = ("en_US", "fr", "ar")

    estimated_label = tr("%s (estimated)")
    observed_estimated_label = tr("%s (observed, estimated)")
    observed_label = tr("%s (observed)")

    start_year = 1961

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=ChadIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, ChadStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # International Women's Day.
        self._add_observed(self._add_womens_day(tr("International Women's Day")))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Labour Day.
        self._add_observed(self._add_labor_day(tr("Labour Day")))

        # Independence Day.
        self._add_observed(self._add_holiday_aug_11(tr("Independence Day")))

        # All Saints' Day.
        self._add_all_saints_day(tr("All Saints' Day"))

        # Republic Day.
        self._add_observed(self._add_holiday_nov_28(tr("Republic Day")))

        if self._year >= 1991:
            # Freedom and Democracy Day.
            self._add_observed(self._add_holiday_dec_1(tr("Freedom and Democracy Day")))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Eid al-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Eid al-Adha"))

        # Mawlid.
        self._add_mawlid_day(tr("Mawlid"))


class TD(Chad):
    pass


class TCD(Chad):
    pass


class ChadIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2015, 2023)
    EID_AL_ADHA_DATES = {
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2015, 2024)
    EID_AL_FITR_DATES = {
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
    }

    MAWLID_DATES_CONFIRMED_YEARS = (2015, 2022)
    MAWLID_DATES = {
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
    }


class ChadStaticHolidays:
    special_public_holidays = {
        2021: (APR, 23, tr("Funeral of Idriss Déby Itno")),  # ✅ wrapped
    }