class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def push(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popping = self.head.data
            self.head = self.head.next
            return popping

    def clear_stack(self):
        while not self.is_empty():
            self.pop()