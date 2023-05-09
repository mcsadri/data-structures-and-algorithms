class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    # solution in part adapted from Class 15 warm-up & code review
    def pre_order(self, root=None, arr=None):
        if root is None and arr is None:
            root = self.root
            arr = []
        if root:
            arr.append(root.value)
            self.pre_order(root.left, arr)
            self.pre_order(root.right, arr)
        return arr

    def in_order(self, root=None, arr=None):
        if root is None and arr is None:
            root = self.root
            arr = []
        if root:
            self.in_order(root.left, arr)
            arr.append(root.value)
            self.in_order(root.right, arr)
        return arr

    def post_order(self, root=None, arr=None):
        if root is None and arr is None:
            root = self.root
            arr = []
        if root:
            self.post_order(root.left, arr)
            self.post_order(root.right, arr)
            arr.append(root.value)
        return arr


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)
