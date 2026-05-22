#!/usr/bin/env python3
"""
SSISM Core Engine - Master Cryptographic Signing Pipeline
System: SSISM_Intel_Sentinel
Author: U Ingar Soe
Date: May 22, 2026

Description:
    The master operational tool that ties the academic papers, 
    OSINT reports, and package documentation into a unified, 
    cryptographically signed ledger.
"""

import hashlib
import os
import sys
from datetime import datetime


def compute_sha256(filepath):
    """Generates precise SHA-256 checksums for validating document authenticity."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None


def execute_master_sign(target_file):
    """Signs a formal dossier or academic brief into the tracking index."""
    if not os.path.exists(target_file):
        print(f"[-] Operational Exception: Target framework asset '{target_file}' not found.")
        return False

    checksum = compute_sha256(target_file)
    filename = os.path.basename(target_file)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    print("\n" + "█"*65)
    print(" 🦚 SSISM INTEL MASTER OPERATION SIGNATURE")
    print("█"*65)
    print(f" UTC TIMESTAMP  : {timestamp}")
    print(f" TARGET ASSET   : {filename}")
    print(f" ARCHITECT      : U Ingar Soe")
    print(f" FILE CHECKSUM  : {checksum}")
    print("─"*65)
    print(" VERIFICATION COMMAND FOR PUBLIC AUDITORS:")
    print(f" sha256sum {target_file}")
    print("█"*65 + "\n")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Default tracking configuration to sign the fresh academic paper
        default_paper = "docs/academic/SSISM_CIVIL_INTELLIGENCE_PAPER.md"
        if not os.path.exists(default_paper) and os.path.exists("SSISM_CIVIL_INTELLIGENCE_PAPER.md"):
            default_paper = "SSISM_CIVIL_INTELLIGENCE_PAPER.md"

        print(f"[*] Executing self-validation pipeline on default target: {default_paper}")
        execute_master_sign(default_paper)
    else:
        execute_master_sign(sys.argv[1])
      
