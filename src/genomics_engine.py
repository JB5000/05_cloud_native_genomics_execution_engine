"""
Genomics Execution Engine Core Module

Provides basic functionality for workflow execution.
"""

def calculate_cost(instance_type: str, hours: float) -> float:
    """Calculate compute cost based on instance type."""
    rates = {
        "t3.medium": 0.0416,
        "m5.large": 0.096,
    }
    return rates.get(instance_type, 0.1) * hours

def select_instance(risk_tolerance: str) -> str:
    """Select instance based on risk tolerance."""
    if risk_tolerance == "low":
        return "on-demand"
    return "spot"


def estimate_run_cost(instance_type: str, total_hours: float, runs: int = 1) -> float:
    """Estimate total run cost across repeated executions."""
    if runs < 1:
        raise ValueError("runs must be >= 1")
    if total_hours < 0:
        raise ValueError("total_hours must be >= 0")
    single_run_cost = calculate_cost(instance_type, total_hours)
    return round(single_run_cost * runs, 4)
