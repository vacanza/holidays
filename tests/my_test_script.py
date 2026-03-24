import holidays
import pytest
# Create an India holidays object for Maharashtra
in_holidays = holidays.India(subdiv="MH", years=[2026])

# Check your new holidays
print(in_holidays.get("2026-10-02"))  # Gandhi Jayanti
print(in_holidays.get("2026-03-04"))  # Gudi Padwa
print(in_holidays.get("2026-02-19"))  # Shivaji Maharaj Jayanti