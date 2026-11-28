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

from holidays.calendars.gregorian import JAN, APR, JUL, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class Kiribati(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """Kiribati holidays.

    References:
        * [Public Holidays Ordinance](https://web.archive.org/web/20250130150749/https://www.paclii.org/ki/legis/consol_act/pho216/)
        * [Public Holidays (Amendment) Act 2002](https://web.archive.org/web/20250130161614/https://www.paclii.org/ki/legis/num_act/pha2002243/)
        * [Public Holidays Act Consolidated](https://web.archive.org/web/20250404213705/https://www.paclii.org/ki/legis/consol_act/pho216.pdf)
        * [Revised National Public Holiday Order 2025](https://www.president.gov.ki/images/Gazettes/2025/PH_2025_revised_181225.pdf)
        * [National Public Holiday Order 2026](https://www.president.gov.ki/images/Gazettes/2025/PH_2026_181225.pdf)
    Note:
        The 2025 holidays list for Kiribati
        (http://web.archive.org/web/20250808191339/https://www.pso.gov.ki/kiribati-national-public-holidays-2025/)
        mentions the following holidays even though they do not appear in the law:
        Labor Day, National Culture and Senior Citizens Day, National Police Day, and World
        Teachers' Day.

        The 2025 and 2026 orders state that Section 2 holidays not listed remain public holidays.
        Holidays listed at changed dates use the Gazette dates for those years, while unlisted
        statutory holidays remain. Distinct Gazette appointments sharing a date with statutory
        holidays retain both names. New appointments are limited to the order years.
    """

    country = "KI"
    observed_label = "%s (observed)"
    start_year = 1980

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        StaticHolidays.__init__(self, KiribatiStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        is_gazette_year = self._year in (2025, 2026)

        self._populate_january_to_june_holidays(is_gazette_year)
        self._populate_july_holidays()
        self._populate_august_to_december_holidays(is_gazette_year)

    def _populate_january_to_june_holidays(self, is_gazette_year):
        # New Year's Day.
        self._add_observed(self._add_new_years_day("New Year's Day"))

        if self._year >= 2003:
            if self._year == 2025:
                self._add_holiday_mar_7("In honour of International Women's Day")
            elif self._year == 2026:
                self._add_holiday_mar_9("In honour of International Women's Day")
            else:
                # International Women's Day.
                self._add_observed(self._add_womens_day("International Women's Day"))

        # Good Friday.
        self._add_good_friday("Good Friday")

        if self._year <= 2002:
            # Holy Saturday.
            self._add_holy_saturday("Holy Saturday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        if is_gazette_year:
            # The annual orders appoint National Health Day on April 7.
            self._add_holiday_apr_7("National Health Day")
        elif self._year >= 2003:
            # National Health Day.
            self._add_observed(self._add_holiday_apr_19("National Health Day"))

        if is_gazette_year:
            self._add_holiday_1st_fri_from_may_1(
                "In honour of International Labour Day"
                if self._year == 2025
                else "International Labour Day"
            )
            self._add_holiday_4th_mon_of_jun("In honour of National Police Day")

        if 1993 <= self._year <= 2002:
            # Public Holiday.
            self._add_observed(self._add_holiday_may_9("Public Holiday"))

    def _populate_july_holidays(self):
        if self._year >= 2002:
            # Gospel Day.
            if self._year == 2026:
                self._add_holiday_jul_10("Gospel Day")
            else:
                self._add_holiday_jul_11("Gospel Day")

        if self._year >= 1993:
            # National Day - Independence Anniversary.
            self._add_observed(self._add_holiday_jul_12("National Day - Independence Anniversary"))

        # These separate Gazette appointments can share dates with Section 2 holidays below.
        culture_days = {
            2025: ((JUL, 15), "National Culture and Senior Citizens Day"),
            2026: ((JUL, 14), "Kiribati Culture and Senior Citizens Day"),
        }
        if self._year in culture_days:
            dt, name = culture_days[self._year]
            self._add_holiday(name, dt)

        special_days = {
            2025: (JUL, 16),
            2026: (JUL, 15),
        }
        if self._year in special_days:
            self._add_holiday("Kiribati Special Day", special_days[self._year])

        if self._year >= 2002:
            # National Day (in honor of Unimwane).
            self._add_holiday_jul_15("National Day (in honor of Unimwane)")
            # National Day (in honor of Unaine).
            self._add_observed(self._add_holiday_jul_16("National Day (in honor of Unaine)"))

    def _populate_august_to_december_holidays(self, is_gazette_year):
        self._populate_august_holidays(is_gazette_year)
        self._populate_november_holiday()
        self._populate_december_holidays(is_gazette_year)

    def _populate_august_holidays(self, is_gazette_year):
        if self._year <= 2002:
            # Public Holiday.
            self._add_holiday_1st_mon_of_aug("Public Holiday")
        else:
            # Youth Day remains a Section 2 holiday, though omitted from the annual orders.
            self._add_observed(self._add_holiday_aug_5("Youth Day"))

        if is_gazette_year:
            if self._year == 2025:
                self._add_holiday_aug_1("In honor of National Youth & Children's Day")
                self._add_holiday_oct_6("In honour of World Teachers Day")
            else:
                self._add_holiday_aug_3("National Youth & Children's Day")
                self._add_holiday_oct_5("World Teachers Day")

    def _populate_november_holiday(self):
        if self._year <= 1992:
            # Public Holiday.
            self._add_observed(self._add_holiday_nov_10("Public Holiday"))

    def _populate_december_holidays(self, is_gazette_year):
        if self._year >= 1993:
            # Human Rights and Peace Day.
            name = "Human Rights and Peace Day"
            if is_gazette_year:
                self._add_holiday_1st_fri_from_dec_10("In honour of Human Rights Day")
            else:
                self._add_observed(
                    self._add_holiday_dec_9(name)
                    if self._year >= 2003
                    else self._add_holiday_dec_10(name)
                )

        if is_gazette_year:
            for day in (29, 30, 31):
                self._add_holiday("Kiribati Holiday", (DEC, day))

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Boxing Day.
        self._add_observed(self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)


class KiribatiStaticHolidays:
    """One-off public holidays appointed by Kiribati's annual Gazette orders."""

    special_public_holidays = {
        2025: ((APR, 25, "Special Day in honour of Pope Francis"),),
        2026: (
            (JAN, 2, "Kiribati Holiday"),
            (DEC, 28, "In honour of Boxing Day (Gift Day)"),
        ),
    }


class KI(Kiribati):
    pass


class KIR(Kiribati):
    pass
