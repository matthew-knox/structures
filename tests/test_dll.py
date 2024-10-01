import unittest
from structures.dll import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up a doubly linked list instance before each test."""
        self.dll = DoublyLinkedList()

    def test_append(self):
        """Test appending elements to the doubly linked list."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        self.assertEqual(self.dll.length(), 3)
        # Check if values are correct by traversing forward
        self.assertEqual(self.traverse_forward(), [10, 20, 30])

    def test_prepend(self):
        """Test prepending elements to the doubly linked list."""
        self.dll.prepend(30)
        self.dll.prepend(20)
        self.dll.prepend(10)
        self.assertEqual(self.dll.length(), 3)
        # Check if values are correct by traversing forward
        self.assertEqual(self.traverse_forward(), [10, 20, 30])

    def test_insert_combination(self):
        """Test a combination of prepend and append."""
        self.dll.prepend(30)
        self.dll.prepend(20)
        self.dll.append(40)
        self.dll.append(50)
        self.assertEqual(self.dll.length(), 4)
        # Expected order: 20 -> 30 -> 40 -> 50
        self.assertEqual(self.traverse_forward(), [20, 30, 40, 50])

    def test_delete_head(self):
        """Test deleting the head of the doubly linked list."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        self.dll.delete(10)  # Delete head node
        self.assertEqual(self.dll.length(), 2)
        # Check the order after deletion
        self.assertEqual(self.traverse_forward(), [20, 30])

    def test_delete_tail(self):
        """Test deleting the tail of the doubly linked list."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        self.dll.delete(30)  # Delete tail node
        self.assertEqual(self.dll.length(), 2)
        # Check the order after deletion
        self.assertEqual(self.traverse_forward(), [10, 20])

    def test_delete_middle(self):
        """Test deleting a middle element from the list."""
