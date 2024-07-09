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

from holidays.entities.ISO_3166.DE import DeHolidays
from tests.common import CommonCountryTests


class TestDeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1991, 2050)
        super().setUpClass(DeHolidays, years=years)
        cls.prov_hols = {
            prov: DeHolidays(subdiv=prov, years=years) for prov in DeHolidays.subdivisions
        }

    def test_no_data_before_1990(self):
        self.assertNoHolidays(DeHolidays(years=1989))
        for p in DeHolidays.subdivisions:
            self.assertNoHolidays(DeHolidays(years=1989, subdiv=p))

    def test_1990_present(self):
        y_1990 = set()
        for p in DeHolidays.subdivisions:
            y_1990.update(DeHolidays(years=1990, subdiv=p).values())
        all_h = {  # Holidays names in their chronological order.
            "Tag der Deutschen Einheit",
            "Reformationstag",
            "Allerheiligen",
            "Buß- und Bettag",
            "Erster Weihnachtstag",
            "Zweiter Weihnachtstag",
        }

        self.assertEqual(
            all_h,
            y_1990,
            f"missing: {all_h - y_1990 if len(all_h - y_1990) > 0 else 'no'},"
            f" extra: {y_1990 - all_h if len(y_1990 - all_h) > 0 else 'no'}",
        )

    def test_all_holidays_present(self):
        y_2015 = set()
        for p in DeHolidays.subdivisions:
            y_2015.update(DeHolidays(years=2015, subdiv=p).values())
        all_h = {  # Holidays names in their chronological order.
            "Neujahr",
            "Heilige Drei Könige",
            "Karfreitag",
            "Ostersonntag",
            "Ostermontag",
            "Erster Mai",
            "Christi Himmelfahrt",
            "Pfingstsonntag",
            "Pfingstmontag",
            "Fronleichnam",
            "Mariä Himmelfahrt",
            "Tag der Deutschen Einheit",
            "Reformationstag",
            "Allerheiligen",
            "Buß- und Bettag",
            "Erster Weihnachtstag",
            "Zweiter Weihnachtstag",
        }

        self.assertEqual(
            all_h,
            y_2015,
            f"missing: {all_h - y_2015 if len(all_h - y_2015) > 0 else 'no'},"
            f" extra: {y_2015 - all_h if len(y_2015 - all_h) > 0 else 'no'}",
        )

    def test_fixed_holidays(self):
        # Neujahr
        self.assertHoliday(f"{year}-01-01" for year in range(1991, 2050))
        # Maifeiertag
        self.assertHoliday(f"{year}-05-01" for year in range(1991, 2050))
        # Tag der Deutschen Einheit
        self.assertHoliday(f"{year}-10-03" for year in range(1991, 2050))
        # Erster Weihnachtstag
        self.assertHoliday(f"{year}-12-25" for year in range(1991, 2050))
        # Zweiter Weihnachtstag
        self.assertHoliday(f"{year}-12-26" for year in range(1991, 2050))

    def test_tag_der_deutschen_einheit_in_1990(self):
        self.assertHoliday("1990-10-03")

    def test_heilige_drei_koenige(self):
        provinces_that_have = {"BW", "BY", "BYP", "ST"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-01-06" for year in range(1991, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-01-06" for year in range(1991, 2050))
            )

    def test_karfreitag(self):
        known_good = (
            "2014-04-18",
            "2015-04-03",
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )

        for province in DeHolidays.subdivisions:
            self.assertHoliday(self.prov_hols[province], known_good)

    def test_ostersonntag(self):
        known_good = (
            "2014-04-20",
            "2015-04-05",
            "2016-03-27",
            "2017-04-16",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
        )
        provinces_that_have = {"BB"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_ostermontag(self):
        known_good = (
            "2014-04-21",
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )

        for province in DeHolidays.subdivisions:
            self.assertHoliday(self.prov_hols[province], known_good)

    def test_75_jahrestag_beendigung_zweiter_weltkrieg(self):
        provinces_that_have = {"BE"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], "2020-05-08")
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], "2020-05-08")

    def test_christi_himmelfahrt(self):
        known_good = (
            "2014-05-29",
            "2015-05-14",
            "2016-05-05",
            "2017-05-25",
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
        )

        for province in DeHolidays.subdivisions:
            self.assertHoliday(self.prov_hols[province], known_good)

    def test_weltkindertag(self):
        known_good = ("2019-09-20", "2021-09-20", "2022-09-20", "2023-09-20")
        provinces_that_have = {"TH"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_frauentag(self):
        self.assertHoliday(self.prov_hols["BE"], (f"{year}-03-08" for year in range(2019, 2050)))
        self.assertHoliday(self.prov_hols["MV"], (f"{year}-03-08" for year in range(2023, 2050)))

        for province in set(DeHolidays.subdivisions):
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-03-08" for year in range(1991, 2019))
            )
        self.assertNoHoliday(self.prov_hols["MV"], (f"{year}-03-08" for year in range(2019, 2023)))
        for province in set(DeHolidays.subdivisions) - {"BE", "MV"}:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-03-08" for year in range(2023, 2050))
            )

    def test_pfingstsonntag(self):
        known_good = (
            "2014-06-08",
            "2015-05-24",
            "2016-05-15",
            "2017-06-04",
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
        )
        provinces_that_have = {"BB"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_pfingstmontag(self):
        known_good = (
            "2014-06-09",
            "2015-05-25",
            "2016-05-16",
            "2017-06-05",
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
        )

        for province in DeHolidays.subdivisions:
            self.assertHoliday(self.prov_hols[province], known_good)

    def test_fronleichnam(self):
        known_good = (
            "2014-06-19",
            "2015-06-04",
            "2016-05-26",
            "2017-06-15",
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
        )
        provinces_that_have = {"BW", "BY", "BYP", "HE", "NW", "RP", "SL"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_mariae_himmelfahrt(self):
        provinces_that_have = {"BY", "SL"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-08-15" for year in range(1991, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-08-15" for year in range(1991, 2050))
            )

    def test_reformationstag(self):
        prov_yes = {"BB", "MV", "SN", "ST", "TH"}
        prov_yes_since_2018 = {"HB", "HH", "NI", "SH"}
        prov_not = set(DeHolidays.subdivisions) - prov_yes
        prov_not_since_2018 = prov_not - prov_yes_since_2018

        for province in prov_yes:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-10-31" for year in range(1991, 2050))
            )
        for province in prov_yes_since_2018:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-10-31" for year in range(2018, 2050))
            )
        for province in DeHolidays.subdivisions:
            self.assertHoliday(self.prov_hols[province], "2017-10-31")

        for province in prov_not:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-10-31" for year in range(1991, 2017))
            )
        for province in prov_not_since_2018:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-10-31" for year in range(2018, 2050))
            )

    def test_allerheiligen(self):
        provinces_that_have = {"BW", "BY", "BYP", "NW", "RP", "SL"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-11-01" for year in range(1991, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-11-01" for year in range(1991, 2050))
            )

    def test_buss_und_bettag(self):
        known_good = (
            "2014-11-19",
            "2015-11-18",
            "2016-11-16",
            "2017-11-22",
            "2018-11-21",
            "2019-11-20",
            "2020-11-18",
            "2021-11-17",
            "2022-11-16",
            "2023-11-22",
            "2024-11-20",
        )
        provinces_that_have = {"SN"}
        provinces_that_dont = set(DeHolidays.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)
