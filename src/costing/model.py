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


def estimate_per_sample_breakdown(
    profile: RunProfile,
    hourly_rate: float,
    storage_rate_per_gb_month: float,
) -> dict[str, float]:
    if profile.samples <= 0:
        raise ValueError("samples must be > 0")
    compute_total = estimate_compute_cost(profile, hourly_rate)
    storage_total = estimate_storage_cost(profile, storage_rate_per_gb_month)
    total = round(compute_total + storage_total, 2)
    return {
        "compute_per_sample": round(compute_total / profile.samples, 4),
        "storage_per_sample": round(storage_total / profile.samples, 4),
        "total_per_sample": round(total / profile.samples, 4),
    }
