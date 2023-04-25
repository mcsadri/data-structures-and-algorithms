from data_structures.stack import Stack


class PseudoQueue:
    """
    solution written with assistance from ChatGPT
    """
    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def enqueue(self, value):
        # Inserts a value into the PseudoQueue, using a first-in, first-out approach.
        self.stack_a.push(value)

    def dequeue(self):
        # Extracts a value from the PseudoQueue, using a first-in, first-out approach.
        if self.stack_b.is_empty():
            while not self.stack_a.is_empty():
                self.stack_b.push(self.stack_a.pop())

        return self.stack_b.pop()
