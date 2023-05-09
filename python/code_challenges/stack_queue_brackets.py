# from data_structures.queue import Queue
from collections import deque


def multi_bracket_validation(input_str):
    # Solution with assistance from ChatGPT and https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
    # Create a deque to store opening parentheses, square brackets, and curly braces
    stack = deque()

    # Define opening and closing characters
    opening = ['(', '[', '{']
    closing = [')', ']', '}']

    # Iterate over the input string
    for char in input_str:
        # If the character is an opening character, add it to the stack
        if char in opening:
            stack.append(char)
        # If the character is a closing character, check if it matches the most recent opening character
        elif char in closing:
            # If the stack is empty, there are no opening characters to match
            if len(stack) == 0:
                return False
            # Check if the most recent opening character matches the current closing character
            elif opening.index(stack[-1]) == closing.index(char):
                stack.pop()
            # If the most recent opening character does not match the current closing character, the string is not balanced
            else:
                return False

    # If the stack is not empty, there are unclosed opening characters and the string is not balanced
    if len(stack) != 0:
        return False

    # If the function has not returned False, the string is balanced
    return True
