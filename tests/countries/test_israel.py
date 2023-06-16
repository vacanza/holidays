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
from datetime import timedelta as td

from holidays.countries.israel import Israel, IL, ISR
from tests.common import TestCase


class TestIsrael(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Israel)

    def _test_observed_holidays(self, holiday_name):
        days_delta = 0 if holiday_name == "Memorial Day" else 1

        # Postponed
        official_holiday = date(2017, 4, 30) + td(days=days_delta)
        observed_holiday = official_holiday + td(days=+1)
        self.assertNotIn(holiday_name, self.holidays.get(official_holiday, ""))
        self.assertHoliday(observed_holiday)
        self.assertHolidayName(f"{holiday_name} (Observed)", observed_holiday)

        # Earlier
        official_holiday = date(2018, 4, 19) + td(days=days_delta)
        observed_holiday = official_holiday + td(days=-1)
        self.assertHoliday(observed_holiday)
        self.assertNotIn(holiday_name, self.holidays.get(official_holiday, ""))
        self.assertHolidayName(f"{holiday_name} (Observed)", observed_holiday)

        # On time
        official_holiday = date(2020, 4, 28) + td(days=days_delta)
        self.assertHoliday(observed_holiday)
        self.assertHolidayName(holiday_name, official_holiday)
        self.assertNoHolidayName(f"{holiday_name} (Observed)", 2020)

    def _test_nonobserved_holidays(self, holiday_name):
        days_delta = 0 if holiday_name == "Memorial Day" else 1

        # Postponed
        official_holiday = date(2017, 4, 30) + td(days=days_delta)
        observed_holiday = official_holiday + td(days=+1)
        self.assertNonObservedHoliday(official_holiday)
        self.assertNonObservedHolidayName(holiday_name, official_holiday)
        self.assertNotEqual(self.holidays_non_observed.get(observed_holiday), holiday_name)

        # Earlier
        official_holiday = date(2018, 4, 19) + td(days=days_delta)
        observed_holiday = official_holiday + td(days=-1)
        self.assertNonObservedHoliday(official_holiday)
        self.assertNonObservedHolidayName(holiday_name, official_holiday)
        self.assertNoNonObservedHoliday(observed_holiday)

        # On time
        official_holiday = date(2020, 4, 28) + td(days=days_delta)
        self.assertNonObservedHoliday(official_holiday)
        self.assertNonObservedHolidayName(holiday_name, official_holiday)
        self.assertNoNonObservedHolidayName(f"{holiday_name} (Observed)", 2020)

    def test_country_aliases(self):
        self.assertCountryAliases(Israel, IL, ISR)

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            Israel(years=2101)

    def test_no_holidays(self):
        self.assertNoHolidays(Israel(years=1947))

    def test_purim_day(self):
        self.assertHolidayName("Purim - Eve", "2017-03-11")
        self.assertHolidayName("Purim", "2017-03-12")
        self.assertHolidayName("Shushan Purim", "2017-03-13")

    def test_memorial_day(self):
        self._test_observed_holidays("Memorial Day")
        self._test_nonobserved_holidays("Memorial Day")

    def test_independence_day(self):
        self._test_observed_holidays("Independence Day")

    def test_2021(self):
        self.assertHolidays(
            ("2021-02-25", "Purim - Eve"),
            ("2021-02-26", "Purim"),
            ("2021-02-27", "Shushan Purim"),
            ("2021-03-27", "Passover I - Eve"),
            ("2021-03-28", "Passover I"),
            ("2021-03-29", "Passover - Chol HaMoed"),
            ("2021-03-30", "Passover - Chol HaMoed"),
            ("2021-03-31", "Passover - Chol HaMoed"),
            ("2021-04-01", "Passover - Chol HaMoed"),
            ("2021-04-02", "Passover VII - Eve"),
            ("2021-04-03", "Passover VII"),
            ("2021-04-14", "Memorial Day (Observed)"),
            ("2021-04-15", "Independence Day (Observed)"),
            ("2021-04-30", "Lag B'Omer"),
            ("2021-05-16", "Shavuot - Eve"),
            ("2021-05-17", "Shavuot"),
            ("2021-09-06", "Rosh Hashanah - Eve"),
            ("2021-09-07", "Rosh Hashanah"),
            ("2021-09-08", "Rosh Hashanah"),
            ("2021-09-15", "Yom Kippur - Eve"),
            ("2021-09-16", "Yom Kippur"),
            ("2021-09-20", "Sukkot I - Eve"),
            ("2021-09-21", "Sukkot I"),
            ("2021-09-22", "Sukkot - Chol HaMoed"),
            ("2021-09-23", "Sukkot - Chol HaMoed"),
            ("2021-09-24", "Sukkot - Chol HaMoed"),
            ("2021-09-25", "Sukkot - Chol HaMoed"),
            ("2021-09-26", "Sukkot - Chol HaMoed"),
            ("2021-09-27", "Sukkot VII - Eve"),
            ("2021-09-28", "Sukkot VII"),
            ("2021-11-29", "Hanukkah"),
            ("2021-11-30", "Hanukkah"),
            ("2021-12-01", "Hanukkah"),
            ("2021-12-02", "Hanukkah"),
            ("2021-12-03", "Hanukkah"),
            ("2021-12-04", "Hanukkah"),
            ("2021-12-05", "Hanukkah"),
            ("2021-12-06", "Hanukkah"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-03-16", "Purim - Eve"),
            ("2022-03-17", "Purim"),
            ("2022-03-18", "Shushan Purim"),
            ("2022-04-15", "Passover I - Eve"),
            ("2022-04-16", "Passover I"),
            ("2022-04-17", "Passover - Chol HaMoed"),
            ("2022-04-18", "Passover - Chol HaMoed"),
            ("2022-04-19", "Passover - Chol HaMoed"),
            ("2022-04-20", "Passover - Chol HaMoed"),
            ("2022-04-21", "Passover VII - Eve"),
            ("2022-04-22", "Passover VII"),
            ("2022-05-04", "Memorial Day (Observed)"),
            ("2022-05-05", "Independence Day (Observed)"),
            ("2022-05-19", "Lag B'Omer"),
            ("2022-06-04", "Shavuot - Eve"),
            ("2022-06-05", "Shavuot"),
            ("2022-09-25", "Rosh Hashanah - Eve"),
            ("2022-09-26", "Rosh Hashanah"),
            ("2022-09-27", "Rosh Hashanah"),
            ("2022-10-04", "Yom Kippur - Eve"),
            ("2022-10-05", "Yom Kippur"),
            ("2022-10-09", "Sukkot I - Eve"),
            ("2022-10-10", "Sukkot I"),
            ("2022-10-11", "Sukkot - Chol HaMoed"),
            ("2022-10-12", "Sukkot - Chol HaMoed"),
            ("2022-10-13", "Sukkot - Chol HaMoed"),
            ("2022-10-14", "Sukkot - Chol HaMoed"),
            ("2022-10-15", "Sukkot - Chol HaMoed"),
            ("2022-10-16", "Sukkot VII - Eve"),
            ("2022-10-17", "Sukkot VII"),
            ("2022-12-19", "Hanukkah"),
            ("2022-12-20", "Hanukkah"),
            ("2022-12-21", "Hanukkah"),
            ("2022-12-22", "Hanukkah"),
            ("2022-12-23", "Hanukkah"),
            ("2022-12-24", "Hanukkah"),
            ("2022-12-25", "Hanukkah"),
            ("2022-12-26", "Hanukkah"),
        )
