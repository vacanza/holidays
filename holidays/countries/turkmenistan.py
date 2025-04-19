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

from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Turkmenistan(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Turkmenistan holidays.

    References:
        * https://en.wikipedia.org/wiki/Public_holidays_in_Turkmenistan
        * https://www.timeanddate.com/holidays/turkmenistan/
        * https://www.mfa.gov.tm/en/articles/2
    """

    country = "TM"
    default_language = "tk"
    start_year = 1992
    supported_languages = ("en_US", "tk", "ru")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        name = tr("Жаңа жыл")
        self._add_new_years_day(name)
        self._add_new_years_day_two(name)

        # Memorial Day
        self._add_holiday_jan_12(tr("Хатыра гүни (Memorial Day)"))

        # Defender of the Fatherland Day
        if self._year >= 2009:
            self._add_holiday_jan_27(tr("Ватанмухадызларың гүни"))

        # International Women's Day
        self._add_womens_day(tr("Халықаралық әйелдер күні"))

        # Nowruz
        name = tr("Наурыз мейрамы")
        self._add_holiday_mar_21(name)
        self._add_holiday_mar_22(name)

        # Victory Day
        self._add_holiday_may_9(tr("Жеңиш гүни"))

        # Constitution and Revival Day
        if self._year >= 2018:
            self._add_holiday_may_18(tr("Конституция ве Түзелиш гүни"))
        else:
            self._add_holiday_may_18(tr("Түзелиш гүни"))

        # Independence Day
        if self._year <= 2017:
            self._add_holiday_oct_27(tr("Гарашсызлык гүни"))
        else:
            self._add_holiday_sep_27(tr("Гарашсызлык гүни"))

        # Day of Remembrance
        if self._year >= 2015:
            self._add_holiday_oct_6(tr("Хатыра гүни (Day of Remembrance)"))

        # Neutrality Day
        if self._year >= 2023:
            self._add_holiday_dec_12(tr("Битараплык гүни"))
        elif self._year >= 2018:
            self._add_holiday_jun_27(tr("Түркменистаның битараплык гүни"))
        elif self._year >= 1995:
            self._add_holiday_dec_12(tr("Битараплык гүни"))

        # Islamic Holidays
        self._add_eid_al_fitr_day(tr("Ораза байрамы"))
        self._add_eid_al_fitr_day_two(tr("Ораза байрамы"))
        self._add_eid_al_fitr_day_three(tr("Ораза байрамы"))

        self._add_eid_al_adha_day(tr("Гурбан байрамы"))
        self._add_eid_al_adha_day_two(tr("Гурбан байрамы"))
        self._add_eid_al_adha_day_three(tr("Гурбан байрамы"))


class TM(Turkmenistan):
    pass


class TKM(Turkmenistan):
    pass
