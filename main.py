import tkinter as tk
from tkinter import messagebox

from data.exceptions import BufferNotFoundException
from ui.editor import MyTextField
from data.piecetree import PieceTree
from ui.treeschema import TreeSchema

class App:
    def __init__(self, root):
        self.root = root

        self.root.geometry("960x640")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.grid_rowconfigure(0, weight=2)
        self.main_frame.grid_rowconfigure(1, weight=3)
        self.main_frame.grid_columnconfigure(0, weight=1)

        try:
            self.piece_tree = PieceTree()
        except BufferNotFoundException:
            messagebox.showerror("Error", "Piece Tree not found. Please try again.")
            self.root.destroy()
            return

        self.tree_schema = TreeSchema(self.main_frame, self.piece_tree)
        self.tree_schema.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

        self.text_field = MyTextField(self.main_frame, self.piece_tree, self.tree_schema)
        self.text_field.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
