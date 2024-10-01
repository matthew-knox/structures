# tests/test_bst.py

import unittest
from structures.bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """Set up a BinarySearchTree instance for testing."""
        self.bst = BinarySearchTree()

    def test_insert(self):
        """Test insertion of new values."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertEqual(self.bst.inorder_traversal(), [30, 50, 70])

    def test_search_existing_value(self):
        """Test searching for an existing value in the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertTrue(self.bst.search(30))
        self.assertTrue(self.bst.search(70))
        self.assertTrue(self.bst.search(50))

    def test_search_non_existing_value(self):
        """Test searching for a non-existing value in the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertFalse(self.bst.search(90))
        self.assertFalse(self.bst.search(10))

    def test_inorder_traversal(self):
        """Test in-order traversal returns values in sorted order."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(60)
        self.bst.insert(80)
        self.assertEqual(self.bst.inorder_traversal(), [20, 30, 50, 60, 70, 80])

    def test_preorder_traversal(self):
        """Test pre-order traversal of the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(60)
        self.bst.insert(80)
        self.assertEqual(self.bst.preorder_traversal(), [50, 30, 20, 70, 60, 80])

    def test_postorder_traversal(self):
        """Test post-order traversal of the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(60)
        self.bst.insert(80)
        self.assertEqual(self.bst.postorder_traversal(), [20, 30, 60, 80, 70, 50])

    def test_delete_leaf_node(self):
        """Test deletion of a leaf node from the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.delete(30)  # 30 is a leaf node
        self.assertFalse(self.bst.search(30))
        self.assertEqual(self.bst.inorder_traversal(), [50, 70])

    def test_delete_node_with_one_child(self):
        """Test deletion of a node with one child."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)  # 30 has one child (20)
        self.bst.delete(30)
        self.assertFalse(self.bst.search(30))
        self.assertEqual(self.bst.inorder_traversal(), [20, 50])

    def test_delete_node_with_two_children(self):
        """Test deletion of a node with two children."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)  # 30 has two children (20 and 40)
        self.bst.delete(30)
        self.assertFalse(self.bst.search(30))
        self.assertEqual(self.bst.inorder_traversal(), [20, 40, 50, 70])

    def test_find_min(self):
        """Test finding the minimum value in the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.assertEqual(self.bst.find_min(), 20)

    def test_find_max(self):
        """Test finding the maximum value in the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(80)
        self.assertEqual(self.bst.find_max(), 80)

    def test_tree_height(self):
        """Test calculating the height of the tree."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(60)
        self.bst.insert(80)
        self.assertEqual(self.bst.height(), 2)

    def test_empty_tree(self):
        """Test that an empty tree behaves correctly."""
        self.assertEqual(self.bst.inorder_traversal(), [])
        self.assertEqual(self.bst.preorder_traversal(), [])
        self.assertEqual(self.bst.postorder_traversal(), [])
        with self.assertRaises(ValueError):
            self.bst.find_min()
        with self.assertRaises(ValueError):
            self.bst.find_max()
        self.assertEqual(self.bst.height(), -1)


if __name__ == '__main__':
    unittest.main()
