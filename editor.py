import tkinter as tk

class MyTextField(tk.Frame):
    def __init__(self, root, tree):
        super().__init__(root)
        self.tree = tree
        self.text = tk.Text(self)
        self.text.pack(fill="both", expand=True)

        self.text.bind("<Key>", self.on_click)
        self.render()

    def on_click(self, event):
        print(event)
        self.tree.insert_char(event.char)
        self.render()
        return "break"

    def render(self):
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", self.tree.get_text())
