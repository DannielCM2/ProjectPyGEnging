from game.game_objects.cube_3d import Cube3D
from engine.scene import Scene

class Level1(Scene):
    def __init__(self, engine):
        super().__init__(engine=engine)

    def scene_objects(self):
        self.objects.append(Cube3D(self.engine.window.ctx))