"""Simple journey generation engine."""

from dataclasses import dataclass
from typing import List


@dataclass
class TripSegment:
    location: str
    days: int


class JourneyGenerator:
    """Generate a linear journey from a list of destinations."""

    def generate(self, destinations: List[str]) -> List[TripSegment]:
        segments = []
        for place in destinations:
            segments.append(TripSegment(location=place, days=2))
        return segments
