"""Underwriting engine."""


def assess_risk(score: float) -> str:
    if score < 0.3:
        return "Low"
    if score < 0.7:
        return "Medium"
    return "High"
