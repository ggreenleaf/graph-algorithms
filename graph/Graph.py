from Edge import Edge
from Vertex import Vertex


class Graph:
    """Simple Graph Library"""
    def __init__(self):
        self.edges = {}
        self.vertices = {}

    def _add_edge(self, edge):
        self.edges[edge.name] = edge
    
    def _remove_edge(self, edge):
        self.edges.pop(edge.name)

    def _add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex

    def _remove_vertex(self, vertex):
        self.vertices.pop(vertex.name)

    def get_vertex(self, name):
        if not self.has_vertex(name):
            raise ValueError('Vertex does not exist in graph')
        return self.vertices[name]

    def get_edge(self, name):
        edge = self.get_edge(name)
        if edge is None:
            return
        return edge

    def has_vertex(self, name):
        return name in self.vertices.keys()

    def create_new_edge(self, name, from_v, to_v):
        if not isinstance(from_v, Vertex) or not isinstance(to_v, Vertex):
            raise ValueError('')

    def remove_vertex(self, name):
        vertex = self.get_vertex(name)
        if (vertex is None):
            return
        try: 
            self._remove_vertex(vertex)
        except KeyError: 
            #silently fail and continue
            #just dont remove from the graph for now
            return

    def remove_edge(self, name):
        edge = self.get_edge(name)
        if (edge is None):
            return

        try:
            self._remove_edge(edge)
        except KeyError:
            #silently fail and continue
            #just dont remove from the graph for now
            return
    
    