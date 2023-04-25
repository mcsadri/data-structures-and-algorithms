from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    a stack data structure class using a linked list as its underlying data storage mechanism
    solution written with assistance from ChatGPT
    """
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        a Stack class method to add a new node with that value to the top of the stack with an O(1) Time performance.
        :param value: the value to be added to the top of the stack
        :return: none
        """
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        """
        a Stack class method to remove the node from the top of the stack
        :return: the value from node from the top of the stack, or an exception when called on an empty stack
        """
        if self.top is None:
            raise InvalidOperationError(Exception("Method not allowed on empty collection"))
        else:
            popped_node = self.top
            self.top = popped_node.next
            popped_node.nest = None
            return popped_node.value

    def peek(self):
        """
        a Stack class method to return the value of the node located at the top of the stack
        :return: the value of the node located at the top of the stack, or an exeption when called on an empty stack
        """
        if self.top is None:
            raise InvalidOperationError(Exception("Method not allowed on empty collection"))
        else:
            return self.top.value

    def is_empty(self):
        """
        a Stack class method to return a Boolena indicating whether or not the stack is empty
        :return: a Boolean indicating whether or not the stack is empty
        """
        return self.top is None


class Node:
    """
    a Node class that has properties for the value stored in the Node, and a pointer to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
