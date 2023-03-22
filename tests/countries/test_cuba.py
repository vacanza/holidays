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

from holidays.countries.cuba import Cuba, CU, CUB
from tests.common import TestCase


class TestCuba(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Cuba)

    def test_country_aliases(self):
        self.assertCountryAliases(Cuba, CU, CUB)

    def test_1968(self):
        self.assertHolidayDates(
            Cuba(years=1968),
            "1968-01-01",
            "1968-05-01",
            "1968-07-25",
            "1968-07-26",
            "1968-07-27",
            "1968-10-10",
            "1968-12-25",
        )

    def test_1969(self):
        self.assertHolidayDates(
            Cuba(years=1969),
            "1969-01-01",
            "1969-05-01",
            "1969-07-25",
            "1969-07-26",
            "1969-07-27",
            "1969-10-10",
        )

    def test_1970(self):
        self.assertHolidayDates(
            Cuba(years=1970),
            "1970-01-01",
            "1970-05-01",
            "1970-07-25",
            "1970-07-26",
            "1970-07-27",
            "1970-10-10",
        )

    def test_1996(self):
        self.assertHolidayDates(
            Cuba(years=1996),
            "1996-01-01",
            "1996-05-01",
            "1996-07-25",
            "1996-07-26",
            "1996-07-27",
            "1996-10-10",
        )

    def test_1997(self):
        self.assertHolidayDates(
            Cuba(years=1997),
            "1997-01-01",
            "1997-05-01",
            "1997-07-25",
            "1997-07-26",
            "1997-07-27",
            "1997-10-10",
            "1997-12-25",
        )

    def test_1998(self):
        self.assertHolidayDates(
            Cuba(years=1998),
            "1998-01-01",
            "1998-05-01",
            "1998-07-25",
            "1998-07-26",
            "1998-07-27",
            "1998-10-10",
            "1998-12-25",
        )

    def test_2006(self):
        self.assertHolidayDates(
            Cuba(years=2006),
            "2006-01-01",
            "2006-01-02",
            "2006-05-01",
            "2006-07-25",
            "2006-07-26",
            "2006-07-27",
            "2006-10-10",
            "2006-12-25",
        )

    def test_2007(self):
        self.assertHolidayDates(
            Cuba(years=2007),
            "2007-01-01",
            "2007-05-01",
            "2007-07-25",
            "2007-07-26",
            "2007-07-27",
            "2007-10-10",
            "2007-12-25",
            "2007-12-31",
        )

    def test_2008(self):
        self.assertHolidayDates(
            Cuba(years=2008),
            "2008-01-01",
            "2008-01-02",
            "2008-05-01",
            "2008-07-25",
            "2008-07-26",
            "2008-07-27",
            "2008-10-10",
            "2008-12-25",
            "2008-12-31",
        )

    def test_2011(self):
        self.assertHolidayDates(
            Cuba(years=2011),
            "2011-01-01",
            "2011-01-02",
            "2011-05-01",
            "2011-05-02",
            "2011-07-25",
            "2011-07-26",
            "2011-07-27",
            "2011-10-10",
            "2011-12-25",
            "2011-12-31",
        )

    def test_2012(self):
        self.assertHolidayDates(
            Cuba(years=2012),
            "2012-01-01",
            "2012-01-02",
            "2012-04-06",
            "2012-05-01",
            "2012-07-25",
            "2012-07-26",
            "2012-07-27",
            "2012-10-10",
            "2012-12-25",
            "2012-12-31",
        )

    def test_2013(self):
        self.assertHolidayDates(
            Cuba(years=2013),
            "2013-01-01",
            "2013-01-02",
            "2013-03-29",
            "2013-05-01",
            "2013-07-25",
            "2013-07-26",
            "2013-07-27",
            "2013-10-10",
            "2013-12-25",
            "2013-12-31",
        )

    def test_2018(self):
        # https://www.officeholidays.com/countries/cuba/2018
        self.assertHolidayDates(
            Cuba(years=2018),
            "2018-01-01",
            "2018-01-02",
            "2018-03-30",
            "2018-05-01",
            "2018-07-25",
            "2018-07-26",
            "2018-07-27",
            "2018-10-10",
            "2018-12-25",
            "2018-12-31",
        )

    def test_2019(self):
        # https://www.officeholidays.com/countries/cuba/2019
        self.assertHolidayDates(
            Cuba(years=2019),
            "2019-01-01",
            "2019-01-02",
            "2019-04-19",
            "2019-05-01",
            "2019-07-25",
            "2019-07-26",
            "2019-07-27",
            "2019-10-10",
            "2019-12-25",
            "2019-12-31",
        )

    def test_2020(self):
        # https://www.officeholidays.com/countries/cuba/2020
        self.assertHolidayDates(
            Cuba(years=2020),
            "2020-01-01",
            "2020-01-02",
            "2020-04-10",
            "2020-05-01",
            "2020-07-25",
            "2020-07-26",
            "2020-07-27",
            "2020-10-10",
            "2020-12-25",
            "2020-12-31",
        )

    def test_2021(self):
        # https://www.officeholidays.com/countries/cuba/2021
        self.assertHolidayDates(
            Cuba(years=2021),
            "2021-01-01",
            "2021-01-02",
            "2021-04-02",
            "2021-05-01",
            "2021-07-25",
            "2021-07-26",
            "2021-07-27",
            "2021-10-10",
            "2021-10-11",
            "2021-12-25",
            "2021-12-31",
        )

    def test_2022(self):
        # https://www.officeholidays.com/countries/cuba/2022
        self.assertHolidayDates(
            Cuba(years=2022),
            "2022-01-01",
            "2022-01-02",
            "2022-04-15",
            "2022-05-01",
            "2022-05-02",
            "2022-07-25",
            "2022-07-26",
            "2022-07-27",
            "2022-10-10",
            "2022-12-25",
            "2022-12-31",
        )

    def test_2023(self):
        # https://www.officeholidays.com/countries/cuba/2023
        self.assertHolidayDates(
            Cuba(years=2023),
            "2023-01-01",
            "2023-01-02",
            "2023-04-07",
            "2023-05-01",
            "2023-07-25",
            "2023-07-26",
            "2023-07-27",
            "2023-10-10",
            "2023-12-25",
            "2023-12-31",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                cu = Cuba(language=language)
                self.assertEqual(
                    cu["2006-01-02"], "Triunfo de la Revolución (Observado)"
                )
                self.assertEqual(cu["2022-01-01"], "Triunfo de la Revolución")
                self.assertEqual(cu["2022-12-25"], "Día de Navidad")

        run_tests((Cuba.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Cuba.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        cu = Cuba(language=en_us)
        self.assertEqual(cu["2006-01-02"], "Liberation Day (Observed)")
        self.assertEqual(cu["2022-01-01"], "Liberation Day")
        self.assertEqual(cu["2022-12-25"], "Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            cu = Cuba(language=language)
            self.assertEqual(cu["2006-01-02"], "Liberation Day (Observed)")
            self.assertEqual(cu["2022-01-01"], "Liberation Day")
            self.assertEqual(cu["2022-12-25"], "Christmas Day")

    def test_l10n_uk(self):
        uk = "uk"

        cu = Cuba(language=uk)
        self.assertEqual(cu["2006-01-02"], "Тріумф революції (вихідний)")
        self.assertEqual(cu["2022-01-01"], "Тріумф революції")
        self.assertEqual(cu["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            cu = Cuba(language=language)
            self.assertEqual(cu["2006-01-02"], "Тріумф революції (вихідний)")
            self.assertEqual(cu["2022-01-01"], "Тріумф революції")
            self.assertEqual(cu["2022-12-25"], "Різдво Христове")
