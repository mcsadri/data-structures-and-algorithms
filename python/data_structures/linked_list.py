class LinkedList:
    """
    code solution via class code review
    A class representing a linked list data structure.
    methods:
      * __init__(head=None): upon instantiation, an empty Linked List is created
      * insert(value): adds a new node with that value to the head of the list with an O(1) Time performance
      * includes(value): indicates whether that value exists as a Node’s value somewhere within the list
      * __str__(): returns a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"
    returns: nothing
    """

    def __init__(self, head=None):
        """
        param: head=None
        return: none
        """
        # initialization here
        self.head = head


    def insert(self, value=""):
        """
        param: value to be added to the linked list
        return: nothing
        """
        old_head = self.head
        self.head = Node(value)
        self.head.next = old_head


    def insert_before(self, search_val, new_val):
        # solution with assistance from ChatGPT
        new_node = Node(new_val)
        try:
            if self.head is None:
                #return
                raise TargetError()

            if self.head.value == search_val:
                new_node.next = self.head
                self.head = new_node
                return

            current_node = self.head
            while current_node.next is not None:
                if current_node.next.value == search_val:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                current_node = current_node.next

            raise TargetError()

        except Exception as e:
            raise TargetError(e)


    def insert_after(self, search_val, new_val):
        # solution with assistance from ChatGPT
        new_node = Node(new_val)

        try:
            if self.head is None:
                # If the linked list is empty, there's nothing to insert after
                raise TargetError()

            current = self.head
            while current is not None:
                if current.value == search_val:
                    # Found a node with the matching value, insert the new node after it
                    new_node = Node(new_val)
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next

            raise TargetError()

        except Exception as e:
            raise TargetError(e)


    def append(self, value):
        # code taken from warm-up solution
        # Create a new node with the given value.
        new_node = Node(value)
        # If the list is empty, set the head to the new node.
        if self.head is None:
            self.head = new_node
        # Otherwise, iterate through the list until the last node is found, and set its next attribute to the new node.
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def kth_from_end(self, k):
        # solution with assistance from ChatGPT
        """
        param: k: an integer representing the index from the tail of the linked list
        return: the value of the node at the kth position from the tail of the linked list
        """
        if k < 0:
            raise TargetError

        # use two pointers to traverse the list
        fast = slow = self.head

        # move the fast pointer k steps ahead of the slow pointer
        for _ in range(k):
            if fast is None:
                raise TargetError
            fast = fast.next

        if fast is None:
            raise TargetError
        # move both pointers until the fast pointer reaches the end of the list
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        return slow.value


    #################################################################
    def zip_lists(self, a, b):
        # solution with assistance from ChatGPT
        """
        param: list_a: a linked list
        param: list_b: a linked list
        return: a new linked list where the two linked list arguments are zipped together into one linked list so that the nodes alternate between the two lists
        """
        # Initialize a new empty linked list
        zipped_list = LinkedList()

        # Initialize pointers to the heads of each list
        current_a = a.head
        current_b = b.head

        # While either list has nodes left to process
        while current_a is not None and current_b is not None:
            # If list a has a node left to process, append it to the zipped list
            if current_a is not None:
                zipped_list.append(current_a.value)
                current_a = current_a.next

            # If list b has a node left to process, append it to the zipped list
            if current_b is not None:
                zipped_list.append(current_b.value)
                current_b = current_b.next

        # Return the new zipped list
        return zipped_list
    ##################################################################


    def includes(self, value):
        """
        param: value to be checked
        return: True if the found, False if the found
        """
        # traverse my linked list
        current = self.head  # 1) initialize a variable named current, set to head
        while current:  # 2) start while loop, choose between current or current.next
            # 3) do a thing
            if current.value == value:
                return True
            current = current.next  # 4) move the pointer for current
        return False


    def __str__(self):
        """
        param: none
        return: all values in linked list as a string + "NULL"
        """
        #start with an empty string
        text= ""
        #traverse my linked list
        current = self.head     # 1) initialize a variable named current, set to head
        while current:  # 2) start while loop, choose between current or current.next
            # 3) do a thing
            text += f"{{ {current.value} }} -> "
            current = current.next  # 4) move the pointer for current
        return text + "NULL"


class Node:
    """
    object class template for a Node in a linked list
    param: value
    param: next=None
    return: nothing
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    pass
