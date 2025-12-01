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

from unittest import TestCase

from holidays.constants import BANK
from holidays.countries.qatar import Qatar
from tests.common import CommonCountryTests


class TestQatar(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1971, 2050)
        super().setUpClass(Qatar, years=years)
        cls.no_estimated_holidays = Qatar(years=years, islamic_show_estimated=False)
        cls.bank_holidays = Qatar(categories=BANK, years=years)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Qatar(categories=BANK, years=1970))

    def test_special_holidays(self):
        self.assertHoliday(
            "2025-01-02",
        )

    def test_sports_day(self):
        name = "اليوم الوطني للرياضة"
        dts = (
            "2012-02-14",
            "2013-02-12",
            "2014-02-11",
            "2015-02-10",
            "2016-02-09",
            "2017-02-14",
            "2018-02-13",
            "2019-02-12",
            "2020-02-11",
            "2021-02-09",
            "2022-02-08",
            "2023-02-14",
            "2024-02-13",
            "2025-02-11",
            "2026-02-10",
            "2027-02-09",
            "2028-02-08",
            "2029-02-13",
            "2030-02-12",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2012, 2050))
        self.assertNoHolidayName(name, range(1971, 2011))

    def test_national_day(self):
        name = "اليوم الوطني لقطر"
        self.assertHolidayName(name, (f"{year}-12-18" for year in range(2007, 2050)))
        self.assertNoHolidayName(name, range(1971, 2007))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        dts = (
            "2018-06-15",
            "2018-06-16",
            "2018-06-17",
            "2019-06-04",
            "2019-06-05",
            "2019-06-06",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1971, 2050))

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        dts = (
            "2018-08-22",
            "2018-08-23",
            "2018-08-24",
            "2019-08-11",
            "2019-08-12",
            "2019-08-13",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1971, 2050))

    def test_new_years_day(self):
        name = "رأس السنة الميلادية"
        self.assertHolidayName(
            name, self.bank_holidays, (f"{year}-01-01" for year in range(1971, 2050))
        )
        self.assertNoHolidayName(name)

    def test_march_bank_holiday(self):
        name = "عطلة البنك"
        dts = (
            "2010-03-07",
            "2011-03-06",
            "2012-03-04",
            "2013-03-03",
            "2014-03-02",
            "2015-03-01",
            "2016-03-06",
            "2017-03-05",
            "2018-03-04",
            "2019-03-03",
            "2020-03-01",
            "2021-03-07",
            "2022-03-06",
            "2023-03-05",
            "2024-03-03",
            "2025-03-02",
        )
        self.assertHolidayName(name, self.bank_holidays, dts)
        self.assertHolidayName(name, self.bank_holidays, range(2010, 2050))
        self.assertNoHolidayName(name, self.bank_holidays, range(1971, 2010))
        self.assertNoHolidayName(name)

    def test_weekend(self):
        for dt in (
            "2003-07-24",  # THU.
            "2003-07-25",  # FRI.
            "2003-07-31",  # THU.
            "2003-08-01",  # FRI.
            "2003-08-02",  # SAT.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2003-07-26",  # SAT.
            "2003-07-27",  # SUN.
            "2003-08-03",  # SUN.
            "2003-08-07",  # THU.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_2011(self):
        self.assertHolidaysInYear(
            2011,
            ("2011-08-31", "عيد الفطر"),
            ("2011-09-01", "عيد الفطر"),
            ("2011-09-02", "عيد الفطر"),
            ("2011-11-06", "عيد الأضحى"),
            ("2011-11-07", "عيد الأضحى"),
            ("2011-11-08", "عيد الأضحى"),
            ("2011-12-18", "اليوم الوطني لقطر"),
        )

    def test_bank_2024(self):
        self.assertBankHolidaysInYear(
            2024,
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-03-03", "عطلة البنك"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2012-01-01", "رأس السنة الميلادية"),
            ("2012-02-14", "اليوم الوطني للرياضة"),
            ("2012-03-04", "عطلة البنك"),
            ("2012-08-19", "عيد الفطر"),
            ("2012-08-20", "عيد الفطر"),
            ("2012-08-21", "عيد الفطر"),
            ("2012-10-26", "عيد الأضحى"),
            ("2012-10-27", "عيد الأضحى"),
            ("2012-10-28", "عيد الأضحى"),
            ("2012-12-18", "اليوم الوطني لقطر"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2012-01-01", "New Year's Day"),
            ("2012-02-14", "National Sports Day"),
            ("2012-03-04", "March Bank Holiday"),
            ("2012-08-19", "Eid al-Fitr"),
            ("2012-08-20", "Eid al-Fitr"),
            ("2012-08-21", "Eid al-Fitr"),
            ("2012-10-26", "Eid al-Adha"),
            ("2012-10-27", "Eid al-Adha"),
            ("2012-10-28", "Eid al-Adha"),
            ("2012-12-18", "Qatar National Day"),
        )
