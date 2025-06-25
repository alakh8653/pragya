"""Trust score calculations."""

from typing import Dict


def trust_score(votes: Dict[str, int]) -> float:
    if not votes:
        return 0.0
    pos = sum(1 for v in votes.values() if v > 0)
    return pos / len(votes)
