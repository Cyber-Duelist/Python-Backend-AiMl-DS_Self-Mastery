""" The stack project is a simple implementation of a stack data structure using a list. 
It allows you to add elements to the top of the stack,
 remove elements from the top of the stack, and check if the stack is empty."""

class Stack :
    def __init__(self) : 
        self.elements = []

#Adding a push method to stack to push elements inside it
    def push(self,element):
        self.elements.append(element)

#Adding a top method to stack to be aware about the top most element without removing it.
    def top(self) :
        return self.elements[-1]

#Adding a pop method to stack to remove the top most integer on the stack
    def pop(self) :
        return self.elements.pop()

#Adding a size method to get the size of the stack
    def size(self) :
        return len(self.elements)

#Adding an empty method to stack that gets no arguments and return true if the stack is empty
    def empty(self) :
        return len(self.elements) == 0

