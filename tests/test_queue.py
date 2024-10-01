import unittest
from structures.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        """Set up a queue instance before each test."""
        self.queue = Queue()

    def test_enqueue(self):
        """Test enqueuing elements into the queue."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(self.queue.get_size(), 2)

    def test_dequeue(self):
        """Test dequeuing elements from the queue."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        dequeued_value = self.queue.dequeue()
        self.assertEqual(dequeued_value, 10)
        self.assertEqual(self.queue.peek(), 20)
        self.assertEqual(self.queue.get_size(), 1)

    def test_dequeue_empty_queue(self):
        """Test dequeuing from an empty queue."""
        dequeued_value = self.queue.dequeue()
        self.assertIsNone(dequeued_value)
        self.assertEqual(self.queue.get_size(), 0)

    def test_peek(self):
        """Test peeking the front element without dequeuing."""
        self.queue.enqueue(30)
        self.assertEqual(self.queue.peek(), 30)
        self.assertEqual(self.queue.get_size(), 1)

    def test_peek_empty_queue(self):
        """Test peeking the front element of an empty queue."""
        peek_value = self.queue.peek()
        self.assertIsNone(peek_value)

    def test_is_empty(self):
        """Test checking if the queue is empty."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())

    def test_enqueue_dequeue_sequence(self):
        """Test a sequence of enqueue and dequeue operations."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.get_size(), 3)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.get_size(), 1)

    # def test_display_queue(self):
    #     """Test displaying the queue elements."""
    #     self.queue.enqueue(10)
    #     self.queue.enqueue(20)
    #     self.queue.enqueue(30)
    #     with self.assertLogs() as captured:
    #         self.queue.display()
    #     self.assertIn("10 -> 20 -> 30 -> None", captured.output[0])

    def test_queue_size(self):
        """Test that the size of the queue is updated correctly."""
        self.assertEqual(self.queue.get_size(), 0)
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.get_size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.get_size(), 1)

    def test_dequeue_until_empty(self):
        """Test dequeuing elements until the queue is empty."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.dequeue(), 30)
        self.assertIsNone(self.queue.dequeue())  # Queue should be empty now

if __name__ == '__main__':
    unittest.main()
