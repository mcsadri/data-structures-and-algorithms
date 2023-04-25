from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    a queue data structure class using a linked list as its underlying data storage mechanism
    solution written with assistance from ChatGPT
    """
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError(Exception("Method not allowed on empty collection"))

        node_to_remove = self.front

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

        self.size -= 1
        return node_to_remove.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError(Exception("Method not allowed on empty collection"))

        return self.front.value

    def is_empty(self):
        return self.front is None


class Node:
    """
    a Node class that has properties for the value stored in the Node, and a pointer to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
