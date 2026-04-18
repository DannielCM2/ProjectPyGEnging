import glfw
import moderngl as mgl

class Window:
    def __init__(self, width=1280, height=720, title="PyGEngine"):
        self.width = width
        self.height = height
        self.title = title

        if not glfw.init():
            raise Exception("GLFW initialization failed")

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.window = glfw.create_window(
            self.width,
            self.height,
            self.title,
            None,
            None
        )

        if not self.window:
            glfw.terminate()
            raise Exception("Failed to create GLFW window")

        glfw.make_context_current(self.window)
        self.ctx = mgl.create_context(require=330)

        if self.ctx is None:
            glfw.terminate()
            raise Exception("Failed to create ModernGL context")

    def should_close(self):
        return glfw.window_should_close(self.window)

    def poll_events(self):
        glfw.poll_events()

    def get_pressed_keys(self):
        pressed = set()

        for key in range(32, 348):
            if glfw.get_key(self.window, key) == glfw.PRESS:
                pressed.add(key)

        return pressed

    def swap_buffers(self):
        glfw.swap_buffers(self.window)

    def destroy(self):
        self.ctx.release()
        glfw.terminate()