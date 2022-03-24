from abc import ABC, abstractmethod
import math
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

class GilbertBuilder(Builder):
    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()

    def build(self, nodes, p, directed=False, loops=False) -> Graph:
        """
        Creates a graph of n nodes with model Gilbert 
        :param n: number of nodes ( > 0)
        :param p: probability to create an edge (0,1)
        :param directed: enable graph directed
        :param loops: allow auto-cycle (loops)
        :return: Graph created
        """
        g = DirectedGraph() if directed else UndirectedGraph()
        for _ in range(nodes):
            g.add_node(Node())

        for n1 in g.nodes.values():
            for n2 in g.nodes.values():
                if random.random() <= p:
                    if loops or n1.id != n2.id:
                        g.add_edge(Edge(source=n1, target=n2))

        return g

class GeographicBuilder(Builder):
    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()

    def dist(self, node1: Node, node2: Node) -> float:
        return math.sqrt((node1.attr["COORDINATE_X"] - node2.attr["COORDINATE_X"])**2 + \
            (node1.attr["COORDINATE_Y"] - node2.attr["COORDINATE_Y"])**2)

    def build(self, nodes, max_dist, directed=False, loops=False) -> Graph:
        """
        Create a random graph with simple geographic method
        :param nodes: number of vertices ( > 0)
        :param max_dist: max distance to generate edge between nodes (0,1)
        :param directed: enable graph directed
        :param loops: allow auto-cycle (loops)
        :return: graph created
        """
        g = DirectedGraph() if directed else UndirectedGraph()
        for _ in range(nodes):
            g.add_node(Node(COORDINATE_X=random.random(), COORDINATE_Y=random.random()))

        for n1 in g.nodes.values():
            for n2 in g.nodes.values():
                if self.dist(n1, n2) <= max_dist:
                    if loops or n1.id != n2.id:
                        g.add_edge(Edge(source=n1, target=n2))

        return g

class BarabasiAlbertBuilder(Builder):
    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()

    def build(self, nodes, degree, directed=False, loops=False) -> Graph:
        """
        Create Barabasi-Albert (BA) graph
        :param nodes: number of nodes ( > 0)
        :param degree: max number of edges of vertex ( > 1)
        :param directed: enable graph directed
        :param loops: allow auto-cycle (loops)
        return: graph created
        """
        g = DirectedGraph() if directed else UndirectedGraph()
        # First d nodes, fully connected
        for _ in range(degree):
            g.add_node(Node())
        for n1 in g.nodes.values():
            for n2 in g.nodes.values():
                g.add_edge(Edge(source=n1, target=n2))

        # Next nodes 
        for _ in range(degree, nodes):
            ni = Node()
            g.add_node(ni)
            for nj in g.nodes.values():
                p = len(g.get_edges_by_node_id(nj.id)) / len(g.edges.values())
                if random.random() <= p and \
                len(g.get_edges_by_node_id(ni.id)) < degree and \
                len(g.get_edges_by_node_id(nj.id)) < degree:
                    if loops or ni.id != nj.id:
                        g.add_edge(Edge(source=ni, target=nj))

        return g

class DorogovtsevMendesBuilder(Builder):
    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()

    def build(self, nodes, directed=False) -> Graph:
        """
        Create a Dorogovtsev-Mendes graph
        :param nodes: number of nodes
        :param directed: enable graph directed
        :return: graph created
        """
        g = DirectedGraph() if directed else UndirectedGraph()

        # First 3 nodes, triangle
        n1 = Node(id=0)
        n2 = Node(id=1)
        n3 = Node(id=2)
        g.add_node(n1)
        g.add_node(n2)
        g.add_node(n3)
        g.add_edge(Edge(source=n1, target=n2))
        g.add_edge(Edge(source=n2, target=n3))
        g.add_edge(Edge(source=n3, target=n1))

        # Next nodes 
        for i in range(3, nodes):
            ni = Node(id=i)
            rand = random.choice(list(g.edges.values()))
            g.add_node(ni)
            g.add_edge(Edge(source=ni, target=rand.source))
            g.add_edge(Edge(source=ni, target=rand.target))

        return g

class GraphFactory:
    def __init__(self, builder=None) -> None:
        self.builder = builder

    def set_builder(self, builder: Builder) -> None:
        self.builder = builder

    def build_graph(self, **kwargs) -> Graph:
        return self.builder.build(**kwargs)


