from abc import ABC, abstractmethod
import random
from graph.Edge import Edge

from graph.Node import Node
from .Graph import DirectedGraph, Graph, UndirectedGraph


class Builder(ABC):
    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()

    @abstractmethod
    def build(self) -> Graph:
        """
        Builds a certain type of graph
        """
        ...

class GridBuilder(Builder):
    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()

    def build(self, columns, rows, directed=False) -> Graph:
        """
        Builds a grid graph
        :param columns: number of columns (> 1)
        :param rows: number of rows (> 1)
        :param directed: will the new graph be directed?
        :return: new graph
        """
        g = DirectedGraph() if directed else UndirectedGraph()
        for i in range(rows):
            for j in range(columns):
                n2 = Node(id=f"{i}x{j}")
                g.add_node(n2)

                if j > 0:
                    n1 = g.get_node_by_id(f"{i}x{j-1}")
                    g.add_edge(Edge(source=n1, target=n2))
                if i > 0:
                    n1 = g.get_node_by_id(f"{i-1}x{j}")
                    g.add_edge(Edge(source=n1, target=n2))

        return g

class ErdosRenyiBuilder(Builder):
    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()

    def build(self, nodes, edges, directed=False, loops=False) -> Graph:
        """
        Creates a graph of n nodes with model Erdos-Renyi
        :param nodes: number of nodes ( > 0)
        :param edges: number of edges ( >= n-1)
        :param directed: enable graph directed
        :param loops: allow auto-cycle (loops)
        :return: Graph created
        """
        g = DirectedGraph() if directed else UndirectedGraph()
        for _ in range(nodes):
            g.add_node(Node())
        for _ in range(edges):
            pair = random.choices(list(g.nodes.values()), k=2) if loops else random.sample(list(g.nodes.values()), k=2)
            g.add_edge(Edge(source=pair[0], target=pair[1]))

        return g

class GraphFactory:
    def __init__(self, builder=None) -> None:
        self.builder = builder

    def set_builder(self, builder: Builder) -> None:
        self.builder = builder

    def build_graph(self, **kwargs) -> Graph:
        return self.builder.build(**kwargs)


