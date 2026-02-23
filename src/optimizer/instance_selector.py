"""Simple selector for spot vs on-demand based on interruption tolerance."""

from dataclasses import dataclass


@dataclass(frozen=True)
class InstanceOption:
    name: str
    hourly_rate: float
    interruption_risk: float


def choose_instance(spot: InstanceOption, ondemand: InstanceOption, max_risk: float) -> InstanceOption:
    if spot.interruption_risk <= max_risk:
        return spot
    return ondemand
