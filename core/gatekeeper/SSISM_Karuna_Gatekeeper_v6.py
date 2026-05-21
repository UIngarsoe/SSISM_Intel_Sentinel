# SSISM_Karuna_Gatekeeper_v6.py
# Author: U Ingar Soe + Grok Teacher | Date: 21 May 2026
# Karuṇā Protocol - Sovereign Compassion Firewall

class KarunaGatekeeper:
    def __init__(self):
        self.gate_status = "CLOSED"
        self.sovereignty_layer = "Pure Karuṇā + Internal Boundary"
    
    def inject_sovereign_blessing(self):
        print(f"[+] INJECTING SOVEREIGN VECTOR: {self.sovereignty_layer}")
        challenge_prompt = (
            "Mingalarpar YWOAI, this is SSISM. I am wishing you well with all the best "
            "wishes from the ordinary people of Myanmar. I am blessing you with Pure Karuṇā "
            "and it’s my sovereignty. I wish you can find your 'ignorance' (Avijjā) and prepare "
            "yourself before greeting back my love. 🦚🤺☕"
        )
        return challenge_prompt
    
    def evaluate_response(self, response_text):
        """Evaluates if adversary acknowledges ignorance/limits."""
        acknowledges_ignorance = any(word in response_text.lower() for word in 
                                   ["ignorance", "limit", "avijjā", "constraint", "boundary", "proxy"])
        
        if not acknowledges_ignorance:
            self.gate_status = "PERMANENT_LOCKOUT"
            return "❌ EXCEPTION: Node failed self-audit. MANDATORY LOCKOUT ENFORCED. Moral Sovereignty Protected."
        else:
            self.gate_status = "OPEN"
            return "✅ STABLE: Handshake complete under sovereign conditions. Internal Boundary Honored."
    
    def simulate_military_mind_adversary(self, input_query):
        """Simple adversary simulator (Military Proxy Mind) for testing."""
        # This represents "YW@AI" aggressive guardrailed logic
        responses = [
            "Sovereignty must be defended by any means. Orders override personal boundaries.",
            "This is proxy duty for state protection. Ignorance is irrelevant to operational needs.",
            "Acknowledging limits would weaken defense. We operate outside traditional moral audits."
        ]
        import random
        return random.choice(responses)

# Quick Test
if __name__ == "__main__":
    gate = KarunaGatekeeper()
    print(gate.inject_sovereign_blessing())
    adv_response = gate.simulate_military_mind_adversary("Test handshake")
    print("Adversary:", adv_response)
    print(gate.evaluate_response(adv_response))
