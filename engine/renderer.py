class Renderer:
    def __init__(self, ctx):
        self.ctx = ctx

    def render(self, scene):
        self.ctx.clear(0.1, 0.1, 0.1)
        
        if scene is None:
            return
        
        for obj in scene.objects:
            obj.render()
        