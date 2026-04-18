from engine.events import Input
from engine.renderer import Renderer
from engine.scene_manager import SceneManager
from engine.window import Window
import time

class Game:
    def __init__(self, title="Game", width=1280, height=720, fps=120):
        self.title = title
        self.width = width
        self.heigth = height
        self.fps = fps
        self.frame_duration = 1 / fps
        self.running = True

        self.window = Window()
        self.renderer = Renderer(self.window.ctx)
        self.scene_manager = SceneManager(self)
        self.input = Input()

    def run(self):
        self.last_time = time.perf_counter()

        while self.running:
            frame_start = time.perf_counter()

            delta_time = frame_start - self.last_time
            self.last_time = frame_start
            
            self.window.poll_events()
            if self.window.should_close():
                self.running = False

            self.renderer.render(self.scene_manager.current_scene)
            self.window.swap_buffers()

            frame_time = time.perf_counter() - frame_start
            sleep_time = self.frame_duration - frame_time

            if sleep_time > 0:
                time.sleep(sleep_time)
        
        self.window.destroy()