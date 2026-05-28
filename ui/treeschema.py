import tkinter as tk
from data.piecetree import PieceTree

class TreeSchema(tk.Frame):
    def __init__(self, root, tree):
        super().__init__(root, bg="white", bd=2, relief="groove")
        self.tree = tree

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.render()

    def render(self):
        self.canvas.delete("all")
        self.draw_in_order(self.tree.root, 100, 0)

    def draw_in_order(self, node, current_x, current_y):
        if node is None:
            return
        self.canvas.create_oval(current_x, current_y, current_x + 80, current_y + 80, fill="red")
        self.draw_in_order(node.left_child, current_x - 25, current_y - 25)
        self.draw_in_order(node.right_child, current_x + 25, current_y - 25)
        #WTF?
