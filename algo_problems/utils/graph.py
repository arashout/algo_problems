from algo_problems.utils.testing import Solution, Test
from typing import List, Tuple

class DirectedGraph:
    def __init__(self, n: int):
        self.vertices = [[] for i in range(n)]

    def n(self) -> int:
        return len(self.vertices)

    def v(self) -> List[int]:
        return range(len(self.vertices))

    def add_edge(self, i: int, j: int, undirected=False):
        # Check if within bounds
        if i >= self.n() or j >= self.n():
            # TODO: Add more information?
            raise IndexError('Vertex index out of bounds')

        self.vertices[i].append(j)

        if undirected:
            self.vertices[j].append(i)

    def get_adj(self, v) -> List[int]:
        if v >= self.n():
            raise IndexError("Vertex not in graph")
        else:
            return self.vertices[v]

    def topological_sort(self) -> List[int]:
        visited = set()
        sorted_vertices = []

        def explore(v: int):
            if v in visited:
                return

            visited.add(v)

            for w in self.get_adj(v):
                explore(w)

            # Once v has been completely explored...
            sorted_vertices.append(v)

        for vertex in self.v():
            explore(vertex)

        return sorted_vertices

    def has_cycle(self) -> bool:
        visited = [False] * self.n()
        recursion_stack = [False] * self.n()

        def helper(v: int) -> bool:
            visited[v] = True
            recursion_stack[v] = True

            for w in self.get_adj(v):
                if not visited[w]:
                    if helper(w):
                        return True
                if recursion_stack[w]:
                    return True

            recursion_stack[v] = False
            return False

        for vertex in self.v():
            if not visited[vertex]:
                if helper(vertex):
                    return True

        return False


def build_simple_graph(n: int, edges: tuple) -> DirectedGraph:
    g = DirectedGraph(n)
    for e in edges:
        g.add_edge(e[0], e[1])
    return g


g = build_simple_graph(
    5,
    [
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 3),
        (2, 4),
        (4, 3)
    ]
)
print(g.topological_sort())
