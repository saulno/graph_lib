from graph.GraphFactory import GraphFactory, GridBuilder

from graph.GraphFactory import BarabasiAlbertBuilder, DorogovtsevMendesBuilder, ErdosRenyiBuilder, GeographicBuilder, GilbertBuilder, GraphFactory, GridBuilder


factory = GraphFactory()



factory.set_builder(GridBuilder())

g = factory.build_graph(columns=5, rows=6, directed=True)
g.to_graphviz("../output_4/grid/generated_30")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Grid 30 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/grid/kruskal_30")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Grid 30 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/grid/prim_30")

g = factory.build_graph(columns=10, rows=10, directed=True)
g.to_graphviz("../output_4/grid/generated_100")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Grid 100 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/grid/kruskal_100")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Grid 100 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/grid/prim_100")



factory.set_builder(ErdosRenyiBuilder())

g = factory.build_graph(nodes=30, edges=15,)
g.to_graphviz("../output_4/erdos/generated_30")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Erdos 30 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/erdos/kruskal_30")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Erdos 30 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/erdos/prim_30")

g = factory.build_graph(nodes=100, edges=40,)
g.to_graphviz("../output_4/erdos/generated_100")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Erdos 100 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/erdos/kruskal_100")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Erdos 100 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/erdos/prim_100")



factory.set_builder(GilbertBuilder())

g = factory.build_graph(nodes=30, p=0.1, loops=True)
g.to_graphviz("../output_4/gilbert/generated_30")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Gilbert 30 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/gilbert/kruskal_30")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Gilbert 30 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/gilbert/prim_30")

g = factory.build_graph(nodes=100, p=0.1, loops=True)
g.to_graphviz("../output_4/gilbert/generated_100")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Gilbert 100 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/gilbert/kruskal_100")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Gilbert 100 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/gilbert/prim_100")



factory.set_builder(GeographicBuilder())

g = factory.build_graph(nodes=30, max_dist=0.1, loops=False)
g.to_graphviz("../output_4/geographic/generated_30")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Geographic 30 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/geographic/kruskal_30")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Geographic 30 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/geographic/prim_30")

g = factory.build_graph(nodes=100, max_dist=0.1, loops=False)
g.to_graphviz("../output_4/geographic/generated_100")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Geographic 100 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/geographic/kruskal_100")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Geographic 100 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/geographic/prim_100")



factory.set_builder(BarabasiAlbertBuilder())

g = factory.build_graph(nodes=30, degree=10, loops=False)
g.to_graphviz("../output_4/barabasi/generated_30")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Barabasi 30 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/barabasi/kruskal_30")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Barabasi 30 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/barabasi/prim_30")

g = factory.build_graph(nodes=100, degree=40, loops=False)
g.to_graphviz("../output_4/barabasi/generated_100")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Barabasi 100 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/barabasi/kruskal_100")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Barabasi 100 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/barabasi/prim_100")



factory.set_builder(DorogovtsevMendesBuilder())

g = factory.build_graph(nodes=30)
g.to_graphviz("../output_4/dorogovstev/generated_30")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Dorogovstev 30 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/dorogovstev/kruskal_30")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Dorogovstev 30 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/dorogovstev/prim_30")

g = factory.build_graph(nodes=100)
g.to_graphviz("../output_4/dorogovstev/generated_100")
g_kruskal, mst_kruskal = g.kruskal()
print(f"Dorogovstev 100 nodes -> Kruskal MST: {mst_kruskal}")
g_kruskal.to_graphviz("../output_4/dorogovstev/kruskal_100")
g_prim, mst_prim = g.prim(g.get_node_by_id(list(g.nodes.keys())[0]))
print(f"Dorogovstev 100 nodes -> Prim MST: {mst_prim}")
g_prim.to_graphviz("../output_4/dorogovstev/prim_100")