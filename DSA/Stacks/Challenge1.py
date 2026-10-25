"""Write a function reverse that gets an integer array as input (a) and 
returns the reversed array."""

#Creating stack from scratch without importing from stack module
class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()

    def is_empty(self):
        return len(self.elements) == 0


def reverse(a):
    s = Stack()

    for item in a:
        s.push(item)

    reversed_array = []

    while not s.is_empty():
        reversed_array.append(s.pop())

    return reversed_array


print(reverse([1, 2, 3, 4, 5]))