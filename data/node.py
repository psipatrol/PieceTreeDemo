class Node:
    def __init__(self, buffer_type, start_pointer, length):
        self.buffer_type = buffer_type
        self.start_pointer = start_pointer
        self.length = length
        self.left_child = None
        self.right_child = None