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
        super().setUpClass(FiHolidays, language="sv_FI")

    def test_sv_fi(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nyårsdagen"),
            ("2022-01-06", "Trettondag"),
            ("2022-02-05", "Runebergsdagen"),
            ("2022-02-28", "Kalevaladagen, den finska kulturens dag"),
            ("2022-03-19", "Minna Canth-dagen, jämställdhetsdagen"),
            ("2022-04-09", "Mikael Agricoladagen, finska språkets dag"),
            ("2022-04-15", "Långfredagen"),
            ("2022-04-17", "Påskdagen"),
            ("2022-04-18", "Annandag påsk"),
            ("2022-04-27", "Nationella veterandagen"),
            ("2022-05-01", "Första maj"),
            ("2022-05-08", "Mors dag"),
            ("2022-05-09", "Europadagen"),
            ("2022-05-12", "Snellmansdagen, finskhetens dag"),
            ("2022-05-15", "De stupades dag"),
            ("2022-05-26", "Kristi himmelsfärdsdag"),
            ("2022-06-05", "Pingst"),
            ("2022-06-06", "Dagen för försvarets fanfest"),
            ("2022-06-24", "Midsommarafton"),
            ("2022-06-25", "Midsommardagen"),
            ("2022-07-06", "Eino Leino-dagen, diktens och sommarens dag"),
            ("2022-08-27", "Den finska naturens dag"),
            ("2022-10-01", "Miina Sillanpää-dagen, medborgarinflytandets dag"),
            ("2022-10-10", "Aleksis Kivi-dagen, den finska litteraturens dag"),
            ("2022-10-24", "FN-dagen"),
            ("2022-11-05", "Alla helgons dag"),
            ("2022-11-06", "Svenska dagen, Gustav Adolfsdagen"),
            ("2022-11-13", "Fars dag"),
            ("2022-11-20", "Barnkonventionens dag"),
            ("2022-12-06", "Självständigshetsdagen"),
            ("2022-12-08", "Sibeliusdagen, den finländska musikens dag"),
            ("2022-12-24", "Julafton"),
            ("2022-12-25", "Juldagen"),
            ("2022-12-26", "Annandag jul"),
        )
