import pytest
from src.genomics_engine import calculate_cost, select_instance

def test_calculate_cost():
    assert calculate_cost("t3.medium", 1) == 0.0416
    assert calculate_cost("m5.large", 2) == 0.192

def test_select_instance():
    assert select_instance("low") == "on-demand"
    assert select_instance("high") == "spot"
