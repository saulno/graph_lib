from abc import ABC, abstractmethod
from .Edge import Edge
from .Node import Node

class Graph(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.nodes = {}
        self.edges = {}

    def add_node(self, node: Node) -> None:
        self.nodes[node.id] = node
    
    def add_edge(self, edge: Edge) -> None:
        self.edges[edge.id] = edge

    def get_node_by_id(self, id) -> Node:
        return self.nodes[id]

    def get_edges_by_node_id(self, id):
        newDict = {}
        for (key, val) in self.edges.items():
            if val.source.id == id or val.target.id == id:
                newDict[key] = val
        return newDict

    @abstractmethod
    def to_graphviz(self, filename) -> None:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

class DirectedGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.directed = True

    def to_graphviz(self, filename) -> None:
        with open(f"{filename}.gv", "w") as file:
            file.write("digraph {\n")
            for node in self.nodes.values():
                attrs = ""
                for key, val in node.attr.items():
                    attrs += f"{key}={val},"
                file.write(f"    {node.id} [{attrs}]\n")

            for edge in self.edges.values():
                file.write(f"    {edge.source.id} -> {edge.target.id}\n")
            file.write("}\n")

    def __str__(self) -> str:
        return f"DirectedGraph(nodes={self.nodes}, edges={self.edges})"

class UndirectedGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.directed = False

    def to_graphviz(self, filename) -> None:
        with open(f"{filename}.gv", "w") as file:
            file.write("graph {\n")
            for node in self.nodes.values():
                attrs = ""
                for key, val in node.attr.items():
                    attrs += f"{key}={val},"
                file.write(f"    {node.id} [{attrs}]\n")

            for edge in self.edges.values():
                file.write(f"    {edge.source.id} -- {edge.target.id}\n")
            file.write("}\n")

    def __str__(self) -> str:
        return f"UndirectedGraph(nodes={self.nodes}, edges={self.edges})"