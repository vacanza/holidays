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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import _timedelta
from holidays.countries.turkey import Turkey
from tests.common import CommonCountryTests


class TestTurkey(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Turkey)

    def test_special_holidays(self):
        self.assertHoliday("1999-12-31")

    def test_new_years_day(self):
        self.assertHolidayName("Yılbaşı", (f"{year}-01-01" for year in self.full_range))

    def test_national_sovereignty_and_childrens_day(self):
        name_1936 = "Ulusal Egemenlik Bayramı"
        name_1981 = "Ulusal Egemenlik ve Çocuk Bayramı"
        self.assertHolidayName(
            name_1936, (f"{year}-04-23" for year in range(self.start_year, 1981))
        )
        self.assertHolidayName(name_1981, (f"{year}-04-23" for year in range(1981, self.end_year)))
        self.assertNoHolidayName(name_1936, range(1981, self.end_year))
        self.assertNoHolidayName(name_1981, range(self.start_year, 1981))

    def test_spring_and_labor_day(self):
        name_1936 = "Bahar Bayramı"
        name_2009 = "Emek ve Dayanışma Günü"
        self.assertHolidayName(
            name_1936, (f"{year}-05-01" for year in range(self.start_year, 1981))
        )
        self.assertHolidayName(name_2009, (f"{year}-05-01" for year in range(2009, self.end_year)))
        self.assertNoHolidayName(name_1936, range(1981, self.end_year))
        self.assertNoHolidayName(name_2009, range(self.start_year, 2009))

    def test_ataturk_youth_and_sports_day(self):
        name_1936 = "Gençlik ve Spor Bayramı"
        name_1981 = "Atatürk'ü Anma, Gençlik ve Spor Bayramı"
        self.assertHolidayName(
            name_1936, (f"{year}-05-19" for year in range(self.start_year, 1981))
        )
        self.assertHolidayName(name_1981, (f"{year}-05-19" for year in range(1981, self.end_year)))
        self.assertNoHolidayName(name_1936, range(1981, self.end_year))
        self.assertNoHolidayName(name_1981, range(self.start_year, 1981))

    def test_freedom_and_constitution_day(self):
        name = "Hürriyet ve Anayasa Bayramı"
        self.assertHolidayName(name, (f"{year}-05-27" for year in range(1963, 1981)))
        self.assertNoHolidayName(name, range(self.start_year, 1963), range(1981, self.end_year))

    def test_democracy_and_national_unity_day(self):
        name = "Demokrasi ve Millî Birlik Günü"
        self.assertHolidayName(name, (f"{year}-07-15" for year in range(2017, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2017))

    def test_victory_day(self):
        self.assertHolidayName("Zafer Bayramı", (f"{year}-08-30" for year in self.full_range))

    def test_republic_day(self):
        name = "Cumhuriyet Bayramı"
        self.assertHolidayName(
            name,
            (f"{year}-10-29" for year in self.full_range),
            (f"{year}-10-30" for year in range(self.start_year, 1981)),
        )
        self.assertHalfDayHolidayName(
            f"{name} (saat 13.00'ten)",
            (f"{year}-10-28" for year in self.full_range),
        )

    def test_eid_al_fitr(self):
        name = "Ramazan Bayramı"
        for ymd in (
            (2000, 1, 8),
            (2000, 12, 27),
            (2010, 9, 9),
            (2018, 6, 15),
            (2019, 6, 4),
            (2020, 5, 24),
            (2021, 5, 13),
            (2022, 5, 2),
            (2023, 4, 21),
        ):
            dt = date(*ymd)
            self.assertHolidayName(name, dt, _timedelta(dt, +1), _timedelta(dt, +2))
            self.assertHalfDayHolidayName(f"{name} (saat 13.00'ten)", _timedelta(dt, -1))
        exception_years = {1968, 2000, 2033}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, (year for year in self.full_range if year not in exception_years)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, exception_years)

    def test_eid_al_adha(self):
        name = "Kurban Bayramı"
        for ymd in (
            (2006, 1, 10),
            (2006, 12, 31),
            (2010, 11, 16),
            (2018, 8, 21),
            (2019, 8, 11),
            (2020, 7, 31),
            (2021, 7, 20),
            (2022, 7, 9),
            (2023, 6, 28),
        ):
            dt = date(*ymd)
            self.assertHolidayName(
                name, dt, _timedelta(dt, +1), _timedelta(dt, +2), _timedelta(dt, +3)
            )
            self.assertHalfDayHolidayName(f"{name} (saat 13.00'ten)", _timedelta(dt, -1))
        self.assertIslamicNoEstimatedHolidayNameCount(
            name,
            4,
            (year for year in self.full_range if year not in {1941, 1942, 1974, 2006, 2007, 2039}),
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 5, 1942, 2006)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 7, 1941, 2007)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 8, 1974, 2039)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Yılbaşı"),
            ("2022-04-23", "Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2022-05-01", "Emek ve Dayanışma Günü"),
            ("2022-05-02", "Ramazan Bayramı"),
            ("2022-05-03", "Ramazan Bayramı"),
            ("2022-05-04", "Ramazan Bayramı"),
            ("2022-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2022-07-09", "Kurban Bayramı"),
            ("2022-07-10", "Kurban Bayramı"),
            ("2022-07-11", "Kurban Bayramı"),
            ("2022-07-12", "Kurban Bayramı"),
            ("2022-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2022-08-30", "Zafer Bayramı"),
            ("2022-10-29", "Cumhuriyet Bayramı"),
        )

    def test_2022_half_day(self):
        self.assertHalfDayHolidaysInYear(
            2022,
            ("2022-05-01", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2022-07-08", "Kurban Bayramı (saat 13.00'ten)"),
            ("2022-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Yılbaşı"),
            ("2023-04-20", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2023-04-21", "Ramazan Bayramı"),
            ("2023-04-22", "Ramazan Bayramı"),
            ("2023-04-23", "Ramazan Bayramı; Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2023-05-01", "Emek ve Dayanışma Günü"),
            ("2023-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2023-06-27", "Kurban Bayramı (saat 13.00'ten)"),
            ("2023-06-28", "Kurban Bayramı"),
            ("2023-06-29", "Kurban Bayramı"),
            ("2023-06-30", "Kurban Bayramı"),
            ("2023-07-01", "Kurban Bayramı"),
            ("2023-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2023-08-30", "Zafer Bayramı"),
            ("2023-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
            ("2023-10-29", "Cumhuriyet Bayramı"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-20", "Eid al-Fitr (from 1pm)"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr; National Sovereignty and Children's Day"),
            ("2023-05-01", "Labour and Solidarity Day"),
            ("2023-05-19", "Commemoration of Atatürk, Youth and Sports Day"),
            ("2023-06-27", "Eid al-Adha (from 1pm)"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-01", "Eid al-Adha"),
            ("2023-07-15", "Democracy and National Unity Day"),
            ("2023-08-30", "Victory Day"),
            ("2023-10-28", "Republic Day (from 1pm)"),
            ("2023-10-29", "Republic Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-04-20", "Рамазан-байрам (з 13:00)"),
            ("2023-04-21", "Рамазан-байрам"),
            ("2023-04-22", "Рамазан-байрам"),
            ("2023-04-23", "День національної незалежності та дітей; Рамазан-байрам"),
            ("2023-05-01", "День праці та солідарності"),
            ("2023-05-19", "День вшанування памʼяті Ататюрка, молоді та спорту"),
            ("2023-06-27", "Курбан-байрам (з 13:00)"),
            ("2023-06-28", "Курбан-байрам"),
            ("2023-06-29", "Курбан-байрам"),
            ("2023-06-30", "Курбан-байрам"),
            ("2023-07-01", "Курбан-байрам"),
            ("2023-07-15", "День демократії та національної єдності"),
            ("2023-08-30", "День Перемоги"),
            ("2023-10-28", "День Республіки (з 13:00)"),
            ("2023-10-29", "День Республіки"),
        )
