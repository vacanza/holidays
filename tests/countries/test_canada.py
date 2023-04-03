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

from datetime import date
from datetime import timedelta as td

from holidays.countries.canada import Canada, CA, CAN
from tests.common import TestCase


class TestCanada(TestCase):
    def setUp(self):
        super().setUp()
        self.holidays = Canada(observed=False)

    @classmethod
    def setUpClass(cls):
        super().setUpClass(Canada)

    def test_country_aliases(self):
        self.assertCountryAliases(Canada, CA, CAN)

    def test_new_years(self):
        self.assertNotIn(date(1866, 12, 31), self.holidays)
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2011, 1, 3), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertIn(date(2011, 1, 3), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_islander_day(self):
        pei_holidays = Canada(subdiv="PE")
        for dt in [
            date(2009, 2, 9),
            date(2010, 2, 15),
            date(2011, 2, 21),
            date(2012, 2, 20),
            date(2013, 2, 18),
            date(2014, 2, 17),
            date(2015, 2, 16),
            date(2016, 2, 15),
            date(2020, 2, 17),
        ]:
            if dt.year >= 2010:
                self.assertNotEqual(self.holidays[dt], "Islander Day")
            elif dt.year == 2009:
                self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, pei_holidays)
            self.assertNotIn(dt + td(days=-1), pei_holidays)
            self.assertNotIn(dt + td(days=+1), pei_holidays)

    def test_yukon_heritage_day(self):
        # https://www.timeanddate.com/holidays/canada/heritage-day-yukon
        yt_holidays = Canada(subdiv="YT")
        for dt in [
            date(2017, 2, 24),
            date(2018, 2, 23),
            date(2019, 2, 22),
            date(2020, 2, 21),
            date(2021, 2, 26),
            date(2022, 2, 25),
        ]:
            self.assertIn(dt, yt_holidays)
            self.assertNotIn(dt + td(days=-1), yt_holidays)
            self.assertNotIn(dt + td(days=+1), yt_holidays)

    def test_family_day(self):
        ab_holidays = Canada(subdiv="AB")
        bc_holidays = Canada(subdiv="BC")
        mb_holidays = Canada(subdiv="MB")
        sk_holidays = Canada(subdiv="SK")
        nb_holidays = Canada(subdiv="NB")
        ns_holidays = Canada(subdiv="NS")
        for dt in [
            date(1990, 2, 19),
            date(1999, 2, 15),
            date(2000, 2, 21),
            date(2006, 2, 20),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertNotIn(dt, bc_holidays)
            self.assertNotIn(dt, mb_holidays)
            self.assertNotIn(dt, sk_holidays)
        dt = date(2007, 2, 19)
        self.assertNotIn(dt, self.holidays)
        self.assertIn(dt, ab_holidays)
        self.assertNotIn(dt, bc_holidays)
        self.assertNotIn(dt, mb_holidays)
        self.assertIn(dt, sk_holidays)
        for dt in [
            date(2008, 2, 18),
            date(2012, 2, 20),
            date(2014, 2, 17),
            date(2018, 2, 19),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertNotIn(dt, bc_holidays)
            self.assertIn(dt, mb_holidays)
            self.assertIn(dt, sk_holidays)
        for dt in [date(2018, 2, 19)]:
            self.assertIn(dt, nb_holidays)
        for dt in [date(2019, 2, 18), date(2020, 2, 17)]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertIn(dt, bc_holidays)
            self.assertIn(dt, mb_holidays)
            self.assertIn(dt, sk_holidays)
        for dt in [date(2013, 2, 11), date(2016, 2, 8)]:
            self.assertNotIn(dt, self.holidays)
            self.assertNotIn(dt, ab_holidays)
            self.assertIn(dt, bc_holidays)
            self.assertNotIn(dt, mb_holidays)
            self.assertNotIn(dt, sk_holidays)
        self.assertEqual(mb_holidays[date(2014, 2, 17)], "Louis Riel Day")
        self.assertEqual(ns_holidays[date(2015, 2, 16)], "Heritage Day")

    def test_st_patricks_day(self):
        nl_holidays = Canada(subdiv="NL", observed=False)
        for dt in [
            date(1900, 3, 19),
            date(1999, 3, 15),
            date(2000, 3, 20),
            date(2012, 3, 19),
            date(2013, 3, 18),
            date(2014, 3, 17),
            date(2015, 3, 16),
            date(2016, 3, 14),
            date(2020, 3, 16),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + td(days=-1), nl_holidays)
            self.assertNotIn(dt + td(days=+1), nl_holidays)

    def test_good_friday(self):
        for dt in [
            date(1900, 4, 13),
            date(1901, 4, 5),
            date(1902, 3, 28),
            date(1999, 4, 2),
            date(2000, 4, 21),
            date(2010, 4, 2),
            date(2018, 3, 30),
            date(2019, 4, 19),
            date(2020, 4, 10),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_easter_monday(self):
        for dt in [
            date(1900, 4, 16),
            date(1901, 4, 8),
            date(1902, 3, 31),
            date(1999, 4, 5),
            date(2000, 4, 24),
            date(2010, 4, 5),
            date(2018, 4, 2),
            date(2019, 4, 22),
            date(2020, 4, 13),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_st_georges_day(self):
        nl_holidays = Canada(subdiv="NL")
        for dt in [
            date(1990, 4, 23),
            date(1999, 4, 26),
            date(2010, 4, 19),
            date(2016, 4, 25),
            date(2020, 4, 20),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + td(days=-1), nl_holidays)
            self.assertNotIn(dt + td(days=+1), nl_holidays)

    def test_victoria_day(self):
        for dt in [
            date(1953, 5, 18),
            date(1999, 5, 24),
            date(2000, 5, 22),
            date(2010, 5, 24),
            date(2015, 5, 18),
            date(2020, 5, 18),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_national_aboriginal_day(self):
        nt_holidays = Canada(subdiv="NT")
        self.assertNotIn(date(1995, 6, 21), nt_holidays)
        for year in range(1996, 2100):
            dt = date(year, 6, 21)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nt_holidays)
            self.assertNotIn(dt + td(days=-1), nt_holidays)
            self.assertNotIn(dt + td(days=+1), nt_holidays)

    def test_st_jean_baptiste_day(self):
        qc_holidays = Canada(subdiv="QC", observed=False)
        self.assertNotIn(date(1924, 6, 24), qc_holidays)
        for year in range(1925, 2100):
            dt = date(year, 6, 24)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, qc_holidays)
            self.assertNotIn(dt + td(days=-1), qc_holidays)
            self.assertNotIn(dt + td(days=+1), qc_holidays)
        self.assertNotIn(date(2001, 6, 25), qc_holidays)
        qc_holidays.observed = True
        self.assertIn(date(2001, 6, 25), qc_holidays)

    def test_discovery_day(self):
        nl_holidays = Canada(subdiv="NL")
        yt_holidays = Canada(subdiv="YT")
        for dt in [
            date(1997, 6, 23),
            date(1999, 6, 21),
            date(2000, 6, 26),
            date(2010, 6, 21),
            date(2016, 6, 27),
            date(2020, 6, 22),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt, yt_holidays)
        for dt in [
            date(1912, 8, 19),
            date(1999, 8, 16),
            date(2000, 8, 21),
            date(2006, 8, 21),
            date(2016, 8, 15),
            date(2020, 8, 17),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertNotIn(dt, nl_holidays)
            self.assertIn(dt, yt_holidays)

    def test_canada_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
        self.assertNotIn(date(2006, 7, 3), self.holidays)
        self.assertNotIn(date(2007, 7, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2006, 7, 3), self.holidays)
        self.assertIn(date(2007, 7, 2), self.holidays)

    def test_nunavut_day(self):
        nu_holidays = Canada(subdiv="NU", observed=False)
        self.assertNotIn(date(1999, 7, 9), nu_holidays)
        self.assertNotIn(date(2000, 7, 9), nu_holidays)
        self.assertIn(date(2000, 4, 1), nu_holidays)
        for year in range(2001, 2100):
            dt = date(year, 7, 9)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nu_holidays)
            self.assertNotIn(dt + td(days=-1), nu_holidays)
            self.assertNotIn(dt + td(days=+1), nu_holidays)
        self.assertNotIn(date(2017, 7, 10), nu_holidays)
        nu_holidays.observed = True
        self.assertIn(date(2017, 7, 10), nu_holidays)

    def test_civic_holiday(self):
        bc_holidays = Canada(subdiv="BC")
        for dt in [date(1900, 8, 6), date(1955, 8, 1), date(1973, 8, 6)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt, bc_holidays)
        for dt in [
            date(1974, 8, 5),
            date(1999, 8, 2),
            date(2000, 8, 7),
            date(2010, 8, 2),
            date(2015, 8, 3),
            date(2020, 8, 3),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, bc_holidays)

    def test_labour_day(self):
        self.assertNotIn(date(1893, 9, 4), self.holidays)
        for dt in [
            date(1894, 9, 3),
            date(1900, 9, 3),
            date(1999, 9, 6),
            date(2000, 9, 4),
            date(2014, 9, 1),
            date(2015, 9, 7),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_national_day_for_truth_and_reconciliation(self):
        bc_holidays = Canada(subdiv="BC")
        mb_holidays = Canada(subdiv="MB")
        ns_holidays = Canada(subdiv="NS")

        for dt in [
            date(1991, 9, 30),
            date(2020, 9, 30),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt, mb_holidays)
            self.assertNotIn(dt, ns_holidays)
        for dt in [
            date(2021, 9, 30),
            date(2022, 9, 30),
        ]:
            self.assertIn(dt, mb_holidays)
            self.assertIn(dt, ns_holidays)
            self.assertNotIn(dt + td(days=-1), mb_holidays)
            self.assertNotIn(dt + td(days=-1), ns_holidays)
            self.assertNotIn(dt, self.holidays)
        for dt in [
            date(2023, 9, 30),
            date(2024, 9, 30),
            date(2030, 9, 30),
        ]:
            self.assertIn(dt, mb_holidays)
            self.assertIn(dt, ns_holidays)
            self.assertIn(dt, bc_holidays)
            self.assertNotIn(dt + td(days=-1), mb_holidays)
            self.assertNotIn(dt + td(days=-1), ns_holidays)
            self.assertNotIn(dt + td(days=-1), bc_holidays)
            self.assertNotIn(dt, self.holidays)

    def test_thanksgiving(self):
        ns_holidays = Canada(subdiv="NB")
        for dt in [
            date(1931, 10, 12),
            date(1990, 10, 8),
            date(1999, 10, 11),
            date(2000, 10, 9),
            date(2013, 10, 14),
            date(2020, 10, 12),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt, ns_holidays)

    def test_remembrance_day(self):
        ab_holidays = Canada(subdiv="AB", observed=False)
        nl_holidays = Canada(subdiv="NL", observed=False)
        self.assertNotIn(date(1930, 11, 11), ab_holidays)
        self.assertNotIn(date(1930, 11, 11), nl_holidays)
        for year in range(1931, 2100):
            dt = date(year, 11, 11)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + td(days=-1), nl_holidays)
            self.assertNotIn(dt + td(days=+1), nl_holidays)
        self.assertNotIn(date(2007, 11, 12), ab_holidays)
        self.assertNotIn(date(2007, 11, 12), nl_holidays)
        ab_holidays.observed = True
        nl_holidays.observed = True
        self.assertNotIn(date(2007, 11, 12), ab_holidays)
        self.assertIn(date(2007, 11, 12), nl_holidays)

    def test_christmas_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.assertNotEqual(
            self.holidays[date(2011, 12, 26)],
            "Christmas Day (Observed)",
        )
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 27), self.holidays)
        self.assertEqual(
            self.holidays[date(2011, 12, 27)],
            "Christmas Day (Observed)",
        )

    def test_boxing_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
        self.assertNotIn(date(2009, 12, 28), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2009, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 27), self.holidays)

    def test_queens_funeral(self):
        for subdiv in Canada.subdivisions:
            holidays_canada = Canada(subdiv=subdiv)
            for year in range(1900, 2100):
                if year == 2022 and subdiv in {
                    "BC",
                    "NB",
                    "NL",
                    "NS",
                    "PE",
                    "YT",
                }:
                    self.assertIn(date(year, 9, 19), holidays_canada)
                else:
                    self.assertNotIn(date(year, 9, 19), holidays_canada)

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                ca = Canada(language=language)
                self.assertEqual(ca["2022-01-01"], "New Year's Day")
                self.assertEqual(ca["2022-12-25"], "Christmas Day")
                self.assertEqual(ca["2022-12-27"], "Christmas Day (Observed)")

            run_tests((Canada.default_language, None, "invalid"))

            self.set_language("fr")
            run_tests((Canada.default_language,))

    def test_l10n_fr(self):
        fr = "fr"

        ca = Canada(language=fr)
        self.assertEqual(ca["2018-01-01"], "Jour de l'an")
        self.assertEqual(ca["2022-12-25"], "Jour de Noël")
        self.assertEqual(ca["2022-12-27"], "Jour de Noël (Observé)")

        self.set_language(fr)
        for language in (None, fr, "invalid"):
            ca = Canada(language=language)
            self.assertEqual(ca["2018-01-01"], "Jour de l'an")
            self.assertEqual(ca["2022-12-25"], "Jour de Noël")
            self.assertEqual(ca["2022-12-27"], "Jour de Noël (Observé)")
