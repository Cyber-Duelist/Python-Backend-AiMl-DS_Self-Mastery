"""Write a function nse that gets an integer array and 
returns an array that contains the nearest smaller element of each element (to the left). 
If there is no smaller element to the left of an element, return -1."""

# using the stack module
from stack import Stack

def nse(a):
    s = Stack()
    result = []

    for x in a:

        while not s.is_empty() and s.top() >= x:
            s.pop()

        if s.is_empty():
            result.append(-1)
        else:
            result.append(s.top())

        s.push(x)

    return result


print(nse([4, 5, 2, 10, 8]))
                                         