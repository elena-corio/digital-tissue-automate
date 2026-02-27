import pytest
from domain.metrics.net_floor_area_ratio import calculate_net_floor_area_ratio
from domain.model.elements import Slabs, Unit

class DummySlab:
    def __init__(self, area):
        self.area = area

class DummyUnit:
    def __init__(self, area):
        self.area = area

def test_calculate_net_floor_area_ratio_normal():
    slabs = [DummySlab(100), DummySlab(200)]
    units = [DummyUnit(50), DummyUnit(100)]
    expected = (50 + 100) / (100 + 200)
    assert calculate_net_floor_area_ratio(units, slabs) == expected

def test_calculate_net_floor_area_ratio_zero_slab():
    slabs = [DummySlab(0), DummySlab(0)]
    units = [DummyUnit(50), DummyUnit(100)]
    assert calculate_net_floor_area_ratio(units, slabs) == 0

def test_calculate_net_floor_area_ratio_empty_lists():
    slabs = []
    units = []
    assert calculate_net_floor_area_ratio(units, slabs) == 0
