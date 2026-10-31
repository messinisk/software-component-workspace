from scw.models.workspace_context import WorkspaceContext
from scw.models.component import Component
from scw.models.interface import Interface

from scw.validator.rules import validate_scw_001


def test_scw_001_valid_manifest():

    document = {
        "apiVersion": "scw/v0.1",
        "kind": "Component",
        "metadata": {}
    }

    result = validate_scw_001(document)

    assert result == []


def test_scw_001_missing_api_version():

    document = {
        "kind": "Component",
        "metadata": {}
    }

    result = validate_scw_001(document)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-001"


def test_scw_001_missing_kind():

    document = {
        "apiVersion": "scw/v0.1",
        "metadata": {}
    }

    result = validate_scw_001(document)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-001"


def test_scw_001_missing_metadata():

    document = {
        "apiVersion": "scw/v0.1",
        "kind": "Component"
    }

    result = validate_scw_001(document)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-001"