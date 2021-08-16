from datetime import date

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import SAT, SUN
from holidays.constants import JAN, MAR, APR, MAY, DEC
from holidays.holiday_base import HolidayBase

class Namibia(HolidayBase):
    def __init__(self, **kwargs):
        #https://www.officeholidays.com/countries/namibia
        #https://www.timeanddate.com/holidays/namibia/
        self.country = "NA"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        return super()._populate(year)