from .node import Node
class BinarySearchTree:
    """
    A class that implements a binary search tree (BST) with basic functionalities.

    Methods:
    --------
    insert(value):
        Inserts a value into the BST.
    search(value):
        Searches for a value in the BST.
    delete(value):
        Deletes a value from the BST.
    inorder_traversal():
        Returns an in-order traversal of the BST.
    preorder_traversal():
        Returns a pre-order traversal of the BST.
    postorder_traversal():
        Returns a post-order traversal of the BST.
    find_min():
        Returns the minimum value in the BST.
    find_max():
        Returns the maximum value in the BST.
    height():
        Returns the height of the BST.
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new node with the given value into the binary search tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def search(self, value) -> bool:
        """Search for a value in the BST. Returns True if found, False otherwise."""
        return self._search(self.root, value)

    def _search(self, current_node, value) -> bool:
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)

    def delete(self, value):
        """Delete a node with the given value from the BST."""
        self.root = self._delete(self.root, value)

    def _delete(self, current_node, value):
        if current_node is None:
            return current_node

        # Find the node to delete
        if value < current_node.value:
            current_node.left = self._delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete(current_node.right, value)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_val = self._min_value_node(current_node.right)
            current_node.value = min_val.value
            current_node.right = self._delete(current_node.right, min_val.value)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_min(self) -> int:
        """Return the minimum value in the BST."""
        if self.root is None:
            raise ValueError("The tree is empty")
        return self._find_min(self.root).value

    def _find_min(self, current_node):
        if current_node.left is None:
            return current_node
        return self._find_min(current_node.left)

    def find_max(self) -> int:
        """Return the maximum value in the BST."""
        if self.root is None:
            raise ValueError("The tree is empty")
        return self._find_max(self.root).value

    def _find_max(self, current_node):
        if current_node.right is None:
            return current_node
        return self._find_max(current_node.right)

    def inorder_traversal(self) -> list:
        """Return the values of the nodes in an in-order traversal."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current_node, result):
        if current_node:
            self._inorder(current_node.left, result)
            result.append(current_node.value)
            self._inorder(current_node.right, result)

    def preorder_traversal(self) -> list:
        """Return the values of the nodes in a pre-order traversal."""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, current_node, result):
        if current_node:
            result.append(current_node.value)
            self._preorder(current_node.left, result)
            self._preorder(current_node.right, result)

    def postorder_traversal(self) -> list:
        """Return the values of the nodes in a post-order traversal."""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, current_node, result):
        if current_node:
            self._postorder(current_node.left, result)
            self._postorder(current_node.right, result)
            result.append(current_node.value)

    def height(self) -> int:
        """Return the height of the BST."""
        return self._height(self.root)

    def _height(self, current_node) -> int:
        if current_node is None:
            return -1  # Empty tree has height -1
        left_height = self._height(current_node.left)
        right_height = self._height(current_node.right)
        return max(left_height, right_height) + 1
