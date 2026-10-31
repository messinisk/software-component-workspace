from scw.graph.graph import DependencyGraph
from scw.models.workspace_context import WorkspaceContext


class GraphBuilder:

    def build(
        self,
        context: WorkspaceContext,
    ) -> DependencyGraph:

        graph = DependencyGraph()

        providers: dict[str, str] = {}

        for component in context.components:

            for interface in component.provides:
                providers[interface] = component.name

        for component in context.components:

            graph.add_node(component.name)

            for interface in component.depends_on:

                provider = providers.get(interface)

                if provider:
                    graph.add_edge(
                        component.name,
                        provider,
                    )

        return graph