import tkinter as tk
from data.piecetree import PieceTree

class TreeSchema(tk.Frame):
    def __init__(self, root, tree):
        super().__init__(root, bg="white", bd=2, relief="groove")

        self.node_size = 25

        self.tree = tree

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.render()

    def render(self):
        self.canvas.delete("all")
        self.draw(self.tree.root, 100, 10)

    # def draw(self, node, current_x, current_y):
    #     if node is None:
    #         return
    #     self.canvas.create_oval(current_x, current_y, current_x + self.node_size, current_y + self.node_size, fill="red")
    #     self.canvas.create_text(current_x, current_y + self.node_size, text=str(node.buffer_type))
    #     self.draw(node.left_child, current_x - 25, current_y + 25)
    #     self.draw(node.right_child, current_x + 25, current_y + 25)
    #     #WTF?

    def draw(self, node, current_x, current_y):
        gen = self.tree.in_order_gen(node)
        next(gen)

        step_y = 30
        center_x = 400
        for n in gen:
            self.canvas.create_oval(center_x + n[1], 0 + step_y * n[2], center_x + n[1] + self.node_size, 0 + step_y * n[2] + self.node_size,fill="red")
            self.canvas.create_text(center_x + n[1], 0 + step_y * n[2] + self.node_size, text=str(n[0].buffer_type))
            print(n[1])

