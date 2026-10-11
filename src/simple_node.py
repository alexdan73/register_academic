class SimpleNode:
    __slots__ = ("value", "next")

    def __init__(self, value):
        self.value = value
        self.next = None