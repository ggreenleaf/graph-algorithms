from .Edge import Edge
from .Vertex import Vertex

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

    def add_vertex(self, name):
        if self.has_vertex(name):
            raise ValueError('Vertex name already exists')
        vertex = Vertex(name)
        self._add_vertex(vertex)
    
    def add_edge(self, weight, from_name, to_name):
        from_v = self.get_vertex(from_name)
        to_v = self.get_vertex(to_name)
        edge = Edge(weight, from_v, to_v)
        self._add_edge(edge)

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

    def get_outgoing_edges(self, vertex_name):
        return [edge.from_vertex.name == vertex_name for edge in self.edges]

    def get_incoming_edges(self, vertex_name):
        return [edge.to_vertex.name == vertex_name for edge in self.edges]

    def get_edges(self, vertex_name):
        outgoing = self.get_outgoing_edges(vertex_name)
        incoming = self.get_incoming_edges(vertex_name)
        return outgoing + incoming

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