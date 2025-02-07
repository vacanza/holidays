import holidays
from datetime import timedelta


def find_long_weekends(
    country, year, month=None, language=None, exact_range=False
):
    """
    Finds long weekends for a given country and year.

    A long weekend is a holiday adjacent to a weekend.

    Parameters:
    - country (str): Country code (e.g., 'IN', 'US').
    - year (int): The year to check.
    - month (int, optional): Month to check (1-12). Defaults to None.
    - language (str, optional): Language for holiday names.
    - exact_range (bool, optional): If True, restricts to given month.

    Returns:
    - List of dictionaries with start date, end date, duration, and holidays.
    """

    try:
        holiday_obj = holidays.country_holidays(
            country, years=year, language=language
        )
    except Exception as e:
        raise ValueError(f"Error fetching holidays: {e}")

    weekends = holiday_obj.weekend
    working_weekend_days = getattr(holiday_obj, "weekend_workdays", set())

    holidays_filtered = {
        d: name for d, name in holiday_obj.items() if month is None or d.month == month
    }

    long_weekends = []
    seen_dates = set()

    for holiday_date, holiday_name in holidays_filtered.items():
        if holiday_date in seen_dates:
            continue

        start_date, end_date = holiday_date, holiday_date
        holidays_involved = [holiday_name]

        # Extend backward
        prev_day = start_date - timedelta(days=1)
        while (
            prev_day in holidays_filtered
            or (prev_day.weekday() in weekends and prev_day.weekday() not in working_weekend_days)
        ):
            if prev_day in holidays_filtered:
                holidays_involved.insert(0, holidays_filtered[prev_day])
            start_date = prev_day
            seen_dates.add(prev_day)
            prev_day -= timedelta(days=1)

        # Extend forward
        next_day = end_date + timedelta(days=1)
        while (
            next_day in holidays_filtered
            or (next_day.weekday() in weekends and next_day.weekday() not in working_weekend_days)
        ):
            if next_day in holidays_filtered:
                holidays_involved.append(holidays_filtered[next_day])
            end_date = next_day
            seen_dates.add(next_day)
            next_day += timedelta(days=1)

        if exact_range and (start_date.month != month or end_date.month != month):
            continue

        long_weekends.append(
            {
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "duration": (end_date - start_date).days + 1,
                "holidays": holidays_involved,
            }
        )

        seen_dates.add(holiday_date)

    return long_weekends
