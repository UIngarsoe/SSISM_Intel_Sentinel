#!/usr/bin/env python3
"""
SSISM Intel Sentinel — Stage 4 Master Logic
===========================================

Reality Before Narrative
A transparent evidence-calibration engine for civic intelligence,
research, policy analysis, and multi-LLM human-in-the-loop workflows.

Author: U Ingar Soe
Project: SSISM Intel Sentinel
Stage: 4 — Master Logic / Evidence Validation
License: MIT

CORE RULE
---------
The system must distinguish:

    OBSERVED
    CALCULATED
    SOURCED
    INFERRED
    UNKNOWN

These five states must never be silently merged.

IMPORTANT
---------
UNEXPLAINED RESIDUAL != CORRUPTION
UNEXPLAINED RESIDUAL != THEFT
UNEXPLAINED RESIDUAL = A VALUE REQUIRING FURTHER EVIDENCE

This module is deliberately conservative:
    Claim Size <= Evidence Capacity
    Potentiality != Prediction != Proven Reality
    Metric != Meaning
    Simulation != Field Reality
    Multi-LLM agreement != Independent proof

The engine assists human judgment. It does not replace it.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


# ---------------------------------------------------------------------------
# 1. Evidence states
# ---------------------------------------------------------------------------

class EvidenceState(str, Enum):
    OBSERVED = "OBSERVED"
    CALCULATED = "CALCULATED"
    SOURCED = "SOURCED"
    INFERRED = "INFERRED"
    UNKNOWN = "UNKNOWN"


class VerificationStatus(str, Enum):
    VERIFIED = "VERIFIED"
    SUPPORTED = "SUPPORTED"
    PLAUSIBLE = "PLAUSIBLE"
    UNCONFIRMED = "UNCONFIRMED"
    CONTRADICTED = "CONTRADICTED"
    UNKNOWN = "UNKNOWN"


@dataclass
class EvidenceItem:
    state: EvidenceState
    statement: str
    source: str | None = None
    calculation: str | None = None
    assumptions: list[str] = field(default_factory=list)
    confidence: str | None = None
    notes: str | None = None


@dataclass
class Claim:
    claim_id: str
    claim: str
    status: VerificationStatus = VerificationStatus.UNKNOWN
    evidence: list[EvidenceItem] = field(default_factory=list)
    counterevidence: list[str] = field(default_factory=list)
    unknowns: list[str] = field(default_factory=list)
    human_review: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "claim_id": self.claim_id,
            "claim": self.claim,
            "status": self.status.value,
            "evidence": [asdict(item) | {"state": item.state.value}
                         for item in self.evidence],
            "counterevidence": self.counterevidence,
            "unknowns": self.unknowns,
            "human_review": self.human_review,
        }


# ---------------------------------------------------------------------------
# 2. Core arithmetic
# ---------------------------------------------------------------------------

def convert_currency(amount: float, rate: float) -> float:
    """Return amount * exchange rate."""
    if amount < 0 or rate < 0:
        raise ValueError("Amount and exchange rate must be non-negative.")
    return amount * rate


def price_gap(foreign_price: float, fx_rate: float,
              local_price: float) -> dict[str, float]:
    """
    Compare a foreign retail price with a local displayed price.

    This function does NOT infer the cause of the gap.
    """
    converted = convert_currency(foreign_price, fx_rate)
    gap = local_price - converted
    multiplier = local_price / converted if converted else float("inf")
    implied_fx = local_price / foreign_price if foreign_price else float("inf")

    return {
        "converted_foreign_price": converted,
        "local_price": local_price,
        "gap": gap,
        "multiplier": multiplier,
        "implied_fx_rate": implied_fx,
    }


# ---------------------------------------------------------------------------
# 3. Price decomposition
# ---------------------------------------------------------------------------

@dataclass
class PriceDecomposition:
    base_product_cost: float
    fx_conversion_cost: float = 0.0
    export_import_costs: float = 0.0
    freight: float = 0.0
    insurance: float = 0.0
    customs_duty: float = 0.0
    commercial_tax: float = 0.0
    import_compliance: float = 0.0
    financing_fx_risk: float = 0.0
    warehousing: float = 0.0
    distribution: float = 0.0
    retail_margin: float = 0.0
    warranty_after_sales: float = 0.0
    scarcity_premium: float = 0.0

    @property
    def explained_total(self) -> float:
        values = asdict(self)
        return sum(values.values())

    def unexplained_residual(self, final_retail_price: float) -> float:
        return final_retail_price - self.explained_total

    def report(self, final_retail_price: float) -> dict[str, float]:
        return {
            **asdict(self),
            "explained_total": self.explained_total,
            "final_retail_price": final_retail_price,
            "unexplained_residual": self.unexplained_residual(
                final_retail_price
            ),
        }


# ---------------------------------------------------------------------------
# 4. Claim ledger
# ---------------------------------------------------------------------------

def build_claim_ledger(claims: Iterable[Claim]) -> list[dict[str, Any]]:
    """Serialize claims into a transparent audit-friendly ledger."""
    return [claim.to_dict() for claim in claims]


# ---------------------------------------------------------------------------
# 5. Multi-LLM orchestration rule
# ---------------------------------------------------------------------------

@dataclass
class LLMNodeObservation:
    node: str
    role: str
    finding: str
    evidence_refs: list[str] = field(default_factory=list)


def compare_llm_nodes(nodes: Iterable[LLMNodeObservation]) -> dict[str, Any]:
    """
    Compare LLM observations without treating agreement as proof.

    Agreement can identify convergence.
    It cannot create independent evidence by itself.
    """
    items = list(nodes)
    findings = {}
    for item in items:
        findings.setdefault(item.finding, []).append(item.node)

    return {
        "node_count": len(items),
        "findings": findings,
        "rule": "LLM agreement is convergence, not independent proof.",
        "human_review_required": True,
    }


# ---------------------------------------------------------------------------
# 6. Artifact integrity
# ---------------------------------------------------------------------------

def sha256_file(path: str | Path) -> str:
    """Return SHA-256 for an artifact."""
    p = Path(path)
    digest = hashlib.sha256()
    with p.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_sha256(payload: Any) -> str:
    """Hash canonical JSON for reproducible claim-ledger verification."""
    raw = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


# ---------------------------------------------------------------------------
# 7. Stage 4 validation
# ---------------------------------------------------------------------------

def validate_claim(claim: Claim) -> list[str]:
    """
    Return validation warnings.

    The engine intentionally refuses to upgrade a claim merely because
    it has many sources or many LLMs agreeing with it.
    """
    warnings: list[str] = []

    if not claim.evidence:
        warnings.append("No evidence attached.")

    for item in claim.evidence:
        if item.state == EvidenceState.SOURCED and not item.source:
            warnings.append(
                f"{claim.claim_id}: SOURCED item has no source reference."
            )

        if item.state == EvidenceState.CALCULATED and not item.calculation:
            warnings.append(
                f"{claim.claim_id}: CALCULATED item has no calculation."
            )

        if item.state == EvidenceState.INFERRED and not item.assumptions:
            warnings.append(
                f"{claim.claim_id}: INFERRED item has no explicit assumptions."
            )

    if claim.status == VerificationStatus.VERIFIED and not claim.human_review:
        warnings.append(
            f"{claim.claim_id}: VERIFIED requires explicit human review."
        )

    return warnings


# ---------------------------------------------------------------------------
# 8. Demonstration / self-test
# ---------------------------------------------------------------------------

def self_test() -> dict[str, Any]:
    """
    Deterministic Stage 4 test using a refrigerator-price example.

    The numbers are a test fixture, not a claim about a real product.
    """
    foreign_price = 5800.0
    assumed_fx = 135.0
    local_price = 6_800_000.0

    gap = price_gap(foreign_price, assumed_fx, local_price)

    claim = Claim(
        claim_id="PRICE-001",
        claim="The displayed local price is substantially above the converted "
              "foreign retail price under the stated assumptions.",
        status=VerificationStatus.SUPPORTED,
        evidence=[
            EvidenceItem(
                state=EvidenceState.OBSERVED,
                statement="A displayed local price of MMK 6,800,000 is visible "
                          "in the test fixture.",
            ),
            EvidenceItem(
                state=EvidenceState.CALCULATED,
                statement="THB 5,800 × MMK 135 = MMK 783,000.",
                calculation="5800 * 135 = 783000",
                assumptions=["FX rate is assumed at MMK 135 per THB."],
            ),
        ],
        unknowns=[
            "Exact model equivalence",
            "Capacity and specification equivalence",
            "Origin and landed cost",
            "Freight and insurance",
            "Customs classification and applicable taxes",
            "Warranty and distribution costs",
            "Retail margin",
        ],
        human_review="Stage 4 deterministic self-test.",
    )

    warnings = validate_claim(claim)

    return {
        "test": "SSISM_STAGE4_SELF_TEST",
        "status": "PASS" if not warnings else "WARN",
        "price_gap": gap,
        "claim": claim.to_dict(),
        "warnings": warnings,
        "core_rule": (
            "UNEXPLAINED RESIDUAL != CORRUPTION; "
            "UNEXPLAINED RESIDUAL != THEFT; "
            "it requires further evidence."
        ),
    }


if __name__ == "__main__":
    result = self_test()
    print(json.dumps(result, ensure_ascii=False, indent=2))
