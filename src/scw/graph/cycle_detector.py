from scw.graph.graph import DependencyGraph


class CycleDetector:

    def has_cycle(
        self,
        graph: DependencyGraph,
    ) -> bool:

        visited: set[str] = set()
        recursion_stack: set[str] = set()

        for node in graph.adjacency:

            if node not in visited and  self._dfs(
                    node,
                    graph,
                    visited,
                    recursion_stack):
                    return True

        return False

    def _dfs(
        self,
        node: str,
        graph: DependencyGraph,
        visited: set[str],
        recursion_stack: set[str],
    ) -> bool:

        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph.adjacency.get(node, set()):

            if neighbor not in visited:

                if self._dfs(
                    neighbor,
                    graph,
                    visited,
                    recursion_stack,
                ):
                    return True

            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)

        return False