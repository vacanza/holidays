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

from holidays.calendars.gregorian import APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.calendars.islamic import _CustomIslamicHolidays
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class SierraLeone(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Sierra Leone holidays.

    References:
        * <https://web.archive.org/web/20241006064824/https://www.officeholidays.com/countries/sierra-leone>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Sierra_Leone>
        * <https://web.archive.org/web/20250408204431/https://www.timeanddate.com/holidays/sierra-leone/>
        * <https://web.archive.org/web/20240727123934/http://salpost.gov.sl/opening-time-national-holidays>
    """

    country = "SL"
    default_language = "en_SL"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # %s (observed).
    observed_label = tr("%s (observed)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observed, estimated)")
    supported_languages = ("en_SL", "en_US")
    # Sierra Leone gained independence on April 27, 1961.
    start_year = 1962

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=SierraLeoneIslamicHolidays, show_estimated=islamic_show_estimated
        )
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("New Year's Day")))

        if self._year >= 2002:
            # Armed Forces Day.
            dts_observed.add(self._add_holiday_feb_18(tr("Armed Forces Day")))

        if self._year >= 2018:
            # International Women's Day.
            dts_observed.add(self._add_womens_day(tr("International Women's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Independence Day.
        dts_observed.add(self._add_holiday_apr_27(tr("Independence Day")))

        # International Worker's Day.
        dts_observed.add(self._add_labor_day(tr("International Worker's Day")))

        # Christmas Day.
        dts_observed.add(self._add_christmas_day(tr("Christmas Day")))

        # Boxing Day.
        dts_observed.add(self._add_christmas_day_two(tr("Boxing Day")))

        # Prophet's Birthday.
        dts_observed.update(self._add_mawlid_day(tr("Prophet's Birthday")))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day(tr("Eid al-Fitr")))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day(tr("Eid al-Adha")))

        if self.observed:
            self._populate_observed(dts_observed)


class SL(SierraLeone):
    pass


class SLE(SierraLeone):
    pass


class SierraLeoneIslamicHolidays(_CustomIslamicHolidays):
    """Sierra Leone Islamic holidays exact dates.

    References:
        * <https://web.archive.org/web/20250408204431/https://www.timeanddate.com/holidays/sierra-leone/>
    """

    # Prophet's Birthday
    MAWLID_DATES = {
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 15),
    }

    # Eid al-Fitr
    EID_AL_FITR_DATES = {
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
    }

    # Eid al-Adha
    EID_AL_ADHA_DATES = {
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
    }
