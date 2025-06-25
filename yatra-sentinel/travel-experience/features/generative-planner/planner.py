"""UI logic for generative planner."""

from dataclasses import dataclass
from typing import List


@dataclass
class PlanningRequest:
    intents: List[str]


def plan(request: PlanningRequest) -> List[str]:
    return [f"Plan step for {i}" for i in request.intents]
