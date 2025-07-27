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
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_WORKDAY


class Turkmenistan(ObservedHolidayBase, InternationalHolidays, IslamicHolidays):
    """Turkmenistan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Turkmenistan>
        * [Labor Code](https://web.archive.org/web/20250419204037/https://www.tds.gov.tm/en/20-labor-code-of-turkmenistan)
        * [State Flag and Constitution Day](https://en.wikipedia.org/wiki/State_Flag_and_Constitution_Day_(Turkmenistan))
        * [Independence Day](https://en.wikipedia.org/wiki/Independence_Day_(Turkmenistan))
        * [Detailed Research](https://archive.org/details/holiday-research-in-central-asia)
    """

    country = "TM"
    default_language = "tk"
    # %s (estimated).
    estimated_label = tr("%s (çak edilýär)")
    # %s (observed).
    observed_label = tr("%s (dynç güni)")
    # %s (observed, estimated)
    observed_estimated_label = tr("%s (dynç güni, çak edilýär)")
    start_year = 1992
    supported_languages = ("en_US", "ru", "tk")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=TurkmenistanIslamicHolidays, show_estimated=islamic_show_estimated
        )
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("Täze ýyl")))

        if 1995 <= self._year <= 2017:
            dts_observed.add(
                # State Flag Day.
                self._add_holiday_feb_19(tr("Türkmenistanyň Döwlet baýdagynyň güni"))
            )

        if 2001 <= self._year <= 2007:
            # Spring Festival.
            dts_observed.add(self._add_holiday_mar_20(tr("Milli bahar baýramy")))
        else:
            # International Women's Day.
            dts_observed.add(self._add_womens_day(tr("Halkara zenanlar güni")))

        # Spring Festival.
        name = tr("Milli bahar baýramy")
        dts_observed.add(self._add_holiday_mar_21(name))
        dts_observed.add(self._add_holiday_mar_22(name))

        if self._year >= 2018:
            dts_observed.add(
                self._add_holiday_may_18(
                    # Constitution and State Flag Day.
                    tr("Türkmenistanyň Konstitusiýasynyň we Döwlet baýdagynyň güni")
                )
            )

        # Independence Day.
        name = tr("Türkmenistanyň Garaşsyzlyk güni")
        if self._year <= 2017:
            dts_observed.add(self._add_holiday_oct_27(name))
        else:
            dts_observed.add(self._add_holiday_sep_27(name))

        if self._year >= 1995:
            # Memorial Day.
            dts_observed.add(self._add_holiday_oct_6(tr("Hatyra güni")))

            # International Neutrality Day.
            dts_observed.add(self._add_holiday_dec_12(tr("Halkara Bitaraplyk güni")))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day(tr("Oraza baýramy")))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day(tr("Gurban baýramy")))

        self._populate_observed(dts_observed)


class TM(Turkmenistan):
    pass


class TKM(Turkmenistan):
    pass


class TurkmenistanIslamicHolidays(_CustomIslamicHolidays):
    # https://web.archive.org/web/20240908061230/https://www.timeanddate.com/holidays/turkmenistan/eid-al-fitr
    EID_AL_FITR_DATES = {
        2010: (SEP, 10),
        2011: (AUG, 31),
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
        2025: (MAR, 30),
    }

    # https://web.archive.org/web/20240912191844/https://www.timeanddate.com/holidays/turkmenistan/eid-al-adha
    EID_AL_ADHA_DATES = {
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 13),
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
