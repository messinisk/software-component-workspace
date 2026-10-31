from dataclasses import dataclass, field

from scw.models.component import Component
from scw.models.interface import Interface


@dataclass
class WorkspaceContext:
    components: list[Component]
    interfaces: list[Interface]
    policies: list = field(default_factory=list)
