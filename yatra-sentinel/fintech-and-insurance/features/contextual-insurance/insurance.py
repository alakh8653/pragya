"""Contextual insurance calculations."""


def quote(value: float, risk: float) -> float:
    return round(value * 0.01 * (1 + risk), 2)
