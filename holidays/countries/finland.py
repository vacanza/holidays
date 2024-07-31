#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import _timedelta
from holidays.constants import PUBLIC, UNOFFICIAL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Finland(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
        - https://en.wikipedia.org/wiki/Public_holidays_in_Finland
        - `Bank holidays (Finnish) <https://www.suomenpankki.fi/fi/raha-ja-maksaminen/pankkivapaapaivat/>`_
        - `Bank holidays (English) <https://www.suomenpankki.fi/en/money-and-payments/bank-holidays/>`_
        - `Bank holidays (Swedish) <https://www.suomenpankki.fi/sv/pengar-och-betalningar/bankfria-dagar-i-finland/>`_
        - https://en.wikipedia.org/wiki/Flag_flying_days_in_Finland#Customary_flag_days
        - https://intermin.fi/en/flag-and-arms/flag-flying-days
    """

    country = "FI"
    default_language = "fi"
    supported_languages = ("en_US", "fi", "sv_FI", "uk")
    supported_categories = (PUBLIC, UNOFFICIAL)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Uudenvuodenpäivä"))

        # Epiphany.
        name = tr("Loppiainen")
        if 1973 <= self._year <= 1990:
            self._add_holiday_1st_sat_from_jan_6(name)
        else:
            self._add_epiphany_day(name)

        # Good Friday.
        self._add_good_friday(tr("Pitkäperjantai"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Pääsiäispäivä"))

        # Easter Monday.
        self._add_easter_monday(tr("Toinen pääsiäispäivä"))

        # May Day.
        self._add_holiday_may_1(tr("Vappu"))

        # Ascension Day.
        name = tr("Helatorstai")
        if 1973 <= self._year <= 1990:
            self._add_holiday_34_days_past_easter(name)
        else:
            self._add_ascension_thursday(name)

        # Whit Sunday.
        self._add_whit_sunday(tr("Helluntaipäivä"))

        # Midsummer Eve.
        name = tr("Juhannusaatto")
        if self._year >= 1955:
            dt = self._add_holiday_1st_fri_from_jun_19(name)
        else:
            dt = self._add_holiday_jun_23(name)

        # Midsummer Day.
        self._add_holiday(tr("Juhannuspäivä"), _timedelta(dt, +1))

        # All Saints' Day.
        name = tr("Pyhäinpäivä")
        if self._year >= 1955:
            self._add_holiday_1st_sat_from_oct_31(name)
        else:
            self._add_holiday_nov_1(name)

        # Independence Day.
        self._add_holiday_dec_6(tr("Itsenäisyyspäivä"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Jouluaatto"))

        # Christmas Day.
        self._add_christmas_day(tr("Joulupäivä"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Tapaninpäivä"))

    def _populate_unofficial_holidays(self):
        if self._year >= 1854:
            # Birthday of the national poet Johan Ludvig Runeberg
            self._add_holiday_feb_5(tr("Runebergin päivä"))

        if self._year >= 2007:
            # Birthday of novelist and playwright Minna Canth and Day of Equality
            self._add_holiday_mar_19(tr("Minna Canthin päivä, tasa-arvon päivä"))

        if self._year >= 1978:
            # The day Mikael Agricola and Day of the Finnish language
            self._add_holiday_apr_9(tr("Mikael Agricolan päivä, suomen kielen päivä"))

        if self._year >= 1987:
            # National Veterans' Day
            self._add_holiday_apr_27(tr("Kansallinen veteraanipäivä"))

        if self._year >= 2019:
            # Europe Day
            self._add_holiday_may_9(tr("Eurooppa-päivä"))

        if self._year >= 1952:
            # Day of Finnish Identity (or The Finnish Identity Day)
            self._add_holiday_may_12(tr("Suomalaisuuden päivä"))

        if self._year >= 1977:
            # Remembrance Day
            self._add_holiday_3rd_sun_of_may(tr("Kaatuneitten muistopäivä"))

        if self._year >= 1992:
            # Birthday of the poet Eino Leino
            self._add_holiday_jul_6(tr("Eino Leinon päivä"))

        if self._year >= 2013:
            # Finland's Nature Day
            self._add_holiday_last_sat_of_aug(tr("Suomen luonnon päivä"))

        if self._year >= 2016:
            # Miina Sillanpää Day, Day of Civic Participation
            self._add_holiday_oct_1(tr("Miina Sillanpään ja kansalaisvaikuttamisen päivä"))

        if self._year >= 1950:
            # Birthday of the National writer Aleksis Kivi
            self._add_holiday_oct_10(tr("Aleksis Kiven päivä"))

        if self._year >= 1987:
            # United Nations Day
            self._add_united_nations_day(tr("Yhdistyneiden Kansakuntien päivä"))

        if self._year >= 1908:
            # Finnish Swedish Heritage Day
            self._add_holiday_nov_6(tr("Ruotsalaisuuden päivä"))

        if self._year >= 2020:
            # Day of Children's Rights
            self._add_holiday_nov_20(tr("Lapsen oikeuksien päivä"))

        if self._year >= 2007:
            # Birthday of the composer Jean Sibelius, Day of Finnish Music
            self._add_holiday_dec_8(tr("Jean Sibeliuksen päivä"))


class FI(Finland):
    pass


class FIN(Finland):
    pass
