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

import warnings
from unittest import TestCase

from holidays.constants import CATHOLIC
from holidays.countries.germany import Germany, DE, DEU
from tests.common import CommonCountryTests


class TestDE(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1991, 2050)
        super().setUpClass(DE, years=years)
        cls.subdiv_holidays = {
            subdiv: DE(subdiv=subdiv, years=years) for subdiv in DE.subdivisions
        }

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_country_aliases(self):
        self.assertAliases(Germany, DE, DEU)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_deprecated(self):
        self.assertEqual(
            sorted(Germany(subdiv="BYP", years=2023).keys()),
            sorted(Germany(subdiv="BY", years=2023).keys()),
        )

    def test_no_public_holidays_before_1990(self):
        self.assertNoHolidays(DE(years=1989))
        for p in DE.subdivisions:
            self.assertNoHolidays(DE(years=1989, subdiv=p))

    def test_no_by_catholic_holidays_before_1991(self):
        self.assertNoHolidays(DE(subdiv="BY", years=1990, categories=(CATHOLIC)))

    def test_1990_present(self):
        y_1990 = set()
        for p in DE.subdivisions:
            y_1990.update(DE(years=1990, subdiv=p).values())
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
        for p in DE.subdivisions:
            y_2015.update(DE(years=2015, subdiv=p).values())
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
        subdivs_that_have = {"BW", "BY", "ST"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-01-06" for year in range(1991, 2050))
            )
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-01-06" for year in range(1991, 2050))
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

        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)

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
        subdivs_that_have = {"BB"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

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

        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_75_jahrestag_beendigung_zweiter_weltkrieg(self):
        subdivs_that_have = {"BE"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], "2020-05-08")
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], "2020-05-08")

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

        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_weltkindertag(self):
        known_good = ("2019-09-20", "2021-09-20", "2022-09-20", "2023-09-20")
        subdivs_that_have = {"TH"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_frauentag(self):
        self.assertHoliday(
            self.subdiv_holidays["BE"], (f"{year}-03-08" for year in range(2019, 2050))
        )
        self.assertHoliday(
            self.subdiv_holidays["MV"], (f"{year}-03-08" for year in range(2023, 2050))
        )

        for subdiv in set(DE.subdivisions):
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-03-08" for year in range(1991, 2019))
            )
        self.assertNoHoliday(
            self.subdiv_holidays["MV"], (f"{year}-03-08" for year in range(2019, 2023))
        )
        for subdiv in set(DE.subdivisions) - {"BE", "MV"}:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-03-08" for year in range(2023, 2050))
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
        subdivs_that_have = {"BB"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

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

        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)

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
        subdivs_that_have = {"BW", "BY", "HE", "NW", "RP", "SL"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_mariae_himmelfahrt(self):
        subdivs_that_have = {"SL"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-08-15" for year in range(1991, 2050))
            )
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-08-15" for year in range(1991, 2050))
            )
        # Bayern (Catholic municipalities).
        self.assertHoliday(
            DE(subdiv="BY", years=range(1991, 2050), categories=(CATHOLIC)),
            (f"{year}-08-15" for year in range(1991, 2050)),
        )

    def test_reformationstag(self):
        subdiv_yes = {"BB", "MV", "SN", "ST", "TH"}
        subdiv_yes_since_2018 = {"HB", "HH", "NI", "SH"}
        subdiv_not = set(DE.subdivisions) - subdiv_yes
        subdiv_not_since_2018 = subdiv_not - subdiv_yes_since_2018

        for subdiv in subdiv_yes:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-10-31" for year in range(1991, 2050))
            )
        for subdiv in subdiv_yes_since_2018:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-10-31" for year in range(2018, 2050))
            )
        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], "2017-10-31")

        for subdiv in subdiv_not:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-10-31" for year in range(1991, 2017))
            )
        for subdiv in subdiv_not_since_2018:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-10-31" for year in range(2018, 2050))
            )

    def test_allerheiligen(self):
        subdivs_that_have = {"BW", "BY", "NW", "RP", "SL"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-11-01" for year in range(1991, 2050))
            )
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-11-01" for year in range(1991, 2050))
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
        subdivs_that_have = {"SN"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neujahr"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Erster Mai"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-10-03", "Tag der Deutschen Einheit"),
            ("2022-12-25", "Erster Weihnachtstag"),
            ("2022-12-26", "Zweiter Weihnachtstag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-10-03", "German Unity Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-10-03", "วันรวมชาติเยอรมัน"),
            ("2022-12-25", "วันคริสต์มาสวันแรก"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-10-03", "День німецької єдності"),
            ("2022-12-25", "Перший день Різдва"),
            ("2022-12-26", "Другий день Різдва"),
        )
