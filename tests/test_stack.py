import unittest
from structures.stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        """Set up a stack instance before each test."""
        self.stack = Stack()

    def test_push(self):
        """Test pushing elements onto the stack."""
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)
        self.assertEqual(self.stack.get_size(), 2)

    def test_pop(self):
        """Test popping elements from the stack."""
        self.stack.push(10)
        self.stack.push(20)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 20)
        self.assertEqual(self.stack.peek(), 10)
        self.assertEqual(self.stack.get_size(), 1)

    def test_pop_empty_stack(self):
        """Test popping from an empty stack."""
        popped_value = self.stack.pop()
        self.assertIsNone(popped_value)
        self.assertEqual(self.stack.get_size(), 0)

    def test_peek(self):
        """Test peeking the top element without popping."""
        self.stack.push(30)
        self.assertEqual(self.stack.peek(), 30)
        self.assertEqual(self.stack.get_size(), 1)

    def test_peek_empty_stack(self):
        """Test peeking the top element of an empty stack."""
        peek_value = self.stack.peek()
        self.assertIsNone(peek_value)

    def test_is_empty(self):
        """Test checking if the stack is empty."""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())

    def test_push_pop_sequence(self):
        """Test a sequence of push and pop operations."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.get_size(), 3)
        self.assertEqual(self.stack.pop(), 30)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.get_size(), 1)

    # def test_display_stack(self):
    #     """Test displaying the stack elements."""
    #     self.stack.push(10)
    #     self.stack.push(20)
    #     self.stack.push(30)
    #     with self.assertLogs() as captured:
    #         self.stack.display()
    #     self.assertIn("30 -> 20 -> 10 -> None", captured.output[0])

    def test_stack_size(self):
        """Test that the size of the stack is updated correctly."""
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.get_size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.get_size(), 1)

    def test_pop_until_empty(self):
        """Test popping elements until the stack is empty."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.pop(), 30)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)
        self.assertIsNone(self.stack.pop())  # Stack should be empty now

if __name__ == '__main__':
    unittest.main()
