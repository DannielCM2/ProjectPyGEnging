from .scene import Scene

class SceneManager:
    def __init__(self, engine):
        self.current_scene = None
        self.engine = engine

    def load_scene(self, scene):
        if not issubclass(scene, Scene):
            raise TypeError(f"Tried to switch to non-Scene ({type(scene).__name__})")
        self.current_scene = scene(self.engine)