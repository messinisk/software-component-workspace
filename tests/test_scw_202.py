from scw.models.workspace_context import WorkspaceContext
from scw.models.component import Component
from scw.models.interface import Interface

from scw.validator.rules import validate_scw_202


def test_scw_202_unique_interface_names():

    context = WorkspaceContext(
        components=[],
        interfaces=[
            Interface(
                name="business_rules",
                version="1.0.0",
            ),
            Interface(
                name="command_line",
                version="1.0.0",
            ),
        ],
    )

    result = validate_scw_202(context)

    assert result == []


def test_scw_202_duplicate_interface_names():

    context = WorkspaceContext(
        components=[],
        interfaces=[
            Interface(
                name="business_rules",
                version="1.0.0",
            ),
            Interface(
                name="business_rules",
                version="1.0.0",
            ),
        ],
    )

    result = validate_scw_202(context)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-202"

