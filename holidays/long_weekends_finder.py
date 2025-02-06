import holidays
from datetime import timedelta, date

def find_long_weekends(year, country, month):
    """
    Finds long weekends for a given year, country, and month.
    
    A long weekend is defined as a holiday adjacent to a weekend.
    
    Parameters:
    - year (int): The year to check (1900–2100).
    - country (str): The country code (e.g., 'IN', 'US').
    - month (int): The month to check (1-12).

    Returns:
    - List of dictionaries containing start date, end date, duration, and holiday names.
    """
    
    # Validate year
    if not isinstance(year, int) or year < 1900 or year > 2100:
        raise ValueError("Invalid year! Please provide an integer between 1900 and 2100.")
    
    # Validate country
    if not isinstance(country, str) or not country.strip():
        raise ValueError("Invalid country! Please provide a valid country code (e.g., 'IN', 'US').")
    
    # Validate month
    if not isinstance(month, int) or month < 1 or month > 12:
        raise ValueError("Invalid month! Please provide an integer between 1 and 12.")

    # Fetch holidays for the given year and country
    try:
        holiday_list = holidays.CountryHoliday(country, years=year)
    except Exception as e:
        raise ValueError(f"Error fetching holidays: {e}")

    # Filter holidays for the given month
    holiday_list = {d: name for d, name in holiday_list.items() if d.month == month}
    
    if not holiday_list:
        return []  # No long weekends in the given month

    long_weekends = []

    # Determine the country's weekend days (default: Saturday & Sunday)
    weekend_days = {5, 6}  # Saturday-Sunday
    if hasattr(holidays, "weekend") and country in holidays.weekend:
        weekend_days = set(holidays.weekend[country])

    # Process each holiday
    for holiday_date, holiday_name in holiday_list.items():
        start_date, end_date = holiday_date, holiday_date
        holidays_involved = [holiday_name]

        # Extend backward if there's a preceding weekend
        while (start_date - timedelta(days=1)).weekday() in weekend_days or (start_date - timedelta(days=1)) in holiday_list:
            start_date -= timedelta(days=1)
            if start_date in holiday_list and start_date != holiday_date:
                holidays_involved.insert(0, holiday_list[start_date])  # Add earlier holidays

        # Extend forward if there's a following weekend
        while (end_date + timedelta(days=1)).weekday() in weekend_days or (end_date + timedelta(days=1)) in holiday_list:
            end_date += timedelta(days=1)
            if end_date in holiday_list and end_date != holiday_date:
                holidays_involved.append(holiday_list[end_date])  # Add later holidays

        # Avoid duplicates
        long_weekend_entry = {
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'duration': (end_date - start_date).days + 1,
            'holidays': holidays_involved
        }
        
        if long_weekend_entry not in long_weekends:
            long_weekends.append(long_weekend_entry)

    return long_weekends
