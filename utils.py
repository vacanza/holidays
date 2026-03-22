from datetime import date

def get_holidays_in_range(holidays_obj, start_date, end_date):
    """
    Returns holidays between start_date and end_date
    """

    result = {}

    for day, name in holidays_obj.items():
        if start_date <= day <= end_date:
            result[day] = name

    return result