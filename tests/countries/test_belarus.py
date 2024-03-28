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

from holidays.countries.belarus import Belarus, BY, BLR
from tests.common import CommonCountryTests


class TestBelarus(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Belarus)

    def test_country_aliases(self):
        self.assertAliases(Belarus, BY, BLR)

    def test_no_holidays(self):
        self.assertNoHolidays(Belarus(years=1997))

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

    def test_substituted(self):
        self.assertHoliday(
            "1998-01-02",
            "1998-04-27",
            "1999-01-08",
            "1999-04-19",
            "2000-05-08",
            "2000-11-06",
            "2001-01-02",
            "2001-03-09",
            "2001-04-23",
            "2001-04-30",
            "2001-07-02",
            "2001-12-24",
            "2001-12-31",
            "2002-01-02",
            "2002-05-10",
            "2002-11-08",
            "2003-01-06",
            "2003-05-05",
            "2004-01-02",
            "2004-01-05",
            "2004-01-06",
            "2004-04-19",
            "2005-03-07",
            "2006-01-02",
            "2006-05-08",
            "2006-11-06",
            "2007-01-02",
            "2007-03-09",
            "2007-04-16",
            "2007-04-30",
            "2007-07-02",
            "2007-12-24",
            "2007-12-31",
            "2008-01-02",
            "2008-05-05",
            "2008-07-04",
            "2008-12-26",
            "2009-01-02",
            "2009-04-27",
            "2010-01-08",
            "2010-04-12",
            "2010-05-10",
            "2011-03-07",
            "2011-05-02",
            "2012-03-09",
            "2012-04-23",
            "2012-07-02",
            "2012-12-24",
            "2012-12-31",
            "2013-01-02",
            "2013-05-10",
            "2014-01-02",
            "2014-01-06",
            "2014-04-30",
            "2014-07-04",
            "2014-12-26",
            "2015-01-02",
            "2015-04-20",
            "2016-01-08",
            "2016-03-07",
            "2017-01-02",
            "2017-04-24",
            "2017-05-08",
            "2017-11-06",
            "2018-01-02",
            "2018-03-09",
            "2018-04-16",
            "2018-04-30",
            "2018-07-02",
            "2018-12-24",
            "2018-12-31",
            "2019-05-06",
            "2019-05-08",
            "2019-11-08",
            "2020-01-06",
            "2020-04-27",
            "2021-01-08",
            "2021-05-10",
            "2022-03-07",
            "2022-05-02",
            "2023-04-24",
            "2023-05-08",
            "2023-11-06",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новы год"),
            ("2022-01-02", "Новы год"),
            ("2022-01-07", "Нараджэнне Хрыстова (праваслаўнае Раство)"),
            ("2022-03-07", "Выходны (перанесены з 12.03.2022)"),
            ("2022-03-08", "Дзень жанчын"),
            ("2022-05-01", "Свята працы"),
            ("2022-05-02", "Выходны (перанесены з 14.05.2022)"),
            ("2022-05-03", "Радаўніца"),
            ("2022-05-09", "Дзень Перамогі"),
            ("2022-07-03", "Дзень Незалежнасці Рэспублікі Беларусь (Дзень Рэспублікі)"),
            ("2022-11-07", "Дзень Кастрычніцкай рэвалюцыі"),
            ("2022-12-25", "Нараджэнне Хрыстова (каталіцкае Раство)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-03-07", "Day off (substituted from 03/12/2022)"),
            ("2022-03-08", "Women's Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Day off (substituted from 05/14/2022)"),
            ("2022-05-03", "Radunitsa"),
            ("2022-05-09", "Victory Day"),
            ("2022-07-03", "Independence Day (Republic Day)"),
            ("2022-11-07", "October Revolution Day"),
            ("2022-12-25", "Catholic Christmas Day"),
        )
