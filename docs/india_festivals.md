# Indian Festivals (Navratri and Durga Puja)

## Overview

Some Indian festivals are complex to model as global holidays because they:
- Follow a lunisolar calendar
- Vary each year
- May be region-specific
- Can span multiple days

Depending on the festival, they may be implemented either as optional holidays or at the subdivision level.

---

## Navratri

- Multi-day Hindu festival (typically 9 days)
- Date varies annually
- Observed across multiple Indian states

### Implementation Notes

- Not a fixed-date holiday
- Handled using Hindu calendar-based date computation (via _add_sharad_navratri)
- Available as an optional holiday in the current implementation

---

## Durga Puja

- Multi-day festival (Saptami–Dashami)
- Primarily observed in eastern India

### Implementation Notes

- Regional festival
- May overlap with Navratri
- Typically represented by key observed days (e.g., Ashtami or Dashami)
- Generally implemented at the subdivision level

---

## Summary

- Some festivals may be available as optional holidays
- Others are better suited for subdivision-level implementation
- Special handling is required due to variable dates