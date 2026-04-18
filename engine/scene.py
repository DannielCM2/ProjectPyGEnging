class Scene:
    def __init__(self, engine):
        self.objects = []
        self.engine = engine
        self.input = engine.input
        self.scene_manager = engine.scene_manager

    def on_load(self):
        pass
    
    def update(self, dt):
        pass

    def on_enter(self):
        pass

    def on_exit(self):
        pass