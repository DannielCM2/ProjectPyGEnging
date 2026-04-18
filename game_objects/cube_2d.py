from engine.game_object import GameObject
from engine.vector2 import Vector2

class Cube2D(GameObject):
    def __init__(self, engine, position=None, size=1, rotation=0):
        super().__init__()

        self.base_vertices = [
            Vector2(0, 0),
            Vector2(0, 1),
            Vector2(1, 1),
            Vector2(1, 0)
        ]

        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

        self.size = size
        self.position = position

        self.engine = engine
        self.speed = 150

        self.target_pos = self.position
        self.moving = False

    def update(self, delta_time):
        self.handle_input()
        if not self.moving:
            return
        
        direction = self.target_pos - self.position
        distance = direction.length()

        if distance > 0.01:
            step = self.speed * delta_time
            if step > distance:
                step = distance

            self.position = self.position + (direction / distance) * step
        else:
            self.position = self.target_pos
            self.moving = False

    def handle_input(self):
        if self.moving:
            return
        
        if self.engine.input.was_pressed('d'):
            self.target_pos = Vector2(self.position.x + 50, self.position.y)
            self.moving = True
        if self.engine.input.was_pressed('a'):
            self.target_pos = Vector2(self.position.x - 50, self.position.y)
            self.moving = True
        if self.engine.input.was_pressed('s'):
            self.target_pos = Vector2(self.position.x, self.position.y + 50)
            self.moving = True
        if self.engine.input.was_pressed('w'):
            self.target_pos = Vector2(self.position.x, self.position.y - 50)
            self.moving = True