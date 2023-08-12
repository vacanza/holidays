from holidays.calendars.gregorian import JAN, APR, JUL, AUG, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Barbados(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Barbados
    https://www.timeanddate.com/holidays/barbados/
    """

    country = "BB"

    special_holidays = {
        # One off 50th Anniversary of CARICOM Holiday.
        # See https://tinyurl.com/brbhol
        2023: (JUL, 31, "50th Anniversary of CARICOM Holiday")
    }

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_new_years_day("New Year's Day")

        # Errol Barrow Day
        self._add_holiday("Errol Barrow Day", JAN, 21)

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # National Heroes Day
        self._add_holiday("National Heroes Day", APR, 28)

        # May Day
        self._add_labor_day("May Day")

        # Whit Monday
        self._add_whit_monday("Whit Monday")

        # Emancipation Day
        self._add_holiday("Emancipation Day", AUG, 1)

        # Kadooment Day
        self._add_holiday_1st_mon_of_aug("Kadooment Day")

        # Independence Day
        self._add_holiday("Independence Day", NOV, 30)

        # Christmas
        self._add_christmas_day("Christmas Day")

        # Boxing Day
        self._add_christmas_day_two("Boxing Day")


class BB(Barbados):
    pass


class BRB(Barbados):
    pass
