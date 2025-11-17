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

import warnings
from unittest import TestCase

from holidays.countries.france import France
from tests.common import CommonCountryTests


class TestFrance(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(France)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_2017(self):
        self.assertHolidays(
            France(years=2017),
            ("2017-01-01", "Jour de l'an"),
            ("2017-04-17", "Lundi de Pâques"),
            ("2017-05-01", "Fête du Travail"),
            ("2017-05-08", "Fête de la Victoire"),
            ("2017-05-25", "Ascension"),
            ("2017-06-05", "Lundi de Pentecôte"),
            ("2017-07-14", "Fête nationale"),
            ("2017-08-15", "Assomption"),
            ("2017-11-01", "Toussaint"),
            ("2017-11-11", "Armistice"),
            ("2017-12-25", "Noël"),
        )

    def test_2024(self):
        self.assertHolidays(
            France(years=2024),
            ("2024-01-01", "Jour de l'an"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-08", "Fête de la Victoire"),
            ("2024-05-09", "Ascension"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-07-14", "Fête nationale"),
            ("2024-08-15", "Assomption"),
            ("2024-11-01", "Toussaint"),
            ("2024-11-11", "Armistice"),
            ("2024-12-25", "Noël"),
        )

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_deprecated(self):
        self.assertEqual(
            sorted(France(subdiv="Alsace-Moselle", years=2023).keys()),
            sorted(France(subdiv="6AE", years=2023).keys()),
        )
        self.assertEqual(
            sorted(France(subdiv="Saint-Barthélémy", years=2023).keys()),
            sorted(France(subdiv="BL", years=2023).keys()),
        )

    def test_new_years_day(self):
        name = "Jour de l'an"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1811, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1811))

    def test_easter_monday(self):
        name = "Lundi de Pâques"
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1886, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1886))

    def test_whit_monday(self):
        name = "Lundi de Pentecôte"
        self.assertHolidayName(
            name,
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, range(1886, 2005), range(2008, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1886), range(2005, 2008))

    def test_labor_day(self):
        name_1919 = "1er mai"
        name_1941 = "Fête du Travail et de la Concorde sociale"
        name_1948 = "Fête du Travail"
        self.assertHolidayName(
            name_1919, (f"{year}-05-01" for year in (*range(1919, 1941), *range(1946, 1948)))
        )
        self.assertHolidayName(name_1941, (f"{year}-05-01" for year in range(1941, 1946)))
        self.assertHolidayName(name_1948, (f"{year}-05-01" for year in range(1948, self.end_year)))
        self.assertNoHolidayName(
            name_1919, range(self.start_year, 1919), range(1941, 1946), range(1948, self.end_year)
        )
        self.assertNoHolidayName(
            name_1941, range(self.start_year, 1941), range(1946, self.end_year)
        )
        self.assertNoHolidayName(name_1948, range(self.start_year, 1948))

    def test_victory_day(self):
        name = "Fête de la Victoire"
        self.assertHolidayName(
            name, (f"{year}-05-08" for year in (*range(1953, 1960), *range(1982, self.end_year)))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1953), range(1960, 1982))

    def test_national_day(self):
        name = "Fête nationale"
        self.assertHolidayName(name, (f"{year}-07-14" for year in range(1880, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1880))

    def test_ascension_day(self):
        name = "Ascension"
        self.assertHolidayName(
            name,
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_assumption_day(self):
        self.assertHolidayName("Assomption", (f"{year}-08-15" for year in self.full_range))

    def test_all_saints_day(self):
        self.assertHolidayName("Toussaint", (f"{year}-11-01" for year in self.full_range))

    def test_armistice_day(self):
        name = "Armistice"
        self.assertHolidayName(name, (f"{year}-11-11" for year in range(1922, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1922))

    def test_christmas_day(self):
        self.assertHolidayName("Noël", (f"{year}-12-25" for year in self.full_range))

    def test_good_friday(self):
        name = "Vendredi saint"
        dt = (
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Alsace, Moselle - 1893.
            if subdiv in {"57", "6AE"}:
                self.assertHolidayName(name, holidays, dt)
                self.assertHolidayName(name, holidays, range(1893, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1893))
            # Guadeloupe, Martinique, French Polynesia - Unknown, but exists.
            elif subdiv in {"971", "972", "PF"}:
                self.assertHolidayName(name, holidays, dt)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_stephens_day(self):
        name = "Saint Étienne"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Alsace, Moselle - 1892.
            if subdiv in {"57", "6AE"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-26" for year in range(1892, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1892))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_mi_careme(self):
        name = "Mi-Carême"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            dt = (
                "2019-03-28",
                "2020-03-19",
                "2021-03-11",
                "2022-03-24",
                "2023-03-16",
                "2024-03-07",
                "2025-03-27",
            )
            # Guadeloupe - Unknown, but exists.
            if subdiv == "971":
                self.assertHolidayName(name, holidays, dt)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_abolition_of_slavery(self):
        name = "Abolition de l'esclavage"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Guadeloupe - 1984.
            if subdiv == "971":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-27" for year in range(1984, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1984))
            # Martinique - 1984.
            elif subdiv == "972":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-22" for year in range(1984, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1984))
            # Guyane - 1984.
            elif subdiv == "973":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-10" for year in range(1984, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1984))
            # Reunion - 1983.
            elif subdiv == "974":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-20" for year in range(1983, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1983))
            # Mayotte - 1984.
            elif subdiv == "976":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-27" for year in range(1984, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1984))
            # Saint Barthelemy - 2012.
            elif subdiv == "BL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-09" for year in range(2012, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2012))
            # Saint Martin - 2012.
            elif subdiv == "MF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-28" for year in range(2012, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2012))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_victor_schoelcher_day(self):
        name = "Fête de Victor Schoelcher"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Guadeloupe, Martinique - 1984.
            if subdiv in {"971", "972"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-21" for year in range(1984, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1984))
            # Saint Martin - 2012.
            elif subdiv == "MF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-21" for year in range(2012, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2012))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_citizenship_day(self):
        name_1953 = "Fête de la prise de possession"
        name_2004 = "Fête de la Citoyenneté"
        self.assertNoHolidayName(name_1953)
        self.assertNoHolidayName(name_2004)
        for subdiv, holidays in self.subdiv_holidays.items():
            # New Caledonia - 1953.
            if subdiv == "NC":
                self.assertHolidayName(
                    name_1953, holidays, (f"{year}-09-24" for year in range(1953, 2004))
                )
                self.assertHolidayName(
                    name_2004, holidays, (f"{year}-09-24" for year in range(2004, self.end_year))
                )
                self.assertNoHolidayName(
                    name_1953, holidays, range(self.start_year, 1953), range(2004, self.end_year)
                )
                self.assertNoHolidayName(name_2004, holidays, range(self.start_year, 2004))
            else:
                self.assertNoHolidayName(name_1953, holidays)
                self.assertNoHolidayName(name_2004, holidays)

    def test_missionary_day(self):
        name = "Arrivée de l'Évangile"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # French Polynesia - 1978.
            if subdiv == "PF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-05" for year in range(1978, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1978))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_internal_autonomy_day(self):
        name = "Fête de l'autonomie"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # French Polynesia - 1985-2024.
            if subdiv == "PF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-29" for year in range(1985, 2025))
                )
                self.assertNoHolidayName(
                    name, holidays, range(self.start_year, 1985), range(2025, self.end_year)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_matarii(self):
        name = "Matāri'i"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # French Polynesia - 2025.
            if subdiv == "PF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-20" for year in range(2025, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2025))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_feast_of_saint_peter_chanel(self):
        name = "Saint Pierre Chanel"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Wallis and Futuna - 1962.
            if subdiv == "WF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-28" for year in range(1962, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1962))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saints_peter_and_paul_day(self):
        name = "Saints Pierre et Paul"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Wallis and Futuna - 1962.
            if subdiv == "WF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-29" for year in range(1962, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1962))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_territory_day(self):
        name = "Fête du Territoire"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Wallis and Futuna - 1962.
            if subdiv == "WF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-29" for year in range(1962, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1962))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jour de l'an"),
            ("2022-03-05", "Arrivée de l'Évangile"),
            ("2022-03-24", "Mi-Carême"),
            ("2022-04-15", "Vendredi saint"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-04-27", "Abolition de l'esclavage"),
            ("2022-04-28", "Saint Pierre Chanel"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-08", "Fête de la Victoire"),
            ("2022-05-22", "Abolition de l'esclavage"),
            ("2022-05-26", "Ascension"),
            ("2022-05-27", "Abolition de l'esclavage"),
            ("2022-05-28", "Abolition de l'esclavage"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-06-10", "Abolition de l'esclavage"),
            ("2022-06-29", "Fête de l'autonomie; Saints Pierre et Paul"),
            ("2022-07-14", "Fête nationale"),
            ("2022-07-21", "Fête de Victor Schoelcher"),
            ("2022-07-29", "Fête du Territoire"),
            ("2022-08-15", "Assomption"),
            ("2022-09-24", "Fête de la Citoyenneté"),
            ("2022-10-09", "Abolition de l'esclavage"),
            ("2022-11-01", "Toussaint"),
            ("2022-11-11", "Armistice"),
            ("2022-12-20", "Abolition de l'esclavage"),
            ("2022-12-25", "Noël"),
            ("2022-12-26", "Saint Étienne"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-03-05", "Missionary Day"),
            ("2022-03-24", "Mi-Careme"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "Abolition of Slavery"),
            ("2022-04-28", "Feast of Saint Peter Chanel"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "Victory Day"),
            ("2022-05-22", "Abolition of Slavery"),
            ("2022-05-26", "Ascension Day"),
            ("2022-05-27", "Abolition of Slavery"),
            ("2022-05-28", "Abolition of Slavery"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-10", "Abolition of Slavery"),
            ("2022-06-29", "Internal Autonomy Day; Saints Peter and Paul Day"),
            ("2022-07-14", "National Day"),
            ("2022-07-21", "Victor Schoelcher Day"),
            ("2022-07-29", "Territory Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-24", "Citizenship Day"),
            ("2022-10-09", "Abolition of Slavery"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-11", "Armistice Day"),
            ("2022-12-20", "Abolition of Slavery"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-03-05", "วันคริสตธรรมมาถึง"),
            ("2022-03-24", "วันเฉลิมฉลองกลางเทศกาลมหาพรต"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-04-27", "วันเลิกทาส"),
            ("2022-04-28", "วันสมโภชนักบุญเปโตร ชาเนล"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-08", "วันแห่งชัยชนะ"),
            ("2022-05-22", "วันเลิกทาส"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-05-27", "วันเลิกทาส"),
            ("2022-05-28", "วันเลิกทาส"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-06-10", "วันเลิกทาส"),
            ("2022-06-29", "วันปกครองตนเอง; วันสมโภชนักบุญเปโตรและเปาโล"),
            ("2022-07-14", "วันชาติฝรั่งเศส"),
            ("2022-07-21", "วันวิกตอร์ เชลแชร์"),
            ("2022-07-29", "วันก่อตั้งดินแดน"),
            ("2022-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2022-09-24", "วันแห่งความเป็นพลเมือง"),
            ("2022-10-09", "วันเลิกทาส"),
            ("2022-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-11", "วันสงบศึก"),
            ("2022-12-20", "วันเลิกทาส"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "วันสมโภชนักบุญสเตเฟน"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-03-05", "День місіонерів"),
            ("2022-03-24", "Свято Мі-Карем"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-27", "День скасування рабства"),
            ("2022-04-28", "День Святого Пʼєра Шанеля"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День Перемоги"),
            ("2022-05-22", "День скасування рабства"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-05-27", "День скасування рабства"),
            ("2022-05-28", "День скасування рабства"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-10", "День скасування рабства"),
            ("2022-06-29", "День Святих Петра і Павла; День автономії"),
            ("2022-07-14", "Національне свято"),
            ("2022-07-21", "День Віктора Шольшера"),
            ("2022-07-29", "День Території"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-09-24", "День громадянства"),
            ("2022-10-09", "День скасування рабства"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День перемирʼя"),
            ("2022-12-20", "День скасування рабства"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День Святого Стефана"),
        )
