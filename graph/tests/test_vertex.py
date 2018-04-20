import unittest
from ..Vertex import Vertex

class TestVertexClass(unittest.TestCase):

    def test_vertex_equal(self):
        vertex_one = Vertex('a')
        vertex_two = Vertex('a')
        self.assertEqual(vertex_one, vertex_two)
    
    def test_vertex_not_equal(self):
        vertex_one = Vertex('a')
        vertex_two = Vertex('b')
        self.assertFalse(vertex_one == vertex_two)