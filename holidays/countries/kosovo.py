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

from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY


class Kosovo(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Kosovo holidays.

    References:
        * <https://web.archive.org/web/20251105011859/https://bqk-kos.org/kalendari-i-festave/>
        * [Law No. 03/L-064](https://web.archive.org/web/20231127220229/https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=2539)
    """

    country = "XK"
    default_language = "sq"
    # %s (estimated).
    estimated_label = tr("%s (e vlerësuar)")
    # %s (observed).
    observed_label = tr("%s (ditë pushimi e shtyrë)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (ditë pushimi e shtyrë, e vlerësuar)")
    supported_languages = ("en_US", "sq", "sr")
    # First full year after independence (2008-02-17).
    start_year = 2009

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        name = tr("Viti i Ri")
        dts_observed.add(self._add_new_years_day(name))
        dts_observed.add(self._add_new_years_day_two(name))

        # Orthodox Christmas Day.
        dts_observed.add(self._add_christmas_day(tr("Krishtlindjet Ortodokse"), JULIAN_CALENDAR))

        dts_observed.add(
            # Independence Day.
            self._add_holiday_feb_17(tr("Dita e Pavarësisë së Republikës së Kosovës"))
        )

        # Catholic Easter.
        dts_observed.add(self._add_easter_sunday(tr("Pashkët Katolike")))

        # Orthodox Easter.
        dts_observed.add(self._add_easter_sunday(tr("Pashkët Ortodokse"), JULIAN_CALENDAR))

        dts_observed.add(
            # Constitution Day.
            self._add_holiday_apr_9(tr("Dita e Kushtetutës së Republikës së Kosovës"))
        )

        # International Workers' Day.
        dts_observed.add(self._add_labor_day(tr("Dita Ndërkombëtare e Punës")))

        # Europe Day.
        dts_observed.add(self._add_europe_day(tr("Dita e Evropës")))

        # Catholic Christmas Day.
        dts_observed.add(self._add_christmas_day(tr("Krishtlindjet Katolike")))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day(tr("Bajrami i Madh, dita e parë")))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day(tr("Bajrami i Vogël, dita e parë")))

        if self.observed:
            self._populate_observed(dts_observed)


class XK(Kosovo):
    pass


class XKK(Kosovo):
    pass
