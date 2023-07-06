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

from holidays.countries.belgium import Belgium, BE, BEL
from tests.common import TestCase


class TestBelgium(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Belgium)

    def test_country_aliases(self):
        self.assertCountryAliases(Belgium, BE, BEL)

    def test_2019(self):
        self.assertHolidays(
            ("2019-01-01", "Nieuwjaar"),
            ("2019-04-21", "Pasen"),
            ("2019-04-22", "Paasmaandag"),
            ("2019-05-01", "Dag van de Arbeid"),
            ("2019-05-30", "Hemelvaart"),
            ("2019-06-09", "Pinksteren"),
            ("2019-06-10", "Pinkstermaandag"),
            ("2019-07-21", "Nationale feestdag"),
            ("2019-08-15", "Onze Lieve Vrouw hemelvaart"),
            ("2019-11-01", "Allerheiligen"),
            ("2019-11-11", "Wapenstilstand"),
            ("2019-12-25", "Kerstmis"),
        )

    def test_2020(self):
        self.assertHolidays(
            ("2020-01-01", "Nieuwjaar"),
            ("2020-04-12", "Pasen"),
            ("2020-04-13", "Paasmaandag"),
            ("2020-05-01", "Dag van de Arbeid"),
            ("2020-05-21", "Hemelvaart"),
            ("2020-05-31", "Pinksteren"),
            ("2020-06-01", "Pinkstermaandag"),
            ("2020-07-21", "Nationale feestdag"),
            ("2020-08-15", "Onze Lieve Vrouw hemelvaart"),
            ("2020-11-01", "Allerheiligen"),
            ("2020-11-11", "Wapenstilstand"),
            ("2020-12-25", "Kerstmis"),
        )

    def test_2021(self):
        self.assertHolidays(
            ("2021-01-01", "Nieuwjaar"),
            ("2021-04-04", "Pasen"),
            ("2021-04-05", "Paasmaandag"),
            ("2021-05-01", "Dag van de Arbeid"),
            ("2021-05-13", "Hemelvaart"),
            ("2021-05-23", "Pinksteren"),
            ("2021-05-24", "Pinkstermaandag"),
            ("2021-07-21", "Nationale feestdag"),
            ("2021-08-15", "Onze Lieve Vrouw hemelvaart"),
            ("2021-11-01", "Allerheiligen"),
            ("2021-11-11", "Wapenstilstand"),
            ("2021-12-25", "Kerstmis"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nieuwjaar"),
            ("2022-04-17", "Pasen"),
            ("2022-04-18", "Paasmaandag"),
            ("2022-05-01", "Dag van de Arbeid"),
            ("2022-05-26", "Hemelvaart"),
            ("2022-06-05", "Pinksteren"),
            ("2022-06-06", "Pinkstermaandag"),
            ("2022-07-21", "Nationale feestdag"),
            ("2022-08-15", "Onze Lieve Vrouw hemelvaart"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Wapenstilstand"),
            ("2022-12-25", "Kerstmis"),
        )

    def test_l10n_de(self):
        self.assertLocalizedHolidays(
            "de",
            ("2022-01-01", "Neujahr"),
            ("2022-04-17", "Ostern"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Tag der Arbeit"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-05", "Pfingsten"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-07-21", "Nationalfeiertag"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Waffenstillstand"),
            ("2022-12-25", "Weihnachten"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-17", "Easter"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-07-21", "National Day"),
            ("2022-08-15", "Assumption of Mary"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-11", "Armistice Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Nouvel An"),
            ("2022-04-17", "Pâques"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-26", "Ascension"),
            ("2022-06-05", "Pentecôte"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-21", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-11-01", "Toussaint"),
            ("2022-11-11", "Jour de l'Armistice"),
            ("2022-12-25", "Noël"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-07-21", "Національне свято"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День перемирʼя"),
            ("2022-12-25", "Різдво Христове"),
        )
