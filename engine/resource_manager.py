class ResourceManager:
    def __init__(self, game=None):
        self.game = game
        self.cache = {}

    def load(self, name, loader_func):
        if name in self.cache:
            return self.cache[name]

        resource = loader_func(name)
        self.cache[name] = resource
        return resource