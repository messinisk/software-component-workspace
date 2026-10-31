from scw.models.workspace_context import WorkspaceContext
from scw.models.component import Component
from scw.models.interface import Interface

from scw.validator.rules import validate_scw_200



def test_scw_200_dependency_to_interface():

    context = WorkspaceContext(
        components=[
            Component(
                name="cli",
                version="1.0.0",
                provides=[],
                depends_on=["business_rules"],
            )
        ],
        interfaces=[],
    )

    result = validate_scw_200(context)

    assert result == []

def test_scw_200_dependency_to_component():

    context = WorkspaceContext(
        components=[
            Component(
                name="core",
                version="1.0.0",
                provides=["business_rules"],
                depends_on=[],
            ),
            Component(
                name="cli",
                version="1.0.0",
                provides=[],
                depends_on=["core"],
            ),
        ],
        interfaces=[],
    )

    result = validate_scw_200(context)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-200"