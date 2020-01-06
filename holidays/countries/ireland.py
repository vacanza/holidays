from holidays.holiday_base import HolidayBase
from .united_kingdom import UnitedKingdom


class Ireland(UnitedKingdom):

    def __init__(self, **kwargs):
        self.country = 'Ireland'
        HolidayBase.__init__(self, **kwargs)


class IE(Ireland):
    pass
