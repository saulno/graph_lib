class Node:
    class_id = 0

    def __init__(self, id=None, position=(0,0), label="", **kwargs) -> None:
        self.id = Node.class_id if not id else id
        self.pos = position
        self.label = label
        self.attr = kwargs if len(kwargs) > 0 else {}

        Node.class_id += 1

    def __str__(self) -> str:
        return f"Node({self.id}, {self.pos}, {self.label}, {self.attr})"