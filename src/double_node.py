class DoubleNode:
    __slots__ = ("value", "previous", "next")

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None