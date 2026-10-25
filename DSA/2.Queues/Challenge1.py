"""Write a function reverse that gets an integer array as input (a) and returns the reversed array."""

from queue import Queue

def reverse(a):
    q =Queue()

#1.Enqueuing elements from 'a' in reverse order
    for i in range(len(a) - 1, -1, -1) :
        q.enqueue(a[i])
    reversed_list = []

#2.Extract items using front() and dequeue()
    while q.size() > 0:
        #Getting the value before it gets deleted
        item = q.front()
        reversed_list.append(item)
        #Now remove it from the queue
        q.dequeue()
    return reversed_list    
print(reverse([1,2,3,4,5]))
print(reverse([1,2,4,5,5,6]))