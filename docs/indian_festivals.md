# Hindu Festivals in India (Navratri and Durga Puja)

This document describes the handling of major Hindu festivals such as Navratri and Durga Puja in this library.

---

## 1. Overview

Some Indian festivals are not fixed-date national holidays. Instead, they:

- Vary each year based on the lunar calendar
- Are observed differently across states
- Span multiple days

Because of this, they are not included as universal holidays for all regions.

---

## 2. Navratri

Navratri is a 9-day Hindu festival dedicated to Goddess Durga.

### Key Characteristics:
- Based on the lunar calendar
- Occurs twice a year (Chaitra Navratri and Sharad Navratri, though Sharad Navratri is more widely observed)
- Spans multiple days (typically 9)

### Regional Observance:
Navratri is widely observed in:

- Gujarat
- Maharashtra
- Uttar Pradesh
- Rajasthan
- Madhya Pradesh
- Karnataka
- Delhi

### Implementation Notes:
- In this library, Navratri is treated as a festival-based holiday
- It is included only in relevant subdivisions
- Typically represented using a starting date or computed via festival logic

---

## 3. Durga Puja

Durga Puja is a major Hindu festival celebrating the victory of Goddess Durga over Mahishasura.

### Key Characteristics:
- Occurs during Navratri (last 4–5 days)
- Includes Saptami, Ashtami, Navami, and Dashami
- Multi-day festival

### Regional Observance:
Primarily celebrated in:

- West Bengal
- Assam
- Odisha
- Tripura

### Implementation Notes:
- Treated as a regional multi-day festival
- Often aligned with Navratri but represented separately due to cultural significance
- Included only in relevant subdivisions

---

## 4. Why These Holidays Are Not Global

These festivals are not added as universal holidays because:

- They are not uniformly observed across all states
- Their dates vary yearly
- They may have different regional interpretations
- They span multiple days rather than a single fixed date

---

## 5. Summary

- Navratri and Durga Puja are implemented as regional festival-based holidays
- They are added only to relevant subdivisions
- Their dates depend on the lunar calendar
- Multi-day nature requires special handling compared to fixed-date holidays