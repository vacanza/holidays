#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td
from typing import Iterable, Set, Tuple

from dateutil.easter import EASTER_ORTHODOX, EASTER_WESTERN, easter
from korean_lunar_calendar import KoreanLunarCalendar

from holidays.calendars import _ChineseLuniSolar, _IslamicLunar
from holidays.calendars import GREGORIAN_CALENDAR, JULIAN_CALENDAR
from holidays.constants import JAN, FEB, MAR, MAY, JUN, AUG, SEP, NOV, DEC


class ChristianHolidays:
    """
    Christian holidays.
    """

    def __init__(self, calendar=GREGORIAN_CALENDAR) -> None:
        self.__verify_calendar(calendar)
        self.__calendar = calendar

    def __get_christmas_day(self, calendar=None):
        """
        Get Christmas Day date.
        """
        calendar = calendar or self.__calendar
        self.__verify_calendar(calendar)

        return (
            date(self._year, DEC, 25)
            if self.__is_gregorian_calendar(calendar)
            else date(self._year, JAN, 7)  # Orthodox.
        )

    def __get_easter_sunday(self, calendar=None):
        """
        Get Easter Sunday date.
        """
        calendar = calendar or self.__calendar
        self.__verify_calendar(calendar)

        return easter(
            self._year,
            method=EASTER_ORTHODOX
            if calendar == JULIAN_CALENDAR
            else EASTER_WESTERN,
        )

    @staticmethod
    def __is_gregorian_calendar(calendar):
        """
        Return True if `calendar` is Gregorian calendar.
        Return False otherwise.
        """
        return calendar == GREGORIAN_CALENDAR

    @staticmethod
    def __verify_calendar(calendar):
        """
        Verify calendar type.
        """
        if calendar not in {GREGORIAN_CALENDAR, JULIAN_CALENDAR}:
            raise ValueError(
                f"Unknown calendar name: {calendar}. "
                "Use `GREGORIAN_CALENDAR` or `JULIAN_CALENDAR`."
            )

    @property
    def _christmas_day(self):
        """
        Return Christmas Day date.
        """
        return self.__get_christmas_day()

    @property
    def _easter_sunday(self):
        """
        Return Easter Sunday date.
        """
        return self.__get_easter_sunday()

    def _add_all_saints_day(self, name) -> date:
        """
        Add All Saints' Day (November 1st).

        Also known as All Hallows' Day, the Feast of All Saints,
        the Feast of All Hallows, the Solemnity of All Saints, and Hallowmas.
        https://en.wikipedia.org/wiki/All_Saints%27_Day
        """
        return self._add_holiday(name, NOV, 1)

    def _add_all_souls_day(self, name) -> date:
        """
        Add All Souls' Day (November 2nd).

        All Souls' Day is a day of prayer and remembrance for the faithful
        departed, observed by certain Christian denominations on 2 November.
        https://en.wikipedia.org/wiki/All_Souls%27_Day
        """
        return self._add_holiday(name, NOV, 2)

    def _add_ascension_thursday(self, name) -> date:
        """
        Add Ascension Thursday (39 days after the Easter Sunday).

        The Solemnity of the Ascension of Jesus Christ, also called Ascension
        Day, or sometimes Holy Thursday.
        https://en.wikipedia.org/wiki/Feast_of_the_Ascension
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=+39),
        )

    def _add_ash_monday(self, name) -> date:
        """
        Add Ash Monday (48 days before Easter Sunday).

        The Clean Monday, also known as Pure Monday, Monday of Lent
        or Green Monday. The first day of Great Lent.
        https://en.wikipedia.org/wiki/Clean_Monday
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=-48),
        )

    def _add_ash_wednesday(self, name) -> date:
        """
        Add Ash Wednesday (46 days before Easter Sunday).

        A holy day of prayer and fasting. It marks the beginning of Lent.
        https://en.wikipedia.org/wiki/Ash_Wednesday
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=-46),
        )

    def _add_assumption_of_mary_day(self, name) -> date:
        """
        Add Assumption Of Mary (August 15th).

        The Feast of the Assumption of Mary, or simply The Assumption marks the
        occasion of the Virgin Mary's bodily ascent to heaven at the end of
        her life.
        https://en.wikipedia.org/wiki/Assumption_of_Mary
        """
        return self._add_holiday(name, AUG, 15)

    def _add_candlemas(self, name) -> date:
        """
        Add Candlemas (February 2nd).

        Also known as the Feast of the Presentation of Jesus Christ,
        the Feast of the Purification of the Blessed Virgin Mary, or the Feast
        of the Holy Encounter, is a Christian holiday commemorating the
        presentation of Jesus at the Temple.
        https://en.wikipedia.org/wiki/Candlemas
        """
        return self._add_holiday(name, FEB, 2)

    def _add_carnival_monday(self, name) -> date:
        """
        Add Carnival Monday (48 days before Easter Sunday).

        Carnival is a Catholic Christian festive season that occurs before
        the liturgical season of Lent.
        https://en.wikipedia.org/wiki/Carnival
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=-48),
        )

    def _add_carnival_tuesday(self, name) -> date:
        """
        Add Carnival Monday (47 days before Easter Sunday).

        Carnival is a Catholic Christian festive season that occurs before
        the liturgical season of Lent.
        https://en.wikipedia.org/wiki/Carnival
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=-47),
        )

    def _add_christmas_day(self, name, calendar=None) -> date:
        """
        Add Christmas Day.

        Christmas is an annual festival commemorating the birth of
        Jesus Christ.
        https://en.wikipedia.org/wiki/Christmas
        """
        calendar = calendar or self.__calendar
        self.__verify_calendar(calendar)

        return self._add_holiday(
            name,
            self.__get_christmas_day(calendar),
        )

    def _add_christmas_day_two(self, name, calendar=None) -> date:
        """
        Add Christmas Day 2.

        A holiday celebrated after Christmas Day, also known as Boxing Day.
        https://en.wikipedia.org/wiki/Boxing_Day
        https://en.wikipedia.org/wiki/Christmas
        """
        calendar = calendar or self.__calendar
        self.__verify_calendar(calendar)

        return self._add_holiday(
            name,
            self.__get_christmas_day(calendar) + td(days=+1),
        )

    def _add_christmas_day_three(self, name, calendar=None) -> date:
        """
        Add Christmas Day 3.

        A holiday celebrated 2 days after Christmas Day (in some countries).
        https://en.wikipedia.org/wiki/Christmas
        """
        calendar = calendar or self.__calendar
        self.__verify_calendar(calendar)

        return self._add_holiday(
            name,
            self.__get_christmas_day(calendar) + td(days=+2),
        )

    def _add_christmas_eve(self, name, calendar=None) -> date:
        """
        Add Christmas Eve.

        Christmas Eve is the evening or entire day before Christmas Day,
        the festival commemorating the birth of Jesus Christ.
        https://en.wikipedia.org/wiki/Christmas_Eve
        """
        calendar = calendar or self.__calendar
        self.__verify_calendar(calendar)

        return self._add_holiday(
            name,
            self.__get_christmas_day(calendar) + td(days=-1),
        )

    def _add_corpus_christi_day(self, name) -> date:
        """
        Add Feast Of Corpus Christi (60 days after Easter Sunday).

        The Feast of Corpus Christi, also known as the Solemnity of the Most
        Holy Body and Blood of Christ, is a Christian liturgical solemnity
        celebrating the Real Presence of the Body and Blood, Soul and Divinity
        of Jesus Christ in the elements of the Eucharist.
        https://en.wikipedia.org/wiki/Feast_of_Corpus_Christi
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=+60),
        )

    def _add_easter_monday(self, name, calendar=None) -> date:
        """
        Add Easter Monday (1 day after Easter Sunday).

        Easter Monday refers to the day after Easter Sunday in either the
        Eastern or Western Christian traditions. It is a public holiday in
        some countries.
        https://en.wikipedia.org/wiki/Easter_Monday
        """
        return self._add_holiday(
            name,
            self.__get_easter_sunday(calendar) + td(days=+1),
        )

    def _add_easter_sunday(self, name, calendar=None) -> date:
        """
        Add Easter Sunday.

        Easter, also called Pascha or Resurrection Sunday is a Christian
        festival and cultural holiday commemorating the resurrection of Jesus
        from the dead.
        https://en.wikipedia.org/wiki/Easter
        """
        return self._add_holiday(name, self.__get_easter_sunday(calendar))

    def _add_epiphany_day(self, name, calendar=None) -> date:
        """
        Add Epiphany Day.

        Epiphany, also known as Theophany in Eastern Christian traditions,
        is a Christian feast day that celebrates the revelation of God
        incarnate as Jesus Christ.
        https://en.wikipedia.org/wiki/Epiphany_(holiday)
        """
        calendar = calendar or self.__calendar
        self.__verify_calendar(calendar)

        return self._add_holiday(
            name,
            date(self._year, JAN, 6)
            if self.__is_gregorian_calendar(calendar)
            else date(self._year, JAN, 19),
        )

    def _add_good_friday(self, name, calendar=None) -> date:
        """
        Add Good Friday (2 days before Easter Sunday).

        Good Friday is a Christian holiday commemorating the crucifixion of
        Jesus and his death at Calvary. It is also known as Holy Friday,
        Great Friday, Great and Holy Friday.
        https://en.wikipedia.org/wiki/Good_Friday
        """
        return self._add_holiday(
            name,
            self.__get_easter_sunday(calendar) + td(days=-2),
        )

    def _add_holy_saturday(self, name) -> date:
        """
        Add Holy Saturday (1 day before Easter Sunday).

        Great and Holy Saturday is a day between Good Friday and Easter Sunday.
        https://en.wikipedia.org/wiki/Holy_Saturday
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=-1),
        )

    def _add_holy_thursday(self, name) -> date:
        """
        Add Holy Thursday (3 days before Easter Sunday).

        Holy Thursday or Maundy Thursday is the day during Holy Week that
        commemorates the Washing of the Feet (Maundy) and Last Supper of
        Jesus Christ with the Apostles, as described in the canonical gospels.
        https://en.wikipedia.org/wiki/Maundy_Thursday
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=-3),
        )

    def _add_immaculate_conception_day(self, name) -> date:
        """
        Add Immaculate Conception Day (December 8th).

        https://en.wikipedia.org/wiki/Immaculate_Conception
        """
        return self._add_holiday(name, DEC, 8)

    def _add_nativity_of_mary_day(self, name) -> date:
        """
        Add Nativity Of Mary Day (September 8th).

        The Nativity of the Blessed Virgin Mary, the Nativity of Mary,
        the Marymas or the Birth of the Virgin Mary, refers to a Christian
        feast day celebrating the birth of Mary, mother of Jesus.
        https://en.wikipedia.org/wiki/Nativity_of_Mary
        """
        return self._add_holiday(name, SEP, 8)

    def _add_palm_sunday(self, name) -> date:
        """
        Add Palm Sunday (7 days before Easter Sunday).

        Palm Sunday is a Christian moveable feast that falls on the Sunday
        before Easter. The feast commemorates Christ's triumphal entry into
        Jerusalem, an event mentioned in each of the four canonical Gospels.
        Palm Sunday marks the first day of Holy Week.
        https://en.wikipedia.org/wiki/Palm_Sunday
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=-7),
        )

    def _add_rejoicing_day(self, name) -> date:
        """
        Add Day Of Rejoicing (9 days after Easter Sunday).

        Add Day Of Rejoicing ("Radonitsa"), in the Russian Orthodox Church is
        a commemoration of the departed observed on the second Tuesday of
        Pascha (Easter).In Ukrainian tradition it is called Provody.
        https://en.wikipedia.org/wiki/Radonitsa
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=+9),
        )

    def _add_saint_johns_day(self, name) -> date:
        """
        Add Saint John's Day (June 24th).

        The Nativity of John the Baptist is a Christian feast day celebrating
        the birth of John the Baptist.
        https://en.wikipedia.org/wiki/Nativity_of_John_the_Baptist
        """
        return self._add_holiday(name, JUN, 24)

    def _add_saint_josephs_day(self, name) -> date:
        """
        Add Saint Joseph's Day (March 19th).

        Saint Joseph's Day, also called the Feast of Saint Joseph or the
        Solemnity of Saint Joseph, is in Western Christianity the principal
        feast day of Saint Joseph, husband of the Virgin Mary and legal father
        of Jesus Christ.
        https://en.wikipedia.org/wiki/Saint_Joseph%27s_Day
        """
        return self._add_holiday(name, MAR, 19)

    def _add_saints_peter_and_paul_day(self, name) -> date:
        """
        Feast of Saints Peter and Paul (June 29th).

        A liturgical feast in honor of the martyrdom in Rome of the apostles
        Saint Peter and Saint Paul, which is observed on 29 June.
        https://en.wikipedia.org/wiki/Feast_of_Saints_Peter_and_Paul
        """
        return self._add_holiday(name, JUN, 29)

    def _add_whit_monday(self, name) -> date:
        """
        Add Whit Monday (50 days after Easter Sunday).

        Whit Monday or Pentecost Monday, also known as Monday of the
        Holy Spirit, is the holiday celebrated the day after Pentecost.
        https://en.wikipedia.org/wiki/Pentecost
        https://en.wikipedia.org/wiki/Whit_Monday
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=+50),
        )

    def _add_whit_sunday(self, name) -> date:
        """
        Add Whit Sunday (49 days after Easter Sunday).

        Whit Sunday, also called Pentecost, is a holiday which commemorates
        the descent of the Holy Spirit upon the Apostles and other followers
        of Jesus Christ while they were in Jerusalem celebrating the
        Feast of Weeks.
        https://en.wikipedia.org/wiki/Pentecost
        """
        return self._add_holiday(
            name,
            self._easter_sunday + td(days=+49),
        )


class ChineseCalendarHolidays:
    """
    Chinese lunisolar calendar holidays.
    """

    def __init__(self) -> None:
        self._chinese_calendar = _ChineseLuniSolar()

    @property
    def _chinese_new_year(self):
        """
        Return Chinese New Year date.
        """
        return self._chinese_calendar.lunar_n_y_date(self._year)

    def _add_dragon_boat_festival(self, name) -> date:
        """
        Add Dragon Boat Festival (5th day of 5th lunar month).

        The Dragon Boat Festival is a traditional Chinese holiday which occurs
        on the fifth day of the fifth month of the Chinese calendar.
        https://en.wikipedia.org/wiki/Dragon_Boat_Festival
        """
        return self._add_chinese_calendar_holiday(name, 5, 5)

    def _add_chinese_calendar_holiday(self, name, month, day) -> date:
        """
        Add Chinese lunar calendar holiday.
        """
        return self._add_holiday(
            name,
            self._convert_chinese_to_gre(month, day),
        )

    def _add_chinese_new_years_eve(self, name) -> date:
        """
        Add Chinese New Year's Eve (last day of 12th lunar month).

        Chinese New Year's Eve is the day before the Chinese New Year.
        https://en.wikipedia.org/wiki/Chinese_New_Year%27s_Eve
        """
        return self._add_holiday(
            name,
            self._chinese_new_year + td(days=-1),
        )

    def _add_chinese_new_years_day(self, name) -> date:
        """
        Add Chinese New Year's Day (first day of the first lunar month).

        Chinese New Year is the festival that celebrates the beginning of
        a new year on the traditional lunisolar and solar Chinese calendar.
        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_holiday(
            name,
            self._chinese_new_year,
        )

    def _add_chinese_new_years_day_two(self, name) -> date:
        """
        Add Chinese New Year's Day Two.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_holiday(
            name,
            self._chinese_new_year + td(days=+1),
        )

    def _add_chinese_new_years_day_three(self, name) -> date:
        """
        Add Chinese New Year's Day Three.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_holiday(
            name,
            self._chinese_new_year + td(days=+2),
        )

    def _add_chinese_new_years_day_four(self, name) -> date:
        """
        Add Chinese New Year's Day Four.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_holiday(
            name,
            self._chinese_new_year + td(days=+3),
        )

    def _add_chinese_new_years_day_five(self, name) -> date:
        """
        Add Chinese New Year's Day Five.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_holiday(
            name,
            self._chinese_new_year + td(days=+4),
        )

    def _add_mid_autumn_festival(self, name):
        """
        Add Mid Autumn Festival (15th day of the 8th lunar month).

        The Mid-Autumn Festival, also known as the Moon Festival or
        Mooncake Festival.
        https://en.wikipedia.org/wiki/Mid-Autumn_Festival
        """
        return self._add_chinese_calendar_holiday(name, 8, 15)

    def _convert_chinese_to_gre(self, month, day):
        """
        Convert lunar calendar date to Gregorian calendar date.
        """
        return self._chinese_calendar.lunar_to_gre(self._year, month, day)


class InternationalHolidays:
    """
    International holidays.
    """

    def _add_labor_day(self, name):
        """
        Add International Workers' Day (May 1st)

        International Workers' Day, also known as Labour Day, is a celebration
        of labourers and the working classes that is promoted by the
        international labour movement.
        https://en.wikipedia.org/wiki/International_Workers%27_Day
        """
        return self._add_holiday(name, MAY, 1)

    def _add_new_years_day(self, name) -> date:
        """
        Add New Year's Day (January 1st).

        New Year's Day is a festival observed in most of the world on
        1 January, the first day of the year in the modern Gregorian calendar.
        https://en.wikipedia.org/wiki/New_Year%27s_Day
        """
        return self._add_holiday(name, JAN, 1)

    def _add_new_years_day_two(self, name) -> date:
        """
        Add New Year's Day Two (January 2nd).

        New Year's Day is a festival observed in most of the world on
        1 January, the first day of the year in the modern Gregorian calendar.
        https://en.wikipedia.org/wiki/New_Year%27s_Day
        """
        return self._add_holiday(name, JAN, 2)

    def _add_new_years_day_three(self, name) -> date:
        """
        Add New Year's Day Three (January 3rd).

        New Year's Day is a festival observed in most of the world on
        1 January, the first day of the year in the modern Gregorian calendar.
        https://en.wikipedia.org/wiki/New_Year%27s_Day
        """
        return self._add_holiday(name, JAN, 3)

    def _add_new_years_day_four(self, name) -> date:
        """
        Add New Year's Day Four (January 4th).

        New Year's Day is a festival observed in most of the world on
        1 January, the first day of the year in the modern Gregorian calendar.
        https://en.wikipedia.org/wiki/New_Year%27s_Day
        """
        return self._add_holiday(name, JAN, 4)

    def _add_remembrance_day(self, name):
        """
        Add Remembrance Day / Armistice Day (Nov 11th)

        It's a memorial day since the end of the First World War in 1919
        to honour armed forces members who have died in the line of duty.
        https://en.wikipedia.org/wiki/Remembrance_Day
        """
        return self._add_holiday(name, NOV, 11)

    def _add_new_years_eve(self, name) -> date:
        """
        Add New Year's Eve (December 31st).

        In the Gregorian calendar, New Year's Eve, also known as Old Year's
        Day or Saint Sylvester's Day in many countries, is the evening or the
        entire day of the last day of the year, on 31 December.
        https://en.wikipedia.org/wiki/New_Year%27s_Eve
        """
        return self._add_holiday(name, DEC, 31)

    def _add_womens_day(self, name):
        """
        Add International Women's Day (March 8th).

        International Women's Day is a global holiday celebrated as a focal
        point in the women's rights movement, bringing attention to issues
        such as gender equality, reproductive rights, and violence and abuse
        against women.
        https://en.wikipedia.org/wiki/International_Women%27s_Day
        """
        return self._add_holiday(name, MAR, 8)

    def _add_world_war_two_victory_day(self, name):
        """
        Add Victory Day (May 9th)

        Victory Day is a holiday that commemorates the victory over Nazi
        Germany in 1945.
        https://en.wikipedia.org/wiki/Victory_Day_(9_May)
        """
        return self._add_holiday(name, MAY, 9)


class IslamicHolidays:
    """
    Islamic holidays.

    The Hijri calendar also known as Islamic calendar, is a lunar
    calendar consisting of 12 lunar months in a year of 354 or 355 days.
    """

    def __init__(self, calendar=_IslamicLunar()) -> None:
        self._islamic_calendar = calendar

    def _add_arafah_day(self, name) -> Set[date]:
        """
        Add Day of Arafah (9th day of 12th month).

        At dawn of this day, Muslim pilgrims will make their way from Mina
        to a nearby hillside and plain called Mount Arafat and the Plain of
        Arafat.
        https://en.wikipedia.org/wiki/Day_of_Arafah
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_adha_dates(self._year),
            days_delta=-1,
        )

    def _add_ashura_day(self, name) -> Set[date]:
        """
        Add Ashura Day (10th day of 1st month).

        Ashura is a day of commemoration in Islam. It occurs annually on the
        10th of Muharram, the first month of the Islamic calendar.
        https://en.wikipedia.org/wiki/Ashura
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.ashura_dates(self._year),
        )

    def _add_ashura_eve(self, name) -> Set[date]:
        """
        Add Ashura Eve (Day before the 10th day of 1st month).

        Ashura is a day of commemoration in Islam. It occurs annually on the
        10th of Muharram, the first month of the Islamic calendar.
        https://en.wikipedia.org/wiki/Ashura
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.ashura_dates(self._year),
            days_delta=-1,
        )

    def _add_eid_al_adha_day(self, name) -> Set[date]:
        """
        Add Eid al-Adha Day (10th day of the 12th month of Islamic calendar).

        Feast of the Sacrifice. It honours the willingness of Ibrahim
        (Abraham) to sacrifice his son Ismail (Ishmael) as an act of obedience
        to Allah's command.
        https://en.wikipedia.org/wiki/Eid_al-Adha
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_adha_dates(self._year),
        )

    def _add_eid_al_adha_day_two(self, name) -> Set[date]:
        """
        Add Eid al-Adha Day Two.

        https://en.wikipedia.org/wiki/Eid_al-Adha
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_adha_dates(self._year),
            days_delta=+1,
        )

    def _add_eid_al_adha_day_three(self, name) -> Set[date]:
        """
        Add Eid al-Adha Day Three.

        https://en.wikipedia.org/wiki/Eid_al-Adha
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_adha_dates(self._year),
            days_delta=+2,
        )

    def _add_eid_al_adha_day_four(self, name) -> Set[date]:
        """
        Add Eid al-Adha Day Four.

        https://en.wikipedia.org/wiki/Eid_al-Adha
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_adha_dates(self._year),
            days_delta=+3,
        )

    def _add_eid_al_fitr_day(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Day (1st day of 10th month of Islamic calendar).

        Holiday of Breaking the Fast. The religious holiday is celebrated
        by Muslims worldwide because it marks the end of the month-long
        dawn-to-sunset fasting of Ramadan.
        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_fitr_dates(self._year),
        )

    def _add_eid_al_fitr_day_two(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Day Two.

        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_fitr_dates(self._year),
            days_delta=+1,
        )

    def _add_eid_al_fitr_day_three(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Day Three.

        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_fitr_dates(self._year),
            days_delta=+2,
        )

    def _add_eid_al_fitr_day_four(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Day Four.

        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.eid_al_fitr_dates(self._year),
            days_delta=+3,
        )

    def _add_hari_hol_johor(self, name) -> Set[date]:
        """
        Hari Hol Johor.

        https://publicholidays.com.my/hari-hol-almarhum-sultan-iskandar/
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.hari_hol_johor_dates(self._year),
        )

    def _add_islamic_calendar_holiday(
        self,
        name: str,
        dates: Iterable[Tuple[date, bool]],
        days_delta: int = 0,
    ) -> Set[date]:
        """
        Add lunar calendar holiday.

        Appends customizable estimation label at the end of holiday name if
        holiday date is an estimation.
        """
        added_dates = set()
        estimated_label = getattr(self, "estimated_label", "estimated")
        for dt, is_estimated in dates:
            if days_delta != 0:
                dt += td(days=days_delta)
            dt = self._add_holiday(
                f"{name}* (*{estimated_label})" if is_estimated else name,
                dt,
            )
            if dt:
                added_dates.add(dt)

        return added_dates

    def _add_islamic_new_year_day(self, name) -> Set[date]:
        """
        Add Islamic New Year Day (last day of Dhu al-Hijjah).

        The Islamic New Year, also called the Hijri New Year, is the day that
        marks the beginning of a new lunar Hijri year, and is the day on which
        the year count is incremented. The first day of the Islamic year is
        observed by most Muslims on the first day of the month of Muharram.
        https://en.wikipedia.org/wiki/Islamic_New_Year
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.hijri_new_year_dates(self._year),
        )

    def _add_isra_and_miraj_day(self, name):
        """
        Add Isra' and Mi'raj Day (27th day of 7th month).

        https://en.wikipedia.org/wiki/Isra%27_and_Mi%27raj
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.isra_and_miraj_dates(self._year),
        )

    def _add_mawlid_day(self, name) -> Set[date]:
        """
        Add Mawlid Day (12th day of 3rd month).

        Mawlid is the observance of the birthday of the Islamic prophet
        Muhammad.
        https://en.wikipedia.org/wiki/Mawlid
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.mawlid_dates(self._year),
        )

    def _add_mawlid_day_two(self, name) -> Set[date]:
        """
        Add Mawlid Day Two.

        Mawlid is the observance of the birthday of the Islamic prophet
        Muhammad.
        https://en.wikipedia.org/wiki/Mawlid
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.mawlid_dates(self._year),
            days_delta=+1,
        )

    def _add_nuzul_al_quran_day(self, name) -> Set[date]:
        """
        Add Nuzul Al Quran (17th day of 9th month).

        Nuzul Al Quran is a Muslim festival to remember the day when Prophet
        Muhammad received his first revelation of Islam's sacred book,
        the holy Quran.
        https://zamzam.com/blog/nuzul-al-quran/
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.nuzul_al_quran_dates(self._year),
        )

    def _add_ramadan_beginning_day(self, name) -> Set[date]:
        """
        Add First Day of Ramadan (1st day of 9th month).

        Ramadan is the ninth month of the Islamic calendar, observed by Muslims
        worldwide as a month of fasting, prayer, reflection, and community
        https://en.wikipedia.org/wiki/Ramadan
        """
        return self._add_islamic_calendar_holiday(
            name,
            self._islamic_calendar.ramadan_beginning_dates(self._year),
        )


class KoreanCalendarHolidays:
    """
    Korean lunisolar calendar holidays.
    """

    def __init__(self) -> None:
        self._korean_calendar = KoreanLunarCalendar()

    @property
    def _korean_new_year(self):
        """
        Return Korean Lunisolar calendar New Year date.
        """
        return self._convert_korean_to_gre(self._year, 1, 1)

    def _add_korean_calendar_holiday(self, name, month, day) -> date:
        """
        Add lunar calendar holiday.
        """
        return self._add_holiday(
            name,
            self._convert_korean_to_gre(self._year, month, day),
        )

    def _add_korean_new_years_day(self, name) -> date:
        """
        Add Korean New Years Day (second new moon after the winter solstice).

        Korean New Year, Seollal is a festival and national holiday
        commemorating the first day of the Chinese lunisolar calendar.
        https://en.wikipedia.org/wiki/Korean_New_Year
        """
        return self._add_holiday(
            name,
            self._korean_new_year,
        )

    def _add_korean_new_years_day_two(self, name) -> date:
        """
        Add Korean New Years Day Two (1 day after New Years Day).

        https://en.wikipedia.org/wiki/Korean_New_Year
        """
        return self._add_holiday(
            name,
            self._korean_new_year + td(days=+1),
        )

    def _add_korean_new_years_day_three(self, name) -> date:
        """
        Add Korean New Years Day Three (2 days after New Years Day).

        https://en.wikipedia.org/wiki/Korean_New_Year
        """
        return self._add_holiday(
            name,
            self._korean_new_year + td(days=+2),
        )

    def _add_korean_new_years_day_four(self, name) -> date:
        """
        Add Korean New Years Day Four (3 days after New Years Day).

        https://en.wikipedia.org/wiki/Korean_New_Year
        """
        return self._add_holiday(
            name,
            self._korean_new_year + td(days=+3),
        )

    def _add_korean_new_years_day_five(self, name) -> date:
        """
        Add Korean New Years Day Five (4 days after New Years Day).

        https://en.wikipedia.org/wiki/Korean_New_Year
        """
        return self._add_holiday(
            name,
            self._korean_new_year + td(days=+4),
        )

    def _add_korean_new_years_eve(self, name) -> date:
        """
        Add Korean New Years Eve (1 day before New Years Day).

        https://en.wikipedia.org/wiki/Korean_New_Year
        """
        return self._add_holiday(
            name,
            self._korean_new_year + td(days=-1),
        )

    def _convert_korean_to_gre(self, year: int, month: int, day: int) -> date:
        """
        Get solar date.
        """
        self._korean_calendar.setLunarDate(year, month, day, False)
        return date(
            self._korean_calendar.solarYear,
            self._korean_calendar.solarMonth,
            self._korean_calendar.solarDay,
        )
