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

from holidays.entities.ISO_3166.FI import FiHolidays
from tests.common import CommonCountryTests


class TestFiHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(FiHolidays)

    def test_fi(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Uudenvuodenpäivä"),
            ("2022-01-06", "Loppiainen"),
            ("2022-02-05", "Runebergin päivä"),
            ("2022-02-28", "Kalevalan päivä, suomalaisen kulttuurin päivä"),
            ("2022-03-19", "Minna Canthin päivä, tasa-arvon päivä"),
            ("2022-04-09", "Mikael Agricolan päivä, suomen kielen päivä"),
            ("2022-04-15", "Pitkäperjantai"),
            ("2022-04-17", "Pääsiäispäivä"),
            ("2022-04-18", "Toinen pääsiäispäivä"),
            ("2022-04-27", "Kansallinen veteraanipäivä"),
            ("2022-05-01", "Vappu"),
            ("2022-05-08", "Äitienpäivä"),
            ("2022-05-09", "Eurooppa-päivä"),
            ("2022-05-12", "J.V. Snellmanin päivä, suomalaisuuden päivä"),
            ("2022-05-15", "Kaatuneitten muistopäivä"),
            ("2022-05-26", "Helatorstai"),
            ("2022-06-05", "Helluntaipäivä"),
            ("2022-06-06", "Puolustusvoimain lippujuhlan päivä"),
            ("2022-06-24", "Juhannusaatto"),
            ("2022-06-25", "Juhannuspäivä"),
            ("2022-07-06", "Eino Leinon päivä, runon ja suven päivä"),
            ("2022-08-27", "Suomen luonnon päivä"),
            ("2022-10-01", "Miina Sillanpään ja kansalaisvaikuttamisen päivä"),
            ("2022-10-10", "Aleksis Kiven päivä, suomalaisen kirjallisuuden päivä"),
            ("2022-10-24", "YK:n päivä"),
            ("2022-11-05", "Pyhäinpäivä"),
            ("2022-11-06", "Ruotsalaisuuden päivä, Kustaa Aadolfin päivä"),
            ("2022-11-13", "Isänpäivä"),
            ("2022-11-20", "Lapsen oikeuksien päivä"),
            ("2022-12-06", "Itsenäisyyspäivä"),
            ("2022-12-08", "Jean Sibeliuksen päivä, suomalaisen musiikin päivä"),
            ("2022-12-24", "Jouluaatto"),
            ("2022-12-25", "Joulupäivä"),
            ("2022-12-26", "Tapaninpäivä"),
        )
