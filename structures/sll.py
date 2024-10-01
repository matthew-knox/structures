# sll.py

from .node import Node

class SinglyLinkedList:
    """
    A class that implements a singly linked list using the Node class.

    Methods:
    --------
    append(value):
        Appends a new node with the given value at the end of the list.
    prepend(value):
        Inserts a new node with the given value at the beginning of the list.
    delete(value):
        Deletes the first occurrence of the node with the given value.
    search(value) -> bool:
        Searches for a node with the given value. Returns True if found.
    display():
        Displays the entire list.
    length() -> int:
        Returns the length of the linked list.
    reverse():
        Reverses the linked list.
    find_middle() -> Node:
        Finds the middle node of the linked list.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def append(self, value):
        """Append a new node with the given value to the end of the list."""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node

    def prepend(self, value):
        """Insert a new node with the given value at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node

    def delete(self, value):
        """Delete the first occurrence of the node with the given value."""
        if self.is_empty():
            print("List is empty. Nothing to delete.")
            return

        # If the value is at the head
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        # If the value was found
        if current.next:
            current.next = current.next.next
        else:
            print(f"Value {value} not found in the list.")

    def search(self, value) -> bool:
        """Search for a node with the given value. Return True if found, False otherwise."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        """Print the values in the linked list."""
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def length(self) -> int:
        """Return the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        """Reverse the linked list in place."""
        previous = None
        current = self.head

        while current:
            next_node = current.next  # Store the next node
            current.next = previous   # Reverse the link
            previous = current        # Move `previous` to this node
            current = next_node       # Move `current` to the next node

        self.head = previous  # Reset the head to the new front (previous tail)

    def find_middle(self):
        """
        Find the middle element in the linked list.
        Uses the two-pointer technique (slow and fast pointers).
        """
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next      # Move `slow` by one node
            fast = fast.next.next # Move `fast` by two nodes

        if slow:
            return slow.value
        return None

    def insert_after(self, prev_value, new_value):
        """Insert a new node with the given value after the node with `prev_value`."""
        current = self.head
        while current:
            if current.value == prev_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Value {prev_value} not found in the list.")
