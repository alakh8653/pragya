"""Loyalty program utilities."""


def status(points: int) -> str:
    if points > 1000:
        return "Gold"
    if points > 500:
        return "Silver"
    return "Bronze"
