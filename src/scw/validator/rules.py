from scw.models.workspace_context import WorkspaceContext

from .result import ValidationMessage


def validate_scw_001(document: dict) -> list[ValidationMessage]:
    messages: list[ValidationMessage] = []

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
    messages: list[ValidationMessage] = []

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
    messages: list[ValidationMessage] = []

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


def validate_scw_100(
    context: WorkspaceContext,
) -> list[ValidationMessage]:

    messages: list[ValidationMessage] = []

    interface_names = {iface.name for iface in context.interfaces}

    for component in context.components:
        for dependency in component.depends_on:
            if dependency not in interface_names:
                messages.append(
                    ValidationMessage(
                        rule_id="SCW-100",
                        level="ERROR",
                        message=(
                            f"Unknown interface "
                            f"'{dependency}' "
                            f"used by component "
                            f"'{component.name}'"
                        ),
                    )
                )

    return messages


def validate_scw_101(
    context: WorkspaceContext,
) -> list[ValidationMessage]:

    messages: list[ValidationMessage] = []

    provided = set()

    for component in context.components:
        provided.update(component.provides)

    for interface in context.interfaces:
        if interface.name not in provided:
            messages.append(
                ValidationMessage(
                    rule_id="SCW-101",
                    level="ERROR",
                    message=(f"Interface '{interface.name}' has no provider"),
                )
            )

    return messages

def validate_scw_200(
    context: WorkspaceContext,
) -> list[ValidationMessage]:

    messages: list[ValidationMessage] = []

    component_names = {
        component.name
        for component in context.components
    }

    for component in context.components:

        for dependency in component.depends_on:

            if dependency in component_names:

                messages.append(
                    ValidationMessage(
                        rule_id="SCW-200",
                        level="ERROR",
                        message=(
                            f"Component '{component.name}' "
                            f"depends on Component "
                            f"'{dependency}'. "
                            f"Components must depend on "
                            f"Interfaces."
                        ),
                    )
                )

    return messages

def validate_scw_201(
    context: WorkspaceContext,
) -> list[ValidationMessage]:

    messages: list[ValidationMessage] = []

    seen: set[str] = set()

    for component in context.components:

        if component.name in seen:

            messages.append(
    ValidationMessage(
        rule_id="SCW-201",
        level="ERROR",
        message=(
            f"Duplicate Component name "
            f"'{component.name}'"
        ),
    )
)

    seen.add(component.name)

    return messages

def validate_scw_202(
    context: WorkspaceContext,
) -> list[ValidationMessage]:

    messages: list[ValidationMessage] = []

    seen: set[str] = set()

    for interface in context.interfaces:

        if interface.name in seen:
            messages.append(
                ValidationMessage(
                    rule_id="SCW-202",
                    level="ERROR",
                    message=(
                        f"Duplicate Interface name "
                        f"'{interface.name}'"
                    ),
                )
            )

        seen.add(interface.name)

    return messages