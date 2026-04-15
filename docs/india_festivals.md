# Indian Festivals (Navratri and Durga Puja)

## Overview

Some Indian festivals are complex to model as global holidays because they:
- Follow a lunisolar calendar
- Vary each year
- May be region-specific
- Can span multiple days

Depending on the festival, they are modeled via dedicated calendar hooks or subdivision-specific holiday definitions.

---

## Navratri

- Multi-day Hindu festival (typically 9 days)
- Date varies annually
- Observed across multiple Indian states

### Implementation Notes

- Not a fixed-date holiday
- Implemented using Hindu calendar-based date computation (via _add_sharad_navratri)
---

## Durga Puja

- Multi-day festival (Saptami–Dashami)
- Primarily observed in eastern India

### Implementation Notes

- Regional festival
- May overlap with Navratri
- Typically represented by key observed days (e.g., Ashtami or Dashami)
- Represented through related Hindu calendar observances (e.g., Saptami, Ashtami, Navami, Dussehra)
---

## Summary

- Added using the Hindu calendar holiday hook in the India implementation
- Other regional or local festivals are better suited for subdivision-level implementation
- Special handling is required due to variable dates
