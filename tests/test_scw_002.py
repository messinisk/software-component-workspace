from scw.validator.rules import validate_scw_002


def test_scw_002_valid_name():

    document = {
        "metadata": {
            "name": "core"
        }
    }

    result = validate_scw_002(document)

    assert result == []


def test_scw_002_missing_metadata():

    document = {}

    result = validate_scw_002(document)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-002"


def test_scw_002_missing_name():

    document = {
        "metadata": {}
    }

    result = validate_scw_002(document)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-002"


def test_scw_002_empty_name():

    document = {
        "metadata": {
            "name": ""
        }
    }

    result = validate_scw_002(document)

    assert len(result) == 1
    assert result[0].rule_id == "SCW-002"