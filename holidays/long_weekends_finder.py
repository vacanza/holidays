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

import calendar
from datetime import timedelta, date

import holidays


def find_long_weekends(country, year, month=None, language=None, exact_range=False):
    # Validate year
    if not isinstance(year, int) or not (1900 <= year <= 2100):
        raise ValueError("Invalid year provided. Year must be an integer between 1900 and 2100.")

    # Validate country
    try:
        holiday_obj = holidays.country_holidays(country, years=year, language=language)
    except Exception as e:
        raise ValueError(f"Error fetching holidays: {e}")

    # Validate month
    if month is not None and (month < 1 or month > 12):
        raise ValueError("Invalid month provided. Month must be between 1 and 12.")

    weekends = holiday_obj.weekend
    working_weekend_days = getattr(holiday_obj, "weekend_workdays", set())

    # Extend holidays to cover the end of the previous year and start of the next year
    if month is None and not exact_range:
        prev_year_holidays = {
            d: name
            for d, name in holidays.country_holidays(
                country, years=year - 1, language=language
            ).items()
            if d.month == 12
        }
        next_year_holidays = {
            d: name
            for d, name in holidays.country_holidays(
                country, years=year + 1, language=language
            ).items()
            if d.month == 1
        }
        holidays_filtered = {**prev_year_holidays, **holiday_obj, **next_year_holidays}
    else:
        holidays_filtered = {d: name for d, name in holiday_obj.items()}

    if month is not None:
        first_day_of_month = date(year, month, 1)
        last_day_of_month = date(year, month, calendar.monthrange(year, month)[1])

        # Allow spillovers only when exact_range is False
        if not exact_range:
            first_day_of_month -= timedelta(days=2)
            last_day_of_month += timedelta(days=2)

        holidays_filtered = {
            d: name
            for d, name in holidays_filtered.items()
            if first_day_of_month <= d <= last_day_of_month
        }

    long_weekends = []
    seen_dates = set()

    for holiday_date, holiday_name in holidays_filtered.items():
        if holiday_date in seen_dates:
            continue

        start_date, end_date = holiday_date, holiday_date
        holidays_involved = [holiday_name]

        prev_day = start_date - timedelta(days=1)
        while prev_day in holidays_filtered or (
            prev_day.weekday() in weekends and prev_day not in working_weekend_days
        ):
            if prev_day in holidays_filtered:
                holidays_involved.insert(0, holidays_filtered[prev_day])
            start_date = prev_day
            seen_dates.add(prev_day)
            prev_day -= timedelta(days=1)

        next_day = end_date + timedelta(days=1)
        while next_day in holidays_filtered or (
            next_day.weekday() in weekends and next_day.weekday() not in working_weekend_days
        ):
            if next_day in holidays_filtered:
                holidays_involved.append(holidays_filtered[next_day])
            end_date = next_day
            seen_dates.add(next_day)
            next_day += timedelta(days=1)

        duration = (end_date - start_date).days + 1
        if duration >= 3:
            if exact_range and month is not None:
                first_day_of_month = date(year, month, 1)
                last_day_of_month = date(year, month, calendar.monthrange(year, month)[1])

                # Trim the long weekend if it exceeds the month
                start_date = max(start_date, first_day_of_month)
                end_date = min(end_date, last_day_of_month)

                # If after trimming, the duration is less than 3 days, skip it
                if (end_date - start_date).days + 1 < 3:
                    continue

            long_weekends.append(
                {
                    "start_date": start_date,
                    "end_date": end_date,
                    "duration": duration,
                    "holidays": holidays_involved,
                }
            )

        seen_dates.add(holiday_date)

    return long_weekends
