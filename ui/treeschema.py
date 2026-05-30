import tkinter as tk

def interpolate(in_range, out_range, value):
    return out_range[0] + (value - in_range[0]) / (in_range[1] - in_range[0]) * (out_range[1] - out_range[0])

class TreeSchema(tk.Frame):
    def __init__(self, root, tree):
        super().__init__(root, bg="white", bd=2, relief="groove")

        self.tree = tree
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.render)

    def render(self, event = None):
        self.canvas.delete("all")
        self.draw()

    def draw(self):
        padding = 25
        width = self.winfo_width() - padding*2

        start_y = 15
        step_y = 30

        text_padding = 5

        tree_spread = self.tree.get_spread(self.tree.root)
        max_offset = 1 - 1 / 2**(tree_spread-1)

        gen = self.tree.in_order_gen(self.tree.root)

        for n in gen:
            if max_offset == 0:
                x0 = width/2 + padding
            else:
                x0 = width/2 + interpolate((0, max_offset), (0, width/2), n[1]) + padding
            y0 = start_y + step_y * (n[2]-1)

            text = self.canvas.create_text(x0, y0, text=str(self.tree.read_from_buffer(n[0])), anchor="center")
            bbox = self.canvas.bbox(text)

            if n[0].left_child is not None:
                child_offset = n[1] - 1 / 2**n[2]
                child_y = start_y + step_y * n[2]
                child_x = width/2 + interpolate((0, max_offset), (0, width/2), child_offset) + padding
                self.canvas.create_line(x0, y0, child_x, child_y, width=2, fill="#A7A7A7")
            if n[0].right_child is not None:
                child_offset = n[1] + 1 / 2**n[2]
                child_y = start_y + step_y * n[2]
                child_x = width/2 + interpolate((0, max_offset), (0, width/2), child_offset) + padding
                self.canvas.create_line(x0, y0, child_x, child_y, width=2, fill="#A7A7A7")


            self.canvas.create_rectangle(bbox[0] - text_padding, bbox[1] - text_padding, bbox[2] + text_padding, bbox[3] + text_padding, fill="#A7A7A7")
            self.canvas.tag_raise(text)
