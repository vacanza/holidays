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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class BonaireSintEustatiusAndSaba(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Bonaire Sint Eustatius And Saba holidays.

    References:
        * [Public Holidays 2025](https://www.sabagov.nl/residents-visitors/public-holidays)
        * [Public Holidays in Sint Eustatius in 2025](https://www.officeholidays.com/countries/bonaire-st-eustatius-saba/sint-eustatius/2025)
        * [Upcoming Bonaire, St Eustatius and Saba Public Holidays](https://www.qppstudio.net/public-holidays/bonaire__st_eustatius_and_saba.htm)
    """

    country = "BQ"
    default_language = "en_BQ"
    # Became special municipalities of the Netherlands on October 10, 2010
    start_year = 2011
    supported_languages = ("en_BQ", "en_US", "nl")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("New Year's Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Easter Sunday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # King's Birthday
        self._add_holiday_apr_27(tr("King's Birthday"))

        # Labor Day.
        self._add_labor_day(tr("Labor Day"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascension Day"))

        # Whit Sunday.
        self._add_whit_sunday(tr("Whit Sunday"))

        # Carnival Monday.
        self._add_carnival_monday(tr("Carnival Monday"))

        # Saba Day.
        self._add_holiday_dec_5(tr("Saba Day"))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        # Boxing Day
        self._add_christmas_day_two(tr("Boxing Day"))


class BQ(BonaireSintEustatiusAndSaba):
    pass


class BES(BonaireSintEustatiusAndSaba):
    pass
