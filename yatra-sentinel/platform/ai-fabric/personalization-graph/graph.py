"""User personalization graph representations."""

from dataclasses import dataclass, field
from typing import Dict, Set


@dataclass
class UserNode:
    user_id: str
    preferences: Dict[str, float] = field(default_factory=dict)
    connections: Set[str] = field(default_factory=set)


def connect(graph: Dict[str, UserNode], a: str, b: str) -> None:
    graph.setdefault(a, UserNode(a)).connections.add(b)
    graph.setdefault(b, UserNode(b)).connections.add(a)
