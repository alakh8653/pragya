"""Dynamic pricing algorithms."""

from typing import List


def optimal_price(base_price: float, demand_index: float) -> float:
    return round(base_price * (1 + demand_index), 2)
