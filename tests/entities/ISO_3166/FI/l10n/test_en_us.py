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
        super().setUpClass(FiHolidays, language="en_US")

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-02-05", "Runeberg Day"),
            ("2022-02-28", "Kalevala Day, Day of Finnish Culture"),
            ("2022-03-19", "Minna Canth Day, Day of Equality"),
            ("2022-04-09", "Mikael Agricola Day, Day of the Finnish Language"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "National War Veterans' Day"),
            ("2022-05-01", "May Day"),
            ("2022-05-08", "Mothers' Day"),
            ("2022-05-09", "Europe Day"),
            ("2022-05-12", "J. V. Snellman Day, Day of Finnish Heritage"),
            ("2022-05-15", "Remembrance Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Flag Day of the Finnish Defense Forces"),
            ("2022-06-24", "Midsummer Eve"),
            ("2022-06-25", "Midsummer Day"),
            ("2022-07-06", "Eino Leino Day, Day of Summer and Poetry"),
            ("2022-08-27", "Finland's Nature Day"),
            ("2022-10-01", "Miina Sillanpää Day, Day of Civic Participation"),
            ("2022-10-10", "Aleksis Kivi Day, Day of Finnish Literature"),
            ("2022-10-24", "United Nations Day"),
            ("2022-11-05", "All Saints' Day"),
            ("2022-11-06", "Finnish Swedish Heritage Day, svenska dagen"),
            ("2022-11-13", "Fathers' Day"),
            ("2022-11-20", "Day of Children's Rights"),
            ("2022-12-06", "Independence Day"),
            ("2022-12-08", "Jean Sibelius Day, Day of Finnish Music"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )
