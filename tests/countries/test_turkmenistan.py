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

from unittest import TestCase

from holidays.countries.turkmenistan import Turkmenistan, TM, TKM
from tests.common import CommonCountryTests, WorkingDayTests


class TestTurkmenistan(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Turkmenistan, years=range(1992, 2050))

    def test_country_aliases(self):
        self.assertAliases(Turkmenistan, TM, TKM)

    def test_no_holidays(self):
        self.assertNoHolidays(Turkmenistan(years=1991))

    def test_new_year(self):
        name = "Жаңа жыл"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1992, 2050)))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(1992, 2050)))

    def test_memorial_day(self):
        self.assertHolidayName(
            "Хатыра гүни (Memorial Day)", (f"{year}-01-12" for year in range(1992, 2050))
        )

    def test_defenders_day(self):
        name = "Ватанмухадызларың гүни"
        for year in range(2009, 2050):
            self.assertHolidayName(name, f"{year}-01-27")
        for year in range(1992, 2009):
            self.assertNoHolidayName(name, year)

    def test_womens_day(self):
        self.assertHolidayName(
            "Халықаралық әйелдер күні", (f"{year}-03-08" for year in range(1992, 2050))
        )

    def test_nowruz(self):
        name = "Наурыз мейрамы"
        for year in range(1992, 2050):
            self.assertHolidayName(name, f"{year}-03-21")
            self.assertHolidayName(name, f"{year}-03-22")

    def test_victory_day(self):
        self.assertHolidayName("Жеңиш гүни", (f"{year}-05-09" for year in range(1992, 2050)))

    def test_constitution_and_revival_day(self):
        for year in range(2018, 2050):
            self.assertHolidayName("Конституция ве Түзелиш гүни", f"{year}-05-18")
        for year in range(1992, 2018):
            self.assertHolidayName("Түзелиш гүни", f"{year}-05-18")

    def test_independence_day(self):
        for year in range(1992, 2018):
            self.assertHolidayName("Гарашсызлык гүни", f"{year}-10-27")
        for year in range(2018, 2050):
            self.assertHolidayName("Гарашсызлык гүни", f"{year}-09-27")

    def test_day_of_remembrance(self):
        for year in range(2015, 2050):
            self.assertHolidayName("Хатыра гүни (Day of Remembrance)", f"{year}-10-06")

    def test_neutrality_day(self):
        for year in range(2023, 2050):
            self.assertHolidayName("Битараплык гүни", f"{year}-12-12")
        for year in range(2018, 2023):
            self.assertHolidayName("Түркменистаның битараплык гүни", f"{year}-06-27")
        for year in range(1995, 2018):
            self.assertHolidayName("Битараплык гүни", f"{year}-12-12")

    def test_eid_al_fitr(self):
        self.assertHolidayName("Ораза байрамы (estimated)", "2024-04-10")
        self.assertHolidayName("Ораза байрамы (estimated)", "2025-04-01")

    def test_eid_al_adha(self):
        self.assertHolidayName("Гурбан байрамы (estimated)", "2024-06-16")
        self.assertHolidayName("Гурбан байрамы (estimated)", "2025-06-06")

    def test_localization(self):
        try:
            turkmen_holidays = Turkmenistan(years=range(1992, 2050), language="tk")
            for holiday in turkmen_holidays:
                self.assertEqual(
                    holiday.lang, "tk", f"Holiday {holiday.name} not localized in Turkmen."
                )
        except FileNotFoundError:
            print("Turkmen language translation files not found")

        try:
            russian_holidays = Turkmenistan(years=range(1992, 2050), language="ru")
            for holiday in russian_holidays:
                self.assertEqual(
                    holiday.lang, "ru", f"Holiday {holiday.name} not localized in Russian."
                )
        except FileNotFoundError:
            print("Russian language translation files not found")

        try:
            english_holidays = Turkmenistan(years=range(1992, 2050), language="en_US")
            for holiday in english_holidays:
                self.assertEqual(
                    holiday.lang, "en_US", f"Holiday {holiday.name} not localized in English."
                )
        except FileNotFoundError:
            print("English language translation files not found")
