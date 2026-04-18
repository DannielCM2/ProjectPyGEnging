from .scene import Scene

class SceneManager:
    def __init__(self, engine):
        self.scene_stack = []
        self.engine = engine
        self.input = engine.input
        self.scene_cache = {}

    def load_scene(self, name):
        scene = self.scene_cache.get(name)

        if scene is None:
            raise ValueError(f"Scene '{name}' not found")

        self.scene_stack.append(scene)
        scene.on_enter()

    def unload_scene(self):
        if self.scene_stack:
            self.scene_stack.pop()

    def cache_scene(self, name, scene):
        self.scene_cache[name] = scene(self.engine)