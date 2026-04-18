from game.game_objects.cube_3d import Cube3D
from engine.scene import Scene
import glfw

class Level1(Scene):
    def __init__(self, engine):
        super().__init__(engine=engine)
        self.on_load()

    def on_load(self):
        self.objects.append(Cube3D(self.engine.window.ctx))
        print(self.objects)

    def update(self, dt):
        if self.input.was_pressed(glfw.KEY_ESCAPE):
            print("Loading level2")
            self.scene_manager.load_scene('level2')