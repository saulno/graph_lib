class Edge:
    class_id = 0

    def __init__(self, source=None, target=None, weight=0, id=None, label="", **kwargs) -> None:
        self.source = source
        self.target = target
        self.weight = weight
        self.id = Edge.class_id if not id else id
        self.label = label
        self.attr = kwargs if len(kwargs) > 0 else {}

        Edge.class_id += 1

    def __str__(self) -> str:
        return f"Edge({self.id}, {self.source}, {self.target}, {self.weight}, {self.label}, {self.attr})"
    