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

from holidays.constants import OPTIONAL
from holidays.countries.denmark import Denmark, DK, DNK
from tests.common import CommonCountryTests


class TestDenmark(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Denmark)

    def test_country_aliases(self):
        self.assertAliases(Denmark, DK, DNK)

    def test_2016(self):
        # http://www.officeholidays.com/countries/denmark/2016.php
        self.assertHolidays(
            ("2016-01-01", "Nytårsdag"),
            ("2016-03-24", "Skærtorsdag"),
            ("2016-03-25", "Langfredag"),
            ("2016-03-27", "Påskedag"),
            ("2016-03-28", "Anden påskedag"),
            ("2016-04-22", "Store bededag"),
            ("2016-05-05", "Kristi himmelfartsdag"),
            ("2016-05-15", "Pinsedag"),
            ("2016-05-16", "Anden pinsedag"),
            ("2016-12-25", "Juledag"),
            ("2016-12-26", "Anden juledag"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Nytårsdag"),
            ("2022-04-14", "Skærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Påskedag"),
            ("2022-04-18", "Anden påskedag"),
            ("2022-05-13", "Store bededag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Pinsedag"),
            ("2022-06-06", "Anden pinsedag"),
            ("2022-12-25", "Juledag"),
            ("2022-12-26", "Anden juledag"),
        )

    def test_2022_optional(self):
        self.assertHolidays(
            Denmark(categories=OPTIONAL, years=2022),
            ("2022-05-01", "Arbejdernes kampdag"),
            ("2022-06-05", "Grundlovsdag"),
            ("2022-12-24", "Juleaftensdag"),
            ("2022-12-31", "Nytårsaften"),
        )

    def test_2024(self):
        # https://www.officeholidays.com/countries/denmark/2024
        self.assertNoHoliday("2024-04-26")
        self.assertNoHolidayName("Store bededag", Denmark(years=2024))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nytårsdag"),
            ("2022-04-14", "Skærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Påskedag"),
            ("2022-04-18", "Anden påskedag"),
            ("2022-05-01", "Arbejdernes kampdag"),
            ("2022-05-13", "Store bededag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Grundlovsdag; Pinsedag"),
            ("2022-06-06", "Anden pinsedag"),
            ("2022-12-24", "Juleaftensdag"),
            ("2022-12-25", "Juledag"),
            ("2022-12-26", "Anden juledag"),
            ("2022-12-31", "Nytårsaften"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-13", "Great Prayer Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Constitution Day; Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-13", "День загальної молитви"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "День Конституції; Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
            ("2022-12-31", "Переддень Нового року"),
        )
