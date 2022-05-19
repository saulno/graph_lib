from __future__ import annotations
from abc import ABC, abstractmethod
from math import inf
from typing import Dict, List, Tuple
from .Edge import Edge
from .Node import Node

class Graph(ABC):
    def __init__(self, show_weights= False) -> None:
        super().__init__()
        self.nodes = {}
        self.edges = {}
        self.show_weights = show_weights

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

    def dijkstra(self, source: Node) -> Graph:
        def min_dist(dist: Dict[int, int], in_tree: Dict[int, bool]) -> Tuple[int, int]:
            mini = inf
            mini_id = -1
            for (id, is_in) in in_tree.items():
                if is_in == False:
                    if dist[id] < mini:
                        mini = dist[id]
                        mini_id = id

            return (mini_id, mini)

        tree = UndirectedGraph(show_weights=True)
        
        dist = {node.id: inf for node in self.nodes.values()}
        parents = {node.id: None for node in self.nodes.values()}
        in_tree = {node.id: False for node in self.nodes.values()}

        dist[source.id] = 0
        source.attr["weight"] = 0

        while False in in_tree.values():
            (u_id, u_dist) = min_dist(dist, in_tree)
            if u_id == -1:
                break
            u = self.get_node_by_id(u_id)
            u.attr["weight"] = u_dist
            tree.add_node(u)
            if parents[u_id]:
                tree.add_edge(Edge(source=self.get_node_by_id(u_id), target=self.get_node_by_id(parents[u_id]), weight=dist[u_id]))
            in_tree[u_id] = True

            for n in self.get_neighbors_for_node(u):
                if e := self.get_edge_for_nodes(u, n):
                    if not in_tree[n.id] and dist[n.id] > u_dist + e.weight:
                        dist[n.id] = u_dist + e.weight
                        parents[n.id] = u_id
            

        return tree


    @abstractmethod
    def get_neighbors_for_node(self, node: Node) -> List[Node]:
        ...
    
    @abstractmethod
    def get_edge_for_nodes(self, node1: Node, node2: Node) -> Edge:
        ...

    @abstractmethod
    def to_graphviz(self, filename) -> None:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

class DirectedGraph(Graph):
    def __init__(self, show_weights= False) -> None:
        super().__init__(show_weights)
        self.directed = True

    def get_neighbors_for_node(self, node: Node) -> List[Node]:
        if not node.id in self.nodes.keys():
            raise Exception("Nodo no exisatente")
        
        neighbors = []
        for _edge_id, edge in self.edges.items():
            if edge.source.id == node.id:
                neighbors.append(edge.target)
        
        return neighbors

    def get_edge_for_nodes(self, node1: Node, node2: Node) -> Edge:
        if not node1.id in self.nodes.keys() or not node2.id in self.nodes.keys():
            raise Exception("Nodo no exisatente")
        
        for edge in self.edges.values():
            if edge.source.id == node1.id and edge.target.id == node2.id:
                return edge
        
        return None

    def to_graphviz(self, filename) -> None:
        with open(f"{filename}.gv", "w") as file:
            file.write("digraph {\n")
            for node in self.nodes.values():
                attrs = ""
                for key, val in node.attr.items():
                    attrs += f"{key}={val},"
                if self.show_weights:
                    file.write(f"    \"{node.id}_({node.attr['weight']})\" [{attrs}]\n")
                else:
                    file.write(f"    {node.id} [{attrs}]\n")

            for edge in self.edges.values():
                if self.show_weights:
                    file.write(f"    \"{edge.source.id}_({edge.source.attr['weight']})\" -> \"{edge.target.id}_({edge.target.attr['weight']})\" [label={edge.weight}, weight={edge.weight}]\n")
                else:
                    file.write(f"    {edge.source.id} -> {edge.target.id}\n")

    def __str__(self) -> str:
        return f"DirectedGraph(nodes={self.nodes}, edges={self.edges})"

class UndirectedGraph(Graph):
    def __init__(self, show_weights= False) -> None:
        super().__init__(show_weights)
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
    
    def get_edge_for_nodes(self, node1: Node, node2: Node) -> Edge:
        if not node1.id in self.nodes.keys() or not node2.id in self.nodes.keys():
            raise Exception("Nodo no exisatente")
        
        for edge in self.edges.values():
            if edge.source.id == node1.id and edge.target.id == node2.id or edge.source.id == node2.id and edge.target.id == node1.id:
                return edge
        
        return None

    def to_graphviz(self, filename) -> None:
        with open(f"{filename}.gv", "w") as file:
            file.write("graph {\n")
            for node in self.nodes.values():
                attrs = ""
                for key, val in node.attr.items():
                    attrs += f"{key}={val},"
                if self.show_weights:
                    file.write(f"    \"{node.id}_({node.attr['weight']})\" [{attrs}]\n")
                else:
                    file.write(f"    {node.id} [{attrs}]\n")

            for edge in self.edges.values():
                if self.show_weights:
                    file.write(f"    \"{edge.source.id}_({edge.source.attr['weight']})\" -- \"{edge.target.id}_({edge.target.attr['weight']})\" [label={edge.weight}, weight={edge.weight}]\n")
                else:
                    file.write(f"    {edge.source.id} -- {edge.target.id}\n")
                
            file.write("}\n")

    def __str__(self) -> str:
        return f"UndirectedGraph(nodes={self.nodes}, edges={self.edges})"