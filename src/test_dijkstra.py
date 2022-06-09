from graph.GraphFactory import GraphFactory, GridBuilder

from graph.GraphFactory import BarabasiAlbertBuilder, DorogovtsevMendesBuilder, ErdosRenyiBuilder, GeographicBuilder, GilbertBuilder, GraphFactory, GridBuilder


factory = GraphFactory()



factory.set_builder(GridBuilder())

g = factory.build_graph(columns=5, rows=6, directed=False)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/grid/generated_30")
g_dijkstra.to_graphviz("../output_3/grid/dijkstra_30")

g = factory.build_graph(columns=50, rows=10, directed=False)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/grid/generated_500")
g_dijkstra.to_graphviz("../output_3/grid/dijkstra_500")



factory.set_builder(ErdosRenyiBuilder())

g = factory.build_graph(nodes=30, edges=15,)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/erdos/generated_30")
g_dijkstra.to_graphviz("../output_3/erdos/dijkstra_30")

g = factory.build_graph(nodes=500, edges=300,)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/erdos/generated_500")
g_dijkstra.to_graphviz("../output_3/erdos/dijkstra_500")



factory.set_builder(GilbertBuilder())

g = factory.build_graph(nodes=30, p=0.1, loops=True)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/gilbert/generated_30")
g_dijkstra.to_graphviz("../output_3/gilbert/dijkstra_30")

g = factory.build_graph(nodes=500, p=0.1, loops=True)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/gilbert/generated_500")
g_dijkstra.to_graphviz("../output_3/gilbert/dijkstra_500")



factory.set_builder(GeographicBuilder())

g = factory.build_graph(nodes=30, max_dist=0.1, loops=False)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/geographic/generated_30")
g_dijkstra.to_graphviz("../output_3/geographic/dijkstra_30")

g = factory.build_graph(nodes=500, max_dist=0.1, loops=False)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/geographic/generated_500")
g_dijkstra.to_graphviz("../output_3/geographic/dijkstra_500")



factory.set_builder(BarabasiAlbertBuilder())

g = factory.build_graph(nodes=30, degree=10, loops=False)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/barabasi/generated_30")
g_dijkstra.to_graphviz("../output_3/barabasi/dijkstra_30")

g = factory.build_graph(nodes=500, degree=200, loops=False)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/barabasi/generated_500")
g_dijkstra.to_graphviz("../output_3/barabasi/dijkstra_500")



factory.set_builder(DorogovtsevMendesBuilder())

g = factory.build_graph(nodes=30)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/dorogovstev/generated_30")
g_dijkstra.to_graphviz("../output_3/dorogovstev/dijkstra_30")

g = factory.build_graph(nodes=500)
g_dijkstra = g.dijkstra(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_3/dorogovstev/generated_500")
g_dijkstra.to_graphviz("../output_3/dorogovstev/dijkstra_500")