#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.dominica import Dominica, DM, DMA
from tests.common import CommonCountryTests


class TestDominica(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Dominica)

    def test_country_aliases(self):
        self.assertAliases(Dominica, DM, DMA)

    def test_no_holidays(self):
        self.assertNoHolidays(Dominica(years=1989))

    def test_special_holidays(self):
        self.assertHoliday(
            "2009-07-28",
            "2009-09-03",
            "2010-01-04",
            "2019-09-19",
        )

    def test_labour_day(self):
        name = "Labour Day"

        # May, 1st.
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1990, 2010)))
        self.assertNoNonObservedHoliday(
            "1994-05-02",
            "2005-05-02",
        )

        # 1st Monday of May.
        dt = (
            "2010-05-03",
            "2011-05-02",
            "2012-05-07",
            "2013-05-06",
            "2014-05-05",
            "2015-05-04",
            "2016-05-02",
            "2017-05-01",
            "2018-05-07",
            "2019-05-06",
            "2020-05-04",
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
        )
        self.assertHolidayName(name, dt)

    def test_first_monday_of_august_holiday(self):
        name_first_mon_aug = "First Monday of August"
        name_emancipation_day = "Emancipation Day"

        dt = (
            "2010-08-02",
            "2011-08-01",
            "2012-08-06",
            "2013-08-05",
            "2014-08-04",
            "2015-08-03",
            "2016-08-01",
            "2017-08-07",
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
        )
        self.assertHolidayName(name_emancipation_day, dt)
        self.assertNoHolidayName(name_first_mon_aug, range(1998, 2051))
        self.assertNoHolidayName(name_emancipation_day, range(1990, 1998))

    def test_2010_public_holidays(self):
        # https://www.dominica-weekly.com/images/dominica-calendar-2010/1600-1280.jpg
        self.assertHolidays(
            Dominica(years=2010),
            ("2010-01-01", "New Year's Day"),
            ("2010-01-04", "Special Public Holiday"),
            ("2010-02-15", "Carnival Monday"),
            ("2010-02-16", "Carnival Tuesday"),
            ("2010-04-02", "Good Friday"),
            ("2010-04-05", "Easter Monday"),
            ("2010-05-03", "Labour Day"),
            ("2010-05-24", "Whit Monday"),
            ("2010-08-02", "Emancipation Day"),
            ("2010-11-03", "Independence Day"),
            ("2010-11-04", "National Day of Community Service"),
            ("2010-12-25", "Christmas Day"),
            ("2010-12-26", "Boxing Day"),
            ("2010-12-27", "Boxing Day (observed)"),
        )

    def test_2011_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2011),
            ("2011-01-01", "New Year's Day"),
            ("2011-03-07", "Carnival Monday"),
            ("2011-03-08", "Carnival Tuesday"),
            ("2011-04-22", "Good Friday"),
            ("2011-04-25", "Easter Monday"),
            ("2011-05-02", "Labour Day"),
            ("2011-06-13", "Whit Monday"),
            ("2011-08-01", "Emancipation Day"),
            ("2011-11-03", "Independence Day"),
            ("2011-11-04", "National Day of Community Service"),
            ("2011-12-25", "Christmas Day"),
            ("2011-12-26", "Boxing Day"),
            ("2011-12-27", "Christmas Day (observed)"),
        )

    def test_2012_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2012),
            ("2012-01-01", "New Year's Day"),
            ("2012-01-02", "New Year's Day (observed)"),
            ("2012-02-20", "Carnival Monday"),
            ("2012-02-21", "Carnival Tuesday"),
            ("2012-04-06", "Good Friday"),
            ("2012-04-09", "Easter Monday"),
            ("2012-05-07", "Labour Day"),
            ("2012-05-28", "Whit Monday"),
            ("2012-08-06", "Emancipation Day"),
            ("2012-11-03", "Independence Day"),
            ("2012-11-04", "National Day of Community Service"),
            ("2012-11-05", "National Day of Community Service (observed)"),
            ("2012-12-25", "Christmas Day"),
            ("2012-12-26", "Boxing Day"),
        )

    def test_2013_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2013),
            ("2013-01-01", "New Year's Day"),
            ("2013-02-11", "Carnival Monday"),
            ("2013-02-12", "Carnival Tuesday"),
            ("2013-03-29", "Good Friday"),
            ("2013-04-01", "Easter Monday"),
            ("2013-05-06", "Labour Day"),
            ("2013-05-20", "Whit Monday"),
            ("2013-08-05", "Emancipation Day"),
            ("2013-11-03", "Independence Day"),
            ("2013-11-04", "National Day of Community Service"),
            ("2013-11-05", "Independence Day (observed)"),
            ("2013-12-25", "Christmas Day"),
            ("2013-12-26", "Boxing Day"),
        )

    def test_2014_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2014),
            ("2014-01-01", "New Year's Day"),
            ("2014-03-03", "Carnival Monday"),
            ("2014-03-04", "Carnival Tuesday"),
            ("2014-04-18", "Good Friday"),
            ("2014-04-21", "Easter Monday"),
            ("2014-05-05", "Labour Day"),
            ("2014-06-09", "Whit Monday"),
            ("2014-08-04", "Emancipation Day"),
            ("2014-11-03", "Independence Day"),
            ("2014-11-04", "National Day of Community Service"),
            ("2014-12-25", "Christmas Day"),
            ("2014-12-26", "Boxing Day"),
        )

    def test_2015_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2015),
            ("2015-01-01", "New Year's Day"),
            ("2015-02-16", "Carnival Monday"),
            ("2015-02-17", "Carnival Tuesday"),
            ("2015-04-03", "Good Friday"),
            ("2015-04-06", "Easter Monday"),
            ("2015-05-04", "Labour Day"),
            ("2015-05-25", "Whit Monday"),
            ("2015-08-03", "Emancipation Day"),
            ("2015-11-03", "Independence Day"),
            ("2015-11-04", "National Day of Community Service"),
            ("2015-12-25", "Christmas Day"),
            ("2015-12-26", "Boxing Day"),
        )

    def test_2016_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2016),
            ("2016-01-01", "New Year's Day"),
            ("2016-02-08", "Carnival Monday"),
            ("2016-02-09", "Carnival Tuesday"),
            ("2016-03-25", "Good Friday"),
            ("2016-03-28", "Easter Monday"),
            ("2016-05-02", "Labour Day"),
            ("2016-05-16", "Whit Monday"),
            ("2016-08-01", "Emancipation Day"),
            ("2016-11-03", "Independence Day"),
            ("2016-11-04", "National Day of Community Service"),
            ("2016-12-25", "Christmas Day"),
            ("2016-12-26", "Boxing Day"),
            ("2016-12-27", "Christmas Day (observed)"),
        )

    def test_2017_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2017),
            ("2017-01-01", "New Year's Day"),
            ("2017-01-02", "New Year's Day (observed)"),
            ("2017-02-27", "Carnival Monday"),
            ("2017-02-28", "Carnival Tuesday"),
            ("2017-04-14", "Good Friday"),
            ("2017-04-17", "Easter Monday"),
            ("2017-05-01", "Labour Day"),
            ("2017-06-05", "Whit Monday"),
            ("2017-08-07", "Emancipation Day"),
            ("2017-11-03", "Independence Day"),
            ("2017-11-04", "National Day of Community Service"),
            ("2017-12-25", "Christmas Day"),
            ("2017-12-26", "Boxing Day"),
        )

    def test_2018_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2018),
            ("2018-01-01", "New Year's Day"),
            ("2018-02-12", "Carnival Monday"),
            ("2018-02-13", "Carnival Tuesday"),
            ("2018-03-30", "Good Friday"),
            ("2018-04-02", "Easter Monday"),
            ("2018-05-07", "Labour Day"),
            ("2018-05-21", "Whit Monday"),
            ("2018-08-06", "Emancipation Day"),
            ("2018-11-03", "Independence Day"),
            ("2018-11-04", "National Day of Community Service"),
            ("2018-11-05", "National Day of Community Service (observed)"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Boxing Day"),
        )

    def test_2019_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2019),
            ("2019-01-01", "New Year's Day"),
            ("2019-03-04", "Carnival Monday"),
            ("2019-03-05", "Carnival Tuesday"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-05-06", "Labour Day"),
            ("2019-06-10", "Whit Monday"),
            ("2019-08-05", "Emancipation Day"),
            ("2019-09-19", "Post-Hurricane Maria Thanksgiving Celebrations"),
            ("2019-11-03", "Independence Day"),
            ("2019-11-04", "National Day of Community Service"),
            ("2019-11-05", "Independence Day (observed)"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-26", "Boxing Day"),
        )

    def test_2020_public_holidays(self):
        # https://dominicaconsulategreece.com/dominica/public-holidays/
        self.assertHolidays(
            Dominica(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-02-24", "Carnival Monday"),
            ("2020-02-25", "Carnival Tuesday"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-04", "Labour Day"),
            ("2020-06-01", "Whit Monday"),
            ("2020-08-03", "Emancipation Day"),
            ("2020-11-03", "Independence Day"),
            ("2020-11-04", "National Day of Community Service"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Boxing Day"),
        )

    def test_2021_public_holidays(self):
        # http://www.q95da.com/news/q95-news-received-on-december-29-2020-at-731pm-the-official-public-holiday-calendar-for-2021-approved-by-the-government-of-dominica
        self.assertHolidays(
            Dominica(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-02-15", "Carnival Monday"),
            ("2021-02-16", "Carnival Tuesday"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-03", "Labour Day"),
            ("2021-05-24", "Whit Monday"),
            ("2021-08-02", "Emancipation Day"),
            ("2021-11-03", "Independence Day"),
            ("2021-11-04", "National Day of Community Service"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Boxing Day (observed)"),
        )

    def test_2022_public_holidays(self):
        # https://dominica.gov.dm/about-dominica/public-holidays
        self.assertHolidays(
            Dominica(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Carnival Monday"),
            ("2022-03-01", "Carnival Tuesday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "Labour Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-01", "Emancipation Day"),
            ("2022-11-03", "Independence Day"),
            ("2022-11-04", "National Day of Community Service"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023_public_holidays(self):
        # https://dominica.gov.dm/about-dominica/public-holidays
        self.assertHolidays(
            Dominica(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-02-20", "Carnival Monday"),
            ("2023-02-21", "Carnival Tuesday"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-08-07", "Emancipation Day"),
            ("2023-11-03", "Independence Day"),
            ("2023-11-04", "National Day of Community Service"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024_public_holidays(self):
        # https://dominica.gov.dm/about-dominica/public-holidays
        self.assertHolidays(
            Dominica(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-02-12", "Carnival Monday"),
            ("2024-02-13", "Carnival Tuesday"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "Labour Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-08-05", "Emancipation Day"),
            ("2024-11-03", "Independence Day"),
            ("2024-11-04", "National Day of Community Service"),
            ("2024-11-05", "Independence Day (observed)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
