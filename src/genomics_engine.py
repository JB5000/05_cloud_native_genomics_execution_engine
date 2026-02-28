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
