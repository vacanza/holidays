from holidays.constants import JAN, JUL, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import IslamicHolidays, InternationalHolidays


class Algeria(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Algeria
    """

    country = "DZ"

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Amazigh New Year / Yennayer
        # In January 2018, Algeria declared Yennayer a national holiday
        if year >= 2018:
            self._add_holiday("Amazigh New Year", JAN, 12)

        # Labour Day
        self._add_labor_day("Labour Day")

        # Independence Day
        if year >= 1962:
            self._add_holiday("Independence Day", JUL, 5)

        # Revolution Day
        if year >= 1963:
            self._add_holiday("Revolution Day", NOV, 1)

        # Islamic New Year
        self._add_islamic_new_year_day("Islamic New Year")

        # Ashura
        self._add_ashura_day("Ashura Day")

        # Mawlid / Prophet's Birthday
        self._add_mawlid_day("Prophet's Birthday")

        # As of April 30, 2023. Algeria has 3 days of Eid holidays
        # (https://www.horizons.dz/english/archives/amp/12021)
        # Eid al-Fitr - Feast Festive
        self._add_eid_al_fitr_day("Eid al-Fitr")
        self._add_eid_al_fitr_day_two("Eid al-Fitr Holiday")
        if year >= 2024:
            self._add_eid_al_fitr_day_three("Eid al-Fitr Holiday")

        # Eid al-Adha - Scarfice Festive
        self._add_eid_al_adha_day("Eid al-Adha")
        self._add_eid_al_adha_day_two("Eid al-Adha Holiday")
        if year >= 2023:
            self._add_eid_al_adha_day_three("Eid al-Adha Holiday")


class DZ(Algeria):
    pass


class DZA(Algeria):
    pass
