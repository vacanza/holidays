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

from holidays.calendars.gregorian import APR, JUL, OCT, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SUN_TO_NEXT_MON


class Grenada(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Grenada Holidays

    References:
        * <https://www.timeanddate.com/holidays/grenada/>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Grenada>
        * <https://laws.gov.gd/index.php/chapters/b-23-39/1042-cap25-bank-holidays-act-2/viewdocument/1042>

        National Heroes' Day:
        * <https://www.gov.gd/component/edocman/grenadas-first-national-heroes-day-and-october-19th-commemoration-events/viewdocument/576>
        * <https://www.gov.gd/component/edocman/throne-speech-2023/viewdocument/544>
        * <https://nowgrenada.com/2022/10/government-to-make-19-october-a-public-holiday-from-2023/>
        * <https://www.gov.gd/component/edocman/throne-speech-2024/viewdocument/1202>

        Emancipation Day:
        * <https://www.gov.gd/component/edocman/grenadas-public-holidays-2025/viewdocument/1386>
        * <https://nowgrenada.com/2025/01/gnrc-chairman-supports-1-august-as-national-holiday/>

        Grenada Calendar:
        * <https://www.gov.gd/component/edocman/grenadas-public-holidays-2025/viewdocument/1386>
        * <https://web.archive.org/web/20230329094946/https://www.gov.gd/pdf/Public%20Holidays%202023.pdf>
        * <https://web.archive.org/web/20180424025139/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20170505034606/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20160518030722/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20150701045051/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20140424191452/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20130805181426/http://gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20120623100105/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20111007094915/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20100108053101/http://www.gov.gd/holiday_events.html>
    """

    country = "GD"
    default_language = "en_GB"
    # %s (observed).
    estimated_label = "%s (observed)"
    supported_languages = ("en_GB", "en_US")

    # Guinea gained independence from United Kingdom on February 7, 1974.
    start_year = 1975

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, GrenadaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Independence Day.
        self._add_observed(self._add_holiday_feb_7(tr("Independence Day")))

        # Good Friday.
        self._add_observed(self._add_good_friday(tr("Good Friday")))

        # Easter Monday.
        self._add_observed(self._add_easter_monday(tr("Easter Monday")))

        # Labor Day.
        self._add_observed(self._add_labor_day(tr("Labour Day")))

        # Whit Monday.
        self._add_observed(self._add_whit_monday(tr("Whit Monday")))

        # Corpus Christi.
        self._add_observed(self._add_corpus_christi_day(tr("Corpus Christi")))

        if self._year < 2025:
            # Emancipation Day.
            self._add_holiday_1st_mon_of_aug(tr("Emancipation Day"))
        if self._year >= 2025:
            self._add_observed(self._add_holiday_aug_1(tr("Emancipation Day")))

        # Carnival Monday.
        self._add_holiday_2nd_mon_of_aug(tr("Carnival Monday"))

        # Carnival Tuesday.
        self._add_holiday_2nd_tue_of_aug(tr("Carnival Tuesday"))

        if self._year >= 2023:
            # National Heroes’ Day.
            self._add_observed(self._add_holiday_oct_19(tr("National Heroes' Day")))

        # Thanksgiving Day.
        self._add_observed(self._add_holiday_oct_25(tr("Thanksgiving Day")))

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two(tr("Boxing Day")))


class GD(Grenada):
    pass


class GRD(Grenada):
    pass


class GrenadaStaticHolidays:
    """Grenada Special Holidays

    References:
        * <https://web.archive.org/web/20150701045051/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20140424191452/http://www.gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20130805181426/http://gov.gd/holiday_events.html>
        * <https://web.archive.org/web/20120623100105/http://www.gov.gd/holiday_events.html>
        * <https://www.gov.gd/component/edocman/grenada-to-host-activities-to-observe-caricoms-50th-anniversary/viewdocument/403>
    """

    special_public_holidays = {
        2012: (
            # Carricou Maroon and String Band Music Festival
            (APR, 27, tr("Carricou Maroon and String Band Music Festival")),
            (APR, 28, tr("Carricou Maroon and String Band Music Festival")),
            (APR, 29, tr("Carricou Maroon and String Band Music Festival")),
            # Aunty Tek Spice Word Festival
            (OCT, 16, tr("Aunty Tek Spice Word Festival")),
            (OCT, 17, tr("Aunty Tek Spice Word Festival")),
            (OCT, 18, tr("Aunty Tek Spice Word Festival")),
            (OCT, 19, tr("Aunty Tek Spice Word Festival")),
            (OCT, 20, tr("Aunty Tek Spice Word Festival")),
            # Camerhogne Folk Festival
            (NOV, 30, tr("Camerhogne Folk Festival")),
            (DEC, 1, tr("Camerhogne Folk Festival")),
            (DEC, 2, tr("Camerhogne Folk Festival")),
        ),
        2013: (
            # Carricou Maroon and String Band Music Festival
            (APR, 26, tr("Carricou Maroon and String Band Music Festival")),
            (APR, 27, tr("Carricou Maroon and String Band Music Festival")),
            (APR, 28, tr("Carricou Maroon and String Band Music Festival")),
            # Aunty Tek Spice Word Festival
            (OCT, 16, tr("Aunty Tek Spice Word Festival")),
            (OCT, 17, tr("Aunty Tek Spice Word Festival")),
            (OCT, 18, tr("Aunty Tek Spice Word Festival")),
            (OCT, 19, tr("Aunty Tek Spice Word Festival")),
            (OCT, 20, tr("Aunty Tek Spice Word Festival")),
            # Camerhogne Folk Festival
            (NOV, 29, tr("Camerhogne Folk Festival")),
            (NOV, 30, tr("Camerhogne Folk Festival")),
            (DEC, 1, tr("Camerhogne Folk Festival")),
        ),
        2014: (
            # Carricou Maroon and String Band Music Festival
            (APR, 25, tr("Carricou Maroon and String Band Music Festival")),
            (APR, 26, tr("Carricou Maroon and String Band Music Festival")),
            (APR, 27, tr("Carricou Maroon and String Band Music Festival")),
            # Aunty Tek Spice Word Festival
            (OCT, 15, tr("Aunty Tek Spice Word Festival")),
            (OCT, 16, tr("Aunty Tek Spice Word Festival")),
            (OCT, 17, tr("Aunty Tek Spice Word Festival")),
            (OCT, 18, tr("Aunty Tek Spice Word Festival")),
            (OCT, 19, tr("Aunty Tek Spice Word Festival")),
            # Camerhogne Folk Festival
            (DEC, 5, tr("Camerhogne Folk Festival")),
            (DEC, 6, tr("Camerhogne Folk Festival")),
            (DEC, 7, tr("Camerhogne Folk Festival")),
        ),
        2015: (
            # Carricou Maroon and String Band Music Festival
            (APR, 24, tr("Carricou Maroon and String Band Music Festival")),
            (APR, 25, tr("Carricou Maroon and String Band Music Festival")),
            (APR, 26, tr("Carricou Maroon and String Band Music Festival")),
            # Aunty Tek Spice Word Festival
            (OCT, 15, tr("Aunty Tek Spice Word Festival")),
            (OCT, 16, tr("Aunty Tek Spice Word Festival")),
            (OCT, 17, tr("Aunty Tek Spice Word Festival")),
            (OCT, 18, tr("Aunty Tek Spice Word Festival")),
            (OCT, 19, tr("Aunty Tek Spice Word Festival")),
            # Camerhogne Folk Festival
            (DEC, 4, tr("Camerhogne Folk Festival")),
            (DEC, 5, tr("Camerhogne Folk Festival")),
            (DEC, 6, tr("Camerhogne Folk Festival")),
        ),
        # CARICOM’s 50th Anniversary.
        2023: (JUL, 4, tr("CARICOM's 50th Anniversary")),
    }
