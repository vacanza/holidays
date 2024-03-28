#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.luxembourg import Luxembourg, LU, LUX
from tests.common import CommonCountryTests


class TestLuxembourg(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Luxembourg)

    def test_country_aliases(self):
        self.assertAliases(Luxembourg, LU, LUX)

    def test_2018(self):
        self.assertHolidays(
            ("2018-01-01", "Neijoerschdag"),
            ("2018-04-02", "Ouschterméindeg"),
            ("2018-05-01", "Dag vun der Aarbecht"),
            ("2018-05-10", "Christi Himmelfaart"),
            ("2018-05-21", "Péngschtméindeg"),
            ("2018-06-23", "Nationalfeierdag"),
            ("2018-08-15", "Léiffrawëschdag"),
            ("2018-11-01", "Allerhellgen"),
            ("2018-12-25", "Chrëschtdag"),
            ("2018-12-26", "Stiefesdag"),
        )

    def test_2019(self):
        self.assertHolidays(
            ("2019-01-01", "Neijoerschdag"),
            ("2019-04-22", "Ouschterméindeg"),
            ("2019-05-01", "Dag vun der Aarbecht"),
            ("2019-05-09", "Europadag"),
            ("2019-05-30", "Christi Himmelfaart"),
            ("2019-06-10", "Péngschtméindeg"),
            ("2019-06-23", "Nationalfeierdag"),
            ("2019-08-15", "Léiffrawëschdag"),
            ("2019-11-01", "Allerhellgen"),
            ("2019-12-25", "Chrëschtdag"),
            ("2019-12-26", "Stiefesdag"),
        )

    def test_2020(self):
        self.assertHolidays(
            ("2020-01-01", "Neijoerschdag"),
            ("2020-04-13", "Ouschterméindeg"),
            ("2020-05-01", "Dag vun der Aarbecht"),
            ("2020-05-09", "Europadag"),
            ("2020-05-21", "Christi Himmelfaart"),
            ("2020-06-01", "Péngschtméindeg"),
            ("2020-06-23", "Nationalfeierdag"),
            ("2020-08-15", "Léiffrawëschdag"),
            ("2020-11-01", "Allerhellgen"),
            ("2020-12-25", "Chrëschtdag"),
            ("2020-12-26", "Stiefesdag"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neijoerschdag"),
            ("2022-04-18", "Ouschterméindeg"),
            ("2022-05-01", "Dag vun der Aarbecht"),
            ("2022-05-09", "Europadag"),
            ("2022-05-26", "Christi Himmelfaart"),
            ("2022-06-06", "Péngschtméindeg"),
            ("2022-06-23", "Nationalfeierdag"),
            ("2022-08-15", "Léiffrawëschdag"),
            ("2022-11-01", "Allerhellgen"),
            ("2022-12-25", "Chrëschtdag"),
            ("2022-12-26", "Stiefesdag"),
        )

    def test_l10n_de(self):
        self.assertLocalizedHolidays(
            "de",
            ("2022-01-01", "Neujahr"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Tag der Arbeit"),
            ("2022-05-09", "Europatag"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-23", "Nationalfeiertag"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-12-25", "Weihnachten"),
            ("2022-12-26", "Zweiter Weihnachtsfeiertag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-09", "Europe Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-23", "National Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "St. Stephen's Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Jour de l'an"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-09", "Journée de l'Europe"),
            ("2022-05-26", "Ascension"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-06-23", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-11-01", "Toussaint"),
            ("2022-12-25", "Noël"),
            ("2022-12-26", "St. Etienne"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-09", "День Європи"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-23", "Національне свято"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День Святого Стефана"),
        )
