from domain.metrics.usable_area_ratio import _is_usable
from domain.model.types import ProgramType
from tests.domain.fixture import load_rulebook


RULEBOOK = load_rulebook()

def test_is_usable_unit():
    assert _is_usable(ProgramType.LIVING, RULEBOOK) is True
    assert _is_usable(ProgramType.CIRCULATION, RULEBOOK) is False
    assert _is_usable(ProgramType.SUPPORT, RULEBOOK) is False