#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.bhutan import Bhutan
from tests.common import CommonCountryTests


class TestBhutan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bhutan)

    def test_birthday_anniversary_of_his_majesty_the_king(self):
        name = "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"
        self.assertHolidayName(
            name,
            (f"{year}-02-21" for year in self.full_range),
            (f"{year}-02-22" for year in self.full_range),
            (f"{year}-02-23" for year in self.full_range),
        )

    def test_birth_anniversary_third_druk_gyalpo(self):
        self.assertHolidayName(
            "མི་དབང་འབྲུག་རྒྱལ་གསུམ་པའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།",
            (f"{year}-05-02" for year in self.full_range),
        )

    def test_coronation_his_majesty(self):
        self.assertHolidayName(
            "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་གསེར་ཁྲི་མངའ་གསོལ་གྱི་དུས་ཆེན་ངལ་གསོལ།",
            (f"{year}-11-01" for year in self.full_range),
        )

    def test_birth_anniversary_fourth_druk_gyalpo(self):
        self.assertHolidayName(
            "མི་དབང་འབྲུག་རྒྱལ་བཞི་པའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།",
            (f"{year}-11-11" for year in self.full_range),
        )

    def test_national_day(self):
        self.assertHolidayName(
            "རྒྱལ་ཡོངས་དུས་ཆེན་གྱི་ངལ་གསོལ།", (f"{year}-12-17" for year in self.full_range)
        )

    def test_winter_solstice(self):
        name = "དགུན་ཉི་ལྡོག་གི་ངལ་གསོལ།"
        self.assertHolidayName(
            name,
            (
                f"{year}-01-02"
                for year in (
                    *range(self.start_year, 2019),
                    *range(2020, 2022),
                    *range(2023, self.end_year),
                )
            ),
            "2019-01-03",
            "2022-01-01",
        )

    def test_day_of_offering(self):
        name = "སྔར་སྲོལ་འབུལ་བའི་ལོ་གསར་གྱི་ངལ་གསོལ།"
        self.assertHolidayName(
            name,
            "2020-01-25",
            "2021-01-14",
            "2022-01-03",
            "2023-01-22",
            "2024-01-12",
            "2025-01-30",
        )
        self.assertHolidayName(name, set(self.full_range) - {2031, 2040})

    def test_losar(self):
        name = "གནམ་ལོ་གསར་ཚེས་ཀྱིས་དུས་སྟོན་ངལ་གསོལ།"
        self.assertHolidayName(
            name,
            "2020-02-24",
            "2021-02-12",
            "2022-03-03",
            "2023-02-21",
            "2024-02-11",
            "2025-02-28",
        )
        self.assertHolidayName(name, self.full_range)

    def test_death_of_zhabdrung(self):
        name = "མཐུ་ཆེན་ཆོས་ཀྱི་རྒྱལ་པོའི་དུས་ཆེན་ངལ་གསོལ།"
        self.assertHolidayName(
            name,
            "2021-04-22",
            "2022-05-11",
            "2023-04-30",
            "2024-04-18",
            "2025-05-07",
        )
        self.assertHolidayName(name, set(self.full_range) - {2010, 2011, 2020})

    def test_lord_buddha_parinirvana(self):
        name = "སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་དུས་ཆེན་ལྔ་འཛོམས་ངལ་གསོལ།"
        self.assertHolidayName(
            name,
            "2020-06-05",
            "2021-05-26",
            "2022-06-14",
            "2023-06-04",
            "2024-05-23",
            "2025-06-11",
        )
        self.assertHolidayName(name, self.full_range)

    def test_birth_anniversary_guru_rinpoche(self):
        name = "ཨོ་རྒྱན་གུ་རུ་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོ།"
        self.assertHolidayName(
            name,
            "2020-06-30",
            "2021-06-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-07-05",
        )
        self.assertHolidayName(name, range(self.start_year, 2027), range(2028, self.end_year))

    def test_first_sermon_lord_buddha(self):
        name = "སྟོན་པ་མཆོག་ཝ་ར་ན་སིར་བདེན་བཞིའི་ཆོས་འཁོར་བསྐོར་བའི་དུས་ཆེན་ངལ་གསོ།"
        self.assertHolidayName(
            name,
            "2020-07-24",
            "2021-07-14",
            "2022-08-01",
            "2023-07-21",
            "2024-07-10",
            "2025-07-28",
        )
        self.assertHolidayName(name, self.full_range)

    def test_blessed_rainy_day(self):
        name = "རྒྱལ་ཡོངས་ཁྲུས་བབས་ངལ་གསོ།"
        self.assertHolidayName(
            name,
            "2020-09-23",
            "2021-09-23",
            "2022-09-23",
            "2023-09-24",
            "2024-09-23",
            "2025-09-23",
        )
        self.assertHolidayName(name, self.full_range)

    def test_dassain(self):
        name = "ལྷོ་མཚམས་ད་སའིན་ངལ་གསོ།"
        self.assertHolidayName(
            name,
            "2020-10-26",
            "2021-10-15",
            "2022-10-05",
            "2023-10-24",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertHolidayName(name, (*range(self.start_year, 2012), *range(2014, 2025)))

    def test_descending_day_lord_buddha(self):
        name = "རྒྱལ་བ་ལྷ་ལས་བབས་པའི་དུས་ཆེན་ངལ་གསོ།"
        self.assertHolidayName(
            name,
            "2020-11-07",
            "2021-10-27",
            "2022-11-15",
            "2023-11-04",
            "2024-11-22",
            "2025-11-11",
        )
        self.assertHolidayName(name, self.full_range)

    def test_thimphu_drubchoe(self):
        name = "ཐིམ་རྫོང་ལྷ་མོའི་དངོས་འཆམ་མཇལ་རྒྱུའི་ངལ་གསོ།"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "15":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-09-23",
                    "2021-09-12",
                    "2022-10-01",
                    "2023-09-21",
                    "2024-09-10",
                    "2025-09-29",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_thimphu_tshechu(self):
        name = "ཐིམ་ཕུ་ཚེས་བཅུའི་ངལ་གསོ།"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "15":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-09-26",
                    "2020-09-27",
                    "2020-09-28",
                    "2021-09-15",
                    "2021-09-16",
                    "2021-09-17",
                    "2022-10-04",
                    "2022-10-05",
                    "2022-10-06",
                    "2023-09-24",
                    "2023-09-25",
                    "2023-09-26",
                    "2024-09-13",
                    "2024-09-14",
                    "2024-09-15",
                    "2025-10-02",
                    "2025-10-03",
                    "2025-10-04",
                )
                self.assertHolidayNameCount(name, 3, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-02", "དགུན་ཉི་ལྡོག་གི་ངལ་གསོལ།"),
            ("2025-01-30", "སྔར་སྲོལ་འབུལ་བའི་ལོ་གསར་གྱི་ངལ་གསོལ།"),
            ("2025-02-21", "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2025-02-22", "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2025-02-23", "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2025-02-28", "གནམ་ལོ་གསར་ཚེས་ཀྱིས་དུས་སྟོན་ངལ་གསོལ།"),
            ("2025-03-01", "གནམ་ལོ་གསར་ཚེས་ཀྱིས་དུས་སྟོན་ངལ་གསོལ།"),
            ("2025-05-02", "མི་དབང་འབྲུག་རྒྱལ་གསུམ་པའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2025-05-07", "མཐུ་ཆེན་ཆོས་ཀྱི་རྒྱལ་པོའི་དུས་ཆེན་ངལ་གསོལ།"),
            ("2025-06-11", "སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་དུས་ཆེན་ལྔ་འཛོམས་ངལ་གསོལ།"),
            ("2025-07-05", "ཨོ་རྒྱན་གུ་རུ་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོ།"),
            ("2025-07-28", "སྟོན་པ་མཆོག་ཝ་ར་ན་སིར་བདེན་བཞིའི་ཆོས་འཁོར་བསྐོར་བའི་དུས་ཆེན་ངལ་གསོ།"),
            ("2025-09-23", "རྒྱལ་ཡོངས་ཁྲུས་བབས་ངལ་གསོ།"),
            ("2025-10-02", "ལྷོ་མཚམས་ད་སའིན་ངལ་གསོ།"),
            ("2025-11-01", "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་གསེར་ཁྲི་མངའ་གསོལ་གྱི་དུས་ཆེན་ངལ་གསོལ།"),
            (
                "2025-11-11",
                "མི་དབང་འབྲུག་རྒྱལ་བཞི་པའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།; རྒྱལ་བ་ལྷ་ལས་བབས་པའི་དུས་ཆེན་ངལ་གསོ།",
            ),
            ("2025-12-17", "རྒྱལ་ཡོངས་དུས་ཆེན་གྱི་ངལ་གསོལ།"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-02", "དགུན་ཉི་ལྡོག་གི་ངལ་གསོལ།"),
            ("2024-01-12", "སྔར་སྲོལ་འབུལ་བའི་ལོ་གསར་གྱི་ངལ་གསོལ།"),
            ("2024-02-10", "གནམ་ལོ་གསར་ཚེས་ཀྱིས་དུས་སྟོན་ངལ་གསོལ།"),
            ("2024-02-11", "གནམ་ལོ་གསར་ཚེས་ཀྱིས་དུས་སྟོན་ངལ་གསོལ།"),
            ("2024-02-21", "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2024-02-22", "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2024-02-23", "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2024-04-18", "མཐུ་ཆེན་ཆོས་ཀྱི་རྒྱལ་པོའི་དུས་ཆེན་ངལ་གསོལ།"),
            ("2024-05-02", "མི་དབང་འབྲུག་རྒྱལ་གསུམ་པའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2024-05-23", "སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་དུས་ཆེན་ལྔ་འཛོམས་ངལ་གསོལ།"),
            ("2024-06-16", "ཨོ་རྒྱན་གུ་རུ་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོ།"),
            ("2024-07-10", "སྟོན་པ་མཆོག་ཝ་ར་ན་སིར་བདེན་བཞིའི་ཆོས་འཁོར་བསྐོར་བའི་དུས་ཆེན་ངལ་གསོ།"),
            ("2024-09-10", "ཐིམ་རྫོང་ལྷ་མོའི་དངོས་འཆམ་མཇལ་རྒྱུའི་ངལ་གསོ།"),
            ("2024-09-13", "ཐིམ་ཕུ་ཚེས་བཅུའི་ངལ་གསོ།"),
            ("2024-09-14", "ཐིམ་ཕུ་ཚེས་བཅུའི་ངལ་གསོ།"),
            ("2024-09-15", "ཐིམ་ཕུ་ཚེས་བཅུའི་ངལ་གསོ།"),
            ("2024-09-23", "རྒྱལ་ཡོངས་ཁྲུས་བབས་ངལ་གསོ།"),
            ("2024-10-12", "ལྷོ་མཚམས་ད་སའིན་ངལ་གསོ།"),
            ("2024-11-01", "མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་གསེར་ཁྲི་མངའ་གསོལ་གྱི་དུས་ཆེན་ངལ་གསོལ།"),
            ("2024-11-11", "མི་དབང་འབྲུག་རྒྱལ་བཞི་པའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"),
            ("2024-11-22", "རྒྱལ་བ་ལྷ་ལས་བབས་པའི་དུས་ཆེན་ངལ་གསོ།"),
            ("2024-12-17", "རྒྱལ་ཡོངས་དུས་ཆེན་གྱི་ངལ་གསོལ།"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-02", "Winter Solstice"),
            ("2024-01-12", "Traditional Day of Offering"),
            ("2024-02-10", "Losar"),
            ("2024-02-11", "Losar"),
            ("2024-02-21", "Birth Anniversary of His Majesty the King"),
            ("2024-02-22", "Birth Anniversary of His Majesty the King"),
            ("2024-02-23", "Birth Anniversary of His Majesty the King"),
            ("2024-04-18", "Death Anniversary of Zhabdrung"),
            ("2024-05-02", "Birth Anniversary of the 3rd Druk Gyalpo"),
            ("2024-05-23", "Lord Buddha's Parinirvana"),
            ("2024-06-16", "Birth Anniversary of Guru Rinpoche"),
            ("2024-07-10", "First Sermon of Lord Buddha"),
            ("2024-09-10", "Thimphu Drubchoe"),
            ("2024-09-13", "Thimphu Tshechu"),
            ("2024-09-14", "Thimphu Tshechu"),
            ("2024-09-15", "Thimphu Tshechu"),
            ("2024-09-23", "Blessed Rainy Day"),
            ("2024-10-12", "Dassain"),
            ("2024-11-01", "Coronation of His Majesty the King"),
            ("2024-11-11", "Birth Anniversary of the 4th Druk Gyalpo - Constitution Day"),
            ("2024-11-22", "Descending Day of Lord Buddha"),
            ("2024-12-17", "National Day"),
        )
