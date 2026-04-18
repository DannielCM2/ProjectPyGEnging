import numpy as np
import moderngl as mgl
from engine.game_object import GameObject

class Cube3D(GameObject):
    def __init__(self, ctx):
        super().__init__(ctx)
        self._build()

    def _build(self):
        vertices = np.array([
            -0.5, -0.5,  0.5,
             0.5, -0.5,  0.5,
             0.5,  0.5,  0.5,
            -0.5,  0.5,  0.5,

            -0.5, -0.5, -0.5,
             0.5, -0.5, -0.5,
             0.5,  0.5, -0.5,
            -0.5,  0.5, -0.5,
        ], dtype="f4")

        indices = np.array([
            0, 1, 2,  0, 2, 3,
            1, 5, 6,  1, 6, 2,
            5, 4, 7,  5, 7, 6,
            4, 0, 3,  4, 3, 7,
            3, 2, 6,  3, 6, 7,
            4, 5, 1,  4, 1, 0 
        ], dtype="i4")

        self.vbo = self.ctx.buffer(vertices.tobytes())
        self.ibo = self.ctx.buffer(indices.tobytes())

        self.program = self.ctx.program(
            vertex_shader="""
                #version 330

                in vec3 in_position;

                void main() {
                    gl_Position = vec4(in_position, 1.0);
                }
            """,
            fragment_shader="""
                #version 330

                out vec4 color;

                void main() {
                    color = vec4(0.2, 0.7, 1.0, 1.0);
                }
            """
        )

        self.vao = self.ctx.vertex_array(
            self.program,
            [(self.vbo, "3f", "in_position")],
            self.ibo
        )

    def render(self):
        self.vao.render(mode=mgl.TRIANGLES)