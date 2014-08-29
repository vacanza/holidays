from datetime import date
import holidays

class TestHolidays(holidays.US):
    def _populate(self, year):
        holidays.US._populate(self, year)
        self[date(year, 12, 31)] = "New Year's Eve"

'2014-12-31' in NYSEHolidays()
