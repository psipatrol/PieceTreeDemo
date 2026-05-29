class Node:
    def __init__(self, buffer_type, start_index, length):
        self.buffer_type = buffer_type
        self.start_index = start_index
        self.length = length
        self.left_child = None
        self.right_child = None