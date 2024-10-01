from .node import Node

class AVLTree:
    def insert(self, root, value):
        # Normal BST insertion
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor
        balance = self.get_balance(root)

        # Perform rotations to balance the tree if needed

        # Left Left Case
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        # Step 1: Perform standard BST delete
        if not root:
            return root

        # If the value to be deleted is smaller than the root's value, go to the left subtree
        if value < root.value:
            root.left = self.delete(root.left, value)

        # If the value to be deleted is greater than the root's value, go to the right subtree
        elif value > root.value:
            root.right = self.delete(root.right, value)

        # If value is equal to root's value, this is the node to be deleted
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.get_min_value_node(root.right)
            root.value = temp.value

            # Delete the inorder successor
            root.right = self.delete(root.right, temp.value)

        # Step 2: Update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get the balance factor
        balance = self.get_balance(root)

        # Step 4: Perform rotations if necessary

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.value)
            result = result + self.inorder_traversal(root.right)
        return result