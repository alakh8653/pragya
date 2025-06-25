"""Social discovery utilities."""

from typing import Iterable


def annotate(listings: Iterable[str]) -> Iterable[str]:
    for listing in listings:
        yield f"{listing} (friends liked)"
