"""Situational context utilities."""

from dataclasses import dataclass
from datetime import datetime
from typing import Tuple


@dataclass
class Location:
    lat: float
    lon: float


def is_night(time: datetime, location: Location) -> bool:
    return time.hour < 6 or time.hour > 18
