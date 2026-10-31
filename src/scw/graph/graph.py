from dataclasses import dataclass, field


@dataclass
class DependencyGraph:
    adjacency: dict[str, set[str]] = field(
        default_factory=dict
    )

    def add_node(self, node: str) -> None:
        self.adjacency.setdefault(
            node,
            set(),
        )

    def add_edge(
        self,
        source: str,
        target: str,
    ) -> None:

        self.add_node(source)
        self.add_node(target)

        self.adjacency[source].add(target)