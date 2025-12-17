#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSISM DISSEMINATION ENGINE SENTINEL V1 
========================================
Author: SSISM Intelligence Cell (U Ingar Soe)
Date: 17 December 2025
Doctrine: SSISM Stress-Test Framework
Classification: Strategic Analysis – Non-Predictive

Description:
This engine simulates the survivability of political actors in Burma (Myanmar)
under engineered uncertainty. It does not predict a 'winner' but calculates
resilience against specific stress scenarios (Optics, Loyalty, Crisis).

Repository: https://github.com/UIngarsoe/-SSISM_DISSEMINATION_ENGINE_V1
"""

import time
import random
from dataclasses import dataclass
from typing import List, Dict

# --- DOCTRINE CONFIGURATION ---
SYSTEM_VERSION = "Sentinel V1"
MODE = "STRESS_TEST"  # Do not change to "PREDICTION"
DO_NOTHING_VALUE = True  # The strategic value of waiting/pause

class Actor:
    """Defines a political target with structural attributes, not personality."""
    def __init__(self, name: str, role: str, real_power: int, optics: int, loyalty: int, crisis_utility: int):
        self.name = name
        self.role = role
        # Attributes rated 0-10
        self.real_power = real_power       # Command authority
        self.optics = optics               # International/Domestic acceptablity
        self.loyalty = loyalty             # Internal military/party cohesion
        self.crisis_utility = crisis_utility # Usefulness during violent unrest

    def __repr__(self):
        return f"[{self.name} | Role: {self.role}]"

class Scenario:
    """Defines the environmental conditions (Scenario A, B, C)."""
    def __init__(self, name: str, description: str, weights: Dict[str, float]):
        self.name = name
        self.description = description
        self.weights = weights  # Multipliers for actor attributes based on scenario needs

def tactical_pause(duration=1):
    """Simulates the 'Waiting' doctrine. Uncertainty is a signal."""
    if DO_NOTHING_VALUE:
        print(f"   ...Analysing Signal Noise ({duration}s)...")
        time.sleep(duration)

def run_stress_test(actors: List[Actor], scenarios: List[Scenario]):
    """
    Runs the stress matrix.
    Formula: Survivability = (Power*W) + (Optics*W) + (Loyalty*W) + (Crisis*W) - Friction
    """
    print(f"\n⚡ INITIATING SSISM STRESS-TEST PROTOCOL [{SYSTEM_VERSION}] ⚡")
    print("="*60)
    
    for scenario in scenarios:
        tactical_pause(1)
        print(f"\n📂 LOADING SCENARIO: {scenario.name}")
        print(f"   > Context: {scenario.description}")
        print("-" * 60)
        
        results = []
        
        for actor in actors:
            # Calculate Base Resilience
            score = (
                (actor.real_power * scenario.weights['power']) +
                (actor.optics * scenario.weights['optics']) +
                (actor.loyalty * scenario.weights['loyalty']) +
                (actor.crisis_utility * scenario.weights['crisis'])
            )
            
            # Apply "Engineered Uncertainty" (Random Friction Variable +/- 5%)
            friction = random.uniform(0.95, 1.05)
            final_score = round(score * friction, 2)
            
            results.append((actor.name, final_score))

        # Sort by Survivability (High to Low)
        results.sort(key=lambda x: x[1], reverse=True)
        
        for rank, (name, score) in enumerate(results, 1):
            print(f"   {rank}. {name}: {score} Survivability Index")
            
    print("\n" + "="*60)
    print("✅ FINAL ANALYSIS: No winner declared. Survivability metrics stored.")
    print("   REMINDER: Uncertainty is the correct output.")

# --- DATA INGESTION ---

# 1. DEFINE TARGETS (Based on Dossier Dec 17, 2025)
targets = [
    Actor("MAH (Snr Gen)", "Apex Controller", real_power=10, optics=1, loyalty=8, crisis_utility=9),
    Actor("MTO (Gen)", "Stabilizer",      real_power=6,  optics=8, loyalty=9, crisis_utility=7),
    Actor("KY (U)",      "Enforcer",        real_power=5,  optics=2, loyalty=10, crisis_utility=8)
]

# 2. DEFINE SCENARIOS (Weights reflect the environment)
scenarios = [
    Scenario("A: Proxy Presidency", "Formal office absorbs pressure; Optics & Stability prioritized.", 
             weights={'power': 0.5, 'optics': 2.0, 'loyalty': 1.0, 'crisis': 0.5}),
    
    Scenario("B: Party-Front", "Parliamentary optics; Party Loyalty prioritized.", 
             weights={'power': 0.5, 'optics': 1.0, 'loyalty': 2.0, 'crisis': 0.8}),
    
    Scenario("C: Hard Continuity", "Existential threat; Real Power & Crisis Utility prioritized.", 
             weights={'power': 2.0, 'optics': 0.1, 'loyalty': 1.0, 'crisis': 2.0})
]

# --- EXECUTION ---
if __name__ == "__main__":
    run_stress_test(targets, scenarios)
    print("\n[SYSTEM] Uploading to Memory Archive...")
    print(f"[GITHUB] Pushing to {__file__} ... Done.")

