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
            self.tree.insert_char(absolute_index, event.char)
            self.render()
            self.schema.render()
            return "break"

    def render(self):
        self.cursor_index = self.text.index(tk.INSERT)
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", self.tree.get_text())
        if self.cursor_index != 0:
            self.text.mark_set("insert", f"{self.cursor_index.split(".")[0]}.%d" % (int(self.cursor_index.split(".")[1]) + 1))
