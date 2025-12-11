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

from holidays.countries.oman import Oman
from tests.common import CommonCountryTests


class TestOman(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1970, 2050)
        super().setUpClass(Oman, years=years)
        cls.no_estimated_holidays = Oman(years=years, islamic_show_estimated=False)

    def test_accession_day(self):
        name = "اليوم الوطني لتولي السلطان"
        self.assertHolidayName(name, (f"{year}-01-11" for year in range(2020, 2050)))
        self.assertNoHolidayName(name, range(1970, 2020))

    def test_renaissance_day(self):
        name = "يوم النهضة"
        self.assertHolidayName(name, (f"{year}-07-23" for year in range(1970, 2020)))
        self.assertNoHolidayName(name, range(2020, 2050))

    def test_national_day(self):
        name = "يوم وطني"
        self.assertHolidayName(name, (f"{year}-11-18" for year in range(2020, 2025)))
        self.assertHolidayName(name, (f"{year}-11-19" for year in range(2020, 2025)))
        self.assertHolidayName(name, (f"{year}-11-20" for year in range(2025, 2050)))
        self.assertHolidayName(name, (f"{year}-11-21" for year in range(2025, 2050)))
        self.assertNoHolidayName(name, range(1970, 2020))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        dts = (
            "2018-09-11",
            "2019-09-01",
            "2020-08-21",
            "2021-08-10",
            "2022-07-30",
            "2023-07-20",
            "2024-07-07",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1970, 2050))

    def test_mawlid(self):
        name = "مولد النبي"
        dts = (
            "2018-11-20",
            "2019-11-09",
            "2020-10-29",
            "2021-10-19",
            "2022-10-09",
            "2023-09-28",
            "2024-09-15",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1970, 2050))

    def test_isra_and_miraj(self):
        name = "الإسراء والمعراج"
        dts = (
            "2018-04-13",
            "2019-04-03",
            "2020-03-22",
            "2021-03-11",
            "2022-03-01",
            "2023-02-19",
            "2024-02-08",
            "2025-01-27",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1970, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        dts = (
            "2019-06-03",
            "2019-06-04",
            "2019-06-05",
            "2019-06-06",
            "2020-05-22",
            "2020-05-23",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-11",
            "2021-05-12",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-04-30",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-20",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2023-04-24",
            "2024-04-09",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-29",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1970, 2050))

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        dts = (
            "2019-08-10",
            "2019-08-11",
            "2019-08-12",
            "2019-08-13",
            "2020-07-30",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-08",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-27",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1970, 2050))

    def test_weekend(self):
        for dt in (
            "2013-04-25",  # THU.
            "2013-04-26",  # FRI.
            "2013-05-03",  # FRI.
            "2013-05-04",  # SAT.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2013-04-27",  # SAT.
            "2013-04-28",  # SUN.
            "2013-05-02",  # THU.
            "2013-05-05",  # SUN.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_2019(self):
        self.assertHolidaysInYear(
            2019,
            ("2019-04-03", "الإسراء والمعراج"),
            ("2019-06-03", "عيد الفطر (المقدرة)"),
            ("2019-06-04", "عيد الفطر"),
            ("2019-06-05", "عيد الفطر"),
            ("2019-06-06", "عيد الفطر"),
            ("2019-07-23", "يوم النهضة"),
            ("2019-08-10", "عيد الأضحى"),
            ("2019-08-11", "عيد الأضحى"),
            ("2019-08-12", "عيد الأضحى"),
            ("2019-08-13", "عيد الأضحى"),
            ("2019-09-01", "رأس السنة الهجرية"),
            ("2019-11-09", "مولد النبي"),
        )

    def test_2021(self):
        self.assertHolidaysInYear(
            2021,
            ("2021-01-11", "اليوم الوطني لتولي السلطان"),
            ("2021-03-11", "الإسراء والمعراج"),
            ("2021-05-11", "عيد الفطر (المقدرة)"),
            ("2021-05-12", "عيد الفطر"),
            ("2021-05-13", "عيد الفطر"),
            ("2021-05-14", "عيد الفطر"),
            ("2021-05-15", "عيد الفطر"),
            ("2021-07-19", "عيد الأضحى"),
            ("2021-07-20", "عيد الأضحى"),
            ("2021-07-21", "عيد الأضحى"),
            ("2021-07-22", "عيد الأضحى"),
            ("2021-08-10", "رأس السنة الهجرية"),
            ("2021-10-19", "مولد النبي"),
            ("2021-11-18", "يوم وطني"),
            ("2021-11-19", "يوم وطني"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-11", "اليوم الوطني لتولي السلطان"),
            ("2023-02-19", "الإسراء والمعراج"),
            ("2023-04-20", "عيد الفطر"),
            ("2023-04-21", "عيد الفطر"),
            ("2023-04-22", "عيد الفطر"),
            ("2023-04-23", "عيد الفطر"),
            ("2023-04-24", "عيد الفطر"),
            ("2023-06-27", "عيد الأضحى"),
            ("2023-06-28", "عيد الأضحى"),
            ("2023-06-29", "عيد الأضحى"),
            ("2023-06-30", "عيد الأضحى"),
            ("2023-07-20", "رأس السنة الهجرية"),
            ("2023-09-28", "مولد النبي"),
            ("2023-11-18", "يوم وطني"),
            ("2023-11-19", "يوم وطني"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-11", "Sultan's Accession Day"),
            ("2023-02-19", "Isra' and Mi'raj"),
            ("2023-04-20", "Eid al-Fitr"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr"),
            ("2023-04-24", "Eid al-Fitr"),
            ("2023-06-27", "Eid al-Adha"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-20", "Islamic New Year"),
            ("2023-09-28", "Prophet's Birthday"),
            ("2023-11-18", "National Day"),
            ("2023-11-19", "National Day"),
        )
