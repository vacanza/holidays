from holidays.fuzzy_search import fuzzy_match

def correct_holiday_name(input_name, holidays_list):
    """
    Corrects the input holiday name using fuzzy matching against holidays_list.
    """
    corrected = fuzzy_match(input_name, holidays_list)
    return corrected if corrected else input_name