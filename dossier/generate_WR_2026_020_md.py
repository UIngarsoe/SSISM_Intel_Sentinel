# generate_WR_2026_020_md.py

content = """---
title: "SSISM Intelligence Dossier – WR-2026-020"
author: "SSISM Analytical Intelligence Unit (U Ingar Soe)"
date: "2026-04-21"
version: "1.0"
category: "Security Sector Analysis / Surveillance State Evolution"
tags: ["Military Intelligence", "PSMS", "Surveillance Technology", "Air Power", "Command Transition"]
status: "PUBLIC / OSINT BRIEFING"
---

# SSISM Intelligence Dossier – WR-2026-020  
## The First 20 Days of Gen. Ye Win Oo: Intelligence Doctrine, Surveillance Expansion, and the Continuity of Air Power Strategy

**Date:** 21 April 2026

---

## Executive Summary

On 30 March 2026, Gen. Ye Win Oo assumed the role of Commander-in-Chief of Defence Services, succeeding Min Aung Hlaing. This marked the first time a former head of Military Security Affairs (MSA) rose to lead the entire armed forces.

The first twenty days of his tenure reveal a pattern consistent with an intelligence-driven command philosophy:

- Expansion and more visible use of technology-based surveillance systems (PSMS)
- Increased scrutiny of civilians interacting with politically sensitive figures
- Continuity—not escalation—of existing air power strategy

This period does not show evidence of a sudden spike in airstrikes. Instead, it shows the elevation of intelligence doctrine to the center of military governance.

---

## 1. Why This Appointment Matters

Ye Win Oo previously led Military Security Affairs (MSA), responsible for:

- Monitoring dissidents and political actors
- Intelligence coordination
- Detention and interrogation oversight
- Internal surveillance networks

His rise signals a doctrinal shift from battlefield command culture to intelligence-centric control culture.

---

## 2. Expansion of PSMS and Monitoring Systems

Early April reports from monitoring groups and rights observers indicate intensified PSMS use at:

- Checkpoints
- Administrative offices
- Hotels and transit points
- Locations visited by politically sensitive individuals

PSMS combines facial recognition, biometrics, database matching, and phone inspection.

This aligns directly with an intelligence-command background.

**Assessment:** Surveillance tightening is the first operational signature.

---

## 3. Surveillance Before Force

The emerging pattern is:

Identify → Track → Document → Arrest selectively.

A classic intelligence doctrine minimizing visibility while maximizing control.

---

## 4. Airstrikes: Continuity, Not Escalation

No verified evidence shows increased airstrikes due to the command transition.

Air operations established in 2025–2026 continue unchanged, documented by Amnesty International, Fortify Rights, and The Irrawaddy.

What changed is intelligence capacity behind the air campaign.

---

## 5. Emerging Command Model

| Previous Pattern | Emerging Pattern |
|------------------|------------------|
| Visible troop presence | Invisible surveillance net |
| Mass arrest sweeps | Targeted monitoring |
| Battlefield focus | Population intelligence focus |
| Reactive repression | Data-driven repression |

---

## Conclusion

The first twenty days under Gen. Ye Win Oo reveal the normalization of intelligence doctrine at the top of Myanmar’s military structure.

Airstrikes continue as before.  
Surveillance is what has intensified.

The risk ahead is quieter, data-driven control.

---

End of Report  
SSISM Analytical Archive
"""

filename = "WR-2026-020_Ye-Win-Oo_Intelligence-Doctrine_PSNS_Surveillance.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"{filename} created successfully.")
