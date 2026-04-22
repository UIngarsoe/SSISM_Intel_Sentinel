# generate_WR_2026_020_v2_md.py

content = """---
title: "SSISM Intelligence Dossier – WR-2026-020 (Updated)"
author: "SSISM Analytical Intelligence Unit (U Ingar Soe)"
date: "2026-04-21"
version: "2.0"
category: "Security Sector Analysis / Intelligence-State Evolution"
tags: ["NDSC", "Military Intelligence", "PSMS", "Surveillance State", "Command Doctrine"]
status: "PUBLIC / OSINT BRIEFING"
---

# SSISM Intelligence Dossier – WR-2026-020 (Updated)
## From Military Intelligence to State Governance: What the 21 April NDSC Meeting Reveals

**Date:** 21 April 2026

---

## Executive Summary

On 30 March 2026, Gen. Ye Win Oo became Commander-in-Chief — the first former Military Security Affairs chief to hold the role.

On 21 April 2026, the first National Defence and Security Council (NDSC) meeting of the new government was held in Naypyidaw.

The agenda discussed at this meeting reveals something critical:

> Intelligence doctrine is no longer confined to the military.  
> It is now shaping state governance priorities.

Peace process management, fuel crisis control, anti-corruption enforcement, ASEAN cooperation, and police coordination were all discussed under a security framing.

This confirms the analytical assessment from the first 20 days: surveillance, monitoring, and intelligence-led control are becoming the core operating logic of the state.

---

## 1. Why the NDSC Meeting Matters

The attendees included the President, Vice Presidents, Speakers of both Hluttaws, Commander-in-Chief, Deputy Commander-in-Chief, and key ministers.

The topics officially discussed:

- Peace process
- Economic management
- Police and administrative “clean governance”
- ASEAN cooperation
- Fuel crisis

These are normally civilian governance topics.

They were discussed inside the NDSC — a security body.

---

## 2. Intelligence Framing of Civilian Issues

Each topic aligns with intelligence priorities:

| Topic | Intelligence Interpretation |
|------|-----------------------------|
| Peace process | Monitoring EAOs and political actors |
| Economic issues | Control of supply chains and movement |
| Police & admin anti-corruption | Internal discipline & data control |
| ASEAN cooperation | Diplomatic narrative management |
| Fuel crisis | Population movement & logistics tracking |

This is governance through a security lens.

---

## 3. PSMS and Surveillance Context

Reports from early April show increased PSMS use at checkpoints, offices, hotels, and politically sensitive locations.

The NDSC discussion of police and administration links directly with this surveillance expansion.

Surveillance is becoming administrative routine.

---

## 4. Air Power: Still Continuity

No evidence shows increased airstrikes due to leadership change.

What changed is the intelligence layer behind operations.

---

## 5. Emerging Model: Intelligence-State

| Past Military Model | Emerging Intelligence-State Model |
|---------------------|-----------------------------------|
| Troop visibility | Data visibility |
| Arrest sweeps | Monitored targeting |
| Battlefield focus | Population data focus |
| Reaction | Anticipation |

---

## Conclusion

The first 20 days showed surveillance expansion.

The 21 April NDSC meeting shows why.

Intelligence doctrine is now guiding how the state thinks about peace, economy, policing, diplomacy, and logistics.

This is the evolution from a military state to an intelligence-state.

---

End of Report  
SSISM Analytical Archive
"""

filename = "WR-2026-020_Ye-Win-Oo_Intelligence-State_NDSC_Update.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"{filename} created successfully.")
