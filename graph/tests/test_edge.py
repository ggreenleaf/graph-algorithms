import unittest
from ..Edge import Edge
from ..Vertex import Vertex


class TestEdgeClass(unittest.TestCase):
    def test_edge_equals(self):
        edge_one = Edge(1, Vertex('a'), Vertex('b'))
        edge_two = Edge(1, Vertex('a'), Vertex('b'))
        edge_one.name = edge_two.name
        self.assertEqual(edge_one,edge_two)
    
    def test_edge_not_equals(self):
        edge_one = Edge(1, Vertex('a'), Vertex('b'))
        edge_two = Edge(1, Vertex('a'), Vertex('b'))
        self.assertNotEqual(edge_one,edge_two)

