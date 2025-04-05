from holidays.calendars.gregorian import JAN, MAR, MAY, SEP, OCT, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Turkmenistan(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Turkmenistan holidays.
    References:
        https://en.wikipedia.org/wiki/Public_holidays_in_Turkmenistan
        https://www.timeanddate.com/holidays/turkmenistan/
    """

    country = "TM"
    start_year = 1991 

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self) 
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        """Add public holidays for Turkmenistan."""
        if self._year >= 1991:
            self._add_holiday_jan_1("New Year's Day")
            
            self._add_holiday_mar_8("International Women's Day")
            
            if self._year >= 1992:
                self._add_holiday_mar_21("Nowruz (Persian New Year)")
                self._add_holiday_mar_22("Nowruz (Persian New Year)")
            
            if self._year >= 1991:
                self._add_holiday_may_9("Victory Day")
            
            if self._year >= 2018: 
                self._add_holiday_may_18("Constitution and Revival Day")
            elif self._year >= 1992: 
                self._add_holiday_may_18("Revival Day")
            
            if self._year >= 1992:
                if self._year <= 2017:
                    self._add_holiday_oct_27("Independence Day")
                else:
                    self._add_holiday_sep_27("Independence Day")
            
            if self._year >= 2015:  
                self._add_holiday_oct_6("Day of Remembrance")
            
        if self._year >= 2023:
            self._add_holiday_dec_12("Neutrality Day")
        elif self._year >= 2018:
            self._add_holiday_jun_27("Day of Turkmenistan's Neutrality")
        elif self._year >= 1995:
            self._add_holiday_dec_12("Neutrality Day")

        self._add_eid_al_fitr_day("Eid al-Fitr")
        self._add_eid_al_fitr_day_two("Eid al-Fitr")
        self._add_eid_al_fitr_day_three("Eid al-Fitr")
        
        self._add_eid_al_adha_day("Eid al-Adha")
        self._add_eid_al_adha_day_two("Eid al-Adha")
        self._add_eid_al_adha_day_three("Eid al-Adha")

class TM(Turkmenistan):
    pass

class TKM(Turkmenistan):
    pass