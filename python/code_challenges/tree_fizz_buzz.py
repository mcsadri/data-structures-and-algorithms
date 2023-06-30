# from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


# attempted solution with assistance via ChatGPT
def fizz_buzz_tree(tree):
    def fizz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    # def generate_tree(node):
    #     value = node.value
    #     fizz_buzz_value = fizz_buzz(value)
    #     node.value = fizz_buzz_value
    #
    #     for i in range(tree.k):
    #         child_value = value * tree.k + i + 1
    #         child_node = tree.Node(child_value)
    #         node.add_child(child_node)
    #
    #     for child in node.children:
    #         generate_tree(child)
    #
    # root = tree.root
    # generate_tree(root)
    #
    # return tree



