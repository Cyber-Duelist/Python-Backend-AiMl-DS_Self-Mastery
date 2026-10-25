class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        if self.empty() :
            self.elements.append((element,element,element))
        else :
            current_min = min(element,self.elements[-1][1])
            current_max = max(element,self.elements[-1][2])
            self.elements.append((element, current_min,current_max))    

    def top(self):
        return self.elements[-1][0]

    def pop(self):
        return self.elements.pop()[0]

    def size(self):
        return len(self.elements)

    def empty(self):
        return len(self.elements) == 0
   
    def min(self) :
        if not self.empty() :
            return self.elements[-1][1]
        return None

    def max(self) :
        if not self.empty() :
            return self.elements[-1][2]
        return None    

# This is the stack module that we can use in different codes for stack operations