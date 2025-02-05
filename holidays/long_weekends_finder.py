import holidays
from datetime import timedelta, date

def get_long_weekends(country: str, year: int, month: int = None):
    """
    Finds long weekends for a given country and year using the holidays framework.

    :param country: Country code (e.g., 'IN' for India).
    :param year: Year for which to find long weekends.
    :param month: Optional month filter (1 for January, 2 for February, etc.).
    :return: A dictionary containing a list of long weekends.
    :raises ValueError: If input values are invalid.
    """
    
    # Validate inputs
    if not isinstance(country, str) or not country:
        raise ValueError("Country code must be a non-empty string.")
    
    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer.")

    if month is not None:
        if not isinstance(month, int) or not (1 <= month <= 12):
            raise ValueError("Month must be an integer between 1 and 12.")

    try:
        holiday_list = holidays.CountryHoliday(country, years=year)
    except Exception as e:
        raise ValueError(f"Invalid country code or error fetching holidays: {str(e)}")

    if month:
        holiday_list = {date: name for date, name in holiday_list.items() if date.month == month}

    long_weekends = []

    for holiday_date, name in holiday_list.items():
        # Ensure holiday_date is a valid date object
        if not isinstance(holiday_date, date):
            continue

        try:
            # Check for Friday holidays
            if holiday_date.weekday() == 4:  # Friday
                following_monday = holiday_date + timedelta(days=3)
                if following_monday in holiday_list:
                    long_weekends.append({
                        'start_date': holiday_date.strftime('%Y-%m-%d'),
                        'end_date': following_monday.strftime('%Y-%m-%d'),
                        'duration': 4,
                        'holidays': [name, holiday_list[following_monday]],
                    })
                else:
                    long_weekends.append({
                        'start_date': holiday_date.strftime('%Y-%m-%d'),
                        'end_date': (holiday_date + timedelta(days=2)).strftime('%Y-%m-%d'),
                        'duration': 3,
                        'holidays': [name],
                    })

            # Check for Monday holidays
            elif holiday_date.weekday() == 0:  # Monday
                previous_friday = holiday_date - timedelta(days=3)
                if previous_friday in holiday_list:
                    long_weekends.append({
                        'start_date': previous_friday.strftime('%Y-%m-%d'),
                        'end_date': holiday_date.strftime('%Y-%m-%d'),
                        'duration': 4,
                        'holidays': [holiday_list[previous_friday], name],
                    })
                else:
                    long_weekends.append({
                        'start_date': (holiday_date - timedelta(days=2)).strftime('%Y-%m-%d'),
                        'end_date': holiday_date.strftime('%Y-%m-%d'),
                        'duration': 3,
                        'holidays': [name],
                    })

        except Exception as e:
            print(f"Error processing holiday {holiday_date}: {e}")

    return {"long_weekends": long_weekends}
