"""
SSISM–Steinberg Analytical Engine
Encoding the analytical methodology of David I. Steinberg into SSISM logic.

Purpose:
    Provide a reproducible analytical structure for evaluating Myanmar-related
    reports, narratives, policies, and media through four Steinberg principles:
        1. Contested Legitimacies
        2. Anti-Propaganda / Anti-Binary Filtering
        3. Evidence-Based Pragmatism
        4. Human Outcome Priority
"""


class SteinbergSSISMEngine:

    def __init__(self, text: str):
        self.text = text.lower()

    # ---------------------------------------------------------
    # 1. Multi-Layer Legitimacy Model (MLLM)
    # ---------------------------------------------------------
    def legitimacy_analysis(self):
        legitimacy = {
            "democratic_legal": [],
            "institutional_sovereign": [],
            "traditional_moral": []
        }

        keywords = {
            "democratic_legal": [
                "election", "vote", "human rights", "democracy",
                "civilian government", "constitution"
            ],
            "institutional_sovereign": [
                "sovereignty", "stability", "national unity",
                "security", "defender", "military role"
            ],
            "traditional_moral": [
                "tradition", "religion", "monarchy",
                "merit", "hpoun", "moral authority"
            ]
        }

        for category, words in keywords.items():
            for word in words:
                if word in self.text:
                    legitimacy[category].append(word)

        return legitimacy

    # ---------------------------------------------------------
    # 2. Propaganda / Binary Narrative Filter
    # ---------------------------------------------------------
    def propaganda_filter(self):
        binary_markers = [
            "evil", "pure", "always", "never",
            "good vs bad", "black and white",
            "hero", "villain"
        ]

        found = [w for w in binary_markers if w in self.text]
        return {"binary_markers_found": found}

    # ---------------------------------------------------------
    # 3. Evidence-Weighted Claim Check
    # ---------------------------------------------------------
    def evidence_weighting(self):
        evidence_markers = [
            "data", "evidence", "report", "study",
            "statistics", "survey", "research"
        ]

        score = sum(1 for w in evidence_markers if w in self.text)
        return {"evidence_score": score}

    # ---------------------------------------------------------
    # 4. Human Outcome Priority Function
    # ---------------------------------------------------------
    def human_outcome_priority(self):
        human_markers = [
            "civilian", "people", "livelihood",
            "suffering", "displacement", "poverty",
            "health", "education"
        ]

        hits = [w for w in human_markers if w in self.text]
        return {"human_focus_terms": hits}

    # ---------------------------------------------------------
    # Full SSISM–Steinberg Analysis
    # ---------------------------------------------------------
    def full_analysis(self):
        return {
            "legitimacy_layers": self.legitimacy_analysis(),
            "propaganda_flags": self.propaganda_filter(),
            "evidence_assessment": self.evidence_weighting(),
            "human_priority": self.human_outcome_priority()
        }


# Example usage
if __name__ == "__main__":
    sample_text = """
    The military claims it is the sole defender of national unity and stability,
    while pro-democracy groups cite elections and human rights violations.
    Civilians suffer from poverty and displacement. Reports and studies show
    worsening health and education conditions.
    """

    engine = SteinbergSSISMEngine(sample_text)
    result = engine.full_analysis()

    from pprint import pprint
    pprint(result)
