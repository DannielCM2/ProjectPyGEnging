from engine.game_object import GameObject
from engine.vector2 import Vector2
import math

class Octagon2D(GameObject):
    def __init__(self, position=None, size=1, rotation=0):
        super().__init__(position=position, size=size, rotation=rotation)

        self.base_vertices = []
        self.edges = []

        sides = 8

        for i in range(sides):
            angle = (2 * math.pi * i) / sides
            x = math.cos(angle)
            y = math.sin(angle)
            self.base_vertices.append(Vector2(x, y))

        for i in range(sides):
            self.edges.append((i, (i + 1) % sides))
