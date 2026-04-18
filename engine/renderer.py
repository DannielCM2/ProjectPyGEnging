import tkinter as tk
from .game_object import GameObject

class Renderer:
    def __init__(self, width=600, height=540, title="Game"):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title(title)
        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg="blue",
            highlightthickness=0
        )
        self.root.resizable(False, False)
        self.canvas.pack(expand=True)
        
        self.debug_text_id = None

    def clear(self):
        self.canvas.delete("all")

    def update(self):
        self.root.update()

    def render_geometry(self, obj):
        if not isinstance(obj, GameObject):
            print(f"Warning: Tried to render non-GameObject ({type(obj).__name__})")
            return

        verts = obj.get_transformed_vertices()

        for start, end in obj.edges:
            p1 = verts[start]
            p2 = verts[end]

            self.canvas.create_line(
                p1.x, p1.y,
                p2.x, p2.y
            )

    def draw_debug(self, fps, keys):
        text = f"FPS: {fps} | Keys: {', '.join(keys)}"

        self.debug_text_id = self.canvas.create_text(
            10, 10,
            anchor="nw",
            text=text,
            fill="red",
            font=("Consolas", 14)
        )

    def bind_keys(self, input_system):
        self.root.bind("<KeyPress>", lambda e: input_system.key_down(e.keysym))
        self.root.bind("<KeyRelease>", lambda e: input_system.key_up(e.keysym))