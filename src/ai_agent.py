import os
import json

class SecurityAgent:
    def __init__(self):
        self.known_safe_programs = {
            "11111111111111111111111111111111": "System Program",
            "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA": "SPL Token Program",
            "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL": "Associated Token Account Program"
        }

    def analyze_simulation(self, simulation_result: dict, raw_payload: dict = None) -> dict:
        result = simulation_result.get("result", {}).get("value", {})
        err = result.get("err")
        logs = result.get("logs", [])
        units_consumed = result.get("unitsConsumed", 0)

        risk_score = 0
        risk_factors = []
        explanation = []

        if err is not None:
            risk_score += 40
            risk_factors.append("TRANSACTION_SIMULATION_FAILED")
            explanation.append(f"Transaction execution would fail on-chain: {err}")

        unknown_program_detected = False
        for log in logs:
            if "Program " in log and " invoke " in log:
                prog_id = log.split("Program ")[1].split(" invoke ")[0]
                if prog_id not in self.known_safe_programs:
                    unknown_program_detected = True
                    risk_factors.append(f"UNKNOWN_PROGRAM_INVOCATION:{prog_id[:8]}...")

        if unknown_program_detected:
            risk_score += 35
            explanation.append("Detected invocation of an unverified or potentially unsafe program.")
        else:
            explanation.append("All invoked programs are official and verified Solana ecosystem programs.")

        if units_consumed > 150000:
            risk_score += 15
            risk_factors.append("HIGH_COMPUTE_UNITS")
            explanation.append(f"Unusually high compute units consumption ({units_consumed}).")

        if risk_score >= 70:
            severity = "CRITICAL"
            recommendation = "REJECT: High risk of drainer or malicious contract."
        elif risk_score >= 35:
            severity = "MEDIUM"
            recommendation = "WARN: Inspect carefully before signing."
        else:
            severity = "LOW"
            recommendation = "APPROVE: Clean and safe transaction."

        return {
            "severity": severity,
            "risk_score": risk_score,
            "risk_factors": risk_factors,
            "explanation": " ".join(explanation),
            "recommendation": recommendation,
            "logs_summary": logs[:5]
        }
