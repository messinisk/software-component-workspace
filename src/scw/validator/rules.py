from .result import ValidationMessage


def validate_scw_001(document: dict) -> list[ValidationMessage]:
    messages = []

    required = [
        "apiVersion",
        "kind",
        "metadata",
    ]

    for field in required:
        if field not in document:
            messages.append(
                ValidationMessage(
                    rule_id="SCW-001",
                    level="ERROR",
                    message=f"Missing required field: {field}",
                )
            )

    return messages


def validate_scw_002(document: dict) -> list[ValidationMessage]:
    messages = []

    metadata = document.get("metadata", {})

    if not metadata.get("name"):
        messages.append(
            ValidationMessage(
                rule_id="SCW-002",
                level="ERROR",
                message="metadata.name is required",
            )
        )

    return messages


def validate_scw_003(document: dict) -> list[ValidationMessage]:
    messages = []

    if document.get("kind") != "Component":
        return messages

    metadata = document.get("metadata", {})

    if not metadata.get("version"):
        messages.append(
            ValidationMessage(
                rule_id="SCW-003",
                level="ERROR",
                message="Component version is required",
            )
        )

    return messages