from datetime import date
import holidays
from hijri_converter import Gregorian

def get_gambia_holidays(year):
    gambia_holidays = {}
    try:
        gm_holidays = holidays.GM(years=year)
        gambia_holidays.update(gm_holidays)
    except KeyError:
        gambia_holidays.update(_get_manual_gambia_holidays(year))
    except Exception as e:
        print(f"Error retrieving holidays for {year}: {e}")
        gambia_holidays.update(_get_manual_gambia_holidays(year))
    return gambia_holidays

def _get_manual_gambia_holidays(year):
    manual_holidays = {}
    manual_holidays[date(year, 1, 1)] = "New Year's Day"
    manual_holidays[date(year, 2, 18)] = "Independence Day"
    manual_holidays[date(year, 5, 1)] = "Labour Day"
    manual_holidays[date(year, 5, 25)] = "Africa Day"
    manual_holidays[date(year, 7, 22)] = "Revolution Day"
    manual_holidays[date(year, 8, 15)] = "Assumption of Mary"
    manual_holidays[date(year, 12, 25)] = "Christmas Day"

    # Calculate approximate Christian movable holidays (simplified)
    easter_sunday = _calculate_easter(year)
    if easter_sunday:
        manual_holidays[easter_sunday - timedelta(days=2)] = "Good Friday (Approximate)"
        manual_holidays[easter_sunday + timedelta(days=1)] = "Easter Monday (Approximate)"

    # Calculate approximate Islamic holidays (using hijri-converter)
    try:
        if year >= 2000:
            # Approximate dates based on common patterns and estimations
            # Note: Actual dates depend on moon sighting.
            hijri_year_start = Gregorian(year, 1, 1).to_hijri().year
            # Eid al-Fitr (end of Ramadan) - roughly 9th/10th month
            gregorian_eid_fitr = Gregorian(hijri_year_start + (year - 2000), 10, 1).to_gregorian()
            manual_holidays[gregorian_eid_fitr] = "Eid al-Fitr (Approximate)"

            # Eid al-Adha (Feast of Sacrifice) - roughly 12th month, 10th day
            gregorian_eid_adha = Gregorian(hijri_year_start + (year - 2000), 12, 10).to_gregorian()
            manual_holidays[gregorian_eid_adha] = "Eid al-Adha (Approximate)"

            # Mawlid (Prophet's Birthday) - roughly 3rd month, 12th day
            gregorian_mawlid = Gregorian(hijri_year_start + (year - 2000), 3, 12).to_gregorian()
            manual_holidays[gregorian_mawlid] = "The Prophet's Birthday (Approximate)"
    except Exception as e:
        print(f"Error calculating Islamic holidays for {year}: {e}")

    return manual_holidays

def _calculate_easter(year):
    """Simplified Easter calculation (Gregorian calendar)."""
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - (b - (b + 8) // 25 + 1) // 3 + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    month = (d + e + 114) // 31
    day = ((d + e + 114) % 31) + 1
    try:
        return date(year, month, day)
    except ValueError:
        return None

if __name__ == "__main__":
    from datetime import timedelta

    start_year = 2025
    end_year = start_year + 30
    all_gambia_holidays = {}

    for year in range(start_year, end_year):
        gambia_holidays = get_gambia_holidays(year)
        if gambia_holidays:
            print(f"\nPublic Holidays in The Gambia for {year}:")
            for date_obj, name in sorted(gambia_holidays.items()):
                print(f"{date_obj}: {name}")
            all_gambia_holidays.update(gambia_holidays)
        else:
            print(f"\nCould not retrieve specific holiday data for {year}.")

    print("\n--- Important Notes ---")
    print("1. The 'holidays' library may not fully support Gambia for all years.")
    print("2. Dates for Islamic holidays are subject to moon sighting and can vary by a day or two.")
    print("3. Dates for Christian movable holidays (Good Friday, Easter Monday) are approximate calculations.")
    print("4. For precise dates, especially for religious holidays, consult official Gambian government announcements and reliable religious calendars for each specific year.")