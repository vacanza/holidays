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

from holidays.countries.french_polynesia import HolidaysPF, FrenchPolynesia, PF, PYF
from tests.common import CommonCountryTests


class TestFrenchPolynesia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysPF, years=range(1881, 2050))

    def test_country_aliases(self):
        self.assertAliases(HolidaysPF, FrenchPolynesia, PF, PYF)

    def test_no_holidays(self):
        self.assertNoHolidays(FrenchPolynesia(years=1880))

    def test_good_friday(self):
        name = "Vendredi saint"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1881, 2050))

    def test_missionary_day(self):
        name = "Arrivée de l'Évangile"
        self.assertHolidayName(name, (f"{year}-03-05" for year in range(1978, 2050)))
        self.assertNoHolidayName(name, range(1881, 1978))

    def test_internal_autonomy_day(self):
        name = "Fête de l'autonomie"
        self.assertHolidayName(name, (f"{year}-06-29" for year in range(1985, 2025)))
        self.assertNoHolidayName(name, range(1881, 1985), range(2025, 2050))

    def test_matarii(self):
        name = "Matāri'i"
        self.assertHolidayName(name, (f"{year}-11-20" for year in range(2025, 2050)))
        self.assertNoHolidayName(name, range(1881, 2025))

    def test_2024(self):
        self.assertHolidays(
            HolidaysPF(years=2024),
            ("2024-01-01", "Jour de l'an"),
            ("2024-03-05", "Arrivée de l'Évangile"),
            ("2024-03-29", "Vendredi saint"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-08", "Fête de la Victoire"),
            ("2024-05-09", "Ascension"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-06-29", "Fête de l'autonomie"),
            ("2024-07-14", "Fête nationale"),
            ("2024-08-15", "Assomption"),
            ("2024-11-01", "Toussaint"),
            ("2024-11-11", "Armistice"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jour de l'an"),
            ("2022-03-05", "Arrivée de l'Évangile"),
            ("2022-04-15", "Vendredi saint"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-08", "Fête de la Victoire"),
            ("2022-05-26", "Ascension"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-06-29", "Fête de l'autonomie"),
            ("2022-07-14", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-11-01", "Toussaint"),
            ("2022-11-11", "Armistice"),
            ("2022-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-03-05", "Missionary Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "Victory Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-29", "Internal Autonomy Day"),
            ("2022-07-14", "National Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-11", "Armistice Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-03-05", "วันคริสตธรรมมาถึง"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-08", "วันแห่งชัยชนะ"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-06-29", "วันปกครองตนเอง"),
            ("2022-07-14", "วันชาติฝรั่งเศส"),
            ("2022-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2022-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-11", "วันสงบศึก"),
            ("2022-12-25", "วันคริสต์มาส"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-03-05", "День місіонерів"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День Перемоги"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-29", "День автономії"),
            ("2022-07-14", "Національне свято"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День перемирʼя"),
            ("2022-12-25", "Різдво Христове"),
        )
