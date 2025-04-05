from datetime import timedelta

def get_long_weekends(holidays_dict):
    """
    Get all long weekends from a given set of holidays.

    A long weekend is when a holiday falls on a Friday (so Fri-Sat-Sun)
    or on a Monday (Sat-Sun-Mon). This helps people plan better vacations.

    Parameters:
        holidays_dict (dict): Keys are datetime.date, values are holiday names.

    Returns:
        list of tuples: Each tuple contains (start_date, end_date, holiday_name)
    """
    long_weekends = []

    for date, name in holidays_dict.items():
        weekday = date.weekday()

        # Case 1: Friday holiday (weekend = Fri-Sat-Sun)
        if weekday == 4:
            start = date
            end = date + timedelta(days=2)
            long_weekends.append((start, end, name))

        # Case 2: Monday holiday (weekend = Sat-Sun-Mon)
        elif weekday == 0:
            start = date - timedelta(days=2)
            end = date
            long_weekends.append((start, end, name))

    return long_weekends
