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

from holidays.constants import GOVERNMENT
from holidays.countries.andorra import Andorra, AD, AND
from tests.common import CommonCountryTests


class TestAndorra(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(AD.start_year, 2050)
        super().setUpClass(Andorra, years=cls.full_range)
        cls.subdiv_holidays = {
            subdiv: Andorra(subdiv=subdiv, years=cls.full_range) for subdiv in Andorra.subdivisions
        }

    def test_country_aliases(self):
        self.assertAliases(Andorra, AD, AND)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Andorra(categories=Andorra.supported_categories, years=AD.start_year - 1)
        )

    def test_new_years_day(self):
        self.assertHolidayName("Cap d'Any", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany(self):
        self.assertHolidayName("Reis", (f"{year}-01-06" for year in self.full_range))

    def test_carnival(self):
        name = "Carnaval"
        self.assertHolidayName(
            name,
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_constitution_day(self):
        name = "Dia de la Constitució"
        self.assertHolidayName(name, (f"{year}-03-14" for year in range(1994, 2050)))
        self.assertNoHolidayName(name, range(AD.start_year, 1994))

    def test_good_friday(self):
        name = "Divendres Sant"
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

    def test_easter_monday(self):
        name = "Dilluns de Pasqua"
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

    def test_labor_day(self):
        self.assertHolidayName("Festa del treball", (f"{year}-05-01" for year in self.full_range))

    def test_whit_monday(self):
        name = "Dilluns de Pentecosta"
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

    def test_assumption_day(self):
        self.assertHolidayName("Assumpció", (f"{year}-08-15" for year in self.full_range))

    def test_our_lady_of_meritxell(self):
        self.assertHolidayName(
            "Nostra Senyora de Meritxell", (f"{year}-09-08" for year in self.full_range)
        )

    def test_all_saints_day(self):
        self.assertHolidayName("Tots Sants", (f"{year}-11-01" for year in self.full_range))

    def test_immaculate_conception(self):
        self.assertHolidayName(
            "Immaculada Concepció", (f"{year}-12-08" for year in self.full_range)
        )

    def test_christmas_day(self):
        self.assertHolidayName("Nadal", (f"{year}-12-25" for year in self.full_range))

    def test_saint_stephens_day(self):
        self.assertHolidayName("Sant Esteve", (f"{year}-12-26" for year in self.full_range))

    def test_saint_rochs_day(self):
        name = "Sant Roc"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "02":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_anthonys_day(self):
        name = "Sant Antoni"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "04":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-17" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_peters_day(self):
        name = "Sant Pere"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "05":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-29" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_julians_day(self):
        name = "Sant Julià"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "06":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-07" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_virgin_mary_of_canolich(self):
        name = "Diada de Canòlich"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "06":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-05-30",
                    "2021-05-29",
                    "2022-05-28",
                    "2023-05-27",
                    "2024-05-25",
                    "2025-05-31",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sant_julia_de_loria_festival(self):
        name = "Festa Major de Sant Julià de Lòria"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "06":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-07-27",
                    "2020-07-28",
                    "2021-08-02",
                    "2021-08-03",
                    "2022-08-01",
                    "2022-08-02",
                    "2023-07-31",
                    "2023-08-01",
                    "2024-07-29",
                    "2024-07-30",
                    "2025-07-28",
                    "2025-07-29",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_andorra_la_vella_festival(self):
        name = "Festa Major d'Andorra la Vella"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "07":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-08-01",
                    "2020-08-02",
                    "2020-08-03",
                    "2021-08-07",
                    "2021-08-08",
                    "2021-08-09",
                    "2022-08-06",
                    "2022-08-07",
                    "2022-08-08",
                    "2023-08-05",
                    "2023-08-06",
                    "2023-08-07",
                    "2024-08-03",
                    "2024-08-04",
                    "2024-08-05",
                    "2025-08-02",
                    "2025-08-03",
                    "2025-08-04",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_michael_of_engolasters_day(self):
        name = "Sant Miquel d'Engolasters"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "08":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-07" for year in range(1979, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AD.start_year, 1979))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_parish_foundation_day(self):
        name = "Diada de la creació de la parròquia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "08":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-14" for year in range(1979, 1997))
                )
                self.assertHolidayName(
                    name,
                    holidays,
                    "1997-06-15",
                    "1998-06-14",
                    "1999-06-20",
                    "2000-06-18",
                    "2020-06-14",
                    "2021-06-20",
                    "2022-06-19",
                    "2023-06-18",
                    "2024-06-16",
                    "2025-06-15",
                )
                self.assertHolidayName(name, holidays, range(1979, 2050))
                self.assertNoHolidayName(name, holidays, range(AD.start_year, 1979))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_escaldes_engordany_festival(self):
        name = "Festa Major d'Escaldes-Engordany"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "08":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-07-25",
                    "2020-07-26",
                    "2021-07-25",
                    "2021-07-26",
                    "2022-07-25",
                    "2022-07-26",
                    "2023-07-25",
                    "2023-07-26",
                    "2024-07-25",
                    "2024-07-26",
                    "2025-07-25",
                    "2025-07-26",
                )
                self.assertHolidayName(name, holidays, range(1979, 2050))
                self.assertNoHolidayName(name, holidays, range(AD.start_year, 1979))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_epiphany_eve(self):
        name = "Vigília de Reis (a partir de les 13h)"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(name, (f"{year}-01-05" for year in self.full_range))

    def test_maundy_thursday(self):
        name = "Dijous Sant (a partir de les 13h)"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertGovernmentHolidayName(name, self.full_range)

    def test_christmas_eve(self):
        name = "Vigília de Nadal (a partir de les 13h)"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Vigília de Cap d'Any (a partir de les 13h)"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_2023(self):
        self.assertHolidays(
            Andorra(years=2023),
            ("2023-01-01", "Cap d'Any"),
            ("2023-01-06", "Reis"),
            ("2023-02-20", "Carnaval"),
            ("2023-03-14", "Dia de la Constitució"),
            ("2023-04-07", "Divendres Sant"),
            ("2023-04-10", "Dilluns de Pasqua"),
            ("2023-05-01", "Festa del treball"),
            ("2023-05-29", "Dilluns de Pentecosta"),
            ("2023-08-15", "Assumpció"),
            ("2023-09-08", "Nostra Senyora de Meritxell"),
            ("2023-11-01", "Tots Sants"),
            ("2023-12-08", "Immaculada Concepció"),
            ("2023-12-25", "Nadal"),
            ("2023-12-26", "Sant Esteve"),
        )

    def test_government_2023(self):
        self.assertHolidays(
            Andorra(categories=GOVERNMENT, years=2023),
            ("2023-01-05", "Vigília de Reis (a partir de les 13h)"),
            ("2023-04-06", "Dijous Sant (a partir de les 13h)"),
            ("2023-12-24", "Vigília de Nadal (a partir de les 13h)"),
            ("2023-12-31", "Vigília de Cap d'Any (a partir de les 13h)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Cap d'Any"),
            ("2024-01-05", "Vigília de Reis (a partir de les 13h)"),
            ("2024-01-06", "Reis"),
            ("2024-01-07", "Sant Julià"),
            ("2024-01-17", "Sant Antoni"),
            ("2024-02-12", "Carnaval"),
            ("2024-03-14", "Dia de la Constitució"),
            ("2024-03-28", "Dijous Sant (a partir de les 13h)"),
            ("2024-03-29", "Divendres Sant"),
            ("2024-04-01", "Dilluns de Pasqua"),
            ("2024-05-01", "Festa del treball"),
            ("2024-05-07", "Sant Miquel d'Engolasters"),
            ("2024-05-20", "Dilluns de Pentecosta"),
            ("2024-05-25", "Diada de Canòlich"),
            ("2024-06-16", "Diada de la creació de la parròquia"),
            ("2024-06-29", "Sant Pere"),
            ("2024-07-25", "Festa Major d'Escaldes-Engordany"),
            ("2024-07-26", "Festa Major d'Escaldes-Engordany"),
            ("2024-07-29", "Festa Major de Sant Julià de Lòria"),
            ("2024-07-30", "Festa Major de Sant Julià de Lòria"),
            ("2024-08-03", "Festa Major d'Andorra la Vella"),
            ("2024-08-04", "Festa Major d'Andorra la Vella"),
            ("2024-08-05", "Festa Major d'Andorra la Vella"),
            ("2024-08-15", "Assumpció"),
            ("2024-08-16", "Sant Roc"),
            ("2024-09-08", "Nostra Senyora de Meritxell"),
            ("2024-11-01", "Tots Sants"),
            ("2024-12-08", "Immaculada Concepció"),
            ("2024-12-24", "Vigília de Nadal (a partir de les 13h)"),
            ("2024-12-25", "Nadal"),
            ("2024-12-26", "Sant Esteve"),
            ("2024-12-31", "Vigília de Cap d'Any (a partir de les 13h)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-05", "Epiphany Eve (from 1pm)"),
            ("2024-01-06", "Epiphany"),
            ("2024-01-07", "Saint Julian's Day"),
            ("2024-01-17", "Saint Anthony's Day"),
            ("2024-02-12", "Carnival"),
            ("2024-03-14", "Constitution Day"),
            ("2024-03-28", "Maundy Thursday (from 1pm)"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-07", "Saint Michael of Engolasters' Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-05-25", "Virgin Mary of Canòlich"),
            ("2024-06-16", "Parish foundation day"),
            ("2024-06-29", "Saint Peter's Day"),
            ("2024-07-25", "Escaldes-Engordany Festival"),
            ("2024-07-26", "Escaldes-Engordany Festival"),
            ("2024-07-29", "Sant Julià de Lòria Festival"),
            ("2024-07-30", "Sant Julià de Lòria Festival"),
            ("2024-08-03", "Andorra la Vella Festival"),
            ("2024-08-04", "Andorra la Vella Festival"),
            ("2024-08-05", "Andorra la Vella Festival"),
            ("2024-08-15", "Assumption Day"),
            ("2024-08-16", "Saint Roch's Day"),
            ("2024-09-08", "Our Lady of Meritxell"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-12-08", "Immaculate Conception"),
            ("2024-12-24", "Christmas Eve (from 1pm)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Saint Stephen's Day"),
            ("2024-12-31", "New Year's Eve (from 1pm)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-01-05", "Переддень Богоявлення (з 13:00)"),
            ("2024-01-06", "Богоявлення"),
            ("2024-01-07", "День Святого Юліана"),
            ("2024-01-17", "День Святого Антонія"),
            ("2024-02-12", "Карнавал"),
            ("2024-03-14", "День Конституції"),
            ("2024-03-28", "Великий четвер (з 13:00)"),
            ("2024-03-29", "Страсна пʼятниця"),
            ("2024-04-01", "Великодній понеділок"),
            ("2024-05-01", "День праці"),
            ("2024-05-07", "День Святого Михаїла Енголастерського"),
            ("2024-05-20", "День Святого Духа"),
            ("2024-05-25", "День Богоматері Каноліхської"),
            ("2024-06-16", "День створення парафії"),
            ("2024-06-29", "День Святого Петра"),
            ("2024-07-25", "Свято парафії Ескальдес-Енгордань"),
            ("2024-07-26", "Свято парафії Ескальдес-Енгордань"),
            ("2024-07-29", "Свято парафії Сант-Жулія-де-Лорія"),
            ("2024-07-30", "Свято парафії Сант-Жулія-де-Лорія"),
            ("2024-08-03", "Свято парафії Андорра-ла-Велья"),
            ("2024-08-04", "Свято парафії Андорра-ла-Велья"),
            ("2024-08-05", "Свято парафії Андорра-ла-Велья"),
            ("2024-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2024-08-16", "День Святого Роха"),
            ("2024-09-08", "День Богоматері Мерічелльської"),
            ("2024-11-01", "День усіх святих"),
            ("2024-12-08", "Непорочне зачаття Діви Марії"),
            ("2024-12-24", "Святий вечір (з 13:00)"),
            ("2024-12-25", "Різдво Христове"),
            ("2024-12-26", "День Святого Стефана"),
            ("2024-12-31", "Переддень Нового року (з 13:00)"),
        )
