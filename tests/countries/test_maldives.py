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

from holidays.countries.maldives import Maldives
from tests.common import CommonCountryTests


class TestMaldives(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Maldives, years=range(1950, 2050))

    def test_new_years_day(self):
        self.assertHolidayName("މީލާދީ އާ އަހަރު ފެށޭ ދުވަސް", (f"{year}-01-01" for year in range(1950, 2050)))

    def test_labor_day(self):
        self.assertHolidayName(
            "ބައިނަލްއަޤްވާމީ މަސައްކަތްތެރިންގެ ދުވަސް", (f"{year}-05-01" for year in range(1950, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName("މިނިވަން ދުވަސް", (f"{year}-07-26" for year in range(1950, 2050)))

    def test_victory_day(self):
        self.assertHolidayName("ނަޞްރުގެ ދުވަސް", (f"{year}-11-03" for year in range(1950, 2050)))

    def test_republic_day(self):
        self.assertHolidayName("ޖުމްހޫރީ ދުވަސް", (f"{year}-11-11" for year in range(1950, 2050)))

    def test_2018(self):
        self.assertHolidaysInYear(
            2018,
            ("2018-01-01", "މީލާދީ އާ އަހަރު ފެށޭ ދުވަސް"),
            ("2018-05-01", "ބައިނަލްއަޤްވާމީ މަސައްކަތްތެރިންގެ ދުވަސް"),
            ("2018-05-16", "ރަމަޟާން މަސް ފެށޭ ދުވަސް (estimated)"),
            ("2018-06-15", "ފިޠުރުޢީދު ދުވަސް (estimated)"),
            ("2018-06-16", "ފިޠުރުޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2018-06-17", "ފިޠުރުޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2018-07-26", "މިނިވަން ދުވަސް"),
            ("2018-08-20", "ޙައްޖުދުވަސް (estimated)"),
            ("2018-08-21", "އަޟްޙާޢީދު ދުވަސް (estimated)"),
            ("2018-08-22", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2018-08-23", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2018-08-24", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2018-09-11", "ހިޖުރީ އާ އަހަރު ފެށޭ ދުވަސް (estimated)"),
            ("2018-11-03", "ނަޞްރުގެ ދުވަސް"),
            ("2018-11-09", "ޤައުމީ ދުވަސް (estimated)"),
            ("2018-11-11", "ޖުމްހޫރީ ދުވަސް"),
            ("2018-11-20", "ކީރިތި ރަސޫލާގެ ޢީދުމީލާދު (estimated)"),
            ("2018-12-08", "ރާއްޖެ އިސްލާމްވީ ދުވަސް (estimated)"),
        )

    def test_2020(self):
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "މީލާދީ އާ އަހަރު ފެށޭ ދުވަސް"),
            ("2020-04-24", "ރަމަޟާން މަސް ފެށޭ ދުވަސް (estimated)"),
            ("2020-05-01", "ބައިނަލްއަޤްވާމީ މަސައްކަތްތެރިންގެ ދުވަސް"),
            ("2020-05-24", "ފިޠުރުޢީދު ދުވަސް (estimated)"),
            ("2020-05-25", "ފިޠުރުޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2020-05-26", "ފިޠުރުޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2020-07-26", "މިނިވަން ދުވަސް"),
            ("2020-07-30", "ޙައްޖުދުވަސް (estimated)"),
            ("2020-07-31", "އަޟްޙާޢީދު ދުވަސް (estimated)"),
            ("2020-08-01", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2020-08-02", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2020-08-03", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2020-08-20", "ހިޖުރީ އާ އަހަރު ފެށޭ ދުވަސް (estimated)"),
            ("2020-10-18", "ޤައުމީ ދުވަސް (estimated)"),
            ("2020-10-29", "ކީރިތި ރަސޫލާގެ ޢީދުމީލާދު (estimated)"),
            ("2020-11-03", "ނަޞްރުގެ ދުވަސް"),
            ("2020-11-11", "ޖުމްހޫރީ ދުވަސް"),
            ("2020-11-16", "ރާއްޖެ އިސްލާމްވީ ދުވަސް (estimated)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "މީލާދީ އާ އަހަރު ފެށޭ ދުވަސް"),
            ("2024-03-11", "ރަމަޟާން މަސް ފެށޭ ދުވަސް (estimated)"),
            ("2024-04-10", "ފިޠުރުޢީދު ދުވަސް (estimated)"),
            ("2024-04-11", "ފިޠުރުޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2024-04-12", "ފިޠުރުޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2024-05-01", "ބައިނަލްއަޤްވާމީ މަސައްކަތްތެރިންގެ ދުވަސް"),
            ("2024-06-15", "ޙައްޖުދުވަސް (estimated)"),
            ("2024-06-16", "އަޟްޙާޢީދު ދުވަސް (estimated)"),
            ("2024-06-17", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2024-06-18", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2024-06-19", "އަޟްޙާޢީދުގެ މުނާސަބަތުގައި (estimated)"),
            ("2024-07-07", "ހިޖުރީ އާ އަހަރު ފެށޭ ދުވަސް (estimated)"),
            ("2024-07-26", "މިނިވަން ދުވަސް"),
            ("2024-09-04", "ޤައުމީ ދުވަސް (estimated)"),
            ("2024-09-15", "ކީރިތި ރަސޫލާގެ ޢީދުމީލާދު (estimated)"),
            ("2024-10-04", "ރާއްޖެ އިސްލާމްވީ ދުވަސް (estimated)"),
            ("2024-11-03", "ނަޞްރުގެ ދުވަސް"),
            ("2024-11-11", "ޖުމްހޫރީ ދުވަސް"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-11", "Beginning of Ramadan (estimated)"),
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-04-11", "Eid al-Fitr (estimated)"),
            ("2024-04-12", "Eid al-Fitr (estimated)"),
            ("2024-05-01", "Labor Day"),
            ("2024-06-15", "Hajj Day (estimated)"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-06-17", "Eid al-Adha (estimated)"),
            ("2024-06-18", "Eid al-Adha (estimated)"),
            ("2024-06-19", "Eid al-Adha (estimated)"),
            ("2024-07-07", "Islamic New Year (estimated)"),
            ("2024-07-26", "Independence Day"),
            ("2024-09-04", "National Day (estimated)"),
            ("2024-09-15", "Mawlid al-Nabi (estimated)"),
            ("2024-10-04", "The Day Maldives Embraced Islam (estimated)"),
            ("2024-11-03", "Victory Day"),
            ("2024-11-11", "Republic Day"),
        )
