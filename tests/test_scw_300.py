from scw.graph.builder import GraphBuilder
from scw.models.component import Component
from scw.models.interface import Interface
from scw.models.workspace_context import WorkspaceContext

def test_graph_creation():

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
                depends_on=["business_rules"],
            ),
        ],
        interfaces=[
            Interface(
                name="business_rules",
                version="1.0.0",
            )
        ],
    )

    graph = GraphBuilder().build(context)

    assert "core" in graph.adjacency
    assert "cli" in graph.adjacency

    assert "core" in graph.adjacency["cli"]

