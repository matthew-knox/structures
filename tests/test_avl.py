import unittest
from structures.avl import AVLTree

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        """Set up an AVL tree instance for testing."""
        self.avl = AVLTree()
        self.root = None

    def test_insert_balanced(self):
        """Test inserting elements in such a way that the tree remains balanced."""
        values = [30, 20, 40, 10, 25, 35, 50]
        for value in values:
            self.root = self.avl.insert(self.root, value)
        # Check if the root is balanced
        self.assertEqual(self.avl.get_balance(self.root), 0)
        # Check if the height is as expected
        self.assertEqual(self.avl.get_height(self.root), 3)

    def test_left_left_rotation(self):
        """Test if left-left rotation is performed correctly."""
        # Inserting values in such a way that a left-left rotation occurs
        self.root = self.avl.insert(self.root, 30)
        self.root = self.avl.insert(self.root, 20)
        self.root = self.avl.insert(self.root, 10)
        # The tree should rebalance with 20 as the new root
        self.assertEqual(self.root.value, 20)
        self.assertEqual(self.root.left.value, 10)
        self.assertEqual(self.root.right.value, 30)

    def test_right_right_rotation(self):
        """Test if right-right rotation is performed correctly."""
        # Inserting values in such a way that a right-right rotation occurs
        self.root = self.avl.insert(self.root, 10)
        self.root = self.avl.insert(self.root, 20)
        self.root = self.avl.insert(self.root, 30)
        # The tree should rebalance with 20 as the new root
        self.assertEqual(self.root.value, 20)
        self.assertEqual(self.root.left.value, 10)
        self.assertEqual(self.root.right.value, 30)

    def test_left_right_rotation(self):
        """Test if left-right rotation is performed correctly."""
        # Inserting values to trigger a left-right rotation
        self.root = self.avl.insert(self.root, 30)
        self.root = self.avl.insert(self.root, 10)
        self.root = self.avl.insert(self.root, 20)
        # The tree should rebalance with 20 as the new root
        self.assertEqual(self.root.value, 20)
        self.assertEqual(self.root.left.value, 10)
        self.assertEqual(self.root.right.value, 30)

    def test_right_left_rotation(self):
        """Test if right-left rotation is performed correctly."""
        # Inserting values to trigger a right-left rotation
        self.root = self.avl.insert(self.root, 10)
        self.root = self.avl.insert(self.root, 30)
        self.root = self.avl.insert(self.root, 20)
        # The tree should rebalance with 20 as the new root
        self.assertEqual(self.root.value, 20)
        self.assertEqual(self.root.left.value, 10)
        self.assertEqual(self.root.right.value, 30)

    def test_inorder_traversal(self):
        """Test the in-order traversal of the AVL tree."""
        values = [40, 20, 10, 30, 60, 50, 70]
        for value in values:
            self.root = self.avl.insert(self.root, value)
        # The in-order traversal should return the values in sorted order
        expected_inorder = [10, 20, 30, 40, 50, 60, 70]
        self.assertEqual(self.avl.inorder_traversal(self.root), expected_inorder)

    def test_delete_leaf_node(self):
        """Test deleting a leaf node and check if the AVL tree rebalances correctly."""
        values = [40, 20, 60, 10, 30, 50, 70]
        for value in values:
            self.root = self.avl.insert(self.root, value)
        # Deleting a leaf node (10)
        self.root = self.avl.delete(self.root, 10)
        self.assertEqual(self.avl.inorder_traversal(self.root), [20, 30, 40, 50, 60, 70])
        # The root should still be balanced
        self.assertEqual(self.avl.get_balance(self.root), 0)

    def test_delete_node_with_one_child(self):
        """Test deleting a node with one child and check if the AVL tree rebalances correctly."""
        values = [40, 20, 60, 10, 50, 70]
        for value in values:
            self.root = self.avl.insert(self.root, value)
        # Deleting a node with one child (50)
        self.root = self.avl.delete(self.root, 50)
        self.assertEqual(self.avl.inorder_traversal(self.root), [10, 20, 40, 60, 70])
        # Check balance of the root
        self.assertEqual(self.avl.get_balance(self.root), 0)

    def test_delete_node_with_two_children(self):
        """Test deleting a node with two children and check if the AVL tree rebalances correctly."""
        values = [40, 20, 60, 10, 30, 50, 70]
        for value in values:
            self.root = self.avl.insert(self.root, value)
        # Deleting a node with two children (20)
        self.root = self.avl.delete(self.root, 20)
        self.assertEqual(self.avl.inorder_traversal(self.root), [10, 30, 40, 50, 60, 70])
        # The root should be balanced after deletion
        self.assertEqual(self.avl.get_balance(self.root), 0)

    def test_delete_root(self):
        """Test deleting the root of the AVL tree and check if the tree rebalances correctly."""
        values = [40, 20, 60, 10, 30, 50, 70]
        for value in values:
            self.root = self.avl.insert(self.root, value)
        # Deleting the root node (40)
        self.root = self.avl.delete(self.root, 40)
        # The new root should be balanced
        self.assertEqual(self.avl.get_balance(self.root), 0)
        # In-order traversal should still return the correct sorted order
        self.assertEqual(self.avl.inorder_traversal(self.root), [10, 20, 30, 50, 60, 70])


if __name__ == '__main__':
    unittest.main()
