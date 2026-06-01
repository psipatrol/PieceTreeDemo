import tkinter as tk
import re

from tkinter import messagebox, filedialog, simpledialog

from data.exceptions import BufferNotFoundException
from ui.editor import MyTextField
from data.piecetree import PieceTree
from ui.treeschema import TreeSchema


def get_save_file_path():
    filename = filedialog.asksaveasfilename(
        title="Create file",
        defaultextension=".txt"
    )
    if not filename:
        return None
    return filename


def ask_for_search_regex():
    search_regex = simpledialog.askstring("Search Regex", "Enter search regex")
    if search_regex is not None:
        return search_regex
    return None


def ask_for_search_text():
    search_text = simpledialog.askstring("Search Text", "Enter search text")
    if search_text is not None:
        return re.escape(search_text)
    return None


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("960x640")

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)
        main_frame.grid_rowconfigure(0, weight=2)
        main_frame.grid_rowconfigure(1, weight=3)
        main_frame.grid_columnconfigure(0, weight=1)

        try:
            self.piece_tree = PieceTree()
        except BufferNotFoundException:
            messagebox.showerror("Error", "Piece Tree not found. Please try again.")
            root.destroy()
            return

        self.tree_schema = TreeSchema(main_frame, self.piece_tree)
        self.tree_schema.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

        self.text_field = MyTextField(main_frame, self.piece_tree, self.tree_schema)
        self.text_field.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))

        menubar = tk.Menu(root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Load File", command=lambda : self.load_file())
        file_menu.add_command(label="Save", command=lambda : self.save_file())
        file_menu.add_command(label="Save As", command=lambda : self.save_file(get_save_file_path()))

        tool_menu = tk.Menu(menubar, tearoff=0)
        tool_menu.add_command(label="Search by text", command=lambda : self.text_field.search(ask_for_search_text()))
        tool_menu.add_command(label="Search by regex", command=lambda : self.text_field.search(ask_for_search_regex()))

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Tool", menu=tool_menu)

        self.root.config(menu=menubar)

    def load_file(self):
        filename = filedialog.askopenfilename(
            title="Select file",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
        )
        if not filename:
            return

        try:
            self.piece_tree.load_file(filename)
            self.text_field.render()
            self.tree_schema.render()
            messagebox.showinfo("Success", "File loaded successfully")
        except BufferNotFoundException as e:
            messagebox.showerror("Error", f"Buffer not found. Please reflect on your behaviour. \n{e}")

    def save_file(self, path = None):
        try:
            self.piece_tree.save_file(path)
        except BufferNotFoundException as e:
            messagebox.showerror("Error", f"Buffer not found. Please reflect on your behaviour. \n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
