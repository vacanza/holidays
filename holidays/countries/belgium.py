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

from gettext import gettext as tr

from holidays.constants import BANK, PUBLIC, SCHOOL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase
from datetime import date, timedelta

def nth_weekday_of_month(year, month, weekday, n):
    """
    weekday: Monday=0 ... Sunday=6
    n: 1 = first, 2 = second, 3 = third, ...
    """
    # First day of the month
    d = date(year, month, 1)

    # Move forward to the first required weekday
    while d.weekday() != weekday:
        d += timedelta(days=1)

    # Jump (n-1) weeks ahead
    d += timedelta(weeks=n - 1)
    return d

def last_weekday_of_month(year, month, weekday):
    if month == 12:
        d = date(year, 12, 31)
    else:
        d = date(year, month + 1, 1) - timedelta(days=1)

    while d.weekday() != weekday:
        d -= timedelta(days=1)
    return d
class Belgium(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Belgium holidays."""

    country = "BE"
    default_language = "nl"
    supported_categories = (BANK, PUBLIC, SCHOOL)
    supported_languages = ("de", "en_US", "fr", "nl", "uk")

    subdivisions = (
        "VLG",  # Flemish Community.
        "WBR", # French Community (Wallonia + Brussels French schools)
        "GER",  # German-speaking Community.
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def show_ranges(self, holidays):
        ranges = []
        for name, group in groupby(sorted(holidays.items()), key=lambda x: x[1]):
            dates = [d for d, _ in group]
            start = dates[0]
            prev = dates[0]

            for d in dates[1:]:
                if d == prev + timedelta(days=1):
                    prev = d
                else:
                    ranges.append((name, start, prev))
                    start = d
                    prev = d

            ranges.append((name, start, prev))

        return ranges

    def _populate_public_holidays(self):
        self._add_new_years_day(tr("Nieuwjaar"))
        self._add_easter_sunday(tr("Pasen"))
        self._add_easter_monday(tr("Paasmaandag"))
        self._add_labor_day(tr("Dag van de Arbeid"))
        self._add_ascension_thursday(tr("O. L. H. Hemelvaart"))
        self._add_whit_sunday(tr("Pinksteren"))
        self._add_whit_monday(tr("Pinkstermaandag"))
        self._add_holiday_jul_21(tr("Nationale feestdag"))
        self._add_assumption_of_mary_day(tr("O. L. V. Hemelvaart"))
        self._add_all_saints_day(tr("Allerheiligen"))
        self._add_remembrance_day(tr("Wapenstilstand"))
        self._add_christmas_day(tr("Kerstmis"))

    # ---------------- BANK HOLIDAYS ----------------

    def _populate_bank_holidays(self):
        self._add_good_friday(tr("Goede Vrijdag"))
        self._add_holiday_40_days_past_easter(tr("Vrijdag na O. L. H. Hemelvaart"))
        self._add_christmas_day_two(tr("Banksluitingsdag"))

    # ---------------- SCHOOL HOLIDAYS ----------------

    def _populate_school_holidays(self):
        if self.subdiv == "VLG":
            self._populate_subdiv_vlg_school_holidays()
        elif self.subdiv == "WBR":
            self._populate_subdiv_wbr_school_holidays()
        elif self.subdiv == "GER":
            self._populate_subdiv_ger_school_holidays()

    # ---------- Flemish Community (VLG) ----------

    def _populate_subdiv_vlg_school_holidays(self):
        year = self._year
        easter = self._easter_sunday

        def add_range(name, start, end):
            # First day
            self._add_holiday(tr(name), start)

            # Remaining days
            duration = (end - start).days
            self._add_multiday_holiday(start, duration, name=tr(name))
        # Paasvakantie: Monday before Easter → 2 weeks
        start = easter - timedelta(days=6)
        end = start + timedelta(days=13)
        add_range("Paasvakantie", start, end)

        # Herfstvakantie: last Monday of October → 1 week
        last_october_day = date(year, 10, 31)
        start = last_october_day - timedelta(days=last_october_day.weekday())
        end = start + timedelta(days=6)
        add_range("Herfstvakantie", start, end)
        # Kerstvakantie: Monday of the week of 25 Dec → 2 weeks
        christmas = date(year, 12, 25)
        start = christmas - timedelta(days=christmas.weekday())
        end = start + timedelta(days=13)
        add_range("Kerstvakantie", start, end)

        prev_christmas = date(year - 1, 12, 25)
        prev_start = prev_christmas - timedelta(days=prev_christmas.weekday())
        prev_end = prev_start + timedelta(days=13)
        add_range("Kerstvakantie", prev_start, prev_end)

        # Krokusvakantie: Easter − 48 days → 1 week
        start = easter - timedelta(days=48)
        end = start + timedelta(days=6)
        add_range("Krokusvakantie", start, end)

        # Zomervakantie: 1 July → 31 August
        start = date(year, 7, 1)
        end = date(year, 8, 31)
        add_range("Zomervakantie", start, end)

        self._add_remembrance_day(tr("Wapenstilstand"))
        self._add_holiday(tr("Dag van de Arbeid"), date(year, 5, 1))
        ascension = self._easter_sunday + timedelta(days=39)

        self._add_holiday(tr("Hemelvaart"), ascension)
        self._add_holiday(tr("Vrijdag na Hemelvaart"), ascension + timedelta(days=1))
        self._add_whit_monday(tr("Pinkstermaandag"))


    # ---------- Wallonia (French + German-speaking schools) ----------
    def _populate_subdiv_wbr_school_holidays(self):
        """
    School holidays for Wallonia (French Community + German-speaking schools).

    Only fixed and well-defined days are implemented.
    Vacation periods are defined yearly by ministerial decree and are
    intentionally left unimplemented.
        """
        year = self._year
        easter = self._easter_sunday

        # Fixed-date holidays
        self._add_holiday(tr("Jour de l'Armistice"), date(year, 11, 11))
        self._add_holiday(tr("Fête du Travail"), date(year, 5, 1))
        self._add_holiday(tr("Fête de la Communauté française"), date(year, 9, 27))

        # Movable holidays
        self._add_easter_monday(tr("Lundi de Pâques"))  
        ascension = easter + timedelta(days=39)
        self._add_holiday(tr("Jeudi de l'Ascension"), ascension)

        pentecost = easter + timedelta(days=50)
        self._add_holiday(tr("Lundi de Pentecôte"), pentecost)
    # NOT IMPLEMENTED:
    # - Vacances d'automne (Toussaint)
    # - Vacances d'hiver (Noël)
    # - Congé de détente (Carnaval)
    # - Vacances de printemps (Pâques)
    # - Vacances d'été
    #
    # These vary each year and are published by official decree.
    def _populate_subdiv_ger_school_holidays(self):
        """
    School holidays for the German-speaking Community (Ostbelgien).

    Dates are published yearly by decree.
    Only fixed and well-defined days are implemented.
    Vacation periods are intentionally left unimplemented.
    """
        year = self._year
        easter = self._easter_sunday

    # Fixed holidays
        self._add_holiday(tr("Tag des Waffenstillstands"), date(year, 11, 11))
        self._add_holiday(tr("Tag der Arbeit"), date(year, 5, 1))
        self._add_holiday(tr("Feiertag der Deutschsprachigen Gemeinschaft"), date(year, 11, 15))

    # Movable Christian holidays
        self._add_easter_monday(tr("Ostermontag"))
        ascension = easter + timedelta(days=39)
        self._add_holiday(tr("Christi Himmelfahrt"), ascension)

        pentecost = easter + timedelta(days=50)
        self._add_holiday(tr("Pfingstmontag"), pentecost)

class BE(Belgium):
    pass


class BEL(Belgium):
    pass
