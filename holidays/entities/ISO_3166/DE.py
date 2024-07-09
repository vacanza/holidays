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

"""Official holidays for Germany in its current form.

This class doesn't return any holidays before 1990-10-03.

Before that date the current Germany was separated into the "German
Democratic Republic" and the "Federal Republic of Germany" which both had
somewhat different holidays. Since this class is called "Germany" it
doesn't really make sense to include the days from the two former
countries.

Note that Germany doesn't have rules for holidays that happen on a
Sunday. Those holidays are still holiday days but there is no additional
day to make up for the "lost" day.

Also note that German holidays are partly declared by each province there
are some weired edge cases:

    - "Mariä Himmelfahrt" is only a holiday in Bavaria (BY) if your
      municipality is mostly catholic which in term depends on census data.
      Since we don't have this data but most municipalities in Bavaria
      *are* mostly catholic, we count that as holiday for whole Bavaria.
      We added BYP for the municipality in Bavaria with more protestants.
      Here this is excluded.
    - There is an "Augsburger Friedensfest" which only exists in the town
      Augsburg. This is excluded for Bavaria.
    - "Gründonnerstag" (Thursday before easter) is not a holiday but pupils
       don't have to go to school (but only in Baden Württemberg) which is
       solved by adjusting school holidays to include this day. It is
       excluded from our list.
    - "Fronleichnam" is a holiday in certain, explicitly defined
      municipalities in Saxony (SN) and Thuringia (TH). We exclude it from
      both provinces.
"""

from gettext import gettext as tr

from holidays.calendars.gregorian import MAY, OCT
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class DeHolidays(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """A class to represent holidays for Germany."""

    country = "DE"
    name = "Germany"
    default_language = "de"
    supported_languages = ("de", "en_US", "uk")
    subdivisions = (
        "BB",
        "BE",
        "BW",
        "BY",
        "BYP",
        "HB",
        "HE",
        "HH",
        "MV",
        "NI",
        "NW",
        "RP",
        "SH",
        "SL",
        "SN",
        "ST",
        "TH",
    )

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, DeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            # New Year's Day.
            self._add_new_years_day(tr("Neujahr"))

            # Good Friday.
            self._add_good_friday(tr("Karfreitag"))

            # Easter Monday.
            self._add_easter_monday(tr("Ostermontag"))

            # Labor Day.
            self._add_labor_day(tr("Erster Mai"))

            # Ascension Day.
            self._add_ascension_thursday(tr("Christi Himmelfahrt"))

            # Whit Monday.
            self._add_whit_monday(tr("Pfingstmontag"))

        # German Unity Day.
        self._add_holiday_oct_3(tr("Tag der Deutschen Einheit"))

        if self._year <= 1994:
            # Repentance and Prayer Day.
            self._add_holiday_1st_wed_before_nov_22(tr("Buß- und Bettag"))

        # Christmas Day.
        self._add_christmas_day(tr("Erster Weihnachtstag"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Zweiter Weihnachtstag"))

    def _populate_subdiv_bb_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            # Easter Sunday.
            self._add_easter_sunday(tr("Ostersonntag"))

            # Whit Sunday.
            self._add_whit_sunday(tr("Pfingstsonntag"))

        # Reformation Day.
        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_be_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 2019:
            # International Women's Day.
            self._add_womens_day(tr("Internationaler Frauentag"))

    def _populate_subdiv_bw_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            # Epiphany.
            self._add_epiphany_day(tr("Heilige Drei Könige"))

            # Corpus Christi.
            self._add_corpus_christi_day(tr("Fronleichnam"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_by_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            self._add_epiphany_day(tr("Heilige Drei Könige"))
            self._add_corpus_christi_day(tr("Fronleichnam"))

            # Assumption Day.
            self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_byp_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            self._add_epiphany_day(tr("Heilige Drei Könige"))
            self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_hb_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 2018:
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_he_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))

    def _populate_subdiv_hh_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 2018:
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_mv_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 2023:
            self._add_womens_day(tr("Internationaler Frauentag"))

        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_ni_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 2018:
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_nw_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_rp_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_sh_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 2018:
            self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_sl_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            self._add_corpus_christi_day(tr("Fronleichnam"))
            self._add_assumption_of_mary_day(tr("Mariä Himmelfahrt"))

        self._add_all_saints_day(tr("Allerheiligen"))

    def _populate_subdiv_sn_public_holidays(self):
        if self._year <= 1989:
            return None

        self._add_holiday_oct_31(tr("Reformationstag"))

        if self._year >= 1995:
            self._add_holiday_1st_wed_before_nov_22(tr("Buß- und Bettag"))

    def _populate_subdiv_st_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 1991:
            self._add_epiphany_day(tr("Heilige Drei Könige"))

        self._add_holiday_oct_31(tr("Reformationstag"))

    def _populate_subdiv_th_public_holidays(self):
        if self._year <= 1989:
            return None

        if self._year >= 2019:
            # World Children's Day.
            self._add_holiday_sep_20(tr("Weltkindertag"))

        self._add_holiday_oct_31(tr("Reformationstag"))


class DeStaticHolidays:
    special_public_holidays = {
        2017: (OCT, 31, tr("Reformationstag")),
    }

    special_be_public_holidays = {
        2020: (
            MAY,
            8,
            # 75th anniversary of the liberation from Nazism and
            # the end of the Second World War in Europe.
            tr(
                "75. Jahrestag der Befreiung vom Nationalsozialismus "
                "und der Beendigung des Zweiten Weltkriegs in Europa"
            ),
        ),
    }
