"""Price forecasting utilities."""

from statistics import mean
from typing import Iterable


def moving_average(values: Iterable[float], window: int = 3) -> float:
    """Return the moving average of the last window values."""
    values = list(values)
    if not values:
        return 0.0
    return mean(values[-window:])
