#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from gettext import gettext as tr

from holidays.calendars.gregorian import SEP, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ALL_TO_NEAREST_MON_LATAM,
    MON_TO_NEXT_TUE,
    SUN_TO_NEXT_MON,
)


class Tonga(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
      - https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/1919/1919-0008/PublicHolidaysAct_3.pdf  # 2020 Rev.  # noqa: E501
      - https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/1919/1919-0008/LaokihengaahiAhoMaloloFaka-Puleanga_3x.pdf  # 2020 Rev. (to)  # noqa: E501
      - https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/1919/1919-0008/PublicHolidaysAct_2.pdf  # 2016 Rev.  # noqa: E501
      - https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/1919/1919-0008/PublicHolidaysAct_1.pdf  # 1988 Rev.  # noqa: E501
      - https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/1919/1919-0008/LaokihengaahiAhoMaloloFaka-Puleanga_1x.pdf  # 1988 Rev. (to)  # noqa: E501
      - http://www.paclii.org/to/legis/num_act/pha2010243/  # Act 10 of 2010.
      - http://www.paclii.org/to/legis/num_act/pha2013243/  # Act 5 of 2013.

    Checked With:
      - https://www.gov.to/press-release/tonga-public-holidays-for-2024/  # 2024
      - https://www.gov.to/press-release/tonga-public-holidays-for-2023/  # 2023
      - https://www.gov.to/press-release/tonga-public-holidays-for-2022/  # 2022
      - https://www.gov.to/press-release/tonga-public-holidays-for-2021/  # 2021
      - https://www.gov.to/press-release/tonga-public-holidays-for-2020/  # 2020
      - https://www.gov.to/press-release/tonga-public-holidays-for-2019-2/  # 2019
      - https://www.gov.to/press-release/tonga-public-holidays-for-2018/  # 2018
      - https://www.officeholidays.com/countries/tonga/2017  # 2017

    1988 Revision Observance Rule:
        Provided always that when any of the days specified falls upon a Sunday,
        the next following Monday shall be a public holiday and that whenever
        the twenty-sixth day of December falls upon a Monday the day following
        shall be a public holiday. (Amended by Act 11 of 1970.)

    2016 and 2020 Revision Observance Rule:
        Provided that when any public holidays specified, except Christmas Day, the
        day immediately succeeding Christmas Day, New Years Day, Good Friday,
        Easter Monday, ANZAC Day, Birthday of the reigning Sovereign of Tonga
        and Birthday of the Heir to the Crown of Tonga, falls upon a Thursday,
        Friday, Saturday or Sunday, that public holiday shall be celebrated on the next
        following Monday; and if it falls on a Tuesday or Wednesday, that public
        holiday shall be celebrated on the Monday before the actual public holiday.
        (Amended by Act 10 of 2010: May 18, 2010.)
        "Birthday of the reigning Sovereign of Tonga and Birthday of the Heir to
        the Crown of Tonga" is add to the exempted list as seen above.
        (Amended by Act 5 of 2013: Jun 28, 2013.)

        Further provided that the Birthday of the reigning Sovereign of Tonga and the
        Birthday of the Heir to the Crown of Tonga shall be celebrated on the day it
        falls, unless it falls on a Sunday in which case it would be celebrated on the
        next following Monday.
        (Inserted by Act 5 of 2013: Jun 28, 2013.)
    """

    country = "TO"
    default_language = "to"
    # %s (Observed).
    observed_label = tr("%s (Fakatokanga'i)")
    supported_languages = ("en_US", "to")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=TongaStaticHolidays)
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date, **kwargs):
        if self._year >= 2010:
            kwargs["rule"] = kwargs["rule"] or ALL_TO_NEAREST_MON_LATAM
        return super()._add_observed(dt, **kwargs)

    def _populate_public_holidays(self):
        # Public Holidays Act, 1988 Revision.
        if self._year <= 1988:
            return None

        # New Year's Day.
        jan_1 = self._add_new_years_day(tr("'Uluaki 'Aho 'o e Ta'u Fo'ou"))
        if self._year <= 2016:
            self._add_observed(jan_1, rule=SUN_TO_NEXT_MON)

        # Birthday of the King/Queen of Tonga.
        # Topou VI: Jul 12 (2012-Present)*
        # George Tupou V: May 4 (2007-2011)
        # Tāufa'āhau Tupou IV: Jul 4: (1965-2006)
        #  * By Cabinet Decision of Jul 6, 2012 this date was declared to be Jul 4,
        #    thus not celebrated in 2012.

        # Birthday of the Reigning Sovereign of Tonga.
        name = tr("'Aho 'Alo'i 'o 'Ene 'Afio ko e Tu'i 'o Tonga 'oku lolotonga Pule")

        if self._year == 2011:
            self._move_holiday(self._add_holiday_may_4(name))
        elif 2007 <= self._year <= 2010:
            self._add_observed(self._add_holiday_may_4(name), rule=SUN_TO_NEXT_MON)
        elif self._year != 2012:
            self._add_observed(self._add_holiday_jul_4(name), rule=SUN_TO_NEXT_MON)

        # Birthday of the Crown Prince/Princess of Tonga.
        # Tupouto'a 'Ulukalala: Sep 17 (2012-Present)
        # Topou VI: Jul 12 (2007-2011)
        # George Tupou V: May 4 (1968-2006)

        # Birthday of the Heir to the Crown of Tonga.
        name = tr("'Aho 'Alo'i 'o e 'Ea ki he Kalauni 'o Tonga")

        if self._year >= 2012:
            self._add_observed(self._add_holiday_sep_17(name), rule=SUN_TO_NEXT_MON)
        elif self._year >= 2010:
            self._move_holiday(self._add_holiday_jul_12(name))
        elif self._year >= 2007:
            self._add_observed(self._add_holiday_jul_12(name))
        else:
            self._add_observed(self._add_holiday_may_4(name))

        # Good Friday.
        self._add_good_friday(tr("Falaite Lelei"))

        # Easter Monday.
        self._add_easter_monday(tr("Monite 'o e Toetu'u"))

        # Anzac Day.
        apr_25 = self._add_anzac_day(tr("'Aho Anzac"))
        if self._year <= 2016:
            self._add_observed(apr_25, rule=SUN_TO_NEXT_MON)

        # Emancipation Day.
        jun_4 = self._add_holiday_jun_4(tr("'Aho Tau'ataina"))
        if self._year >= 2010:
            self._move_holiday(jun_4)
        else:
            self._add_observed(jun_4)

        # Coronation Date of Tongan Monarchy since 1970.*
        # Topou VI: Jul 4 (2015-Present)**
        # George Tupou V: Aug 1 (2008-2011)
        # Tāufa'āhau Tupou IV: Jul 4: (1967-2006)**
        #  *  No celebration for in-between years i.e. 2007, 2012-2014.
        #  ** Has de facto merged with King's Birthday.

        if 2008 <= self._year <= 2011:
            name = tr(
                # Anniversary of the Coronation Day of the reigning Sovereign of Tonga.
                "Fakamanatu 'o e 'Aho Hilifaki Kalauni 'o 'Ene 'Afio ko e Tu'i 'o Tonga "
                "'a ia 'oku lolotonga Pule"
            )
            if self._year >= 2010:
                self._move_holiday(self._add_holiday_aug_1(name))
            else:
                self._add_observed(self._add_holiday_aug_1(name))

        # Constitution Day.
        nov_4 = self._add_holiday_nov_4(tr("'Aho Konisitutone"))
        if self._year >= 2010:
            self._move_holiday(nov_4)
        else:
            self._add_observed(nov_4)

        dec_4 = self._add_holiday_dec_4(
            # Anniversary of the Coronation of HM King George Tupou I.
            tr("'Aho Fakamanatu 'o e Hilifaki Kalauni 'o 'Ene 'Afio ko Siaosi Tupou I")
        )
        if self._year >= 2010:
            self._move_holiday(dec_4)
        else:
            self._add_observed(dec_4)

        # Christmas Day.
        self._add_christmas_day(tr("'Aho Kilisimasi"))

        # Boxing Day.
        dec_26 = self._add_christmas_day_two(tr("'Aho 2 'o e Kilisimasi"))
        if self._year <= 2009:
            self._add_observed(dec_26, rule=MON_TO_NEXT_TUE)


class TO(Tonga):
    pass


class TON(Tonga):
    pass


class TongaStaticHolidays:
    """
    References:
      - https://www.stuff.co.nz/sport/league/99338959/tonga-government-declares-public-holiday-over-rugby-league-teams-deeds  # noqa: E501
      - https://www.rnz.co.nz/international/pacific-news/398653/tonga-declares-public-holiday-for-pm-pohiva-s-state-funeral  # noqa: E501
      - https://www.nrl.com/news/2019/11/06/tonga-declare-public-holiday-for-woolfs-winning-warriors/  # noqa: E501
    """

    # Special Cases.

    # Tonga Rugby Public Holiday.
    rugby_special_holidays = tr("'Aho malolo 'akapulu 'a Tonga")

    special_public_holidays = {
        2017: (NOV, 29, rugby_special_holidays),
        2019: (
            # State Funeral of 'Akilisi Pohiva.
            (SEP, 19, tr("Me'afaka'eiki 'o e Siteiti 'Akilisi Pohiva")),
            (NOV, 15, rugby_special_holidays),
        ),
    }
    # Special Case for 2021
    special_public_holidays_observed = {
        # Boxing Day.
        2021: (DEC, 27, tr("'Aho 2 'o e Kilisimasi")),
    }
