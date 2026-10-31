from scw.models.workspace_context import WorkspaceContext
from scw.models.component import Component
from scw.models.interface import Interface

from scw.validator.rules import validate_scw_100

def test_scw_100_interface_exists():

    cli = Component(
        name="cli",
        version="1.0.0",
        provides=[],
        depends_on=["business_rules"],
    )

    interface = Interface(
        name="business_rules",
        version="1.0.0",
    )

    context = WorkspaceContext(
        components=[cli],
        interfaces=[interface],
        policies=[],
    )

    result = validate_scw_100(context)

    assert result == []

def test_scw_100_unknown_interface():

    cli = Component(
        name="cli",
        version="1.0.0",
        provides=[],
        depends_on=["missing_interface"],
    )

    context = WorkspaceContext(
        components=[cli],
        interfaces=[],
        policies=[],
    )

    result = validate_scw_100(context)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-100"