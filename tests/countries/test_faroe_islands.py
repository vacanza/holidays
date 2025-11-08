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

from holidays.countries.faroe_islands import FaroeIslands
from tests.common import CommonCountryTests


class TestFaroeIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(FaroeIslands)

    def test_new_years_day(self):
        self.assertHolidayName("Nýggjársdagur", (f"{year}-01-01" for year in self.full_range))

    def test_maundy_thursday(self):
        name = "Skírhósdagur"
        self.assertHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Langifríggjadagur"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Páskadagur"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Annar páskadagur"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_great_prayer_day(self):
        name = "Dýri biðidagur"
        self.assertHolidayName(
            name,
            "2020-05-08",
            "2021-04-30",
            "2022-05-13",
            "2023-05-05",
            "2024-04-26",
            "2025-05-16",
        )
        self.assertHolidayName(name, self.full_range)

    def test_ascension_day(self):
        name = "Kristi himmalsferðardagur"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_sunday(self):
        name = "Hvítusunnudagur"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Annar hvítusunnudagur"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_saint_olafs_day(self):
        self.assertHolidayName("Ólavsøkudagur", (f"{year}-07-29" for year in self.full_range))

    def test_christmas_eve(self):
        self.assertHolidayName("Jólaaftan", (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Jóladagur", (f"{year}-12-25" for year in self.full_range))

    def test_christmas_second_day(self):
        self.assertHolidayName("Annar jóladagur", (f"{year}-12-26" for year in self.full_range))

    def test_new_years_eve(self):
        self.assertHolidayName("Nýggjársaftan", (f"{year}-12-31" for year in self.full_range))

    def test_national_flag_day(self):
        name = "Flaggdagur"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, (f"{year}-04-25" for year in self.full_range))

    def test_constitution_day(self):
        name = "Grundlógardagur"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, (f"{year}-06-05" for year in self.full_range))

    def test_saint_olafs_eve(self):
        name = "Ólavsøkuaftan"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, (f"{year}-07-28" for year in self.full_range))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Nýggjársdagur"),
            ("2025-04-17", "Skírhósdagur"),
            ("2025-04-18", "Langifríggjadagur"),
            ("2025-04-20", "Páskadagur"),
            ("2025-04-21", "Annar páskadagur"),
            ("2025-04-25", "Flaggdagur"),
            ("2025-05-16", "Dýri biðidagur"),
            ("2025-05-29", "Kristi himmalsferðardagur"),
            ("2025-06-05", "Grundlógardagur"),
            ("2025-06-08", "Hvítusunnudagur"),
            ("2025-06-09", "Annar hvítusunnudagur"),
            ("2025-07-28", "Ólavsøkuaftan"),
            ("2025-07-29", "Ólavsøkudagur"),
            ("2025-12-24", "Jólaaftan"),
            ("2025-12-25", "Jóladagur"),
            ("2025-12-26", "Annar jóladagur"),
            ("2025-12-31", "Nýggjársaftan"),
        )

    def test_l10n_da(self):
        self.assertLocalizedHolidays(
            "da",
            ("2025-01-01", "Nytårsdag"),
            ("2025-04-17", "Skærtorsdag"),
            ("2025-04-18", "Langfredag"),
            ("2025-04-20", "Påskedag"),
            ("2025-04-21", "Anden påskedag"),
            ("2025-04-25", "Flagdag"),
            ("2025-05-16", "Store bededag"),
            ("2025-05-29", "Kristi himmelfartsdag"),
            ("2025-06-05", "Grundlovsdag"),
            ("2025-06-08", "Pinsedag"),
            ("2025-06-09", "Anden pinsedag"),
            ("2025-07-28", "Olavsaften"),
            ("2025-07-29", "Olavsdag"),
            ("2025-12-24", "Juleaftensdag"),
            ("2025-12-25", "Juledag"),
            ("2025-12-26", "Anden juledag"),
            ("2025-12-31", "Nytårsaften"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-25", "National Flag Day"),
            ("2025-05-16", "Great Prayer Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-05", "Constitution Day"),
            ("2025-06-08", "Whit Sunday"),
            ("2025-06-09", "Whit Monday"),
            ("2025-07-28", "Saint Olaf's Eve"),
            ("2025-07-29", "Saint Olaf's Day"),
            ("2025-12-24", "Christmas Eve"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Second Day of Christmas"),
            ("2025-12-31", "New Year's Eve"),
        )

    def test_l10n_is(self):
        self.assertLocalizedHolidays(
            "is",
            ("2025-01-01", "Nýársdagur"),
            ("2025-04-17", "Skírdagur"),
            ("2025-04-18", "Föstudagurinn langi"),
            ("2025-04-20", "Páskadagur"),
            ("2025-04-21", "Annar í páskum"),
            ("2025-04-25", "Fánadagur"),
            ("2025-05-16", "Kóngsbænadagur"),
            ("2025-05-29", "Uppstigningardagur"),
            ("2025-06-05", "Stjórnarskrárdagur"),
            ("2025-06-08", "Hvítasunnudagur"),
            ("2025-06-09", "Annar í hvítasunnu"),
            ("2025-07-28", "Ólafsnótt"),
            ("2025-07-29", "Ólafsdagur"),
            ("2025-12-24", "Aðfangadagur"),
            ("2025-12-25", "Jóladagur"),
            ("2025-12-26", "Annar í jólum"),
            ("2025-12-31", "Gamlársdagur"),
        )

    def test_l10n_no(self):
        self.assertLocalizedHolidays(
            "no",
            ("2025-01-01", "Nyttårsdag"),
            ("2025-04-17", "Skjærtorsdag"),
            ("2025-04-18", "Langfredag"),
            ("2025-04-20", "Første påskedag"),
            ("2025-04-21", "Andre påskedag"),
            ("2025-04-25", "Flaggdag"),
            ("2025-05-16", "Store bededag"),
            ("2025-05-29", "Kristi himmelfartsdag"),
            ("2025-06-05", "Grunnlovsdag"),
            ("2025-06-08", "Første pinsedag"),
            ("2025-06-09", "Andre pinsedag"),
            ("2025-07-28", "Olavsaften"),
            ("2025-07-29", "Olavsdag"),
            ("2025-12-24", "Julaften"),
            ("2025-12-25", "Første juledag"),
            ("2025-12-26", "Andre juledag"),
            ("2025-12-31", "Nyttårsaften"),
        )

    def test_l10n_sv(self):
        self.assertLocalizedHolidays(
            "sv",
            ("2025-01-01", "Nyårsdagen"),
            ("2025-04-17", "Skärtorsdagen"),
            ("2025-04-18", "Långfredagen"),
            ("2025-04-20", "Påskdagen"),
            ("2025-04-21", "Annandag påsk"),
            ("2025-04-25", "Flaggdagen"),
            ("2025-05-16", "Stora bönedagen"),
            ("2025-05-29", "Kristi himmelsfärdsdag"),
            ("2025-06-05", "Grundlagsdag"),
            ("2025-06-08", "Pingstdagen"),
            ("2025-06-09", "Annandag pingst"),
            ("2025-07-28", "Olafsafton"),
            ("2025-07-29", "Olafsdagen"),
            ("2025-12-24", "Julafton"),
            ("2025-12-25", "Juldagen"),
            ("2025-12-26", "Annandag jul"),
            ("2025-12-31", "Nyårsafton"),
        )
