from game_objects.cube_2d import Cube2D
from game_objects.octagon_2d import Octagon2D
from engine.vector2 import Vector2
from engine.scene import Scene

class Level1(Scene):
    def __init__(self, engine):
        super().__init__(engine=engine)

    def scene_objects(self):
        self.objects.append(Cube2D(self.engine, position=Vector2(50, 50), size=50))
        # self.objects.append(Cube2D(self.engine, position=Vector2(40, 40), size=80))
        # self.objects.append(Octagon2D(position=Vector2(90, 90), size=80, rotation=10))