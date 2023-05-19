from data_structures.binary_tree import BinaryTree, Node


# solution with assistance from ChatGPT
class BinarySearchTree(BinaryTree):

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_helper(value, self.root)

    def _add_helper(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._add_helper(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._add_helper(value, current_node.right)

    def contains(self, value):
        return self._contains_helper(value, self.root)

    def _contains_helper(self, value, current_node):
        if current_node is None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self._contains_helper(value, current_node.left)
        else:
            return self._contains_helper(value, current_node.right)
