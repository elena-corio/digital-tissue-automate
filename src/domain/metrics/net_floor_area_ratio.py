"""
Calculate net floor area ratio for a list of units and slabs.
"""

from domain.model.elements import Slabs, Unit

# Note: it can also be calculated as slab area - core area - column area
# so it only depedns on structural model
def calculate_net_floor_area_ratio(units: list[Unit], slabs: list[Slabs]) -> float:
    """
    Calculate net floor area ratio for a list of units.

    """
    total_unit_area = sum(unit.area for unit in units)
    total_slab_area = sum(slab.area for slab in slabs)
    return total_unit_area / total_slab_area if total_slab_area > 0 else 0
