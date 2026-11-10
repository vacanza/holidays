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

from datetime import date
from unittest import TestCase

from holidays.financial.euronext import Euronext
from tests.common import CommonFinancialTests


class TestEuronext(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Euronext, with_subdiv_categories=True)

    def test_no_holidays(self):
        super().test_no_holidays()
        self.assertNoHolidays(self.holidays_half_day)
        self.assertNoHolidays(self.subdiv_half_day_holidays["XMIL"])
        self.assertNoHolidays(self.subdiv_half_day_holidays["XATH"])

    def _weekend_holidays(self, month, day):
        return (dt for year in self.full_range if (dt := date(year, month, day)).weekday() > 4)

    def _no_weekend_holidays(self, month, day):
        return (dt for year in self.full_range if (dt := date(year, month, day)).weekday() < 5)

    def test_new_years_day(self):
        name = "New Year's Day"
        name_observed = f"Substitute for {name}"
        self.assertHolidayName(name, self._no_weekend_holidays(1, 1))
        self.assertNoHoliday(self._weekend_holidays(1, 1))

        obs_dts = (
            "2022-01-03",
            "2023-01-02",
        )
        self.assertNoHolidayName(name_observed)
        self.assertNoHoliday(obs_dts)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XDUB":
                self.assertHolidayName(name_observed, holidays, obs_dts)
            else:
                self.assertNoHolidayName(name_observed, holidays)
                self.assertNoHoliday(holidays, obs_dts)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
            "2026-04-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
            "2026-04-06",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", self._no_weekend_holidays(5, 1))
        self.assertNoHoliday(self._weekend_holidays(5, 1))

    def test_christmas_day(self):
        name = "Christmas Day"
        name_observed = f"Substitute for {name}"
        self.assertHolidayName(name, self._no_weekend_holidays(12, 25))
        self.assertNoHoliday(self._weekend_holidays(12, 25))

        obs_dts = (
            "2021-12-27",
            "2022-12-27",
        )
        self.assertNoHolidayName(name_observed)
        self.assertNoHoliday(obs_dts)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XDUB":
                self.assertHolidayName(name_observed, holidays, obs_dts)
            else:
                self.assertNoHolidayName(name_observed, holidays)
                self.assertNoHoliday(holidays, obs_dts)

    def test_saint_stephens_day(self):
        name = "Saint Stephen's Day"
        name_observed = f"Substitute for {name}"
        self.assertHolidayName(name, self._no_weekend_holidays(12, 26))
        self.assertNoHoliday(self._weekend_holidays(12, 26))

        obs_dts = (
            "2020-12-28",
            "2021-12-28",
            "2026-12-28",
        )
        self.assertNoHolidayName(name_observed)
        self.assertNoHoliday(obs_dts)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XDUB":
                self.assertHolidayName(name_observed, holidays, obs_dts)
            else:
                self.assertNoHolidayName(name_observed, holidays)
                self.assertNoHoliday(holidays, obs_dts)

    def test_christmas_eve(self):
        name = "Christmas Eve"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            match subdiv:
                case "XMIL":
                    self.assertHolidayName(
                        name,
                        holidays,
                        (dt for dt in self._no_weekend_holidays(12, 24) if dt.year >= 2023),
                    )
                    self.assertNoHoliday(
                        holidays,
                        (dt for dt in self._weekend_holidays(12, 24) if dt.year >= 2023),
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2023))
                case "XATH":
                    self.assertHolidayName(
                        name,
                        holidays,
                        (dt for dt in self._no_weekend_holidays(12, 24) if dt.year >= 2026),
                    )
                    self.assertNoHoliday(
                        holidays,
                        (dt for dt in self._weekend_holidays(12, 24) if dt.year >= 2026),
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2026))
                case "XOSL":
                    self.assertHolidayName(name, holidays, self._no_weekend_holidays(12, 24))
                    self.assertNoHoliday(holidays, self._weekend_holidays(12, 24))
                case _:
                    self.assertNoHolidayName(name, holidays)

    def test_christmas_eve_half_day(self):
        name_half_day_1400 = "Christmas Eve (markets close at 14:00 CET)"
        name_half_day_1405 = "Christmas Eve (markets close at 14:05 CET)"
        self.assertNoHolidayName(name_half_day_1400)
        self.assertNoHolidayName(name_half_day_1405)

        for subdiv, holidays in self.subdiv_half_day_holidays.items():
            match subdiv:
                case "XDUB":
                    self.assertHolidayName(
                        name_half_day_1400,
                        holidays,
                        "2022-12-23",
                        "2023-12-22",
                        self._no_weekend_holidays(12, 24),
                    )
                    self.assertHolidayName(name_half_day_1400, holidays, self.full_range)
                    self.assertNoHoliday(holidays, self._weekend_holidays(12, 24))

                case "XMIL" | "XOSL" | "XATH":
                    self.assertNoHolidayName(name_half_day_1405, holidays)
                    self.assertNoHolidayName(name_half_day_1400, holidays)
                case _:
                    self.assertNoHolidayName(name_half_day_1400, holidays)
                    self.assertHolidayName(
                        name_half_day_1405, holidays, self._no_weekend_holidays(12, 24)
                    )
                    self.assertNoHoliday(holidays, self._weekend_holidays(12, 24))

    def test_new_years_eve(self):
        name = "New Year's Eve"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            match subdiv:
                case "XMIL":
                    self.assertHolidayName(
                        name,
                        holidays,
                        (dt for dt in self._no_weekend_holidays(12, 31) if dt.year >= 2023),
                    )
                    self.assertNoHoliday(
                        holidays,
                        (dt for dt in self._weekend_holidays(12, 31) if dt.year >= 2023),
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2023))
                case "XATH":
                    self.assertHolidayName(
                        name,
                        holidays,
                        (dt for dt in self._no_weekend_holidays(12, 31) if dt.year >= 2027),
                    )
                    self.assertNoHoliday(
                        holidays,
                        (dt for dt in self._weekend_holidays(12, 31) if dt.year >= 2027),
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2027))
                case "XOSL":
                    self.assertHolidayName(name, holidays, self._no_weekend_holidays(12, 31))
                    self.assertNoHoliday(holidays, self._weekend_holidays(12, 31))
                case _:
                    self.assertNoHolidayName(name, holidays)

    def test_new_years_eve_half_day(self):
        name_half_day_1400 = "New Year's Eve (markets close at 14:00 CET)"
        name_half_day_1405 = "New Year's Eve (markets close at 14:05 CET)"
        self.assertNoHolidayName(name_half_day_1400)
        self.assertNoHolidayName(name_half_day_1405)

        for subdiv, holidays in self.subdiv_half_day_holidays.items():
            match subdiv:
                case "XDUB":
                    self.assertHolidayName(
                        name_half_day_1400,
                        holidays,
                        "2022-12-30",
                        "2023-12-29",
                        self._no_weekend_holidays(12, 31),
                    )
                    self.assertHolidayName(name_half_day_1400, holidays, self.full_range)
                    self.assertNoHoliday(holidays, self._weekend_holidays(12, 31))

                case "XMIL" | "XOSL" | "XATH":
                    self.assertNoHolidayName(name_half_day_1405, holidays)
                    self.assertNoHolidayName(name_half_day_1400, holidays)
                case _:
                    self.assertNoHolidayName(name_half_day_1400, holidays)
                    self.assertHolidayName(
                        name_half_day_1405, holidays, self._no_weekend_holidays(12, 31)
                    )
                    self.assertNoHoliday(holidays, self._weekend_holidays(12, 31))

    def test_irish_may_bank_holiday(self):
        name = "Irish May Bank Holiday"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XDUB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2021-05-03",
                    "2022-05-02",
                    "2023-05-01",
                    "2024-05-06",
                    "2025-05-05",
                    "2026-05-04",
                )
                self.assertHolidayName(name, holidays, range(2021, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2021))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_assumption_day(self):
        name = "Assumption Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            match subdiv:
                case "XMIL":
                    self.assertHolidayName(
                        name,
                        holidays,
                        (dt for dt in self._no_weekend_holidays(8, 15) if dt.year >= 2023),
                    )
                    self.assertNoHoliday(
                        holidays,
                        (dt for dt in self._weekend_holidays(8, 15) if dt.year >= 2023),
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2023))
                case "XATH":
                    self.assertHolidayName(
                        name,
                        holidays,
                        (dt for dt in self._no_weekend_holidays(8, 15) if dt.year >= 2026),
                    )
                    self.assertNoHoliday(
                        holidays,
                        (dt for dt in self._weekend_holidays(8, 15) if dt.year >= 2026),
                    )
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2026))
                case _:
                    self.assertNoHolidayName(name, holidays)

    def test_maundy_thursday(self):
        name = "Maundy Thursday"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XOSL":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2019-04-18",
                    "2020-04-09",
                    "2021-04-01",
                    "2022-04-14",
                    "2023-04-06",
                    "2024-03-28",
                    "2025-04-17",
                    "2026-04-02",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XOSL":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2019-05-30",
                    "2020-05-21",
                    "2021-05-13",
                    "2022-05-26",
                    "2023-05-18",
                    "2024-05-09",
                    "2025-05-29",
                    "2026-05-14",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XOSL":
                self.assertHolidayName(name, holidays, self._no_weekend_holidays(5, 17))
                self.assertNoHoliday(holidays, self._weekend_holidays(5, 17))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            match subdiv:
                case "XOSL":
                    self.assertHolidayName(
                        name,
                        holidays,
                        "2019-06-10",
                        "2020-06-01",
                        "2021-05-24",
                        "2022-06-06",
                        "2023-05-29",
                        "2024-05-20",
                        "2025-06-09",
                        "2026-05-25",
                    )
                    self.assertHolidayName(name, holidays, self.full_range)
                case "XATH":
                    # Orthodox Whit Monday (Orthodox Easter + 50 days).
                    self.assertHolidayName(
                        name,
                        holidays,
                        "2026-06-01",
                        "2027-06-21",
                        "2028-06-05",
                        "2029-05-28",
                        "2030-06-17",
                        "2032-06-21",
                    )
                    self.assertHolidayName(name, holidays, range(2026, self.end_year))
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2026))
                case _:
                    self.assertNoHolidayName(name, holidays)

    def test_epiphany(self):
        name = "Epiphany"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XATH":
                self.assertHolidayName(
                    name,
                    holidays,
                    (dt for dt in self._no_weekend_holidays(1, 6) if dt.year >= 2026),
                )
                self.assertNoHoliday(
                    holidays,
                    (dt for dt in self._weekend_holidays(1, 6) if dt.year >= 2026),
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2026))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_ash_monday(self):
        name = "Ash Monday"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XATH":
                # Orthodox Ash Monday (Orthodox Easter - 48 days).
                self.assertHolidayName(
                    name,
                    holidays,
                    "2026-02-23",
                    "2027-03-15",
                    "2028-02-28",
                    "2029-02-19",
                    "2030-03-11",
                    "2032-03-15",
                )
                self.assertHolidayName(name, holidays, range(2026, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2026))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_national_holiday(self):
        name = "National Holiday"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XATH":
                self.assertHolidayName(
                    name,
                    holidays,
                    (dt for dt in self._no_weekend_holidays(3, 25) if dt.year >= 2026),
                    (dt for dt in self._no_weekend_holidays(10, 28) if dt.year >= 2026),
                )
                self.assertNoHoliday(
                    holidays,
                    (dt for dt in self._weekend_holidays(3, 25) if dt.year >= 2026),
                    (dt for dt in self._weekend_holidays(10, 28) if dt.year >= 2026),
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2026))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_good_friday_orthodox(self):
        name = "Good Friday (Orthodox)"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XATH":
                # Divergence years only; in coincidence years Orthodox Good Friday
                # is the same date as Catholic Good Friday and gets no separate entry.
                self.assertHolidayName(
                    name,
                    holidays,
                    "2026-04-10",
                    "2027-04-30",
                    "2029-04-06",
                    "2030-04-26",
                    "2032-04-30",
                    # Shared with Labour Day (not a coincidence year).
                    "2043-05-01",
                )
                self.assertNoHolidayName(
                    name,
                    holidays,
                    "2028-04-14",
                    "2031-04-11",
                    "2034-04-07",
                    "2037-04-03",
                    "2038-04-23",
                    "2041-04-19",
                    "2045-04-07",
                    "2048-04-03",
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2026))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_easter_monday_orthodox(self):
        name = "Easter Monday (Orthodox)"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "XATH":
                # Divergence years only; in coincidence years Orthodox Easter Monday
                # is the same date as Catholic Easter Monday and gets no separate entry.
                self.assertHolidayName(
                    name,
                    holidays,
                    "2026-04-13",
                    "2027-05-03",
                    "2029-04-09",
                    "2030-04-29",
                    "2032-05-03",
                )
                self.assertNoHolidayName(
                    name,
                    holidays,
                    "2028-04-17",
                    "2031-04-14",
                    "2034-04-10",
                    "2037-04-06",
                    "2038-04-26",
                    "2041-04-22",
                    "2045-04-10",
                    "2048-04-06",
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2026))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_wednesday_before_easter(self):
        name = "Wednesday before Easter (markets close at 13:00 CET)"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_half_day_holidays.items():
            if subdiv == "XOSL":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2019-04-17",
                    "2020-04-08",
                    "2021-03-31",
                    "2022-04-13",
                    "2023-04-05",
                    "2024-03-27",
                    "2025-04-16",
                    "2026-04-01",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-04-16", "Wednesday before Easter (markets close at 13:00 CET)"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labour Day"),
            ("2025-05-05", "Irish May Bank Holiday"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-09", "Whit Monday"),
            ("2025-08-15", "Assumption Day"),
            (
                "2025-12-24",
                "Christmas Eve; Christmas Eve (markets close at 14:00 CET); "
                "Christmas Eve (markets close at 14:05 CET)",
            ),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Saint Stephen's Day"),
            (
                "2025-12-31",
                "New Year's Eve; New Year's Eve (markets close at 14:00 CET); "
                "New Year's Eve (markets close at 14:05 CET)",
            ),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-04-16", "Wednesday before Easter (markets close at 13:00 CET)"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-05", "Irish May Bank Holiday"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-09", "Pentecost Monday"),
            ("2025-08-15", "Assumption Day"),
            (
                "2025-12-24",
                "Christmas Eve; Christmas Eve (markets close at 14:00 CET); "
                "Christmas Eve (markets close at 14:05 CET)",
            ),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Saint Stephen's Day"),
            (
                "2025-12-31",
                "New Year's Eve; New Year's Eve (markets close at 14:00 CET); "
                "New Year's Eve (markets close at 14:05 CET)",
            ),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2025-01-01", "Jour de l'an"),
            ("2025-04-16", "Mercredi avant Pâques (fermeture des marchés à 13h00 HEC)"),
            ("2025-04-17", "Jeudi saint"),
            ("2025-04-18", "Vendredi saint"),
            ("2025-04-21", "Lundi de Pâques"),
            ("2025-05-01", "Fête du Travail"),
            ("2025-05-05", "Jour férié de mai en Irlande"),
            ("2025-05-29", "Ascension"),
            ("2025-06-09", "Lundi de Pentecôte"),
            ("2025-08-15", "Assomption"),
            (
                "2025-12-24",
                "Veille de Noël; Veille de Noël (fermeture des marchés à 14h00 HEC); "
                "Veille de Noël (fermeture des marchés à 14h05 HEC)",
            ),
            ("2025-12-25", "Jour de Noël"),
            ("2025-12-26", "Saint-Étienne"),
            (
                "2025-12-31",
                "Saint-Sylvestre; Saint-Sylvestre (fermeture des marchés à 14h00 HEC); "
                "Saint-Sylvestre (fermeture des marchés à 14h05 HEC)",
            ),
        )

    def test_l10n_it(self):
        self.assertLocalizedHolidays(
            "it",
            ("2025-01-01", "Capodanno"),
            ("2025-04-16", "Mercoledì prima di Pasqua (i mercati chiudono alle 13:00 CET)"),
            ("2025-04-17", "Giovedì Santo"),
            ("2025-04-18", "Venerdì santo"),
            ("2025-04-21", "Lunedì dell'Angelo"),
            ("2025-05-01", "Festa del Lavoro"),
            ("2025-05-05", "Festa di maggio irlandese"),
            ("2025-05-29", "Ascensione"),
            ("2025-06-09", "Lunedì di Pentecoste"),
            ("2025-08-15", "Maria Santissima Assunta"),
            (
                "2025-12-24",
                "Vigilia di Natale; Vigilia di Natale (i mercati chiudono alle 14:00 CET); "
                "Vigilia di Natale (i mercati chiudono alle 14:05 CET)",
            ),
            ("2025-12-25", "Natale"),
            ("2025-12-26", "Santo Stefano"),
            (
                "2025-12-31",
                "Vigilia di Capodanno; Vigilia di Capodanno (i mercati chiudono alle 14:00 CET); "
                "Vigilia di Capodanno (i mercati chiudono alle 14:05 CET)",
            ),
        )

    def test_l10n_nl(self):
        self.assertLocalizedHolidays(
            "nl",
            ("2025-01-01", "Nieuwjaarsdag"),
            ("2025-04-16", "Woensdag voor Pasen (markten sluiten om 13:00 uur CET)"),
            ("2025-04-17", "Witte Donderdag"),
            ("2025-04-18", "Goede vrijdag"),
            ("2025-04-21", "Tweede paasdag"),
            ("2025-05-01", "Dag van de Arbeid"),
            ("2025-05-05", "Meifeestdag in Ierland"),
            ("2025-05-29", "Hemelvaartsdag"),
            ("2025-06-09", "Tweede pinksterdag"),
            ("2025-08-15", "Maria-Hemelvaart"),
            (
                "2025-12-24",
                "Kerstavond; Kerstavond (markten sluiten om 14:00 uur CET); "
                "Kerstavond (markten sluiten om 14:05 uur CET)",
            ),
            ("2025-12-25", "Eerste kerstdag"),
            ("2025-12-26", "Tweede kerstdag"),
            (
                "2025-12-31",
                "Oudejaarsavond; Oudejaarsavond (markten sluiten om 14:00 uur CET); "
                "Oudejaarsavond (markten sluiten om 14:05 uur CET)",
            ),
        )

    def test_l10n_no(self):
        self.assertLocalizedHolidays(
            "no",
            ("2025-01-01", "Første nyttårsdag"),
            ("2025-04-16", "Onsdag før påske (markedene stenger kl. 13:00 CET)"),
            ("2025-04-17", "Skjærtorsdag"),
            ("2025-04-18", "Langfredag"),
            ("2025-04-21", "Andre påskedag"),
            ("2025-05-01", "Arbeidernes dag"),
            ("2025-05-05", "Irsk mai-ferie"),
            ("2025-05-29", "Kristi himmelfartsdag"),
            ("2025-06-09", "Andre pinsedag"),
            ("2025-08-15", "Marias opptakelse i himmelen"),
            (
                "2025-12-24",
                "Julaften; Julaften (markedene stenger kl. 14:00 CET); "
                "Julaften (markedene stenger kl. 14:05 CET)",
            ),
            ("2025-12-25", "Første juledag"),
            ("2025-12-26", "Andre juledag"),
            (
                "2025-12-31",
                "Nyttårsaften; Nyttårsaften (markedene stenger kl. 14:00 CET); "
                "Nyttårsaften (markedene stenger kl. 14:05 CET)",
            ),
        )

    def test_l10n_pt_pt(self):
        self.assertLocalizedHolidays(
            "pt_PT",
            ("2025-01-01", "Ano Novo"),
            ("2025-04-16", "Quarta-feira antes da Páscoa (os mercados fecham às 13:00 CET)"),
            ("2025-04-17", "Quinta-feira Santa"),
            ("2025-04-18", "Sexta-feira Santa"),
            ("2025-04-21", "Segunda-feira de Páscoa"),
            ("2025-05-01", "Dia do Trabalhador"),
            ("2025-05-05", "Feriado de maio irlandês"),
            ("2025-05-29", "Quinta-feira da Ascensão"),
            ("2025-06-09", "Segunda-feira de Pentecoste"),
            ("2025-08-15", "Assunção de Nossa Senhora"),
            (
                "2025-12-24",
                "Véspera de Natal; Véspera de Natal (os mercados fecham às 14:00 CET); "
                "Véspera de Natal (os mercados fecham às 14:05 CET)",
            ),
            ("2025-12-25", "Dia de Natal"),
            ("2025-12-26", "Dia de Santo Estêvão"),
            (
                "2025-12-31",
                "Véspera de Ano Novo; Véspera de Ano Novo (os mercados fecham às 14:00 CET); "
                "Véspera de Ano Novo (os mercados fecham às 14:05 CET)",
            ),
        )

    def test_l10n_xath(self):
        # Athens-specific holidays only (2026, the first XATH year).
        expected = {
            "en_GB": (
                ("2026-01-06", "Epiphany"),
                ("2026-02-23", "Ash Monday"),
                ("2026-03-25", "National Holiday"),
                ("2026-04-10", "Good Friday (Orthodox)"),
                ("2026-04-13", "Easter Monday (Orthodox)"),
                ("2026-06-01", "Whit Monday"),
                ("2026-10-28", "National Holiday"),
                ("2026-12-24", "Christmas Eve"),
            ),
            "en_US": (
                ("2026-01-06", "Epiphany"),
                ("2026-02-23", "Ash Monday"),
                ("2026-03-25", "National Holiday"),
                ("2026-04-10", "Good Friday (Orthodox)"),
                ("2026-04-13", "Easter Monday (Orthodox)"),
                ("2026-06-01", "Pentecost Monday"),
                ("2026-10-28", "National Holiday"),
                ("2026-12-24", "Christmas Eve"),
            ),
            "fr": (
                ("2026-01-06", "Épiphanie"),
                ("2026-02-23", "Lundi pur"),
                ("2026-03-25", "Fête nationale"),
                ("2026-04-10", "Vendredi saint (orthodoxe)"),
                ("2026-04-13", "Lundi de Pâques (orthodoxe)"),
                ("2026-06-01", "Lundi de Pentecôte"),
                ("2026-10-28", "Fête nationale"),
                ("2026-12-24", "Veille de Noël"),
            ),
            "it": (
                ("2026-01-06", "Epifania"),
                ("2026-02-23", "Lunedì pulito"),
                ("2026-03-25", "Festa nazionale"),
                ("2026-04-10", "Venerdì santo (ortodosso)"),
                ("2026-04-13", "Lunedì di Pasqua (ortodosso)"),
                ("2026-06-01", "Lunedì di Pentecoste"),
                ("2026-10-28", "Festa nazionale"),
                ("2026-12-24", "Vigilia di Natale"),
            ),
            "nl": (
                ("2026-01-06", "Driekoningen"),
                ("2026-02-23", "Schone Maandag"),
                ("2026-03-25", "Nationale feestdag"),
                ("2026-04-10", "Goede Vrijdag (orthodox)"),
                ("2026-04-13", "Paasmaandag (orthodox)"),
                ("2026-06-01", "Tweede pinksterdag"),
                ("2026-10-28", "Nationale feestdag"),
                ("2026-12-24", "Kerstavond"),
            ),
            "no": (
                ("2026-01-06", "Helligtrekongersdag"),
                ("2026-02-23", "Rene mandag"),
                ("2026-03-25", "Nasjonaldag"),
                ("2026-04-10", "Langfredag (ortodoks)"),
                ("2026-04-13", "Andre påskedag (ortodoks)"),
                ("2026-06-01", "Andre pinsedag"),
                ("2026-10-28", "Nasjonaldag"),
                ("2026-12-24", "Julaften"),
            ),
            "pt_PT": (
                ("2026-01-06", "Epifania"),
                ("2026-02-23", "Segunda-feira Limpa"),
                ("2026-03-25", "Feriado nacional"),
                ("2026-04-10", "Sexta-feira Santa (ortodoxa)"),
                ("2026-04-13", "Segunda-feira de Páscoa (ortodoxa)"),
                ("2026-06-01", "Segunda-feira de Pentecoste"),
                ("2026-10-28", "Feriado nacional"),
                ("2026-12-24", "Véspera de Natal"),
            ),
        }
        for language, holidays in expected.items():
            instance = Euronext(subdiv="XATH", years=2026, language=language)
            for dt, name in holidays:
                self.assertEqual(name, instance.get(dt), (language, dt))
