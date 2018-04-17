from Vertex import Vertex
from uuid import uuid1

class Edge:
    """A simple Edge library"""
    def __init__(self, weight, from_vertex, to_vertex):
        if (not isinstance(from_vertex, Vertex) or not isinstance(to_vertex, Vertex)):
            raise TypeError('from or to vertex must be of Vertex Type')
        self.weight = weight
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.name = uuid1() #does this guarentee a unique id?

    #we want to find it by name cause multiple edges with the same from,to vertex and weight
    #are allowed in our graph
    def __eq__(self, other):
        if isinstance(other, Edge):
            return self.name == other.name
    