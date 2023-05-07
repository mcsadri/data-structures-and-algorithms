class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self, node):
        results = []
        results.append(self.value)

        if node.left:
            self.pre_order(node.left)

        if node.right:
            self.pre_order(node.right)

    def some_method(self):
        # method body here
        pass

    def some_method(self):
        # method body here
        pass


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right







#
# class BinaryTree:
#     """
#     Put docstring here
#     """
#
#     def __init__(self):
#         # initialization here
#         pass
#
#     def some_method(self):
#         # method body here
#         pass
#
# class Node:
#     pass
