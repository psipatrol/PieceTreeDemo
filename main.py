import tkinter as tk

from ui.editor import MyTextField
from data.piecetree import PieceTree
from ui.treeschema import TreeSchema

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("960x640")

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    main_frame.grid_rowconfigure(0, weight=2)
    main_frame.grid_rowconfigure(1, weight=3)
    main_frame.grid_columnconfigure(0, weight=1)

    piece_tree = PieceTree()

    tree_schema = TreeSchema(main_frame, piece_tree)
    tree_schema.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

    text_field = MyTextField(main_frame, piece_tree)
    text_field.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))

    root.mainloop()