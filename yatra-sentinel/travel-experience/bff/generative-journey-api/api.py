"""API to orchestrate journey generation."""

from typing import List
import importlib


JourneyGenerator = importlib.import_module(
    'yatra-sentinel.platform.ai-fabric.journey-generator.generator'
).JourneyGenerator


def plan_trip(destinations: List[str]):
    gen = JourneyGenerator()
    return gen.generate(destinations)
