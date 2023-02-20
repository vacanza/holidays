#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, MAR, MAY, JUL, AUG, NOV
from holidays.holiday_base import HolidayBase


class Morocco(HolidayBase):
    """
    Moroccan holidays
    Note that holidays falling on a sunday is "lost",
    it will not be moved to another day to make up for the collision.

    # Holidays after 2020: the following four moving date holidays whose exact
    # date is announced yearly are estimated (and so denoted):
    # - Eid El Fetr*
    # - Eid El Adha*
    # - 1er Moharram*
    # - Aid al Mawlid Annabawi*
    # *only if hijri-converter library is installed, otherwise a warning is
    #  raised that this holiday is missing. hijri-converter requires
    #  Python >= 3.6
    Primary sources:
    https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Maroc
    https://www.mmsp.gov.ma/fr/pratiques.aspx?id=38
    """

    country = "MA"

    def _populate(self, year):
        super()._populate(year)

        def _add_holiday(dt: date, hol: str) -> None:
            """Only add if in current year; prevents adding holidays across
            years (handles multi-day Islamic holidays that straddle Gregorian
            years).
            """
            if dt.year == year:
                self[dt] = hol

        # New Year's Day
        self[date(year, JAN, 1)] = "Nouvel an - Premier janvier"

        # Independence Manifesto Day post 1944
        if year > 1944:
            self[date(year, JAN, 11)] = (
                "Commémoration de la présentation "
                "du manifeste de l'indépendance"
            )

        # Labor day
        self[date(year, MAY, 1)] = "Fête du Travail"

        # Throne day
        if year > 2000:
            self[date(year, JUL, 30)] = "Fête du Trône"
        elif year > 1962:
            self[date(year, MAR, 3)] = "Fête du Trône"
        else:
            self[date(year, NOV, 18)] = "Fête du Trône"

        # Oued Ed-Dahab Day
        self[date(year, AUG, 14)] = "Journée de Oued Ed-Dahab"

        # Revolution Day
        self[date(year, AUG, 20)] = (
            "Commémoration de la révolution du " "Roi et du peuple"
        )

        # Youth day
        if year > 2000:
            self[date(year, AUG, 21)] = "Fête de la jeunesse"
        else:
            self[date(year, JUL, 9)] = "Fête du Trône"

        # Green March
        if year > 1975:
            self[date(year, NOV, 6)] = "Marche verte"

        # Independance day
        if year > 1956:
            self[date(year, NOV, 18)] = "Fête de l'indépendance"

        # Eid al-Fitr - Feast Festive
        # date of observance is announced yearly, This is an estimate since
        # having the Holiday on Weekend does change the number of days,
        # deceided to leave it since marking a Weekend as a holiday
        # wouldn't do much harm.
        for yr in (year - 1, year):
            for date_obs in _islamic_to_gre(yr, 10, 1):
                hol_date = date_obs
                _add_holiday(hol_date, "Eid al-Fitr")
                _add_holiday(hol_date + td(days=+1), "Eid al-Fitr")

        # Eid al-Adha - Sacrifice Festive
        # date of observance is announced yearly
        for yr in (year - 1, year):
            for date_obs in _islamic_to_gre(yr, 12, 10):
                hol_date = date_obs
                _add_holiday(hol_date, "Eid al-Adha")
                _add_holiday(hol_date + td(days=+1), "Eid al-Adha")

        # Islamic New Year - (hijari_year, 1, 1)
        for date_obs in _islamic_to_gre(year, 1, 1):
            hol_date = date_obs
            self[hol_date] = "1er Moharram"

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        for yr in (year - 1, year):
            for date_obs in _islamic_to_gre(yr, 3, 12):
                hol_date = date_obs
                _add_holiday(hol_date, "Aid al Mawlid Annabawi")
                _add_holiday(hol_date + td(days=+1), "Aid al Mawlid Annabawi")


class MA(Morocco):
    pass


class MOR(Morocco):
    pass
