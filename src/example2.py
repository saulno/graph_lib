from graph.GraphFactory import ErdosRenyiBuilder, GraphFactory, GridBuilder


factory = GraphFactory()

factory.set_builder(GridBuilder())
g = factory.build_graph(columns=5, rows=3, directed=True)
g.to_graphviz("grid")

factory.set_builder(ErdosRenyiBuilder())
g = factory.build_graph(nodes=100, edges=40,)
g.to_graphviz("erdosloop")

factory.set_builder(ErdosRenyiBuilder())
g = factory.build_graph(nodes=100, edges=40, loops=True)
g.to_graphviz("erdosnoloop")

# factory.set_builder(GridBuilder())
# g = factory.build_graph(columns=5, rows=3, directed=True)
# g.to_graphviz("g2")

