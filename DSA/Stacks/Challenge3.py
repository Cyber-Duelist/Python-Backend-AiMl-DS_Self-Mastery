"""Write a function isBalancedParentheses that gets a string of parentheses, brackets, and braces and returns true if the string is balanced, otherwise false.

That is, every opening symbol must have a corresponding closing symbol."""
from stack import Stack


def isBalancedParentheses(text):
    stack = Stack()

    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:
        if char in mapping.values():
            stack.push(char)

        elif char in mapping:
            if stack.is_empty() or stack.top() != mapping[char]:
                return False

            stack.pop()

    return stack.is_empty()


print(isBalancedParentheses("{[]}"))