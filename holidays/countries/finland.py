#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import _timedelta
from holidays.constants import PUBLIC, UNOFFICIAL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Finland(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Finland holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Finland>
        * [Bank holidays (Finnish)](https://www.suomenpankki.fi/fi/raha-ja-maksaminen/pankkivapaapaivat/)
        * [Bank holidays (English)](https://www.suomenpankki.fi/en/money-and-payments/bank-holidays/)
        * [Bank holidays (Swedish)](https://www.suomenpankki.fi/sv/pengar-och-betalningar/bankfria-dagar-i-finland/)
        * <https://en.wikipedia.org/wiki/Flag_flying_days_in_Finland#Customary_flag_days>
        * <https://intermin.fi/en/flag-and-arms/flag-flying-days>
        * <https://intermin.fi/en/flag-and-arms/flag-days/2024>
        * <https://en.wikipedia.org/wiki/Independence_Day_(Finland)>
    """

    country = "FI"
    default_language = "fi"
    supported_languages = ("en_US", "fi", "sv_FI", "uk")
    supported_categories = (PUBLIC, UNOFFICIAL)
    start_year = 1853

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

        if self._year >= 1917:
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
            # Runeberg Day.
            self._add_holiday_feb_5(tr("Runebergin päivä"))

        if self._year >= 1860:
            # Kalevala Day, Day of Finnish Culture.
            self._add_holiday_feb_28(tr("Kalevalan päivä, suomalaisen kulttuurin päivä"))

        if self._year >= 2007:
            #  Minna Canth Day, Day of Equality.
            self._add_holiday_mar_19(tr("Minna Canthin päivä, tasa-arvon päivä"))

        if self._year >= 1978:
            # Mikael Agricola Day, Day of the Finnish Language.
            self._add_holiday_apr_9(tr("Mikael Agricolan päivä, suomen kielen päivä"))

        if self._year >= 1987:
            # National War Veterans' Day.
            self._add_holiday_apr_27(tr("Kansallinen veteraanipäivä"))

        if self._year >= 2019:
            # Europe Day.
            self._add_europe_day(tr("Eurooppa-päivä"))

        if self._year >= 1918:
            # Mother's Day.
            self._add_holiday_2nd_sun_of_may(tr("Äitienpäivä"))

        if self._year >= 1952:
            # J. V. Snellman Day, Day of Finnish Heritage.
            self._add_holiday_may_12(tr("J.V. Snellmanin päivä, suomalaisuuden päivä"))

        if self._year >= 1977:
            # Remembrance Day.
            self._add_holiday_3rd_sun_of_may(tr("Kaatuneitten muistopäivä"))

        if self._year >= 1942:
            # Flag Day of the Finnish Defense Forces.
            self._add_holiday_jun_6(tr("Puolustusvoimain lippujuhlan päivä"))

        if self._year >= 1992:
            # Eino Leino Day, Day of Summer and Poetry.
            self._add_holiday_jul_6(tr("Eino Leinon päivä, runon ja suven päivä"))

        if self._year >= 2013:
            # Finland's Nature Day.
            self._add_holiday_last_sat_of_aug(tr("Suomen luonnon päivä"))

        if self._year >= 2016:
            # Miina Sillanpää Day, Day of Civic Participation.
            self._add_holiday_oct_1(tr("Miina Sillanpään ja kansalaisvaikuttamisen päivä"))

        if self._year >= 1950:
            # Aleksis Kivi Day, Day of Finnish Literature.
            self._add_holiday_oct_10(tr("Aleksis Kiven päivä, suomalaisen kirjallisuuden päivä"))

        if self._year >= 1987:
            # United Nations Day.
            self._add_united_nations_day(tr("YK:n päivä"))

        if self._year >= 1908:
            # Finnish Swedish Heritage Day, svenska dagen.
            self._add_holiday_nov_6(tr("Ruotsalaisuuden päivä, Kustaa Aadolfin päivä"))

        if self._year >= 1949:
            # Father's Day.
            self._add_holiday_2nd_sun_of_nov(tr("Isänpäivä"))

        if self._year >= 2020:
            # Day of Children's Rights.
            self._add_holiday_nov_20(tr("Lapsen oikeuksien päivä"))

        if self._year >= 2007:
            # Jean Sibelius Day, Day of Finnish Music.
            self._add_holiday_dec_8(tr("Jean Sibeliuksen päivä, suomalaisen musiikin päivä"))


class FI(Finland):
    pass


class FIN(Finland):
    pass
