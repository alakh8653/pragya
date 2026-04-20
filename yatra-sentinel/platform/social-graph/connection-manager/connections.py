"""Manage user connections."""

from collections import defaultdict
from typing import DefaultDict, Set


class ConnectionManager:
    def __init__(self):
        self.edges: DefaultDict[str, Set[str]] = defaultdict(set)

    def connect(self, a: str, b: str) -> None:
        self.edges[a].add(b)
        self.edges[b].add(a)

    def connections_of(self, user: str) -> Set[str]:
        return self.edges[user]
