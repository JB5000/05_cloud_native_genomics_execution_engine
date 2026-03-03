import pytest

from src.costing.model import RunProfile, estimate_per_sample_breakdown, estimate_total_cost
from src.optimizer.instance_selector import InstanceOption, choose_instance


def test_total_cost_estimation() -> None:
    profile = RunProfile(samples=100, hours_per_sample=0.8, storage_gb_per_sample=3.5)
    total = estimate_total_cost(profile, hourly_rate=0.42, storage_rate_per_gb_month=0.023)
    assert total == 41.65


def test_instance_selection_prefers_spot_when_risk_is_acceptable() -> None:
    spot = InstanceOption(name="c6i.large-spot", hourly_rate=0.05, interruption_risk=0.08)
    ondemand = InstanceOption(name="c6i.large", hourly_rate=0.12, interruption_risk=0.01)
    chosen = choose_instance(spot, ondemand, max_risk=0.10)
    assert chosen.name == "c6i.large-spot"


def test_per_sample_breakdown() -> None:
    profile = RunProfile(samples=50, hours_per_sample=1.0, storage_gb_per_sample=2.0)
    breakdown = estimate_per_sample_breakdown(
        profile,
        hourly_rate=0.3,
        storage_rate_per_gb_month=0.02,
    )
    assert breakdown["compute_per_sample"] == 0.3
    assert breakdown["storage_per_sample"] == 0.04
    assert breakdown["total_per_sample"] == 0.34


def test_per_sample_breakdown_requires_positive_samples() -> None:
    profile = RunProfile(samples=0, hours_per_sample=1.0, storage_gb_per_sample=2.0)
    with pytest.raises(ValueError):
        estimate_per_sample_breakdown(profile, hourly_rate=0.3, storage_rate_per_gb_month=0.02)
