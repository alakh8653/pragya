"""Risk analysis module."""

from dataclasses import dataclass
from typing import List


@dataclass
class RiskEvent:
    description: str
    severity: int


def aggregate_risk(events: List[RiskEvent]) -> float:
    if not events:
        return 0.0
    score = sum(e.severity for e in events) / len(events)
    return round(score, 2)
