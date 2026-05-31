import tkinter as tk

class MyTextField(tk.Frame):
    def __init__(self, root, tree, schema):
        super().__init__(root)
        self.tree = tree
        self.schema = schema
        self.text = tk.Text(self)
        self.text.pack(fill="both", expand=True)
        self.text.bind("<Key>", self.on_click)

        self.cursor_index = 0

        self.render()

    def on_click(self, event):
        self.cursor_index = self.text.index(tk.INSERT)
        chars_count = self.text.count("1.0", self.cursor_index, "chars") or (0,)
        absolute_index = chars_count[0]
        if 8 <= event.state <= 12:
            if event.keysym == "BackSpace":
                if absolute_index > 0:
                    self.tree.delete_at_index(absolute_index - 1)
                    self.render(absolute_index - 1)
                    self.schema.render()
                return "break"
            else:
                if event.char:
                    self.tree.insert_char(absolute_index, event.char)
                    self.render(absolute_index + 1)
                    self.schema.render()
                return "break"

    def render(self, new_index=None):
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", self.tree.get_text())
        if new_index is not None:
            self.text.mark_set("insert", f"1.0+{new_index}c")

