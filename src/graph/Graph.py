from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
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

    def bfs(self, node: Node) -> Graph:
        visited = []
        queue = []
        tree = UndirectedGraph()

        if not node.id in self.nodes.keys():
            raise Exception("Nodo no exisatente")

        queue += [(node, neigh) for neigh in self.get_neighbors_for_node(node)]
        visited.append(node.id)
        tree.add_node(node)

        while len(queue) > 0:
            parent, neighbor = queue.pop(0)
            if not neighbor.id in visited:
                visited.append(neighbor.id)
                tree.add_node(neighbor)
                tree.add_edge(Edge(parent, neighbor))
                queue += [(neighbor, neigh) for neigh in self.get_neighbors_for_node(neighbor) if not neigh.id in visited and not neigh.id in queue]
        
        return tree
    
    def dfs_iterative(self, node: Node) -> Graph:
        visited = []
        stack = []
        tree = UndirectedGraph()

        if not node.id in self.nodes.keys():
            raise Exception("Nodo no exisatente")

        stack += [(node, neigh) for neigh in self.get_neighbors_for_node(node)]
        visited.append(node.id)
        tree.add_node(node)

        while len(stack) > 0:
            parent, neighbor = stack.pop()
            if not neighbor.id in visited:
                visited.append(neighbor.id)
                tree.add_node(neighbor)
                tree.add_edge(Edge(parent, neighbor))
                stack += [(neighbor, neigh) for neigh in self.get_neighbors_for_node(neighbor) if not neigh.id in visited and not neigh.id in stack]
        
        return tree
    
    def dfs_recursive(self, node: Node) -> Graph:
        visited = []
        tree = UndirectedGraph()

        if not node.id in self.nodes.keys():
            raise Exception("Nodo no exisatente")

        self.dfs_r(node, tree, visited)

        return tree

    def dfs_r(self, node: Node, tree: Graph, visited: List[str]):
        tree.add_node(node)
        visited.append(node.id)
        for neighbor in self.get_neighbors_for_node(node):
            if not neighbor.id in visited:
                tree.add_edge(Edge(node, neighbor))
                self.dfs_r(neighbor, tree, visited)

    @abstractmethod
    def get_neighbors_for_node(self, node: Node) -> List[Node]:
        ...

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

    def get_neighbors_for_node(self, node: Node) -> List[Node]:
        if not node.id in self.nodes.keys():
            raise Exception("Nodo no exisatente")
        
        neighbors = []
        for _edge_id, edge in self.edges.items():
            if edge.source.id == node.id:
                neighbors.append(edge.target)
        
        return neighbors


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

    def get_neighbors_for_node(self, node: Node) -> List[Node]:
        if not node.id in self.nodes.keys():
            raise Exception("Nodo no exisatente")
        
        neighbors = []
        for _edge_id, edge in self.edges.items():
            if edge.source.id == node.id:
                neighbors.append(edge.target)
            elif edge.target.id == node.id:
                neighbors.append(edge.source)
        
        return neighbors

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