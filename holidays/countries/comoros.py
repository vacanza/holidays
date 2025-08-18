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

from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase


class Comoros(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Comoros holidays.

    References:
        * [Public holidays in the Comoros](https://en.wikipedia.org/wiki/Public_holidays_in_the_Comoros)
        * [UNION DES COMORES](https://web.archive.org/web/20240723035934/https://munganyo.km/public/storage/xnXxUFrh28LH1bQZpqAsLhGqXeearo-metaRGVjcmV0IE7CsDI0LTA1NlBSIGR1IDEwIGF2cmlsIDIwMjQgUG9ydGFudCBKb3VybsOpZSBjaG9tw6llIGV0IHBhecOpZS5wZGY=-.pdf)
        * [Union des Comores 2021](https://web.archive.org/web/20250712053206/https://scontent-del1-2.xx.fbcdn.net/v/t39.30808-6/471586197_1113861707132176_3696210890184034016_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=833d8c&_nc_ohc=3hfvuVNGVbMQ7kNvwHvrgbW&_nc_oc=AdnuDzvtcvdBJMoN-qSW7Pnx2fnzj2TFgwMSRklpM_Na-5AaB9y8D0U5BINcxL-vVL0&_nc_zt=23&_nc_ht=scontent-del1-2.xx&_nc_gid=HWC_59SRsyDfwGxku5bqXw&oh=00_AfSk0LCPS7PARPjdX5-vfM_lr7WxZnrkA9jRyrdUFhoyMQ&oe=68736290)
    """

    country = "KM"
    # %s (estimated).
    estimated_label = "%s (estimated)"
    # %s (observed, estimated).
    observed_estimated_label = "%s (observed, estimated)"
    # Independence from France on July 6, 1975.
    start_year = 1976

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
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Cheikh al Maarouf.
        self._add_holiday_mar_18("Cheikh al Maarouf")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # National Day.
        self._add_holiday_jul_6("National Day")

        # Maore Day.
        self._add_holiday_nov_12("Maore Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid al-Fitr")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid al-Adha")

        # Islamic New Year.
        self._add_islamic_new_year_day("Islamic New Year")

        # The Prophet's Birthday.
        self._add_mawlid_day("The Prophet's Birthday")

        # The Prophet's Ascension.
        self._add_isra_and_miraj_day("The Prophet's Ascension")


class KM(Comoros):
    pass


class COM(Comoros):
    pass
