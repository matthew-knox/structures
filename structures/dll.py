# dll.py

from .node import Node

class DoublyLinkedList:
    """
    A class that implements a doubly linked list using the Node class.

    Methods:
    --------
    append(value):
        Appends a new node with the given value to the end of the list.
    prepend(value):
        Inserts a new node with the given value at the beginning of the list.
    delete(value):
        Deletes the first occurrence of the node with the given value.
    search(value) -> bool:
        Searches for a node with the given value. Returns True if found.
    display_forward():
        Displays the list in forward order.
    display_backward():
        Displays the list in reverse order.
    length() -> int:
        Returns the length of the doubly linked list.
    """

    def __init__(self):
        self.head = None  # The head node of the list
        self.tail = None  # The tail node of the list

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def append(self, value):
        """Append a new node with the given value to the end of the list."""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Set the current tail's next to new node
            new_node.prev = self.tail  # Set new node's previous to current tail
            self.tail = new_node       # Update tail to the new node

    def prepend(self, value):
        """Insert a new node with the given value at the beginning of the list."""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Set new node's next to current head
            self.head.prev = new_node  # Set current head's previous to new node
            self.head = new_node       # Update head to the new node

    def delete(self, value):
        """Delete the first occurrence of the node with the given value."""
        if self.is_empty():
            print("List is empty. Nothing to delete.")
            return

        current = self.head

        # Traverse the list to find the node to delete
        while current and current.value != value:
            current = current.next

        if current is None:
            print(f"Value {value} not found in the list.")
            return

        # If the node to be deleted is the head
        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # If the list is now empty
        elif current == self.tail:
            self.tail = current.prev
            if self.tail:
                self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def search(self, value) -> bool:
        """Search for a node with the given value. Return True if found, False otherwise."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display_forward(self):
        """Display the values in the linked list from head to tail."""
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        """Display the values in the linked list from tail to head."""
        if self.is_empty():
            print("List is empty.")
            return

        current = self.tail
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

    def length(self) -> int:
        """Return the length of the doubly linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
