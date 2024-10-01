import unittest
from structures.sll import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up a singly linked list instance before each test."""
        self.sll = SinglyLinkedList()

    def test_append(self):
        """Test appending elements to the linked list."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        self.assertEqual(self.sll.length(), 3)
        self.assertEqual(self.sll.find_middle(), 20)  # Middle element should be 20

    def test_prepend(self):
        """Test prepending elements to the linked list."""
        self.sll.prepend(30)
        self.sll.prepend(20)
        self.sll.prepend(10)
        self.assertEqual(self.sll.length(), 3)
        self.assertEqual(self.sll.find_middle(), 20)  # Middle element should be 20

    def test_insert_after(self):
        """Test inserting an element after a specific node."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        self.sll.insert_after(20, 25)
        self.assertTrue(self.sll.search(25))
        self.assertEqual(self.sll.length(), 4)
        self.assertEqual(self.sll.find_middle(), 25)  # Middle element should be 25

    def test_delete(self):
        """Test deleting an element from the linked list."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        self.sll.delete(20)  # Deleting the middle element
        self.assertFalse(self.sll.search(20))
        self.assertEqual(self.sll.length(), 2)
        self.assertEqual(self.sll.find_middle(), 30)  # Middle element should be 30

    def test_delete_non_existent(self):
        """Test deleting a non-existent element."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.delete(100)  # Try deleting a value that doesn't exist
        self.assertEqual(self.sll.length(), 2)  # Length should remain unchanged
        self.assertTrue(self.sll.search(10))
        self.assertTrue(self.sll.search(20))

    def test_search(self):
        """Test searching for elements in the list."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        self.assertTrue(self.sll.search(20))
        self.assertFalse(self.sll.search(40))  # 40 is not

    def test_reverse(self):
        """Test reversing the linked list."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        self.sll.reverse()  # Reverse the list
        self.assertEqual(self.sll.length(), 3)
        # Check if the reverse is correct by displaying and manually comparing
        current = self.sll.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [30, 20, 10])

    def test_find_middle(self):
        """Test finding the middle element of the list."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        self.sll.append(40)
        self.sll.append(50)
        self.assertEqual(self.sll.find_middle(), 30)  # Middle element should be 30
        self.sll.append(60)
        self.assertEqual(self.sll.find_middle(), 40)  # Middle should now be 40 with 6 elements

    def test_empty_list(self):
        """Test the behavior of an empty linked list."""
        self.assertTrue(self.sll.is_empty())
        self.assertEqual(self.sll.length(), 0)
        self.assertEqual(self.sll.find_middle(), None)  # Middle of an empty list is None
        self.sll.reverse()  # Reversing an empty list should not cause issues
        self.sll.delete(10)  # Deleting from an empty list should not cause issues

    # def test_display(self):
    #     """Test displaying the linked list."""
    #     self.sll.append(10)
    #     self.sll.append(20)
    #     self.sll.append(30)
    #     with self.assertLogs() as captured_logs:
    #         self.sll.display()  # Check that it outputs the list correctly
    #     output = captured_logs.output[0].strip()
    #     self.assertIn("10 -> 20 -> 30 -> None", output)

    def test_length(self):
        """Test calculating the length of the linked list."""
        self.assertEqual(self.sll.length(), 0)  # Empty list
        self.sll.append(10)
        self.sll.append(20)
        self.assertEqual(self.sll.length(), 2)


if __name__ == '__main__':
    unittest.main()