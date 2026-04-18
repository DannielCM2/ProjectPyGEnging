from .vector2 import Vector2
import math

class GameObject:
    def __init__(self):
        self._position = Vector2(0, 0)
        self._size = 0
        self._rotation = 0
        self._base_vertices = []
        self._transformed_vertices = []
        self._edges = []
        self._dirty = False

    @property
    def base_vertices(self):
        return self._base_vertices
    
    @base_vertices.setter
    def base_vertices(self, vertices):
        self._base_vertices = vertices
        self._dirty = True
    
    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self, edges):
        self._edges = edges
        self._dirty = True

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position
        self._dirty = True

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
        self._dirty = True

    def get_transformed_vertices(self):
        if self._dirty:
            self._transform_vertices()
        return self._transformed_vertices
    
    def _transform_vertices(self):
        self._dirty = False

        rad = math.radians(self._rotation)
        cos_r = math.cos(rad)
        sin_r = math.sin(rad)

        if len(self._transformed_vertices) != len(self._base_vertices):
            self._transformed_vertices = [Vector2(0, 0) for _ in self._base_vertices]

        for i, v in enumerate(self._base_vertices):
            x = v.x * self._size
            y = v.y * self._size

            rx = x * cos_r - y * sin_r
            ry = x * sin_r + y * cos_r

            tv = self._transformed_vertices[i]
            tv.x = rx + self._position.x
            tv.y = ry + self._position.y

    def update(self):
        pass