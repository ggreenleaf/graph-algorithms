import Edge
import Vertex

class Graph:
    """Simple Graph Library"""
    def __init__(self):
        self.edges = list()
        self.vertices = list()

    def add_edge(self, edge):
        self.edges.append(edge)

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
    
    