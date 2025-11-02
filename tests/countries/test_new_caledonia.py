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

from holidays.countries.new_caledonia import NewCaledonia
from tests.common import CommonCountryTests


class TestNewCaledonia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NewCaledonia, years=range(1854, 2050))

    def test_citizenship_day(self):
        name_1953 = "Fête de la prise de possession"
        name_2004 = "Fête de la Citoyenneté"

        self.assertHolidayName(name_1953, (f"{year}-09-24" for year in range(1953, 2004)))
        self.assertHolidayName(name_2004, (f"{year}-09-24" for year in range(2004, 2050)))
        self.assertNoHolidayName(name_1953, range(1854, 1953), range(2004, 2050))
        self.assertNoHolidayName(name_2004, range(1854, 2004))

    def test_2024(self):
        self.assertHolidays(
            NewCaledonia(years=2024),
            ("2024-01-01", "Jour de l'an"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-08", "Fête de la Victoire"),
            ("2024-05-09", "Ascension"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-07-14", "Fête nationale"),
            ("2024-08-15", "Assomption"),
            ("2024-09-24", "Fête de la Citoyenneté"),
            ("2024-11-01", "Toussaint"),
            ("2024-11-11", "Armistice"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jour de l'an"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-08", "Fête de la Victoire"),
            ("2022-05-26", "Ascension"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-14", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-09-24", "Fête de la Citoyenneté"),
            ("2022-11-01", "Toussaint"),
            ("2022-11-11", "Armistice"),
            ("2022-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "Victory Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-07-14", "National Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-24", "Citizenship Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-11", "Armistice Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-08", "วันแห่งชัยชนะ"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-07-14", "วันชาติฝรั่งเศส"),
            ("2022-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2022-09-24", "วันแห่งความเป็นพลเมือง"),
            ("2022-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-11", "วันสงบศึก"),
            ("2022-12-25", "วันคริสต์มาส"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День Перемоги"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-07-14", "Національне свято"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-09-24", "День громадянства"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День перемирʼя"),
            ("2022-12-25", "Різдво Христове"),
        )
