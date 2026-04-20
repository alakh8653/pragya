"""Proactive resolution engine."""

from typing import Callable, List


class Resolver:
    """Simple rules-based resolver."""

    def __init__(self):
        self._rules: List[Callable[[], None]] = []

    def add_rule(self, rule: Callable[[], None]) -> None:
        self._rules.append(rule)

    def run(self) -> None:
        for rule in self._rules:
            rule()
