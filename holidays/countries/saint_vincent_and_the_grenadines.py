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

from holidays.calendars.gregorian import JUL, AUG, SEP, _timedelta
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE


class SaintVincentAndTheGrenadines(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Saint Vincent and the Grenadines holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Saint_Vincent_and_the_Grenadines>
        * <https://www.timeanddate.com/holidays/saint-vincent-and-the-grenadines/>
        * <https://web.archive.org/web/20250513011200/https://www.gov.vc/images/pdf_documents/VINCENTIANS-PREPARE-FOR-MAY-21--SPIRITUAL-BAPTIST-LIBERATION-DAY-NATIONAL-HOLIDAY.pdf>
        * [2019-2025](https://web.archive.org/web/20250214232128/https://pmoffice.gov.vc/pmoffice/index.php/public-holidays)
        * <https://web.archive.org/web/20250607111242/https://www.stvincenttimes.com/august-3rd-and-4th-2020-declared-public-holidays-in-svg/>
    """

    country = "VC"
    default_language = "en_VC"
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_languages = ("en_US", "en_VC")
    start_year = 1979

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # National Heroes' Day.
        self._add_observed(self._add_holiday_mar_14(tr("National Heroes' Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # National Workers Day.
        self._add_observed(self._add_labor_day(tr("National Workers Day")))

        if self._year >= 2025:
            # National Spiritual Baptist Day.
            self._add_holiday_may_21(tr("National Spiritual Baptist Day"))

        # Whit Monday.
        self._add_whit_monday(tr("Whit Monday"))

        # Carnival Monday.
        name = tr("Carnival Monday")
        if self._year == 2020:
            self._add_holiday_aug_3(name)
        else:
            self._add_holiday_2nd_mon_of_jul(name)

        # Carnival Tuesday.
        name = tr("Carnival Tuesday")
        if self._year == 2020:
            self._add_holiday_aug_4(name)
        else:
            self._add_holiday_1_day_past_2nd_mon_of_jul(name)

        # Emancipation Day.
        self._add_observed(self._add_holiday_aug_1(tr("Emancipation Day")))

        # Independence Day.
        self._add_holiday_oct_27(tr("Independence Day"))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two(tr("Boxing Day")))


class VC(SaintVincentAndTheGrenadines):
    pass


class VCT(SaintVincentAndTheGrenadines):
    pass
