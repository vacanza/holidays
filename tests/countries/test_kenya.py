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

from holidays.constants import HINDU
from holidays.countries.kenya import Kenya
from tests.common import CommonCountryTests


class TestKenya(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Kenya)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Kenya(categories=HINDU, years=range(self.start_year, 1984)))

    def test_special_holidays(self):
        self.assertHoliday(
            "2015-11-26",
            "2017-08-08",
            "2017-10-25",
            "2017-10-26",
            "2017-11-28",
            "2020-02-11",
            "2022-04-29",
            "2022-08-09",
            "2022-09-10",
            "2022-09-11",
            "2022-09-12",
            "2022-09-13",
            "2023-11-13",
            "2024-05-10",
            "2024-11-01",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_madaraka_day(self):
        name = "Madaraka Day"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2011, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2011))
        obs_dts = (
            "2014-06-02",
            "2025-06-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_mazingira_day(self):
        name_1990 = "Moi Day"
        name_2021 = "Utamaduni Day"
        name_2025 = "Mazingira Day"

        self.assertHolidayName(
            name_1990, (f"{year}-10-10" for year in (*range(1990, 2010), *range(2018, 2021)))
        )
        self.assertHolidayName(name_2021, (f"{year}-10-10" for year in range(2021, 2025)))
        self.assertHolidayName(name_2025, (f"{year}-10-10" for year in range(2025, self.end_year)))
        self.assertNoHolidayName(
            name_1990, range(self.start_year, 1990), range(2010, 2018), range(2021, self.end_year)
        )
        self.assertNoHolidayName(
            name_2021, range(self.start_year, 2021), range(2025, self.end_year)
        )
        self.assertNoHolidayName(name_2025, range(self.start_year, 2025))
        dts_1990 = ("2004-10-11",)
        self.assertHolidayName(f"{name_1990} (observed)", dts_1990)
        dts_2021 = ("2021-10-11",)
        self.assertHolidayName(f"{name_2021} (observed)", dts_2021)
        dts_2025 = ("2027-10-11",)
        self.assertHolidayName(f"{name_2025} (observed)", dts_2025)
        self.assertNoNonObservedHoliday(dts_1990, dts_2021, dts_2025)

    def test_mashujaa_day(self):
        name_1964 = "Kenyatta Day"
        name_2011 = "Mashujaa Day"
        self.assertHolidayName(
            name_1964, (f"{year}-10-20" for year in range(self.start_year, 2011))
        )
        self.assertHolidayName(name_2011, (f"{year}-10-20" for year in range(2011, self.end_year)))
        self.assertNoHolidayName(name_1964, range(2011, self.end_year))
        self.assertNoHolidayName(name_2011, range(self.start_year, 2011))
        dts_1964 = ("2002-10-21",)
        self.assertHolidayName(f"{name_1964} (observed)", dts_1964)
        dts_2011 = (
            "2013-10-21",
            "2019-10-21",
            "2024-10-21",
        )
        self.assertHolidayName(f"{name_2011} (observed)", dts_2011)
        self.assertNoNonObservedHoliday(dts_1964, dts_2011)

    def test_jamhury_day(self):
        name_1964 = "Independence Day"
        name_2011 = "Jamhuri Day"
        self.assertHolidayName(
            name_1964, (f"{year}-12-12" for year in range(self.start_year, 2011))
        )
        self.assertHolidayName(name_2011, (f"{year}-12-12" for year in range(2011, self.end_year)))
        self.assertNoHolidayName(name_1964, range(2011, self.end_year))
        self.assertNoHolidayName(name_2011, range(self.start_year, 2011))
        dts_1964 = (
            "2004-12-13",
            "2010-12-13",
        )
        self.assertHolidayName(f"{name_1964} (observed)", dts_1964)
        dts_2011 = (
            "2021-12-13",
            "2027-12-13",
        )
        self.assertHolidayName(f"{name_2011} (observed)", dts_2011)
        self.assertNoNonObservedHoliday(dts_1964, dts_2011)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Idd-ul-Fitr"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2019-06-05",
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-21",
            "2024-04-10",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2001-12-17",
            "2004-11-15",
            "2009-09-21",
            "2012-08-20",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoIslamicNoEstimatedNonObservedHoliday(obs_dts)

    def test_diwali(self):
        name = "Diwali"
        self.assertNoHolidayName(name)
        self.assertHinduHolidayName(
            name,
            "2019-10-28",
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
        )
        self.assertHinduHolidayName(name, range(1984, self.end_year))
        self.assertNoHinduHolidayName(name, range(self.start_year, 1984))

    def test_eid_al_adha(self):
        name = "Idd-ul-Azha"
        self.assertNoHolidayName(name)
        self.assertIslamicIslamicNoEstimatedHolidayName(
            name,
            "2019-08-12",
            "2020-07-31",
            "2021-07-20",
            "2022-07-11",
            "2023-06-28",
            "2024-06-17",
        )
        self.assertIslamicIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_2010(self):
        self.assertHolidaysInYear(
            2010,
            ("2010-01-01", "New Year's Day"),
            ("2010-04-02", "Good Friday"),
            ("2010-04-05", "Easter Monday"),
            ("2010-05-01", "Labour Day"),
            ("2010-09-10", "Idd-ul-Fitr (estimated)"),
            ("2010-10-20", "Kenyatta Day"),
            ("2010-12-12", "Independence Day"),
            ("2010-12-13", "Independence Day (observed)"),
            ("2010-12-25", "Christmas Day"),
            ("2010-12-26", "Boxing Day"),
            ("2010-12-27", "Boxing Day (observed)"),
        )

    def test_2019(self):
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "New Year's Day"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-05-01", "Labour Day"),
            ("2019-06-01", "Madaraka Day"),
            ("2019-06-05", "Idd-ul-Fitr"),
            ("2019-10-10", "Moi Day"),
            ("2019-10-20", "Mashujaa Day"),
            ("2019-10-21", "Mashujaa Day (observed)"),
            ("2019-12-12", "Jamhuri Day"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-26", "Boxing Day"),
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-29", "State Funeral for Former President Mwai Kibaki"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-05-03", "Idd-ul-Fitr"),
            ("2022-06-01", "Madaraka Day"),
            ("2022-08-09", "Election Day"),
            ("2022-09-10", "Day of Mourning for Queen Elizabeth II"),
            ("2022-09-11", "Day of Mourning for Queen Elizabeth II"),
            ("2022-09-12", "Day of Mourning for Queen Elizabeth II"),
            ("2022-09-13", "Inauguration Day"),
            ("2022-10-10", "Utamaduni Day"),
            ("2022-10-20", "Mashujaa Day"),
            ("2022-12-12", "Jamhuri Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Idd-ul-Fitr"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-10", "National Tree Growing Day"),
            ("2024-06-01", "Madaraka Day"),
            ("2024-06-17", "Idd-ul-Azha"),
            ("2024-10-10", "Utamaduni Day"),
            ("2024-10-20", "Mashujaa Day"),
            ("2024-10-21", "Mashujaa Day (observed)"),
            ("2024-10-31", "Diwali"),
            ("2024-11-01", "Inauguration Day"),
            ("2024-12-12", "Jamhuri Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid-al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-10", "National Tree Growing Day"),
            ("2024-06-01", "Madaraka Day"),
            ("2024-06-17", "Eid-al-Adha"),
            ("2024-10-10", "Utamaduni Day"),
            ("2024-10-20", "Mashujaa Day"),
            ("2024-10-21", "Mashujaa Day (observed)"),
            ("2024-10-31", "Diwali"),
            ("2024-11-01", "Inauguration Day"),
            ("2024-12-12", "Jamhuri Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_sw(self):
        self.assertLocalizedHolidays(
            "sw",
            ("2024-01-01", "Siku ya Mwaka Mpya"),
            ("2024-03-29", "Ijumaa Kuu"),
            ("2024-04-01", "Jumatatu ya Pasaka"),
            ("2024-04-10", "Sikukuu ya Idd-ul-Fitr"),
            ("2024-05-01", "Siku ya Kazi"),
            ("2024-05-10", "Siku ya Kitaifa ya Kupanda Miti"),
            ("2024-06-01", "Siku ya Madaraka"),
            ("2024-06-17", "Sikukuu ya Idd-ul-Azha"),
            ("2024-10-10", "Siku ya Utamaduni"),
            ("2024-10-20", "Siku ya Mashujaa"),
            ("2024-10-21", "Siku ya Mashujaa (imezingatiwa)"),
            ("2024-10-31", "Diwali"),
            ("2024-11-01", "Siku ya Uzinduzi"),
            ("2024-12-12", "Siku ya Jamhuri"),
            ("2024-12-25", "Siku ya Krismasi"),
            ("2024-12-26", "Siku ya Ndondi"),
        )
