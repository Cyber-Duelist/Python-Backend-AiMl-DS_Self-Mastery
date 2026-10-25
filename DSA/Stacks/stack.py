class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()

    def top(self):
        if not self.is_empty():
            return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0


# This is the stack module that we can use in different codes for stack operations