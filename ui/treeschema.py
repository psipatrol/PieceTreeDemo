import tkinter as tk

class TreeSchema(tk.Frame):
    def __init__(self, root, tree):
        super().__init__(root, bg="white", bd=2, relief="groove")
        self.tree = tree

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True)
        self.render()

    def render(self):
        self.canvas.delete("all")
        self.canvas.create_oval(10, 10, 80, 80, fill="red")
        self.canvas.create_oval(100, 100, 180, 180, fill="red")
