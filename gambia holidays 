from datetime import date
from holidays.holiday_base import HolidayBase


class GM(HolidayBase):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays in The Gambia.

    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_the_Gambia
    - https://www.timeanddate.com/holidays/gambia/
    """

    def __init__(self, **kwargs):
        self.country = "GM"
        self.default_language = "en"
        self.supported_languages = ["en"]
        super().__init__(**kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, 1, 1)] = "New Year's Day"

        # Independence Day
        self[date(year, 2, 18)] = "Independence Day"

        # Good Friday (Date varies)
        if year == 2025:
            self[date(year, 4, 18)] = "Good Friday"
        elif year == 2026:
            self[date(year, 4, 3)] = "Good Friday"
        elif year == 2027:
            self[date(year, 3, 26)] = "Good Friday"
        elif year == 2028:
            self[date(year, 4, 14)] = "Good Friday"
        elif year == 2029:
            self[date(year, 3, 30)] = "Good Friday"
        elif year == 2030:
            self[date(year, 4, 19)] = "Good Friday"
        # Add more years as needed

        # Easter Monday (Date varies)
        if year == 2025:
            self[date(year, 4, 21)] = "Easter Monday"
        elif year == 2026:
            self[date(year, 4, 6)] = "Easter Monday"
        elif year == 2027:
            self[date(year, 3, 29)] = "Easter Monday"
        elif year == 2028:
            self[date(year, 4, 17)] = "Easter Monday"
        elif year == 2029:
            self[date(year, 4, 2)] = "Easter Monday"
        elif year == 2030:
            self[date(year, 4, 22)] = "Easter Monday"
        # Add more years as needed

        # Labour Day
        self[date(year, 5, 1)] = "Labour Day"

        # End of Ramadan (Eid al-Fitr) - Date varies based on the Islamic calendar
        # These dates are based on estimations and may vary slightly.
        # Refer to reliable Islamic calendar sources for precise dates.
        if year == 2025:
            self[date(year, 3, 31)] = "End of Ramadan (Eid al-Fitr)"  # Approximate
        elif year == 2026:
            self[date(year, 3, 20)] = "End of Ramadan (Eid al-Fitr)"  # Approximate
        # Add more years as needed

        # Feast of the Sacrifice (Eid al-Adha) - Date varies based on the Islamic calendar
        # These dates are based on estimations and may vary slightly.
        # Refer to reliable Islamic calendar sources for precise dates.
        if year == 2025:
            self[date(year, 6, 9)] = "Feast of the Sacrifice (Eid al-Adha)"  # Approximate
        elif year == 2026:
            self[date(year, 5, 29)] = "Feast of the Sacrifice (Eid al-Adha)"  # Approximate
        # Add more years as needed

        # Prophet's Birthday (Mawlid al-Nabi) - Date varies based on the Islamic calendar
        # These dates are based on estimations and may vary slightly.
        # Refer to reliable Islamic calendar sources for precise dates.
        if year == 2025:
            self[date(year, 1, 29)] = "Prophet's Birthday (Mawlid al-Nabi)"  # Approximate
        elif year == 2026:
            self[date(year, 1, 19)] = "Prophet's Birthday (Mawlid al-Nabi)"  # Approximate
        # Add more years as needed

        # Christmas Day
        self[date(year, 12, 25)] = "Christmas Day"


if __name__ == "__main__":
    gm_holidays = GM(years=2025)
    print(gm_holidays)