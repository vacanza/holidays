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


from holidays.constants import PUBLIC, SCHOOL
from holidays.countries.bulgaria import Bulgaria, BG, BLG
from tests.common import TestCase


class TestBulgaria(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bulgaria, years=range(1990, 2050), years_non_observed=range(2017, 2030))

    def test_country_aliases(self):
        self.assertCountryAliases(Bulgaria, BG, BLG)

    def test_no_holidays(self):
        self.assertNoHolidays(Bulgaria(categories=(PUBLIC, SCHOOL), years=1989))

    def test_new_years_day(self):
        name = "Нова година"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1990, 2050)))
        dt = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
            "2028-01-03",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_liberation_day(self):
        name = "Ден на Освобождението на България от османско иго"
        self.assertHolidayName(name, (f"{year}-03-03" for year in range(1990, 2050)))
        dt = (
            "2018-03-05",
            "2019-03-04",
            "2024-03-04",
            "2029-03-05",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        self.assertHolidayName(
            "Велики петък",
            "2019-04-26",
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
        )

    def test_easter_saturday(self):
        self.assertHolidayName(
            "Велика събота",
            "2019-04-27",
            "2020-04-18",
            "2021-05-01",
            "2022-04-23",
            "2023-04-15",
        )

    def test_easter(self):
        self.assertHolidayName(
            "Великден",
            "2019-04-28",
            "2019-04-29",
            "2020-04-19",
            "2020-04-20",
            "2021-05-02",
            "2021-05-03",
            "2022-04-24",
            "2022-04-25",
            "2023-04-16",
            "2023-04-17",
        )

    def test_labour_day(self):
        name = "Ден на труда и на международната работническа солидарност"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1990, 2050)))
        dt = (
            "2021-05-04",
            "2022-05-02",
            "2027-05-04",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_saint_georges_day(self):
        name = "Гергьовден, Ден на храбростта и Българската армия"
        self.assertHolidayName(name, (f"{year}-05-06" for year in range(1990, 2050)))
        dt = (
            "2017-05-08",
            "2018-05-07",
            "2023-05-08",
            "2028-05-08",
            "2029-05-07",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_twenty_fourth_of_may(self):
        name = (
            "Ден на светите братя Кирил и Методий, на българската азбука, "
            "просвета и култура и на славянската книжовност"
        )
        self.assertHolidayName(name, (f"{year}-05-24" for year in range(1990, 2050)))
        dt = (
            "2020-05-25",
            "2025-05-26",
            "2026-05-25",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_unification_day(self):
        name = "Ден на Съединението"
        self.assertHolidayName(name, (f"{year}-09-06" for year in range(1990, 2050)))
        dt = (
            "2020-09-07",
            "2025-09-08",
            "2026-09-07",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Ден на Независимостта на България"
        self.assertHolidayName(name, (f"{year}-09-22" for year in range(1990, 2050)))
        dt = (
            "2018-09-24",
            "2019-09-23",
            "2024-09-23",
            "2029-09-24",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_awakening_day(self):
        name = "Ден на народните будители"
        self.assertHolidayName(
            name,
            Bulgaria(categories=(SCHOOL,), years=range(1990, 2050)),
            (f"{year}-11-01" for year in range(1990, 2050)),
        )
        self.assertNoHolidayName(name)

    def test_christmas_eve(self):
        name = "Бъдни вечер"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(1990, 2050)))
        dt = (
            "2017-12-27",
            "2022-12-27",
            "2023-12-27",
            "2028-12-27",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Рождество Христово"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1990, 2050)))
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1990, 2050)))
        dt = (
            "2020-12-28",
            "2021-12-27",
            "2021-12-28",
            "2022-12-28",
            "2026-12-28",
            "2027-12-27",
            "2027-12-28",
        )
        self.assertHolidayName(f"{name} (почивен ден)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Нова година"),
            ("2022-01-03", "Нова година (почивен ден)"),
            ("2022-03-03", "Ден на Освобождението на България от османско иго"),
            ("2022-04-22", "Велики петък"),
            ("2022-04-23", "Велика събота"),
            ("2022-04-24", "Великден"),
            ("2022-04-25", "Великден"),
            ("2022-05-01", "Ден на труда и на международната работническа солидарност"),
            (
                "2022-05-02",
                "Ден на труда и на международната работническа солидарност (почивен ден)",
            ),
            ("2022-05-06", "Гергьовден, Ден на храбростта и Българската армия"),
            (
                "2022-05-24",
                "Ден на светите братя Кирил и Методий, на българската азбука, "
                "просвета и култура и на славянската книжовност",
            ),
            ("2022-09-06", "Ден на Съединението"),
            ("2022-09-22", "Ден на Независимостта на България"),
            ("2022-11-01", "Ден на народните будители"),
            ("2022-12-24", "Бъдни вечер"),
            ("2022-12-25", "Рождество Христово"),
            ("2022-12-26", "Рождество Христово"),
            ("2022-12-27", "Бъдни вечер (почивен ден)"),
            ("2022-12-28", "Рождество Христово (почивен ден)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (Observed)"),
            ("2022-03-03", "Liberation Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-23", "Holy Saturday"),
            ("2022-04-24", "Easter"),
            ("2022-04-25", "Easter"),
            ("2022-05-01", "Labor Day and International Workers' Solidarity Day"),
            ("2022-05-02", "Labor Day and International Workers' Solidarity Day (Observed)"),
            ("2022-05-06", "St. George's Day (Day of the Bulgarian Army)"),
            ("2022-05-24", "Day of Slavonic Alphabet, Bulgarian Enlightenment and Culture"),
            ("2022-09-06", "Unification Day"),
            ("2022-09-22", "Independence Day"),
            ("2022-11-01", "The Day of the People's Awakeners"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day"),
            ("2022-12-27", "Christmas Eve (Observed)"),
            ("2022-12-28", "Christmas Day (Observed)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-03", "Новий рік (вихідний)"),
            ("2022-03-03", "День визволення Болгарії від османського іга"),
            ("2022-04-22", "Страсна пʼятниця"),
            ("2022-04-23", "Велика субота"),
            ("2022-04-24", "Великдень"),
            ("2022-04-25", "Великдень"),
            ("2022-05-01", "День праці та міжнародної солідарності трудящих"),
            ("2022-05-02", "День праці та міжнародної солідарності трудящих (вихідний)"),
            ("2022-05-06", "День Святого Георгія та День хоробрості і болгарської армії"),
            (
                "2022-05-24",
                "День святих братів Кирила і Мефодія, болгарської писемності, "
                "освіти і культури та словʼянської літератури",
            ),
            ("2022-09-06", "День обʼєднання"),
            ("2022-09-22", "День незалежності Болгарїі"),
            ("2022-11-01", "День національних будителів"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Різдво Христове"),
            ("2022-12-27", "Святий вечір (вихідний)"),
            ("2022-12-28", "Різдво Христове (вихідний)"),
        )
