import math

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

        self.root = Node(buffer_type=BufferType.ORIGINAL, start_index=0, length=len(self.original_text))

    def insert_char(self, index, char):
        if char == '\r':
            char = '\n'
        self.added_text += char

        buffer_start_index = len(self.added_text) - 1
        self.insert_to_tree(self.root, index, buffer_start_index)

    def insert_to_tree(self, node, global_index, buffer_start_index, offset = 0):
        if node is None:
            return

        left_subtree_len = self.get_subtree_len(node.left_child)
        current_node_start = offset + left_subtree_len
        current_node_end = current_node_start + node.length

        #go left
        if global_index <= current_node_start:
            if node.left_child is None:
                node.left_child = Node(buffer_type=BufferType.ADDED, start_index=buffer_start_index, length=1)
            else:
                self.insert_to_tree(node.left_child, global_index, buffer_start_index, offset)

        #split
        if current_node_start < global_index < current_node_end:
            left_length = global_index - current_node_start
            right_length = node.length - left_length

            left_family = node.left_child
            right_family = node.right_child

            node.left_child = Node(buffer_type=node.buffer_type, start_index=node.start_index, length=left_length)
            node.left_child.left_child = left_family

            node.right_child = Node(buffer_type=node.buffer_type, start_index=node.start_index + left_length, length=right_length)
            node.right_child.right_child = right_family

            node.start_index = buffer_start_index
            node.buffer_type = BufferType.ADDED
            node.length = 1

        #go right
        if global_index >= current_node_end:
            #merge
            if node.buffer_type == BufferType.ADDED and global_index == current_node_end and buffer_start_index == node.start_index + node.length:
                node.length += 1
                return
            if node.right_child is None:
                node.right_child = Node(buffer_type=BufferType.ADDED, start_index=buffer_start_index, length=1)
            else:
                self.insert_to_tree(node.right_child, global_index, buffer_start_index, current_node_end)

    # PARAMETERS
    def get_subtree_len(self, node):
        if node is None:
            return 0
        return self.get_subtree_len(node.left_child) + node.length + self.get_subtree_len(node.right_child)

    def get_spread(self, node):
        return max(self.get_max_spread_left(node), self.get_max_spread_right(node))

    def get_max_spread_left(self, node):
        if node is None:
            return 0
        return self.get_max_spread_left(node.left_child) + 1

    def get_max_spread_right(self, node):
        if node is None:
            return 0
        return self.get_max_spread_right(node.right_child) + 1

    # TRAVERSING
    def get_text(self):
        gen = self.in_order_gen(self.root)
        text = ""
        for n in gen:
            text += self.read_from_buffer(n[0])
        return text

    def in_order_gen(self, node, offset = 0, depth = 1):
        if node is None:
            return None
        yield from self.in_order_gen(node.left_child, offset - 1/(2**depth), depth + 1)
        yield node, offset, depth
        yield from self.in_order_gen(node.right_child, offset + 1/(2**depth), depth + 1)
        return None

    # READING BUFFER
    def read_from_buffer(self, node):
        match node.buffer_type:
            case BufferType.ORIGINAL:
                return self.original_text[node.start_index:node.start_index + node.length]
            case BufferType.ADDED:
                return self.added_text[node.start_index:node.start_index + node.length]
            case _:
                return ""