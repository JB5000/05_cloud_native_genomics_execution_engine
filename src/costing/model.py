"""Cost model helpers for cloud genomics batch runs."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RunProfile:
    samples: int
    hours_per_sample: float
    storage_gb_per_sample: float


def estimate_compute_cost(profile: RunProfile, hourly_rate: float) -> float:
    return round(profile.samples * profile.hours_per_sample * hourly_rate, 2)


def estimate_storage_cost(profile: RunProfile, storage_rate_per_gb_month: float) -> float:
    return round(profile.samples * profile.storage_gb_per_sample * storage_rate_per_gb_month, 2)


def estimate_total_cost(profile: RunProfile, hourly_rate: float, storage_rate_per_gb_month: float) -> float:
    compute = estimate_compute_cost(profile, hourly_rate)
    storage = estimate_storage_cost(profile, storage_rate_per_gb_month)
    return round(compute + storage, 2)
