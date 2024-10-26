from queue import PriorityQueue
from dataclasses import dataclass, field


@dataclass(order=True)
class Vertex:
    cost: float
    name: str = field(compare=False)


@dataclass(order=True)
class Path:
    cost: float
    prev: str = field(compare=False)


class Dijkstra(object):
    def __init__(self) -> None:
        self.queue = PriorityQueue()

    def set_graph(self, graph: dict[str, dict[str, int]]) -> None:
        self.graph = graph

    def create_path_table(self, start: str) -> None:
        self.path_table: dict[str, Path] = dict()
        for vertex in self.graph:
            self.path_table[vertex] = Path(float('inf'), '-')
        self.path_table[start] = Path(0, 'strat')

    def sum_costs(self, first: float, second: float) -> float:
        if self.opt_crit == 'max':
            return max(first, second)
        else:
            return first+second

    def run(self, start: str, end: str, opt_crit: str = 'max'
            ) -> tuple[dict[str, Path], list[str]]:
        self.opt_crit = opt_crit
        self.create_path_table(start)

        searched = set()
        active = Vertex(cost=0, name=start)
        while active.name != end:
            for vertex_name, vertex_cost in self.graph[active.name].items():
                new_cost = self.sum_costs(active.cost, vertex_cost)
                if new_cost < self.path_table[vertex_name].cost:
                    self.path_table[vertex_name] = Path(new_cost, active.name)
                    self.queue.put(Vertex(new_cost, vertex_name))

            active = self.queue.get()
            while active.name in searched:
                active = self.queue.get()
            searched.add(active.name)

        path = [end]
        cur = end
        while cur != start:
            path.append(self.path_table[cur].prev)
            cur = self.path_table[cur].prev
        return self.path_table, path[::-1]
