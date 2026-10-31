from scw.models.workspace_context import WorkspaceContext
from scw.models.component import Component
from scw.models.interface import Interface
from scw.graph.cycle_detector import DependencyGraph
from scw.graph.graph import DependencyGraph
from scw.graph.cycle_detector import CycleDetector


def test_scw_301_no_cycle():

    graph = DependencyGraph(
        adjacency={
            "cli": {"core"},
            "core": set(),
        }
    )

    detector = CycleDetector()

    assert detector.has_cycle(graph) is False


def test_scw_301_cycle_detected():

    graph = DependencyGraph(
        adjacency={
            "a": {"b"},
            "b": {"a"},
        }
    )

    detector = CycleDetector()

    assert detector.has_cycle(graph) is True

def test_scw_301_no_cycle():

    graph = DependencyGraph(
        adjacency={
            "cli": {"core"},
            "core": set(),
        }
    )

    detector = CycleDetector()

    assert detector.has_cycle(graph) is False


def test_scw_301_cycle_detected():

    graph = DependencyGraph(
        adjacency={
            "a": {"b"},
            "b": {"a"},
        }
    )

    detector = CycleDetector()

    assert detector.has_cycle(graph) is True