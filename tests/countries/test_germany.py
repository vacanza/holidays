#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import warnings
from unittest import TestCase

from holidays.constants import CATHOLIC
from holidays.countries.germany import Germany, DE, DEU
from tests.common import CommonCountryTests


class TestGermany(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1990, 2050)
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

    def test_no_catholic_holidays_before_1991(self):
        for subdiv in ("BY", "SN", "TH"):
            self.assertNoHolidays(DE(subdiv=subdiv, years=1990, categories=CATHOLIC))

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
            f"missing: {all_h - y_1990 or 'no'}, extra: {y_1990 - all_h or 'no'}",
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
            f"missing: {all_h - y_2015 or 'no'}, extra: {y_2015 - all_h or 'no'}",
        )

    def test_fixed_holidays(self):
        self.assertHolidayName("Neujahr", (f"{year}-01-01" for year in range(1991, 2050)))
        self.assertHolidayName("Erster Mai", (f"{year}-05-01" for year in range(1991, 2050)))
        self.assertHolidayName(
            "Tag der Deutschen Einheit", (f"{year}-10-03" for year in range(1990, 2050))
        )
        self.assertHolidayName(
            "Erster Weihnachtstag", (f"{year}-12-25" for year in range(1990, 2050))
        )
        self.assertHolidayName(
            "Zweiter Weihnachtstag", (f"{year}-12-26" for year in range(1990, 2050))
        )

    def test_heilige_drei_koenige(self):
        name = "Heilige Drei Könige"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"BW", "BY", "ST"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-06" for year in range(1991, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-01-06" for year in range(1991, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_karfreitag(self):
        name = "Karfreitag"
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
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, known_good)
            self.assertHolidayName(name, holidays, range(1991, 2050))
        self.assertHolidayName(name, known_good)
        self.assertHolidayName(name, range(1991, 2050))

    def test_ostersonntag(self):
        name = "Ostersonntag"
        self.assertNoHolidayName(name)
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
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BB":
                self.assertHolidayName(name, holidays, known_good)
                self.assertHolidayName(name, holidays, range(1991, 2050))
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_ostermontag(self):
        name = "Ostermontag"
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
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, known_good)
            self.assertHolidayName(name, holidays, range(1991, 2050))
        self.assertHolidayName(name, known_good)
        self.assertHolidayName(name, range(1991, 2050))

    def test_75_jahrestag_beendigung_zweiter_weltkrieg(self):
        dt = "2020-05-08"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BE":
                self.assertHoliday(holidays, dt)
            else:
                self.assertNoHoliday(holidays, dt)

    def test_80_jahrestag_beendigung_zweiter_weltkrieg(self):
        dt = "2025-05-08"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BE":
                self.assertHoliday(holidays, dt)
            else:
                self.assertNoHoliday(holidays, dt)

    def test_75_jahrestag_des_aufstandes_vom_17_juni_1953(self):
        dt = "2028-06-17"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BE":
                self.assertHoliday(holidays, dt)
            else:
                self.assertNoHoliday(holidays, dt)

    def test_christi_himmelfahrt(self):
        name = "Christi Himmelfahrt"
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
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, known_good)
            self.assertHolidayName(name, holidays, range(1991, 2050))
        self.assertHolidayName(name, known_good)
        self.assertHolidayName(name, range(1991, 2050))

    def test_weltkindertag(self):
        name = "Weltkindertag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-20" for year in range(2019, 2050))
                )
                self.assertNoHoliday(holidays, (f"{year}-09-20" for year in range(1991, 2019)))
                self.assertNoHolidayName(name, range(1991, 2019))
            else:
                self.assertNoHoliday(holidays, (f"{year}-09-20" for year in range(1991, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_frauentag(self):
        name = "Internationaler Frauentag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-08" for year in range(2019, 2050))
                )
                self.assertNoHoliday(holidays, (f"{year}-03-08" for year in range(1991, 2019)))
                self.assertNoHolidayName(name, range(1991, 2019))
            elif subdiv == "MV":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-08" for year in range(2023, 2050))
                )
                self.assertNoHoliday(holidays, (f"{year}-03-08" for year in range(1991, 2023)))
                self.assertNoHolidayName(name, range(1991, 2023))
            else:
                self.assertNoHoliday(holidays, (f"{year}-03-08" for year in range(1991, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_pfingstsonntag(self):
        name = "Pfingstsonntag"
        self.assertNoHolidayName(name)
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
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BB":
                self.assertHolidayName(name, holidays, known_good)
                self.assertHolidayName(name, holidays, range(1991, 2050))
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_pfingstmontag(self):
        name = "Pfingstmontag"
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
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, known_good)
            self.assertHolidayName(name, holidays, range(1991, 2050))
        self.assertHolidayName(name, known_good)
        self.assertHolidayName(name, range(1991, 2050))

    def test_fronleichnam(self):
        name = "Fronleichnam"
        self.assertNoHolidayName(name)
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
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"BW", "BY", "HE", "NW", "RP", "SL"}:
                self.assertHolidayName(name, holidays, known_good)
                self.assertHolidayName(name, holidays, range(1991, 2050))
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)
        for subdiv in ("SN", "TH"):
            catholic_holidays = DE(subdiv=subdiv, categories=CATHOLIC, years=range(1991, 2050))
            self.assertHolidayName(name, catholic_holidays, known_good)
            self.assertHolidayName(name, catholic_holidays, range(1991, 2050))

    def test_mariae_himmelfahrt(self):
        name = "Mariä Himmelfahrt"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in range(1991, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-08-15" for year in range(1991, 2050)))
                self.assertNoHolidayName(name, holidays)

        self.assertHolidayName(
            name,
            DE(subdiv="BY", categories=CATHOLIC, years=range(1991, 2050)),
            (f"{year}-08-15" for year in range(1991, 2050)),
        )

    def test_reformationstag(self):
        name = "Reformationstag"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"BB", "MV", "SN", "ST", "TH"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-31" for year in range(1991, 2050))
                )
            elif subdiv in {"HB", "HH", "NI", "SH"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-31" for year in range(2018, 2050))
                )
                self.assertNoHoliday(holidays, (f"{year}-10-31" for year in range(1991, 2017)))
                self.assertNoHolidayName(name, range(1991, 2017))
            else:
                self.assertNoHoliday(
                    holidays,
                    (f"{year}-10-31" for year in (*range(1991, 2017), *range(2018, 2050))),
                )
                self.assertNoHolidayName(name, range(1991, 2017), range(2018, 2050))
        self.assertHolidayName(name, "2017-10-31")

    def test_allerheiligen(self):
        name = "Allerheiligen"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"BW", "BY", "NW", "RP", "SL"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in range(1991, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-11-01" for year in range(1991, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_buss_und_bettag(self):
        name = "Buß- und Bettag"
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
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SN":
                self.assertHolidayName(name, holidays, known_good)
                self.assertHolidayName(name, holidays, range(1991, 2050))
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays, range(1995, 2050))
        self.assertHolidayName(
            name,
            "1990-11-21",
            "1991-11-20",
            "1992-11-18",
            "1993-11-17",
            "1994-11-16",
        )
        self.assertNoHolidayName(name, range(1995, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-03-08", "Internationaler Frauentag"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-17", "Ostersonntag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Erster Mai"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-05", "Pfingstsonntag"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-16", "Fronleichnam"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-09-20", "Weltkindertag"),
            ("2022-10-03", "Tag der Deutschen Einheit"),
            ("2022-10-31", "Reformationstag"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-16", "Buß- und Bettag"),
            ("2022-12-25", "Erster Weihnachtstag"),
            ("2022-12-26", "Zweiter Weihnachtstag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-20", "World Children's Day"),
            ("2022-10-03", "German Unity Day"),
            ("2022-10-31", "Reformation Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-16", "Repentance and Prayer Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-06-16", "วันสมโภชพระคริสตวรกาย"),
            ("2022-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2022-09-20", "วันเด็กสากล"),
            ("2022-10-03", "วันรวมชาติเยอรมัน"),
            ("2022-10-31", "วันแห่งการปฏิรูป"),
            ("2022-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-16", "วันแห่งการอธิษฐานและการกลับใจ"),
            ("2022-12-25", "วันคริสต์มาสวันแรก"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-03-08", "Міжнародний жіночий день"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-09-20", "Всесвітній день дітей"),
            ("2022-10-03", "День німецької єдності"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-16", "День молитви та покаяння"),
            ("2022-12-25", "Перший день Різдва"),
            ("2022-12-26", "Другий день Різдва"),
        )
