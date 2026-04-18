import numpy as np
import moderngl as mgl
from engine.game_object import GameObject

class Cube2D(GameObject):
    def __init__(self, ctx, x=0.0, y=0.0, size=0.5):
        super().__init__(ctx)

        self.x = x
        self.y = y
        self.size = size

        self._build()

    def _build(self):
        s = self.size

        vertices = np.array([
            self.x - s, self.y - s,
            self.x + s, self.y - s,
            self.x + s, self.y + s,

            self.x - s, self.y - s,
            self.x + s, self.y + s,
            self.x - s, self.y + s,
        ], dtype="f4")

        self.vbo = self.ctx.buffer(vertices.tobytes())

        self.program = self.ctx.program(
            vertex_shader="""
                #version 330
                in vec2 in_position;

                void main() {
                    gl_Position = vec4(in_position, 0.0, 1.0);
                }
            """,
            fragment_shader="""
                #version 330
                out vec4 color;

                void main() {
                    color = vec4(1.0);
                }
            """
        )

        self.vao = self.ctx.vertex_array(
            self.program,
            [(self.vbo, "2f", "in_position")]
        )

    def render(self):
        self.vao.render(mode=mgl.TRIANGLES)