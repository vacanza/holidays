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

from holidays.calendars.gregorian import JAN, MAY, JUL, OCT
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON, MON_TO_NEXT_TUE


class Vanuatu(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Vanuatu holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Vanuatu>
        * <https://web.archive.org/web/20250419100625/https://www.timeanddate.com/holidays/vanuatu>
        * <https://web.archive.org/web/20250419062251/https://gov.vu/index.php/events/holidays>
    """

    country = "VU"
    default_language = "en_VU"
    # %s (observed).
    observed_label = tr("%s (observed)")
    # On 30 July 1980, Vanuatu gained independence from Britain and France.
    start_year = 1981
    supported_languages = ("en_US", "en_VU", "fr")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, VanuatuStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        if self._year >= 1999:
            # Father Lini Day.
            self._add_observed(self._add_holiday_feb_21(tr("Father Lini Day")))

        # Custom Chief's Day.
        self._add_observed(self._add_holiday_mar_5(tr("Custom Chief's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Labour Day")))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        # Children's Day.
        self._add_observed(self._add_holiday_jul_24(tr("Children's Day")))

        # Independence Day.
        self._add_observed(self._add_holiday_jul_30(tr("Independence Day")))

        # Assumption Day.
        self._add_observed(self._add_assumption_of_mary_day(tr("Assumption Day")))

        # Constitution Day.
        self._add_observed(self._add_holiday_oct_5(tr("Constitution Day")))

        # Unity Day.
        self._add_observed(self._add_holiday_nov_29(tr("Unity Day")))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        self._add_observed(
            # Family Day.
            self._add_christmas_day_two(tr("Family Day")),
            rule=SUN_TO_NEXT_MON + MON_TO_NEXT_TUE,
        )


class VU(Vanuatu):
    pass


class VTU(Vanuatu):
    pass


class VanuatuStaticHolidays:
    """Vanuatu special holidays.

    References:
        * [2012 General Election](https://web.archive.org/web/20241222131603/https://www.paclii.org/vu/legis/sub_leg/phadopheo2012600.pdf)
        * [2022 General Election](https://web.archive.org/web/20261127091523/https://electoral.gov.vu/images/2022/10/09/edc-snap-election-polling-day-public-holiday-official-gazette-no-74-of-2022-dated-23-september-2022_page_04.jpg)
        * [2024 Referendum](https://web.archive.org/web/20261127081335/https://pina.com.fj/2024/05/28/vanuatu-pm-salwai-urges-citizens-to-vote-tomorrow/)
        * [2025 General Election](https://web.archive.org/web/20250116065640/https://www.fbcnews.com.fj/world/pacific-islands/earthquake-doesnt-derail-vanuatus-snap-election)
    """

    # Election Day.
    election_day = tr("Election Day")
    # 40th Independence Anniversary.
    independence_anniversary = tr("40th Independence Anniversary")

    special_public_holidays = {
        2012: (OCT, 30, election_day),
        2020: (
            (JUL, 23, independence_anniversary),
            (JUL, 27, independence_anniversary),
            (JUL, 28, independence_anniversary),
            (JUL, 29, independence_anniversary),
            (JUL, 31, independence_anniversary),
        ),
        2022: (OCT, 13, election_day),
        # Referendum Day.
        2024: (MAY, 29, tr("Referendum Day")),
        2025: (JAN, 16, election_day),
    }
