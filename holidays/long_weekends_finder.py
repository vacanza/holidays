from datetime import timedelta
import holidays
import calendar

def find_long_weekends(country, year, month=None, language=None, exact_range=False):
    # Validate year
    if not isinstance(year, int) or not (1900 <= year <= 2100):
        raise ValueError("Invalid year provided. Year must be an integer between 1900 and 2100.")

    # Validate country (ensure it's a valid country code supported by the holidays library)
    try:
        holiday_obj = holidays.country_holidays(country, years=year, language=language)
    except Exception as e:
        raise ValueError(f"Error fetching holidays: {e}")

    # Validate month (if provided)
    if month is not None and (month < 1 or month > 12):
        raise ValueError("Invalid month provided. Month must be between 1 and 12.")

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

        # Extend backward to find preceding weekends or holidays
        prev_day = start_date - timedelta(days=1)
        while prev_day in holidays_filtered or (
            prev_day.weekday() in weekends and prev_day.weekday() not in working_weekend_days
        ):
            if prev_day in holidays_filtered:
                holidays_involved.insert(0, holidays_filtered[prev_day])
            start_date = prev_day
            seen_dates.add(prev_day)
            prev_day -= timedelta(days=1)

        # Extend forward to find succeeding weekends or holidays
        next_day = end_date + timedelta(days=1)
        while next_day in holidays_filtered or (
            next_day.weekday() in weekends and next_day.weekday() not in working_weekend_days
        ):
            if next_day in holidays_filtered:
                holidays_involved.append(holidays_filtered[next_day])
            end_date = next_day
            seen_dates.add(next_day)
            next_day += timedelta(days=1)

        # Ensure only actual long weekends (3+ days) are considered
        duration = (end_date - start_date).days + 1
        if duration >= 3:
            if exact_range and month is not None:
                # Adjust start_date and end_date to fit within the month
                start_date = max(start_date, holiday_date.replace(month=month, day=1))
                last_day_of_month = calendar.monthrange(year, month)[1]
                end_date = min(end_date, holiday_date.replace(month=month, day=last_day_of_month))

                # Recalculate duration after adjustment
                duration = (end_date - start_date).days + 1

            # Ensure that the final duration is still a long weekend (3+ days)
            if duration >= 3:
                long_weekends.append(
                    {
                        "start_date": start_date.strftime("%Y-%m-%d"),
                        "end_date": end_date.strftime("%Y-%m-%d"),
                        "duration": duration,
                        "holidays": holidays_involved,
                    }
                )

        seen_dates.add(holiday_date)

    return long_weekends
