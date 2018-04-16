from Edge import Edge
from Vertex import Vertex

class Graph:
    """Simple Graph Library"""
    def __init__(self):
        self.edges = list()
        self.vertices = list()

    def add_edge(self, edge):
        if not isinstance(edge, Edge):
            raise ValueError("edge must be of type Edge")
        self.edges.append(edge)

        v1 = edge.to_vertex
        v2 = edge.from_vertex
        self.add_vertex(v1)
        self.add_vertex(v2)

    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            raise ValueError('vertex must be of type Vertex')
        if vertex in self.vertices:
            raise ValueError("Vertex already exists in graph")
        
        self.vertices.append(vertex)

    def remove_edge(self, edge):
        try:
            self.edges.remove(edge)
        except ValueError:
            pass
            #do nothing for now we just can't remove it from the graph

    def remove_vertex(self, vertex):
        self.vertices.remove(vertex)
        #find all edges that have that vertex and remove those as well
        for edge in self.edges: 
                if vertex == edge.from_vertex or vertex == edge.to_vertex:
                    self.edges.remove(edge)
    
    