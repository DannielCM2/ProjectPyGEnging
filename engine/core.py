from engine.events import Input
from engine.renderer import Renderer
from engine.scene_manager import SceneManager
import time

class Game:
    def __init__(self, title="Game", width=1280, height=720, fps=60):
        self.title = title
        self.width = width
        self.heigth = height
        self.fps = fps
        self.frame_duration = 1 / fps
        self.running = True

        self.scene_manager = SceneManager(self)
        self.input = Input()
        self.renderer = Renderer()
        self.renderer.bind_keys(self.input)

        self.fps_counter = 0
        self.fps_timer = 0
        self.current_fps = 0

    def run(self):
        self.last_time = time.time()
        while self.running:
            current_time = time.time()
            delta_time = current_time - self.last_time
            self.last_time = current_time

            self.fps_counter += 1
            self.fps_timer += delta_time

            if self.fps_timer >= 1.0:
                self.current_fps = self.fps_counter
                self.fps_counter = 0
                self.fps_timer = 0
            
            self.update(delta_time)
            self.input.reset()
            self.render()

            elapsed = time.time() - current_time
            time.sleep(max(0, self.frame_duration - elapsed))
    
    def update(self, delta_time):
        if self.scene_manager.current_scene:
            for obj in self.scene_manager.current_scene.objects:
                obj.update(delta_time)

    def render(self):
        self.renderer.clear()

        if self.scene_manager.current_scene:
            for obj in self.scene_manager.current_scene.objects:
               self.renderer.render_geometry(obj)
        
        self.renderer.draw_debug(
           self.current_fps,
           self.input.keys_down
        )

        self.renderer.update()