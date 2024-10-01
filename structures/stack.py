from .node import Node

class Stack:
    """
    Stack implementation using a singly linked list.
    Follows Last-In, First-Out (LIFO) principle.
    """
    def __init__(self):
        self.top = None  # Reference to the top of the stack
        self.size = 0  # Track the size of the stack

    def push(self, value):
        """Push a new element onto the stack."""
        new_node = Node(value)
        new_node.next = self.top  # Point to the current top node
        self.top = new_node  # Update the top to the new node
        self.size += 1

    def pop(self):
        """Pop the top element off the stack."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        popped_value = self.top.value
        self.top = self.top.next  # Update the top to the next node
        self.size -= 1
        return popped_value

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.value

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def get_size(self):
        """Return the size of the stack."""
        return self.size

    def display(self):
        """Display the elements of the stack."""
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
