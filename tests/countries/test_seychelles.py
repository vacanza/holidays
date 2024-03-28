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

from holidays.countries.seychelles import Seychelles, SC, SYC
from tests.common import CommonCountryTests


class TestSeychelles(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Seychelles)

    def test_country_aliases(self):
        self.assertAliases(Seychelles, SC, SYC)

    def test_no_holidays(self):
        self.assertNoHolidays(Seychelles(years=1993))

    def test_special_holidays(self):
        # Election Dates have its own separate checklists.
        self.assertHoliday(
            "2007-05-12",
            "2011-05-21",
            "2011-10-01",
            "2015-12-05",
            "2015-12-18",
            "2016-09-10",
            "2019-03-07",
            "2020-01-03",
            "2020-10-24",
            "2020-10-26",
        )

    def test_2009(self):
        # https://web.archive.org/web/20091208104016/https://www.cbs.sc/PublicHolidays.html
        self.assertHolidays(
            Seychelles(years=2009),
            ("2009-01-01", "New Year's Day"),
            ("2009-01-02", "New Year Holiday"),
            ("2009-04-10", "Good Friday"),
            ("2009-04-11", "Easter Saturday"),
            ("2009-05-01", "Labour Day"),
            ("2009-06-05", "Liberation Day"),
            ("2009-06-11", "The Fete Dieu"),
            ("2009-06-18", "National Day"),
            ("2009-06-29", "Independence Day"),
            ("2009-08-15", "Assumption Day"),
            ("2009-11-01", "All Saints Day"),
            ("2009-11-02", "All Saints Day (observed)"),
            ("2009-12-08", "The Feast of the Immaculate Conception"),
            ("2009-12-25", "Christmas Day"),
        )

    def test_2012(self):
        # https://web.archive.org/web/20121023221205/https://www.cbs.sc/PublicHolidays.html
        self.assertHolidays(
            Seychelles(years=2012),
            ("2012-01-01", "New Year's Day"),
            ("2012-01-02", "New Year Holiday"),
            ("2012-04-06", "Good Friday"),
            ("2012-04-07", "Easter Saturday"),
            ("2012-05-01", "Labour Day"),
            ("2012-06-05", "Liberation Day"),
            ("2012-06-07", "The Fete Dieu"),
            ("2012-06-18", "National Day"),
            ("2012-06-29", "Independence Day"),
            ("2012-08-15", "Assumption Day"),
            ("2012-11-01", "All Saints Day"),
            ("2012-12-08", "The Feast of the Immaculate Conception"),
            ("2012-12-25", "Christmas Day"),
        )

    def test_2019(self):
        # https://web.archive.org/web/20191029202210/http://cbs.sc/PublicHolidays.html
        self.assertHolidays(
            Seychelles(years=2019),
            ("2019-01-01", "New Year's Day"),
            ("2019-01-02", "New Year Holiday"),
            ("2019-03-07", "Funeral of the Former President France Albert René"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-20", "Easter Saturday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-05-01", "Labour Day"),
            ("2019-06-20", "The Fete Dieu"),
            ("2019-06-18", "Constitution Day"),
            ("2019-06-29", "Independence (National) Day"),
            ("2019-08-15", "Assumption Day"),
            ("2019-11-01", "All Saints Day"),
            ("2019-12-08", "The Feast of the Immaculate Conception"),
            ("2019-12-09", "The Feast of the Immaculate Conception (observed)"),
            ("2019-12-25", "Christmas Day"),
        )

    def test_2021(self):
        # https://web.archive.org/web/20211206090711/https://www.cbs.sc/PublicHolidays.html
        self.assertHolidays(
            Seychelles(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-01-02", "New Year Holiday"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-03", "Easter Saturday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-01", "Labour Day"),
            ("2021-06-03", "The Fete Dieu"),
            ("2021-06-18", "Constitution Day"),
            ("2021-06-29", "Independence (National) Day"),
            ("2021-08-15", "Assumption Day"),
            ("2021-08-16", "Assumption Day (observed)"),
            ("2021-11-01", "All Saints Day"),
            ("2021-12-08", "The Feast of the Immaculate Conception"),
            ("2021-12-25", "Christmas Day"),
        )

    def test_2023(self):
        # https://web.archive.org/web/20230318041823/https://www.cbs.sc/PublicHolidays.html
        self.assertHolidays(
            Seychelles(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year Holiday"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-08", "Easter Saturday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-06-08", "The Fete Dieu"),
            ("2023-06-18", "Constitution Day"),
            ("2023-06-19", "Constitution Day (observed)"),
            ("2023-06-29", "Independence (National) Day"),
            ("2023-08-15", "Assumption Day"),
            ("2023-11-01", "All Saints Day"),
            ("2023-12-08", "The Feast of the Immaculate Conception"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_default(self):
        # https://www.psb.gov.sc/public-holidays
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year Holiday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Easter Saturday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-30", "The Fete Dieu"),
            ("2024-06-18", "Constitution Day"),
            ("2024-06-29", "Independence (National) Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-11-01", "All Saints Day"),
            ("2024-12-08", "The Feast of the Immaculate Conception"),
            ("2024-12-09", "The Feast of the Immaculate Conception (observed)"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year Holiday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Easter Saturday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-30", "Corpus Christi"),
            ("2024-06-18", "Constitution Day"),
            ("2024-06-29", "Independence (National) Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-11-01", "All Saints Day"),
            ("2024-12-08", "Immaculate Conception"),
            ("2024-12-09", "Immaculate Conception (observed)"),
            ("2024-12-25", "Christmas Day"),
        )
