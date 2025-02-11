#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import timedelta

import holidays


def find_long_weekends(country, year, month=None, language=None, exact_range=False):
    
    # Validate year
    if not isinstance(year, int) or not (1900 <= year <= 2100):
        raise ValueError("Invalid year provided. Year must be an integer between 1900 and 2100.")

    # Validate country (ensure it's a valid country code supported by the holidays library)
    try:
        holiday_obj = holidays.country_holidays(country, years=year, language=language)
    except KeyError:
        raise ValueError(f"Invalid country code: {country}")
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

        # Extend backward
        prev_day = start_date - timedelta(days=1)
        while prev_day in holidays_filtered or (
            prev_day.weekday() in weekends and prev_day.weekday() not in working_weekend_days
        ):
            if prev_day in holidays_filtered:
                holidays_involved.insert(0, holidays_filtered[prev_day])
            start_date = prev_day
            seen_dates.add(prev_day)
            prev_day -= timedelta(days=1)

        # Extend forward
        next_day = end_date + timedelta(days=1)
        while next_day in holidays_filtered or (
            next_day.weekday() in weekends and next_day.weekday() not in working_weekend_days
        ):
            if next_day in holidays_filtered:
                holidays_involved.append(holidays_filtered[next_day])
            end_date = next_day
            seen_dates.add(next_day)
            next_day += timedelta(days=1)

        # Exact range filtering
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
