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
            self.original_text = f.read()

        self.root = Node(buffer_type=BufferType.ORIGINAL, start_pointer=0, length=len(self.original_text))

    def insert_char(self, index, char):
        if char == '\r':
            char = '\n'
        self.added_text += char

        buffer_pointer = len(self.added_text) - 1

        print(f"inserting {char} at index {index}")
        self.insert_to_tree(index, buffer_pointer, self.root)

    def insert_to_tree(self, index, buffer_pointer, node, offset = 0):
        if node is None:
            return

        left_subtree_len = self.get_subtree_len(node.left_child)
        current_node_start = offset + left_subtree_len
        current_node_end = current_node_start + node.length

        #go left
        if index <= current_node_start:
            if node.left_child is None:
                node.left_child = Node(buffer_type=BufferType.ADDED, start_pointer=buffer_pointer, length=1)
            else:
                self.insert_to_tree(index, buffer_pointer, node.left_child, offset)

        #go right
        if index >= current_node_end:
            if node.right_child is None:
                node.right_child = Node(buffer_type=BufferType.ADDED, start_pointer=buffer_pointer, length=1)
            else:
                self.insert_to_tree(index, buffer_pointer, node.right_child, current_node_end)

    def get_subtree_len(self, node):
        if node is None:
            return 0
        return self.get_subtree_len(node.left_child) + node.length + self.get_subtree_len(node.right_child)

    def get_text(self):
        text = self.in_order(self.root)
        return text

    def in_order(self, node):
        if node is None:
            return ""
        text_l = self.in_order(node.left_child)
        text = self.read_from_buffer(node)
        text_r = self.in_order(node.right_child)
        return text_l + text + text_r

    def read_from_buffer(self, node):
        match node.buffer_type:
            case BufferType.ORIGINAL:
                print(f"read {self.original_text[node.start_pointer:node.start_pointer+node.length]} from original buffer")
                return self.original_text[node.start_pointer:node.start_pointer+node.length]
            case BufferType.ADDED:
                return self.added_text[node.start_pointer:node.start_pointer+node.length]
            case _:
                return ""