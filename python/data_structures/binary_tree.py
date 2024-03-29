class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    # solution in part adapted from Class 15 warm-up & code review
    # def pre_order(self, root=None, arr=None):
    #     if root is None and arr is None:
    #         root = self.root
    #         arr = []
    #     if root:
    #         arr.append(root.value)
    #         self.pre_order(root.left, arr)
    #         self.pre_order(root.right, arr)
    #     return arr

    # alt solution using helper functions via class demo
    def pre_order(self):
        traversal = []

        def walk(root):
            if root:
                # root value operation
                traversal.append(root.value)
                # left
                walk(root.left)
                # right
                walk(root.right)

        # invoke the helper
        walk(self.root)

        return traversal

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

    # debugged helper function solution with assistance from ChatGPT
    def find_maximum_value(self):
        maximum = None

        def walk(root, max_val):
            nonlocal maximum
            if root:
                if max_val is None:
                    maximum = root.value
                elif root.value > max_val:
                    maximum = root.value
                walk(root.left, maximum)
                walk(root.right, maximum)

        walk(self.root, maximum)
        return maximum


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)
