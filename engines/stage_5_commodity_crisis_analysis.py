#!/usr/bin/env python3
"""
SSISM / TAIE Module - Stage 5: Commodity Price Inflation & Social Media Sentiment Analysis
Author: Technical Research & Civic Intelligence Unit
License: AGPL-3.0 / Open Source System Integration

Description:
    Processes citizen feedback, social media discourse, and price variance metrics 
    surrounding chronic commodity inflation and economic burdens in Myanmar.
"""

import json
import math
import sys
from datetime import datetime
from typing import Dict, List, Any


class CommodityCrisisAnalyzer:
    """
    Core engine to evaluate economic distress metrics, social media debate vectors,
    and public sentiment parity across diverse socio-economic groups.
    """

    def __init__(self, target_currency: str = "MMK"):
        self.target_currency = target_currency
        self.timestamp = datetime.utcnow().isoformat() + "Z"

    def calculate_price_burden_index(self, basket: Dict[str, float], baseline: Dict[str, float]) -> float:
        """
        Calculates normalized economic distress index using Weighted Logarithmic Price Variance.
        Formula:
            Burden Index = SUM( w_i * ln( P_current_i / P_baseline_i ) )
        """
        total_burden = 0.0
        weights = {
            "rice": 0.35,
            "cooking_oil": 0.25,
            "fuel": 0.20,
            "medicine": 0.10,
            "transport": 0.10
        }

        for item, price in basket.items():
            base_price = baseline.get(item, 1.0)
            weight = weights.get(item, 0.10)
            if base_price > 0 and price > 0:
                ratio = price / base_price
                total_burden += weight * math.log(ratio)

        # Scale to 0 - 100 Index
        distress_score = min(100.0, max(0.0, total_burden * 25.0))
        return round(distress_score, 2)

    def analyze_social_media_consensus(self, comments_dataset: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Analyzes multi-factional social media comments to determine core consensus points.
        Evaluates how opposing political factions express identical underlying economic pain.
        """
        total_comments = len(comments_dataset)
        if total_comments == 0:
            return {"status": "NO_DATA"}

        price_outcry_count = 0
        shared_consensus_count = 0

        keywords_price = ["စျေးတက်", "အခက်အခဲ", "မဝယ်နိုင်", "မမျှော်လင့်နိုင်", "ကုန်စျေးနှုန်း", "ငွေကြေး"]
        keywords_shared_pain = ["အားလုံး", "ဘယ်ဘက်မှ", "တူတူဘဲ", "ဒုက္ခ", "မလွယ်ဘူး"]

        for comment in comments_dataset:
            text = comment.get("text", "")
            if any(kw in text for kw in keywords_price):
                price_outcry_count += 1
            if any(kw in text for kw in keywords_shared_pain):
                shared_consensus_count += 1

        return {
            "total_analyzed": total_comments,
            "price_outcry_ratio": round(price_outcry_count / total_comments, 2),
            "cross_faction_consensus_ratio": round(shared_consensus_count / total_comments, 2),
            "dominant_theme": "Universal Household Economic Strain across all demographics."
        }

    def generate_stage_5_report(self, price_data: Dict[str, float], baseline_data: Dict[str, float], comments: List[Dict[str, str]]) -> Dict[str, Any]:
        distress_score = self.calculate_price_burden_index(price_data, baseline_data)
        consensus = self.analyze_social_media_consensus(comments)

        return {
            "engine_stage": "Stage 5 - Commodity Crisis & Social Reality Synthesizer",
            "execution_timestamp": self.timestamp,
            "metrics": {
                "economic_burden_index": distress_score,
                "distress_level": "CRITICAL" if distress_score > 50 else "MODERATE",
            },
            "discourse_analysis": consensus,
            "system_conclusion": (
                "Despite polarization in social media debates, online commentary converges "
                "on a singular operational reality: unprecedented commodity price escalation "
                "imposes an unsustainable burden across all population sectors."
            )
        }


def main():
    # Sample baseline (historical) vs current local prices in MMK
    baseline_prices = {"rice": 45000, "cooking_oil": 6000, "fuel": 1800, "medicine": 2500, "transport": 1000}
    current_prices = {"rice": 135000, "cooking_oil": 18500, "fuel": 4800, "medicine": 8500, "transport": 3500}

    sample_comments = [
        {"user_id": "u1", "text": "ကုန်စျေးနှုန်းတွေက အဆမတန် တက်လွန်းလို့ ဝယ်မစားနိုင်တော့ဘူး။ ဘယ်လိုမှ မလွယ်ဘူး။"},
        {"user_id": "u2", "text": "ဘက်ပေါင်းစုံက လူတွေအားလုံး တူတူဘဲ ဒုက္ခရောက်နေကြတာ။ စျေးတွေက အနိမ့်ဆုံး မရှိတော့ဘူး။"},
        {"user_id": "u3", "text": "ဆီစျေး၊ ဆန်စျေးတွေက စံချိန်တင်အောင် တက်နေတယ်။ အခြေခံလူတန်းစားတင် မဟုတ်ဘူး အားလုံး ခက်ခဲနေတာ။"},
        {"user_id": "u4", "text": "အွန်လိုင်းမှာ ဘာပဲငြင်းကြငြင်းကြ၊ အပြင်မှာ စျေးဝယ်ရင် အားလုံး ခင်းဗျာ တူတူဘဲ ညည်းနေကြတာ။"}
    ]

    analyzer = CommodityCrisisAnalyzer()
    report = analyzer.generate_stage_5_report(current_prices, baseline_prices, sample_comments)

    print(json.dumps(report, indent=2, ensure-ascii=False))


if __name__ == "__main__":
    main()
