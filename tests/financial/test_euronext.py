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

from holidays.financial.euronext import Euronext
from tests.common import CommonFinancialTests


class TestEuronext(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Euronext, with_subdiv_categories=True)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        weekday_dts = (
            "2021-01-01",
            "2024-01-01",
            "2025-01-01",
            "2026-01-01",
        )
        weekend_dts = (
            "2022-01-01",
            "2023-01-01",
        )
        obs_dts = (
            "2023-01-02",
            "2022-01-03",
        )
        self.assertHolidayName(name, weekday_dts)
        self.assertNoHoliday(weekend_dts)
        self.assertNoHoliday(obs_dts)
        self.assertSubdivXdubHolidayName(name, weekday_dts)
        self.assertNoSubdivXdubHoliday(weekend_dts)
        self.assertSubdivXdubHolidayName(name, obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        weekday_dts = (
            "2023-12-25",
            "2024-12-25",
            "2025-12-25",
            "2026-12-25",
        )
        weekend_dts = (
            "2021-12-25",
            "2022-12-25",
            "2027-12-25",
        )
        obs_dts = (
            "2021-12-27",
            "2022-12-27",
            "2027-12-27",
        )
        self.assertHolidayName(name, weekday_dts)
        self.assertNoHoliday(weekend_dts)
        self.assertNoHoliday(obs_dts)
        self.assertSubdivXdubHolidayName(name, weekday_dts)
        self.assertNoSubdivXdubHoliday(weekend_dts)
        self.assertSubdivXdubHolidayName(name, obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        weekday_dts = (
            "2022-12-26",
            "2023-12-26",
            "2024-12-26",
            "2025-12-26",
        )
        weekend_dts = (
            "2021-12-26",
            "2026-12-26",
            "2027-12-26",
        )
        obs_dts = (
            "2021-12-28",
            "2026-12-28",
            "2027-12-28",
        )
        self.assertHolidayName(name, weekday_dts)
        self.assertNoHoliday(weekend_dts)
        self.assertNoHoliday(obs_dts)
        self.assertSubdivXdubHolidayName(name, weekday_dts)
        self.assertNoSubdivXdubHoliday(weekend_dts)
        self.assertSubdivXdubHolidayName(name, obs_dts)

    def test_stephens_day(self):
        name = "Stephen's Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        weekday_dts = (
            "2022-12-26",
            "2023-12-26",
            "2024-12-26",
            "2025-12-26",
        )
        weekend_dts = (
            "2021-12-26",
            "2026-12-26",
            "2027-12-26",
        )
        obs_dts = (
            "2021-12-28",
            "2026-12-28",
            "2027-12-28",
        )
        self.assertHolidayName(name, weekday_dts)
        self.assertNoHoliday(weekend_dts)
        self.assertNoHoliday(obs_dts)
        self.assertSubdivXdubHolidayName(name, weekday_dts)
        self.assertNoSubdivXdubHoliday(weekend_dts)
        self.assertSubdivXdubHolidayName(name, obs_dts)

    def test_labour_day(self):
        name = "Labour Day"
        self.assertNonObservedHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2023-05-01",
            "2024-05-01",
            "2025-05-01",
            "2026-05-01",
        )
        self.assertNoHoliday(
            "2021-05-01",
            "2022-05-01",
            "2027-05-01",
        )

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
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
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
            "2026-04-06",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_eve_half_day(self):
        name = "Christmas Eve (Half Day Trading)"
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-24" for year in self.full_range)
        )
        weekday_dts = (
            "2024-12-24",
            "2025-12-24",
            "2026-12-24",
        )
        weekend_dts = (
            "2022-12-24",
            "2023-12-24",
        )
        xdub_obs_dts = (
            "2022-12-23",
            "2023-12-22",
        )
        self.assertHalfDayHolidayName(name, weekday_dts)
        self.assertNoHalfDayHoliday(weekend_dts)
        self.assertNoSubdivXmilHalfDayHoliday(weekday_dts, weekend_dts)
        self.assertSubdivXdubHalfDayHolidayName(name, weekday_dts, xdub_obs_dts)
        self.assertNoSubdivXdubHalfDayHoliday(weekend_dts)

    def test_new_years_eve_half_day(self):
        name = "New Year's Eve (Half Day Trading)"
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-31" for year in self.full_range)
        )
        weekday_dts = (
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        weekend_dts = (
            "2022-12-31",
            "2023-12-31",
        )
        xdub_obs_dts = (
            "2022-12-30",
            "2023-12-29",
        )
        self.assertHalfDayHolidayName(name, weekday_dts)
        self.assertNoHalfDayHoliday(weekend_dts)
        self.assertNoSubdivXmilHalfDayHoliday(weekday_dts, weekend_dts)
        self.assertSubdivXdubHalfDayHolidayName(name, weekday_dts, xdub_obs_dts)
        self.assertNoSubdivXdubHalfDayHoliday(weekend_dts)

    def test_may_bank_holiday(self):
        name = "May Bank Holiday"
        self.assertNoHolidayName(name)
        self.assertSubdivXdubHolidayName(
            name,
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
            "2025-05-05",
            "2026-05-04",
        )
        self.assertSubdivXdubHolidayName(name, self.full_range)

    def test_assumption_of_mary(self):
        name = "Assumption of Mary"
        self.assertNoHolidayName(name)
        weekday_dts = (
            "2022-08-15",
            "2023-08-15",
            "2024-08-15",
            "2025-08-15",
        )
        weekend_dts = (
            "2021-08-15",
            "2026-08-15",
            "2027-08-15",
        )
        self.assertSubdivXmilHolidayName(name, weekday_dts)
        self.assertNoSubdivXmilHoliday(weekend_dts)

    def test_new_years_eve(self):
        name = "New Year's Eve"
        self.assertNoHolidayName(name)
        weekday_dts = (
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        weekend_dts = (
            "2022-12-31",
            "2023-12-31",
        )
        self.assertSubdivXmilHolidayName(name, weekday_dts)
        self.assertNoSubdivXmilHoliday(weekend_dts)
        self.assertSubdivXoslHolidayName(name, weekday_dts)
        self.assertNoSubdivXoslHoliday(weekend_dts)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertNoHolidayName(name)
        self.assertSubdivXoslHolidayName(
            name,
            "2021-05-17",
            "2022-05-17",
            "2023-05-17",
            "2024-05-17",
        )
        self.assertNoSubdivXoslHoliday(
            "2020-05-17",
            "2025-05-17",
        )

    def test_maundy_thursday(self):
        name = "Maundy Thursday"
        self.assertNoHolidayName(name)
        self.assertSubdivXoslHolidayName(
            name,
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
            "2026-04-02",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertNoHolidayName(name)
        self.assertSubdivXoslHolidayName(
            name,
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
            "2026-05-14",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertNoHolidayName(name)
        self.assertSubdivXoslHolidayName(
            name,
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
            "2026-05-25",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_wednesday_before_maundy_thursday_half_day(self):
        name = "Wednesday before Maundy Thursday (Half Day Trading)"
        self.assertSubdivXoslHalfDayHolidayName(name, self.full_range)
        dts = (
            "2021-03-31",
            "2022-04-13",
            "2023-04-05",
            "2024-03-27",
            "2025-04-16",
            "2026-04-01",
        )
        self.assertSubdivXoslHalfDayHolidayName(name, dts)
        self.assertNoHalfDayHolidayName(name, dts)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-03-27", "Wednesday before Maundy Thursday (Half Day Trading)"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-06", "May Bank Holiday"),
            ("2024-05-09", "Ascension Day"),
            ("2024-05-17", "Constitution Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-08-15", "Assumption of Mary"),
            ("2024-12-24", "Christmas Eve; Christmas Eve (Half Day Trading)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day; Stephen's Day"),
            ("2024-12-31", "New Year's Eve; New Year's Eve (Half Day Trading)"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2024-01-01", "Jour de l'An"),
            ("2024-03-27", "Mercredi avant le Jeudi saint (Demi-journée de négociation)"),
            ("2024-03-28", "Jeudi saint"),
            ("2024-03-29", "Vendredi saint"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-06", "Jour férié de mai"),
            ("2024-05-09", "Ascension"),
            ("2024-05-17", "Jour de la Constitution"),
            ("2024-05-20", "Lundi de Pentecôte"),
            ("2024-08-15", "Assomption"),
            ("2024-12-24", "Veille de Noël; Veille de Noël (Demi-journée de négociation)"),
            ("2024-12-25", "Jour de Noël"),
            ("2024-12-26", "Lendemain de Noël; Saint-Étienne"),
            ("2024-12-31", "Saint-Sylvestre; Saint-Sylvestre (Demi-journée de négociation)"),
        )

    def test_l10n_it(self):
        self.assertLocalizedHolidays(
            "it",
            ("2024-01-01", "Capodanno"),
            ("2024-03-27", "Mercoledì prima del Giovedì Santo (Mezza giornata di negoziazione)"),
            ("2024-03-28", "Giovedì Santo"),
            ("2024-03-29", "Venerdì Santo"),
            ("2024-04-01", "Lunedì dell'Angelo"),
            ("2024-05-01", "Festa dei Lavoratori"),
            ("2024-05-06", "Giorno festivo di maggio"),
            ("2024-05-09", "Ascensione"),
            ("2024-05-17", "Giorno della Costituzione"),
            ("2024-05-20", "Lunedì di Pentecoste"),
            ("2024-08-15", "Assunzione di Maria"),
            (
                "2024-12-24",
                "Vigilia di Natale; Vigilia di Natale (Mezza giornata di negoziazione)",
            ),
            ("2024-12-25", "Natale"),
            ("2024-12-26", "Giorno di Santo Stefano; Santo Stefano"),
            (
                "2024-12-31",
                "Vigilia di Capodanno; Vigilia di Capodanno (Mezza giornata di negoziazione)",
            ),
        )

    def test_l10n_nl(self):
        self.assertLocalizedHolidays(
            "nl",
            ("2024-01-01", "Nieuwjaarsdag"),
            ("2024-03-27", "Woensdag voor Witte Donderdag (halve handelsdag)"),
            ("2024-03-28", "Witte Donderdag"),
            ("2024-03-29", "Goede Vrijdag"),
            ("2024-04-01", "Tweede paasdag"),
            ("2024-05-01", "Dag van de Arbeid"),
            ("2024-05-06", "Feestdag in mei"),
            ("2024-05-09", "Hemelvaartsdag"),
            ("2024-05-17", "Dag van de Grondwet"),
            ("2024-05-20", "Tweede pinksterdag"),
            ("2024-08-15", "Maria-Tenhemelopneming"),
            (
                "2024-12-24",
                "Kerstavond; Kerstavond (halve handelsdag)",
            ),
            ("2024-12-25", "Eerste kerstdag"),
            ("2024-12-26", "Sint-Stefanusdag; Tweede kerstdag"),
            (
                "2024-12-31",
                "Oudejaarsdag; Oudejaarsdag (halve handelsdag)",
            ),
        )

    def test_l10n_no(self):
        self.assertLocalizedHolidays(
            "no",
            ("2024-01-01", "Første nyttårsdag"),
            ("2024-03-27", "Onsdag før skjærtorsdag (Halv handelsdag)"),
            ("2024-03-28", "Skjærtorsdag"),
            ("2024-03-29", "Langfredag"),
            ("2024-04-01", "Andre påskedag"),
            ("2024-05-01", "Arbeidernes dag"),
            ("2024-05-06", "Offentlig fridag i mai"),
            ("2024-05-09", "Kristi himmelfartsdag"),
            ("2024-05-17", "Grunnlovsdag"),
            ("2024-05-20", "Andre pinsedag"),
            ("2024-08-15", "Jomfru Marias himmelfart"),
            ("2024-12-24", "Julaften; Julaften (Halv handelsdag)"),
            ("2024-12-25", "Første juledag"),
            ("2024-12-26", "Andre juledag; Stefanusdagen"),
            ("2024-12-31", "Nyttårsaften; Nyttårsaften (Halv handelsdag)"),
        )

    def test_l10n_pt_pt(self):
        self.assertLocalizedHolidays(
            "pt_PT",
            ("2024-01-01", "Dia de Ano Novo"),
            ("2024-03-27", "Quarta-feira antes da Quinta-feira Santa (Meio dia de negociação)"),
            ("2024-03-28", "Quinta-feira Santa"),
            ("2024-03-29", "Sexta-feira Santa"),
            ("2024-04-01", "Segunda-feira de Páscoa"),
            ("2024-05-01", "Dia do Trabalhador"),
            ("2024-05-06", "Feriado Bancário de Maio"),
            ("2024-05-09", "Dia da Ascensão"),
            ("2024-05-17", "Dia da Constituição"),
            ("2024-05-20", "Segunda-feira de Pentecostes"),
            ("2024-08-15", "Assunção de Maria"),
            ("2024-12-24", "Véspera de Natal; Véspera de Natal (Meio dia de negociação)"),
            ("2024-12-25", "Dia de Natal"),
            ("2024-12-26", "Boxing Day; Dia de Santo Estêvão"),
            ("2024-12-31", "Véspera de Ano Novo; Véspera de Ano Novo (Meio dia de negociação)"),
        )
