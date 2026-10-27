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

from holidays import financial_holidays
from holidays.constants import HALF_DAY
from holidays.financial.euronext import XAMS, XBRU, XDUB, XLIS, XMIL, XOSL, XPAR, Euronext
from tests.common import CommonFinancialTests


class TestEuronext(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Euronext, with_subdiv_categories=True)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Euronext(subdiv="XMIL", categories=HALF_DAY, years=range(2021, 2050))
        )

    def test_market_subclasses_default_subdivision(self):
        # Each market subclass defaults to its own subdivision, so the
        # market-specific holidays are included without an explicit subdiv.
        self.assertEqual(XPAR(years=2025).subdiv, "XPAR")
        self.assertEqual(XAMS(years=2025).subdiv, "XAMS")
        self.assertEqual(XBRU(years=2025).subdiv, "XBRU")
        self.assertEqual(XDUB(years=2025).subdiv, "XDUB")
        self.assertEqual(XLIS(years=2025).subdiv, "XLIS")
        self.assertEqual(XMIL(years=2025).subdiv, "XMIL")
        self.assertEqual(XOSL(years=2025).subdiv, "XOSL")
        # Dublin, Milan and Oslo specific holidays.
        self.assertIn("2025-05-05", XDUB(years=2025))
        self.assertIn("2025-08-15", XMIL(years=2025))
        self.assertIn("2025-04-17", XOSL(years=2025))
        self.assertIn("2024-05-17", XOSL(years=2024))
        # The same applies when the market is requested by its code.
        self.assertIn("2024-05-17", financial_holidays("XOSL", years=2024))
        self.assertIn("2025-08-15", financial_holidays("XMIL", years=2025))
        self.assertIn("2022-12-27", financial_holidays("XDUB", years=2022))
        # A market subclass always uses its own subdivision, even when a
        # different subdivision is passed explicitly as a keyword argument.
        # Positional construction is not supported: like the other
        # ObservedHolidayBase entities (e.g. UnitedKingdom), Euronext is
        # constructed with keywords or via financial_holidays().
        self.assertEqual(XOSL(subdiv="XAMS", years=2025).subdiv, "XOSL")

    def test_new_years_day(self):
        # Holidays that fall on a weekend are not included.
        self.assertHolidayName(
            "New Year's Day",
            (f"{year}-01-01" for year in self.full_range if date(year, 1, 1).weekday() < 5),
        )
        self.assertNoHoliday("2022-01-01", "2023-01-01")

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
        # Holidays that fall on a weekend are not included.
        self.assertHolidayName(
            "Labour Day",
            (f"{year}-05-01" for year in self.full_range if date(year, 5, 1).weekday() < 5),
        )
        self.assertNoHoliday("2021-05-01", "2022-05-01")

    def test_christmas_day(self):
        # Holidays that fall on a weekend are not included.
        self.assertHolidayName(
            "Christmas Day",
            (f"{year}-12-25" for year in self.full_range if date(year, 12, 25).weekday() < 5),
        )
        self.assertNoHoliday("2021-12-25", "2022-12-25")

    def test_saint_stephens_day(self):
        # Holidays that fall on a weekend are not included.
        self.assertHolidayName(
            "Saint Stephen's Day",
            (f"{year}-12-26" for year in self.full_range if date(year, 12, 26).weekday() < 5),
        )
        self.assertNoHoliday("2021-12-26", "2026-12-26")

    def test_weekend_holidays_are_not_trading_days(self):
        self.assertNoHoliday(
            "2020-12-26",
            "2021-05-01",
            "2021-12-25",
            "2021-12-26",
            "2022-01-01",
            "2022-05-01",
            "2022-12-25",
            "2026-12-26",
        )
        self.assertNoSubdivXmilHoliday("2021-08-15", "2026-08-15")
        self.assertNoSubdivXoslHoliday("2020-05-17", "2026-05-17")

    def test_christmas_eve(self):
        name = "Christmas Eve (markets close at 14:05 CET)"
        self.assertNoHolidayName("Christmas Eve")
        self.assertHalfDayHolidayName(
            name,
            "2019-12-24",
            "2020-12-24",
            "2021-12-24",
            "2024-12-24",
            "2025-12-24",
            "2026-12-24",
        )
        self.assertNoHalfDayHolidayName(name, "2022-12-24", "2023-12-24")

    def test_new_years_eve(self):
        name = "New Year's Eve (markets close at 14:05 CET)"
        self.assertNoHolidayName("New Year's Eve")
        self.assertHalfDayHolidayName(
            name,
            "2019-12-31",
            "2020-12-31",
            "2021-12-31",
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        self.assertNoHalfDayHolidayName(name, "2022-12-31", "2023-12-31")

    def test_2019(self):
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "New Year's Day"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-05-01", "Labour Day"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-26", "Saint Stephen's Day"),
        )

    def test_2020(self):
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-01", "Labour Day"),
            ("2020-12-25", "Christmas Day"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labour Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Saint Stephen's Day"),
        )

    # Dublin (XDUB).

    def test_dublin_irish_may_bank_holiday(self):
        self.assertSubdivXdubHolidayName(
            "Irish May Bank Holiday",
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
            "2025-05-05",
            "2026-05-04",
        )
        # Euronext Dublin has been closed on May Day since 2021.
        self.assertNoSubdivXdubHolidayName("Irish May Bank Holiday", 2019, 2020)

    def test_dublin_weekend_substitutes(self):
        # New Year's Day substitutes.
        self.assertSubdivXdubHolidayName(
            "Substitute for New Year's Day", "2022-01-03", "2023-01-02"
        )
        # Christmas Day substitutes.
        self.assertSubdivXdubHolidayName(
            "Substitute for Christmas Day", "2021-12-27", "2022-12-27"
        )
        # Saint Stephen's Day substitutes.
        self.assertSubdivXdubHolidayName(
            "Substitute for Saint Stephen's Day", "2020-12-28", "2021-12-28", "2026-12-28"
        )
        # Other markets have no weekend substitutes.
        self.assertNoSubdivXparHoliday("2022-01-03", "2023-01-02", "2022-12-27")

    def test_dublin_observed_flag(self):
        # The Dublin weekend substitutes use _move_holiday with
        # force_observed=True, so they stay in place regardless of
        # the observed flag, and the actual weekend dates are not in
        # the calendar (the holidays were moved to the substitutes).
        self.assertIn("2022-01-03", XDUB(years=2022, observed=False))
        self.assertNotIn("2022-01-01", XDUB(years=2022, observed=False))
        self.assertIn("2022-12-27", XDUB(years=2022, observed=False))
        self.assertNotIn("2022-12-25", XDUB(years=2022, observed=False))
        self.assertIn("2021-12-28", XDUB(years=2021, observed=False))
        # Weekend dates are excluded regardless of the observed flag for
        # other markets.
        self.assertNotIn("2022-01-01", XPAR(years=2022, observed=False))
        self.assertNotIn("2022-12-25", XPAR(years=2022, observed=False))

    def test_half_day_eves_observed_flag(self):
        # The Eve half days use forced observed moves, so weekend Eves
        # stay suppressed and Dublin's Friday substitutes stay in place
        # regardless of the observed flag.
        name = "Christmas Eve (markets close at 14:05 CET)"
        self.assertNoSubdivXparHalfDayHolidayName(name, "2022-12-24")
        self.assertNoSubdivXparHalfDayHolidayName(
            "New Year's Eve (markets close at 14:05 CET)", "2022-12-31"
        )
        self.assertNotIn("2022-12-24", XPAR(years=2022, observed=False, categories=HALF_DAY))
        self.assertNotIn("2022-12-31", XPAR(years=2022, observed=False, categories=HALF_DAY))
        self.assertSubdivXdubHalfDayHolidayName(
            "Christmas Eve (markets close at 14:00 CET)", "2022-12-23"
        )
        self.assertIn("2022-12-23", XDUB(years=2022, observed=False, categories=HALF_DAY))

    def test_dublin_half_day_substitutes(self):
        # Christmas Eve half trading day observed on the preceding Friday.
        self.assertSubdivXdubHalfDayHolidayName(
            "Christmas Eve (markets close at 14:00 CET)", "2022-12-23", "2023-12-22"
        )
        # New Year's Eve half trading day observed on the preceding Friday.
        self.assertSubdivXdubHalfDayHolidayName(
            "New Year's Eve (markets close at 14:00 CET)", "2022-12-30", "2023-12-29"
        )
        self.assertNoSubdivXdubHalfDayHolidayName(
            "Christmas Eve (markets close at 14:00 CET)", "2022-12-24", "2023-12-24"
        )
        self.assertNoSubdivXdubHalfDayHolidayName(
            "New Year's Eve (markets close at 14:00 CET)", "2022-12-31", "2023-12-31"
        )

    def test_dublin_2019(self):
        self.assertSubdivXdubHolidayDatesInYear(
            2019,
            "2019-01-01",
            "2019-04-19",
            "2019-04-22",
            "2019-05-01",
            "2019-12-25",
            "2019-12-26",
        )

    def test_dublin_2020(self):
        self.assertSubdivXdubHolidayDatesInYear(
            2020,
            "2020-01-01",
            "2020-04-10",
            "2020-04-13",
            "2020-05-01",
            "2020-12-25",
            "2020-12-28",
        )

    def test_dublin_2022(self):
        self.assertSubdivXdubHolidayDatesInYear(
            2022,
            "2022-01-03",
            "2022-04-15",
            "2022-04-18",
            "2022-05-02",
            "2022-12-26",
            "2022-12-27",
        )

    # Milan (XMIL).

    def test_milan_assumption_day(self):
        name = "Assumption Day"
        # Holidays that fall on a weekend are not included.
        self.assertSubdivXmilHolidayName(
            name,
            (
                f"{year}-08-15"
                for year in range(2023, self.end_year)
                if date(year, 8, 15).weekday() < 5
            ),
        )
        self.assertNoSubdivXmilHolidayName(name, 2021, 2022)
        self.assertNoSubdivXmilHolidayName(name, "2026-08-15")

    def test_milan_christmas_eve_and_new_years_eve(self):
        # Full-day closures in Milan (not half trading days).
        self.assertSubdivXmilHolidayName("Christmas Eve", "2024-12-24", "2025-12-24", "2026-12-24")
        self.assertSubdivXmilHolidayName(
            "New Year's Eve", "2024-12-31", "2025-12-31", "2026-12-31"
        )
        self.assertNoSubdivXmilHalfDayHolidayName("Christmas Eve", "2024-12-24")
        self.assertNoSubdivXmilHalfDayHolidayName("New Year's Eve", "2024-12-31")
        # Holidays that fall on a weekend are not included.
        self.assertNoSubdivXmilHolidayName("Christmas Eve", "2023-12-24")
        self.assertNoSubdivXmilHolidayName("New Year's Eve", "2023-12-31")

    def test_milan_2025(self):
        self.assertSubdivXmilHolidayDatesInYear(
            2025,
            "2025-01-01",
            "2025-04-18",
            "2025-04-21",
            "2025-05-01",
            "2025-08-15",
            "2025-12-24",
            "2025-12-25",
            "2025-12-26",
            "2025-12-31",
        )

    # Oslo (XOSL).

    def test_oslo_maundy_thursday(self):
        name = "Maundy Thursday"
        self.assertSubdivXoslHolidayName(
            name,
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
            "2026-04-02",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_oslo_ascension_day(self):
        name = "Ascension Day"
        self.assertSubdivXoslHolidayName(
            name,
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
            "2026-05-14",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_oslo_constitution_day(self):
        # Holidays that fall on a weekend are not included.
        self.assertSubdivXoslHolidayName(
            "Constitution Day",
            (f"{year}-05-17" for year in self.full_range if date(year, 5, 17).weekday() < 5),
        )
        self.assertNoSubdivXoslHolidayName("Constitution Day", "2020-05-17", "2026-05-17")

    def test_oslo_whit_monday(self):
        name = "Whit Monday"
        self.assertSubdivXoslHolidayName(
            name,
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
            "2026-05-25",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_oslo_christmas_eve_and_new_years_eve(self):
        # Full-day closures in Oslo (not half trading days).
        self.assertSubdivXoslHolidayName("Christmas Eve", "2024-12-24", "2025-12-24", "2026-12-24")
        self.assertSubdivXoslHolidayName(
            "New Year's Eve", "2024-12-31", "2025-12-31", "2026-12-31"
        )
        self.assertNoSubdivXoslHalfDayHolidayName("Christmas Eve", "2024-12-24")
        self.assertNoSubdivXoslHalfDayHolidayName("New Year's Eve", "2024-12-31")
        # Holidays that fall on a weekend are not included.
        self.assertNoSubdivXoslHolidayName("Christmas Eve", "2023-12-24")
        self.assertNoSubdivXoslHolidayName("New Year's Eve", "2023-12-31")

    def test_oslo_wednesday_before_easter(self):
        name = "Wednesday before Easter (markets close at 13:00 CET)"
        self.assertSubdivXoslHalfDayHolidayName(
            name,
            "2019-04-17",
            "2020-04-08",
            "2021-03-31",
            "2022-04-13",
            "2023-04-05",
            "2024-03-27",
            "2025-04-16",
            "2026-04-01",
        )
        self.assertSubdivXoslHalfDayHolidayName(name, self.full_range)

    def test_oslo_2019(self):
        self.assertSubdivXoslHolidayDatesInYear(
            2019,
            "2019-01-01",
            "2019-04-18",
            "2019-04-19",
            "2019-04-22",
            "2019-05-01",
            "2019-05-17",
            "2019-05-30",
            "2019-06-10",
            "2019-12-24",
            "2019-12-25",
            "2019-12-26",
            "2019-12-31",
        )

    def test_oslo_2020(self):
        self.assertSubdivXoslHolidayDatesInYear(
            2020,
            "2020-01-01",
            "2020-04-09",
            "2020-04-10",
            "2020-04-13",
            "2020-05-01",
            "2020-05-21",
            "2020-06-01",
            "2020-12-24",
            "2020-12-25",
            "2020-12-31",
        )

    def test_oslo_2024(self):
        self.assertSubdivXoslHolidayDatesInYear(
            2024,
            "2024-01-01",
            "2024-03-28",
            "2024-03-29",
            "2024-04-01",
            "2024-05-01",
            "2024-05-09",
            "2024-05-17",
            "2024-05-20",
            "2024-12-24",
            "2024-12-25",
            "2024-12-26",
            "2024-12-31",
        )

    # Localization.

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
