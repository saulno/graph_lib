from graph.GraphFactory import GraphFactory, GridBuilder

from graph.GraphFactory import BarabasiAlbertBuilder, DorogovtsevMendesBuilder, ErdosRenyiBuilder, GeographicBuilder, GilbertBuilder, GraphFactory, GridBuilder


factory = GraphFactory()



factory.set_builder(GridBuilder())

g = factory.build_graph(columns=5, rows=6, directed=True)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/grid/generated_30")
g_bfs.to_graphviz("../output_2/grid/bfs_30")
g_dfsi.to_graphviz("../output_2/grid/dfs_iterative_30")
g_dfsr.to_graphviz("../output_2/grid/dfs_recursive_30")

g = factory.build_graph(columns=10, rows=10, directed=True)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/grid/generated_100")
g_bfs.to_graphviz("../output_2/grid/bfs_100")
g_dfsi.to_graphviz("../output_2/grid/dfs_iterative_100")
g_dfsr.to_graphviz("../output_2/grid/dfs_recursive_100")

g = factory.build_graph(columns=50, rows=10, directed=True)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/grid/generated_500")
g_bfs.to_graphviz("../output_2/grid/bfs_500")
g_dfsi.to_graphviz("../output_2/grid/dfs_iterative_500")
g_dfsr.to_graphviz("../output_2/grid/dfs_recursive_500")



factory.set_builder(ErdosRenyiBuilder())

g = factory.build_graph(nodes=30, edges=15,)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/erdos/generated_30")
g_bfs.to_graphviz("../output_2/erdos/bfs_30")
g_dfsi.to_graphviz("../output_2/erdos/dfs_iterative_30")
g_dfsr.to_graphviz("../output_2/erdos/dfs_recursive_30")

g = factory.build_graph(nodes=100, edges=40,)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/erdos/generated_100")
g_bfs.to_graphviz("../output_2/erdos/bfs_100")
g_dfsi.to_graphviz("../output_2/erdos/dfs_iterative_100")
g_dfsr.to_graphviz("../output_2/erdos/dfs_recursive_100")

g = factory.build_graph(nodes=500, edges=300,)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/erdos/generated_500")
g_bfs.to_graphviz("../output_2/erdos/bfs_500")
g_dfsi.to_graphviz("../output_2/erdos/dfs_iterative_500")
g_dfsr.to_graphviz("../output_2/erdos/dfs_recursive_500")



factory.set_builder(GilbertBuilder())

g = factory.build_graph(nodes=30, p=0.1, loops=True)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/gilbert/generated_30")
g_bfs.to_graphviz("../output_2/gilbert/bfs_30")
g_dfsi.to_graphviz("../output_2/gilbert/dfs_iterative_30")
g_dfsr.to_graphviz("../output_2/gilbert/dfs_recursive_30")

g = factory.build_graph(nodes=100, p=0.1, loops=True)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/gilbert/generated_100")
g_bfs.to_graphviz("../output_2/gilbert/bfs_100")
g_dfsi.to_graphviz("../output_2/gilbert/dfs_iterative_100")
g_dfsr.to_graphviz("../output_2/gilbert/dfs_recursive_100")

g = factory.build_graph(nodes=500, p=0.1, loops=True)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/gilbert/generated_500")
g_bfs.to_graphviz("../output_2/gilbert/bfs_500")
g_dfsi.to_graphviz("../output_2/gilbert/dfs_iterative_500")
g_dfsr.to_graphviz("../output_2/gilbert/dfs_recursive_500")



factory.set_builder(GeographicBuilder())

g = factory.build_graph(nodes=30, max_dist=0.1, loops=False)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/geographic/generated_30")
g_bfs.to_graphviz("../output_2/geographic/bfs_30")
g_dfsi.to_graphviz("../output_2/geographic/dfs_iterative_30")
g_dfsr.to_graphviz("../output_2/geographic/dfs_recursive_30")

g = factory.build_graph(nodes=100, max_dist=0.1, loops=False)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/geographic/generated_100")
g_bfs.to_graphviz("../output_2/geographic/bfs_100")
g_dfsi.to_graphviz("../output_2/geographic/dfs_iterative_100")
g_dfsr.to_graphviz("../output_2/geographic/dfs_recursive_100")

g = factory.build_graph(nodes=500, max_dist=0.1, loops=False)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/geographic/generated_500")
g_bfs.to_graphviz("../output_2/geographic/bfs_500")
g_dfsi.to_graphviz("../output_2/geographic/dfs_iterative_500")
g_dfsr.to_graphviz("../output_2/geographic/dfs_recursive_500")



factory.set_builder(BarabasiAlbertBuilder())

g = factory.build_graph(nodes=30, degree=10, loops=False)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/barabasi/generated_30")
g_bfs.to_graphviz("../output_2/barabasi/bfs_30")
g_dfsi.to_graphviz("../output_2/barabasi/dfs_iterative_30")
g_dfsr.to_graphviz("../output_2/barabasi/dfs_recursive_30")

g = factory.build_graph(nodes=100, degree=40, loops=False)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/barabasi/generated_100")
g_bfs.to_graphviz("../output_2/barabasi/bfs_100")
g_dfsi.to_graphviz("../output_2/barabasi/dfs_iterative_100")
g_dfsr.to_graphviz("../output_2/barabasi/dfs_recursive_100")

g = factory.build_graph(nodes=500, degree=200, loops=False)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/barabasi/generated_500")
g_bfs.to_graphviz("../output_2/barabasi/bfs_500")
g_dfsi.to_graphviz("../output_2/barabasi/dfs_iterative_500")
g_dfsr.to_graphviz("../output_2/barabasi/dfs_recursive_500")



factory.set_builder(DorogovtsevMendesBuilder())

g = factory.build_graph(nodes=30)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/dorogovstev/generated_30")
g_bfs.to_graphviz("../output_2/dorogovstev/bfs_30")
g_dfsi.to_graphviz("../output_2/dorogovstev/dfs_iterative_30")
g_dfsr.to_graphviz("../output_2/dorogovstev/dfs_recursive_30")

g = factory.build_graph(nodes=100)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/dorogovstev/generated_100")
g_bfs.to_graphviz("../output_2/dorogovstev/bfs_100")
g_dfsi.to_graphviz("../output_2/dorogovstev/dfs_iterative_100")
g_dfsr.to_graphviz("../output_2/dorogovstev/dfs_recursive_100")

g = factory.build_graph(nodes=500)
g_bfs = g.bfs(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsi = g.dfs_iterative(g.get_node_by_id(list(g.nodes.keys())[0]))
g_dfsr = g.dfs_recursive(g.get_node_by_id(list(g.nodes.keys())[0]))
g.to_graphviz("../output_2/dorogovstev/generated_500")
g_bfs.to_graphviz("../output_2/dorogovstev/bfs_500")
g_dfsi.to_graphviz("../output_2/dorogovstev/dfs_iterative_500")
g_dfsr.to_graphviz("../output_2/dorogovstev/dfs_recursive_500")