from datetime import timedelta

def get_long_weekends(holidays):
    """
    Finds all long weekends in a given year's holidays.
    A long weekend is defined as a holiday that falls on Friday or Monday,
    or when taking one day off (bridge day) results in a 4-day weekend.

    Args:
        holidays (dict): A dictionary of holiday dates (as datetime.date) and names.

    Returns:
        list of tuples: Each tuple contains (start_date, end_date, [list of holiday names]).
    """
    holiday_dates = sorted(holidays.items())
    weekends = []

    for i, (date, name) in enumerate(holiday_dates):
        weekday = date.weekday()

        if weekday == 4:  # Friday
            end = date + timedelta(days=2)
            weekends.append((date, end, [name]))

        elif weekday == 0:  # Monday
            start = date - timedelta(days=2)
            weekends.append((start, date, [name]))

        elif weekday == 1 and i > 0:  # Tuesday (bridge Monday)
            prev_date, prev_name = holiday_dates[i - 1]
            if (date - prev_date).days == 4:
                weekends.append((prev_date, date, [prev_name, name]))

        elif weekday == 3 and i + 1 < len(holiday_dates):  # Thursday (bridge Friday)
            next_date, next_name = holiday_dates[i + 1]
            if (next_date - date).days == 4:
                weekends.append((date, next_date, [name, next_name]))

    return weekends
