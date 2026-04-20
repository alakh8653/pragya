"""Multi-currency wallet."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Wallet:
    balances: Dict[str, float] = field(default_factory=dict)

    def deposit(self, currency: str, amount: float) -> None:
        self.balances[currency] = self.balances.get(currency, 0) + amount
