# A class for a single node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# This is my implementation of a stack using a "Linked List" data structure with a head marking the top of the stack
class Stack:
    def __init__(self):
        self.head = None


    # Checks if stack is empty
    def is_empty(self):
        return self.head == None


    # Push something onto the stack
    def push(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node


    # Pop the top element off the stack
    def pop(self):
        if self.is_empty():
            return None
        else:
            popping = self.head.data
            self.head = self.head.next
            return popping


    # Clears the stack by "popping" all the elements until it is empty
    def clear_stack(self):
        while not self.is_empty():
            self.pop()

    
    # Removes the element in the stack with the given co-ords by removing everything from the stack, 
    # holding it in a temporary stack and putting it back in the original one
    def remove_element(self, co_ords):
        temp = Stack()

        while self.head and self.head.data[0] != co_ords:
            temp.push(self.pop())

        if self.head:
            self.pop()

        while temp.is_empty() == False:
            self.push(temp.pop())
           

    # def print_stack(self):
    #     current = self.head
    #     while current:
    #         print(current.data)
    #         current = current.next