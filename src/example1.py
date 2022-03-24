from graph.Edge import Edge
from graph.Graph import Graph
from graph.Node import Node
from graph.Edge import Edge
from graph.Graph import DirectedGraph, UndirectedGraph

n1 = Node(position=(0,0), label="nodo 1", color="red")
print(n1)
n2 = Node(position=(0,0), label="nodo 2", color="red")
print(n2)

e1 = Edge(id="e_1", source=n1, target=n2)
print(e1)

g = UndirectedGraph()
g.add_node(n1)
g.add_node(n2)
g.add_edge(e1)
print(g)

g.to_graphviz("g1")