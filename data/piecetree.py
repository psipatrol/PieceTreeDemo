from data.buffers import BufferType
from data.node import Node

class PieceTree:
    def __init__(self):
        self.text = "Piece Tree Demo..."
        self.original_buffer_path = "buffers/original_buffer.txt"
        self.added_buffer_path = "buffers/added_buffer.txt"

        self.original_text = ""
        self.added_text = ""

        with open(str(self.original_buffer_path), "r") as f:
            original_text = f.read()

        self.root = Node(buffer_type=BufferType.ORIGINAL, start_pointer=0, length=len(original_text))

    def insert_char(self, index, char):
        if char == '\r':
            char = '\n'
        self.added_text += char

    def get_text(self):
        text = ""
        self.in_order(self.root, text)
        return text

    def in_order(self, node, result):
        if node is None:
            return
        self.in_order(node.left_child, result)
        result += node.text
        self.in_order(node.right_child, result)

    def read_from_buffer(self, node):
        match node.buffer_type:
            case BufferType.ORIGINAL:
                print("orginal")
            case BufferType.ADDED:
                print("added")
            case _:
                print("error")