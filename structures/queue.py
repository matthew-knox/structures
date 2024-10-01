from .node import Node

class Queue:
    """
    Queue implementation using a singly linked list.
    Follows First-In, First-Out (FIFO) principle.
    """
    def __init__(self):
        self.front = None  # Reference to the front of the queue
        self.rear = None  # Reference to the rear of the queue
        self.size = 0  # Track the size of the queue

    def enqueue(self, value):
        """Enqueue a new element at the rear of the queue."""
        new_node = Node(value)
        if self.rear is None:  # If queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Point the current rear to the new node
            self.rear = new_node  # Update the rear to the new node
        self.size += 1

    def dequeue(self):
        """Dequeue the front element from the queue."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        dequeued_value = self.front.value
        self.front = self.front.next  # Update the front to the next node
        if self.front is None:  # If the queue becomes empty
            self.rear = None  # Reset the rear
        self.size -= 1
        return dequeued_value

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.value

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def get_size(self):
        """Return the size of the queue."""
        return self.size

    def display(self):
        """Display the elements of the queue."""
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
