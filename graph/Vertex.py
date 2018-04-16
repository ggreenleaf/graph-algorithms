class Vertex:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == self.name