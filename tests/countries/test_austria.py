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

from holidays.countries.austria import Austria
from tests.common import CommonCountryTests


class TestAustria(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Austria, with_subdiv_categories=True)

    def test_new_years_day(self):
        self.assertHolidayName("Neujahr", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany(self):
        name = "Heilige Drei Könige"
        self.assertHolidayName(
            name,
            (
                f"{year}-01-06"
                for year in (*range(self.start_year, 1946), *range(1950, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(1946, 1950))

    def test_good_friday(self):
        name = "Karfreitag"
        # PUBLIC.
        self.assertNoHolidayName(name)
        # BANK.
        self.assertBankHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertBankHolidayName(name, self.full_range)
        # PROTESTANT.
        self.assertProtestantHolidayName(
            name,
            "2013-03-29",
            "2014-04-18",
            "2015-04-03",
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
        )
        self.assertProtestantHolidayName(name, range(1956, 2019))
        self.assertNoProtestantHolidayName(
            name, range(self.start_year, 1956), range(2019, self.end_year)
        )

    def test_easter_monday(self):
        name = "Ostermontag"
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
        name = "Staatsfeiertag"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1946, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1946))

    def test_ascension_day(self):
        name = "Christi Himmelfahrt"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Pfingstmontag"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_corpus_christi(self):
        name = "Fronleichnam"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_saint_peter_and_pauls_day(self):
        name = "Peter und Paul"
        self.assertHolidayName(name, (f"{year}-06-29" for year in range(self.start_year, 1946)))
        self.assertNoHolidayName(name, range(1946, self.end_year))

    def test_assumption_day(self):
        self.assertHolidayName("Mariä Himmelfahrt", (f"{year}-08-15" for year in self.full_range))

    def test_national_day(self):
        name = "Nationalfeiertag"
        self.assertHolidayName(name, (f"{year}-10-26" for year in range(1967, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1967))

    def test_all_saints_day(self):
        self.assertHolidayName("Allerheiligen", (f"{year}-11-01" for year in self.full_range))

    def test_immaculate_conception(self):
        name = "Mariä Empfängnis"
        self.assertHolidayName(
            name,
            (
                f"{year}-12-08"
                for year in (*range(self.start_year, 1945), *range(1955, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(1945, 1955))

    def test_christmas_eve(self):
        name = "Heiliger Abend"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Christtag", (f"{year}-12-25" for year in self.full_range))

    def test_saint_stephens_day(self):
        self.assertHolidayName("Stephanstag", (f"{year}-12-26" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Silvester"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_saint_martins_day(self):
        name = "Hl. Martin"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_bank_holidays.items():
            if subdiv == "1":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-11" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_josephs_day(self):
        name = "Hl. Josef"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_bank_holidays.items():
            if subdiv in {"2", "6", "7", "8"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-19" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_1920_carinthian_plebiscite_anniversary(self):
        name = "Tag der Volksabstimmung"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_bank_holidays.items():
            if subdiv == "2":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-10" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_leopolds_day(self):
        name = "Hl. Leopold"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_bank_holidays.items():
            if subdiv in {"3", "9"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_florians_day(self):
        name = "Hl. Florian"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_bank_holidays.items():
            if subdiv == "4":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-04" for year in range(2004, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2004))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_ruperts_day(self):
        name = "Hl. Rupert"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_bank_holidays.items():
            if subdiv == "5":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-24" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_2021(self):
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "Neujahr"),
            ("2021-01-06", "Heilige Drei Könige"),
            ("2021-04-05", "Ostermontag"),
            ("2021-05-01", "Staatsfeiertag"),
            ("2021-05-13", "Christi Himmelfahrt"),
            ("2021-05-24", "Pfingstmontag"),
            ("2021-06-03", "Fronleichnam"),
            ("2021-08-15", "Mariä Himmelfahrt"),
            ("2021-10-26", "Nationalfeiertag"),
            ("2021-11-01", "Allerheiligen"),
            ("2021-12-08", "Mariä Empfängnis"),
            ("2021-12-25", "Christtag"),
            ("2021-12-26", "Stephanstag"),
        )

    def test_bank_2021(self):
        self.assertBankHolidaysInYear(
            2021,
            ("2021-04-02", "Karfreitag"),
            ("2021-12-24", "Heiliger Abend"),
            ("2021-12-31", "Silvester"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-03-19", "Hl. Josef"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Staatsfeiertag"),
            ("2022-05-04", "Hl. Florian"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-16", "Fronleichnam"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-09-24", "Hl. Rupert"),
            ("2022-10-10", "Tag der Volksabstimmung"),
            ("2022-10-26", "Nationalfeiertag"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Hl. Martin"),
            ("2022-11-15", "Hl. Leopold"),
            ("2022-12-08", "Mariä Empfängnis"),
            ("2022-12-24", "Heiliger Abend"),
            ("2022-12-25", "Christtag"),
            ("2022-12-26", "Stephanstag"),
            ("2022-12-31", "Silvester"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-03-19", "Saint Joseph's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-04", "Saint Florian's Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-24", "Saint Rupert's Day"),
            ("2022-10-10", "1920 Carinthian plebiscite"),
            ("2022-10-26", "National Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-11", "Saint Martin's Day"),
            ("2022-11-15", "Saint Leopold's Day"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-03-19", "วันสมโภชนักบุญโยเซฟ"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-04", "วันสมโภชนักบุญฟลอเรียน"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-06-16", "วันสมโภชพระคริสตวรกาย"),
            ("2022-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2022-09-24", "วันสมโภชนักบุญรูเพิร์ตแห่งซาลซ์บูร์ก"),
            ("2022-10-10", "วันครบรอบการลงประชามติคารินเทีย"),
            ("2022-10-26", "วันชาติออสเตรีย"),
            ("2022-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-11", "วันสมโภชนักบุญมาร์ติน"),
            ("2022-11-15", "วันสมโภชนักบุญลีโอโพลด์"),
            ("2022-12-08", "วันสมโภชแม่พระผู้ปฏิสนธินิรมล"),
            ("2022-12-24", "วันคริสต์มาสอีฟ"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "วันสมโภชนักบุญสเตเฟน"),
            ("2022-12-31", "วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-03-19", "День Святого Йосипа"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-04", "День Святого Флоріана"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-09-24", "День Святого Руперта"),
            ("2022-10-10", "Річниця референдуму 1920 року в Карінтії"),
            ("2022-10-26", "Національне свято"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День Святого Мартина"),
            ("2022-11-15", "День Святого Леопольда"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День Святого Стефана"),
            ("2022-12-31", "Переддень Нового року"),
        )
