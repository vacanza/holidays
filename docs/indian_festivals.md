# Indian Festivals (Navratri and Durga Puja)

## Overview

Some Indian festivals are not included as global holidays because they:
- Follow a lunisolar calendar
- Vary each year
- Are region-specific
- Span multiple days

These are typically implemented at the subdivision level.

---

## Navratri

- Multi-day Hindu festival (typically 9 days)
- Date varies annually
- Observed across multiple Indian states

### Implementation Notes
- Not a fixed-date holiday
- Should be handled using:
  - Precomputed date mappings, or
  - Festival-based logic
- Recommended to include only in relevant subdivisions

---

## Durga Puja

- Multi-day festival (Saptami–Dashami)
- Primarily observed in eastern India

### Implementation Notes
- Regional festival
- May overlap with Navratri
- Typically represented by key observed days (e.g., Ashtami or Dashami)
- Should be added at subdivision level

---

## Summary

- These festivals are not globally applicable
- Implementation should be subdivision-specific
- Special handling is required due to variable dates