# node.py

class Node:
    """
    A class representing a node in the binary search tree.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    left : Node
        Reference to the left child node.
    right : Node
        Reference to the right child node.
    """

    def __init__(self, value):
        self.value = value
        self.left = None    # for BST
        self.right = None   # for BST
        self.next = None    # for SLL
        self.prev = None    # for DLL
        self.height = 1     # for AVL
