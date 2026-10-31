from scw.models.workspace_context import WorkspaceContext
from scw.models.component import Component
from scw.models.interface import Interface


from scw.validator.rules import validate_scw_003


def test_scw_003_valid_component():

    document = {
        "kind": "Component",
        "metadata": {
            "version": "1.0.0"
        }
    }

    result = validate_scw_003(document)

    assert result == []


def test_scw_003_missing_version():

    document = {
        "kind": "Component",
        "metadata": {}
    }

    result = validate_scw_003(document)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-003"


def test_scw_003_empty_version():

    document = {
        "kind": "Component",
        "metadata": {
            "version": ""
        }
    }

    result = validate_scw_003(document)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-003"


def test_scw_003_non_component_is_ignored():

    document = {
        "kind": "Interface",
        "metadata": {}
    }

    result = validate_scw_003(document)

    assert result == []