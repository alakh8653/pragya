"""Partner tier logic."""


def commission_rate(tier: str) -> float:
    return {
        "Bronze": 0.05,
        "Silver": 0.08,
        "Gold": 0.12,
    }.get(tier, 0.0)
