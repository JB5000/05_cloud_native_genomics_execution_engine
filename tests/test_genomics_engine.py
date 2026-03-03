import pytest
from src.genomics_engine import calculate_cost, estimate_run_cost, select_instance

def test_calculate_cost():
    assert calculate_cost("t3.medium", 1) == 0.0416
    assert calculate_cost("m5.large", 2) == 0.192

def test_select_instance():
    assert select_instance("low") == "on-demand"
    assert select_instance("high") == "spot"


def test_estimate_run_cost_multiple_runs():
    assert estimate_run_cost("m5.large", total_hours=2, runs=3) == 0.576


def test_estimate_run_cost_invalid_runs():
    with pytest.raises(ValueError):
        estimate_run_cost("t3.medium", total_hours=1, runs=0)
