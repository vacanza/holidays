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

from holidays.countries.belarus import Belarus, BY, BLR
from tests.common import TestCase


class TestBelarus(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Belarus)

    def test_country_aliases(self):
        self.assertCountryAliases(Belarus, BY, BLR)

    def test_2018(self):
        # http://calendar.by/procal.php?year=2018
        # https://www.officeholidays.com/countries/belarus/index.php
        self.assertHoliday(
            "2018-01-01",
            "2018-01-07",
            "2018-03-08",
            "2018-04-17",
            "2018-05-01",
            "2018-05-09",
            "2018-07-03",
            "2018-11-07",
            "2018-12-25",
        )

    def test_new_year(self):
        self.assertHoliday(
            "2019-01-01",
            "2020-01-01",
            "2020-01-02",
            "2021-01-01",
            "2021-01-02",
        )

        self.assertNoHoliday("2019-01-02")

    def test_radunitsa(self):
        # http://calendar.by/content.php?id=20
        self.assertHoliday(
            "2012-04-24",
            "2013-05-14",
            "2014-04-29",
            "2015-04-21",
            "2016-05-10",
            "2017-04-25",
            "2018-04-17",
            "2019-05-07",
            "2020-04-28",
            "2021-05-11",
            "2022-05-03",
            "2023-04-25",
            "2024-05-14",
            "2025-04-29",
            "2026-04-21",
            "2027-05-11",
            "2028-04-25",
            "2029-04-17",
            "2030-05-07",
        )

    def test_pre_1998(self):
        self.assertNoHoliday("1997-07-03")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новы год"),
            ("2022-01-02", "Новы год"),
            ("2022-01-07", "Нараджэнне Хрыстова (праваслаўнае Раство)"),
            ("2022-03-08", "Дзень жанчын"),
            ("2022-05-01", "Свята працы"),
            ("2022-05-03", "Радаўніца"),
            ("2022-05-09", "Дзень Перамогі"),
            (
                "2022-07-03",
                "Дзень Незалежнасці Рэспублікі Беларусь (Дзень Рэспублікі)",
            ),
            ("2022-11-07", "Дзень Кастрычніцкай рэвалюцыі"),
            ("2022-12-25", "Нараджэнне Хрыстова (каталіцкае Раство)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-03-08", "Women's Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-03", "Radunitsa"),
            ("2022-05-09", "Victory Day"),
            ("2022-07-03", "Independence Day (Republic Day)"),
            ("2022-11-07", "October Revolution Day"),
            ("2022-12-25", "Catholic Christmas Day"),
        )
